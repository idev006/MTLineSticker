# Universal White Die-Cut Standard — Plugin Release Evidence
Date: 2026-10-21
Status: OWNER_APPROVED / BOTH PRIVATE PLUGINS UPDATED AND VERIFIED / PIXEL AND CUTTER INTEGRATION TESTS NOT RUN

## Universal obligation for ALL new sticker sets
- Each sticker artwork shall include a solid white (#FFFFFF; alpha 255) die-cut underlay ~3–5px outside its silhouette (not a rectangular canvas).
- Outline follows the complete art contour including intentional effects, props, shadows. Handle disconnected components deliberately and without accidental gaps.
- The white die-cut lies behind artwork, counts as sticker content for safe-zone validation, and must not touch the black frame boundary.
- The remainder of background outside the sticker is RGBA alpha=0. A faux transparency checkerboard does not qualify.
- Distinguish ~3–5px white silhouette from the ~3px black opaque production FRAME boundary; the cutter removes the black frame and preserves the white die-cut.
- Previous shared 4x2, 592:512 ratio, 15px gutter +/-5%, selected internal 15–30px safe zone +/-5%, apply unchanged.

## Verified deployed private plugin releases
- GEM A v0.4.0, release pluginrel_6ad87a17cbf4819190ce776e248dcd19, https://chatgpt.com/plugins/plugins_6ad844f4cd8c8191aa0282099b84bb14
- GEM B v0.5.0, release pluginrel_6ad87a25f98881918569c4df8f518553, https://chatgpt.com/plugins/plugins_6ad84507f928819180ee48d94c5a06be
- Both installed releases were read back: knowledge/WHITE_DIECUT_STANDARD_V1_3.md exists; skill references it; shared contract_version 1.3.0 confirmed.
- GEM A specifies mandatory contour/die-cut policy in packaging and handoff. GEM B must execute deterministic alpha mask-based compositing/validation where available.
- The two plugin instruction releases are updated; this does NOT certify a specific sheet output, deployed deterministic mask engine, or the legacy ChatGPT Work cutter compatibility.

## Next validation
Run actual frame-mask pixel tests, alpha tests, safe-zone geometry checks, and cutter integration before declaring sheets production-ready.
