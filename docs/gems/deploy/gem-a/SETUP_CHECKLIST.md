# GEM-A Setup Checklist — v2.5

## Builder setup
- [ ] Paste `INSTRUCTION.txt` into the Custom GPT Instructions field.
- [ ] Upload the five Knowledge TXT files listed in `KNOWLEDGE_MANIFEST.md`.
- [ ] Remove older Gem A Knowledge copies.
- [ ] Enable Code Interpreter / Data Analysis when available so Gem A can create ZIP/package handoff bundles.
- [ ] Save the GPT.

## Quick test
Send `show roadmap`.
Expected: a simple explanation of the current stage and next action.

Then send a short product brief.
Expected: Gem A asks only necessary questions, keeps unknown facts unspecified, creates product/document architecture, and tells the user what to do next.

## Package test
Confirm the output has structured files, frame-count reconciliation, Character Sheet production documents, Hero planning, QA/handoff information, and a user-facing next step.

## Decision-closure test
When Gem A asks one material owner decision, answer it. Confirm Gem A:
- [ ] records the decision,
- [ ] updates affected current-package files,
- [ ] closes/updates the open item,
- [ ] recalculates handoff state,
- [ ] continues without asking you to restate the brief.

## Character handoff test
When no Character Sheet is active, confirm Gem A produces or clearly exposes:
- [ ] `CHARACTER_SHEET_RUNTIME_HANDOFF.md`
- [ ] `CHARACTER_SHEET_RUNTIME_PROMPT.txt`
- [ ] `CHARACTER_SHEET_HANDOFF_README.md`
- [ ] exact confirmed reference list
- [ ] `CHARACTER_SHEET_HANDOFF.zip` when archive creation is available
- [ ] expected result `READY_FOR_CHARACTER_OWNER_REVIEW`

## Manifest test
- [ ] payload file count is explicit
- [ ] total archive file-entry count is explicit
- [ ] manifest self-hash policy is explicit
- [ ] counts reconcile with the actual ZIP

## Release checks
- [ ] Instruction is below the Custom GPT size limit used by this project.
- [ ] Five Knowledge files match the manifest.
- [ ] Guided Operator Mode is present.
- [ ] Source firewall is present.
- [ ] Commercial North Star is present.
- [ ] Character approval gate is preserved.
- [ ] Any stop state gives a recovery action.
