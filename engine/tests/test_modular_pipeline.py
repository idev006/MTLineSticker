from pathlib import Path

import numpy as np
from PIL import Image

from line_sticker_pipeline.modules.background_remover import BackgroundRemovalModule
from line_sticker_pipeline.modules.line_normalizer import LineNormalizerModule
from line_sticker_pipeline.orchestrator import WorkspacePaths


def _synthetic_frame(path: Path, size=(320, 280)):
    w, h = size
    arr = np.zeros((h, w, 3), dtype=np.uint8)
    arr[:] = (20, 220, 205)  # controlled cyan/green background
    arr[60:230, 90:230] = (180, 120, 70)  # foreground block
    Image.fromarray(arr, mode="RGB").save(path)


def test_background_stage_preserves_dimensions(tmp_path):
    raw = tmp_path / "raw"
    out = tmp_path / "transparent"
    raw.mkdir()
    src = raw / "001.png"
    _synthetic_frame(src, (320, 280))

    result = BackgroundRemovalModule().run(raw, out)
    produced = out / "001.png"
    with Image.open(produced) as im:
        assert im.size == (320, 280)
        assert im.mode == "RGBA"
    assert result.stage == "background_remove"
    assert result.config["resize"] is False


def test_normalizer_is_the_resize_stage(tmp_path):
    transparent = tmp_path / "transparent"
    out = tmp_path / "line"
    transparent.mkdir()
    rgba = np.zeros((280, 320, 4), dtype=np.uint8)
    rgba[30:250, 60:260] = (180, 120, 70, 255)
    Image.fromarray(rgba, mode="RGBA").save(transparent / "001.png")

    result = LineNormalizerModule(width=370, height=320, margin=20).run(transparent, out)
    with Image.open(out / "001.png") as im:
        assert im.size == (370, 320)
        assert im.mode == "RGBA"
    assert result.stage == "line_normalize"


def test_workspace_paths_are_stage_separated(tmp_path):
    paths = WorkspacePaths(tmp_path)
    assert paths.raw_frames.name == "01_raw_frames"
    assert paths.transparent_master.name == "02_transparent_master"
    assert paths.line_ready.name == "03_line_ready"
    assert paths.submission.name == "04_submission"
