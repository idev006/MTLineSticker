# Product Architecture

Brand → Characters → Sticker Sets → Individual Stickers

## Shared layer
Character masters, materials, poses, expressions, visual standards and project standards live outside individual sets.

## Set layer
Each sellable set owns its brief, captions, caption matrix, manifest, QA, marketing and submission package.

## Current set IDs
- SET-001-EVERYDAY-ADMIN
- SET-002-MEETING
- SET-003-FOLLOWUP
- SET-004-DOCUMENT
- SET-005-OFFICE-LIFE

## Sticker IDs
Use SET###-STK###, e.g. SET001-STK001.

## Lifecycle
IDEA → RESEARCH → CONTENT_LOCK → CHARACTER_MAPPING → PROTOTYPE → QA → APPROVED → SUBMISSION → RELEASED

## Rule
Do not fork shared character masters inside a set. Deliberate caption reuse must be recorded in data/CAPTION_REGISTRY.csv.
