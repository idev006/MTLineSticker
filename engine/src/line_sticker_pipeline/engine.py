from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Dict, Any
import json, hashlib

import cv2
import numpy as np
from PIL import Image


@dataclass
class EngineConfig:
    output_width: int = 370
    output_height: int = 320
    inner_border_crop: int = 8
    bg_tolerance: int = 42
    bg_softness: int = 18
    fit_margin: int = 10


class StickerEngine:
    """Deterministic static-sticker image engine for bordered contact sheets.

    Background removal is deliberately conservative: only background-colored
    pixels connected to a frame edge may become transparent. This prevents the
    destructive mottling seen when a global color threshold is applied to
    foreground textures that happen to resemble the background color.
    """

    def __init__(self, config: EngineConfig | None = None):
        self.config = config or EngineConfig()

    def process_folder(self, input_dir: str | Path, output_dir: str | Path,
                       patterns: Tuple[str, ...] = ('.png', '.jpg', '.jpeg')) -> Dict[str, Any]:
        input_dir = Path(input_dir)
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        sheets = sorted([p for p in input_dir.iterdir() if p.is_file() and p.suffix.lower() in patterns])
        report = {
            'input_dir': str(input_dir), 'output_dir': str(output_dir), 'sheets': [],
            'totals': {'sheets': 0, 'frames_detected': 0, 'stickers_exported': 0}
        }
        global_idx = 1
        for sheet in sheets:
            if sheet.name.startswith('._'):
                continue
            sheet_out = output_dir / sheet.stem
            sheet_out.mkdir(exist_ok=True)
            sheet_report = self.process_sheet(sheet, sheet_out, start_index=global_idx)
            report['sheets'].append(sheet_report)
            report['totals']['sheets'] += 1
            report['totals']['frames_detected'] += sheet_report['frames_detected']
            report['totals']['stickers_exported'] += sheet_report['stickers_exported']
            global_idx += sheet_report['stickers_exported']
        (output_dir / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
        return report

    def process_sheet(self, sheet_path: str | Path, output_dir: str | Path, start_index: int = 1) -> Dict[str, Any]:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        image = cv2.imread(str(sheet_path), cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError(f'cannot read image: {sheet_path}')
        rects = self.detect_frames(image)
        if not rects:
            raise ValueError(f'no sticker frames detected: {sheet_path}')

        items = []
        idx = start_index
        numbered_sheet = self._sheet_has_frame_numbers(image, rects)
        for order, (x, y, w, h) in enumerate(rects, start=1):
            crop = image[y:y+h, x:x+w].copy()
            rgba = self.extract_sticker_rgba(crop, remove_frame_number=numbered_sheet)
            fitted = self.fit_to_canvas(rgba, self.config.output_width, self.config.output_height, self.config.fit_margin)
            out_name = f'{idx:02d}.png'
            out_path = output_dir / out_name
            Image.fromarray(fitted, mode='RGBA').save(out_path, dpi=(72, 72), optimize=True)
            items.append({
                'index': idx, 'frame_order': order,
                'frame_rect': [int(x), int(y), int(w), int(h)],
                'output_file': out_name,
                'output_size': [self.config.output_width, self.config.output_height],
                'file_size_bytes': out_path.stat().st_size,
                'sha256': sha256_file(out_path),
            })
            idx += 1

        sheet_report = {
            'sheet': Path(sheet_path).name,
            'sheet_size': list(Image.open(sheet_path).size),
            'frames_detected': len(rects), 'stickers_exported': len(items), 'stickers': items,
        }
        (output_dir / 'sheet_report.json').write_text(json.dumps(sheet_report, ensure_ascii=False, indent=2), encoding='utf-8')
        return sheet_report

    def detect_frames(self, image: np.ndarray) -> List[Tuple[int, int, int, int]]:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        mask = cv2.inRange(gray, 0, 85)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
        contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        H, W = gray.shape
        rects: list[tuple[int, int, int, int]] = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if w * h < 30000 or w < 200 or h < 150:
                continue
            if w > W * .98 and h > H * .98:
                continue
            ratio = w / h
            if .55 <= ratio <= 1.20:
                rects.append((x, y, w, h))
        rects = dedupe_rects(rects)
        if len(rects) > 10:
            rects = sorted(rects, key=lambda r: r[2] * r[3], reverse=True)[:10]
        return sorted(rects, key=lambda r: (r[1], r[0]))

    def extract_sticker_rgba(self, frame_bgr: np.ndarray, remove_frame_number: bool = True) -> np.ndarray:
        c = self.config.inner_border_crop
        if frame_bgr.shape[0] <= c * 2 or frame_bgr.shape[1] <= c * 2:
            raise ValueError('frame too small after border crop')
        frame = frame_bgr[c:-c, c:-c].copy()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if remove_frame_number:
            rgb = self._remove_frame_number(rgb)

        bg = estimate_bg_color(rgb)
        dist = color_distance(rgb, bg)
        high = float(self.config.bg_tolerance + self.config.bg_softness)
        candidate = (dist <= high).astype(np.uint8)
        outside = border_connected_mask(candidate)

        alpha = np.full(dist.shape, 255, dtype=np.uint8)
        low = max(1.0, float(self.config.bg_tolerance - self.config.bg_softness))
        soft = np.clip((dist - low) / max(1.0, high - low), 0.0, 1.0)
        alpha[outside > 0] = np.round(soft[outside > 0] * 255.0).astype(np.uint8)

        rgb_clean = rgb.copy()
        rgb_clean[alpha == 0] = 0

        ys, xs = np.where(alpha > 2)
        if not len(xs):
            return np.dstack([rgb_clean, alpha])
        pad = 2
        x0, x1 = max(0, xs.min()-pad), min(rgb.shape[1], xs.max()+1+pad)
        y0, y1 = max(0, ys.min()-pad), min(rgb.shape[0], ys.max()+1+pad)
        return np.dstack([rgb_clean[y0:y1, x0:x1], alpha[y0:y1, x0:x1]])

    def _sheet_has_frame_numbers(self, image: np.ndarray, rects: list[tuple[int, int, int, int]]) -> bool:
        scores=[]; c=self.config.inner_border_crop
        for x,y,w,h in rects:
            frame=image[y+c:y+h-c, x+c:x+w-c]
            if frame.size == 0: continue
            gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            band=gray[:min(22,gray.shape[0]), min(60,gray.shape[1]):]
            scores.append(int((band < 100).sum()))
        return bool(scores) and float(np.median(scores)) < 60.0

    def _remove_frame_number(self, rgb: np.ndarray) -> np.ndarray:
        bg = estimate_bg_color(rgb)
        h, w, _ = rgb.shape
        rgb[:min(36,h), :min(55,w)] = bg
        return rgb

    def fit_to_canvas(self, rgba: np.ndarray, out_w: int, out_h: int, margin: int) -> np.ndarray:
        h, w = rgba.shape[:2]
        if h <= 0 or w <= 0:
            raise ValueError('empty RGBA sticker')
        scale = min((out_w - 2*margin)/w, (out_h - 2*margin)/h)
        new_w = max(2, int(round(w*scale))); new_h = max(2, int(round(h*scale)))
        resized = resize_rgba_premultiplied(rgba, (new_w, new_h))
        canvas = np.zeros((out_h, out_w, 4), dtype=np.uint8)
        x=(out_w-new_w)//2; y=(out_h-new_h)//2
        canvas[y:y+new_h, x:x+new_w] = resized
        return canvas


def border_connected_mask(candidate: np.ndarray) -> np.ndarray:
    mask = (candidate > 0).astype(np.uint8)
    if mask.size == 0:
        return mask
    n, labels = cv2.connectedComponents(mask, connectivity=8)
    border_labels = set(np.unique(np.concatenate((labels[0], labels[-1], labels[:,0], labels[:,-1]))).tolist())
    border_labels.discard(0)
    out = np.zeros_like(mask)
    for label in border_labels:
        out[labels == label] = 1
    return out


def resize_rgba_premultiplied(rgba: np.ndarray, size: tuple[int,int]) -> np.ndarray:
    arr = rgba.astype(np.float32) / 255.0
    a = arr[...,3:4]
    premul = arr[...,:3] * a
    target = tuple(map(int,size))
    premul_r = cv2.resize(premul, target, interpolation=cv2.INTER_LANCZOS4)
    alpha_r = cv2.resize(a[...,0], target, interpolation=cv2.INTER_LANCZOS4)[...,None]
    alpha_r = np.clip(alpha_r, 0.0, 1.0)
    rgb = np.zeros_like(premul_r)
    np.divide(premul_r, np.maximum(alpha_r, 1e-6), out=rgb, where=alpha_r > 1e-6)
    out = np.concatenate([np.clip(rgb,0,1), alpha_r], axis=2)
    out_u8 = np.round(out*255.0).astype(np.uint8)
    out_u8[out_u8[...,3] == 0, :3] = 0
    return out_u8


def dedupe_rects(rects: List[Tuple[int, int, int, int]]) -> List[Tuple[int, int, int, int]]:
    kept=[]
    for r in sorted(rects,key=lambda r:r[2]*r[3],reverse=True):
        x,y,w,h=r
        if any(abs(x-x2)<10 and abs(y-y2)<10 and abs(w-w2)<15 and abs(h-h2)<15 for x2,y2,w2,h2 in kept):
            continue
        kept.append(r)
    return kept


def estimate_bg_color(rgb: np.ndarray) -> np.ndarray:
    h,w,_=rgb.shape; size=max(8,min(h,w)//12); border=max(6,min(h,w)//40)
    samples=[rgb[:size,:size],rgb[:size,-size:],rgb[-size:,:size],rgb[-size:,-size:],
             rgb[:border,:],rgb[-border:,:],rgb[:,:border],rgb[:,-border:]]
    pixels=np.vstack([s.reshape(-1,3) for s in samples]).astype(np.float32)
    return np.median(pixels,axis=0).astype(np.uint8)


def color_distance(rgb: np.ndarray, bg: np.ndarray) -> np.ndarray:
    diff=rgb.astype(np.int32)-bg.reshape(1,1,3).astype(np.int32)
    return np.sqrt((diff*diff).sum(axis=2))


def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(65536),b''): h.update(chunk)
    return h.hexdigest()
