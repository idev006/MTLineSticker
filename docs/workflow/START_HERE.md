# START HERE — MTLineSticker User Roadmap

**Version:** 1.0  
**Status:** Active  
**Audience:** Product Owner / operator who wants to create a LINE sticker set with the least confusion possible.

This is the easiest entry point for the whole project. Follow the roadmap in order. Do not jump ahead unless the required gate is already approved.

## The whole process in one line

```text
Idea → Gem A → Production Package → Character Sheet → Owner Approval → Gem B Hero → Owner Approval → Full 40 → Engine/QA → LINE Submission
```

## Roadmap

| Step | What you do | Tool | What you attach | What you must get before next step |
|---|---|---|---|---|
| 1 | Describe the sticker set | Gem A | brief + current references + captions/seed captions | Production Document Package |
| 2 | Create Character Sheet Candidate | Image AI | `02_CHARACTER/` + approved references | `READY_FOR_CHARACTER_OWNER_REVIEW` |
| 3 | Approve Character Sheet | Product Owner | Candidate + checklist | `CHARACTER_SHEET_ACTIVE` |
| 4 | Create Hero stickers only | Gem B | Production Package + `CHARACTER_SHEET_ACTIVE` + current references | `READY_FOR_VISUAL_OWNER_REVIEW` |
| 5 | Approve Hero set | Product Owner | Hero set + Hero QA | `FULL_PRODUCTION_UNLOCKED` |
| 6 | Create full sticker set | Gem B | approved package + active Character + approved Hero direction | full masters / `READY_FOR_ENGINE` |
| 7 | Prepare release assets | Engine/scripts + human QA | approved masters | `LINE_SUBMISSION_READY` |
| 8 | Submit and learn | LINE Creators Market | final assets + metadata | release + learning notes |

---

## Step 1 — Send the idea to Gem A

### You prepare
- target audience,
- product goal,
- concept,
- Character description,
- current reference images,
- important locked traits,
- 40 captions if available, or ask Gem A to propose them.

### Copy-paste prompt

```text
ช่วยสร้าง Production Document Package สำหรับ LINE Sticker 1 ชุด

เป้าหมาย:
ต้องการสติกเกอร์ที่ใช้ได้จริงในแชตประจำวัน สื่อสารชัด ใช้งานบ่อย มีเอกลักษณ์ และมีศักยภาพขายได้จริงใน LINE Creators Market

กลุ่มเป้าหมาย:
[ใส่กลุ่มเป้าหมาย]

Product Concept:
[ใส่ concept]

Character Source:
ใช้ภาพอ้างอิงที่แนบเป็น visual evidence หลัก

Character Requirements / Owner Locks:
[ใส่ข้อกำหนดสำคัญ]

Captions:
[วาง F01-F40 ถ้ามี หรือระบุให้ Gem A ช่วยเสนอ]

ขอให้ Gem A วิเคราะห์ product / target audience / JTBD / positioning / commercial potential และสร้าง Production Document Package แบบหลายไฟล์ให้ครบตาม governance ของ Gem A

ห้าม invent ข้อมูลที่ไม่มีหลักฐาน
ถ้ายังไม่มี approved Character Sheet ให้ handoff state ต้องไม่เป็น READY_FOR_GEM_B
ถ้ารองรับ ขอผลลัพธ์เป็น ZIP package
```

### Before next step
You should have a package containing folders such as:

```text
00_PACKAGE/
01_PRODUCT/
02_CHARACTER/
03_COMMUNICATION/
04_VISUAL_PRODUCTION/
05_QA/
06_HANDOFF/
```

If the package claims `READY_FOR_GEM_B` while Character Sheet is still missing, stop and return it to Gem A.

---

## Step 2 — Create Character Sheet Candidate

### Attach
Send the whole current:

```text
02_CHARACTER/
```

plus the exact reference images approved for this Character.

Recommended files inside `02_CHARACTER/`:
- `CHARACTER_BIBLE.md`
- `CHARACTER_SHEET_SPECIFICATION.md`
- `CHARACTER_SHEET_GENERATION_PROMPT.md`
- `CHARACTER_SHEET_NEGATIVE_CONSTRAINTS.md`
- `CHARACTER_SHEET_APPROVAL_CHECKLIST.md`

### Important visual rule
The Character Sheet should already look close to the intended final sticker style.

Do not approve a semi-realistic Character Sheet if the final product should be a cartoon. Fix the style now, before activation.

### Copy-paste prompt

```text
คุณคือ Senior Character Designer / Visual Development Artist / LINE Sticker Production Designer

ฉันแนบโฟลเดอร์ `02_CHARACTER/` ทั้งหมด และภาพ reference ที่ยืนยันแล้ว

เป้าหมาย:
สร้าง Character Sheet Candidate เพียง 1 ชุด เพื่อให้ Product Owner ตรวจสอบก่อนอนุมัติ

ก่อนสร้าง:
1. อ่านไฟล์ทั้งหมดใน `02_CHARACTER/`
2. ใช้ CHARACTER_BIBLE.md เป็น Character requirements
3. ใช้ CHARACTER_SHEET_SPECIFICATION.md เป็น sheet structure
4. ใช้ CHARACTER_SHEET_GENERATION_PROMPT.md เป็น prompt หลัก
5. ใช้ CHARACTER_SHEET_NEGATIVE_CONSTRAINTS.md เป็นข้อห้าม
6. ใช้ CHARACTER_SHEET_APPROVAL_CHECKLIST.md เป็น QA checklist
7. ใช้ภาพ reference เป็น visual evidence หลัก

Authority:
- owner-locked documented requirements ชนะรายละเอียดที่ขัดกันใน reference
- ห้าม invent age / ethnicity / nationality / profession / rank หรือ facts ที่ไม่มีหลักฐาน

Character Sheet ต้องทดสอบอย่างน้อย:
front, 3/4, side, rear/rear-3/4, face/hair close-up, full-body proportion, expression range, pose/action range, wardrobe states, accessory states และ cross-view identity consistency

Visual style ต้องตรงกับ final sticker direction ตั้งแต่ Character Sheet
ห้ามคิดว่าจะไปแก้ style ทีหลังใน Gem B

ผลลัพธ์สุดท้าย:
READY_FOR_CHARACTER_OWNER_REVIEW

ห้ามออกสถานะ CHARACTER_SHEET_ACTIVE เอง
```

---

## Step 3 — Product Owner approves Character Sheet

Check at least:
- identity looks like the intended Character,
- all views look like the same Character,
- haircut/hairline are consistent,
- body proportion is correct,
- wardrobe/accessory rules are correct,
- visual style is already correct for sticker production,
- expressions are readable,
- no unsupported details were invented.

If approved, record the asset as for example:

```text
CHAR-SSOT-001_v1.0_CHARACTER_SHEET_ACTIVE.png
```

If not approved, revise the Character Sheet. Do not continue to Hero production hoping Gem B will repair it.

---

## Step 4 — Send the controlled bundle to Gem B

### Attach
Minimum normal bundle:

```text
1. LINE_Sticker_Set1_Production_Document_Package.zip
2. CHAR-SSOT-001_v1.0_CHARACTER_SHEET_ACTIVE.png
3. current approved reference images
4. optional STYLE_REFERENCE / GOLDEN_REFERENCE
5. optional OWNER_NOTES.md
```

### Copy-paste Hero prompt

```text
คุณคือ GEM-B — Sticker Visual Producer ของโครงการ MTLineSticker

ฉันแนบ:
1. current Production Document Package
2. CHARACTER_SHEET_ACTIVE
3. current approved reference images
4. optional style/golden reference or owner notes

Authority:
- Production Package = Product / Communication / QA / Production SSOT
- CHARACTER_SHEET_ACTIVE = Character Visual SSOT
- current reference images = secondary fidelity evidence
- owner-locked requirements override conflicting raw references

เป้าหมายรอบนี้:
สร้างเฉพาะ Hero Sticker Set ตาม HERO_PLAN.md
ห้ามสร้าง Full Production 40 stickers

ก่อนสร้าง:
- อ่าน HERO_PLAN.md
- อ่าน Hero entries ใน FRAME_COMMUNICATION_MATRIX.md
- อ่าน VISUAL_DIRECTION.md
- อ่าน QA_RULES.md และ AUTO_REJECT_RULES.md
- ตรวจว่ามี CHARACTER_SHEET_ACTIVE จริง

สำหรับทุก Hero:
- ใช้ exact caption ตาม lock state
- ภาษาไทยต้องถูกต้อง
- รักษา Character identity / haircut / proportions / wardrobe / accessories ตาม Character Sheet
- รักษา visual style ของ Character Sheet
- expression / pose / silhouette ต้องอ่านได้เร็วในแชต
- ห้าม invent product strategy หรือ Character facts
- ห้ามสร้าง non-Hero frames

Final state:
READY_FOR_VISUAL_OWNER_REVIEW

ห้ามออก FULL_PRODUCTION_UNLOCKED เอง
```

---

## Step 5 — Product Owner approves Hero set

Approve only when:
- Character is consistent across all Hero frames,
- captions are correct,
- style matches the active Character Sheet,
- communication is understandable quickly,
- Hero set represents both high-frequency utility and signature/purchase appeal,
- no recurring defect suggests the full 40 will fail.

If approved, record:

```text
FULL_PRODUCTION_UNLOCKED
```

If not approved, revise only the failed Hero frames or upstream Character Sheet if the defect is systemic.

---

## Step 6 — Full production

### Copy-paste prompt

```text
Hero Set ได้รับ Product Owner approval แล้ว และสถานะคือ FULL_PRODUCTION_UNLOCKED

ให้ GEM-B ดำเนิน Full Production ตาม Production Document Package และ approved Hero direction

กฎ:
- ใช้ CHARACTER_SHEET_ACTIVE เดิม
- ห้ามเปลี่ยน style ระหว่าง batch
- ใช้ exact captions
- ทำตาม FRAME_TO_SHEET_MAPPING
- ทำเป็น controlled batches ตาม MASTER_SHEET_PLAN
- QA ทุก batch ก่อนทำ batch ถัดไป
- failed/rejected frames ต้องแก้ที่ต้นเหตุ ไม่ซ่อน defect

เมื่อ Full Production ผ่าน visual QA และ mapping reconciliation แล้ว ให้ส่งสถานะ READY_FOR_ENGINE
```

---

## Step 7 — Engine / deterministic QA

Use scripts/engine for mechanical and repeatable work such as:
- crop/slice,
- resize,
- rename,
- transparency checks,
- dimensions,
- missing/duplicate file checks,
- checksums,
- packaging/export folders.

Do not ask the engine to fix visual identity, bad captions or wrong Character style.

After final human QA, record:

```text
LINE_SUBMISSION_READY
```

---

## Step 8 — LINE submission and learning

Before submission, verify current official LINE Creators Market requirements because platform rules can change.

After release, record what you learn:
- which stickers are used most,
- which captions are weak,
- which visuals attract attention,
- customer feedback,
- sales/use patterns where available.

Feed those lessons into the next set rather than endlessly tuning documents before release.

---

# Where am I now?

Use this quick state lookup:

| You currently have... | Next action |
|---|---|
| Idea only | Go to Gem A |
| Gem A package, no Character Sheet | Generate Character Sheet Candidate |
| Character Sheet Candidate | Product Owner review |
| `CHARACTER_SHEET_ACTIVE`, package not final-ready | Final Gate A / resolve blockers |
| `READY_FOR_GEM_B` + active Character | Gem B Hero only |
| Hero images | Product Owner Hero review |
| `FULL_PRODUCTION_UNLOCKED` | Full production |
| Full visual masters | Engine / deterministic QA |
| `READY_FOR_ENGINE` | Build final exports |
| `LINE_SUBMISSION_READY` | Submit to LINE |

# Golden rule

```text
If you do not know what to do next, look at the current STATE first.
The STATE tells you the next tool and the next gate.
```

For copy-ready prompts only, see [`COPY_PASTE_PROMPT_LIBRARY.md`](COPY_PASTE_PROMPT_LIBRARY.md).
For deeper rationale, see the other documents in `docs/workflow/` and `docs/gems/`.
