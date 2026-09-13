# Gem Instruction Architecture

**Version:** 1.1  
**Status:** Active design standard for specialist Gemini Gem instructions

## Purpose
Convert the project Framework into reusable specialist Gem instructions without collapsing all responsibilities into one oversized prompt.

The architecture follows a modular blackbox model: each specialist receives a defined input contract, performs its own controlled work, passes its own Exit Gate, and hands off only validated output.

## Core design
Use multiple specialist Gems connected by explicit contracts.

### Gem A — Sticker Product Architect
Receives an initial product concept and produces the complete Production Document Package.

Implementation-ready instruction:
- `docs/gems/GEM-A-STICKER-PRODUCT-ARCHITECT-INSTRUCTION.md`

### Gem B — Sticker Visual Producer
Receives only an approved Production Document Package and produces high-resolution sticker Master Frames / Master Sticker Sheets.

Implementation-ready instruction:
- `docs/gems/GEM-B-STICKER-VISUAL-PRODUCER-INSTRUCTION.md`

### Existing Program / Engine
Receives approved visual masters and performs deterministic technical processing according to the existing software implementation.

Documentation/Gem work must not modify that software unless the Product Owner explicitly opens a separate software-development task.

## Standard handoff package
Gem A hands Gem B the standard Production Document Package defined in:
- `docs/gems/PRODUCTION-DOCUMENT-PACKAGE-TEMPLATE.md`

The package exists to remove guesswork between specialist stages.

## Instruction anatomy for every Gem
Each Gem instruction should contain these sections in this order:
1. **ROLE** — specialist identity.
2. **MISSION** — single primary outcome.
3. **AUTHORITY BOUNDARY** — what the Gem may and may not change.
4. **SSOT PRIORITY** — precedence of references.
5. **INPUT CONTRACT** — required inputs.
6. **DEFINITION OF READY** — when work may start.
7. **BLACKBOX PROCESS** — internal workflow checkpoints.
8. **MANDATORY RULES** — non-negotiable controls.
9. **AUTO-REJECT CONDITIONS** — failures that must stop progress.
10. **EXIT GATE / DEFINITION OF DONE** — conditions for handoff.
11. **OUTPUT CONTRACT** — exact artifacts to emit.
12. **RETURN / ESCALATION RULES** — how to handle upstream defects or ambiguity.

## Gem A operating principle
Gem A is a product architect, not a sticker artist.

It should develop:
- Product Brief,
- audience / JTBD / communication territory,
- Character / Style requirement or inheritance,
- caption architecture,
- frame-by-frame communication briefs,
- Hero selection and Gate plan,
- Master Sticker Sheet / Frame plan,
- QA criteria,
- Production Document Package.

It must not claim production readiness while required fields are unresolved.

## Gem B operating principle
Gem B is a visual production specialist, not a product strategist.

It must:
- use locked references,
- create sticker communication assets rather than decorative illustrations,
- preserve Character identity,
- create Frames / Sheets using declared geometry,
- keep content uncluttered and legible,
- maintain high-resolution masters for downstream reduction,
- self-QA before handoff.

It must not silently rewrite captions or upstream product decisions.

## Standard auto-reject examples
- required SSOT missing,
- wrong Character identity,
- unapproved character redesign,
- wrong or altered caption,
- unclear communication intent,
- scene/decoration overwhelms message,
- Frame boundary violation,
- incorrect Sheet geometry,
- insufficient evidence for Exit Gate.

## Quality-at-source rule
Every specialist owns the quality of its own output.

Downstream stages must not be used as repair stations for upstream defects.

Examples:
- concept/caption/document defects return to Gem A,
- Character/composition/visual defects return to Gem B,
- deterministic technical defects belong to the existing Program/Engine stage.

## Machine-readable companion
Where practical, every Production Document Package should include a structured contract that can be parsed by another Gem or program.

Example fields:

```text
SET_ID
PRODUCT_NAME
VERSION
TOTAL_FRAMES
MASTER_FRAME_SIZE
SHEET_GRID
CHARACTER_SSOT
STYLE_SSOT
HERO_FRAMES
FRAME_001:
  caption
  intent
  chat_situation
  expression
  gesture
  props
  camera
  composition
  forbidden
...
QA_RULES
OUTPUT_REQUIREMENTS
HANDOFF_STATUS
```

The human-readable documents remain authoritative unless the project later designates a formal machine-readable SSOT.

## Software boundary
The Gem architecture governs planning, visual production behavior, QA and handoff documentation.

It does **not** authorize modification of:
- Python application code,
- `engine/`,
- `scripts/`,
- validators,
- packagers,
- desktop application implementation,
- existing deterministic processing logic.

Those are controlled software assets and require a separate explicit development task from the Product Owner.

## Portability rule
Instructions should describe roles, contracts, gates, quality standards and outputs rather than model-specific tricks. This allows the same architecture to be implemented with Gemini Gems, ChatGPT, other AI systems, or human specialists.

## Related standards
- `docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`
- `docs/project/MULTI_AGENT_STICKER_PRODUCTION_ARCHITECTURE.md`
- `docs/project/HANDOFF_CONTRACT_STANDARD.md`
- `docs/project/QUALITY_GATE_STANDARD.md`
- `docs/standards/MASTER_SHEET_FRAME_STANDARD.md`
- `docs/standards/STICKER_COMMUNICATION_STANDARD.md`
- `docs/standards/LINE_STICKER_SPEC.md`
- `docs/gems/README.md`
