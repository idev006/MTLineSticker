from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from PIL import Image

from ..contracts import ArtifactRef, StageResult, STAGE_FRAME_EXTRACT, sha256_file
from ..engine import EngineConfig, StickerEngine


class FrameExtractorModule:
    """Stage 1: contact sheet -> raw frame masters.

    This stage must not resize, remove background, create alpha, or otherwise
    modify the frame interior beyond cropping the configured frame border.
    """

    stage_name = STAGE_FRAME_EXTRACT

    def __init__(self, border_crop: int = 8):
        self.border_crop = max(0, int(border_crop))

    def run(self, input_path: str | Path, output_path: str | Path, **kwargs) -> StageResult:
        input_path = Path(input_path)
        output_path = Path(output_path)
        output_path.mkdir(parents=True, exist_ok=True)
        if not input_path.is_dir():
            raise ValueError("FrameExtractorModule expects an input folder containing contact sheets")

        config = EngineConfig(output_mode="frame_crop", inner_border_crop=self.border_crop)
        report = StickerEngine(config).process_folder(input_path, output_path)
        inputs: list[ArtifactRef] = []
        outputs: list[ArtifactRef] = []

        for sheet in report["sheets"]:
            source = input_path / sheet["sheet"]
            with Image.open(source) as im:
                inputs.append(ArtifactRef(path=str(source), sha256=sha256_file(source), width=im.width, height=im.height, mode=im.mode))
            sheet_dir = output_path / source.stem
            for item in sheet["stickers"]:
                produced = sheet_dir / item["output_file"]
                with Image.open(produced) as im:
                    outputs.append(ArtifactRef(
                        path=str(produced), sha256=sha256_file(produced), width=im.width, height=im.height, mode=im.mode,
                        source_path=str(source), source_sha256=sha256_file(source),
                        metadata={"frame_order": item["frame_order"], "frame_rect": item["frame_rect"], "crop_rect": item["crop_rect"]},
                    ))

        result = StageResult(
            stage=self.stage_name,
            status="PASS",
            inputs=inputs,
            outputs=outputs,
            metrics={"sheets": report["totals"]["sheets"], "frames": report["totals"]["frames_detected"]},
            config={"border_crop": self.border_crop, "resize": False, "background_removal": False},
        )
        result.write_manifest(output_path / "manifest.frame_extract.json")
        return result
