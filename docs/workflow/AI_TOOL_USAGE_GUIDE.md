# AI & Tool Usage Guide for MTLineSticker

**Version:** 1.0  
**Status:** Active

This guide explains which tool or AI role should be used at each stage, what inputs it receives, what it may decide, and where human approval is mandatory.

---

## 1. Tool map

| Stage | Primary tool / role | Main input | Main output | Human approval required? |
|---|---|---|---|---|
| Product architecture | Gem A | Product brief, references, captions | Production Document Package | Yes for unresolved decisions |
| Character Sheet generation | Image-generation AI | `02_CHARACTER/` + approved references | Character Sheet Candidate | **Yes** |
| Character activation | Product Owner | Candidate + checklist | `CHARACTER_SHEET_ACTIVE` | **Yes** |
| Hero production | Gem B | Package + active Character Sheet | Hero images | **Yes** |
| Full visual production | Gem B / controlled image AI | Approved Hero system + package | Full sticker masters | Batch QA |
| Technical preparation | Engine/scripts | Approved masters | resized/export/package assets | Final human QA |
| Repository control | GitHub | Docs/assets/decisions | SSOT/history/PRs | Review/merge policy |
| LINE submission | LINE Creators Market | final exports + metadata | submitted product | Human |

---

## 2. Gem A — Sticker Product Architect

### Use Gem A when
- starting a new set,
- turning a concept into a controlled plan,
- designing or validating caption architecture,
- creating Character documentation,
- planning Hero frames,
- defining Sheet mapping,
- creating QA/gate/handoff documents,
- evaluating commercial potential.

### Do not use Gem A for
- final Character Sheet artwork,
- final sticker artwork,
- self-approving a Character Sheet,
- bypassing Hero owner review,
- deterministic file processing that belongs to the engine.

### Recommended input
Keep the Product Owner prompt simple:
- target audience,
- product goal,
- Character concept,
- current references,
- owner locks,
- captions or seed captions.

Gem A owns the internal documentation rigor.

### Minimum expected output
A structured multi-file Production Document Package, preferably ZIP, with the standard folders `00_PACKAGE` through `06_HANDOFF`.

### Acceptance test
Before trusting Gem A output, check:
- 40-frame artifacts are actually populated 40/40,
- commercial analysis contains evidence rather than vague adjectives,
- no unsupported demographics or Character facts are invented,
- Character Sheet documentation is complete,
- handoff state matches Character Sheet reality,
- reference-count conflicts are not silently resolved by the AI.

---

## 3. Image-generation AI — Character Sheet Candidate

### Inputs
Recommended:
- entire `02_CHARACTER/` folder,
- exact approved reference images,
- only the active/current reference set.

Do not unnecessarily attach unrelated product files when they do not improve Character generation.

### Copy-ready Character Sheet prompt pattern

```text
You are a Senior Character Designer / Visual Development Artist / LINE Sticker Production Designer.

I attach the complete `02_CHARACTER/` folder and the approved current reference images.

Goal: create one Character Sheet Candidate only. Do not create Hero stickers or the full set.

Before generating:
1. Read all files in `02_CHARACTER/`.
2. Treat CHARACTER_BIBLE.md as Character requirements.
3. Treat CHARACTER_SHEET_SPECIFICATION.md as sheet structure and inspection requirements.
4. Treat CHARACTER_SHEET_GENERATION_PROMPT.md as the primary generation prompt.
5. Apply CHARACTER_SHEET_NEGATIVE_CONSTRAINTS.md.
6. Use CHARACTER_SHEET_APPROVAL_CHECKLIST.md for self-QA.
7. Use attached images as current visual evidence.

Authority rule:
- Owner-locked documented requirements override conflicting visual reference details.
- Do not invent exact age, ethnicity, nationality, profession, rank or unsupported identity facts.
- Keep unknown non-blocking facts unspecified.

Character Sheet must test front, 3/4, side, rear/rear-3/4, face/hair close-up, full-body proportions, expressions, poses/actions, wardrobe states, accessory states and cross-view identity consistency.

Reject your own candidate if canonical views appear to be different people/Characters, if locked identity features drift, or if mandatory Character rules are violated.

Output state: READY_FOR_CHARACTER_OWNER_REVIEW.
Do not declare CHARACTER_SHEET_ACTIVE.
```

### What the AI may decide
- composition of the sheet,
- arrangement of required views,
- visual execution choices within the documented style freedom.

### What it may not decide
- which disputed reference is authoritative,
- new locked Character traits,
- demographic facts not supported by SSOT,
- whether its own output is approved.

---

## 4. Product Owner — Character approval

Human review is mandatory.

Use `CHARACTER_SHEET_APPROVAL_CHECKLIST.md` and compare against both documented locks and current references.

If approved, record:

```text
CHAR-SSOT-XXX vX.Y — CHARACTER_SHEET_ACTIVE
```

Store the approved image and approval record in the repository/set asset structure according to the project naming standard.

If rejected, identify the defect category:
- identity,
- hair,
- proportions,
- wardrobe,
- accessory,
- style,
- unsupported invention,
- cross-view inconsistency.

Revise the candidate; do not compensate later in Hero production.

---

## 5. Gem B — Hero production

### Inputs
- current Production Document Package,
- `CHARACTER_SHEET_ACTIVE`,
- approved current visual references if required,
- no obsolete Character Sheet versions.

### Copy-ready Hero prompt pattern

```text
You are GEM-B — Sticker Visual Producer for MTLineSticker.

Attached:
1. current Production Document Package,
2. CHARACTER_SHEET_ACTIVE,
3. approved current references if supplied.

Goal: create only the Hero frames defined by HERO_PLAN.md.
Do not produce the full 40 stickers yet.

Authority:
- Production Package controls product/communication/QA requirements.
- CHARACTER_SHEET_ACTIVE is the Character Visual SSOT.
- Locked captions must be reproduced exactly.

Before generating:
1. Read HERO_PLAN.md.
2. Read the Hero entries in FRAME_COMMUNICATION_MATRIX.md.
3. Read VISUAL_DIRECTION.md.
4. Read QA_RULES.md and AUTO_REJECT_RULES.md.
5. Validate that the active Character Sheet is present.

For each Hero preserve Character identity, caption accuracy, intended communication, expression/pose logic, accessory states, small-size readability and commercial purpose.

Do not invent Character strategy or rewrite captions.
Do not generate non-Hero frames.

Output state: READY_FOR_VISUAL_OWNER_REVIEW.
Do not declare FULL_PRODUCTION_UNLOCKED.
```

### Hero QA focus
- exact Thai text,
- Character continuity,
- high-frequency utility representation,
- signature/product differentiation,
- emotional warmth,
- humor when required,
- purchase-hook strength,
- production repeatability.

---

## 6. Full production AI

Start only after explicit `FULL_PRODUCTION_UNLOCKED`.

### Recommended method
Produce in controlled batches, commonly one sheet / 10 frames at a time, unless the active set SSOT says otherwise.

For each batch:
1. Load active Character Sheet.
2. Load only the relevant Frame briefs/mapping when practical.
3. Generate candidates.
4. QA Thai captions.
5. QA Character continuity.
6. QA transparency/background requirement.
7. QA safe area/cropping.
8. Approve/revise before next batch.

### Do not
- regenerate Character identity differently per batch,
- change style mid-set,
- improvise captions,
- use old Character Sheet versions,
- hide defects that should be corrected at source.

---

## 7. GitHub — project SSOT and change control

GitHub is not merely backup storage. It is the controlled project truth.

### Store in GitHub
- governing project documents,
- Gem deployment instructions/knowledge,
- set-specific documentation,
- Character SSOT documentation,
- approved visual assets where repository policy permits,
- QA decisions,
- decision logs,
- handoff state,
- pipeline/runbook documents.

### Change workflow
Recommended:

```text
read latest main
→ create branch
→ make small coherent changes
→ inspect diff
→ open PR
→ review / CI if applicable
→ merge
→ verify main SHA
```

Never assume an earlier chat contains the latest repository truth.

---

## 8. Deterministic Engine / Scripts

Use deterministic tooling for repeatable mechanical operations rather than generative judgment.

Typical responsibilities:
- crop/slice,
- resize,
- rename,
- validate dimensions,
- validate alpha/transparency,
- package exports,
- count files,
- detect missing/duplicate assets,
- create checksums,
- build release folders.

If the project has active engine/script standards, those standards outrank ad-hoc AI instructions.

Do not ask an image model to replace deterministic validation when a reliable script exists.

---

## 9. Image editors (Photopea / Photoshop / equivalent)

Use image editors for controlled finishing operations such as:
- checking transparent edges,
- local cleanup,
- canvas/safe-area inspection,
- verifying output dimensions,
- correcting minor export defects where allowed.

Do not use manual editing to conceal a systemic Character-generation defect. If the identity is wrong, fix the source generation/SSOT process.

---

## 10. LINE Creators Market

Use it only after `LINE_SUBMISSION_READY`.

Before submission, verify the current official LINE Creators Market requirements. External platform rules can change, so repository documents should record the source/version/date when a rule is platform-derived.

Prepare current required:
- sticker assets,
- main/tab assets when applicable,
- title,
- description,
- language metadata,
- any other submission metadata required by the platform.

---

## 11. Tool-selection rule of thumb

Use:
- **Gem A** when the problem is product architecture, documentation, caption strategy, commercial planning or handoff logic.
- **Image-generation AI** when creating a visual candidate.
- **Gem B** when producing controlled Hero/full sticker visuals from approved SSOT.
- **GitHub** when recording authoritative project truth and controlled changes.
- **Engine/scripts** when the operation should be deterministic and repeatable.
- **Human Product Owner** when a gate changes authority or unlocks downstream production.

The wrong tool at the wrong stage creates expensive rework.
