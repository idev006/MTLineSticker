from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Any

from .contracts import StageResult
from .modules import FrameExtractorModule, BackgroundRemovalModule, LineNormalizerModule, SubmissionModule


@dataclass
class WorkspacePaths:
    root: Path

    @property
    def raw_frames(self) -> Path:
        return self.root / "01_raw_frames"

    @property
    def transparent_master(self) -> Path:
        return self.root / "02_transparent_master"

    @property
    def line_ready(self) -> Path:
        return self.root / "03_line_ready"

    @property
    def submission(self) -> Path:
        return self.root / "04_submission"


class ModularStickerOrchestrator:
    """Application-facing coordinator for independently runnable engine stages.

    The UI may call any stage directly. This class owns no Qt code and may be
    reused by CLI or future API adapters.
    """

    def __init__(self,
                 frame_extractor: FrameExtractorModule | None = None,
                 background_remover: BackgroundRemovalModule | None = None,
                 normalizer: LineNormalizerModule | None = None,
                 submission: SubmissionModule | None = None):
        self.frame_extractor = frame_extractor or FrameExtractorModule()
        self.background_remover = background_remover or BackgroundRemovalModule()
        self.normalizer = normalizer or LineNormalizerModule()
        self.submission = submission or SubmissionModule()

    def extract_frames(self, contact_sheet_folder: str | Path, workspace: str | Path) -> StageResult:
        paths = WorkspacePaths(Path(workspace))
        return self.frame_extractor.run(contact_sheet_folder, paths.raw_frames)

    def remove_background(self, frame_folder: str | Path, workspace: str | Path) -> StageResult:
        paths = WorkspacePaths(Path(workspace))
        return self.background_remover.run(frame_folder, paths.transparent_master)

    def normalize_for_line(self, transparent_folder: str | Path, workspace: str | Path) -> StageResult:
        paths = WorkspacePaths(Path(workspace))
        return self.normalizer.run(transparent_folder, paths.line_ready)

    def build_submission(self, line_ready_folder: str | Path, workspace: str | Path) -> StageResult:
        paths = WorkspacePaths(Path(workspace))
        return self.submission.run(line_ready_folder, paths.submission)
