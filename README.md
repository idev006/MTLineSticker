# MTLineSticker — Police Admin LINE Sticker Project

Repository SSOT for the LINE sticker project focused on Thai administrative police officers. The current development direction is **พี่พร้อม: Paper-Tear Mascot** — a deliberately rough torn-paper collage character designed around real administrative-work workflows.

## Current status
- Target: Thai administrative police officers at operational level
- Product: Set 01, 40 static LINE stickers
- Content status: Caption Candidate v0.9
- Character status: Paper-Tear Mascot v0.5, not yet Master Locked
- Engine status: Python RC baseline stored in `engine/`
- Production rule: technical PASS is not sufficient; Visual QA remains a mandatory release gate

## SSOT map
- `docs/00_PROJECT_CHARTER.md`
- `docs/01_TARGET_AUDIENCE.md`
- `docs/02_PRODUCT_STRATEGY.md`
- `docs/research/03_WORKFLOW_RESEARCH.md`
- `docs/content/04_CAPTION_SYSTEM.md`
- `docs/character/17_CHARACTER_BIBLE_v0.5_PAPER_TEAR.md`
- `docs/character/18_CHARACTER_PROP_SHEET_PRODUCTION_BRIEF_v0.5.md`
- `docs/production/07_PRODUCTION_PIPELINE.md`
- `docs/marketing/08_GO_TO_MARKET.md`
- `docs/qa/09_QA_CHECKLIST.md`
- `docs/10_ROADMAP.md`
- `docs/11_DECISION_LOG.md`
- `engine/README.md`
- `engine/MTLineSticker-engine-python-source.zip`

## Python production engine
The repository now also stores the Python engine project used for bordered contact-sheet processing. The source snapshot includes OpenCV/NumPy/Pillow processing, LINE technical validation, folder scanning, parallel workers, SQLite job state, locking, package generation, CLI, PySide6 shell source, tests, and engine documentation.

See `engine/README.md` and `engine/MTLineSticker-engine-python-source.zip`.

## Design principle
**Workflow-first + Distinctiveness-first.** Captions come from real work situations; the character must be recognisable without relying on uniform, text or props alone.

## Engineering principle
**Document-driven + Engine-first + Visual-QA-gated.** Project decisions and implementation must follow versioned documents; uncertain or visually defective outputs must not silently become PASS.
