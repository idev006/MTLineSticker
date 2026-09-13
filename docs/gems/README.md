# Specialist Gem Instruction Pack

This directory contains implementation-ready instructions and handoff templates for the specialist Gemini Gems used by the MT LINE Sticker production architecture.

## Documents

1. `GEM-A-STICKER-PRODUCT-ARCHITECT-INSTRUCTION.md`
   - converts concept into a complete Production Document Package
   - owns product strategy, caption/use-case architecture, Hero planning, Frame/Sheet planning and documentation quality
   - does not produce final visual masters

2. `GEM-B-STICKER-VISUAL-PRODUCER-INSTRUCTION.md`
   - converts an approved Production Document Package into high-resolution Master Frames / Master Sticker Sheets
   - owns Character fidelity, visual communication, composition, clutter control and visual QA
   - does not rewrite upstream product strategy and does not perform final technical export

3. `PRODUCTION-DOCUMENT-PACKAGE-TEMPLATE.md`
   - standard contract passed from Gem A to Gem B
   - contains product, Character/Style, caption matrix, frame briefs, Hero plan, Sheet plan, QA rules and handoff manifest

## Pipeline

`Product Owner -> Gem A -> Gate A -> Gem B -> Gate B -> Existing Program/Engine -> Gate C -> Final Human QA -> LINE Submission Ready`

## Blackbox rule

Each specialist is treated as a controlled blackbox with:
- Input Contract
- Definition of Ready
- Authority Boundary
- Internal specialist process
- Internal QA
- Exit Gate / Definition of Done
- Output Contract
- Return / escalation path

Only outputs that pass the specialist's own Exit Gate may be handed downstream.

## Quality at Source

A downstream component must not be used as a repair stage for defects that belong upstream.

Examples:
- product/caption defects return to Gem A
- Character/composition/visual defects return to Gem B
- deterministic technical defects belong to the existing Program/Engine stage

## Software boundary

The documents in this directory govern AI/human production behavior only.

**Do not modify the existing Python application, engine, scripts, validators, packaging pipeline or other deterministic tooling as part of documentation/Gem-instruction work unless the Product Owner explicitly opens a separate software-development task.**

## SSOT references

Read together with:
- `docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`
- `docs/project/MULTI_AGENT_STICKER_PRODUCTION_ARCHITECTURE.md`
- `docs/project/HANDOFF_CONTRACT_STANDARD.md`
- `docs/project/QUALITY_GATE_STANDARD.md`
- `docs/project/GEM_INSTRUCTION_ARCHITECTURE.md`
- `docs/standards/MASTER_SHEET_FRAME_STANDARD.md`
- `docs/standards/STICKER_COMMUNICATION_STANDARD.md`
- `docs/standards/LINE_STICKER_SPEC.md`
