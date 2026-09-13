# Production Document Package Template

**Version:** 1.0  
**Purpose:** Standard handoff package from Gem A (Sticker Product Architect) to Gem B (Sticker Visual Producer)

---

## 0. Package Header

- `SET_ID:`
- `PRODUCT_NAME:`
- `VERSION:`
- `OWNER:`
- `HANDOFF_STATUS:`
- `TOTAL_FRAMES:`
- `STICKER_TYPE:`
- `TARGET_RELEASE:`

Accepted handoff status to Gem B: `READY_FOR_GEM_B`

---

## 1. Product Concept

### Core concept

### Product promise

### Primary use context

### Target audience

### JTBD / communication territory

### Differentiation from existing sets

---

## 2. Character / Style SSOT

- `CHARACTER_SSOT:`
- `STYLE_SSOT:`
- `GOLDEN_REFERENCE:`
- `INHERITED_FROM:`

### Locked identity traits

### Approved exceptions

### Prohibited drift

---

## 3. Caption Architecture

### Caption principles

### Tone rules

### Diversity / redundancy rules

### Approved caption list

| Frame ID | Caption | Intent | Category | Status |
|---|---|---|---|---|
| F001 |  |  |  | LOCKED |

---

## 4. Frame Communication Matrix

Complete one block per Frame.

### FRAME F001
- `CAPTION:`
- `SENDER_INTENT:`
- `CHAT_SITUATION:`
- `EMOTION_TONE:`
- `PRIMARY_EXPRESSION:`
- `PRIMARY_GESTURE_ACTION:`
- `MINIMUM_PROPS:`
- `CAMERA_GUIDANCE:`
- `COMPOSITION_GUIDANCE:`
- `CHARACTER_REFERENCE:`
- `STYLE_REFERENCE:`
- `FORBIDDEN_TRAITS:`
- `ONE_SECOND_TEST_EXPECTATION:`
- `HERO:` YES / NO
- `NOTES:`

Repeat through final Frame ID.

---

## 5. Hero Plan

- `HERO_FRAME_IDS:`
- `ANCHOR_HERO_ID:`
- `SEQUENTIAL_GATE_REQUIRED:` YES / NO

### Hero purpose matrix

| Hero | What it tests | Pass condition |
|---|---|---|
|  |  |  |

### Hero Gate outcome values
- PASS
- PASS_WITH_CORRECTION
- FAIL
- BLOCKED

---

## 6. Master Frame / Sticker Sheet Plan

### Frame profile
- `MASTER_FRAME_WIDTH:` 512
- `MASTER_FRAME_HEIGHT:` 512
- `MASTER_FORMAT:` PNG / RGBA preferred when applicable
- `SAFE_PADDING_TARGET:`
- `QUALITY_TARGET:` High-resolution clean master suitable for resize-down

### Sheet profile
- `SHEET_GRID_COLUMNS:` 5
- `SHEET_GRID_ROWS:` 2
- `FRAMES_PER_SHEET:` 10
- `LOGICAL_SHEET_WIDTH:` 2560
- `LOGICAL_SHEET_HEIGHT:` 1024
- `FRAME_ORDER:` row-major unless explicitly overridden
- `CROSS_FRAME_BLEED:` PROHIBITED

### Sheet mapping

| Sheet ID | Frame IDs |
|---|---|
| S01 | F001–F010 |

---

## 7. Visual Production Rules

### Communication hierarchy

### Character fidelity rules

### Camera / composition rules

### Prop density rules

### Typography handling

### Background / transparency intent

### Visual variety requirements

---

## 8. Quality Gates

### Gate A — Documentation / Product Architecture
Pass criteria:

### Gate B — Visual Master
Pass criteria:

### Gate C — Technical Engine Handoff
Gem A does not certify technical compliance; list only expected downstream handoff fields.

### Final Human QA
Expected review scope:

---

## 9. Auto-Reject Conditions

Examples:
- wrong Character identity
- altered caption
- unclear primary intent
- chibi drift when not approved
- cluttered scene
- infographic/poster treatment
- Frame boundary violation
- wrong Sheet geometry
- insufficient resolution / master quality

Add set-specific blockers below:

---

## 10. Responsibility Matrix

| Work item | Owner |
|---|---|
| Concept / product architecture | Gem A |
| Caption / Frame intent | Gem A |
| Character/style visual execution | Gem B |
| Master Frame / Sheet visual generation | Gem B |
| Visual QA | Gem B + Owner Gate as specified |
| Split / resize / technical normalization | Existing Program / Engine |
| Technical validation / packaging | Existing Program / Engine |
| Final release decision | Human/Product Owner |

**Restriction:** AI documentation work must not modify existing Python, engine, scripts, validators, or packaging code unless the Product Owner explicitly opens a separate software-development task.

---

## 11. Handoff Manifest

- `PACKAGE_VERSION:`
- `SOURCE_DOCUMENTS:`
- `CHARACTER_REFERENCE_FILES:`
- `STYLE_REFERENCE_FILES:`
- `CAPTION_LOCK_STATUS:`
- `FRAME_MATRIX_COMPLETE:` YES / NO
- `HERO_PLAN_COMPLETE:` YES / NO
- `SHEET_PLAN_COMPLETE:` YES / NO
- `QA_RULES_COMPLETE:` YES / NO
- `UNRESOLVED_ISSUES:` NONE / list
- `HANDOFF_STATUS:` READY_FOR_GEM_B / BLOCKED / OWNER_DECISION_REQUIRED / SSOT_CONFLICT

### Gem A sign-off statement
> I have completed the Product Architecture blackbox, performed internal QA, and confirm that Gem B can execute visual production from this package without inventing product strategy.

---

## 12. Machine-Readable Companion Schema

Use this compact field structure when a structured companion is needed:

```text
SET_ID:
PRODUCT_NAME:
VERSION:
TOTAL_FRAMES:
MASTER_FRAME_SIZE: 512x512
SHEET_GRID: 5x2
CHARACTER_SSOT:
STYLE_SSOT:
GOLDEN_REFERENCE:
HERO_FRAMES:

FRAME_001:
  caption:
  intent:
  chat_situation:
  emotion_tone:
  expression:
  gesture_action:
  props:
  camera:
  composition:
  forbidden:
  one_second_test:

QA_RULES:
AUTO_REJECT:
OUTPUT_REQUIREMENTS:
HANDOFF_STATUS:
```

The human-readable Production Document Package remains authoritative unless the project explicitly designates a different formal SSOT.
