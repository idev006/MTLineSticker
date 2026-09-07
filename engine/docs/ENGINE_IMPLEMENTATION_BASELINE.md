# Engine Implementation Baseline — 2026-08-28

Status: BASELINED FOR REPOSITORY SYNC

## Purpose
Record the Python processing engine as part of the same document-driven MTLineSticker project SSOT.

## Approved technology baseline
- Python 3.11+
- OpenCV
- NumPy
- Pillow
- PySide6 / Qt 6
- concurrent.futures / ProcessPoolExecutor
- SQLite
- pytest
- Optional ONNX Runtime / local segmentation models
- Optional Thai OCR assistance

## Architecture
Desktop UI -> in-process application contract -> ProductionPipeline -> parallel worker runner -> StickerEngine -> technical validator -> LINE package builder.

The UI must not own image-processing business logic. The engine must remain UI-independent and reusable by future CLI/API adapters.

## Processing requirements
- folder scan and input discovery
- explicit job state
- configurable worker count
- project/output locking
- deterministic parallel execution
- transactional final output
- LINE static sticker technical preflight
- visual QA as a hard release gate

## Repository location
The preserved Python RC source snapshot is stored at:
`engine/MTLineSticker-engine-python-source.zip`

Engine-specific usage notes are stored at:
`engine/README.md`

## Quality governance
Technical compliance does not imply visual acceptance. Background-removal artifacts, foreground erosion, halos, speckling, unreadable text, or character damage must cause Visual QA failure even when dimensions, PNG format, transparency, file size, and packaging checks pass.
