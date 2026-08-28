from __future__ import annotations

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Protocol, Sequence
import hashlib
import json
from datetime import datetime, timezone


STAGE_FRAME_EXTRACT = "frame_extract"
STAGE_BACKGROUND_REMOVE = "background_remove"
STAGE_LINE_NORMALIZE = "line_normalize"
STAGE_SUBMISSION = "submission"


@dataclass(frozen=True)
class ArtifactRef:
    path: str
    sha256: str
    width: int | None = None
    height: int | None = None
    mode: str | None = None
    source_path: str | None = None
    source_sha256: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class StageResult:
    stage: str
    status: str
    inputs: list[ArtifactRef]
    outputs: list[ArtifactRef]
    warnings: list[str] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)
    config: dict[str, Any] = field(default_factory=dict)
    module_version: str = "1"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def write_manifest(self, path: str | Path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(asdict(self), ensure_ascii=False, indent=2), encoding="utf-8")
        return path


class StageModule(Protocol):
    stage_name: str

    def run(self, input_path: str | Path, output_path: str | Path, **kwargs: Any) -> StageResult: ...


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()
