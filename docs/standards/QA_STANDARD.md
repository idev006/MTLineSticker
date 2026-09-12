# QA Standard

**Version:** 1.1  
**Scope:** All sticker sets in this repository.

## Gate rule
A set cannot become APPROVED while any blocking QA item fails. Visual attractiveness never overrides a communication, character, typography, or technical defect.

## 1. Character Fit QA
- approved Character Sheet / character SSOT is active during review
- face, haircut, age language, proportions and body language match the locked identity
- signature wardrobe, palette and accessories match the set rules
- no silent adult-to-chibi or other unapproved style conversion
- secondary characters use controlled references when continuity matters

## 2. Communication Fit QA
- one clear primary intent
- caption and image support the same message
- likely chat use case is obvious
- expression and gesture communicate before decorative detail
- key prop clarifies the action rather than competing with it
- candidate passes the 1-second test at chat-preview scale

BLOCK when the artwork reads mainly as a poster, infographic, scene illustration, or decorative image rather than a sendable chat sticker.

## 3. Caption / Typography QA
- exact approved wording
- Thai spelling and diacritics reviewed 100%
- caption hierarchy remains readable after reduction
- no accidental duplicate wording
- AI-rendered Thai is not treated as final unless exactness is verified; use deterministic typography when needed

## 4. Composition / Readability QA
- no clipping of face, hands, gesture, caption or essential props
- silhouette reads clearly
- subject is not too small for chat use
- scene complexity is controlled
- safe margin is preserved for final export
- decorative effects do not merge with the cutout edge

## 5. Technical QA
- final asset is PNG
- real alpha transparency in final sticker image
- current LINE dimensions/file-size requirements satisfied
- even-numbered dimensions when required by platform guidance
- RGB color mode and required resolution baseline
- naming, manifest and sticker ID are correct
- review borders/frame numbers do not appear in final individual assets
- main image, tab icon and submission package complete before release

## 6. Production-source QA
Preferred SSOT:
`approved individual master -> deterministic review sheet -> QA -> LINE export`

Do not treat an AI-generated contact sheet as the final production source unless it was deterministically assembled from approved individual masters.

## 7. Portfolio / Commercial QA
- sticker adds real communication utility or emotional value
- set has sufficient variety
- adjacent stickers do not become near-duplicates
- set remains differentiated from other products in the portfolio
- visual identity supports recognition at small size

## 8. Blocking defects
Any of the following = BLOCK:
- wrong character identity
- wrong/unclear communication intent
- image does not support the caption
- incorrect Thai text
- poor chat-size readability
- important crop or unsafe composition
- non-transparent final background
- current LINE technical noncompliance
- review/contact-sheet artifacts left in final stickers
- unapproved character/style drift

See `docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md` and `docs/standards/STICKER_COMMUNICATION_STANDARD.md`.
