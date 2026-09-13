# Gem Instruction Architecture

**Version:** 1.3  
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

## Specialist Gems
### Gem A — Sticker Product Architect
Input: initial concept plus available owner constraints/reference material.

Mission: produce a complete Production Document Package.

Literal handoff state after Gate A PASS: `READY_FOR_GEM_B`.

Deployment pack: `docs/gems/deploy/gem-a/`.

### Gem B — Sticker Visual Producer
Input: approved Production Document Package plus required Character/Style/Golden Reference context.

Mission: create high-resolution Visual Master Package containing Master Frames and/or Master Sticker Sheets with Visual QA evidence.

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

Do not consume all slots unless required. Preserve room for Character, Product Package, Golden Reference and other active-set context.

See `docs/gems/GEM_KNOWLEDGE_PACKAGING_STANDARD.md`.

## Authority precedence
1. current official platform requirements
2. latest explicit Product Owner decision that does not conflict with platform requirements
3. active CPDF / global standards
4. Character / Style SSOT
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
Each Gem corrects defects it owns before handoff. Gem B does not repair weak product architecture; downstream technical tooling does not repair visual/product defects.

## Machine-readable companion
Production Document Packages should include stable structured fields for Set ID, version, Frame count, Frame geometry, Sheet grid, Character/Style references, Hero IDs, per-Frame caption/intent/chat situation/expression/action/props/composition/forbidden traits, QA rules, output requirements and handoff status.

Human-readable SSOT remains authoritative unless the project explicitly designates another formal SSOT.

## Software boundary
Gem architecture, deployment packs and documentation must not modify existing Python application code, `engine/`, `scripts/`, validators, packagers, desktop implementation or deterministic processing logic unless the Product Owner opens a separate explicit software-development task.

## Portability rule
Describe roles, contracts, gates, knowledge and outputs rather than vendor-specific tricks. The architecture should remain portable across Gemini Gems, ChatGPT, other AI systems, or human specialists.

## Related documents
- `docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`
- `docs/project/MULTI_AGENT_STICKER_PRODUCTION_ARCHITECTURE.md`
- `docs/project/HANDOFF_CONTRACT_STANDARD.md`
- `docs/project/HANDOFF_STATUS_ADDENDUM.md`
- `docs/project/QUALITY_GATE_STANDARD.md`
- `docs/gems/GEM_KNOWLEDGE_PACKAGING_STANDARD.md`
- `docs/gems/PRODUCTION-DOCUMENT-PACKAGE-TEMPLATE.md`
- `docs/standards/MASTER_SHEET_FRAME_STANDARD.md`
- `docs/standards/STICKER_COMMUNICATION_STANDARD.md`
