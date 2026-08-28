# LINE Sticker Production Engine

This directory contains the Python engine snapshot for the MTLineSticker project.

## Scope
- bordered contact-sheet frame detection
- sticker extraction and transparent PNG export
- LINE static sticker technical validation
- folder scanning and deduplication
- parallel worker execution
- SQLite job state
- locking and transactional output
- LINE package generation
- CLI and PySide6 desktop shell source
- automated tests and engine-specific documentation

## Source package
`MTLineSticker-engine-python-source.zip` contains the complete Python project snapshot, including `src/`, `tests/`, `docs/`, `pyproject.toml`, and `.gitignore`.

## Important status note
This snapshot is the preserved RC Python baseline available from the development workspace. Visual QA remains a mandatory release gate; technical validation alone does not guarantee acceptable sticker artwork or LINE marketplace approval.

## Architecture
PySide6/Qt6 desktop shell -> in-process ProductionPipeline -> spawn-based parallel workers -> StickerEngine -> validator -> LINE package builder.

The engine is UI-independent and intended to remain reusable by future CLI/API adapters.
