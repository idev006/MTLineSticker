# COPY-PASTE Prompt Library — MTLineSticker

**Version:** 1.0  
**Status:** Active

This file is intentionally practical. Copy the prompt for the stage you are in, replace the bracketed fields, attach the listed files, and run it.

---

## Prompt A — Start a new set in Gem A

Attach:
- current reference images,
- captions if already available.

```text
ช่วยสร้าง Production Document Package สำหรับ LINE Sticker 1 ชุด

กลุ่มเป้าหมาย:
[ใส่กลุ่มเป้าหมาย]

เป้าหมาย:
ต้องการสติกเกอร์ที่ใช้ได้จริงในแชตประจำวัน สื่อสารชัด ใช้งานบ่อย มีเอกลักษณ์ และมีศักยภาพขายได้จริงใน LINE Creators Market

Product Concept:
[ใส่ concept]

Character Source:
ใช้ภาพอ้างอิงที่แนบเป็น visual evidence หลักของตัวละคร

Character Requirements / Owner Locks:
[ใส่ข้อกำหนดสำคัญ]

Captions:
[วาง F01-F40 หรือระบุว่าให้ Gem A ช่วยเสนอ]

ให้วิเคราะห์ target audience, JTBD, positioning, differentiation, commercial potential และสร้าง Production Document Package ตาม governance ของ Gem A

ห้าม invent ข้อมูลที่ไม่มีหลักฐาน
ถ้ายังไม่มี approved Character Sheet ห้าม READY_FOR_GEM_B
ถ้ารองรับ ขอผลลัพธ์เป็น ZIP package
```

---

## Prompt B — Create Character Sheet Candidate

Attach:
- entire `02_CHARACTER/`,
- exact approved current reference images.

```text
คุณคือ Senior Character Designer / Visual Development Artist / LINE Sticker Production Designer

ฉันแนบ `02_CHARACTER/` ทั้งโฟลเดอร์ และภาพ reference ที่ยืนยันแล้ว

สร้าง Character Sheet Candidate เพียง 1 ชุด
ห้ามสร้าง Hero Sticker หรือ Full Production

ก่อนสร้าง:
1. อ่านทุกไฟล์ใน `02_CHARACTER/`
2. CHARACTER_BIBLE.md = Character requirements
3. CHARACTER_SHEET_SPECIFICATION.md = sheet structure
4. CHARACTER_SHEET_GENERATION_PROMPT.md = primary generation prompt
5. CHARACTER_SHEET_NEGATIVE_CONSTRAINTS.md = forbidden / rejection rules
6. CHARACTER_SHEET_APPROVAL_CHECKLIST.md = self-QA
7. reference images = visual evidence

Owner-locked documented requirements override conflicting raw references.
ห้าม invent unsupported age, ethnicity, nationality, profession, rank หรือ identity facts

ต้องทดสอบ front, 3/4, side, rear/rear-3/4, face/hair close-up, full-body proportion, expressions, poses/actions, wardrobe/accessory states และ cross-view consistency

Visual style ของ Character Sheet ต้องใกล้เคียง final sticker style ที่ต้องการแล้ว
ห้ามหวังให้ Gem B มาแก้ style ทีหลัง

Output state:
READY_FOR_CHARACTER_OWNER_REVIEW

ห้ามประกาศ CHARACTER_SHEET_ACTIVE เอง
```

---

## Prompt C — Revise Character Sheet style

Use when identity is acceptable but the sheet is too realistic, too serious, too young, too muscular, etc.

```text
ปรับ Character Sheet Candidate นี้ โดยคง identity และ owner locks เดิมทั้งหมด

แก้เฉพาะประเด็นต่อไปนี้:
[ใส่รายการ เช่น]
- ให้เป็น Soft Anime / Modern Cartoon LINE Sticker Style มากขึ้น
- ไม่ photorealistic
- ไม่ดูจริงจังเกินไป
- ลุคผู้ใหญ่ประมาณช่วงอายุ 40 ตาม owner direction
- รูปร่างสมส่วน ไม่ผอม ไม่บึกบึน
- ด้านข้างและด้านหลังผมสั้นเกรียนมากคล้ายโกน
- hairline ด้านหน้าคม สะอาด
- clean outline
- simplified shading
- sticker-friendly expression and silhouette

ห้ามเปลี่ยน Character identity, wardrobe logic, mandatory accessories หรือข้อกำหนดอื่นที่ไม่ได้ขอแก้

ผลลัพธ์ยังเป็น Character Sheet Candidate
สถานะ READY_FOR_CHARACTER_OWNER_REVIEW
```

---

## Prompt D — Gem B Hero Production

Attach:
- current Production Document Package ZIP,
- `CHARACTER_SHEET_ACTIVE`,
- current approved references,
- optional style/golden reference or owner notes.

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
- raw references = secondary fidelity evidence

เป้าหมายรอบนี้:
สร้างเฉพาะ Hero Sticker Set ตาม HERO_PLAN.md
ห้ามสร้าง Full Production 40 stickers

ก่อนสร้าง:
- อ่าน HERO_PLAN.md
- อ่าน Hero entries ใน FRAME_COMMUNICATION_MATRIX.md
- อ่าน VISUAL_DIRECTION.md
- อ่าน QA_RULES.md และ AUTO_REJECT_RULES.md
- ตรวจ active Character Sheet

ทุก Hero ต้อง:
- ใช้ exact caption
- ภาษาไทยถูกต้อง
- รักษา identity / haircut / proportions / wardrobe / accessories
- รักษา visual style ของ Character Sheet
- expression / pose / silhouette อ่านง่ายในแชต
- ห้าม invent product strategy หรือ Character facts
- ห้ามสร้าง non-Hero frames

Final state:
READY_FOR_VISUAL_OWNER_REVIEW

ห้าม FULL_PRODUCTION_UNLOCKED เอง
```

---

## Prompt E — Revise failed Hero only

```text
แก้เฉพาะ Hero Frames ต่อไปนี้:
[ใส่ Frame IDs]

ใช้ Production Package และ CHARACTER_SHEET_ACTIVE เดิมเป็น SSOT
ห้ามแก้ caption ที่ locked
ห้าม redesign Character
ห้ามเปลี่ยน style ทั้งชุด

Defects ที่ต้องแก้:
[ใส่ defect ต่อ frame เช่น identity drift / Thai typo / wrong watch wrist / weak expression / visual clutter]

หลังแก้ให้ทำ self-QA เฉพาะ frame ที่แก้และรายงาน PASS / RISK / REJECT
สถานะยังคง READY_FOR_VISUAL_OWNER_REVIEW จนกว่า Product Owner จะ approve
```

---

## Prompt F — Full Production after Hero approval

Use only after the Product Owner explicitly records `FULL_PRODUCTION_UNLOCKED`.

```text
Product Owner อนุมัติ Hero Set แล้ว
Current state: FULL_PRODUCTION_UNLOCKED

ให้ GEM-B ดำเนิน Full Production ตาม Production Document Package, CHARACTER_SHEET_ACTIVE และ approved Hero direction

กฎ:
- exact captions only
- follow FRAME_TO_SHEET_MAPPING
- follow MASTER_SHEET_PLAN
- keep Character and style consistent across all batches
- optional accessories only when frame brief supports them
- QA each batch before moving to the next
- failed frames must be corrected at source

เมื่อ Full Production ผ่าน visual QA และ mapping reconciliation แล้ว ส่งสถานะ READY_FOR_ENGINE
```

---

## Prompt G — Continue next batch only

```text
ดำเนินการเฉพาะ batch ถัดไปตาม MASTER_SHEET_PLAN

ใช้ SSOT เดิมทั้งหมด:
- Production Document Package
- CHARACTER_SHEET_ACTIVE
- approved Hero visual direction

ห้ามเปลี่ยน Character/style/captions
หลังสร้าง batch นี้ ให้ QA caption, identity, proportions, accessories, composition, safe area และ consistency ก่อนจบงาน
```

---

## Prompt H — Ask AI to audit a package before use

```text
ตรวจ Production Document Package นี้ก่อนนำไปใช้ downstream

ตรวจอย่างน้อย:
- Caption Master actual N/N
- Frame Communication Matrix actual N/N
- Frame-to-Sheet Mapping actual N/N
- missing / duplicate / mismatch
- commercial scorecard evidence
- Character Sheet documentation completeness
- unsupported invention / context contamination
- reference authority conflicts
- Hero Plan readiness
- handoff status correctness

สรุปเป็น PASS / RISK / BLOCKER และระบุ next action ที่ต้องทำ
```

---

## Prompt I — Owner approval record for Character Sheet

Use only when the Product Owner has personally approved the candidate.

```text
Product Owner Decision:
Character Sheet Candidate นี้ได้รับอนุมัติให้เป็น Character Visual SSOT สำหรับชุดนี้

Asset ID:
CHAR-SSOT-[ID]_v[VERSION]

State:
CHARACTER_SHEET_ACTIVE

Effective from:
[date/version]

Any future visual production must follow this active Character Sheet unless a newer owner-approved version replaces it.
```

---

## Prompt J — Owner approval record for Hero

```text
Product Owner Decision:
Hero Sticker Set นี้ได้รับอนุมัติ

State transition:
READY_FOR_VISUAL_OWNER_REVIEW
→ FULL_PRODUCTION_UNLOCKED

Gem B may proceed to controlled Full Production according to the active Production Package, CHARACTER_SHEET_ACTIVE, approved Hero direction and QA rules.
```

---

# Which prompt do I use?

| Current situation | Use prompt |
|---|---|
| New idea / new set | A |
| Need Character Sheet | B |
| Character Sheet style wrong | C |
| Character active, need Hero | D |
| Some Hero frames failed | E |
| Hero approved, create all stickers | F |
| Continue one production batch | G |
| Need audit before continuing | H |
| Approve Character Sheet | I |
| Approve Hero and unlock full production | J |

If unsure, check [`START_HERE.md`](START_HERE.md) first.
