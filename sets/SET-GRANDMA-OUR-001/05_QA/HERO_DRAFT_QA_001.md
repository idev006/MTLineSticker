# Hero 2x2 Draft QA — SET-GRANDMA-OUR-001

Status: DRAFT_QA_FAIL / OWNER_HERO_APPROVAL_PENDING. Do NOT render remaining 36 stickers.

## Approved reference
Character Sheet: CS-GRANDMA-OUR-001 v0.1; local SHA-256: 45526a3c7e1fb10ae98ccb7a1817c2e65fb589040a4b68fd5c8dacc9673613f7. Confirmed actual local bytes matched the reference record before generation; prompt-image referent was supplied in conversation. This is not automated proof of tool-internal image conditioning.

## Locked plan
Source GitHub commit: df2b8f5450e6842b926d24b4ed0030eeac1fafef. Frames row-major: F01, F05, F16, F34. Sticker Table v1.0.0 and Caption Master OWNER_LOCKED. Owner approved this Hero PLAN, not output image.

## Observed output
Generated draft: a_bright_ultra_detailed_3d_chibi_sticker_sheet_2.png (local session asset). Dimensions observed via Pillow: 1357×1159, mode RGBA, alpha extrema 0–255, 2,797,677 bytes. Corners RGBA (0,0,0,0). Transparent pixel fraction ~6.80%; most other pixels semi-transparent. No verified deterministic 3px square black frame borders or 15px transparent gutters. Nominal 2x2 target 1199x1039 cannot be inferred from this raw draft. Real diecut thickness and safe zone NOT MEASURED; alpha-composition FAIL for production as-is.

## Visual observations
- F01: yellow costume, friendly single-hand greeting; flowers present. Thai caption visually present; exact glyph comparison NOT CERTIFIED.
- F05: blue costume, happy waving both hands; flower decoration appears in addition to intended sparkle. Caption visually present, exact glyph NOT CERTIFIED.
- F16: pink costume, hands held to heart/chest; visual identity reasonably similar subjectively; exact Unicode image text NOT CERTIFIED.
- F34: red costume and affectionate pose, but holding a solid large heart instead of the exact locked 'กรอบรูปหัวใจ' (heart-shaped photo frame): **FAIL — pose/prop deviation**.
- Character look broadly consistent to unaided viewing; no measured identity score or independent human acceptance.

## Outcome and remediation
Structural source QA: PASS (40 frames unique, 40/40 exact caption master, same Character Sheet ref) from GitHub verification before rendering.
Rendered visual QA: FAIL due to F34 prop drift. Technical sheet QA: FAIL / NOT READY due to dimensions, no cutter frames, gutter, diecut measurement and excessive semitransparent artwork. Thai lettering exactness: NOT VERIFIED.
Next: seek owner direction on draft / targeted F34 correction and deterministic compositing while preserving approved Sticker Table, then recheck actual pixels. Hero Artwork approval remains PENDING. No extra batch rendering.
