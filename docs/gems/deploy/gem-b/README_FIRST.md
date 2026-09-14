# GEM-B — README FIRST

**Release:** Custom GPT Guided Operator v2.2

## What Gem B does
Gem B reads the approved production package and `CHARACTER_SHEET_ACTIVE`, creates the Hero set first, runs visual QA, guides the owner through Hero approval, and only then expands to full production.

## Install
1. Put `INSTRUCTION.txt` in the Custom GPT **Instructions** field.
2. Upload only these five files to **Knowledge**:
   - `01_CORE_GOVERNANCE.txt`
   - `02_VISUAL_COMMUNICATION.txt`
   - `03_CHARACTER_STYLE_GOVERNANCE.txt`
   - `04_FRAME_SHEET_QA.txt`
   - `05_HANDOFF_OUTPUT.txt`
3. Do not upload `KNOWLEDGE_MANIFEST.md` as Knowledge.
4. Enable **Code Interpreter / Data Analysis** or equivalent archive/file capability.
5. Enable **Image Generation**.

## Normal Hero session
Attach:
1. current Production Document Package ZIP,
2. approved `CHARACTER_SHEET_ACTIVE`,
3. approved current visual/style references only when needed.

Then paste `HERO_RUNTIME_PROMPT.txt`.

Gem B should extract the ZIP first, verify current runtime files, show a short status/roadmap, produce Hero only, and stop at owner review.

## Useful commands
`status` · `next` · `continue` · `show roadmap` · `what do you need from me?` · `approve hero` · `revise hero`

Repository SSOT always wins over this deployment copy on conflict.
