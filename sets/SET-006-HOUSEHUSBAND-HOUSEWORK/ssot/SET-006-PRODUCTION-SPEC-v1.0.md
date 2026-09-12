# SET-006 Production Spec v1.1

## Production principle
Every deliverable is a **LINE communication asset**. Artwork must be designed from the approved caption/use case outward; do not treat the task as creating a standalone illustration.

Mandatory references:
- approved “พ่อบ้านสายวินัย” Character Sheet
- `docs/standards/STICKER_COMMUNICATION_STANDARD.md`
- `docs/standards/LINE_STICKER_SPEC.md`
- SET-006 Visual Style Application and QA Checklist

## Per-sticker communication brief — required before generation
Each sticker must record:
- exact caption
- sender intent
- likely chat situation
- primary expression
- primary gesture/action
- required prop(s), if any
- forbidden visual traits / failure conditions

No candidate should be generated without this brief.

## Character lock
- adult male, approx. 30–40
- clean-shaven
- very short police/military-inspired haircut with neat sharp hairline
- athletic adult proportions; NO chibi/childlike redesign
- navy T-shirt
- black shorts
- vivid orange shoes when visible
- black tactical watch on LEFT wrist
- black crossbody bag only when it does not obstruct the action
- sunglasses optional

Character mismatch = reject candidate before other aesthetic review.

## Review sheet
- 4 sheets
- 10 stickers per sheet
- grid 2 rows × 5 columns
- logical master frame: 512×512 px
- review sheet logical size: 2560×1024 px
- transparent background
- black frame lines allowed **only for review sheet**
- frame number allowed **only for review sheet**
- artwork must not cross frame boundaries
- safe padding target: 20 px at 512 master scale

Review sheets are QA/contact sheets and are not the source of truth for final upload assets. Individual sticker masters are the production SSOT.

## Individual master
- one PNG per sticker
- transparent RGBA
- 512×512 master canvas (internal production master)
- no black square frame in final art
- no review number in final art
- face/expression + main action/gesture must remain readable after reduction
- props limited to those that improve communication speed

## LINE export
Before submission, export each sticker to a size compliant with the latest official LINE static-sticker guideline. Current working square target: **320×320 px transparent PNG**, subject to current official maximum limits and rules.

Re-check official requirements on submission day, including allowed quantity, dimensions, file size, PNG/transparency, RGB, even dimensions, margin guidance and review policy.

## Naming
- `SET006-001.png` … `SET006-040.png`
- `SET006-main.png`
- `SET006-tab.png`
- Review sheets: `SET006-sheet-01-review.png` etc.

## Typography
Final Thai text must be proofread 100%. AI-rendered Thai text is a candidate only until spelling and wording are deterministically verified.

## Acceptance blockers
Reject a candidate when any of these occurs:
- wrong character identity / hair / face / proportions
- chibi redesign
- communication intent unclear
- image merely decorates caption rather than supporting it
- poster/infographic/environmental scene instead of sticker art
- caption typo/wrong wording
- poor thumbnail readability
- important crop/safe-area violation
- final background not truly transparent
- current LINE technical noncompliance

## Asset retention
Retain:
- 512 master PNG for each sticker
- final LINE PNG
- communication brief / caption mapping
- review sheet
- approved Hero references
- QA report and gate result
