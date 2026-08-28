from __future__ import annotations

from pathlib import Path
import numpy as np
from PIL import Image

from ..contracts import ArtifactRef, StageResult, STAGE_LINE_NORMALIZE, sha256_file
from ..engine import EngineConfig, StickerEngine
from ..validator import StaticStickerValidator


class LineNormalizerModule:
    """Stage 3: transparent master folder -> LINE-ready sticker canvases."""

    stage_name = STAGE_LINE_NORMALIZE

    def __init__(self, width: int = 370, height: int = 320, margin: int = 20):
        self.width = int(width)
        self.height = int(height)
        self.margin = int(margin)
        self._engine = StickerEngine(EngineConfig(output_mode="line_sticker", output_width=self.width, output_height=self.height, fit_margin=self.margin))

    def run(self, input_path: str | Path, output_path: str | Path, **kwargs) -> StageResult:
        input_path = Path(input_path)
        output_path = Path(output_path)
        output_path.mkdir(parents=True, exist_ok=True)
        files = sorted(p for p in input_path.glob("*.png") if not p.name.startswith("manifest."))
        if not files:
            raise RuntimeError("no transparent master PNG files found")

        inputs: list[ArtifactRef] = []
        outputs: list[ArtifactRef] = []
        for idx, src in enumerate(files, 1):
            with Image.open(src) as im:
                rgba = np.array(im.convert("RGBA"))
                inputs.append(ArtifactRef(path=str(src), sha256=sha256_file(src), width=im.width, height=im.height, mode=im.mode))
            fitted = self._engine.fit_to_canvas(rgba, self.width, self.height, self.margin)
            dst = output_path / f"{idx:03d}.png"
            Image.fromarray(fitted, mode="RGBA").save(dst, dpi=(72, 72), optimize=True)
            outputs.append(ArtifactRef(path=str(dst), sha256=sha256_file(dst), width=self.width, height=self.height, mode="RGBA", source_path=str(src), source_sha256=sha256_file(src)))

        failed = [v for v in StaticStickerValidator().validate_many([Path(x.path) for x in outputs]) if not v.passed]
        result = StageResult(
            stage=self.stage_name,
            status="PASS" if not failed else "FAILED",
            inputs=inputs,
            outputs=outputs,
            warnings=[] if not failed else [f"technical_validation_failures:{len(failed)}"],
            metrics={"images": len(outputs), "technical_failures": len(failed)},
            config={"canvas": [self.width, self.height], "margin": self.margin, "dpi": 72},
        )
        result.write_manifest(output_path / "manifest.line_normalize.json")
        if failed:
            raise RuntimeError(f"{len(failed)} normalized sticker(s) failed LINE technical validation")
        return result
