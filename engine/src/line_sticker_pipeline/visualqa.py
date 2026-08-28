from __future__ import annotations
from pathlib import Path
from typing import Iterable
import json, math

from PIL import Image, ImageDraw

from .standards import LINE_STATIC_2026_08
from .validator import StaticStickerValidator


class VisualQaInspector:
    def __init__(self, edge_spill_limit: int = 250, strong_spill_limit: int = 25):
        self.edge_spill_limit=edge_spill_limit
        self.strong_spill_limit=strong_spill_limit
        self.validator=StaticStickerValidator()

    def inspect_many(self, paths: Iterable[str | Path], output_dir: str | Path | None = None) -> dict:
        paths=[Path(p) for p in paths]
        results=[self.inspect_one(p) for p in paths]
        count=len(paths)
        issues=[]
        if count not in LINE_STATIC_2026_08.allowed_counts:
            issues.append(f'invalid_sticker_count:{count}')
        failed=[r for r in results if r['issues']]
        report={
            'status':'PASS' if not issues and not failed else 'REVIEW_REQUIRED',
            'sticker_count':count,
            'allowed_counts':list(LINE_STATIC_2026_08.allowed_counts),
            'issues':issues,
            'failed_stickers':len(failed),
            'stickers':results,
        }
        if output_dir is not None:
            out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
            (out/'visual_qa_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
            self.write_contact_sheet(paths,out/'visual_qa_sheet.png')
        return report

    def inspect_one(self, path: str | Path) -> dict:
        path=Path(path)
        validation=self.validator.validate(path)
        issues=list(validation.issues)
        edge_spill,strong_spill=self._measure_edge_spill(path)
        if edge_spill > self.edge_spill_limit:
            issues.append(f'edge_background_spill:{edge_spill}')
        if strong_spill > self.strong_spill_limit:
            issues.append(f'strong_edge_background_spill:{strong_spill}')
        return {
            'file':path.name,
            'technical_pass':validation.passed,
            'content_margin':validation.content_margin,
            'bytes':validation.bytes,
            'edge_background_spill_pixels':edge_spill,
            'strong_edge_background_spill_pixels':strong_spill,
            'issues':issues,
        }

    def _measure_edge_spill(self, path: Path) -> tuple[int,int]:
        with Image.open(path) as im:
            rgba=im.convert('RGBA')
        pix=rgba.load()
        w,h=rgba.size
        alpha=rgba.getchannel('A')
        bbox=alpha.getbbox()
        if bbox is None:
            return 0,0
        edge=0
        strong=0
        for y in range(max(0,bbox[1]-2),min(h,bbox[3]+2)):
            for x in range(max(0,bbox[0]-2),min(w,bbox[2]+2)):
                r,g,b,a=pix[x,y]
                if a <= 24:
                    continue
                if not self._touches_transparency(alpha,x,y,w,h):
                    continue
                chroma=(g-r)>18 and (b-r)>8
                cyanish=(g>150 and b>140 and r<230)
                if chroma and cyanish:
                    edge+=1
                    if a > 96:
                        strong+=1
        return edge,strong

    def _touches_transparency(self, alpha: Image.Image, x: int, y: int, w: int, h: int) -> bool:
        for yy in range(max(0,y-2),min(h,y+3)):
            for xx in range(max(0,x-2),min(w,x+3)):
                if alpha.getpixel((xx,yy)) <= 8:
                    return True
        return False

    def write_contact_sheet(self, paths: list[Path], destination: str | Path) -> None:
        destination=Path(destination)
        thumb_w,thumb_h=185,160
        pad,label_h,cols=18,24,5
        bgs=[('white',(255,255,255)),('chat-green',(205,234,190)),('dark',(34,38,46))]
        rows=max(1,math.ceil(len(paths)/cols))
        canvas_w=cols*(thumb_w+pad)+pad
        block_h=rows*(thumb_h+label_h+pad)+pad
        canvas=Image.new('RGB',(canvas_w,len(bgs)*block_h),(238,242,247))
        d=ImageDraw.Draw(canvas)
        for bi,(name,bg) in enumerate(bgs):
            base_y=bi*block_h
            d.text((pad,base_y+4),name,fill=(16,32,51) if name!='dark' else (230,235,242))
            for i,p in enumerate(paths):
                x=pad+(i%cols)*(thumb_w+pad); y=base_y+pad+(i//cols)*(thumb_h+label_h+pad)
                d.rounded_rectangle((x-6,y-6,x+thumb_w+6,y+thumb_h+label_h+6),radius=8,fill=bg,outline=(205,214,226))
                with Image.open(p) as im:
                    im=im.convert('RGBA')
                    im.thumbnail((thumb_w,thumb_h),Image.LANCZOS)
                    canvas.paste(im,(x+(thumb_w-im.width)//2,y+(thumb_h-im.height)//2),im)
                d.text((x,y+thumb_h+5),p.name,fill=(16,32,51) if name!='dark' else (230,235,242))
        canvas.save(destination)
