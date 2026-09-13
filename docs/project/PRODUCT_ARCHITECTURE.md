# Product Architecture

## Product hierarchy
`Brand → Character/IP → Sticker Product/Set → Visual Master Package → Frame → Individual Technical Sticker File`

## Shared layer
Character masters, visual standards, communication standards, CPDF, QA rules, Frame/Sheet standards, handoff contracts, and Gem architecture live outside individual sets.

## Set layer
Each sellable set owns its Product Brief, Character inheritance/adaptation notes, caption/use-case matrix, Hero plan, Frame production briefs, Master Sheet plan, QA evidence, manifest, launch metadata, and submission package.

## Production architecture
`Gem A — Product Architect → Gate A → Gem B — Visual Producer → Gate B → Program/Engine → Gate C → Final Human QA → Gate D → LINE Submission Ready`

Cross-stage readiness states are:
- `READY_FOR_GEM_B`
- `READY_FOR_ENGINE`
- `READY_FOR_FINAL_QA`
- `LINE_SUBMISSION_READY`

Each component is a Blackbox with Input Contract, Definition of Ready, authority boundary, internal QA, Exit Gate, Output Contract, and return path.

## Frame / Sheet model
A **Frame** is one sticker production unit.

A **Master Sticker Sheet** is a high-resolution file containing multiple equal-size Frames in a deterministic Grid. Default working profile is 512×512 px per Frame, 5×2 Grid, 10 Frames per Sheet unless set-specific SSOT overrides it.

Master Sheets may be upstream Visual Master artifacts when geometry, mapping, visual QA, Character fidelity, and communication clarity pass Gate B. Final submission is built from individual technically prepared files produced downstream.

## Lifecycle SSOT
- Planning SSOT: Framework + active set Product/Production documents
- Visual SSOT: approved Visual Master Package
- Technical SSOT: individual prepared files + validation/manifest evidence

## Responsibility boundary
- Product meaning / captions / use cases / Character requirements → Gem A
- Visual communication / Character fidelity / Master Frame/Sheet quality → Gem B
- split / resize / approved alpha processing / validation / naming / manifest / package → existing Program/Engine
- final acceptance → Product Owner / Human QA

## Lifecycle states
`IDEA → RESEARCH → PRODUCT_DEFINED → READY_FOR_GEM_B → VISUAL_PRODUCTION → READY_FOR_ENGINE → TECHNICAL_PRODUCTION → READY_FOR_FINAL_QA → LINE_SUBMISSION_READY → SUBMITTED → RELEASED`

## Current set IDs
- SET-001-EVERYDAY-ADMIN
- SET-002-MEETING
- SET-003-FOLLOWUP
- SET-004-DOCUMENT
- SET-005-OFFICE-LIFE
- SET-006-HOUSEHUSBAND-HOUSEWORK

## Sticker IDs
Use stable set/sticker IDs according to the set manifest. IDs should not change after approval.

## Rule
Do not fork shared Character masters inside a set. Do not silently overwrite upstream SSOT during downstream production. Deliberate caption reuse must be recorded in `data/CAPTION_REGISTRY.csv` where applicable.

## Governing documents
- `docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`
- `docs/project/MULTI_AGENT_STICKER_PRODUCTION_ARCHITECTURE.md`
- `docs/project/HANDOFF_CONTRACT_STANDARD.md`
- `docs/project/HANDOFF_STATUS_ADDENDUM.md`
- `docs/project/QUALITY_GATE_STANDARD.md`
- `docs/project/GEM_INSTRUCTION_ARCHITECTURE.md`
- `docs/gems/GEM_KNOWLEDGE_PACKAGING_STANDARD.md`
- `docs/standards/MASTER_SHEET_FRAME_STANDARD.md`
