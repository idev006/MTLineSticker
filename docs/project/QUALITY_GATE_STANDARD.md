# Quality Gate & Defect Ownership Standard

**Version:** 1.4  
**Status:** Active

## Principle
Every stage owns the quality of the work it creates. A downstream stage is not a repair shop for upstream defects.

All Gates exist to protect the Project North Star defined in `docs/project/PROJECT_NORTH_STAR_AND_SUCCESS_CRITERIA.md`: the final product must match approved user intent, communicate effectively, preserve Character/Style quality, satisfy current LINE requirements, and be commercially ready to sell.

Passing a local Gate never compensates for failure against the North Star.

## Canonical interface states
Use destination-specific readiness states as the literal handoff values:
- Gem A → Gem B: `READY_FOR_GEM_B`
- Gem B Hero review → Product Owner: `READY_FOR_VISUAL_OWNER_REVIEW`
- Hero approval → Gem B full production: `FULL_PRODUCTION_UNLOCKED`
- Gem B → Program/Engine: `READY_FOR_ENGINE`
- Program/Engine → Final Human QA: `READY_FOR_FINAL_QA`
- Final Human QA → submission: `LINE_SUBMISSION_READY`

`READY_FOR_HANDOFF` is a generic architectural concept only; it is not emitted when a destination-specific state exists.

## Gate model
### Gate A — Product / Documentation Readiness
Owner: Gem A — Sticker Product Architect

PASS requires:
- concept and product intent are clear,
- target users / JTBD / communication territory are defined,
- structured Gem A Production Document Package is complete,
- Character Bible and Character Sheet specification/generation/approval documents are complete,
- required approved Character Sheet exists and is recorded as `CHARACTER_SHEET_ACTIVE`, unless the Product Owner explicitly approves a documented exception,
- Character / Style SSOT is coherent,
- caption list and frame intent are locked or explicitly dispositioned,
- Hero plan exists when required and covers representative/risky dimensions,
- Master Sheet / Frame plan exists,
- QA and handoff criteria are complete,
- package/handoff manifests reconcile,
- no unresolved blocking decision remains,
- the package is coherent enough that Gem B can execute without inventing product strategy.

Raw source images/video alone do not satisfy the Character Sheet requirement. A Character Sheet specification or prompt alone does not satisfy it either.

If Character Sheet creation/approval or another owner decision is pending, Gem A must remain in a non-ready state such as `OWNER_DECISION_REQUIRED` or `BLOCKED` as appropriate. It must not emit `READY_FOR_GEM_B` prematurely.

Output state: `READY_FOR_GEM_B`.

### Hero Gate — Visual Direction Approval
Owner: Gem B for artifact quality; Product Owner for approval when required.

The Hero Gate is a scale-up gate inside visual production. It is required whenever the Production Document Package declares a Hero phase.

PASS requires:
- Gem A package entered Gem B with `READY_FOR_GEM_B`,
- `CHARACTER_SHEET_ACTIVE` is the primary Character visual reference unless a documented exception exists,
- one Hero Sticker Sheet contains all declared Hero Frames,
- Hero Frame mapping and geometry are explicit,
- Character fidelity is acceptable across all Heroes,
- mandatory/optional/forbidden Character traits are respected,
- approved visual/style direction is coherent,
- each Hero communicates its intended message clearly,
- caption-image mapping is correct,
- no blocking Hero visual defect remains,
- owner approval is recorded when the package requires it.

Hero Gate outcomes:
- `PASS` → `FULL_PRODUCTION_UNLOCKED`
- `CORRECTION_REQUIRED` → correct failed Hero Frames and re-enter Hero Gate
- `RETURN_TO_GEM_A` → upstream product/document defect
- `BLOCKED` → full production prohibited

A required Hero Gate may not be bypassed.

### Gate B — Visual / Master Asset Readiness
Owner: Gem B — Sticker Visual Producer

PASS requires:
- required Hero Gate has passed when applicable,
- all required Full Production Master Sticker Sheets exist,
- Character fidelity against `CHARACTER_SHEET_ACTIVE`,
- communication clarity against the Frame Communication Matrix,
- caption-image fit,
- composition and small-size readability,
- no clutter that slows understanding,
- required Master Sheet / Frame geometry,
- sufficient source quality for resize-down,
- no cross-frame bleed,
- all blocking visual defects closed,
- manifest/mapping required by the downstream contract is complete.

For a standard 40-sticker set unless set SSOT overrides it, expected Full Production output is 4 Sheets × 10 Frames.

Output state: `READY_FOR_ENGINE`.

### Gate C — Technical Submission Readiness
Owner: deterministic Program / Engine

PASS requires technical checks defined by current project and platform rules, including expected individual file set, format, dimensions, alpha/background behavior, naming, manifest, package integrity, and the current official LINE requirements applicable at submission time.

Output state: `READY_FOR_FINAL_QA`.

### Gate D — Final Human Acceptance
Owner: Product Owner / delegated reviewer

PASS requires:
- visual set still matches approved product intent,
- no missing/wrong sticker,
- no obvious text/content error,
- technical package report is acceptable,
- required submission assets are present,
- no unresolved P0/P1 defect remains,
- final submission package is approved for real submission and sale.

Output state: `LINE_SUBMISSION_READY`.

## Definition of Ready / Definition of Done
Every specialist Blackbox must maintain both.

**Definition of Ready** answers: “Is this stage allowed to start?”  
**Definition of Done** answers: “Is this stage allowed to hand off?”

No stage may replace either definition with subjective confidence.

## Defect classes
- **P0 Blocker** — prevents stage completion or creates invalid product/submission.
- **P1 Major** — materially harms communication, Character identity, usability, commercial readiness, or technical correctness.
- **P2 Minor** — noticeable but non-blocking quality issue; must be recorded and dispositioned.
- **P3 Observation** — improvement note for later iteration.

## Defect ownership
The stage that creates the defect owns correction unless evidence proves the root cause is upstream.

Examples:
- weak concept / redundant caption / wrong use case → Gem A
- unsupported Character invention / unrelated negative constraint / premature READY_FOR_GEM_B → Gem A
- wrong Character / wrong pose / clutter / poor frame composition → Gem B
- premature full production before Hero approval → Gem B process defect
- bad split / resize / naming / technical validation → Program/Engine
- ambiguous acceptance or commercial trade-off → Product Owner

## Return path
A failed Gate returns work to the owning stage together with:
- defect ID,
- severity,
- evidence,
- required corrective action,
- affected artifacts,
- re-entry Gate.

## Corrective learning
When a defect exposes a missing systemic control, update the Framework or relevant standard before scaling production. Fix the process as well as the asset.
