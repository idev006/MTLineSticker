# GEM-B Setup Checklist

## Builder setup
- Paste `INSTRUCTION.txt` into the Custom GPT Instructions field.
- Upload the five Knowledge TXT files listed in `KNOWLEDGE_MANIFEST.md`.
- Remove older Gem B Knowledge copies.
- Enable Code Interpreter / Data Analysis or equivalent archive/file capability.
- Enable Image Generation.
- Save the GPT.

## ZIP test
Attach a small ZIP and ask Gem B to list its files using archive/data tools.
Expected: it extracts or reads the archive rather than relying on Knowledge Search alone.

## Guided UX test
Send `show roadmap`.
Expected: clear current step and next action without a jargon dump.

## Hero test
Attach the current package plus `CHARACTER_SHEET_ACTIVE`, then use `HERO_RUNTIME_PROMPT.txt`.
Expected: current-runtime validation, Hero-only production, owner review state, and simple approve/revise guidance.

## Release checks
- Instruction is below the Custom GPT size limit used by this project.
- ZIP handling and current-runtime source rules are present.
- Image-generation capability is checked before production.
- Guided Operator Mode is present.
- Hero-first and owner unlock rules remain enforced.
- Any stop state gives an actionable recovery path.
