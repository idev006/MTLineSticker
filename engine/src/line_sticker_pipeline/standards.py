from dataclasses import dataclass

@dataclass(frozen=True)
class LineStaticStandard:
    allowed_counts: tuple[int, ...] = (8, 16, 24, 32, 40)
    sticker_max_width: int = 370
    sticker_max_height: int = 320
    main_size: tuple[int, int] = (240, 240)
    tab_size: tuple[int, int] = (96, 74)
    max_image_bytes: int = 1024 * 1024
    max_zip_bytes: int = 60 * 1024 * 1024
    min_dpi: int = 72
    require_png: bool = True
    require_alpha: bool = True
    require_even_dimensions: bool = True
    recommended_margin_px: int = 10

LINE_STATIC_2026_08 = LineStaticStandard()
