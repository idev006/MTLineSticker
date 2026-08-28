from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import cv2
import numpy as np
from PIL import Image

from ..contracts import ArtifactRef, StageResult, STAGE_BACKGROUND_REMOVE, sha256_file
from ..engine import border_connected_mask, color_distance, estimate_bg_color, suppress_edge_spill


@dataclass
class RemovalResult:
    rgba: np.ndarray
    confidence: float
    method: str
    warnings: list[str]
    metrics: dict[str, float]


class BackgroundRemovalProvider(Protocol):
    name: str

    def remove(self, rgb: np.ndarray) -> RemovalResult: ...


class ClassicalBackgroundProvider:
    """Conservative Stage-2 provider for controlled sticker backgrounds.

    Only background-like pixels connected to the outer image border may become
    transparent. The provider deliberately preserves image dimensions.
    """

    name = "classical_border_connected_v1"

    def __init__(self, tolerance: int = 42, softness: int = 18, edge_spill_tolerance: int = 150, edge_spill_radius: int = 8):
        self.tolerance = int(tolerance)
        self.softness = int(softness)
        self.edge_spill_tolerance = int(edge_spill_tolerance)
        self.edge_spill_radius = int(edge_spill_radius)

    def remove(self, rgb: np.ndarray) -> RemovalResult:
        bg = estimate_bg_color(rgb)
        dist = color_distance(rgb, bg)
        high = float(self.tolerance + self.softness)
        low = max(1.0, float(self.tolerance - self.softness))
        candidate = (dist <= high).astype(np.uint8)
        outside = border_connected_mask(candidate)
        alpha = np.full(dist.shape, 255, dtype=np.uint8)
        soft = np.clip((dist - low) / max(1.0, high - low), 0.0, 1.0)
        alpha[outside > 0] = np.round(soft[outside > 0] * 255.0).astype(np.uint8)
        alpha = suppress_edge_spill(alpha, dist, self.edge_spill_tolerance, self.edge_spill_radius, rgb, bg)

        rgba = np.dstack([rgb.copy(), alpha])
        rgba[alpha <= 2, :3] = 0
        transparent_ratio = float(np.mean(alpha <= 8))
        opaque_ratio = float(np.mean(alpha >= 247))
        soft_ratio = float(np.mean((alpha > 8) & (alpha < 247)))
        warnings: list[str] = []
        if transparent_ratio < 0.05:
            warnings.append("very_little_background_removed")
        if opaque_ratio < 0.08:
            warnings.append("foreground_may_be_over_removed")
        if soft_ratio > 0.25:
            warnings.append("large_soft_alpha_region")

        confidence = max(0.0, min(1.0, 1.0 - (0.35 if warnings else 0.0) - min(0.25, soft_ratio)))
        return RemovalResult(
            rgba=rgba,
            confidence=confidence,
            method=self.name,
            warnings=warnings,
            metrics={"transparent_ratio": transparent_ratio, "opaque_ratio": opaque_ratio, "soft_alpha_ratio": soft_ratio},
        )


class BackgroundRemovalModule:
    stage_name = STAGE_BACKGROUND_REMOVE

    def __init__(self, provider: BackgroundRemovalProvider | None = None):
        self.provider = provider or ClassicalBackgroundProvider()

    def run(self, input_path: str | Path, output_path: str | Path, **kwargs) -> StageResult:
        input_path = Path(input_path)
        output_path = Path(output_path)
        output_path.mkdir(parents=True, exist_ok=True)
        if not input_path.is_dir():
            raise ValueError("BackgroundRemovalModule expects a folder of raw frame images")

        files = sorted(p for p in input_path.rglob("*.png") if not p.name.startswith("manifest."))
        if not files:
            raise RuntimeError("no raw frame PNG files found")

        inputs: list[ArtifactRef] = []
        outputs: list[ArtifactRef] = []
        warnings: list[str] = []
        confidences: list[float] = []
        for idx, src in enumerate(files, 1):
            with Image.open(src) as im:
                rgb = np.array(im.convert("RGB"))
                original_size = im.size
                inputs.append(ArtifactRef(path=str(src), sha256=sha256_file(src), width=im.width, height=im.height, mode=im.mode))
            removed = self.provider.remove(rgb)
            if removed.rgba.shape[1::-1] != original_size:
                raise RuntimeError(f"provider changed image dimensions for {src.name}")
            dst = output_path / f"{idx:03d}.png"
            Image.fromarray(removed.rgba, mode="RGBA").save(dst, optimize=True)
            confidences.append(removed.confidence)
            warnings.extend(f"{src.name}:{w}" for w in removed.warnings)
            outputs.append(ArtifactRef(
                path=str(dst), sha256=sha256_file(dst), width=original_size[0], height=original_size[1], mode="RGBA",
                source_path=str(src), source_sha256=sha256_file(src),
                metadata={"provider": removed.method, "confidence": removed.confidence, **removed.metrics},
            ))

        status = "PASS" if not warnings else "REVIEW_REQUIRED"
        result = StageResult(
            stage=self.stage_name,
            status=status,
            inputs=inputs,
            outputs=outputs,
            warnings=warnings,
            metrics={"images": len(outputs), "mean_confidence": float(np.mean(confidences)) if confidences else 0.0},
            config={"provider": getattr(self.provider, "name", self.provider.__class__.__name__), "resize": False, "dimension_preserving": True},
        )
        result.write_manifest(output_path / "manifest.background_remove.json")
        return result
