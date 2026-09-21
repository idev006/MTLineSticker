# THAI CAPTION RENDERING PROTOCOL v1.0 — SET-009

## Purpose
กำหนดวิธีสร้างข้อความภาษาไทยบน Sticker Sheet ให้ถูกต้องแบบ **ZERO ERROR** และทำซ้ำได้โดยมนุษย์หรือ AI โดยไม่อาศัยการเดา การจำจากแชต หรือการให้โมเดลแต่งข้อความใหม่เอง

เอกสารนี้เป็นข้อกำหนดบังคับสำหรับทุกงาน Hero / Full / Revision ที่มีข้อความภาษาไทย

---

## Core Rule — Canonical Caption Only
แหล่งข้อความที่อนุญาตมีเพียง `FULL-STICKER-PRODUCTION-TABLE-v1.0.md` หรือเวอร์ชัน active ที่ Owner อนุมัติเท่านั้น

- ห้าม paraphrase
- ห้ามย่อคำ
- ห้ามเพิ่มคำ
- ห้ามตัดคำ
- ห้ามแก้เว้นวรรคเอง
- ห้ามเปลี่ยนคำลงท้าย
- ห้ามแก้ `สอ.ภ.6`
- ห้ามใช้ข้อความจากภาพรุ่นก่อนเป็น source

ผิดแม้ 1 ตัวอักษร = REJECT FRAME

---

## Canonical Caption Manifest
ก่อนสร้างภาพต้องสร้างรายการ Caption 01–40 แบบ row-major จาก Production Table และใช้รายการเดียวกันตลอดงาน

โครงสร้างแนะนำ:

```yaml
captions:
  01: "สวัสดีครับ"
  02: "ขอบคุณครับ"
  03: "รับทราบครับ"
  ...
  40: "สุขภาพแข็งแรงนะครับ"
```

กฎ:
- key เป็น logical frame index เท่านั้น ไม่ต้องพิมพ์เลขลงบน artwork
- string ต้อง copy จาก SSOT แบบ exact string
- ห้ามแก้ manifest ระหว่าง generate โดยไม่มี Change Note

---

## Why the Latest Successful Sheet Matters
รอบที่ข้อความถูกต้องทุกแคปชั่นมี pattern สำคัญที่ต้องรักษา:
1. ใช้รายการข้อความที่กำหนดชัดเจนล่วงหน้า
2. ใช้หนึ่ง Caption ต่อหนึ่ง Frame
3. กำหนดลำดับ Frame แบบ row-major ชัดเจน
4. เน้นคำสั่งว่า Thai caption ต้องตรง exact string และห้ามสะกดใหม่เอง
5. สร้างทั้งชุดภายใต้บริบทเดียวกัน ทำให้ mapping ของข้อความต่อ Frame มีความสม่ำเสมอ
6. ตรวจผลลัพธ์หลัง render และถือความผิดพลาดด้านข้อความเป็น blocking defect

อย่างไรก็ตาม การสร้างตัวอักษรด้วย generative image ยังมีความแปรปรวน จึงต้องมี deterministic fallback ตามด้านล่าง

---

## Preferred Production Method — Deterministic Text Overlay
สำหรับงานระดับ production แนะนำให้แยก `visual artwork` กับ `Thai text` ออกจากกัน

### Phase A — Generate Visual Artwork
- สร้าง character / pose / prop / expression โดยไม่มี caption หรือเว้นพื้นที่ caption ไว้
- ห้ามสร้างตัวอักษรมั่วหรือ pseudo-text ในพื้นที่ caption

### Phase B — Render Thai Caption Deterministically
- นำ exact caption จาก Canonical Caption Manifest มาวางด้วย text renderer จริง
- ใช้ฟอนต์ภาษาไทยที่ทีมอนุมัติ
- render ด้วย UTF-8/Unicode text engine
- คงข้อความแบบ exact string
- ปรับเพียง typography เช่น size, line break, outline, shadow โดยห้ามเปลี่ยนตัวอักษร

### Phase C — Visual Composition
- รวม artwork + caption + prop + white backing
- ตรวจ safe area และ frame border ตาม `PRODUCTION-SPEC-v1.0.md`

**เหตุผล:** วิธีนี้ลดความเสี่ยงการสะกดภาษาไทยผิดจากการให้ image model สร้างตัวอักษรโดยตรง และทำให้ผลลัพธ์ repeatable มากกว่า

---

## Allowed Alternative — Direct Generative Text
ใช้ได้เมื่อระบบ image generation สามารถสร้าง Thai text ได้ดีและต้องการงานเร็ว แต่ต้องผ่านกฎต่อไปนี้:

1. ให้ model รับ exact caption list ทั้งหมดก่อน generate
2. บังคับ one-frame-one-caption mapping
3. ระบุชัดว่า `DO NOT paraphrase / rewrite / translate / abbreviate`
4. ห้ามใส่หมายเลข Frame ลงใน artwork
5. หลัง render ต้องตรวจทุก Frame เทียบ manifest
6. Frame ใดผิด = REJECT และ regenerate Frame นั้นหรือ regenerate whole sheet
7. ห้ามปล่อย downstream แม้ผิดเพียง 1 ตัวอักษร

---

## Thai Text QC Checklist
ตรวจทุก Caption หลัง render:
- [ ] พยัญชนะครบ
- [ ] สระครบและถูกตำแหน่ง
- [ ] วรรณยุกต์ครบและถูกตำแหน่ง
- [ ] การันต์ถูกต้อง
- [ ] คำลงท้ายถูกต้อง
- [ ] เว้นวรรคตรง SSOT
- [ ] เครื่องหมายตรง SSOT
- [ ] `สอ.ภ.6` ถูกต้อง
- [ ] ไม่มีตัวอักษรเกิน
- [ ] ไม่มีตัวอักษรหาย
- [ ] ไม่มี pseudo-Thai glyph
- [ ] ไม่มีข้อความจาก Frame อื่นหลุดมา

---

## Frame Mapping QC
ภาษาไทยถูกแต่ไปอยู่ผิด Frame = REJECT เช่นเดียวกับการสะกดผิด

ต้องตรวจ:
- Frame 01 = Caption 01
- Frame 02 = Caption 02
- ...
- Frame 40 = Caption 40

Ordering = left-to-right, top-to-bottom (row-major)

---

## Repair Strategy
เมื่อพบ Caption ผิด:

### Preferred
- regenerate เฉพาะ Frame ที่ผิด โดยคง caption exact string และ visual intent เดิม
- assemble กลับเข้า sheet โดยไม่เปลี่ยน pixel geometry ของ Frame อื่น

### If multiple frames fail
- regenerate whole sheet จาก canonical manifest เดียวกัน
- ห้ามแก้ caption ระหว่างรอบ

### Never
- ห้ามยอมรับคำที่ “ใกล้เคียง”
- ห้ามใช้ OCR auto-correction เป็น authority
- ห้ามแก้ source caption เพื่อให้ตรงกับภาพที่ generate ผิด

---

## Release Gate
Sticker Sheet จะผ่าน `THAI TEXT QC PASS` ได้เมื่อ:
- Caption ทุก Frame exact-match SSOT
- Mapping ทุก Frame ถูกต้อง
- ไม่มีภาษาไทยผิดแม้ 1 ตัวอักษร
- ไม่มี pseudo-text หรือ glyph ผิดรูป

หากไม่ผ่านข้อใดข้อหนึ่ง ห้ามส่งเข้า downstream extractor และห้ามถือว่าเป็น final artifact

---

## AI Instruction Block
AI ที่อ่านเอกสารนี้ให้ปฏิบัติดังนี้:

> Use only the canonical Thai captions from the active Production Table. Treat each caption as immutable UTF-8 text. Do not paraphrase, rewrite, abbreviate, translate, or normalize wording. Maintain one-to-one row-major mapping between logical Frame index and caption. Prefer deterministic Thai text overlay after artwork generation. If Thai text is generated directly in the image, verify every rendered caption character-by-character against the canonical manifest. Any mismatch, missing glyph, extra glyph, incorrect tone mark, spacing error, or wrong frame mapping is a blocking defect and must be regenerated before release.

---

## Status
**ACTIVE / MANDATORY for SET-009**
