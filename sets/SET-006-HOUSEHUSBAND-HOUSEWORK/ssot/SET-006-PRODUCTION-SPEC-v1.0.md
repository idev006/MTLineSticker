# SET-006 Production Spec v1.2

**Status:** Active production specification  
**Supersedes:** v1.1 working rules  
**Set:** SET-006-HOUSEHUSBAND-HOUSEWORK

## 1. Core production principle
SET-006 is a LINE sticker communication product. Every sticker must be produced from a communication brief and approved as an individual sticker master before it is treated as production-ready.

## 2. Per-sticker preflight — mandatory before generation
Each sticker must define:
- sticker ID
- exact caption
- sender intent
- likely chat situation
- emotion/tone
- primary visual cue / gesture/action
- required prop, if any
- forbidden distractions
- approved Character Sheet reference
- H01 Golden Reference for rendering/communication consistency

No generation should begin when these fields are undefined.

## 3. Individual master — production SSOT
The source of truth is **one approved PNG per sticker**.

Working master requirements:
- 512×512 px internal master canvas
- RGBA / real transparency in approved production master
- no black review frame
- no review number
- no contact-sheet annotation
- no scene background unless specifically approved and still compatible with sticker readability
- content kept inside safe area
- typography exact and proofread

Naming:
- `SET006-001.png` … `SET006-040.png`

## 4. Hero Golden Reference
H01 / #01 “ล้างจานอยู่ครับ” approved by the owner is the SET-006 Hero Golden Reference.

It anchors:
- adult face/proportions,
- very-short military/police-inspired haircut,
- navy shirt,
- black shorts where visible,
- orange-shoe signature where visible,
- black tactical watch on left wrist,
- restrained use of black crossbody bag,
- bold Thai caption hierarchy,
- simplified sticker-first housework storytelling.

The Golden Reference does not replace the Character Sheet; both must be used together.

## 5. Review/contact sheets
Review sheets are QA artifacts only.

Planned full-set review architecture:
- 4 sheets
- 10 stickers per sheet
- 2 rows × 5 columns
- logical master frame: 512×512 px
- logical review sheet size: 2560×1024 px
- black frame lines and frame numbers allowed only for review sheets
- no artwork may cross frame boundaries

Preferred creation method:
`approved individual masters -> deterministic assembly -> review sheet`

Do **not** use an AI-generated multi-panel sheet as the authoritative source for final slicing when geometry, transparency, typography, or per-frame QA cannot be guaranteed.

## 6. Safe area
Internal 512 master target:
- minimum controlled safe padding target: 20 px
- preserve additional breathing room when action/typography allows

Before LINE export, verify effective trimmed margin against the latest official guideline; current project baseline recognizes LINE's recommendation of around 10 px between trimmed content and image edge.

## 7. Small-size / 1-second test
Every approved master must be reviewed after reduction to near-delivery/chat-preview scale.

PASS requires:
- face/expression still readable,
- action/gesture obvious,
- caption hierarchy readable,
- intended message understood in about one second,
- key prop recognizable without scene study.

## 8. Typography
Final Thai text must be exact and proofread 100%.

AI-rendered Thai is candidate-level only until exactness is verified. If exact generation text cannot be guaranteed, apply the caption through a deterministic typography layer.

## 9. LINE export
Before submission, verify the latest official LINE Creators Market requirements. Official rules override this document if changed.

Current working baseline:
- sticker PNG, transparent background
- maximum 370×320 px
- working square export target may be 320×320 when composition suits it
- even-numbered width/height
- RGB, at least 72 dpi
- ≤1 MB per sticker
- Main image 240×240
- Chat thumbnail 96×74

Do not upscale a weak source merely to hit a target size.

## 10. Hero production gate
Sequence:
1. H01 — approved / Golden Reference
2. H02 standalone master -> QA -> approval
3. H03 standalone master -> QA -> approval
4. H04 standalone master -> QA -> approval
5. H05 standalone master -> QA -> approval
6. H06 standalone master -> QA -> approval
7. deterministic Hero review sheet from accepted masters
8. six-Hero consistency audit
9. owner Hero Fit Gate approval
10. only then unlock full 40 production

A combined Hero sheet cannot substitute for accepted individual masters.

## 11. Full production
After Hero Fit Gate PASS:
- produce individual stickers in controlled batches
- run frame-level QA before marking approved
- assemble review sheets from accepted masters
- correct only failed frames instead of unnecessarily regenerating passed frames

## 12. Asset retention
Retain:
- approved Character Sheet
- H01 Golden Reference
- all approved 512 masters
- final LINE PNGs
- deterministic review sheets
- Main image and tab icon
- QA/gate reports
- revision history

## 13. Blocking defects
Any of the following blocks production acceptance:
- character drift
- unapproved chibi conversion
- unclear chat intent
- scene/illustration complexity that weakens sticker communication
- wrong Thai text
- failure of 1-second/small-size test
- important crop
- missing real alpha transparency
- review artifacts in final image
- current LINE technical noncompliance

See:
- `../../../docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`
- `../../../docs/standards/STICKER_COMMUNICATION_STANDARD.md`
- `../docs/08-qa-checklist.md`
- `../reviews/HERO-FIT-GATE.md`
