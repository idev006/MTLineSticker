# COPY-PASTE Prompt Library — MTLineSticker

**Version:** 1.1  
**Status:** Active  
**Principle:** attach the listed files, copy the prompt, and let the specialist guide the next step.

If unsure where you are, send `show roadmap` or read [`START_HERE.md`](START_HERE.md).

---

## A — Start a new set in Gem A

Attach:
- current Character/person references,
- captions if already available.

```text
Create a Production Document Package for one LINE sticker set.

Target audience:
[enter audience]

Goal:
Create a sticker set that is useful in real chats, quickly understood, repeatedly usable, distinctive, and commercially credible.

Product concept:
[enter concept]

Character / Owner Locks:
[enter required traits]

Captions:
[paste captions or ask Gem A to propose them]

Use only current input, current attachments and active SSOT as source truth.
Guide me step by step. Ask only for decisions actually needed to continue.
At the end, tell me the current state, what files were produced, and give me a copy-paste prompt for the next stage.
```

---

## B — Create Character Sheet Candidate

Attach:
- complete current `02_CHARACTER/`,
- exact approved current references.

```text
Create one Character Sheet Candidate only.
Do not create Hero or Full Production.

Read every file in 02_CHARACTER/ and use it as the production specification.
Use attached references as current visual evidence.
Owner-locked requirements override conflicting raw-reference details.

Test front, 3/4, side, rear/rear-3/4, face/hair close-up, full-body proportions, expressions, poses/actions, wardrobe/accessory states and cross-view consistency.

The Character Sheet visual style should already be close to the intended final sticker style.
Do not defer a major style transformation to Gem B.

Output:
READY_FOR_CHARACTER_OWNER_REVIEW

Do not self-declare CHARACTER_SHEET_ACTIVE.
```

---

## C — Revise Character Sheet

```text
Revise this Character Sheet Candidate while preserving the approved identity and owner locks.

Change only:
[list requested changes]

Do not change unrelated traits.
The result remains a Character Sheet Candidate.
Output:
READY_FOR_CHARACTER_OWNER_REVIEW
```

---

## D — Gem B Hero Production

Attach:
1. current Production Document Package ZIP,
2. `CHARACTER_SHEET_ACTIVE`,
3. current approved style/golden/reference assets only when needed.

```text
The attached ZIP is the current Production Document Package.

Use archive / Code Interpreter / Data Analysis capability to extract it first.
Do not use Knowledge Search alone to infer ZIP contents.
Do not use prior-chat set-specific facts to reconstruct Hero IDs, captions or readiness.

Use CHARACTER_SHEET_ACTIVE as the primary Character Visual SSOT.

Please guide me through this step:
1. show a short current-step / input-status summary,
2. extract the ZIP and report required files found/missing,
3. validate READY_FOR_GEM_B,
4. if valid, create only the Hero scope declared by the current package,
5. run Hero visual QA,
6. stop at READY_FOR_VISUAL_OWNER_REVIEW,
7. tell me exactly whether to reply `approve hero` or how to request a revision.

Do not create Full Production until I explicitly approve Hero.
```

---

## E — Revise failed Hero only

```text
Revise only these Hero Frames:
[Frame IDs]

Defects:
[defect per frame]

Use the same current Production Package and CHARACTER_SHEET_ACTIVE.
Do not change locked captions, Character identity or the whole-set style.
Run QA on the revised frames.
Keep status READY_FOR_VISUAL_OWNER_REVIEW until owner approval.
```

---

## F — Approve Hero

Use only after the Product Owner has reviewed the Hero set.

```text
approve hero
```

Expected transition:

```text
READY_FOR_VISUAL_OWNER_REVIEW
→ FULL_PRODUCTION_UNLOCKED
```

Gem B should confirm the approval and show the next production step before continuing.

---

## G — Full Production

```text
continue

FULL_PRODUCTION_UNLOCKED has been approved by the Product Owner.
Proceed with controlled Full Production using the current Production Package, CHARACTER_SHEET_ACTIVE and approved Hero direction.
Follow FRAME_TO_SHEET_MAPPING and MASTER_SHEET_PLAN.
Keep exact captions and visual continuity.
QA every batch before moving on.
```

---

## H — Continue next batch only

```text
continue next batch only

Use the same active SSOT.
Create only the next declared batch/sheet.
QA caption mapping, Character identity, style, proportions, accessories, composition and sheet consistency before delivery.
```

---

## I — Audit before continuing

```text
Audit the current Production Package before downstream use.
Check actual N/N Caption Master, Frame Communication Matrix, Frame-to-Sheet Mapping, missing/duplicate/mismatch, commercial evidence, Character Sheet documentation, current-source discipline, reference-authority conflicts, Hero readiness and handoff state.
Summarize PASS / RISK / BLOCKER.
If something stops progress, give the shortest recovery action and a copy-paste continue command.
```

---

## J — Character Sheet approval record

Use only after the Product Owner has personally approved the candidate.

```text
Product Owner Decision:
This Character Sheet Candidate is approved as the Character Visual SSOT.

Asset ID:
CHAR-SSOT-[ID]_v[VERSION]

State:
CHARACTER_SHEET_ACTIVE

Future visual production must follow this version until a newer owner-approved version replaces it.
```

---

# Quick selector

| Situation | Prompt |
|---|---|
| New set | A |
| Create Character Sheet | B |
| Fix Character Sheet | C |
| Character approved, create Hero | D |
| Fix Hero | E |
| Approve Hero | F |
| Full Production | G |
| One next batch | H |
| Audit | I |
| Approve Character Sheet | J |

## Simple navigation commands

Both specialist Gems should understand:

```text
status
next
continue
show roadmap
what do you need from me?
what is blocking?
```

Gem B additionally:

```text
approve hero
revise hero
```
