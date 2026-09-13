# Modular Sticker Production Architecture

**Version:** 1.0  
**Status:** Active companion to CPDF 1.2

## Purpose
Define how specialist AI Gems, human reviewers, and deterministic software cooperate from concept to LINE submission-ready files.

Core rule:

> Every component must complete and verify its own work before handoff. Downstream components must not be used to repair upstream defects.

## System model

```text
PRODUCT OWNER
  ↓
GEM A — Sticker Product Architect
  ↓ Production Document Package
GATE A — Documentation Readiness
  ↓
GEM B — Sticker Visual Producer
  ↓ High-resolution Master Frames / Master Sheets
GATE B — Master Asset Readiness
  ↓
PROGRAM / ENGINE — Deterministic Production
  ↓ Individual technically prepared sticker files
GATE C — Technical Submission Readiness
  ↓
FINAL HUMAN QA
  ↓
LINE SUBMISSION READY
```

## Specialist Gem principle
Each Gem has a narrow mission and bounded authority. It must accept only ready inputs, run internal quality checks, pass an Exit Gate, and emit a structured Output Contract.

A downstream Gem must not silently rewrite locked upstream SSOT. If an upstream defect is found, return it to the owning stage with evidence.

## Gem A — Sticker Product Architect
Mission: transform an initial concept into a production-ready document package.

Responsibilities include product intent, target users, JTBD/use cases, Character/Style SSOT, caption architecture, Hero plan, frame briefs, Sticker Sheet plan, forbidden drift, QA criteria, and handoff documents.

Output: **Production Document Package**. Gem A does not create final sticker artwork.

## Gem B — Sticker Visual Producer
Mission: create high-resolution master sticker artwork from the approved document package.

Responsibilities include Character/Style fidelity, communication clarity, composition, exact Frame/Sheet geometry, visual density control, and visual self-QA.

Output: approved Master Frames and/or Master Sticker Sheets plus frame mapping evidence.

Gem B must not independently rewrite captions, product strategy, or locked character identity.

## Program / Engine — Deterministic Production
Mission: convert approved master artwork into technically valid individual files and packages.

Appropriate automated responsibilities include sheet splitting, resizing, alpha/background processing where required, naming, dimension/format validation, set completeness validation, manifest generation, export, and packaging.

Technical PASS does not replace Visual QA PASS.

## Blackbox model
A Blackbox is an internal specialist process whose implementation may change without breaking the pipeline as long as its contracts remain valid.

Every Blackbox defines:
1. Input Contract
2. Definition of Ready
3. Responsibility and authority boundary
4. Internal quality controls
5. Exit Gate / Definition of Done
6. Output Contract
7. Defect return path

## Quality at Source
Defects are fixed by the stage that owns them.

- weak or duplicate caption → Gem A
- character drift or cluttered composition → Gem B
- invalid dimensions or package → Engine
- unresolved strategic decision → Product Owner

## Standard states
`DRAFT → IN_PROCESS → INTERNAL_QA → READY_FOR_GATE → PASS | PASS_WITH_CORRECTION | FAIL | BLOCKED → READY_FOR_HANDOFF`

Only `READY_FOR_HANDOFF` artifacts may be consumed as trusted upstream inputs.

## SSOT precedence
1. current official platform requirements
2. active Framework / global standards
3. Character SSOT
4. Product / Set SSOT
5. locked Production Document Package
6. current execution task

## Traceability
Every final sticker should trace backward through:

`final file → master frame → sheet/frame ID → frame brief → caption/use case → product brief → character/style SSOT`.
