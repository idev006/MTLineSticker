# Specialist Gem System

This directory contains the governance, deployment instructions, knowledge packs, operational playbook and handoff contracts for the specialist Gemini Gems used by the MTLineSticker production architecture.

## Current architecture

```text
Product Owner
→ Gem A — Product Architecture
→ Production Document Package
→ Character Sheet Generation
→ Product Owner Character Approval
→ CHARACTER_SHEET_ACTIVE
→ Gate A / READY_FOR_GEM_B
→ Gem B — Hero Production
→ READY_FOR_VISUAL_OWNER_REVIEW
→ Product Owner Hero Approval
→ FULL_PRODUCTION_UNLOCKED
→ Gem B — Full Production
→ READY_FOR_ENGINE
→ Existing Program/Engine
→ Final Human QA
→ LINE_SUBMISSION_READY
```

The Character Sheet and Hero approvals are explicit authority-changing gates. They must not be collapsed into a generic Gem A → Gem B handoff.

Each Gem is a controlled Blackbox. **Gem Instruction is the Orchestrator; attached TXT files are the Specialist Knowledge Pack; repository documents and active approved artifacts remain SSOT.**

## Start here

For day-to-day operation, read:

- [`GEM_OPERATIONAL_PLAYBOOK.md`](GEM_OPERATIONAL_PLAYBOOK.md) — practical setup, runtime input bundles, authority rules, copy-ready prompt patterns, state cheat sheet and failure recovery.
- [`../workflow/AI_TOOL_USAGE_GUIDE.md`](../workflow/AI_TOOL_USAGE_GUIDE.md) — which AI/tool to use at each stage.
- [`../workflow/LINE_STICKER_END_TO_END_PIPELINE.md`](../workflow/LINE_STICKER_END_TO_END_PIPELINE.md) — full production pipeline.
- [`../workflow/PRODUCTION_RUNBOOK_AND_GATES.md`](../workflow/PRODUCTION_RUNBOOK_AND_GATES.md) — gates/checklists/operator runbook.

## Deployable Gem packages

### Gem A — Sticker Product Architect
Use:
- `deploy/gem-a/INSTRUCTION.txt` as the Gemini Gem Instruction,
- the five `.txt` files listed in `deploy/gem-a/KNOWLEDGE_MANIFEST.md` as fixed Knowledge attachments,
- current runtime/project references as needed.

Gem A converts product intent into a validated Production Document Package. It does **not** create final Character Sheet artwork or final sticker artwork.

### Character Sheet stage — separate from Gem A and Gem B Hero production
Use an image-generation AI with:
- the complete current `02_CHARACTER/` folder,
- the exact approved current reference set.

The AI produces a **Character Sheet Candidate** only. Product Owner approval is required before the result may become `CHARACTER_SHEET_ACTIVE`.

The active Character Sheet should already express the intended production visual style. Do not approve an overly realistic sheet while expecting Gem B to cartoonize it later; fix style upstream before activation.

### Gem B — Sticker Visual Producer
Use:
- `deploy/gem-b/INSTRUCTION.txt` as the Gemini Gem Instruction,
- the five `.txt` files listed in `deploy/gem-b/KNOWLEDGE_MANIFEST.md` as fixed Knowledge attachments,
- current runtime package: normally Production Package + `CHARACTER_SHEET_ACTIVE` + approved visual/style context.

Gem B first produces only the declared Hero scope. It may expand to full production only after explicit Product Owner approval creates `FULL_PRODUCTION_UNLOCKED`.

Gem B does not rewrite upstream product strategy and does not perform deterministic final export.

## Runtime handoff to Gem B

Recommended Hero handoff bundle:
1. current Production Document Package ZIP,
2. approved `CHARACTER_SHEET_ACTIVE`,
3. exact current visual references when useful for fidelity checks,
4. approved separate Style / Golden Reference when applicable,
5. optional current `OWNER_NOTES.md`.

Do not attach obsolete Character Sheets, superseded references or old style experiments.

## Knowledge budget

Platform constraint recorded by Product Owner: maximum **10 attached knowledge files per Gem**.

Project default:
- 5 fixed compiled knowledge files,
- remaining capacity reserved for current runtime/project context where supported.

See `GEM_KNOWLEDGE_PACKAGING_STANDARD.md` and the active deploy manifest for each Gem.

## Authoring/reference documents

- `GEM-A-STICKER-PRODUCT-ARCHITECT-INSTRUCTION.md` — detailed role/reference specification
- `GEM-B-STICKER-VISUAL-PRODUCER-INSTRUCTION.md` — detailed role/reference specification
- `PRODUCTION-DOCUMENT-PACKAGE-TEMPLATE.md` — standard Gem A package contract
- `GEM_KNOWLEDGE_PACKAGING_STANDARD.md` — packaging/budget/loading rules
- `GEM_OPERATIONAL_PLAYBOOK.md` — operator-facing usage guide

The files under `deploy/` are the preferred implementation-ready Gem configuration. Old chat copies or authoring drafts do not override active deploy files.

## Quality at Source

Only outputs that pass the appropriate source-stage gate may move downstream.

- product/caption/document/commercial architecture defects → Gem A
- Character identity/style defects discovered before activation → Character Sheet stage
- Hero/full-production visual defects → Gem B
- deterministic technical defects → existing Program/Engine

Do not use downstream stages to hide upstream defects.

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
- `docs/workflow/`
