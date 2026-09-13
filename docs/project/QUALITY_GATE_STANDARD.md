# Quality Gate & Defect Ownership Standard

**Version:** 1.0  
**Status:** Active

## Principle
Every stage owns the quality of the work it creates. A downstream stage is not a repair shop for upstream defects.

## Gate model
### Gate A — Product / Documentation Readiness
Owner: Gem A — Sticker Product Architect

PASS requires:
- concept and product intent are clear,
- target users / JTBD / communication territory are defined,
- Character / Style SSOT is available,
- caption list and frame intent are locked,
- Hero plan exists,
- Master Sheet / Frame plan exists,
- QA and handoff criteria are complete,
- no unresolved blocking decision remains.

Output state: `READY_FOR_VISUAL_PRODUCTION`.

### Gate B — Visual / Master Asset Readiness
Owner: Gem B — Sticker Visual Producer

PASS requires:
- Character fidelity,
- communication clarity,
- caption-image fit,
- composition and small-size readability,
- no clutter that slows understanding,
- required Master Sheet / Frame geometry,
- sufficient source quality for resize-down,
- no frame bleed,
- all blocking visual defects closed.

Output state: `READY_FOR_ENGINE`.

### Gate C — Technical Submission Readiness
Owner: deterministic Program / Engine

PASS requires technical checks defined by current project and platform rules, including expected file set, format, dimensions, alpha/background behavior, naming, manifest, and package integrity.

Output state: `READY_FOR_FINAL_QA`.

### Gate D — Final Human Acceptance
Owner: Product Owner / delegated reviewer

PASS requires:
- visual set still matches approved product intent,
- no missing/wrong sticker,
- no obvious text/content error,
- technical package report is acceptable,
- final submission package is approved.

Output state: `LINE_SUBMISSION_READY`.

## Definition of Ready / Definition of Done
Every specialist Blackbox must maintain both.

**Definition of Ready** answers: “Is this stage allowed to start?”

**Definition of Done** answers: “Is this stage allowed to hand off?”

No stage may replace either definition with subjective confidence.

## Defect classes
- **P0 Blocker** — prevents stage completion or creates invalid product/submission.
- **P1 Major** — materially harms communication, character identity, usability, or technical correctness.
- **P2 Minor** — noticeable but non-blocking quality issue; must be recorded and dispositioned.
- **P3 Observation** — improvement note for later iteration.

## Defect ownership
The stage that creates the defect owns correction unless the evidence proves the root cause is upstream.

Examples:
- weak concept / redundant caption / wrong use case → Gem A
- wrong character / wrong pose / clutter / poor frame composition → Gem B
- bad split / resize / naming / technical validation → Engine
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
