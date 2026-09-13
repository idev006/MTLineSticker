# Modular Sticker Production Architecture

**Version:** 1.2  
**Status:** Active companion to CPDF 1.5

## Purpose
Define how specialist AI Gems, external Character Sheet creation, human reviewers, and deterministic software cooperate from concept to LINE submission-ready files.

Core rule:
> Every component must complete and verify its own work before handoff. Downstream components must not be used to repair upstream defects.

## System model

```text
PRODUCT OWNER
  ↓ requirements + text/image/video references + captions/constraints
GEM A — Sticker Product Architect
  ↓ structured Production Document Package
CHARACTER SHEET CREATION — outside Gem A
  ↓ Character Sheet candidate
PRODUCT OWNER CHARACTER APPROVAL
  ↓ CHARACTER_SHEET_ACTIVE
GATE A
  ↓ READY_FOR_GEM_B
GEM B — Sticker Visual Producer
  ↓ Hero Sticker Sheet
PRODUCT OWNER HERO REVIEW
  ↓ FULL_PRODUCTION_UNLOCKED
GEM B — Full Production
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
Mission: transform user intent and allowed text/image/video references into a production-ready structured documentation package.

Responsibilities include product intent, target users, JTBD/use cases, Character Bible, Character/Style requirements, Character Sheet specification/generation prompt/negative constraints/approval checklist, caption architecture, Hero plan, Frame briefs, Sticker Sheet plan, QA criteria, manifests and handoff documents.

Preferred output: one ZIP archive preserving the required Gem A package structure when archive creation is supported; otherwise the same exact named files separately.

Gem A does not create the Character Sheet image or final sticker artwork.

Gem A may prepare documentation before Character Sheet approval, but `READY_FOR_GEM_B` is prohibited until required `CHARACTER_SHEET_ACTIVE` exists and Gate A passes unless a Product Owner exception is explicitly documented.

## Character Sheet creation and approval
Character Sheet image creation is a controlled step outside Gem A. It uses Gem A's Character Bible/specification/generation prompt together with relevant references.

The Product Owner reviews the candidate against the approval checklist. Approval creates `CHARACTER_SHEET_ACTIVE`, the canonical active visual Character reference for Gem B.

Raw source images/video, a prompt, or an unapproved candidate do not substitute for `CHARACTER_SHEET_ACTIVE`.

## Gem B — Sticker Visual Producer
Mission: create high-resolution Hero and full-production master sticker artwork from the approved Gem A package plus `CHARACTER_SHEET_ACTIVE`.

Responsibilities include package preflight, Character/Style fidelity, communication clarity, composition, Frame/Sheet geometry, visual density control, Hero production, visual self-QA, full production after approval, and output manifests.

Normal input requires `READY_FOR_GEM_B`, a coherent Gem A package, and `CHARACTER_SHEET_ACTIVE`.

When Hero gating is declared, Gem B first outputs one Hero Sticker Sheet and `READY_FOR_VISUAL_OWNER_REVIEW`. Full production stays locked until Product Owner Hero approval advances the state to `FULL_PRODUCTION_UNLOCKED`.

Output after full production and Gate B PASS: **Visual Master Package** with status `READY_FOR_ENGINE`.

Gem B must not independently rewrite captions, product strategy, Character identity, or optional/mandatory trait classification.

## Program / Engine — Deterministic Production
Mission: convert approved visual masters into technically prepared individual files and packages.

Appropriate automated responsibilities include Sheet splitting, resizing, approved alpha/background processing, naming, technical validation, set completeness validation, manifest generation, export, and packaging.

Output: **Technical Output Package** with individual files and status `READY_FOR_FINAL_QA`.

Technical PASS does not replace Visual QA PASS.

## Product Owner / Final Human QA
Product Owner owns material product decisions, Character Sheet approval, Hero visual approval when required, and final acceptance.

Output state after final PASS: `LINE_SUBMISSION_READY`.

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
- weak/duplicate caption, unsupported Character rule, incomplete package, premature READY_FOR_GEM_B → Gem A
- Character drift, wrong visual mapping, cluttered composition, premature full production → Gem B
- invalid split / resize / naming / technical package → Program/Engine
- unresolved strategic or acceptance decision → Product Owner

## State vocabulary
Literal cross-stage readiness values are:
- `READY_FOR_GEM_B`
- `READY_FOR_VISUAL_OWNER_REVIEW`
- `FULL_PRODUCTION_UNLOCKED`
- `READY_FOR_ENGINE`
- `READY_FOR_FINAL_QA`
- `LINE_SUBMISSION_READY`

`READY_FOR_HANDOFF` is a generic concept only.

## Lifecycle SSOT
- Planning SSOT: Framework + set Product/Production documents
- Character visual SSOT: `CHARACTER_SHEET_ACTIVE` + approval/version record
- Visual production SSOT: approved Visual Master Package
- Technical SSOT: individual submission files + manifest/validation evidence

## Authority precedence
1. current official platform requirements
2. latest explicit Product Owner decision that does not conflict with platform requirements
3. active Framework / global standards
4. Character / Style SSOT including `CHARACTER_SHEET_ACTIVE`
5. Product / Set SSOT
6. approved handoff package
7. compiled Gem knowledge pack
8. current execution notes/task

## Traceability
Every final sticker should trace backward through:
`final individual file → manifest/validation → Master Frame or Sheet cell → Frame ID → Frame brief → caption/use case → Product Brief → Character Bible → CHARACTER_SHEET_ACTIVE`.

## Software boundary
This architecture does not authorize changes to existing Python, `engine/`, `scripts/`, validators, packagers, desktop software or deterministic production logic. Such work requires a separate explicit software-development task from the Product Owner.
