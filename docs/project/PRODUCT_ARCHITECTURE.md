# Product Architecture

## Product hierarchy
`Brand → Character/IP → Sticker Product/Set → Master Sheet → Frame → Individual Sticker File`

## Shared layer
Character masters, visual standards, communication standards, CPDF, QA rules, Frame/Sheet standards, handoff contracts, and Gem architecture live outside individual sets.

## Set layer
Each sellable set owns its Product Brief, Character inheritance/adaptation notes, caption/use-case matrix, Hero plan, Frame production briefs, Master Sheet plan, QA evidence, manifest, launch metadata, and submission package.

## Production architecture
The project uses specialist components with explicit handoffs:

`Gem A — Product Architect → Gate A → Gem B — Visual Producer → Gate B → Deterministic Engine → Gate C → Final Human QA → LINE Submission Ready`

Each component is a Blackbox with Input Contract, Definition of Ready, authority boundary, internal QA, Exit Gate, Output Contract, and return path.

## Frame / Sheet model
A **Frame** is one sticker production unit.

A **Master Sticker Sheet** is a high-resolution file that contains multiple equal-size Frames in a deterministic Grid. Default working profile is 512×512 px per Frame, 5×2 Grid, 10 Frames per Sheet unless a set-specific spec overrides it.

Master Sheets are production/review inputs. Final submission is built from individual prepared sticker files.

## Responsibility boundary
- Product meaning / captions / use cases / Character requirements → Product Architecture stage
- Visual communication / Character fidelity / Master Frame quality → Visual Production stage
- Split / resize / alpha processing / validation / naming / manifest / package → Program/Engine
- Final acceptance → Product Owner / Human QA

## Lifecycle states
`IDEA → RESEARCH → PRODUCT_DEFINED → DOCUMENT_PACKAGE_READY → HERO_GATE → VISUAL_PRODUCTION → MASTER_ASSET_GATE → TECHNICAL_PRODUCTION → FINAL_QA → LINE_SUBMISSION_READY → SUBMITTED → RELEASED`

## Current set IDs
- SET-001-EVERYDAY-ADMIN
- SET-002-MEETING
- SET-003-FOLLOWUP
- SET-004-DOCUMENT
- SET-005-OFFICE-LIFE
- SET-006-HOUSEHUSBAND-HOUSEWORK

## Sticker IDs
Use stable set/sticker IDs according to the set's manifest. IDs should not change after approval.

## Rule
Do not fork shared Character masters inside a set. Do not silently overwrite upstream SSOT during downstream production. Deliberate caption reuse must be recorded in `data/CAPTION_REGISTRY.csv` where applicable.

## Governing documents
- `docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`
- `docs/project/MULTI_AGENT_STICKER_PRODUCTION_ARCHITECTURE.md`
- `docs/project/HANDOFF_CONTRACT_STANDARD.md`
- `docs/project/QUALITY_GATE_STANDARD.md`
- `docs/project/GEM_INSTRUCTION_ARCHITECTURE.md`
- `docs/standards/MASTER_SHEET_FRAME_STANDARD.md`
