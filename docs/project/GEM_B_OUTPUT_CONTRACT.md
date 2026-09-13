# Gem B Output Contract

**Version:** 1.1  
**Status:** Active  
**Applies to:** Gem B — Sticker Visual Producer

## Purpose
Define the minimum input preflight and visual outputs Gem B must produce, including controlled Hero review before full-set production.

## Input preflight
Gem B must not start visual production merely because files were supplied.

Minimum normal input requires:
- Gem A package status `READY_FOR_GEM_B`,
- complete structured Gem A Production Document Package or its extracted equivalent,
- approved `CHARACTER_SHEET_ACTIVE`,
- approved Style SSOT when separate,
- Golden Reference when applicable,
- no unresolved blocking open item.

Gem B must validate Package/Handoff manifests, Character authority, caption/frame mapping, Hero Plan, Sheet Plan and QA/auto-reject rules before production.

Raw source images/video, a Character Sheet generation prompt, or an unapproved Character Sheet candidate do not replace `CHARACTER_SHEET_ACTIVE` unless an explicit Product Owner exception is documented.

## Core rule
Gem B does not jump directly from approved documents to full-set production when a Hero Gate is required.

The standard sequence is:

`READY_FOR_GEM_B -> HERO_PRODUCTION -> READY_FOR_VISUAL_OWNER_REVIEW -> OWNER_APPROVAL -> FULL_PRODUCTION_UNLOCKED -> FULL_PRODUCTION -> READY_FOR_ENGINE`

## Phase A — Hero Review Output
When the Production Document Package requires a Hero Gate, Gem B must first produce a complete Hero Sticker Sheet for owner review.

Minimum Hero Output Package:
- `HERO_STICKER_SHEET` — one sheet containing every required Hero Frame,
- `HERO_FRAME_INDEX` — Frame ID, caption, intent and sheet position for every Hero,
- `CHARACTER_REFERENCE_USED` — exact `CHARACTER_SHEET_ACTIVE` identity/version,
- `GOLDEN_REFERENCE_USED` — when applicable,
- `HERO_VISUAL_QA` — Character fit, communication fit, composition, readability and caption mapping result,
- `HERO_REVIEW_STATUS` — `READY_FOR_VISUAL_OWNER_REVIEW`, `BLOCKED`, or `RETURN_TO_GEM_A`.

The Hero Sheet must contain all Hero Frames declared by Gem A. Its geometry must be explicit and every cell must be equal-size with no cross-frame bleed.

Hero selection is defined upstream by Gem A and should test representative and risky dimensions of the set rather than merely early/easy Frames.

## Hero Review objective
The Hero Sheet exists so the Product Owner can validate the visual direction before scale-up, including:
- Character identity and resemblance against `CHARACTER_SHEET_ACTIVE`,
- rendering/style direction,
- expression and pose language,
- mandatory/optional Character trait handling,
- communication clarity,
- caption-image fit,
- typography treatment,
- prop density,
- overall commercial look and feel.

Hero approval is a visual-direction decision, not final LINE technical certification.

## Phase B — Full Production Output
Full production may start only after the Hero Gate has passed and owner approval has been recorded when the package requires it.

For a standard 40-sticker product, minimum Full Production Output is:
- `STICKER_SHEET_01` — 10 Frames,
- `STICKER_SHEET_02` — 10 Frames,
- `STICKER_SHEET_03` — 10 Frames,
- `STICKER_SHEET_04` — 10 Frames,
- `SHEET_MANIFEST` — Sheet ID, Frame IDs, captions, ordering, grid, logical Frame size and references used,
- `VISUAL_QA_REPORT` — per-Frame and per-Sheet result,
- `PRODUCTION_STATUS` — `READY_FOR_ENGINE`, `BLOCKED`, or `RETURN_TO_GEM_A`.

Default profile unless set SSOT overrides it:
- 10 Frames per production Sheet,
- Grid 5 columns x 2 rows,
- logical Frame size 512 x 512 px,
- logical Sheet size 2560 x 1024 px,
- row-major order,
- no cross-frame bleed.

## Full-set acceptance
Gem B may emit `READY_FOR_ENGINE` only when:
- every required Frame exists,
- all Frame IDs reconcile with the approved Production Document Package,
- Character fidelity passes against the active Character Sheet across the set,
- captions and intents map correctly,
- no blocking visual defect remains,
- all required Sheets have valid declared geometry,
- Sheet manifest is complete,
- output is suitable for deterministic downstream processing.

## Failure and return rules
If a visual defect belongs to Gem B, Gem B corrects it before handoff.

If Gem B discovers an upstream defect such as premature `READY_FOR_GEM_B`, conflicting captions, missing Frame intent, unresolved Character authority, unsupported Character constraints or strategy ambiguity, it returns the work to Gem A with evidence and does not invent a replacement decision.

## Output authority boundary
Gem B owns visual master quality only. It does not certify final LINE platform compliance and does not modify the existing Python application, engine, scripts, validators, packagers or deterministic processing logic.