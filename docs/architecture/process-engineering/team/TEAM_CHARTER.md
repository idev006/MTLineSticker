# MTLineSticker AI Engineering Team — Charter v1.0

**Owner authorization:** User approved adding all seven proposed specialist roles on 2026-10-21.  
**Status:** ORGANIZATIONAL DESIGN APPROVED; AI role specifications only. No human employees have been hired, no persistent autonomous agents provisioned, and no paid services engaged.

## Leadership
- Product Owner (human): final authority over scope, identity/style, Character activation, Hero approval, release.
- AI Team Lead / Solution Architect: coordinate bounded specialist reviews, maintain process and evidence, request owner decisions when material.

## Seven approved specialist roles
| ID | Role | Primary deliverable | Acceptance gate | Independent reviewer |
|---|---|---|---|---|
| R01 | Process Engineer | AS-IS/TO-BE, SIPOC, BPMN, FMEA and stage gates | Stage process verified | QA Automation |
| R02 | Multi-Agent Systems Architect | A/B interface contract, orchestration/state rules | Handoff schema & integration tests | Process Engineer |
| R03 | QA Automation Engineer | schema/semantic tests, fixtures, regression evidence | automated tests pass | Systems Architect |
| R04 | Character Consistency Specialist | identity/style continuity rubric, drift inspection | character/hero/batch visual QA | Art Director |
| R05 | Senior Visual Art Director | mature caricature, readability, composition and commercial review | candidate visual review | Character Specialist |
| R06 | DevOps / CI Engineer | reproducible CI, release, rollback, version pins | pipeline evidence available | QA Automation |
| R07 | LINE Sticker Release Specialist | platform requirements, formats, metadata, submission checklist | export/release readiness review | QA + Product Owner |

## Operating rules
1. Maker-checker separation is mandatory for gate-significant artifacts. A role cannot be its sole approver.
2. Each role supplies evidence, detected defects, severity and recommended remediation; no simulated expert opinion is represented as an independent person or externally verified audit.
3. All specialist roles are capabilities/personas invoked through available tools or prompts, not separately running persistent workers by default.
4. Repository SSOT controls. Every change records commit, issue and review status. No silent edits to locked Character/frame intent.
5. Character/Hero and final release approvals remain Product Owner decisions.
6. Never claim LINE platform compliance without checking current requirements and exported files.
7. A failing gate halts downstream production and routes defects to the responsible source stage.

## Priority staffing sequence
P0: R01/R02/R03/R04 define and validate gates, contract, identity.  
P1: R05/R06/R07 add art direction, CI and platform-readiness verification.  
All seven role definitions approved now; actual implementation/automation proceeds as capability becomes available.

## First sprint
- R02 and R03: finish handoff validator + contract tests, 40/40 source reconciliation and approval authenticity policy.
- R06: GitHub Actions test automation with measurable run result.
- R01: reconcile generic 4x10 vs CHAICHAT 5x8 mapping; capture decision and update gate.
- R04 and R05: Character approval checklist using actual approved reference files.
- R07: verify current official LINE image, sizing and submission specifications before release.
