# END-TO-END PRODUCTION PIPELINE v1.0 — SET-009

## Purpose
กำหนด workflow สำหรับทีมงานตั้งแต่ต้นน้ำจนปลายน้ำของชุด **สหกรณ์ออมทรัพย์ตำรวจภูธรภาค 6 หมายเลข 1** เพื่อให้ทุกคนใช้ขั้นตอนเดียวกัน มีจุดตรวจ (gate) ชัดเจน และลดความผิดพลาดด้านคอนเทนต์ ภาพ ภาษาไทย และสเปกการผลิต

เอกสารนี้มีวัตถุประสงค์เชิงปฏิบัติว่า **ไม่ว่าใครจะเข้ามารับช่วงงานในอนาคต หากอ่าน Pipeline นี้และเอกสารอ้างอิงบังคับที่ระบุไว้ จะต้องสามารถสร้าง ตรวจ และส่งมอบสติ๊กเกอร์ได้ตามมาตรฐานเดียวกัน โดยไม่ต้องอาศัยความรู้ที่อยู่ในตัวบุคคล ความทรงจำ คำบอกเล่า หรือบริบทจากแชตเดิม**

ดังนั้น Pipeline ต้องทำหน้าที่เป็นทั้ง:
- ลำดับขั้นตอนการทำงานตั้งแต่ต้นน้ำถึงปลายน้ำ
- แผนที่ชี้ไปยัง SSOT ที่ต้องอ่านในแต่ละขั้น
- นิยาม Gate / Acceptance / Rejection ที่ใช้ตัดสินงาน
- คู่มือส่งต่องานให้บุคคลหรือทีมใหม่
- กลไกป้องกันความรู้สูญหายเมื่อเปลี่ยนคนทำงาน

### Self-Sufficient Execution Standard
ผู้ปฏิบัติงานที่ไม่เคยเห็นโครงการนี้มาก่อนต้องสามารถตอบคำถามต่อไปนี้จากเอกสารได้โดยไม่ต้องถามเจ้าของงาน:
1. กำลังผลิตอะไร เพื่อใคร และใช้ในบริบทใด
2. Character ที่ถูกต้องต้องหน้าตาและมีบุคลิกอย่างไร
3. 40 เฟรมต้องใช้ Caption / Intent / Pose / Expression / Prop ใด
4. Caption ภาษาไทยฉบับอนุมัติคือข้อความใดแบบตัวอักษรต่อตัวอักษร
5. Sticker Sheet, Frame, White Backing, Margin, Padding และ Frame Border หมายถึงอะไร
6. ขนาดและรูปแบบไฟล์ที่ต้องผลิตคืออะไร
7. จุดใดถือว่า PASS / REJECT / REWORK
8. ต้อง QC อะไรก่อนส่งต่อขั้นถัดไป
9. Artifact ใดคือฉบับ Active/Approved และห้ามใช้ Draft ใด
10. เมื่อมีการเปลี่ยนแปลงต้องบันทึกและอนุมัติอย่างไร

หากเอกสารใดไม่สามารถตอบคำถามที่จำเป็นต่อการผลิตได้ ให้ถือว่า documentation ยังไม่สมบูรณ์และต้องแก้เอกสารก่อนผลิตต่อ

## Core Principle
**Document First → Design → Review → Produce → QC → Approve → Export → Archive**

ห้ามข้าม Gate ที่กำหนด

---

## Normative Reference — Sticker Sheet Production Spec
เอกสาร `PRODUCTION-SPEC-v1.0.md` เป็น **Normative / Mandatory Reference** สำหรับทุกขั้นตอนที่เกี่ยวข้องกับ Sticker Sheet, Frame, Layout, White Backing, Die-cut Base, Transparency, Margin, Padding และ Frame Border

### Mandatory Rule
- สมาชิกทีมทุกคนที่เกี่ยวข้องกับ Visual Production, Layout, Prepress, QC และ Final Export ต้องอ่าน `PRODUCTION-SPEC-v1.0.md` ก่อนเริ่มงาน
- ห้ามใช้ความเข้าใจจากความจำหรือคำอธิบายปากเปล่าแทนเอกสาร Production Spec
- หากข้อความใน workflow นี้ขัดกับ `PRODUCTION-SPEC-v1.0.md` ให้ยึด `PRODUCTION-SPEC-v1.0.md` เป็นข้อกำหนดหลักด้าน Sticker Sheet/Frame
- หาก Production Spec มีเวอร์ชันใหม่ที่ Owner อนุมัติ ต้อง update reference ใน pipeline และใช้เวอร์ชันใหม่ทันที

### Canonical Terminology
คำต่อไปนี้ให้ใช้ตามนิยามใน `PRODUCTION-SPEC-v1.0.md` เท่านั้น:
- **Sticker Sheet** = ไฟล์ PNG หนึ่งไฟล์ที่รวมสติ๊กเกอร์หลายตัวในรูปแบบกริด
- **Frame** = เซลล์แต่ละช่องของกริดใน Sticker Sheet
- **White Backing / Die-cut Base** = พื้นสีขาวทึบเต็มรูปทรงรองรับ artwork สำหรับไดคัท ไม่ใช่เพียงเส้น outline
- **Frame Border** = เส้นกรอบสี่เหลี่ยมมุมฉากที่แบ่งแต่ละ Frame
- **Margin / Padding** = ระยะเว้นตามค่าที่ล็อกใน Production Spec

### Mandatory Pre-production Check
ก่อนสร้าง Hero Sheet, Full Sticker Sheet หรือ Revision Sheet ทีมต้องเปิดตรวจ `PRODUCTION-SPEC-v1.0.md` และยืนยันว่าเข้าใจนิยามและ Acceptance/Rejection Criteria ล่าสุดแล้ว

---

## Mandatory Reading Order for New Team Members
ผู้ที่เข้ามารับงานใหม่ต้องอ่านตามลำดับนี้ก่อนเริ่มผลิต:
1. `END-TO-END-PRODUCTION-PIPELINE-v1.0.md`
2. `SET-009-PRODUCT-SSOT-v1.0.md`
3. `PROJECT-CREATIVE-BRIEF-v1.0.md`
4. `CHARACTER-BIBLE-v1.0.md` และ Character Sheet ที่ Owner ยืนยันเป็น Visual SSOT
5. `FULL-STICKER-PRODUCTION-TABLE-v1.0.md`
6. `CONTENT-QC-PROTOCOL-v1.0.md` และ `CONTENT-QC-REPORT-v1.0.md`
7. `PRODUCTION-SPEC-v1.0.md`
8. Approved Hero reference และ revision/change notes ล่าสุดถ้ามี

ห้ามเริ่มผลิตหากเอกสารที่ Pipeline ระบุว่า Required/Active สูญหาย ไม่ชัดเจน หรือมีหลายเวอร์ชันโดยไม่รู้ว่าเวอร์ชันใดเป็นฉบับใช้งาน

---

## STAGE 0 — Project Initialization
### Owner / Project Lead
- ยืนยันชื่อชุด รหัสชุด วัตถุประสงค์ กลุ่มเป้าหมาย และช่องทางใช้งาน
- ยืนยัน repository และโฟลเดอร์ SSOT
- กำหนด Character Sheet ที่เป็น Visual SSOT
- ยืนยัน Production Spec ที่ active สำหรับชุดนี้

### Required Artifacts
- `SET-009-PRODUCT-SSOT-v1.0.md`
- `PROJECT-CREATIVE-BRIEF-v1.0.md`
- `CHARACTER-BIBLE-v1.0.md`
- `PRODUCTION-SPEC-v1.0.md`

### Gate 0 — Project Lock
ผ่านเมื่อ Product Owner ยืนยัน scope, character direction และ active Production Spec

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

ทุกการวางองค์ประกอบต้องเผื่อข้อจำกัดจาก `PRODUCTION-SPEC-v1.0.md` ตั้งแต่ขั้นออกแบบ เช่น พื้นที่ปลอดภัย, padding, white backing และการไม่ชน Frame Border

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
ก่อนเริ่มสร้าง Hero ต้องอ่าน `PRODUCTION-SPEC-v1.0.md` อีกครั้ง และใช้เป็น checklist ระหว่างสร้างภาพ

ผลิต Hero 6–12 เฟรมเพื่อทดสอบ:
- Character fidelity
- สีและ lighting
- อ่านอารมณ์ได้ทันที
- Text readability
- Pose diversity
- Prop scale
- White backing quality
- Sticker Sheet geometry
- ความถูกต้องตามนิยาม Sticker Sheet / Frame / White Backing

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
- ต้องออกแบบให้อยู่ภายใน safe area ตาม Frame/Margin/Padding ใน `PRODUCTION-SPEC-v1.0.md`

---

## STAGE 8 — Sticker Sheet Assembly
### Production / Layout Team
**ต้องเปิดและ Apply `PRODUCTION-SPEC-v1.0.md` ทุกครั้ง ห้ามทำจากความจำ**

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

### Required Layout Sign-off
ก่อนส่ง Image QC ผู้จัดทำ Sticker Sheet ต้องตรวจ checklist จาก `PRODUCTION-SPEC-v1.0.md` ครบทุกข้อ และยืนยันว่าไม่มี requirement ใดถูกตีความเองนอกเอกสาร

---

## STAGE 9 — Image QC
### Graphic QA
QC ต้องใช้ `PRODUCTION-SPEC-v1.0.md` เป็น reference หลักด้าน geometry และ technical acceptance

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
- Frame 512 × 512 px
- Margin/Padding ถูกต้อง
- Frame border ถูกต้อง
- ไม่มีหมายเลขกำกับ

### Gate 5 — Visual QC
พบ defect ใด ๆ หรือผิด Rejection Criteria ใน `PRODUCTION-SPEC-v1.0.md` ต้อง REJECT และแก้ก่อนขั้นถัดไป

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
- Sticker Sheet spec โดยอ้างอิง `PRODUCTION-SPEC-v1.0.md`

### Gate 7 — Owner Approval
ต้องมี Owner approval ก่อน Final Export

---

## STAGE 12 — Final Export
### Production Team
ก่อน export ต้องตรวจ active Production Spec version อีกครั้ง

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
- Active `PRODUCTION-SPEC` version ที่ใช้ผลิต
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
6. หากเปลี่ยน Production Spec ต้องตรวจ Hero/Full Sheet ที่เกี่ยวข้องใหม่ตาม requirement ที่เปลี่ยน
7. Product Owner อนุมัติใหม่

---

## Team Responsibility Summary
- **Product Owner** — final decision / approval
- **Project Lead** — SSOT, workflow, traceability
- **Marketing / Strategy** — usage coverage, target fit
- **Thai Copy Team** — caption correctness and naturalness
- **Senior Graphic Designer** — character, pose, visual language
- **Production Artist** — artwork execution
- **Layout / Prepress** — sheet geometry, backing, transparency โดยยึด `PRODUCTION-SPEC-v1.0.md`
- **QC Team** — content, visual, technical, language checks

---

## Non-Negotiable Blocking Rules
- ห้ามภาษาไทยผิด
- ห้าม white backing มีรูหรือช่องโปร่งใส
- ห้ามสติ๊กเกอร์ชน frame
- ห้าม background ของ Sticker Sheet ไม่โปร่งใส
- ห้ามตีความ Sticker Sheet / Frame / White Backing นอกนิยามของ `PRODUCTION-SPEC-v1.0.md`
- ห้ามสร้าง Sticker Sheet โดยไม่อ่าน active Production Spec
- ห้ามข้าม Content QC
- ห้ามข้าม Hero Approval
- ห้ามข้าม Thai Text QC หลัง render
- ห้ามใช้ caption / pose ที่ไม่ได้มาจาก Production SSOT
- ห้ามพึ่งพาความรู้จากบุคคลหรือแชตแทน SSOT; ถ้าข้อมูลจำเป็นไม่มีในเอกสาร ต้องแก้เอกสารก่อนเดินงานต่อ

## Production Status Flow
`DRAFT → CONTENT REVIEW → CONTENT LOCK → HERO → HERO APPROVED → FULL PRODUCTION → IMAGE QC → THAI TEXT QC → OWNER REVIEW → FINAL APPROVED → RELEASED`
