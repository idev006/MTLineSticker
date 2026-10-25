# GEM A → GEM B transfer pack (preflight, NOT production authorization)

Project: `SET-KHE-NOI-FIRST-HOME-001` — เข้น้อย กลับบ้านครั้งแรก
Canonical project documents: `sets/SET-KHE-NOI-FIRST-HOME-001/`
Authoritative project document commit at preparation: `90ff0e84b99c53a982ce077783ae7217721b207e`.
Owner-approved Caption Master v0.4.0; 40 frames; 5 sheets each 4 columns × 2 rows; Hero IDs F01/F09/F17/F29.

## GEM B reading sequence
1. Read `README_FIRST.md`, `project.json`, `PACKAGE_MANIFEST.json`, `approvals.json`, `references.json`, `handoff.json`.
2. Read `01_PRODUCT/CAPTION_MASTER.md` together with `frames.json`, `03_FRAMES/FRAME_COMMUNICATION_MATRIX.md` and `03_FRAMES/FRAME_TO_SHEET_MAPPING.md` and verify 40/40 approved literal captions, 40 unique IDs, five 8-frame sheets, 40 unique cells.
3. Read `02_CHARACTER/CHARACTER_BIBLE.md`, `02_CHARACTER/GLOBAL_CHARACTER_LOCKS.md`, `02_CHARACTER/CHARACTER_SHEET_RUNTIME_HANDOFF.md` and `07_REFERENCES/REFERENCE_INDEX.md`. Do not infer identity or image pixels from text.
4. Read `04_PRODUCTION/HERO_PLAN.md`, `04_PRODUCTION/SHEET_FRAME_SPEC.json`, `04_PRODUCTION/ACCEPTANCE_MATRIX.md` and `05_QA/AUTO_REJECT_RULES.md`.
5. Verify the separate canonical receipt `gate-reports/SET-KHE-NOI-FIRST-HOME-001/A1_LATEST.json` **BEFORE** any artwork generation.

## Immutable artistic inputs
- Owner-locked Caption Master v0.4.0, 40 Thai captions; do not paraphrase, regenerate or alter.
- Character Sheet is already marked owner approved. The owner **personally attaches actual Character Sheet and black bag photo to GEM B during A2**; never require binary images or ZIP files in GitHub and never request owner reapproval merely because the binary was not in GitHub.
- Character's anatomical **LEFT HAND** holds the black hard briefcase in the travel-home look. Maintain uniform, expression, physical identity, approved image style, humorous arrogant cadet persona, varied distinct comedic situations.
- The SHA in `approvals.json` is a recorded claim: GEM B must compare with the actual owner-provided binary only if reliable exact bytes/digest are available. Do not self-certify from metadata.
- 40 images, five 4×2 sheets, frame geometry aspect ratio 592×512 equivalent (`width*512==height*592`), RGBA true-alpha, white die-cut ~3–5px around complete silhouette, ~3px opaque black square cutter border, safe zone 15–30px (nominal 20), nominal sheet gutter 15px ±5%; verify each on real output, not via docs.

## Explicit production gate machine
- If A1 receipt missing/FAIL/`validator_executed!=true`/exit!=0, treat status `A1_BLOCKED_RETURN_DOCUMENT_ENGINEERING_TO_GEM_A`; do NOT start Hero generation. Local Python verification is allowed; GitHub Actions are not required. The receipt must contain exact validated commit and SHA256 verification.
- After A1 PASS, begin **A2_RUNTIME_ASSET_READINESS** upon owner attaching actual images to GEM B. Verify identity, technical quality, anatomical LEFT bag and known digest when available.
- Only after both gates and applicable owner Hero authorization generate HERO F09, F01, F17, F29 (actual Hero order from project plan controls if different). Review each Hero with owner as required.
- After approved Heroes, render 40 frames and five 4×2 sheets and perform pixel QA (alpha, die-cut, cutter, Thai caption, consistency, no duplicative meaning/expression/pose/gags). Do not claim image QA PASS until checking actual images.
- GEM B returns only precise upstream document defects to GEM A, detailing file, expected, actual, severity, fix owner, test and pinned SHA.

## Audit finding at this transfer-pack publication
The actual `README_FIRST.md` and `06_HANDOFF/GEM_B_RUNTIME_HANDOFF.md` contain repeated generic text rather than actionable per-section instructions and should be editorially upgraded within GEM A while maintaining a correctly regenerated SHA256 Manifest. There is not yet a demonstrated official A1 validator PASS on the GitHub-pinned real package. Accordingly this pack is **PREPARATORY ONLY** and does not override the FAIL receipt or authorize Hero rendering.
