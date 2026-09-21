# STICKER SHEET COOKBOOK v1.1 — SET-009

> **Supersedes:** `STICKER-SHEET-COOKBOOK-v1.0.md`

## Purpose
Execution cookbook สำหรับมนุษย์หรือ AI ที่ต้องสร้าง Sticker Sheet ของ `SET-009-PPR6-SAVINGS-COOP-01` ให้ได้มาตรฐานเดียวกันทุกครั้ง และพร้อมส่งต่อให้ downstream extractor แยกแต่ละ Frame ออกเป็นสติ๊กเกอร์รายตัวแบบ deterministic

เป้าหมายคือ: **คนหรือ AI ที่ไม่เคยเห็นประวัติแชต เมื่ออ่านเอกสารนี้และ normative references แล้ว ต้องสามารถสร้าง, ตรวจ, ซ่อม, และส่งมอบ Sticker Sheet ได้โดยไม่ต้องเดา**

---

## Mandatory Reading Order
1. `SET-009-PRODUCT-SSOT-v1.0.md`
2. `CHARACTER-BIBLE-v1.0.md`
3. `FULL-STICKER-PRODUCTION-TABLE-v1.0.md`
4. `THAI-CAPTION-RENDERING-PROTOCOL-v1.0.md`
5. `PRODUCTION-SPEC-v1.0.md`
6. `CONTENT-QC-PROTOCOL-v1.0.md`
7. `END-TO-END-PRODUCTION-PIPELINE-v1.0.md`

หากข้อกำหนดด้าน Sticker Sheet geometry / Frame / transparency / backing / margin / padding / border ขัดกัน ให้ยึด `PRODUCTION-SPEC-v1.0.md`

หากข้อกำหนดด้าน caption / Thai text / mapping ขัดกัน ให้ยึด `THAI-CAPTION-RENDERING-PROTOCOL-v1.0.md` และ active Production Table

---

## Canonical Definitions
- **Sticker Sheet** = PNG หนึ่งไฟล์ที่รวมหลาย Sticker Frame เป็น grid/matrix
- **Frame** = cell แต่ละช่องใน grid
- **Sticker Artwork** = character + caption + props + effects
- **White Backing / Die-cut Base** = พื้นขาวทึบ 100% รอง artwork ตาม silhouette และไม่มีรูภายใน
- **Downstream Extractor** = โปรแกรมปลายทางที่ตัด Frame ออกจาก sheet ตาม geometry ที่กำหนด
- **Canonical Caption Manifest** = รายการ caption 01–40 ที่ copy จาก active Production Table แบบ exact string

---

## World-Class Acceptance Model
Sticker Sheet ต้องผ่านพร้อมกัน 5 ด้าน:
1. **Character Fidelity** — ตัวละครตรง Visual SSOT
2. **Communication Quality** — pose / expression / prop สื่อ intent ชัด
3. **Thai Language Accuracy** — exact caption, zero error
4. **Production Geometry** — Frame, grid, backing, alpha, margin, padding, border ถูกต้อง
5. **Machine Handoff Reliability** — downstream crop ได้โดยไม่ต้อง OCR หรือเดาขอบ

หาก downstream ต้องซ่อม sheet ก่อนตัด ให้ถือว่า upstream artifact ยังไม่ DONE

---

## Recipe 1 — Lock Inputs
ก่อน generate ต้องล็อก:
- active Character SSOT
- active Production Table
- active Production Spec
- active Thai Caption Rendering Protocol
- grid dimensions
- output version

ห้ามใช้ข้อความจากภาพเก่าหรือจาก memory แทน SSOT

---

## Recipe 2 — Build Canonical Caption Manifest
สร้าง manifest 01–40 จาก Production Table แบบ exact string

กฎ:
- one logical frame = one immutable caption
- row-major mapping
- no frame number printed in artwork
- no paraphrase / rewrite / normalization

ก่อน generate ให้ตรวจ manifest 1 รอบเต็ม

---

## Recipe 3 — Plan Visual Frame
ทุก Frame ต้องกำหนดตาม Production Table:
- Caption
- Intent
- Pose / Gesture
- Facial Expression
- Prop
- Outfit
- Camera / Composition
- QA Note

ห้ามใช้ pose เดิมเพียงเปลี่ยน caption หาก intent ต่างกัน

---

## Recipe 4 — Thai Text Strategy
### Preferred: deterministic overlay
1. Generate artwork โดยไม่สร้าง Thai caption หรือเว้นพื้นที่ caption ไว้
2. Render exact caption ด้วย Unicode Thai text renderer และฟอนต์ที่อนุมัติ
3. รวม caption กับ artwork
4. ทำ visual QC และ Thai Text QC

### Alternative: direct generative text
ใช้ได้เฉพาะเมื่อระบบสามารถสร้าง Thai text ได้ดี และต้อง:
- ป้อน exact caption manifest
- ยืนยัน one-frame-one-caption
- forbid paraphrase / rewrite
- verify rendered caption character-by-character
- reject/regenerate ทุก Frame ที่ mismatch

รายละเอียดทั้งหมดให้ยึด `THAI-CAPTION-RENDERING-PROTOCOL-v1.0.md`

---

## Recipe 5 — Build 5×8 Full Sheet
สำหรับ Full 40:
- columns = 5
- rows = 8
- ordering = row-major
- Frame = 512 × 512 px
- background = transparent
- Frame border ≈ 3 px
- margin = 20 px
- padding = 20 px
- square corners
- no frame number on artwork

ห้าม resize Frame เพื่อให้พอดี canvas

---

## Recipe 6 — White Backing
ทุก sticker ต้องมี:
- opaque solid white 100%
- continuous backing
- ~5 px white die-cut allowance รอบ artwork
- no transparent hole
- no pinhole
- no internal cutout
- no void ระหว่าง character / text / prop ภายใน die-cut base

White backing ไม่ใช่แค่ stroke

---

## Recipe 7 — Preflight Before Render
ต้องตอบ YES ทุกข้อ:
- [ ] Caption Manifest exact match SSOT
- [ ] Frame mapping 01–40 ถูกต้อง
- [ ] Pose/Expression/Prop ตรง Production Table
- [ ] Grid 5×8
- [ ] Frame 512×512
- [ ] Margin/Padding 20 px
- [ ] White backing rule เข้าใจชัด
- [ ] Background transparent
- [ ] ไม่มีเลข Frame บน artwork

---

## Recipe 8 — Post-render QC
### A. Visual QC
ตรวจ character, anatomy, pose, prop, crop, readability, frame contact

### B. Thai Text QC
เทียบทุก caption กับ canonical manifest แบบตัวอักษรต่อตัวอักษร

ผิดแม้ 1 ตัว = REJECT FRAME

ภาษาไทยถูกแต่ไปอยู่ผิด Frame = REJECT FRAME

### C. Technical QC
ตรวจ PNG, alpha, dimensions, Frame geometry, white backing, safe area

---

## Recipe 9 — Repair
หากเสียไม่กี่ Frame:
- regenerate เฉพาะ Frame เสีย
- ห้ามเปลี่ยน Frame ที่ผ่านแล้ว
- reassemble ในตำแหน่งเดิม
- rerun regression QC

หากผิดจำนวนมากหรือ mapping หลุด:
- regenerate whole sheet จาก canonical manifest เดิม
- ห้ามแก้ source captions ให้เข้ากับภาพผิด

---

## Recipe 10 — Machine Handoff Contract
Recommended metadata:

```yaml
set_id: SET-009-PPR6-SAVINGS-COOP-01
sheet_type: full
columns: 5
rows: 8
frame_width: 512
frame_height: 512
ordering: row-major
background: transparent
format: PNG
alpha_required: true
white_backing_required: true
white_backing_internal_holes_allowed: false
caption_source: FULL-STICKER-PRODUCTION-TABLE-v1.0.md
caption_protocol: THAI-CAPTION-RENDERING-PROTOCOL-v1.0.md
production_spec: PRODUCTION-SPEC-v1.0.md
```

Downstream extractor ต้องสามารถคำนวณ crop rectangles จาก metadata/grid โดยไม่ใช้ OCR และไม่แก้ pixel content ภายใน Frame

---

## Release Gate
ห้าม Release ถ้ายังไม่ครบ:
- [ ] Content QC PASS
- [ ] Character Fidelity PASS
- [ ] Visual QC PASS
- [ ] Thai Text QC PASS
- [ ] Technical QC PASS
- [ ] Production Spec PASS
- [ ] Downstream handoff test PASS
- [ ] Owner Approval

---

## AI Execution Directive
AI ที่ได้รับเอกสารนี้ต้องถือว่า Caption เป็น immutable data ไม่ใช่ creative text และต้องแยกงาน `visual generation` ออกจาก `text correctness` ในเชิงตรรกะ แม้ระบบจะ generate พร้อมกันได้ก็ตาม

ลำดับที่ต้องทำ:
`READ SSOT → BUILD CAPTION MANIFEST → MAP 01–40 → PLAN VISUALS → GENERATE → VERIFY THAI EXACTLY → VERIFY GEOMETRY → REPAIR FAILURES → RELEASE`

หากมี uncertainty ใน blocking requirement ให้หยุดที่ QC และห้ามส่งต่อ downstream

---

## Status
**ACTIVE — v1.1**
