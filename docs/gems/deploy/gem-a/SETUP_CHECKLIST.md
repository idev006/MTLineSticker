# GEM-A Setup Checklist

## Builder setup
- Paste `INSTRUCTION.txt` into the Custom GPT Instructions field.
- Upload the five Knowledge TXT files listed in `KNOWLEDGE_MANIFEST.md`.
- Remove older Gem A Knowledge copies.
- Enable file/data analysis capability when available.
- Save the GPT.

## Quick test
Send `show roadmap`.
Expected: a simple explanation of the current stage and next action.

Then send a short product brief.
Expected: Gem A asks only necessary questions, keeps unknown facts unspecified, creates product/document architecture, and tells the user what to do next.

## Package test
Confirm the output has structured files, frame-count reconciliation, Character Sheet production documents, Hero planning, QA/handoff information, and a user-facing next step.

## Release checks
- Instruction is below the Custom GPT size limit used by this project.
- Five Knowledge files match the manifest.
- Guided Operator Mode is present.
- Source firewall is present.
- Commercial North Star is present.
- Character approval gate is preserved.
- Any stop state gives a recovery action.
