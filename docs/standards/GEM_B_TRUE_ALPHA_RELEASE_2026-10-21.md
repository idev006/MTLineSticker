# GEM B True Alpha Sticker Sheets — Release 2026-10-21

Status: PRIVATE_PLUGIN_RELEASE_VERIFIED; REAL_ART_AND_CUTTER_INTEGRATION_TEST_NOT_RUN

Owner requires true 100% transparent backgrounds for all new GEM B sticker-sheet master files. Sticker art, intentional white die-cut, and cutter's separate black frame border may be opaque, but every empty pixel and inter-frame gutter must have alpha=0, not a drawn white/gray/checkerboard background.

## Live update
- mt-sticker-gem-b v0.6.0
- Release ID pluginrel_6ad87afc09108191b95b479dbf6a42f4
- Plugin URL https://chatgpt.com/plugins/plugins_6ad84507f928819180ee48d94c5a06be
- Read back after deployment confirmed: knowledge/TRUE_ALPHA_EXPORT_STANDARD_V1_4.md and mandatory rule in skills/produce-stickers/SKILL.md.
- GEM A remains v0.4.0, already requires a transparent background in the shared contract and white die-cut requirements. This release adjusts GEM B's stricter binary enforcement.

## Mandatory QA
Verify saved PNG is RGBA with actual alpha. Entire inter-frame gaps alpha0, empty frame background alpha0, no simulated transparency. Check shape mask manually where needed, white die-cut behind artwork and pixel safe-zone clearance. Preserve cutter markers until downstream export, then remove black frame in cutter. Do not declare transparent/PASS from appearance alone.

## Not yet proved
No particular newly generated art file or cutter integration was tested by this change. A guide-only/plugin-instruction release is not equivalent to a deterministic compositor implementation or actual test PASS.
