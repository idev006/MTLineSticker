from __future__ import annotations

from pathlib import Path

from ..contracts import ArtifactRef, StageResult, STAGE_SUBMISSION, sha256_file
from ..packaging import LineStaticPackageBuilder
from ..validator import StaticStickerValidator


class SubmissionModule:
    """Stage 4: LINE-ready stickers -> validated submission package."""

    stage_name = STAGE_SUBMISSION
    allowed_counts = (8, 16, 24, 32, 40)

    def run(self, input_path: str | Path, output_path: str | Path, **kwargs) -> StageResult:
        input_path = Path(input_path)
        output_path = Path(output_path)
        output_path.mkdir(parents=True, exist_ok=True)
        files = sorted(p for p in input_path.glob("*.png") if not p.name.startswith("manifest."))
        if len(files) not in self.allowed_counts:
            raise RuntimeError(f"invalid LINE static sticker count: {len(files)}")

        inputs = [ArtifactRef(path=str(p), sha256=sha256_file(p)) for p in files]
        failed = [v for v in StaticStickerValidator().validate_many(files) if not v.passed]
        if failed:
            raise RuntimeError(f"{len(failed)} sticker(s) failed pre-package validation")

        package = LineStaticPackageBuilder().build(files, output_path)
        result = StageResult(
            stage=self.stage_name,
            status="PASS",
            inputs=inputs,
            outputs=[],
            metrics={"stickers": len(files), "package": package},
            config={"allowed_counts": list(self.allowed_counts)},
        )
        result.write_manifest(output_path / "manifest.submission.json")
        return result
