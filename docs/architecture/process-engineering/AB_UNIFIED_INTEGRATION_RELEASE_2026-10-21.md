# GEM A + GEM B Coordinated Plugin Release — 2026-10-21

Status: PLUGIN_RELEASES_UPDATED / INTEGRATION_TEST_NOT_RUN
Owner instruction: harmonize both plugins with seven approved expert review roles and shared universal production contract.

## Verified live plugin releases
- GEM A `mt-sticker-gem-a` v0.2.0; release `pluginrel_6ad861d72a808191afb960282651e247`
- GEM B `mt-sticker-gem-b` v0.3.0; release `pluginrel_6ad861e5e5888191a1b4f8806a175fd6`
- Both contain `knowledge/SHARED_HANDOFF_CONTRACT.md` v1.1.0, verified by re-reading release files after update.

## Shared boundary
- GEM A owns requirements, approved Character authority, communications matrix, frame IDs and mappings, source references, package and Gate A.
- GEM B validates package and owner-authorized runtime reference, produces Hero and batch visuals and renders deterministic sticker sheets, checks geometry/alpha and prepares cutter handoff.
- Owner approvals for Character/Hero/release are never automatic.
- Seven role lenses defined in `docs/architecture/process-engineering/team/TEAM_CHARTER.md` guide reviews, not separate real staff.

## Universal all-set sheet spec
8 frames per sheet, 4x2; 592x512 frame; 3px inward opaque black frame border; 15px true-alpha gutter; sticker safe clearance >=15px from inner border, target 20px, configurable up to 30px; RGBA PNG with alpha0 background. For complete 8-frame zero-outer-margin output sheet: 2413x1039 pixels. Cutter must remove border; sticker sheets are not LINE upload files.

## Handoff
Contract v1.1.0: set and run IDs, git source revision, character reference/owner approval, reference index, 40 unique frames for 40-set, Hero IDs, per-sheet map, universal spec version, gate and QA evidence. On conflict return to GEM A; do not silently rewrite approvals/creative intents.

## Not yet verified
No end-to-end live GEM A -> GEM B handoff regression fixture or ChatGPT Work cutter integration test executed. No proof of pixel-correct outputs or LINE-ready assets yet. Require actual binary and test evidence before claiming full production readiness.

## Historical content
Legacy process-engineering documents that say plugin implementation had not begun remain historical. The two versions above are the newer verified private plugin releases; repository deployment instructions may still be older and require future migration/reconciliation.
