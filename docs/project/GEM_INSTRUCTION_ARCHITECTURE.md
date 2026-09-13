# Gem Instruction Architecture

**Version:** 1.4  
**Status:** Active design standard for specialist Gemini Gem instructions

## Purpose
Implement the project Framework as multiple specialist Gems without turning each Gem Instruction into an oversized knowledge dump.

## Core model
Use four layers:
1. **Gem Instruction = Orchestrator**
2. **Fixed Knowledge Pack = compiled specialist rules**
3. **Runtime Project Context = current set-specific inputs/references**
4. **Repository SSOT = authoritative source documents**

The Instruction routes work; the Knowledge Pack teaches stable specialist rules; runtime context supplies the active set; repository SSOT resolves conflicts.

`KNOWLEDGE_MANIFEST.md` is an installer/deployment control document. It is not normally attached as Gem knowledge and must not consume one of the fixed/runtime attachment slots.

## Specialist Gems
### Gem A — Sticker Product Architect
Input: user intent plus available owner constraints, captions/seed captions, and text/image/video reference material supported by the Gem environment.

Mission: produce the complete structured Production Document Package defined by `GEM_A_OUTPUT_CONTRACT.md`, including Character Bible and Character Sheet specification/generation/approval documents.

Gem A does not create the Character Sheet image or final sticker artwork.

If required Character Sheet creation/approval is pending, Gem A remains non-ready. Literal handoff state after Character approval and Gate A PASS: `READY_FOR_GEM_B`.

Deployment pack: `docs/gems/deploy/gem-a/`.

### Character Sheet controlled step
Character Sheet image creation occurs outside Gem A using its approved Character documentation and relevant references. Product Owner approval activates `CHARACTER_SHEET_ACTIVE`.

### Gem B — Sticker Visual Producer
Input: approved structured Gem A Production Document Package with `READY_FOR_GEM_B` plus required `CHARACTER_SHEET_ACTIVE`, Style SSOT when separate, and Golden Reference when applicable.

Mission: create Hero output first when required, then high-resolution Full Production Visual Master Package after Product Owner Hero approval.

Hero review state: `READY_FOR_VISUAL_OWNER_REVIEW`.  
Owner Hero approval state: `FULL_PRODUCTION_UNLOCKED`.  
Literal handoff state after Gate B PASS: `READY_FOR_ENGINE`.

Deployment pack: `docs/gems/deploy/gem-b/`.

### Existing Program / Engine
Receives the approved Visual Master Package and performs existing deterministic technical preparation. Gem/documentation work does not modify this software.

## Orchestrator instruction anatomy
Keep each deployed Instruction concise and focused on:
- ROLE
- MISSION
- AUTHORITY BOUNDARY
- knowledge-loading order
- SSOT/conflict rule
- Definition of Ready
- Blackbox routing/checkpoints
- stop/return behavior
- Exit Gate
- destination-specific output state
- output contract
- software boundary

Detailed domain rules belong in attached Knowledge Files, not duplicated throughout the Instruction.

## Knowledge attachment budget
Project deployment constraint recorded by Product Owner: maximum 10 attached knowledge files per Gem.

Default design:
- 5 fixed compiled Knowledge Files
- up to 5 runtime/project-specific attachments

Do not count `INSTRUCTION.txt` or `KNOWLEDGE_MANIFEST.md` as fixed knowledge attachments. `INSTRUCTION.txt` belongs in the Gem Instructions field; the manifest is deployment guidance.

Do not consume all runtime slots unless required. Preserve room for Character, Product Package, Golden Reference and other active-set context.

See `docs/gems/GEM_KNOWLEDGE_PACKAGING_STANDARD.md`.

## Authority precedence
1. current official platform requirements
2. latest explicit Product Owner decision that does not conflict with platform requirements
3. active CPDF / global standards
4. Character / Style SSOT including `CHARACTER_SHEET_ACTIVE`
5. Product / Set SSOT
6. approved handoff package
7. compiled Knowledge Pack
8. current execution notes/task

If two authoritative sources conflict, stop and return the conflict. Do not choose silently.

## Blackbox contract
Every Gem must have:
1. Input Contract
2. Definition of Ready
3. Authority Boundary
4. Internal specialist process/checkpoints
5. Internal QA
6. Exit Gate / Definition of Done
7. Output Contract
8. Return / escalation path

## Quality at Source
Each Gem corrects defects it owns before handoff. Gem B does not repair weak product architecture or premature handoff; downstream technical tooling does not repair visual/product defects.

## Machine-readable companion
Production Document Packages should include stable structured fields for Set ID, version, Frame count, Frame geometry, Sheet grid, Character/Style references, active Character Sheet identity/version, Hero IDs, per-Frame caption/intent/chat situation/expression/action/props/composition/forbidden traits, QA rules, output requirements, open decisions and handoff status.

Human-readable SSOT remains authoritative unless the project explicitly designates another formal SSOT.

## Software boundary
Gem architecture, deployment packs and documentation must not modify existing Python application code, `engine/`, `scripts/`, validators, packagers, desktop implementation or deterministic processing logic unless the Product Owner opens a separate explicit software-development task.

## Portability rule
Describe roles, contracts, gates, knowledge and outputs rather than vendor-specific tricks. The architecture should remain portable across Gemini Gems, ChatGPT, other AI systems, or human specialists.

## Related documents
- `docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`
- `docs/project/MULTI_AGENT_STICKER_PRODUCTION_ARCHITECTURE.md`
- `docs/project/GEM_A_OUTPUT_CONTRACT.md`
- `docs/project/CHARACTER_SHEET_LIFECYCLE.md`
- `docs/project/HANDOFF_CONTRACT_STANDARD.md`
- `docs/project/HANDOFF_STATUS_ADDENDUM.md`
- `docs/project/QUALITY_GATE_STANDARD.md`
- `docs/project/GEM_B_OUTPUT_CONTRACT.md`
- `docs/gems/GEM_KNOWLEDGE_PACKAGING_STANDARD.md`
- `docs/gems/PRODUCTION-DOCUMENT-PACKAGE-TEMPLATE.md`
- `docs/standards/MASTER_SHEET_FRAME_STANDARD.md`
- `docs/standards/STICKER_COMMUNICATION_STANDARD.md`
