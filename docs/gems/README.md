# Specialist Custom GPT System — MTLineSticker

This directory contains the governance, deployment instructions, Knowledge packs, operator guides and handoff contracts for the specialist Custom GPTs known in the project as **Gem A** and **Gem B**.

## User-first principle

The system follows:

> **Strict inside, simple outside. Always make the next correct action obvious.**

Every specialist GPT must satisfy both:
1. expert task performance, and
2. Guided Operator UX.

The canonical UX requirements are in:
- [`../standards/GEM_USER_EXPERIENCE_STANDARD.md`](../standards/GEM_USER_EXPERIENCE_STANDARD.md)

## Canonical roadmap

```text
1 Product Brief
→ 2 Gem A Production Package
→ 3 Character Sheet
→ 4 Product Owner Character Approval
→ 5 Gate A / READY_FOR_GEM_B
→ 6 Gem B Hero Production
→ 7 Product Owner Hero Approval
→ 8 Full Production
→ 9 Engine / Technical QA
→ 10 LINE Submission
```

Character activation and Hero approval are explicit authority-changing gates.

## Start here

For normal operators:
- [`../workflow/START_HERE.md`](../workflow/START_HERE.md)
- [`../workflow/COPY_PASTE_PROMPT_LIBRARY.md`](../workflow/COPY_PASTE_PROMPT_LIBRARY.md)
- [`GEM_OPERATIONAL_PLAYBOOK.md`](GEM_OPERATIONAL_PLAYBOOK.md)

For deployment:
- `deploy/gem-a/README_FIRST.md`
- `deploy/gem-a/SETUP_CHECKLIST.md`
- `deploy/gem-b/README_FIRST.md`
- `deploy/gem-b/SETUP_CHECKLIST.md`

## Gem A — Sticker Product Architect

Implementation-ready folder:

```text
docs/gems/deploy/gem-a/
```

Install:
- `INSTRUCTION.txt` → Custom GPT Instructions
- 5 TXT files listed in `KNOWLEDGE_MANIFEST.md` → Knowledge
- operator files are guidance, not Knowledge

Gem A converts a concise Product Owner brief into a validated multi-file Production Document Package. It does not create final Character Sheet artwork or final sticker artwork.

Gem A uses Guided Operator Mode by default: it shows where the user is, asks only necessary owner decisions, gives copy-paste next actions and never expects the user to manage internal gates manually.

## Character Sheet stage

Character Sheet generation is a separate visual stage. Use the package's complete current `02_CHARACTER/` plus exact approved references.

The result is a **Character Sheet Candidate**. Only the Product Owner may activate it as:

```text
CHARACTER_SHEET_ACTIVE
```

The active sheet must already represent the intended production rendering style closely enough for downstream reproduction. Do not approve a realism/style mismatch and expect Gem B to repair it later.

## Gem B — Sticker Visual Producer

Implementation-ready folder:

```text
docs/gems/deploy/gem-b/
```

Install:
- `INSTRUCTION.txt` → Custom GPT Instructions
- 5 TXT files listed in `KNOWLEDGE_MANIFEST.md` → Knowledge
- enable Code Interpreter / Data Analysis or equivalent archive/file access
- enable Image Generation

Normal Hero session:
1. attach current Production Package ZIP,
2. attach `CHARACTER_SHEET_ACTIVE`,
3. attach only current approved visual/style references when useful,
4. paste `HERO_RUNTIME_PROMPT.txt`.

Gem B must extract/read the current ZIP using archive/data tools when available. File Search/Knowledge Search alone is not evidence that ZIP-internal files are missing.

Gem B is Hero-first. It may not expand to full production until explicit Product Owner approval creates:

```text
FULL_PRODUCTION_UNLOCKED
```

## Current-runtime source discipline

Set-specific execution facts must come from current user input, current runtime files, active SSOT or fixed governance.

Do not reconstruct Hero IDs, captions, Character facts, visual direction or readiness state from stale chats, old examples or unrelated Knowledge.

## Guided Operator behavior

Both Gems support simple commands such as:

```text
status
next
continue
show roadmap
what do you need from me?
```

Gem B additionally supports:

```text
approve hero
revise hero
```

A stop state must always include recovery instructions and the smallest next user action. A status word alone is not an acceptable user experience.

## Quality at Source

- product/caption/document/commercial defects → Gem A
- Character identity/style defects before activation → Character Sheet stage
- Hero/full-production visual defects → Gem B
- deterministic file/export defects → Engine/scripts
- authority-changing approvals → Product Owner

Do not use downstream stages to hide upstream defects.

## Repository authority

The repository and active approved set/Character artifacts are SSOT. Old chat copies, exported deployment ZIPs and authoring drafts do not override the latest active repository version.
