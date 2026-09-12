# Character Product Development Framework (CPDF)

**Version:** 1.1  
**Status:** Active project framework  
**Purpose:** Govern development of character-based LINE sticker products as commercial communication products, not illustration collections.

## 1. Core product principle
A LINE sticker is a **communication product**. Artwork exists to make a message, emotion, status, response, request, or action faster and clearer in chat.

Quality is not equal to visual beauty. Product quality combines:
- communication clarity,
- user usefulness,
- character consistency,
- readability at chat size,
- technical/platform compliance,
- visual distinctiveness,
- commercial relevance,
- controlled production quality.

## 2. Product-development flow
1. Opportunity / user need
2. Market and audience research
3. Product Brief
4. Goals / objectives / KPI
5. Positioning / JTBD / use cases
6. Character + Style SSOT
7. Production architecture / caption matrix
8. Hero prototype
9. Hero Fit Gate
10. Full production
11. Frame-level QA
12. Technical LINE compliance
13. Main image / tab / metadata / launch package
14. Submission / release
15. Post-launch measurement and learning

A downstream stage must not begin while a blocking upstream gate is unresolved.

## 3. Communication-first sticker design
Every sticker must have a written communication brief before generation:
- exact caption,
- sender intent,
- likely chat situation,
- emotion/tone,
- visual cue / gesture,
- required prop only when useful,
- forbidden distractions,
- character reference.

**One sticker = one primary communication intent.**

Do not create an illustration first and add a caption afterward.

## 4. The 1-second test
At chat-preview scale, a user should understand the primary intent in approximately one second from the combination of expression, gesture/action, caption, and key prop.

FAIL when:
- the viewer must study the scene,
- props compete with the message,
- the character becomes too small,
- the caption is secondary or hard to read,
- the image is attractive but the communication use case is unclear.

## 5. Character governance
When a Character Sheet is approved:
- it becomes a mandatory active reference,
- locked face, haircut, proportions, wardrobe, palette, signature accessories and age language must be preserved,
- style drift such as adult-to-chibi conversion is a blocking defect unless explicitly approved,
- approved exceptions must be documented.

A successful candidate from a controlled prototype gate may become a **Golden Reference** for subsequent production, but it does not replace the Character Sheet.

## 6. Hero Prototype Gate
Full-set production is blocked until a small representative Hero Set passes.

Hero prototypes must test multiple dimensions such as:
- close/medium communication pose,
- full-body action,
- prop-heavy action,
- emotional/reaction use,
- signature character identity,
- set-specific visual territory.

For a newly corrected or unstable character pipeline, generate **one anchor Hero first**. If it fails character fit, do not batch-generate the remaining Heroes.

## 7. QA layers
Every production candidate is reviewed in this order:
1. **Character Fit** — same person/IP and locked traits.
2. **Communication Fit** — intent is immediate and image supports the caption.
3. **Caption / Typography** — exact wording, correct Thai, readable hierarchy.
4. **Composition / Small-size Readability** — safe area, silhouette, face, gesture and caption survive reduction.
5. **Technical Compliance** — PNG, real transparency, dimensions, file size and current LINE requirements.
6. **Portfolio / Commercial Fit** — useful, non-redundant, differentiated and consistent with the set.

Any blocking failure prevents approval regardless of visual attractiveness.

## 8. Review sheet versus production asset
A review/contact sheet is a QA artifact only. It may include frame borders, numbers and annotations.

The production SSOT is the **individual sticker master**. Final LINE submission assets must never depend on slicing a visually generated sheet unless the sheet was assembled deterministically from approved individual masters.

Preferred pipeline:
`individual master -> deterministic review sheet -> QA -> LINE export`

Not preferred:
`AI-generated review sheet -> crop into final stickers`

## 9. Typography control
AI-rendered Thai text is candidate-level only unless verified exactly. Final typography must be proofread 100%. When reliable exact wording cannot be guaranteed by generation, add text using a deterministic production layer.

## 10. Platform compliance
Project standards must be checked against the latest official LINE Creators Market creation and review guidelines before submission. Official platform rules override internal assumptions.

## 11. Corrective learning rule
When a gate failure reveals a process weakness:
1. reject the defective asset,
2. record root cause,
3. update the relevant framework/standard,
4. update the set-specific documents,
5. regenerate only after the preventive control is in place.

This prevents the same defect from propagating across a full set.

## 12. Evidence required to unlock full production
- approved Character Sheet / Style SSOT,
- locked production/caption matrix,
- approved Hero Golden Reference(s),
- Hero Fit Gate result = PASS,
- current QA checklist,
- current production/technical spec.

See also:
- `docs/standards/STICKER_COMMUNICATION_STANDARD.md`
- `docs/standards/LINE_STICKER_SPEC.md`
- `docs/standards/QA_STANDARD.md`
- `docs/standards/VISUAL_STYLE_GUIDE.md`
