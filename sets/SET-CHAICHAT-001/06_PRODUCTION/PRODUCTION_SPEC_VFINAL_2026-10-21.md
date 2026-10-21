# CHAICHAT #1 — Production Specification vFinal
Date: 2026-10-21
Status: PRODUCT_OWNER_APPROVED
Scope: five PNG master contact sheets as input for the existing ChatGPT Work sticker cutter; NOT direct LINE upload files.

## Sheet contract
- 40 unique frames F01-F40; 5 sheet PNGs, 8 frames per sheet, 4 columns x 2 rows.
- Mapping S1 F01-F08, S2 F09-F16, S3 F17-F24, S4 F25-F32, S5 F33-F40.
- Per-frame rectangle 592 x 512 pixels, 90-degree corners, independent border; no outer sheet border.
- Per-frame border: solid #000000, thickness exactly 3 pixels, alpha=255, raster-aligned, drawn inward; no antialiasing of the black frame boundary.
- Clear transparent space between *outer edges* of adjacent frames: exactly 15 pixels, horizontally and vertically. These margins are distinct from the sticker safe zone.
- Production-origin convention for deterministic 4x2 montage: top-left frame begins at (0,0); frame col c, row r starts x=c*(592+15), y=r*(512+15), c=0..3, r=0..1. Therefore sheet raster = 2413 x 1039 pixels, with zero outer-sheet margin. Any alternative outer-sheet margin or cutter coordinate contract requires a cutter compatibility test and owner decision.
- Transparent background: RGBA PNG; alpha=0 in all unoccupied sheet/frame background regions and all inter-frame gap pixels. The 3px black frame border is intentionally opaque and must be removed by the cutter. White silhouette die-cut, when present, is an opaque sticker component, not the sheet background.
- Sticker safe zone inside each frame: permitted minimum 15px, preferred target 20px, configurable within owner-approved 15..30px, measured from INSIDE EDGE of the 3px border. The entire sticker composite (including fingers, hair, props, effects, shadows, garment text, and die-cut) must remain inside it.
- Character/style source: latest owner-approved attached Character Sheet; navy puffer, white backwards cap, gray inner layer, dark pants, white trainers; only CHAICHAT garment branding permitted; no floating captions.
- Preserve original transparency: never flatten onto white, draw checkerboard into image, or use visually simulated alpha.

## Acceptance gates / deterministic QA
1. PNG decodes as RGBA; dimensions 2413x1039 under specified zero-outer-margin grid.
2. Eight rectangles at exact coordinates and size; no omitted/duplicate frame IDs.
3. Each border black opaque and exactly 3px; all 15px inter-frame gap pixels alpha=0, no other content.
4. For non-border regions, background alpha=0; sticker alpha and edges visually reviewed; no accidental white canvas; die-cut remains inside safe area.
5. Frame content bounding boxes, after excluding border, remain at least 15px inward from border's inner edge; target 20px. Fail any breach.
6. Face, costume, CHAICHAT typography, gesture, no-caption, no clipping inspected per frame.
7. Perform a real cutter integration test before declaring CUTTER_COMPATIBLE or PRODUCTION_READY. A rendered preview or image model assertion does not constitute technical QA.

## Scope and compatibility
This document supersedes generic golden-standard 5x2/10-per-sheet and 5px border settings FOR THIS SET. Sheet-master pixel size differs from LINE upload limits; the existing cutter must extract and resize individual outputs after border removal. Existing cutter assumptions about border=5, gap=24, layout=5x2, or sheet dimensions must be checked and updated only after inspecting cutter code. Hero four frames were approved visually, not certified for geometry/alpha.
