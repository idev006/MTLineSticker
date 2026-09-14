# GEM-A — README FIRST

**Release:** Custom GPT Guided Operator v2.4

## What Gem A does
Gem A turns a simple sticker-product idea, current references and captions into a controlled Production Document Package. It guides the user through the work; the user does not need to understand internal gates or file contracts.

## Install
1. Put `INSTRUCTION.txt` in the Custom GPT **Instructions** field.
2. Upload only these five files to **Knowledge**:
   - `01_CORE_GOVERNANCE.txt`
   - `02_PRODUCT_COMMUNICATION.txt`
   - `03_CHARACTER_STYLE_GOVERNANCE.txt`
   - `04_QUALITY_HANDOFF.txt`
   - `05_PRODUCTION_PACKAGE.txt`
3. Do not upload `KNOWLEDGE_MANIFEST.md` as Knowledge.
4. Enable file/data tools if available so Gem A can create/read structured files and ZIP packages.

## Normal use
Attach current references and send the prompt from `START_RUNTIME_PROMPT.txt`.

Gem A should:
- orient you on the roadmap,
- analyze the product,
- create the package,
- tell you exactly what is still needed,
- provide a copy-paste next prompt for Character Sheet generation,
- never claim `READY_FOR_GEM_B` before required Character approval.

## Useful commands
`status` · `next` · `continue` · `show roadmap` · `what do you need from me?`

Repository SSOT always wins over this deployment copy on conflict.
