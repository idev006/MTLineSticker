# Production Runbook & Gates

**Version:** 1.0  
**Status:** Active  
**Purpose:** Operational checklist for running one LINE sticker set through the MTLineSticker production pipeline.

---

## 1. Run start

Before any work:

- Read latest `main` from GitHub.
- Identify the active set and active Character/Style SSOT.
- Confirm current Product Owner brief.
- Confirm the exact current reference set.
- Remove obsolete/duplicate references from the working context.
- Confirm whether captions are LOCKED, DRAFT or SEED.
- Confirm whether a Character Sheet already exists and whether it is ACTIVE.

If any of the above is ambiguous, record the ambiguity rather than guessing.

---

## 2. Gate 0 — Product brief ready

### Must have
- product concept,
- target audience,
- intended chat use,
- Character concept/reference,
- caption source or caption-generation permission,
- explicit owner locks/forbidden traits if any.

### PASS when
A reasonable product architect can understand what is being sold and to whom without inventing strategy.

### FAIL / stop when
- audience is unknown and material,
- concept contradicts owner constraints,
- reference ownership/authority is ambiguous,
- captions claimed as locked are incomplete or conflicting.

---

## 3. Gate 1 — Gem A package acceptance

### Required artifacts
Check all folders `00_PACKAGE` through `06_HANDOFF`.

### 40-frame reconciliation
For a 40-frame set verify:

```text
CAPTION_MASTER
Expected: 40
Distinct: 40
Missing: 0
Duplicate: 0

FRAME_COMMUNICATION_MATRIX
Expected: 40
Distinct: 40
Missing: 0
Duplicate: 0

FRAME_TO_SHEET_MAPPING
Expected: 40
Distinct: 40
Missing: 0
Duplicate: 0

Cross-file mismatch: 0
```

### Commercial acceptance
`COMMERCIAL_SCORECARD.md` must include:
- per-caption Frequency/Breadth/Naturalness score,
- RepeatUseScore,
- High/Medium/Low counts and IDs,
- portfolio category counts/percentages,
- differentiation,
- signature territory,
- ranked purchase hooks,
- redundancy risk,
- commercial risks,
- recommendations that preserve locked source truth.

### Character documentation acceptance
`02_CHARACTER/` must be detailed enough to generate and judge a Character Sheet candidate.

### Reference authority acceptance
If expected and observed reference count differs:
- status = `REFERENCE_COUNT_CONFLICT`,
- do not let AI choose the authoritative subset,
- Product Owner must resolve it.

### PASS state
Package may proceed to Character Sheet generation even if final handoff remains `OWNER_DECISION_REQUIRED` due to missing Character Sheet.

---

## 4. Gate 2 — Character Sheet candidate ready

### Input package to image AI
- complete `02_CHARACTER/` folder,
- exact current approved reference images.

### Candidate must include
- front,
- 3/4,
- side,
- rear/rear-3/4,
- face/hair close-up,
- full body,
- expressions,
- poses/actions,
- wardrobe states,
- mandatory/optional accessory states.

### Auto-reject conditions
- faces look like different people across views,
- hairline/haircut changes materially,
- body proportions drift,
- owner-locked facial hair rule violated,
- mandatory accessory placement wrong,
- optional accessory made permanent,
- unsupported demographic traits invented,
- forbidden tactical/military drift appears without authorization.

### Candidate state
`READY_FOR_CHARACTER_OWNER_REVIEW`

---

## 5. Gate 3 — Character activation

### Product Owner review checklist
- identity fidelity,
- hair fidelity,
- face proportions,
- body proportions,
- wardrobe logic,
- accessory logic,
- personality/tone,
- cross-view consistency,
- suitability for small sticker production.

### PASS action
Record explicit approval and version.

Example:

```text
CHAR-SSOT-001 v1.0
STATE: CHARACTER_SHEET_ACTIVE
APPROVED_BY: Product Owner
```

### FAIL action
Return to Character Sheet generation with defect-specific correction instructions.

Do not proceed to Hero production on a rejected or unapproved sheet.

---

## 6. Gate 4 — READY_FOR_GEM_B

### Must have
- accepted Gem A package,
- active Character Sheet,
- resolved blocking reference conflicts,
- Hero plan,
- QA rules,
- explicit mappings,
- no blocking open item.

### PASS state
`READY_FOR_GEM_B`

---

## 7. Gate 5 — Hero production

### Produce only Hero frames
Use `HERO_PLAN.md` as the authoritative selection.

### For every Hero verify
- exact caption,
- intended use case,
- expression,
- pose/action,
- props,
- Character consistency,
- optional/mandatory accessory rules,
- readability,
- commercial purpose.

### Hero review categories
1. Utility Hero
2. Relationship/emotional Hero
3. Signature concept Hero
4. Humor/memorable Hero
5. difficult continuity/pose/prop Hero as needed

### Output state
`READY_FOR_VISUAL_OWNER_REVIEW`

---

## 8. Gate 6 — Hero owner approval

### Product Owner questions
- Would I recognize the Character immediately?
- Does the sticker communicate in about one second?
- Is Thai text exact?
- Does the set feel distinct enough to buy?
- Are high-frequency frames easy to use?
- Are signature frames memorable?
- Can this visual system be repeated across 40 frames?

### PASS state
`FULL_PRODUCTION_UNLOCKED`

### FAIL
Revise Hero frames. If the defect is systemic, return to Character Sheet or Gem A rather than patching all future frames.

---

## 9. Gate 7 — Full production batches

### Recommended batch strategy
For a standard 40 set:

```text
Batch 1: F01–F10
Batch 2: F11–F20
Batch 3: F21–F30
Batch 4: F31–F40
```

Use the actual mapping file if the set differs.

### Batch QA before next batch
- 10 expected frames present,
- Frame IDs correct,
- captions exact,
- no duplicate/missing frame,
- Character consistent,
- no accessory drift,
- no clipping/cross-frame bleed,
- background/transparency correct,
- visual variety sufficient,
- one-second communication preserved.

Do not defer obvious defects until all 40 are complete.

---

## 10. Gate 8 — Full-set visual QA

### Set-level checks
- all required frames present,
- no duplicated pose pattern excessive enough to feel repetitive,
- no visual style drift between sheets,
- Character identity stable,
- palette stable,
- text treatment stable,
- emotional range matches plan,
- signature frames visually strong,
- utility frames remain simple/readable.

### Exit state
`READY_FOR_ENGINE`

---

## 11. Gate 9 — Engine / technical preparation

Run deterministic validators/builders where available.

### Validate
- file count,
- file names,
- dimensions,
- alpha/transparency,
- output format,
- safe-area/crop,
- checksums if used,
- package completeness.

### Defect routing
- visual defect → visual production,
- caption defect → source Frame/caption artifact,
- mapping defect → Gem A/package,
- export/tooling defect → engine/scripts,
- Character systemic defect → Character Sheet owner stage.

Do not fix the wrong layer.

---

## 12. Gate 10 — Final human QA

Review final exported assets at actual intended viewing size.

### Mandatory checks
- Thai spelling 100%,
- no clipped glyphs,
- no accidental background,
- no broken alpha edges,
- no draft/candidate asset,
- correct final count,
- correct main/tab assets if required,
- correct title/description/metadata,
- Character and commercial quality preserved after export.

### PASS state
`LINE_SUBMISSION_READY`

---

## 13. Submission and archive

After submission:
- record submission date/version,
- store release package/reference,
- record any LINE review feedback,
- update set status,
- preserve approved source masters,
- avoid overwriting released SSOT without versioning.

---

## 14. Defect escalation matrix

| Defect | Owning stage | Correct action |
|---|---|---|
| Weak audience/positioning | Gem A / Product | revise Product architecture |
| Weak/generic captions | Gem A / Product Owner | recommendation + owner decision |
| Wrong identity | Character Sheet | regenerate/reapprove Character |
| Character drift in Hero | Gem B or Character Sheet | determine local vs systemic defect |
| Wrong Thai caption | Frame/production | correct source/candidate |
| Missing frame | Mapping/production | reconcile IDs and regenerate |
| Wrong transparency | production/engine | source or export correction |
| Wrong dimensions | engine/export | deterministic correction |
| Reference conflict | Product Owner | resolve authority |
| AI invented facts | originating AI stage | remove invention and regenerate docs/assets |

---

## 15. Recovery rules

### If AI output is poor
Do not immediately add more prompt text. First determine whether the defect is:
- missing SSOT,
- conflicting SSOT,
- wrong reference set,
- unclear Frame brief,
- model execution defect.

Fix the owning input first.

### If multiple batches drift
Stop full production. Re-check `CHARACTER_SHEET_ACTIVE`, visual direction and Gem B prompt. Do not continue accumulating drift.

### If owner changes Character locks mid-project
Create a new Character/SSOT version. Re-evaluate already approved Hero/full assets; do not silently apply the new rule only to later frames.

### If platform requirements change
Update the relevant standards document with source/date/version. Do not rewrite historical released artifacts as if the new rule always existed.

---

## 16. End-of-run evidence packet

A complete production run should be reconstructable from:
- Product Owner brief,
- Gem A package,
- reference set,
- Character Sheet candidate(s),
- Character approval record,
- Hero candidates,
- Hero approval record,
- full production masters,
- QA results,
- engine/export outputs,
- final release package,
- submission/release notes.

If the team cannot reconstruct why an asset was approved, the process is not sufficiently controlled.
