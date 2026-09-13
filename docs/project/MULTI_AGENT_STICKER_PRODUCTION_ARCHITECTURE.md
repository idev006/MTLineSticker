# Modular Sticker Production Architecture

**Version:** 1.1  
**Status:** Active companion to CPDF 1.3

## Purpose
Define how specialist AI Gems, human reviewers, and deterministic software cooperate from concept to LINE submission-ready files.

Core rule:
> Every component must complete and verify its own work before handoff. Downstream components must not be used to repair upstream defects.

## System model

```text
PRODUCT OWNER
  ↓
GEM A — Sticker Product Architect
  ↓ Production Document Package / READY_FOR_GEM_B
GATE A
  ↓
GEM B — Sticker Visual Producer
  ↓ Visual Master Package / READY_FOR_ENGINE
GATE B
  ↓
PROGRAM / ENGINE — Deterministic Production
  ↓ Individual Technical Output Package / READY_FOR_FINAL_QA
GATE C
  ↓
FINAL HUMAN QA
  ↓ LINE_SUBMISSION_READY
GATE D
```

## Specialist principle
Each specialist has a narrow mission and bounded authority. It accepts only ready inputs, performs internal QA, passes its Exit Gate, and emits the contract required by the next stage.

A downstream component must not silently rewrite locked upstream SSOT. If an upstream defect is discovered, return it to the owning stage with evidence.

## Gem A — Sticker Product Architect
Mission: transform an initial concept into a production-ready document package.

Responsibilities include product intent, target users, JTBD/use cases, Character/Style requirement or inheritance, caption architecture, Hero plan, Frame briefs, Sticker Sheet plan, forbidden drift, QA criteria, and handoff documents.

Output: **Production Document Package** with status `READY_FOR_GEM_B`.

Gem A does not create final sticker artwork.

## Gem B — Sticker Visual Producer
Mission: create high-resolution master sticker artwork from the approved document package.

Responsibilities include Character/Style fidelity, communication clarity, composition, Frame/Sheet geometry, visual density control, and visual self-QA.

Output: **Visual Master Package** containing approved Master Frames and/or Master Sticker Sheets, Frame mapping, visual QA evidence, and status `READY_FOR_ENGINE`.

Gem B must not independently rewrite captions, product strategy, or locked Character identity.

## Program / Engine — Deterministic Production
Mission: convert approved visual masters into technically prepared individual files and packages.

Appropriate automated responsibilities include Sheet splitting, resizing, approved alpha/background processing, naming, technical validation, set completeness validation, manifest generation, export, and packaging.

Output: **Technical Output Package** with individual files and status `READY_FOR_FINAL_QA`.

Technical PASS does not replace Visual QA PASS.

## Product Owner / Final Human QA
Mission: verify that the final technical outputs still represent the approved product and are complete for submission.

Output state after PASS: `LINE_SUBMISSION_READY`.

## Blackbox model
Every Blackbox defines:
1. Input Contract
2. Definition of Ready
3. Responsibility and authority boundary
4. Internal quality controls
5. Exit Gate / Definition of Done
6. Output Contract
7. Defect return path

## Quality at Source
Defects are fixed by the stage that owns them:
- weak or duplicate caption → Gem A
- Character drift or cluttered composition → Gem B
- invalid split / resize / naming / package → Program/Engine
- unresolved strategic or acceptance decision → Product Owner

## State vocabulary
Internal working states may differ by specialist, but the literal cross-stage readiness values are:
- `READY_FOR_GEM_B`
- `READY_FOR_ENGINE`
- `READY_FOR_FINAL_QA`
- `LINE_SUBMISSION_READY`

`READY_FOR_HANDOFF` is a generic concept only.

## Lifecycle SSOT
- Planning SSOT: Framework + set Product/Production documents
- Visual SSOT: approved Visual Master Package
- Technical SSOT: individual submission files + manifest/validation evidence

## Authority precedence
1. current official platform requirements
2. latest explicit Product Owner decision that does not conflict with platform requirements
3. active Framework / global standards
4. Character / Style SSOT
5. Product / Set SSOT
6. approved handoff package
7. compiled Gem knowledge pack
8. current execution notes/task

## Traceability
Every final sticker should trace backward through:
`final individual file → manifest/validation → Master Frame or Sheet cell → Frame ID → Frame brief → caption/use case → Product Brief → Character/Style SSOT`.

## Software boundary
This architecture does not authorize changes to existing Python, `engine/`, `scripts/`, validators, packagers, desktop software or deterministic production logic. Such work requires a separate explicit software-development task from the Product Owner.
