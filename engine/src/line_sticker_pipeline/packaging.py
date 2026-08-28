from __future__ import annotations
from pathlib import Path
from PIL import Image
import zipfile, json
from .standards import LINE_STATIC_2026_08
from .validator import StaticStickerValidator

class PackageError(RuntimeError): pass

class LineStaticPackageBuilder:
    def __init__(self):
        self.std=LINE_STATIC_2026_08; self.validator=StaticStickerValidator()
    def build(self,sticker_paths:list[str|Path],output_dir:str|Path,main_source:str|Path|None=None,tab_source:str|Path|None=None):
        paths=[Path(p) for p in sticker_paths]
        if len(paths) not in self.std.allowed_counts: raise PackageError(f'invalid sticker count {len(paths)}; allowed {self.std.allowed_counts}')
        bad=[v for v in self.validator.validate_many(paths) if not v.passed]
        if bad: raise PackageError(f'{len(bad)} sticker(s) failed technical validation')
        out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
        main_src=Path(main_source) if main_source else paths[0]; tab_src=Path(tab_source) if tab_source else paths[0]
        _fit_rgba(main_src,out/'main.png',*self.std.main_size); _fit_rgba(tab_src,out/'tab.png',*self.std.tab_size)
        zip_path=out/'line_submission.zip'; manifest={'sticker_count':len(paths),'stickers':[],'main':'main.png','tab':'tab.png'}
        with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
            for i,p in enumerate(paths,1):
                arc=f'{i:02d}.png'; z.write(p,arc); manifest['stickers'].append(arc)
            z.write(out/'main.png','main.png'); z.write(out/'tab.png','tab.png'); z.writestr('manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
        if zip_path.stat().st_size>self.std.max_zip_bytes:
            zip_path.unlink(missing_ok=True); raise PackageError('zip exceeds LINE limit')
        (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
        return {'zip':str(zip_path),'zip_bytes':zip_path.stat().st_size,'manifest':manifest}

def _fit_rgba(src:Path,dst:Path,w:int,h:int):
    im=Image.open(src).convert('RGBA'); im.thumbnail((w,h),Image.LANCZOS)
    canvas=Image.new('RGBA',(w,h),(0,0,0,0)); canvas.alpha_composite(im,((w-im.width)//2,(h-im.height)//2)); canvas.save(dst,dpi=(72,72))
