# SET-008 — PRODUCTION SPEC v1.0

## Output Model
Full set target: **40 LINE Stickers**

## Sheet Workflow
เพื่อการตรวจงานภายใน:
- 4 sheets × 10 frames
- grid 5 columns × 2 rows
- frame working canvas: 512 × 512 px
- margin between outer sheet and content: 20 px
- padding within each frame: 20 px
- transparent background
- review frame border may be used on sheet preview only; do not bake border into final sticker export unless specifically approved

## Sticker Artwork
- no-text / gesture-first
- polished semi-realistic cartoon
- recognizable likeness
- white sticker outline for separation from chat backgrounds
- gesture and face must remain readable after downscaling
- avoid fine detail that disappears at small size

## Composition
- use medium/full body depending on intent
- crop must never remove gesture-critical hands or props
- keep safe empty space around silhouette
- props only when needed to disambiguate intent

## Consistency
Every frame must be compared against `CHARACTER_SHEET_ACTIVE` once approved.
Critical consistency fields:
- face/head silhouette
- hairstyle
- visual age
- body build
- jacket construction and colors
- illustration style

## No-Text Policy
No caption by default. Minimal universal symbol icons such as ✓, !, ? may be used sparingly if they improve readability.

## Asset Workflow
1. Character Sheet Candidate
2. Owner approves `CHARACTER_SHEET_ACTIVE`
3. Hero Set 12
4. Owner approves Hero
5. Full production sheets 1–4
6. QA
7. Crop/export final LINE assets

## LINE Export Note
Final marketplace export dimensions and package assets must follow the repository's current LINE platform standard documents at export time. Do not assume working-frame 512×512 is the final LINE submission dimension; it is the internal generation/review frame.

## File Hygiene
Do not commit generated production PNGs, temp crops, ZIP exports, logs or cache files to source-control paths unless repository policy explicitly designates an approved asset path and the owner requests it. Documentation remains authoritative in `ssot/`.
