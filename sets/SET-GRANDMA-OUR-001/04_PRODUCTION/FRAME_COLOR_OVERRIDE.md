# SET-GRANDMA-OUR-001 — Project-specific Sticker Frame Color Override

Status: OWNER_APPROVED on 2026-11-06 (Asia/Bangkok), per explicit direct instruction in ChatGPT conversation.
Scope: this set only (all subsequent sheets S01–S05 and Hero working frames). Applies to WORKING cutter frames, not to any individual LINE-ready PNG.
Supersedes ONLY border color in global geometry standard; all other specifications remain unchanged.

- Border color: light green `#9EDB75` / RGBA `(158,219,117,255)`.
- Border width: 3px inward, completely opaque, four sides, sharp square corners (90 degrees), no rounding, antialias, shadows, gradients, gaps or shared borders.
- Working Sticker Frame size: 592×512 px; 4 columns × 2 rows per normal sheet.
- Working Sticker Sheet: 2413×1039 px, zero exterior margin; between frames, gutter 15px, alpha=0 everywhere.
- Binary-alpha rule: every output pixel alpha must be either 0 or 255, never 1..254; any painted pixel fully opaque.
- Die-cut: opaque white silhouette outside actual sticker elements (3–5px) kept clear from cutter border by nominal 20px.
- Do not change approved Character Sheet, Character Bible, Sticker Table, captions, costumes, props, or pose contracts.
- S01 review artwork is a candidate pending Thai text proof, image-conditioned reference provenance and character/pose review; geometric/binary alpha test pass does not mean production release.
- Programmatic cutter: use the exact border RGBA + known cell coordinates and verified transparency/geometry, not hue-detection alone. This applies to project processing and MUST NOT silently rewrite global plugin defaults for other sets.

Owner consent is a specific new exception to the prior global black border rule. If plugin code hard-codes black, project-specific color support must be implemented before full project production QA can be marked PASS.
