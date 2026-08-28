from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from PIL import Image

@dataclass(frozen=True)
class ValidationResult:
    path: str
    passed: bool
    width: int
    height: int
    mode: str
    bytes: int
    has_alpha: bool
    even_dimensions: bool
    issues: tuple[str, ...]
    dpi: tuple[float, float] | None = None

class StaticStickerValidator:
    def __init__(self, max_width: int = 370, max_height: int = 320, max_bytes: int = 1024 * 1024):
        self.max_width=max_width; self.max_height=max_height; self.max_bytes=max_bytes
    def validate(self, path: str | Path) -> ValidationResult:
        path=Path(path); issues=[]
        with Image.open(path) as im:
            width,height=im.size; mode=im.mode; has_alpha='A' in im.getbands(); dpi=im.info.get('dpi')
        size=path.stat().st_size
        if path.suffix.lower()!='.png': issues.append('format_not_png')
        if width>self.max_width or height>self.max_height: issues.append('dimensions_exceed_limit')
        if width%2 or height%2: issues.append('dimensions_not_even')
        if not has_alpha: issues.append('missing_alpha')
        if size>self.max_bytes: issues.append('file_too_large')
        if dpi is None or min(dpi)<71.5: issues.append('dpi_below_72_or_missing')
        return ValidationResult(str(path),not issues,width,height,mode,size,has_alpha,width%2==0 and height%2==0,tuple(issues),dpi)
    def validate_many(self, paths: Iterable[str | Path]) -> list[ValidationResult]:
        return [self.validate(p) for p in paths]
