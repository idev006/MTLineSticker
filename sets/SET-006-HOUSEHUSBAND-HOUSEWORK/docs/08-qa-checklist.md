# 08 — QA Checklist

**Version:** 1.1  
**Applies to:** SET-006-HOUSEHUSBAND-HOUSEWORK

## A. Character Fit QA — every frame
- [ ] approved Character Sheet is active during generation/review
- [ ] H01 Golden Reference is used as the rendering/communication anchor
- [ ] clean-shaven adult male identity preserved
- [ ] police/military very-short haircut + sharp hairline preserved
- [ ] same facial proportions / same adult age language
- [ ] athletic adult body language; no unapproved chibi proportions
- [ ] navy shirt unless approved task adaptation
- [ ] black shorts when visible
- [ ] orange shoes when visible
- [ ] black tactical watch on left wrist
- [ ] crossbody bag used only when it supports, or at least does not obstruct, the action

## B. Communication Fit QA
- [ ] one primary intent only
- [ ] intended chat situation is written and obvious
- [ ] image strengthens the caption rather than decorating it
- [ ] expression + gesture/action communicate quickly
- [ ] passes **1-second test** at chat-preview scale
- [ ] key prop clarifies the action
- [ ] props/scenery do not overwhelm character or caption
- [ ] candidate reads as a sendable sticker, not a poster/infographic/scene illustration

## C. Caption / Typography QA
- [ ] exact approved Thai wording
- [ ] Thai spelling and diacritics correct 100%
- [ ] caption matches Production Sheet
- [ ] readable after reduction to LINE delivery size
- [ ] no accidental duplicate wording
- [ ] no derogatory / humiliating tone inconsistent with brand
- [ ] AI-rendered Thai is not considered final until exact wording is verified
- [ ] use deterministic text layer when exact generation typography cannot be guaranteed

## D. Composition / Small-size QA
- [ ] content inside safe area
- [ ] no important crop of head, face, hands, action, caption or essential prop
- [ ] silhouette readable
- [ ] face/expression remains readable at chat size
- [ ] action remains readable at chat size
- [ ] no unnecessary micro-props or scene clutter
- [ ] decorative effects do not create ambiguous cutout edges

## E. Technical QA
- [ ] individual master PNG exists
- [ ] RGBA / real transparent background
- [ ] master retained at high resolution
- [ ] final LINE export compliant with current official requirements
- [ ] dimensions even-numbered when required
- [ ] file size within platform limit
- [ ] review-sheet border/number absent from final individual asset
- [ ] naming / manifest / ID correct

## F. Production-source QA
- [ ] individual sticker master is SSOT
- [ ] review sheet is assembled from approved individual masters
- [ ] no AI-generated multi-panel sheet is used directly as final slicing source unless exact geometry and per-frame QA are deterministically guaranteed
- [ ] every frame has its own acceptance record

## G. Commercial / Portfolio QA
- [ ] use case is practical and likely to be sent
- [ ] at least 2 brand pillars visible where appropriate
- [ ] no obvious near-duplicate pose/message within adjacent stickers
- [ ] sticker adds communication or emotional value
- [ ] housework theme remains distinct from Set 1
- [ ] set retains enough visual/action variety

## H. Gate blockers
Any of these = BLOCK:
- wrong character face/hair/age/proportion
- unapproved chibi conversion
- unclear communication intent
- image and caption disagree
- fails 1-second test
- incorrect Thai text
- poor small-size readability
- content cropped
- non-transparent final background
- LINE technical noncompliance
- contact-sheet artifacts in final asset
- secondary-character inconsistency affecting continuity

## I. Hero-specific rule
H02–H06 must be produced and accepted as **standalone individual Hero masters**. A combined six-Hero review sheet alone cannot satisfy Hero Fit Gate evidence.

See:
- `reviews/HERO-FIT-GATE.md`
- `../../../../docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`
- `../../../../docs/standards/STICKER_COMMUNICATION_STANDARD.md`
