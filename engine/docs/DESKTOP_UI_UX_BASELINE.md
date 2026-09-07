# Desktop UI/UX Baseline — MT LINE Sticker Studio

Status: SOURCE IMPLEMENTED / NATIVE WINDOWS UAT PENDING

## Goal
Provide a production desktop shell around the sticker engine without moving image-processing logic into the UI.

## Main workflow
Select or drag Input Folder -> Scan -> review queue -> choose worker count -> Start -> live progress/status -> Preview/Visual QA -> open output/package.

## Implemented controls
- Input folder and output folder selection
- folder drag/drop
- recursive scan option
- configurable workers 1–32
- auto-package option
- Scan / Start / Cancel / Open Output
- metrics: input files, generated stickers, technical failures, effective workers
- job table with state/stage/progress/error
- live progress bar and technical log
- generated-sticker preview
- persistent QSettings
- cooperative cancellation
- close protection while a job is active
- safe input/output folder validation

## Architecture
PySide6 main thread -> QThread application worker -> ProductionPipeline -> spawn-based ProcessPool workers -> StickerEngine -> validator -> transactional export/package.

The UI does not own image-processing rules. Engine logic remains reusable by CLI and future API adapters.

## Visual QA policy
Technical PASS never implies artwork approval. Final candidate images must be reviewed on light and dark backgrounds for mottling, holes, edge erosion, cyan/green fringe, clipped content, unreadable Thai text and background residue.

## Release gate
Native Windows execution, display-scaling checks, cancel/recovery checks, PyInstaller build and UAT on a clean Windows machine are required before declaring Desktop Production Release.
