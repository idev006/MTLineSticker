# MT LINE Sticker Studio — Engine + Desktop

This directory is the canonical Python implementation for the MTLineSticker project.

## Current source layout
- `src/line_sticker_pipeline/` — engine, pipeline, parallel runner, validator, packaging, job state, locking, CLI and PySide6 desktop UI
- `pyproject.toml` — package/dependency definition
- `tools/` — Windows run/test/build scripts

## Architecture
PySide6/Qt6 desktop shell -> QThread application worker -> in-process ProductionPipeline -> spawn-based ProcessPool workers -> StickerEngine -> LINE technical validator -> transactional export/package.

The UI contains no image-processing business logic; the engine remains reusable by CLI and future API adapters.

## Reliability model
- SHA-256 folder scanning/deduplication
- explicit job state in SQLite
- project lock with stale-lock recovery
- configurable 1–32 workers
- cooperative cancellation
- transactional final output
- technical validation before packaging
- Visual QA is mandatory and cannot be replaced by technical PASS

## Background-removal safety
The current engine uses border-connected background matting rather than destructive global threshold removal. Enclosed foreground pixels are preserved, transparent RGB is neutralized, and RGBA resizing uses premultiplied alpha to reduce color fringe.

## Desktop status
PySide6 desktop source is implemented. Native Windows runtime/UAT and clean-machine executable validation remain required before declaring the desktop binary a Production Release.
