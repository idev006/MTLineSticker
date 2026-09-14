# AI & Tool Usage Guide for MTLineSticker

**Version:** 1.1  
**Status:** Active

This guide explains which tool or AI role should be used at each stage, what inputs it receives, what it may decide, where human approval is mandatory, and how authority moves safely from product concept to released sticker assets.

For Gem-specific runtime bundles and copy-ready operating prompts, also see `docs/gems/GEM_OPERATIONAL_PLAYBOOK.md`.

---

## 1. Tool map

| Stage | Primary tool / role | Main input | Main output | Human approval required? |
|---|---|---|---|---|
| Product architecture | Gem A | Product brief, references, captions | Production Document Package | Yes for unresolved decisions |
| Character Sheet generation | Image-generation AI | `02_CHARACTER/` + approved references | Character Sheet Candidate | **Yes** |
| Character activation | Product Owner | Candidate + checklist | `CHARACTER_SHEET_ACTIVE` | **Yes** |
| Gate A final | Gem A / controlled review | Package + active Character Sheet | `READY_FOR_GEM_B` | No if all locked requirements already resolved |
| Hero production | Gem B | Package + active Character Sheet + approved style context | Hero visuals | **Yes** |
| Hero activation | Product Owner | Hero output + QA | `FULL_PRODUCTION_UNLOCKED` | **Yes** |
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
- all declared Frame artifacts are actually populated N/N,
- commercial analysis contains evidence rather than vague adjectives,
- no unsupported demographics or Character facts are invented,
- Character Sheet documentation is complete,
- handoff state matches Character Sheet reality,
- reference-count conflicts are not silently resolved by the AI.

If Character approval is still pending, the package may be useful for Character Sheet generation but must not pretend that `READY_FOR_GEM_B` already exists.

---

## 3. Image-generation AI — Character Sheet Candidate

### Inputs
Recommended:
- entire `02_CHARACTER/` folder,
- exact approved reference images,
- only the active/current reference set.

Do not unnecessarily attach unrelated product files when they do not improve Character generation.

### Character Sheet is both identity SSOT and visual-style SSOT
Do not approve a Character Sheet merely because the face, hair and clothing are correct. The sheet should also closely express the **intended final sticker rendering style**.

For example, if the intended product style is:

```text
Soft Anime / Modern Cartoon LINE Sticker Style
```

then the Character Sheet should already look sticker-ready: stylized, clean, expressive, readable at small size and not overly photorealistic.

**Do not activate an overly realistic or overly serious sheet while expecting Gem B to transform the style later.** Fix the style upstream before activation; otherwise identity/style drift becomes more likely during Hero and full production.

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
- Do not invent exact age, ethnicity, nationality, profession, rank or unsupported identity facts unless the Product Owner explicitly locks them.
- Keep unknown non-blocking facts unspecified.

Character Sheet must test front, 3/4, side, rear/rear-3/4, face/hair close-up, full-body proportions, expressions, poses/actions, wardrobe states, accessory states and cross-view identity consistency.

The Character Sheet must also reflect the intended final sticker visual style closely enough to act as Visual SSOT.
Reject your own candidate if canonical views appear to be different people/Characters, if locked identity features drift, if style drifts across views, or if mandatory Character rules are violated.

Output state: READY_FOR_CHARACTER_OWNER_REVIEW.
Do not declare CHARACTER_SHEET_ACTIVE.
```

### What the AI may decide
- composition of the sheet,
- arrangement of required views,
- visual execution choices inside approved style freedom.

### What it may not decide
- which disputed reference is authoritative,
- new locked Character traits,
- unsupported demographic facts,
- whether its own output is approved.

---

## 4. Product Owner — Character approval

Human review is mandatory.

Use `CHARACTER_SHEET_APPROVAL_CHECKLIST.md` and compare against both documented locks and current references.

Review two dimensions separately:
1. **Identity continuity** — face, haircut, hairline, body proportion, wardrobe, accessories and cross-view consistency.
2. **Production-style continuity** — cartoon/realism level, line/shading treatment, emotional tone, silhouette, expression readability and sticker readiness.

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

## 5. Reference authority and reference-count conflicts

If the Product Owner declares a specific reference set or count and the actual attachments do not match, do not let any AI silently decide which references are primary, supplemental or excluded.

Record the conflict explicitly, for example:

```text
REFERENCE_COUNT_CONFLICT
Expected: 5
Observed: 6
Owner decision required: identify the authoritative reference set.
```

After resolution, downstream production should use only the confirmed current references. Obsolete or disputed references should not accompany Gem B unless there is a documented reason.

---

## 6. Gem B — Hero production

### Required runtime handoff bundle
Recommended:
- current Production Document Package ZIP,
- approved `CHARACTER_SHEET_ACTIVE`,
- exact approved current visual references when useful for fidelity checking,
- approved separate Style / Golden Reference if needed,
- optional current `OWNER_NOTES.md`.

Do **not** attach obsolete Character Sheets, old style experiments or superseded reference sets.

If runtime attachment capacity is limited, prefer compact authoritative files rather than many loosely related examples.

### Authority hierarchy
Normal visual authority is:

```text
Repository / active set SSOT
→ Production Document Package
→ CHARACTER_SHEET_ACTIVE
→ Approved separate Style / Golden Reference
→ Approved current raw references
→ conversational suggestions
```

Raw photos can support likeness checking but must not silently override an active stylized Character Sheet or owner-locked Character rule.

### Copy-ready Hero prompt pattern

```text
You are GEM-B — Sticker Visual Producer for MTLineSticker.

Attached:
1. current Production Document Package,
2. CHARACTER_SHEET_ACTIVE,
3. approved current references if supplied,
4. approved Style/Golden Reference if supplied,
5. current Owner Notes if supplied.

Goal: create only the Hero Frames defined by HERO_PLAN.md.
Do not produce the full set yet.

Authority:
- Production Package controls product/communication/caption/QA requirements.
- CHARACTER_SHEET_ACTIVE is the Character Visual SSOT.
- Approved separate Style/Golden Reference may refine style only when it does not conflict with the active Character Sheet.
- Raw references are supplementary fidelity evidence only.

Before generating:
1. Validate current handoff state and package integrity.
2. Read HERO_PLAN.md.
3. Read Hero entries in FRAME_COMMUNICATION_MATRIX.md.
4. Read VISUAL_DIRECTION.md.
5. Read QA_RULES.md and AUTO_REJECT_RULES.md.
6. Confirm CHARACTER_SHEET_ACTIVE is present.
7. Stop if any blocker would require invention.

For each Hero:
- reproduce locked Thai caption exactly,
- preserve Character identity and active visual style,
- preserve mandatory wardrobe/accessory states,
- use optional accessories only when the Frame brief supports them,
- prioritize 1-second communication clarity,
- keep silhouette and expression readable at sticker size,
- preserve commercial purpose / purchase-hook intent where declared,
- reject identity drift, style drift, caption errors and unsupported additions.

Output only the declared Hero scope.
Final state after successful internal QA:
READY_FOR_VISUAL_OWNER_REVIEW

Do not declare FULL_PRODUCTION_UNLOCKED yourself.
```

### Hero QA focus
- exact Thai text,
- Character continuity,
- visual-style continuity,
- high-frequency utility representation,
- signature/product differentiation,
- emotional warmth,
- humor when required,
- purchase-hook strength,
- production repeatability.

---

## 7. Product Owner — Hero approval

Hero review is an authority-changing gate.

If Hero output proves the Character system, visual language and communication quality are production-ready, the Product Owner may explicitly authorize:

```text
FULL_PRODUCTION_UNLOCKED
```

Do not infer this state merely because Hero images look good or because Gem B asks to continue.

If a Hero exposes a global Character or style defect, correct the source Character Sheet / active visual SSOT before scaling to 40 stickers.

---

## 8. Full production AI

Start only after explicit `FULL_PRODUCTION_UNLOCKED`.

### Recommended method
Produce in controlled batches, commonly one sheet / 10 frames at a time, unless the active set SSOT says otherwise.

For each batch:
1. Load active Character Sheet.
2. Load only the relevant Frame briefs/mapping when practical.
3. Preserve the approved Hero-calibrated visual language.
4. Generate candidates.
5. QA Thai captions.
6. QA Character identity and style continuity.
7. QA transparency/background requirement.
8. QA safe area/cropping.
9. Approve/revise before next batch.

### Copy-ready continuation pattern

```text
Continue as GEM-B using the same Production Package and CHARACTER_SHEET_ACTIVE.
Product Owner has explicitly approved the Hero system and set FULL_PRODUCTION_UNLOCKED.

Produce only the next declared production batch according to FRAME_TO_SHEET_MAPPING.md and MASTER_SHEET_PLAN.md.
Preserve the exact approved Character identity, style, caption text, visual language and Hero-calibrated quality.

Run per-Frame and per-Sheet QA before delivery.
Report defects instead of hiding them or silently changing the design system.
```

### Do not
- regenerate Character identity differently per batch,
- change style mid-set,
- improvise captions,
- use old Character Sheet versions,
- hide defects that should be corrected at source.

---

## 9. Set-specific Owner Notes

`OWNER_NOTES.md` may be useful when the current approved visual direction needs concise clarification without changing global Gem rules.

Example only:

```text
STYLE LOCK:
Soft Anime / Modern Cartoon LINE Sticker Style.
Friendly, mature, warm, polished and sticker-ready; not photorealistic, not chibi.

AGE APPEARANCE:
Adult appearance around 40 years old, only when explicitly approved for this Character.

BODY:
Average-fit / proportionate adult male; neither bulky/muscular nor skinny/slender.

HAIR:
Very short buzz cut; sides and back extremely short / near-shaved; front hairline clean and sharply defined.
```

Set-specific notes must not leak into unrelated projects or Characters.

---

## 10. GitHub — project SSOT and change control

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

## 11. Deterministic Engine / Scripts

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

## 12. Image editors (Photopea / Photoshop / equivalent)

Use image editors for controlled finishing operations such as:
- checking transparent edges,
- local cleanup,
- canvas/safe-area inspection,
- verifying output dimensions,
- correcting minor export defects where allowed.

Do not use manual editing to conceal a systemic Character-generation defect. If the identity or global style is wrong, fix the source generation/SSOT process.

---

## 13. LINE Creators Market

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

## 14. State cheat sheet

| State | Meaning | Authority |
|---|---|---|
| `READY_FOR_CHARACTER_OWNER_REVIEW` | Character candidate ready for human review | Character-generation stage |
| `CHARACTER_SHEET_ACTIVE` | approved Character Visual SSOT | Product Owner |
| `READY_FOR_GEM_B` | package + required active visual authority ready | Gate A |
| `READY_FOR_VISUAL_OWNER_REVIEW` | Hero output ready for owner review | Gem B after Hero QA |
| `FULL_PRODUCTION_UNLOCKED` | full visual production authorized | Product Owner |
| `READY_FOR_ENGINE` | validated visual masters ready for deterministic processing | Gem B / Gate B |
| `LINE_SUBMISSION_READY` | final release package passed required QA | final release process |

---

## 15. Tool-selection rule of thumb

Use:
- **Gem A** when the problem is product architecture, documentation, caption strategy, commercial planning or handoff logic.
- **Image-generation AI** when creating a Character Sheet Candidate or other controlled visual candidate.
- **Product Owner** when approval changes authority or unlocks downstream work.
- **Gem B** when producing controlled Hero/full sticker visuals from approved SSOT.
- **GitHub** when recording authoritative project truth and controlled changes.
- **Engine/scripts** when the operation should be deterministic and repeatable.

The wrong tool at the wrong stage creates expensive rework.
