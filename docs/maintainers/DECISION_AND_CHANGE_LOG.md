# Maintainer Decision & Change Log
As of 2026-10-21. Distinguish owner decisions from actual deployment and actual binary QA.

| Change | Owner decision | Plugin deployments | Image/cutter evidence |
|---|---|---|---|
| Universal 8 artworks / sheet, 4×2; five sheets for forty | Approved | GEM A/B prior releases; geometry v1.2 instruction present | Not established for latest assets |
| Frame aspect ratio fixed 592:512, frame border approx. 3px, 15px gutter and safe zone tolerance ±5% | Approved | GEM A v0.3.0 and GEM B v0.4.0 geometry policy v1.2.0 | Cutter integration NOT_RUN |
| Shaped solid white die-cut 3–5px following each individual sticker contour | Approved 2026-10-21 | GEM A v0.4.0, GEM B v0.5.0; contract v1.3.0 | No passing per-artwork pixel certificate |
| 100% empty-background true transparency; reject checkerboard fakes | Reaffirmed 2026-10-21 | GEM B v0.6.0, true alpha policy v1.4.0 | No newly certified sticker sheet/cutter pass |

## Proof and records
- [Die-cut deployment record](../standards/UNIVERSAL_WHITE_DIECUT_RELEASE_2026-10-21.md), Git commit `7b02761`
- [True-alpha GEM B record](../standards/GEM_B_TRUE_ALPHA_RELEASE_2026-10-21.md), Git commit `42642cf`
- GEM A release `pluginrel_6ad87a17cbf4819190ce776e248dcd19`
- GEM B release `pluginrel_6ad87afc09108191b95b479dbf6a42f4`

## Historical inconsistencies to watch
- Older documents may say v1.1/v1.2, 4×10 or arbitrary sheet dimensions; do not silently adopt them.
- A shared contract document can carry older heading text while containing new `contract_version: 1.3.0`. Resolve both heading and references in next coordinated maintenance pass; record changes.
- The project set README may say 'pending Hero' even if the owner approved Heroes in a later chat. Before modifying source status, collect reliable approval receipts; do not infer release authorization from a picture alone.

## Future change-log entry template
Date / decision ID / requested by / motivation / scope / new standard version / A old→new / B old→new / source commits / deployment release IDs / automated tests / actual cutter test / owner approval / rollback plan.
