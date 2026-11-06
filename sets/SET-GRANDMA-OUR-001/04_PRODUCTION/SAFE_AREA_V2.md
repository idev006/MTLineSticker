# Safe Area v2 — SET-GRANDMA-OUR-001

Status: Applied for next S01 remake following Product Owner's request on 2026-11-06 to implement the proposed Safe Composition / Auto-Fit improvement. These are **internal QC criteria**, not LINE official safe-margin rules.

- Inner-border-to-outermost-visible-diecut minimum: **40 px** on each of four sides (hard gate).
- Generation target: **48 px** from the inner side of the cutter border after complete art + caption + props + decorations + white diecut are included.
- In pre-diecut 592x512 RGBA art, reserve **56 px from canvas edge** (3px border + up to 5px diecut + 48px production target); accounting must not double-count diecut when inspecting final postprocessed frame.
- Smart-fit may proportionally shrink/recenter unframed artwork without upscaling or cropping elements, no alpha 1..254. If required scale is below 0.70 or text becomes illegible, block and regenerate/recompose instead. No unconditional automatic acceptance after rescaling.
- Approved light-green cutter `#9EDB75`, 3px square 90-degree four-sided frame; 15px fully transparent gutters; working frame 592x512, 4x2 sheet 2413x1039.
- Strict binary alpha: art alpha 255, empty alpha 0, no intermediate values. White diecut opaque 3–5px.
- Approved Character Sheet visual input and SSOT-locked Caption Master & Sticker Table remain unchanged. Record source/target frame SHA-256 and measured side clearances for each frame. Require exact glyph, likeness and layout QA separately.
- S01 is NOT automatically owner approved. Do not proceed to S02–S05 from code-only test success.

Plugin reference: MT Sticker GEM A v0.36.0 `knowledge/SAFE_COMPOSITION_V2.json`, `scripts/safe_composition.py`.
