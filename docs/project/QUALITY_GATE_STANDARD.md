# Quality Gate & Defect Ownership Standard

**Version:** 1.2  
**Status:** Active

## Principle
Every stage owns the quality of the work it creates. A downstream stage is not a repair shop for upstream defects.

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
- Character / Style SSOT is available or an explicit owner-approved exception exists,
- caption list and frame intent are locked,
- Hero plan exists when required,
- Master Sheet / Frame plan exists,
- QA and handoff criteria are complete,
- no unresolved blocking decision remains.

Output state: `READY_FOR_GEM_B`.

### Hero Gate — Visual Direction Approval
Owner: Gem B for artifact quality; Product Owner for approval when required.

The Hero Gate is a scale-up gate inside visual production. It is required whenever the Production Document Package declares a Hero phase.

PASS requires:
- one Hero Sticker Sheet contains all declared Hero Frames,
- Hero Frame mapping and geometry are explicit,
- approved Character Sheet / Character visual reference is used,
- Character fidelity is acceptable across all Heroes,
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
- Character fidelity,
- communication clarity,
- caption-image fit,
- composition and small-size readability,
- no clutter that slows understanding,
- required Master Sheet / Frame geometry,
- sufficient source quality for resize-down,
- no cross-frame bleed,
- all blocking visual defects closed,
- manifest/mapping required by the downstream contract is complete.

For a standard 40-sticker set unless set SSOT overrides it, expected Full Production output is 4 Sheets x 10 Frames.

Output state: `READY_FOR_ENGINE`.

### Gate C — Technical Submission Readiness
Owner: deterministic Program / Engine

PASS requires technical checks defined by current project and platform rules, including expected individual file set, format, dimensions, alpha/background behavior, naming, manifest, and package integrity.

Output state: `READY_FOR_FINAL_QA`.

### Gate D — Final Human Acceptance
Owner: Product Owner / delegated reviewer

PASS requires:
- visual set still matches approved product intent,
- no missing/wrong sticker,
- no obvious text/content error,
- technical package report is acceptable,
- required submission assets are present,
- final submission package is approved.

Output state: `LINE_SUBMISSION_READY`.

## Definition of Ready / Definition of Done
Every specialist Blackbox must maintain both.

**Definition of Ready** answers: “Is this stage allowed to start?”  
**Definition of Done** answers: “Is this stage allowed to hand off?”

No stage may replace either definition with subjective confidence.

## Defect classes
- **P0 Blocker** — prevents stage completion or creates invalid product/submission.
- **P1 Major** — materially harms communication, Character identity, usability, or technical correctness.
- **P2 Minor** — noticeable but non-blocking quality issue; must be recorded and dispositioned.
- **P3 Observation** — improvement note for later iteration.

## Defect ownership
The stage that creates the defect owns correction unless evidence proves the root cause is upstream.

Examples:
- weak concept / redundant caption / wrong use case → Gem A
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
