# Hero to Full Production Gate

**Version:** 1.0  
**Status:** Active

## Purpose
Prevent premature full-set production by requiring an explicit Hero review and approval checkpoint before Gem B expands into the complete sticker set.

## Gate sequence

`Gate A PASS -> Gem B Hero Production -> Hero QA -> Owner Hero Review -> Hero Gate PASS -> Full Production Unlocked -> Gem B Full Production -> Gate B PASS`

## Hero Gate required inputs
- approved Production Document Package,
- approved Character Sheet / active Character visual reference,
- declared Hero Frame IDs,
- exact Hero captions and intents,
- Hero Sheet geometry,
- visual QA criteria,
- Golden Reference when applicable.

## Hero Gate PASS criteria
PASS requires:
- every declared Hero appears on one Hero Sticker Sheet,
- Hero Sheet geometry and Frame mapping are explicit,
- Character identity is consistent with the approved Character Sheet,
- required visual direction is coherent across all Heroes,
- each Hero communicates its approved intent quickly,
- caption-image relationships are correct,
- no blocking visual defect remains,
- owner acceptance is recorded when owner review is required by the package.

## Hero Gate outcomes
- `PASS` -> set `FULL_PRODUCTION_UNLOCKED` and allow Gem B to create the full production Sheets.
- `CORRECTION_REQUIRED` -> correct failed Hero Frames only, rebuild/review the Hero Sheet, then re-enter this Gate.
- `RETURN_TO_GEM_A` -> use when the defect is upstream product/documentation ambiguity.
- `BLOCKED` -> production must not expand.

## Mandatory stop rule
Gem B must not generate the complete 40-sticker production set before Hero Gate PASS when the set requires a Hero Gate.

Producing full Sheets before Hero approval is a process defect even if the resulting artwork appears attractive.

## Standard 40-sticker release after Hero PASS
Unless set-specific SSOT overrides it, Gem B produces:
- Sheet 01: Frames 01–10,
- Sheet 02: Frames 11–20,
- Sheet 03: Frames 21–30,
- Sheet 04: Frames 31–40.

Each Sheet contains 10 equal Frames in a 5x2 Grid using the approved logical Frame profile.

## Change control after Hero approval
Owner approval locks the visual direction used for scale-up.

Gem B may vary poses, camera and props as allowed by the Production Document Package, but must not silently change:
- Character identity,
- locked style direction,
- approved captions,
- product strategy,
- declared communication intent.

A material direction change requires owner review and may require re-entry to the Hero Gate.

## Relationship to Gate B
Hero Gate approves the direction to scale. Gate B approves the completed visual master package for downstream Program/Engine processing.

Hero PASS does not automatically mean `READY_FOR_ENGINE`; the completed full-set output must still pass Gate B.

## Software boundary
This Gate governs documentation and visual-production workflow only. It does not authorize modification of Python, engine, scripts, validators, packaging or other deterministic tooling.
