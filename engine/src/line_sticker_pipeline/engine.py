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
    output_mode: str = 'frame_crop'
    output_width: int = 370
    output_height: int = 320
    inner_border_crop: int = 8
    bg_tolerance: int = 42
    bg_softness: int = 18
    fit_margin: int = 20
    edge_spill_tolerance: int = 150
    edge_spill_radius: int = 8
    final_edge_cleanup_radius: int = 4


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
        image = read_color_image(sheet_path)
        if image is None:
            raise ValueError(f'cannot read image: {sheet_path}')
        rects = self.detect_frames(image)
        if not rects:
            raise ValueError(f'no sticker frames detected: {sheet_path}')

        items = []
        idx = start_index
        numbered_sheet = self._sheet_has_frame_numbers(image, rects) if self.config.output_mode == 'line_sticker' else False
        for order, (x, y, w, h) in enumerate(rects, start=1):
            crop_x,crop_y,crop_w,crop_h = inset_rect(x,y,w,h,self.config.inner_border_crop,image.shape[1],image.shape[0])
            crop = image[crop_y:crop_y+crop_h, crop_x:crop_x+crop_w].copy()
            out_name = f'{idx:02d}.png'
            out_path = output_dir / out_name
            if self.config.output_mode == 'frame_crop':
                output = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
                Image.fromarray(output, mode='RGB').save(out_path, dpi=(72, 72), optimize=True)
                output_size = [int(crop_w), int(crop_h)]
            elif self.config.output_mode == 'line_sticker':
                rgba = self.extract_sticker_rgba(crop, remove_frame_number=numbered_sheet)
                output = self.fit_to_canvas(rgba, self.config.output_width, self.config.output_height, self.config.fit_margin, source_bg=estimate_bg_color(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)))
                Image.fromarray(output, mode='RGBA').save(out_path, dpi=(72, 72), optimize=True)
                output_size = [self.config.output_width, self.config.output_height]
            else:
                raise ValueError(f'unknown output mode: {self.config.output_mode}')
            items.append({
                'index': idx, 'frame_order': order,
                'frame_rect': [int(x), int(y), int(w), int(h)],
                'crop_rect': [int(crop_x), int(crop_y), int(crop_w), int(crop_h)],
                'output_file': out_name,
                'output_size': output_size,
                'file_size_bytes': out_path.stat().st_size,
                'sha256': sha256_file(out_path),
            })
            idx += 1

        sheet_report = {
            'sheet': Path(sheet_path).name,
            'sheet_size': list(Image.open(sheet_path).size),
            'output_mode': self.config.output_mode,
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
        alpha = suppress_edge_spill(alpha, dist, self.config.edge_spill_tolerance, self.config.edge_spill_radius, rgb, bg)

        rgb_clean = rgb.copy()
        rgb_clean[alpha <= 2] = 0

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

    def fit_to_canvas(self, rgba: np.ndarray, out_w: int, out_h: int, margin: int, source_bg: np.ndarray | None = None) -> np.ndarray:
        h, w = rgba.shape[:2]
        if h <= 0 or w <= 0:
            raise ValueError('empty RGBA sticker')
        if margin < 0 or out_w <= margin * 2 or out_h <= margin * 2:
            raise ValueError('invalid output canvas margin')
        scale = min((out_w - 2*margin)/w, (out_h - 2*margin)/h)
        new_w = max(2, int(round(w*scale))); new_h = max(2, int(round(h*scale)))
        resized = resize_rgba_premultiplied(rgba, (new_w, new_h))
        if source_bg is not None:
            resized = final_edge_cleanup(resized, source_bg, self.config.final_edge_cleanup_radius)
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


def inset_rect(x: int, y: int, w: int, h: int, inset: int, max_w: int, max_h: int) -> tuple[int,int,int,int]:
    inset=max(0,int(inset))
    x0=min(max_w,max(0,int(x)+inset))
    y0=min(max_h,max(0,int(y)+inset))
    x1=max(0,min(max_w,int(x)+int(w)-inset))
    y1=max(0,min(max_h,int(y)+int(h)-inset))
    if x1 <= x0 or y1 <= y0:
        raise ValueError('frame too small after border crop')
    return x0,y0,x1-x0,y1-y0


def estimate_bg_color(rgb: np.ndarray) -> np.ndarray:
    h,w,_=rgb.shape; size=max(8,min(h,w)//12); border=max(6,min(h,w)//40)
    samples=[rgb[:size,:size],rgb[:size,-size:],rgb[-size:,:size],rgb[-size:,-size:],
             rgb[:border,:],rgb[-border:,:],rgb[:,:border],rgb[:,-border:]]
    pixels=np.vstack([s.reshape(-1,3) for s in samples]).astype(np.float32)
    return np.median(pixels,axis=0).astype(np.uint8)


def color_distance(rgb: np.ndarray, bg: np.ndarray) -> np.ndarray:
    diff=rgb.astype(np.int32)-bg.reshape(1,1,3).astype(np.int32)
    return np.sqrt((diff*diff).sum(axis=2))


def suppress_edge_spill(alpha: np.ndarray, dist: np.ndarray, tolerance: int, radius: int, rgb: np.ndarray | None = None, bg: np.ndarray | None = None) -> np.ndarray:
    if radius <= 0 or tolerance <= 0:
        return alpha
    transparent = (alpha <= 8).astype(np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (radius * 2 + 1, radius * 2 + 1))
    edge_band = cv2.dilate(transparent, kernel, iterations=1).astype(bool) & (alpha > 8)
    spill = edge_band & (dist <= float(tolerance))
    chroma_spill = np.zeros_like(edge_band, dtype=bool)
    if rgb is not None and bg is not None:
        rgb_i=rgb.astype(np.int16)
        bg_i=bg.astype(np.int16)
        green_blue_bias=((rgb_i[...,1]-rgb_i[...,0]) > max(18, int((bg_i[1]-bg_i[0]) * 0.20))) & ((rgb_i[...,2]-rgb_i[...,0]) > max(8, int((bg_i[2]-bg_i[0]) * 0.15)))
        chroma_spill = edge_band & green_blue_bias & (dist <= float(tolerance + 36))
        spill = spill | chroma_spill
    if not np.any(spill):
        return alpha
    cleaned = alpha.copy()
    spill_alpha = np.square(np.clip(dist[spill] / max(1.0, float(tolerance)), 0.0, 1.0)) * 255.0
    cleaned[spill] = np.minimum(cleaned[spill], np.round(spill_alpha).astype(np.uint8))
    cleaned[(edge_band & (dist <= float(tolerance) * 0.50))] = 0
    cleaned[chroma_spill] = 0
    return cleaned


def final_edge_cleanup(rgba: np.ndarray, bg: np.ndarray, radius: int) -> np.ndarray:
    if radius <= 0 or rgba.size == 0:
        return rgba
    out=rgba.copy()
    alpha=out[...,3]
    transparent=(alpha <= 8).astype(np.uint8)
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(radius*2+1,radius*2+1))
    edge_band=cv2.dilate(transparent,kernel,iterations=1).astype(bool) & (alpha > 8)
    rgb=out[...,:3].astype(np.int16)
    bg_i=bg.astype(np.int16)
    dist=color_distance(out[...,:3],bg)
    green_blue_bias=((rgb[...,1]-rgb[...,0]) > max(16, int((bg_i[1]-bg_i[0]) * 0.16))) & ((rgb[...,2]-rgb[...,0]) > max(6, int((bg_i[2]-bg_i[0]) * 0.12)))
    spill=edge_band & green_blue_bias & (dist <= 220.0)
    near_bg=edge_band & (dist <= 70.0)
    out[spill | near_bg,3]=0
    out[out[...,3] <= 2,:3]=0
    return out


def read_color_image(path: str | Path) -> np.ndarray | None:
    path=Path(path)
    if not path.is_file():
        return None
    data=np.fromfile(path,dtype=np.uint8)
    if data.size == 0:
        return None
    return cv2.imdecode(data,cv2.IMREAD_COLOR)


def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(65536),b''): h.update(chunk)
    return h.hexdigest()
