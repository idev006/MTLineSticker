# Gem B Knowledge Manifest

**Manifest version:** 1.2
**Status:** Active
**Deploy Instruction:** `INSTRUCTION.txt` v2.2
**Fixed Knowledge:** 5 files

Put `INSTRUCTION.txt` in the Custom GPT Instructions field.

Attach these five fixed Knowledge files:
1. `01_CORE_GOVERNANCE.txt` v1.3
2. `02_VISUAL_COMMUNICATION.txt` v1.0
3. `03_CHARACTER_STYLE_GOVERNANCE.txt` v1.1
4. `04_FRAME_SHEET_QA.txt` v1.0
5. `05_HANDOFF_OUTPUT.txt` v2.0

Do NOT attach this manifest, README, setup checklist, runtime prompt or changelog as Knowledge.

Required/strongly recommended Custom GPT capabilities:
- Code Interpreter / Data Analysis or equivalent archive/file access
- Image Generation

Normal runtime priority:
1. current approved Gem A Production Package,
2. `CHARACTER_SHEET_ACTIVE`,
3. separate active Style/Golden Reference when applicable,
4. current approved references/Owner Notes only when useful.

Operator files:
- `README_FIRST.md`
- `SETUP_CHECKLIST.md`
- `HERO_RUNTIME_PROMPT.txt`
- `CHANGELOG.md`

Guided Operator Mode and ZIP runtime handling are part of the active Instruction. Repository SSOT, including `docs/standards/GEM_USER_EXPERIENCE_STANDARD.md`, wins on conflict.
