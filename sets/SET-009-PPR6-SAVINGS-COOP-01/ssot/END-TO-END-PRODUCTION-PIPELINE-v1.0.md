# END-TO-END PRODUCTION PIPELINE v1.0 — SET-009

## Purpose
กำหนด workflow สำหรับทีมงานตั้งแต่ต้นน้ำจนปลายน้ำของชุด **สหกรณ์ออมทรัพย์ตำรวจภูธรภาค 6 หมายเลข 1** เพื่อให้ทุกคนใช้ขั้นตอนเดียวกัน มีจุดตรวจ (gate) ชัดเจน และลดความผิดพลาดด้านคอนเทนต์ ภาพ ภาษาไทย และสเปกการผลิต

## Core Principle
**Document First → Design → Review → Produce → QC → Approve → Export → Archive**

ห้ามข้าม Gate ที่กำหนด

---

## STAGE 0 — Project Initialization
### Owner / Project Lead
- ยืนยันชื่อชุด รหัสชุด วัตถุประสงค์ กลุ่มเป้าหมาย และช่องทางใช้งาน
- ยืนยัน repository และโฟลเดอร์ SSOT
- กำหนด Character Sheet ที่เป็น Visual SSOT

### Required Artifacts
- `SET-009-PRODUCT-SSOT-v1.0.md`
- `PROJECT-CREATIVE-BRIEF-v1.0.md`
- `CHARACTER-BIBLE-v1.0.md`

### Gate 0 — Project Lock
ผ่านเมื่อ Product Owner ยืนยัน scope และ character direction

---

## STAGE 1 — Character Lock
### Creative / Senior Graphic Designer
- ตรวจ Character Sheet เทียบ Character Bible
- ล็อก silhouette, proportion, สี, หงอน, หาง, สีหน้า, signature outfit
- กำหนด accessory ที่อนุญาตและไม่อนุญาต
- ตรวจว่า character สามารถต่อยอดเป็น sticker, plush, keychain, mug และ merchandise อื่นได้

### Gate 1 — Character Approval
ห้ามเข้าสู่การผลิต Hero หาก Character Sheet ยังไม่ถูกยืนยันเป็น Visual SSOT

---

## STAGE 2 — Content Architecture
### Marketing + Strategy + Copy Team
- ออกแบบรายการ 40 เฟรม
- กำหนด Caption, Intent, Usage Scenario และกลุ่มผู้ใช้
- ต้องครอบคลุมเจ้าหน้าที่สหกรณ์และสมาชิกสหกรณ์
- ให้ everyday utility เป็นแกนหลัก และเสริม service / savings / activity / warm relationship

### Required Artifact
- `CONTENT-ARCHITECTURE-v0.1.md`

---

## STAGE 3 — Frame-Level Visual Planning
### Creative Team
สำหรับทุกเฟรมกำหนด:
- Caption
- Intent
- Pose / Gesture
- Facial Expression
- Prop
- Outfit
- Camera / Composition
- Merchandise suitability
- QA note

### Required Artifact
- `FULL-STICKER-PRODUCTION-TABLE-v1.0.md`

---

## STAGE 4 — Content QC
### QC Team
ตรวจครบทั้งชุดในมิติ:
1. Caption duplication
2. Semantic / Intent overlap
3. Pose / silhouette overlap
4. Facial-expression overlap
5. Prop repetition
6. Usage coverage

จัดสถานะทุกเฟรมเป็น:
- KEEP
- REWORK
- REPLACE

### Required Artifacts
- `CONTENT-QC-PROTOCOL-v1.0.md`
- `CONTENT-QC-REPORT-v1.0.md`

### Gate 2 — Content Lock
ห้ามเริ่ม Full Production หากยังมี blocking REWORK / REPLACE

---

## STAGE 5 — Thai Caption Verification
### Thai Copy QC
**ZERO ERROR RULE**

ก่อนสร้างภาพต้องตรวจ Approved Caption ทุกเฟรมแบบตัวอักษรต่อตัวอักษร:
- พยัญชนะ
- สระ
- วรรณยุกต์
- การันต์
- เว้นวรรค
- เครื่องหมาย
- คำลงท้าย
- `สอ.ภ.6` และข้อความองค์กร

ห้าม AI ดัดแปลง ปรับคำ หรือสะกดใหม่เอง

### Gate 3 — Caption Lock
Caption ที่ไม่ผ่านการตรวจภาษาไทยห้ามส่งเข้า Image Production

---

## STAGE 6 — Hero Calibration
### Visual Production Team
ผลิต Hero 6–12 เฟรมเพื่อทดสอบ:
- Character fidelity
- สีและ lighting
- อ่านอารมณ์ได้ทันที
- Text readability
- Pose diversity
- Prop scale
- White backing quality
- Sticker Sheet geometry

### Gate 4 — Hero Approval
Product Owner ต้องอนุมัติ Hero ก่อน Full 40

---

## STAGE 7 — Full Sticker Production
### Visual Production Team
ผลิต artwork ตาม Production Table ที่ล็อกแล้ว

ข้อบังคับ:
- ไม่แก้ Caption เอง
- ไม่เปลี่ยน pose / prop / intent โดยไม่มี change note
- ยึด Character Sheet เป็น Visual SSOT
- ทุกเฟรมต้องพร้อมสำหรับ white backing และ die-cut

---

## STAGE 8 — Sticker Sheet Assembly
### Production / Layout Team
Apply `PRODUCTION-SPEC-v1.0.md` ทุกครั้ง

### Mandatory Sheet Spec
- PNG
- Transparent background
- Grid ตามจำนวนเฟรม
- Frame = 512 × 512 px
- Frame border ≈ 3 px
- Margin = 20 px
- Padding = 20 px
- มุมฉาก
- ไม่มีเลขกำกับเฟรม
- Sticker ห้ามชน frame border

### Mandatory White Backing Spec
- Solid opaque white 100%
- ต่อเนื่องเต็มชิ้น
- ไม่มีรู ไม่มีช่องว่าง ไม่มี pinhole
- ขอบขาวรอบ artwork ≈ 5 px
- ห้ามตีความเป็นเพียง white outline

---

## STAGE 9 — Image QC
### Graphic QA
ตรวจอย่างน้อย:
- Character consistency
- Pose ตรง Production Table
- Expression ตรง Intent
- Prop ถูกต้อง
- ไม่มี anatomy defect
- ไม่มี crop / overlap ผิด
- Sticker ไม่ชน frame
- Sheet background transparent จริง
- White backing solid 100%

### Gate 5 — Visual QC
พบ defect ใด ๆ ต้อง REJECT และแก้ก่อนขั้นถัดไป

---

## STAGE 10 — Thai Text QC on Rendered Image
### Thai Copy QC
อ่านข้อความจากภาพที่ render แล้วเทียบกับ Approved Caption ทุกเฟรม

**ผิดแม้เพียง 1 ตัวอักษร = REJECT**

รวมถึงต้องตรวจว่าไม่มี:
- ตัวอักษรหาย
- วรรณยุกต์ผิดตำแหน่ง
- ตัวอักษรซ้อน
- คำขาด
- คำถูกสร้างเพิ่ม
- `สอ.ภ.6` ผิด

### Gate 6 — Text QC PASS
ห้ามส่งออก final หากยังไม่ได้ PASS

---

## STAGE 11 — Final Owner Review
### Product Owner
ตรวจ:
- ภาพรวมทั้งชุด
- ความหลากหลายของการใช้งาน
- ภาพลักษณ์องค์กร
- Hero consistency
- Caption accuracy
- Sticker Sheet spec

### Gate 7 — Owner Approval
ต้องมี Owner approval ก่อน Final Export

---

## STAGE 12 — Final Export
### Production Team
จัดเตรียม:
- Final Sticker Sheets
- Individual frames (ถ้าต้องใช้)
- LINE upload assets
- Main image / Tab image ตาม requirement
- Merchandise-ready selected poses

ทุก final artifact ต้องผ่าน QA ก่อน release

---

## STAGE 13 — Archive & Traceability
### Project Lead
เก็บ:
- SSOT documents
- Approved Production Table
- QC reports
- Approved Hero reference
- Final sheet version
- Revision notes
- Owner approval status

ห้ามใช้ไฟล์ draft หรือไฟล์ rejected เป็น production source

---

## Change Control
หากมีการเปลี่ยน Caption / Pose / Prop / Outfit / Character / Production Spec หลัง Lock:
1. เปิด Change Note
2. ระบุเหตุผล
3. ประเมินผลกระทบ
4. QC เฉพาะส่วนที่กระทบและ regression check ส่วนที่เกี่ยวข้อง
5. Update SSOT version
6. Product Owner อนุมัติใหม่

---

## Team Responsibility Summary
- **Product Owner** — final decision / approval
- **Project Lead** — SSOT, workflow, traceability
- **Marketing / Strategy** — usage coverage, target fit
- **Thai Copy Team** — caption correctness and naturalness
- **Senior Graphic Designer** — character, pose, visual language
- **Production Artist** — artwork execution
- **Layout / Prepress** — sheet geometry, backing, transparency
- **QC Team** — content, visual, technical, language checks

---

## Non-Negotiable Blocking Rules
- ห้ามภาษาไทยผิด
- ห้าม white backing มีรูหรือช่องโปร่งใส
- ห้ามสติ๊กเกอร์ชน frame
- ห้าม background ของ Sticker Sheet ไม่โปร่งใส
- ห้ามข้าม Content QC
- ห้ามข้าม Hero Approval
- ห้ามข้าม Thai Text QC หลัง render
- ห้ามใช้ caption / pose ที่ไม่ได้มาจาก Production SSOT

## Production Status Flow
`DRAFT → CONTENT REVIEW → CONTENT LOCK → HERO → HERO APPROVED → FULL PRODUCTION → IMAGE QC → THAI TEXT QC → OWNER REVIEW → FINAL APPROVED → RELEASED`
