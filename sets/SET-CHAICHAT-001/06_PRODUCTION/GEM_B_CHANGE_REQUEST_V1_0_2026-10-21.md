# MT Sticker GEM B — Change Request v1.0
Date: 2026-10-21
Status: OWNER_APPROVED_REQUIREMENTS / IMPLEMENTATION_PENDING
Project: CHAICHAT #1 (SET-CHAICHAT-001)
Authority: [Production Specification vFinal](../06_PRODUCTION/PRODUCTION_SPEC_VFINAL_2026-10-21.md)

## Required plugin changes
1. Load per-set output specification from GitHub SSOT rather than hardcoded generic 5x2/10-frame/5px settings.
2. Implement deterministic sheet compositor separate from image generation: render individual approved character poses into 592x512 transparent frame canvases; add solid 3px black borders and 15px alpha-zero inter-frame gaps; assemble exactly 4 columns by 2 rows per sheet.
3. Output one RGBA PNG sheet per batch of 8; five total, each dimension 2413x1039 pixels under zero-outer-margin convention. Never trust generative rendering for pixel-perfect geometry, border or alpha.
4. Enforce sticker safe zone from inside border: >=15px, preferred 20px, configurable <=30px, including die-cut, shadows, props, hair, and hands.
5. Verify via deterministic pixel-level tests: 8 rects, border=3px #000000 alpha255, gap 15px alpha0, RGBA mode, exact sheet size, content bounding-box constraints, no duplicated/missing IDs.
6. Inspect frame-level face DNA, gestures, outfit, CHAICHAT garment lettering, absence of speech captions and clipping. Any failure blocks sheet approval and triggers correction.
7. Cutter compatibility: inspect existing ChatGPT Work cutter code/interfaces, verify coordinates, border removal, and transparent alpha preservation with an actual 8-frame integration fixture; do not assert success without test evidence.
8. Persist QA evidence and owner review status in SSOT; image binaries may remain attached in runtime by owner authorization, no mandatory GitHub upload.
9. Version plugin instruction/playbook/tests; add fixture with transparent margin and 3px border. Do not alter global plugin defaults for other sets without backward compatibility tests.
10. Proceed sheet-by-sheet and verify each artifact before declaring full 40/40 ready.

## Acceptance criteria
- All 5 sheets meet the geometry/alpha spec; 40 unique identities/actions and no text overlays.
- 100% of frame boundary/gap/safe area pixel tests pass; manual visual review recorded per frame.
- End-to-end cutter trial successfully yields eight clean cropped transparent assets from one production sheet, correctly excluding frame borders.
- No fabricated test PASS: report NOT RUN until actual tests.
- No claim of ZIP or LINE readiness before individual export and LINE checks.

## Implementation status
Requirements and project-specific spec approved. **Plugin code/instructions, compositor, validators, and ChatGPT Work cutter have NOT been changed or tested by this document.**
