# SET-009 PRODUCTION SPEC v1.0

## Scope
เอกสารนี้เป็นข้อกำหนดการผลิต Sticker Sheet สำหรับชุด **สหกรณ์ออมทรัพย์ตำรวจภูธรภาค 6 หมายเลข 1** (`SET-009-PPR6-SAVINGS-COOP-01`) และให้ถือเป็น Production SSOT สำหรับรูปแบบ Sticker Sheet/Frame จนกว่าจะมีเวอร์ชันใหม่ที่อนุมัติแทน

## Terminology
- **Sticker Sheet** = ไฟล์ภาพ PNG 1 ไฟล์ที่รวมสติ๊กเกอร์หลายตัวเรียงเป็นกริด
- **Frame** = แต่ละเซลล์ของกริดใน Sticker Sheet
- **Inter-frame Margin / Gutter** = ช่องว่างโปร่งใสระหว่างขอบนอกของ Frame หนึ่งกับ Frame ถัดไป เพื่อไม่ให้เส้น border ชิดติดกันและช่วยให้โปรแกรม downstream ตัดเฟรมได้ง่าย
- **Internal Padding / Safe Area** = ระยะว่างขั้นต่ำจากด้านในของ Frame Border ถึงขอบนอกสุดของ White Backing / Sticker Artwork

## Sticker Sheet Requirements
- File format: **PNG**
- Background: **transparent / โปร่งใส**
- Layout: grid เช่น **5 columns × 8 rows** หรือจำนวนอื่นตามรอบการผลิต
- ไม่ต้องมีหมายเลขกำกับสติ๊กเกอร์หรือหมายเลขเฟรมบนภาพ

## Frame Geometry — MANDATORY
ข้อกำหนดนี้เป็น **BLOCKING / ห้ามตีความคลุมเครือ**

- ขนาดแต่ละ Frame: **512 × 512 px exact**
- Frame shape: **สี่เหลี่ยมมุมฉาก 90°**
- Frame border: **5 px** สำหรับ production รุ่นปัจจุบัน
- Frame border color: สีที่ Owner กำหนดในรอบผลิต; หากไม่ได้ระบุให้ใช้สีดำสนิท `#000000`
- **Inter-frame Margin / Gutter: 20–30 px**; ค่าแนะนำมาตรฐาน = **24 px**
- **Internal Padding / Safe Area: อย่างน้อย 20–30 px**; ค่าแนะนำมาตรฐาน = **28 px** จากขอบด้านในของ border ถึง White Backing/Artwork
- Sticker Artwork และ White Backing **ห้ามชนหรือแตะ Frame Border**
- Frame Borders **ห้ามชิดติดกัน**; ต้องมี transparent gutter คั่นชัดเจน
- Border ต้องเป็น geometry ที่วาดแบบ deterministic ไม่ใช่เส้นที่ AI วาดแบบอิสระ
- ห้ามใช้ anti-aliased/blurred/painterly border ที่ทำให้โปรแกรม downstream หา frame rectangle ยาก

### Full 40 Deterministic Layout
สำหรับ 5 columns × 8 rows เมื่อใช้:
- frame = 512 px
- gutter = 24 px
- outer sheet margin = 24 px

ขนาด canvas ที่แนะนำคือ:
- Width = `(5 × 512) + (6 × 24)` = **2704 px**
- Height = `(8 × 512) + (9 × 24)` = **4312 px**

ตำแหน่ง Frame ต้องคำนวณแบบ row-major จากค่าคงที่เหล่านี้ และ downstream extractor ต้องสามารถ crop ได้โดยไม่ใช้ OCR/edge detection

## Sticker White Backing / Die-cut Base
ข้อกำหนดนี้เป็น **MANDATORY / ห้ามละเมิด**

สติ๊กเกอร์ทุกตัวต้องมีพื้นสีขาวรองรับตามรูปร่างโดยรวมของสติ๊กเกอร์ เพื่อให้เหมือนสติ๊กเกอร์สำหรับลอกแปะและช่วยให้ไดคัทได้ง่าย

### White Backing Requirements
- สีขาวต้องเป็น **opaque solid white 100% / สีขาวทึบ 100%**
- White backing ต้องเป็นพื้นที่ **ต่อเนื่องเต็มชิ้น**
- ต้องมีขอบสีขาวรอบรูปร่างสติ๊กเกอร์ประมาณ **5 px**
- ห้ามมี transparent hole อยู่ภายใน white backing
- ห้ามมีช่องว่าง รอยแหว่ง รูเข็ม หรือพื้นที่โปร่งใสภายในแม้เพียงเล็กน้อย
- แม้ช่องว่างที่เกิดจากซอกแขน ขา ตัวอักษร อุปกรณ์ประกอบ ช่องระหว่างชิ้นส่วน หรือรูปร่างภายในของภาพ ต้องถูกเติมเป็น **สีขาวทึบ** หากอยู่ภายในขอบเขตของ die-cut base
- ห้ามตีความ white backing เป็นเพียงเส้น stroke/outline สีขาวรอบวัตถุเท่านั้น
- ต้องมองเป็น **solid white backing shape** ที่ตัว artwork วางอยู่ด้านบน

### Practical Interpretation
ให้คิดเหมือนสติ๊กเกอร์เด็กแบบลอกแปะ: ด้านหลังเป็นแผ่นสีขาวทึบตาม silhouette ของสติ๊กเกอร์ ไม่มีรูทะลุหรือพื้นที่โปร่งใสภายใน และมีขอบขาวเผื่อสำหรับการไดคัท

## Thai Caption Accuracy — ZERO ERROR RULE
ข้อกำหนดนี้เป็น **MANDATORY / BLOCKING / ห้ามผิดโดยเด็ดขาด**

ข้อความภาษาไทยบนสติ๊กเกอร์ทุกเฟรมต้องตรงกับข้อความที่อนุมัติใน Production Table แบบ **ตัวอักษรต่อตัวอักษร** และต้องถูกต้องตามอักขรวิธีไทย

### Mandatory Thai Text Requirements
- ห้ามสะกดผิดแม้แต่ 1 ตัวอักษร
- ห้ามสระ วรรณยุกต์ การันต์ หรือเครื่องหมายตกหล่น
- ห้ามมีตัวอักษรเกิน ตัวอักษรซ้ำ หรืออักขระเพี้ยน
- ห้ามสลับตำแหน่งสระ/วรรณยุกต์
- ห้าม AI ดัดแปลงข้อความให้เป็นคำใกล้เคียงเอง
- ห้ามเปลี่ยนคำลงท้าย เช่น `ครับ` เป็นคำอื่นโดยไม่ได้รับอนุมัติ
- ห้ามใช้ข้อความ placeholder หรือข้อความจำลองแทนข้อความจริง
- `สอ.ภ.6` ต้องเขียนตรงตามนี้ทุกครั้งเมื่อมีการใช้ identifier นี้
- ก่อนอนุมัติภาพ ต้องอ่านข้อความจากภาพจริงเทียบกับ SSOT ทีละเฟรม

### Text Production Rule
Caption ในภาพต้องคัดลอกจากข้อความที่ล็อกใน `FULL-STICKER-PRODUCTION-TABLE-v1.0.md` เท่านั้น ห้ามพิมพ์ใหม่จากความจำเมื่อเข้าสู่ขั้นผลิตภาพ

### Thai Text Rejection Criteria
Reject เฟรมทันทีหากพบข้อใดข้อหนึ่ง:
- มีคำไทยสะกดผิดแม้ 1 จุด
- สระ/วรรณยุกต์/การันต์ผิดหรือตกหล่น
- คำไม่ตรงกับ Approved Caption
- ตัวอักษรอ่านไม่ออกหรือถูก artwork บดบังจนตีความผิดได้
- `สอ.ภ.6` ผิดรูปแบบ

## Layering Concept
ลำดับเชิงภาพ:
1. Transparent Sticker Sheet background
2. Transparent outer margin / inter-frame gutters
3. Deterministic Frame border
4. Transparent internal padding / safe area
5. Solid opaque white die-cut backing (ไม่มีรูภายใน)
6. Sticker artwork / character / text / props

พื้นที่นอก white die-cut backing ภายใน Frame ยังคงเป็น transparent ยกเว้น frame border

## QA Acceptance Criteria
Sticker/Frame จะถือว่าผ่านเมื่อ:
- [ ] Frame มีขนาด 512 × 512 px exact
- [ ] Inter-frame Margin/Gutter อยู่ในช่วง 20–30 px
- [ ] Internal Padding/Safe Area อย่างน้อย 20 px และแนะนำ 28 px
- [ ] Frame border 5 px และเป็นมุมฉาก
- [ ] Frame Borders ไม่ชิดติดกัน
- [ ] Sticker/White Backing ไม่ชน Frame Border
- [ ] Sticker Sheet background และ gutters เป็น transparent จริง
- [ ] White backing เป็นสีขาวทึบ 100%
- [ ] White backing ไม่มี transparent hole แม้ขนาดเล็ก
- [ ] ไม่มี pinhole / gap / void / internal cutout ใน white backing
- [ ] มีขอบขาวรอบ artwork ประมาณ 5 px สำหรับ die-cut
- [ ] ไม่มีหมายเลขกำกับบนสติ๊กเกอร์
- [ ] Caption ตรงกับ Approved Caption แบบตัวอักษรต่อตัวอักษร
- [ ] ภาษาไทยสะกดถูกต้อง 100%
- [ ] สระ วรรณยุกต์ การันต์ และเครื่องหมายครบถ้วน
- [ ] ข้อความอ่านได้ชัดเจนเมื่อดูในขนาดใช้งานจริง
- [ ] Downstream crop test ผ่านโดยใช้ geometry เท่านั้น ไม่ต้อง OCR หรือเดาขอบ

## Rejection Criteria
ต้อง Reject และแก้ไขทันทีหากพบข้อใดข้อหนึ่ง:
- White backing มีช่องโปร่งใสภายในแม้เพียงจุดเดียว
- ใช้เฉพาะ white outline แต่ไม่มี solid white base
- สติ๊กเกอร์หรือ white backing ชนขอบ Frame
- Frame borders ชิดติดกันหรือไม่มี gutter ตามกำหนด
- Internal padding ต่ำกว่าค่าขั้นต่ำจนเสี่ยงต่อการไดคัท
- พื้นหลัง Sticker Sheet หรือ gutter ไม่โปร่งใส
- Frame ผิดขนาดอย่างมีนัยสำคัญ
- Border ถูก generate แบบไม่สม่ำเสมอจน downstream ตรวจ/crop ยาก
- มีหมายเลขเฟรม/หมายเลขสติ๊กเกอร์บน artwork โดยไม่ได้รับคำสั่งเฉพาะ
- มีข้อความภาษาไทยผิดแม้เพียง 1 ตัวอักษร
- Caption ไม่ตรงกับ SSOT
- Downstream extraction test ไม่ผ่าน

## Pre-Render / Post-Render Gate
ก่อนสร้าง Sticker Sheet ทุกครั้ง ต้องโหลดและ apply เอกสารนี้เป็นข้อกำหนดบังคับ

หลังสร้างภาพแล้วต้องตรวจอย่างน้อย 3 gate:
1. **Geometry/Production QC** — frame size, grid, border, gutters, internal padding, transparency, white backing
2. **Thai Text QC** — ตรวจ caption จากภาพจริงทุกเฟรมเทียบกับ SSOT แบบ character-by-character
3. **Extraction QC** — ทดสอบ crop ทั้ง 40 Frame จาก geometry จริง และยืนยันว่าแต่ละ output เป็น 512 × 512 px โดยไม่มีเฟรมเหลื่อม

ห้ามส่งภาพให้ Product Owner ตรวจในฐานะงานผ่านมาตรฐาน หาก gate ใด gate หนึ่งยังไม่ผ่าน

## Locked Owner Requirements
1. Owner ยืนยันว่า **พื้นสีขาวรองรับสติ๊กเกอร์ห้ามมีช่องว่างใด ๆ แม้แต่รอยหรือรูขนาดเล็ก ต้องเป็นสีขาวทึบเต็มพื้นที่ภายใน die-cut backing**
2. Owner ยืนยันว่า **ข้อความภาษาไทยห้ามผิดโดยเด็ดขาด แม้เพียง 1 ตัวอักษร**
3. Owner ยืนยันว่า **Frame ต้องมี Margin/Gutter และ Padding ประมาณ 20–30 px เพื่อให้ border ไม่ชิดกันและ sticker ไม่ชิด frame สำหรับงานไดคัท/downstream extraction**

ข้อกำหนดเหล่านี้เป็นข้อกำหนดระดับสูงสุดของ Production และ QA สำหรับ SET-009
