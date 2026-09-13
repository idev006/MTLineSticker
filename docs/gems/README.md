# Specialist Gem System

This directory contains the governance, deployment instructions, knowledge packs and handoff templates for the specialist Gemini Gems used by the MT LINE Sticker production architecture.

## Current architecture
`Product Owner -> Gem A -> Gate A -> Gem B -> Gate B -> Existing Program/Engine -> Gate C -> Final Human QA -> LINE Submission Ready`

Each Gem is a controlled Blackbox. **Gem Instruction is the Orchestrator; attached TXT files are the Specialist Knowledge Pack; repository documents remain SSOT.**

## Deployable Gem packages
### Gem A — Sticker Product Architect
Use:
- `deploy/gem-a/INSTRUCTION.txt` as the Gemini Gem Instruction
- the five `.txt` files listed in `deploy/gem-a/KNOWLEDGE_MANIFEST.md` as fixed Knowledge attachments
- up to five additional runtime/project files as needed

Gem A converts concept into a validated Production Document Package. It does not produce final sticker artwork.

### Gem B — Sticker Visual Producer
Use:
- `deploy/gem-b/INSTRUCTION.txt` as the Gemini Gem Instruction
- the five `.txt` files listed in `deploy/gem-b/KNOWLEDGE_MANIFEST.md` as fixed Knowledge attachments
- up to five additional runtime/project files, normally the Production Package and Character/Style/Golden Reference context

Gem B converts approved production documentation into high-resolution Master Frames / Master Sticker Sheets. It does not rewrite upstream product strategy or perform deterministic final export.

## Knowledge budget
Platform constraint recorded by Product Owner: maximum **10 attached knowledge files per Gem**.

Project default:
- 5 fixed compiled knowledge files
- 5 slots reserved for runtime/project context

See `GEM_KNOWLEDGE_PACKAGING_STANDARD.md`.

## Authoring/reference documents
- `GEM-A-STICKER-PRODUCT-ARCHITECT-INSTRUCTION.md` — detailed role/reference specification
- `GEM-B-STICKER-VISUAL-PRODUCER-INSTRUCTION.md` — detailed role/reference specification
- `PRODUCTION-DOCUMENT-PACKAGE-TEMPLATE.md` — standard Gem A -> Gem B contract
- `GEM_KNOWLEDGE_PACKAGING_STANDARD.md` — packaging/budget/loading rules

The files under `deploy/` are the preferred implementation-ready Gem configuration.

## Quality at Source
Only outputs that pass the specialist's own Exit Gate may be handed downstream.
- product/caption/document defects -> Gem A
- Character/composition/visual defects -> Gem B
- deterministic technical defects -> existing Program/Engine

## Software boundary
**Do not modify the existing Python application, engine, scripts, validators, packaging pipeline or other deterministic tooling as part of documentation/Gem work unless the Product Owner explicitly opens a separate software-development task.**

## SSOT references
- `docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`
- `docs/project/MULTI_AGENT_STICKER_PRODUCTION_ARCHITECTURE.md`
- `docs/project/HANDOFF_CONTRACT_STANDARD.md`
- `docs/project/QUALITY_GATE_STANDARD.md`
- `docs/project/GEM_INSTRUCTION_ARCHITECTURE.md`
- `docs/standards/MASTER_SHEET_FRAME_STANDARD.md`
- `docs/standards/STICKER_COMMUNICATION_STANDARD.md`
- `docs/standards/LINE_STICKER_SPEC.md`
