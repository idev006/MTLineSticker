# MTLineSticker — Gem Operational Playbook

**Version:** 1.0  
**Status:** Active  
**Scope:** Practical setup and day-to-day use of Gem A and Gem B in the controlled LINE sticker production workflow.

This playbook is the operator-facing guide for using the specialist Gems. Repository SSOT and active set/Character artifacts always outrank chat memory, old examples and AI assumptions.

---

## 1. Canonical production flow

```text
Product Owner brief + current references
        ↓
Gem A — Sticker Product Architect
        ↓
Production Document Package
        ↓
Character Sheet generation (image-generation AI)
        ↓
READY_FOR_CHARACTER_OWNER_REVIEW
        ↓
Product Owner approval
        ↓
CHARACTER_SHEET_ACTIVE
        ↓
Gate A final validation
        ↓
READY_FOR_GEM_B
        ↓
Gem B — Hero production only
        ↓
READY_FOR_VISUAL_OWNER_REVIEW
        ↓
Product Owner Hero approval
        ↓
FULL_PRODUCTION_UNLOCKED
        ↓
Gem B — controlled full production
        ↓
READY_FOR_ENGINE
        ↓
Deterministic Engine / Scripts
        ↓
Final Human QA
        ↓
LINE_SUBMISSION_READY
```

Do not skip Character approval or Hero approval to save time. Those gates exist to prevent multiplying a visual defect across 40 stickers.

---

## 2. Gem A — what it is for

Gem A owns product architecture and documentation. It turns a concise Product Owner brief into an evidence-disciplined Production Document Package.

### Gem A should handle
- target audience / JTBD,
- positioning and differentiation,
- commercial scorecard,
- caption portfolio and lock states,
- 40-frame communication architecture,
- Character Bible and Character Sheet production documents,
- Hero strategy,
- Frame-to-Sheet mapping,
- QA / auto-reject rules,
- handoff manifests and readiness state.

### Gem A must not
- create final Character Sheet artwork,
- self-approve a Character Sheet,
- create final sticker artwork,
- silently resolve disputed reference authority,
- invent unsupported identity facts,
- unlock Gem B when required gates are incomplete.

### Gem A deployment
Use the deployable configuration under:

```text
docs/gems/deploy/gem-a/
```

- put `INSTRUCTION.txt` in the Gem Instructions field,
- attach the five fixed Knowledge files listed by `KNOWLEDGE_MANIFEST.md`,
- do not attach `KNOWLEDGE_MANIFEST.md` itself as Knowledge unless a platform-specific workflow explicitly requires it,
- keep the user runtime prompt concise; Gem A owns internal rigor.

The current Knowledge Manifest is authoritative for active versions. Do not rely on version numbers copied into old chat messages.

---

## 3. Recommended Gem A runtime input

A Product Owner normally supplies:
- target audience,
- product goal,
- concept / positioning,
- Character description,
- exact current reference images,
- owner-locked traits,
- captions or seed captions,
- any explicit constraints that materially change the product.

A useful prompt can remain simple. Do not force the Product Owner to restate internal gate names, manifests or QA fields.

### Gem A acceptance test
Before using its package downstream, verify at minimum:
- `CAPTION_MASTER` is populated for all declared Frames,
- `FRAME_COMMUNICATION_MATRIX` is populated for all declared Frames,
- `FRAME_TO_SHEET_MAPPING` is explicit for all declared Frames,
- missing / duplicate / mismatch evidence is reported,
- commercial analysis is evidence-based,
- unsupported demographics or identity facts were not invented,
- reference-count conflicts were not silently resolved,
- Character Sheet documentation is sufficient for visual SSOT approval,
- current handoff state matches reality.

If Character Sheet approval is still pending, the package must not claim `READY_FOR_GEM_B`.

---

## 4. Character Sheet is a separate controlled stage

The Character Sheet is created **outside Gem A** by an image-generation AI using:

```text
02_CHARACTER/
```

from the current Production Document Package plus the exact approved reference images.

Recommended input files:
- `CHARACTER_BIBLE.md`
- `CHARACTER_SHEET_SPECIFICATION.md`
- `CHARACTER_SHEET_GENERATION_PROMPT.md`
- `CHARACTER_SHEET_NEGATIVE_CONSTRAINTS.md`
- `CHARACTER_SHEET_APPROVAL_CHECKLIST.md`
- current approved person/Character reference images.

Sending the whole `02_CHARACTER/` folder is preferred when the image AI can read it.

---

## 5. Critical rule — lock the final visual style before Character activation

Do not approve a Character Sheet merely because the face and clothes are correct.

`CHARACTER_SHEET_ACTIVE` is the Character **Visual SSOT**, so it should already represent the intended production style closely enough for Gem B to reproduce it consistently.

If the intended final product is, for example:

```text
Soft Anime / Modern Cartoon LINE Sticker Style
```

then the Character Sheet should already show that direction: clean stylized anatomy, sticker-friendly rendering, clear expressions, simplified detail and appropriate small-size readability.

Do **not** activate a semi-photorealistic or overly serious Character Sheet with the expectation that Gem B will later cartoonize it. That creates avoidable identity/style drift.

### Character Sheet approval must cover both
1. **Identity continuity** — face, hair, proportions, wardrobe, accessories and cross-view consistency.
2. **Production style continuity** — level of stylization, line/shading treatment, emotional tone, silhouette and sticker readability.

If either is wrong, revise the Character Sheet before activation.

---

## 6. Reference authority rule

If the Product Owner says there are 5 authoritative images but 6 attachments are observed, AI must not choose which one is supplemental or excluded.

Record:

```text
REFERENCE_COUNT_CONFLICT
Expected: 5
Observed: 6
Owner decision required: identify the authoritative reference set.
```

Only the Product Owner resolves reference authority.

After resolution, use only the confirmed current set downstream. Avoid attaching old or disputed references to Gem B.

---

## 7. Activating the Character Sheet

An image-generation AI may output:

```text
READY_FOR_CHARACTER_OWNER_REVIEW
```

It may not declare its own output active.

After human review, the Product Owner may record an approved asset such as:

```text
CHAR-SSOT-001 v1.0 — CHARACTER_SHEET_ACTIVE
```

Store the approved sheet and approval record according to project/set asset conventions.

Never send an unapproved candidate to Gem B as if it were active.

---

## 8. Gem B — what it is for

Gem B is the controlled visual producer. It executes approved visual briefs; it does not redesign upstream product strategy.

### Gem B may
- choose approved visual execution details,
- compose poses and props inside Frame briefs,
- generate Hero visuals,
- generate full-production sheets after unlock,
- perform visual self-QA.

### Gem B may not
- rewrite locked captions,
- redefine the target audience or product strategy,
- silently redesign `CHARACTER_SHEET_ACTIVE`,
- convert optional traits to mandatory,
- bypass Hero review,
- self-approve `FULL_PRODUCTION_UNLOCKED`,
- claim deterministic LINE export compliance,
- modify engine/scripts as part of visual work.

---

## 9. Gem B deployment

Use:

```text
docs/gems/deploy/gem-b/
```

- `INSTRUCTION.txt` → Gem Instructions,
- five fixed Knowledge files → as listed in `KNOWLEDGE_MANIFEST.md`,
- runtime/project files → only current authoritative set inputs.

The deploy folder, not an old authoring draft, is the implementation-ready configuration.

---

## 10. Recommended Gem B runtime handoff bundle

For Hero production, provide:

1. current `LINE_Sticker_Set*_Production_Document_Package.zip`,
2. approved `CHARACTER_SHEET_ACTIVE`,
3. exact current visual references **only when useful for fidelity checking**,
4. approved Style / Golden Reference when separate from the Character Sheet,
5. optional concise `OWNER_NOTES.md` for current approved execution notes.

Do not attach obsolete Character Sheets or old style experiments.

### If runtime attachment slots are limited
Prefer compact authoritative bundles:
- one Production Package ZIP,
- one active Character Sheet,
- one reference contact sheet or approved reference bundle,
- one Golden/Style Reference,
- one Owner Notes file.

Do not sacrifice authority clarity merely to attach more examples.

---

## 11. Authority hierarchy for Gem B

Normal visual authority:

```text
Repository / active set SSOT
        ↓
Production Document Package
        ↓
CHARACTER_SHEET_ACTIVE
        ↓
Approved separate Style / Golden Reference
        ↓
Approved current raw visual references
        ↓
Conversation suggestions
```

A raw photo can help check likeness but must not silently override a Character lock or active stylized Character Sheet.

If authority conflicts cannot be resolved from active SSOT, stop and request an owner decision.

---

## 12. Copy-ready Gem B Hero prompt

```text
You are GEM-B — Sticker Visual Producer for MTLineSticker.

Attached:
1. current Production Document Package,
2. CHARACTER_SHEET_ACTIVE,
3. approved current references if supplied,
4. approved Style/Golden Reference if supplied,
5. current Owner Notes if supplied.

Goal: create only the Hero Frames declared in HERO_PLAN.md.
Do not produce the full set yet.

Authority:
- Production Package controls product, communication, caption and QA requirements.
- CHARACTER_SHEET_ACTIVE is the Character Visual SSOT.
- Approved separate Style/Golden Reference controls additional style details when it does not conflict with the active Character Sheet.
- Raw references are supplementary fidelity evidence only.

Before generating:
1. Validate the package and current handoff state.
2. Read HERO_PLAN.md.
3. Read Hero entries in FRAME_COMMUNICATION_MATRIX.md.
4. Read VISUAL_DIRECTION.md.
5. Read QA_RULES.md and AUTO_REJECT_RULES.md.
6. Confirm CHARACTER_SHEET_ACTIVE is present.
7. Stop if any unresolved blocker would require invention.

For every Hero:
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

---

## 13. Hero review gate

The Product Owner reviews Hero output for:
- exact Thai text,
- Character consistency,
- visual style consistency,
- face / hair continuity,
- body proportion,
- expression and gesture clarity,
- optional accessory discipline,
- high-frequency usefulness,
- signature concept strength,
- warmth / humor as intended,
- commercial/purchase appeal,
- repeatability across the remaining set.

If the problem is Character identity or global style, fix the source SSOT rather than patching each Hero individually.

Only explicit owner approval may create:

```text
FULL_PRODUCTION_UNLOCKED
```

---

## 14. Full production prompt pattern

Use only after Hero approval:

```text
Continue as GEM-B using the same Production Package and CHARACTER_SHEET_ACTIVE.
Product Owner has approved the Hero system and explicitly set FULL_PRODUCTION_UNLOCKED.

Produce only the next declared production batch according to FRAME_TO_SHEET_MAPPING.md and MASTER_SHEET_PLAN.md.
Preserve the exact approved Character identity, style, caption text, visual language and Hero-calibrated quality.

Run per-Frame and per-Sheet QA before delivery.
Do not silently regenerate failed Frames as different designs; report and correct the defect at source.
```

Default working pattern for a standard 40-frame set is controlled batches / sheets rather than generating all 40 without review, unless active set SSOT explicitly says otherwise.

---

## 15. Example of set-specific Owner Notes

The following is an **example only**, not a global Character rule:

```text
STYLE LOCK:
Soft Anime / Modern Cartoon LINE Sticker Style.
Friendly, mature, warm and commercially sticker-ready; not photorealistic, not chibi.

AGE APPEARANCE:
Adult appearance around 40 years old, if explicitly approved by the Product Owner.

BODY:
Average-fit / proportionate adult male; neither bulky/muscular nor skinny/slender.

HAIR:
Very short police/military-inspired buzz cut; both sides and back extremely short / near-shaved; front hairline clean and sharply defined.
```

Set-specific notes must never be copied into another set unless they are independently approved there.

---

## 16. Common failure modes and recovery

### Gem A package is structurally complete but Character is not approved
Do not send to Gem B as ready. Generate/review Character Sheet first.

### Character Sheet looks too realistic while final stickers should be cartoon-like
Revise the Character Sheet before activation. Do not defer the style transformation to Hero production.

### Gem B begins producing all 40 immediately
Stop. Return to Hero-only scope until owner approval creates `FULL_PRODUCTION_UNLOCKED`.

### Thai caption is wrong
Treat as visual-production defect; regenerate/correct before downstream handoff. Do not ask the engine to repair text embedded in artwork.

### Character changes between batches
Stop production. Compare against `CHARACTER_SHEET_ACTIVE` and the approved Hero system; correct the batch before continuing.

### More reference files are attached than the owner declared
Raise `REFERENCE_COUNT_CONFLICT`; do not guess authority.

### The user changes a locked Character trait after approval
Create a controlled revision / new Character Sheet version and re-evaluate downstream impact. Do not silently mutate the active SSOT.

---

## 17. State cheat sheet

| State | Meaning | Who may authorize / cause it |
|---|---|---|
| `READY_FOR_CHARACTER_OWNER_REVIEW` | Character candidate ready for human review | Character-generation stage |
| `CHARACTER_SHEET_ACTIVE` | approved Character Visual SSOT | Product Owner |
| `READY_FOR_GEM_B` | Gem A package and required visual authority ready | Gate A after requirements pass |
| `READY_FOR_VISUAL_OWNER_REVIEW` | Hero visuals ready for owner review | Gem B after Hero QA |
| `FULL_PRODUCTION_UNLOCKED` | full-set visual production authorized | Product Owner |
| `READY_FOR_ENGINE` | validated visual masters ready for deterministic processing | Gem B / Gate B |
| `LINE_SUBMISSION_READY` | release package passed final required QA | Final release process / human QA |

Never infer an approval state merely because an AI says the work "looks good".

---

## 18. Operating principle

The purpose of the Gem system is not to maximize automation. It is to maximize **commercially useful, visually consistent, auditable sticker production with low rework**.

Use the right intelligence at the right stage:
- Gem A for product architecture,
- image-generation AI for visual candidates,
- Product Owner for authority-changing decisions,
- Gem B for controlled visual production,
- deterministic tooling for mechanical export/validation,
- GitHub for persistent project truth.
