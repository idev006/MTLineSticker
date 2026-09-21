# STICKER SHEET COOKBOOK v1.0 — SET-009

## Purpose
เอกสารนี้เป็น **execution cookbook** สำหรับมนุษย์หรือ AI ที่ต้องสร้าง Sticker Sheet ของชุด `SET-009-PPR6-SAVINGS-COOP-01` ให้ได้มาตรฐานเดียวกันทุกครั้ง และให้ผลลัพธ์สามารถส่งต่อเข้าสู่โปรแกรม downstream เพื่อแยกแต่ละ Frame ออกเป็นสติ๊กเกอร์รายตัวได้อย่าง deterministic

เป้าหมายคือ: **ผู้ปฏิบัติงานคนใหม่หรือ AI ที่ไม่เคยเห็นประวัติแชตมาก่อน เมื่ออ่านเอกสารนี้และ normative references ที่ระบุ ต้องสามารถสร้าง Sticker Sheet ที่ถูกต้องตามมาตรฐานได้โดยไม่ต้องเดา**

---

## Normative References
ต้องอ่านก่อนเริ่มงาน:
1. `PRODUCTION-SPEC-v1.0.md` — สเปกเชิงเทคนิคของ Sticker Sheet / Frame / White Backing
2. `FULL-STICKER-PRODUCTION-TABLE-v1.0.md` — Caption, Intent, Pose, Expression, Prop, Outfit และ QA ของแต่ละ Frame
3. `CHARACTER-BIBLE-v1.0.md` — ข้อกำหนดตัวละคร
4. `CONTENT-QC-PROTOCOL-v1.0.md` — กฎตรวจความซ้ำด้าน caption / intent / pose
5. `END-TO-END-PRODUCTION-PIPELINE-v1.0.md` — workflow และ gates

หากเอกสารขัดกันในประเด็น Sticker Sheet geometry, Frame geometry, transparency, white backing, margin, padding หรือ border ให้ยึด `PRODUCTION-SPEC-v1.0.md`

---

## Canonical Definitions
- **Sticker Sheet** = PNG หนึ่งไฟล์ที่รวมสติ๊กเกอร์หลายตัวเป็น grid
- **Frame** = เซลล์แต่ละช่องใน grid
- **Sticker Artwork** = ตัวละคร + caption + prop + visual effects ที่อยู่ภายใน Frame
- **White Backing / Die-cut Base** = พื้นสีขาวทึบ 100% ที่รอง Sticker Artwork ตาม silhouette เพื่อให้ไดคัทได้ง่าย
- **Frame Border** = เส้นกรอบมุมฉากที่ใช้แบ่งแต่ละ Frame
- **Margin / Padding** = ระยะปลอดภัยตาม Production Spec
- **Downstream Extractor** = โปรแกรมปลายทางที่อ่าน Sticker Sheet และตัดแต่ละ Frame ออกเป็นไฟล์สติ๊กเกอร์รายตัว

---

## World-Class Output Principle
Sticker Sheet ที่ผ่านมาตรฐานต้องมีคุณสมบัติพร้อมกันทั้ง 4 ด้าน:
1. **Visual Quality** — คาแรคเตอร์คงที่ สีหน้า/ท่าทางสื่อความหมายชัด
2. **Language Accuracy** — ภาษาไทยถูกต้อง 100%; ผิด 1 ตัวอักษร = Reject
3. **Production Geometry** — grid, Frame, margin, padding, border และ transparency ถูกต้อง
4. **Machine Handoff Reliability** — โปรแกรม downstream สามารถ crop Frame ตาม grid ได้โดยไม่ต้องเดาตำแหน่งหรือซ่อมไฟล์

---

## Recipe A — Decide Sheet Grid
เลือกจำนวนคอลัมน์และแถวตามจำนวนสติ๊กเกอร์ในรอบนั้น

ตัวอย่าง:
- Hero 6 = grid ที่กำหนดเฉพาะรอบนั้น แต่ทุก Frame ยังต้อง 512 × 512 px
- Full 40 = 5 columns × 8 rows

สูตรพื้นที่ Frame-only:
- Width = columns × 512
- Height = rows × 512

หาก Production Spec กำหนด outer margin รอบ sheet ให้รวมค่าดังกล่าวตามเอกสาร active version

**ห้าม resize แต่ละ Frame ให้เล็กลงเพื่อให้พอดีกับ canvas**

---

## Recipe B — Build Deterministic Grid
1. สร้าง canvas แบบ RGBA
2. background ต้อง transparent
3. วาง grid ตามจำนวน columns × rows
4. แต่ละ Frame ต้องมี effective cell size = 512 × 512 px
5. วาด Frame Border ≈ 3 px เป็นสี่เหลี่ยมมุมฉาก
6. ใช้ row-major ordering: ซ้ายไปขวา, บนลงล่าง
7. ห้ามมีเลขลำดับพิมพ์อยู่ใน artwork

### Downstream Ordering Contract
Frame index สำหรับโปรแกรมปลายทางให้อิงตำแหน่งเชิงตรรกะ:
- Frame 1 = row 1, column 1
- เดินซ้าย → ขวา
- เมื่อจบแถวให้ขึ้นแถวถัดไป

โปรแกรม downstream ต้องไม่ต้องใช้ OCR หรือ content detection เพื่อหาขอบ Frame

---

## Recipe C — Compose Each Frame
สำหรับแต่ละ Frame:
1. อ่านข้อมูลจาก `FULL-STICKER-PRODUCTION-TABLE-v1.0.md`
2. ใช้ Caption แบบ exact string เท่านั้น
3. สร้าง Character ตาม Visual SSOT / Character Bible
4. ใช้ Pose / Expression / Prop ตาม Production Table
5. จัดองค์ประกอบให้อยู่ภายใน safe area
6. ห้าม artwork หรือ white backing แตะ Frame Border
7. ห้ามเปลี่ยน Caption หรือ Intent เอง

---

## Recipe D — Thai Caption Zero-Error
ก่อน render:
- copy Caption จาก SSOT แบบตัวอักษรต่อตัวอักษร
- ห้าม paraphrase
- ห้ามแก้คำโดย AI
- ห้ามสร้างตัวสะกดใหม่เอง

หลัง render:
- อ่านข้อความจากภาพจริง
- เทียบกับ SSOT อีกครั้ง
- ตรวจพยัญชนะ สระ วรรณยุกต์ การันต์ เว้นวรรค เครื่องหมาย และ `สอ.ภ.6`

**Mismatch ใด ๆ = Reject ทั้ง Frame**

---

## Recipe E — White Backing / Die-cut Base
White Backing เป็น mandatory production layer

ขั้นตอน:
1. สร้าง silhouette รวมของ character + caption + prop ที่ควรรวมเป็นสติ๊กเกอร์เดียว
2. ขยาย silhouette ออกโดยประมาณ 5 px เพื่อสร้าง die-cut allowance
3. fill พื้นที่นี้ด้วย opaque white 100%
4. ต้องเป็น solid shape เดียวหรือ solid connected base ตามที่ artwork ต้องการ
5. เติมช่องว่างภายในทั้งหมดให้เป็นสีขาวทึบ
6. ห้ามมี transparent hole / pinhole / void / internal cutout
7. วาง artwork บน white backing

### Reject Immediately If
- มีรูโปร่งใสแม้ 1 จุดภายใน backing
- มีเพียง white outline แต่กลางยังโปร่งใส
- มีซอกระหว่างแขน ขา ตัวอักษร หรือ prop ที่ทะลุเป็น transparent ใน die-cut base

---

## Recipe F — Frame Safety
ทุก Frame ต้องตรวจ:
- 512 × 512 px
- border ≈ 3 px
- margin = 20 px
- padding = 20 px
- sticker ไม่ชน border
- ไม่มีองค์ประกอบถูก crop
- ไม่มีหมายเลขกำกับ

หาก Frame ใดละเมิด ให้ Reject เฉพาะ Frame และสร้างใหม่ ไม่ควรบิด scale ทั้ง sheet เพื่อชดเชย

---

## Recipe G — Export Contract
ไฟล์ Sticker Sheet final:
- Format: PNG
- Color mode: RGBA
- Background: transparent จริง
- Lossless
- ห้าม flatten ด้วยพื้นสีขาวทั้ง sheet
- ห้าม JPEG
- ห้ามเพิ่ม shadow หรือ canvas decoration ที่อยู่นอกแต่ละ Frame โดยไม่ได้กำหนด

ชื่อไฟล์ควร deterministic เช่น:
- `SET-009-HERO-SHEET-v1.0.png`
- `SET-009-FULL-SHEET-01-v1.0.png`

---

## Machine Handoff Contract
Sticker Sheet ถูกออกแบบให้โปรแกรม downstream ทำงานต่อดังนี้:
1. อ่าน image dimensions
2. อ่านค่า grid columns / rows จาก job config หรือ manifest
3. คำนวณ Frame rectangles แบบ deterministic
4. crop แต่ละ Frame ตาม rectangle
5. เก็บ alpha channel
6. ไม่ต้อง infer sticker contour เพื่อหา Frame
7. การแยก Frame ต้องไม่เปลี่ยน pixel content ภายใน Frame

### Recommended Downstream Metadata
ควรส่งคู่กับ PNG:
```yaml
set_id: SET-009-PPR6-SAVINGS-COOP-01
sheet_type: hero | full | revision
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
production_spec: PRODUCTION-SPEC-v1.0.md
```

หมายเหตุ: metadata เป็น machine-handoff recommendation; หากระบบ downstream มี schema ของตัวเอง ให้ map ค่าเหล่านี้โดยคง semantic เดิม

---

## Automated Validation Targets
ก่อนส่งให้ downstream โปรแกรมหรือ AI ควรตรวจอัตโนมัติเท่าที่ทำได้:
- PNG signature ถูกต้อง
- มี alpha channel
- dimensions สอดคล้องกับ grid × 512
- crop rectangles หารลงตัวตาม Frame geometry
- alpha นอก artwork เป็น transparent ตาม spec
- ไม่มี artwork แตะพื้นที่ต้องห้ามบริเวณ Frame Border

การตรวจภาษาไทยและ character fidelity ยังต้องมี visual/QC gate เพิ่มเติมแม้ automation ผ่าน

---

## Human / AI Execution Checklist
ผู้ปฏิบัติงานต้องตอบ YES ได้ครบก่อน release:
- [ ] อ่าน active Production Spec แล้ว
- [ ] ใช้ Character SSOT ถูกเวอร์ชัน
- [ ] ใช้ Production Table ถูกเวอร์ชัน
- [ ] Caption exact match ทุก Frame
- [ ] Grid ถูกต้อง
- [ ] Frame 512 × 512 px ทุกช่อง
- [ ] Margin/Padding 20 px
- [ ] Border ≈ 3 px และมุมฉาก
- [ ] Background transparent
- [ ] White backing ทึบ 100%
- [ ] White backing ไม่มี internal hole
- [ ] ไม่มี sticker ชน Frame
- [ ] ไม่มีหมายเลขกำกับ
- [ ] Export เป็น PNG lossless
- [ ] Downstream crop ได้แบบ deterministic
- [ ] Visual QC PASS
- [ ] Thai Text QC PASS

---

## AI Execution Rule
AI ที่ได้รับมอบหมายให้สร้าง Sticker Sheet ต้อง:
1. อ่าน normative references ก่อน
2. สรุป internal constraints ให้ตนเองก่อน generate
3. ห้าม invent ค่า geometry
4. ห้าม invent / rewrite Caption
5. ห้าม skip White Backing
6. ห้ามส่งงานต่อหากมี uncertainty ใน blocking requirement
7. หากระบบสร้างภาพไม่สามารถรับประกันภาษาไทยถูกต้อง ต้องใช้ขั้นตอน post-render text correction / compositing ที่ควบคุมข้อความได้ก่อน release

---

## Definition of Done
Sticker Sheet ถือว่า **DONE** เมื่อ:
- มนุษย์ดูแล้วได้คุณภาพ visual ตามมาตรฐานชุด
- ภาษาไทยถูกต้อง 100%
- ผ่าน Production Spec ทุกข้อ
- ผ่าน Content/Visual/Text QC ที่เกี่ยวข้อง
- downstream extractor สามารถแยก Frame ได้โดยใช้ geometry ที่กำหนดโดยไม่ต้องเดา
- ไม่มี manual repair ที่จำเป็นก่อนขั้นตอน downstream

หากข้อใดข้อหนึ่งไม่ผ่าน ให้ถือว่ายังไม่ใช่ Final Artifact
