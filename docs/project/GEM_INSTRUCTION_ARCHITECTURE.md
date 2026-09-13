# Gem Instruction Architecture

**Version:** 1.2  
**Status:** Active design standard for specialist Gemini Gems

## Purpose
Implement the sticker-production architecture as specialist Gems without turning a single Gem Instruction into an oversized prompt.

## Core model
A deployed Gem has four layers:
1. **Instruction = Orchestrator** — role, mission, loading order, Blackbox routing, stop conditions, gates and output routing.
2. **Knowledge Pack = Specialist Knowledge Base** — compiled, role-specific rules derived from repository SSOT.
3. **Repository SSOT = Project Truth** — authoritative framework, standards and set documents.
4. **Runtime Project Context** — current Character/Product/Production Package/Golden Reference.

The Instruction must stay compact. Detailed domain rules belong in attached knowledge files.

## Specialist Gems
### Gem A — Sticker Product Architect
Input: concept / owner constraints / inherited IP context.  
Output: validated Production Document Package with status `READY_FOR_GEM_B`.

### Gem B — Sticker Visual Producer
Input: approved Production Document Package + visual references.  
Output: validated high-resolution Master Frames / Master Sticker Sheets for downstream technical processing.

### Existing Program / Engine
Receives approved visual masters and performs deterministic processing according to the existing software implementation. Gem/documentation work does not authorize software changes.

## Blackbox contract
Every specialist uses:
`Input Contract -> Definition of Ready -> Internal Blackbox -> Internal QA -> Exit Gate -> Output Contract -> Handoff`

A downstream specialist must not repair defects owned by an upstream specialist.

## Instruction responsibilities
Every Gem Instruction must define only the control plane:
- ROLE and MISSION,
- AUTHORITY BOUNDARY,
- SSOT / knowledge precedence,
- REQUIRED KNOWLEDGE MANIFEST,
- INPUT CONTRACT and Definition of Ready,
- BLACKBOX checkpoints,
- STOP / RETURN / ESCALATION states,
- Exit Gate / Definition of Done,
- Output Contract / Handoff status.

Detailed caption rules, visual rules, frame geometry, QA checklists and examples should live in Knowledge Packs unless essential to orchestration.

## Knowledge-file budget
Platform constraint recorded by Product Owner: maximum **10 attached knowledge files per Gem**.

Deployment policy:
- target **5 fixed knowledge files**,
- reserve **5 slots for runtime/project-specific knowledge**,
- compile related SSOT documents into role-specific knowledge bundles,
- do not mirror repository files 1:1 into Gem attachments.

See `docs/gems/GEM_KNOWLEDGE_PACKAGING_STANDARD.md`.

## Knowledge loading policy
At runtime the Orchestrator must:
1. identify current stage,
2. load mandatory fixed knowledge,
3. load relevant runtime/project context,
4. validate DoR,
5. execute the Blackbox,
6. apply Exit Gate,
7. hand off only validated output.

## SSOT priority
1. latest explicit Product Owner decision,
2. active Framework / standards,
3. Character / Style SSOT,
4. set Product / Production SSOT,
5. approved handoff package,
6. compiled knowledge pack,
7. working notes.

A compiled knowledge file never outranks its source SSOT.

## Quality at source
- product/caption/document defects -> Gem A,
- Character/composition/visual defects -> Gem B,
- deterministic technical defects -> existing Program/Engine.

## Software boundary
Gem architecture and documentation must not modify Python application code, `engine/`, `scripts/`, validators, packagers, desktop implementation or deterministic processing logic unless the Product Owner explicitly opens a separate software-development task.

## Deployment artifacts
Implementation-ready deployment packs live under:
- `docs/gems/deploy/gem-a/`
- `docs/gems/deploy/gem-b/`

Each deployment folder contains an `INSTRUCTION.txt`, a `KNOWLEDGE_MANIFEST.md`, and no more than five fixed `.txt` knowledge files by default.

## Related standards
- `docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`
- `docs/project/MULTI_AGENT_STICKER_PRODUCTION_ARCHITECTURE.md`
- `docs/project/HANDOFF_CONTRACT_STANDARD.md`
- `docs/project/QUALITY_GATE_STANDARD.md`
- `docs/standards/MASTER_SHEET_FRAME_STANDARD.md`
- `docs/standards/STICKER_COMMUNICATION_STANDARD.md`
- `docs/gems/GEM_KNOWLEDGE_PACKAGING_STANDARD.md`
- `docs/gems/PRODUCTION-DOCUMENT-PACKAGE-TEMPLATE.md`
