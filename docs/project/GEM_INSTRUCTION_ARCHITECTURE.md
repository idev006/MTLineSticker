# Gem Instruction Architecture

**Version:** 1.0  
**Status:** Design standard for specialist Gemini Gem instructions

## Purpose
Convert the project Framework into reusable specialist Gem instructions without collapsing all responsibilities into one oversized prompt.

## Core design
Use multiple specialist Gems connected by explicit contracts.

### Gem A — Sticker Product Architect
Receives an initial product concept and produces the complete Production Document Package.

### Gem B — Sticker Visual Producer
Receives only an approved Production Document Package and produces high-resolution sticker Master Frames / Master Sticker Sheets.

### Program / Engine
Receives approved visual masters and performs deterministic technical processing.

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
```

The human-readable documents remain authoritative unless the project later designates a formal machine-readable SSOT.

## Portability rule
Instructions should describe roles, contracts, and standards rather than model-specific tricks. This lets the same architecture be implemented with Gemini Gems, ChatGPT, other AI systems, or human specialists.
