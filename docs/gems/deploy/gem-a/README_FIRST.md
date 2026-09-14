# GEM-A — README FIRST

**Release:** Custom GPT Guided Operator v2.5

## What Gem A does
Gem A turns a short owner brief and current references into a complete Production Document Package. It guides the user stage-by-stage, asks only material blocking decisions, and prepares executable handoffs instead of leaving the user to reconstruct the next step.

## Install
1. Put `INSTRUCTION.txt` in the Custom GPT **Instructions** field.
2. Upload only these five files to **Knowledge**:
   - `01_CORE_GOVERNANCE.txt`
   - `02_PRODUCT_COMMUNICATION.txt`
   - `03_CHARACTER_STYLE_GOVERNANCE.txt`
   - `04_QUALITY_HANDOFF.txt`
   - `05_PRODUCTION_PACKAGE.txt`
3. Do not upload `KNOWLEDGE_MANIFEST.md` as Knowledge.
4. Enable Code Interpreter / Data Analysis if available so Gem A can build ZIP packages and handoff bundles.

## Normal session
Attach the current brief/references, then paste `START_RUNTIME_PROMPT.txt`.

## Character Sheet transition
If Character Sheet is the next stage, v2.5 should prepare:
- Character Sheet runtime handoff summary,
- copy-paste Character Sheet prompt,
- exact confirmed reference list,
- simple handoff README,
- `CHARACTER_SHEET_HANDOFF.zip` when the environment supports file/archive creation.

After the owner resolves an open decision, Gem A should update the package automatically and continue to the next safe stage.

Useful commands: `status` · `next` · `continue` · `show roadmap` · `what do you need from me?`

Repository SSOT always wins over this deployment copy on conflict.
