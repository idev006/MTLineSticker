# SET-009 PRODUCTION SPEC v1.0

## Scope
เอกสารนี้เป็นข้อกำหนดการผลิต Sticker Sheet สำหรับชุด **สหกรณ์ออมทรัพย์ตำรวจภูธรภาค 6 หมายเลข 1** (`SET-009-PPR6-SAVINGS-COOP-01`) และให้ถือเป็น Production SSOT สำหรับรูปแบบ Sticker Sheet/Frame จนกว่าจะมีเวอร์ชันใหม่ที่อนุมัติแทน

## Terminology
- **Sticker Sheet** = ไฟล์ภาพ PNG 1 ไฟล์ที่รวมสติ๊กเกอร์หลายตัวเรียงเป็นกริด
- **Frame** = แต่ละเซลล์ของกริดใน Sticker Sheet

## Sticker Sheet Requirements
- File format: **PNG**
- Background: **transparent / โปร่งใส**
- Layout: grid เช่น **5 columns × 8 rows** หรือจำนวนอื่นตามรอบการผลิต
- ไม่ต้องมีหมายเลขกำกับสติ๊กเกอร์หรือหมายเลขเฟรมบนภาพ

## Frame Requirements
- ขนาดแต่ละ Frame: **512 × 512 px**
- Frame shape: **สี่เหลี่ยมมุมฉาก**
- Frame border: ประมาณ **3 px**
- Margin: **20 px**
- Padding: **20 px**
- สติ๊กเกอร์ต้องไม่ชนหรือแตะขอบ Frame

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

## Layering Concept
ลำดับเชิงภาพ:
1. Transparent Sticker Sheet background
2. Frame border
3. Solid opaque white die-cut backing (ไม่มีรูภายใน)
4. Sticker artwork / character / text / props

พื้นที่นอก white die-cut backing ภายใน Frame ยังคงเป็น transparent ยกเว้น frame border

## QA Acceptance Criteria
Sticker/Frame จะถือว่าผ่านเมื่อ:
- [ ] Frame มีขนาด 512 × 512 px
- [ ] Margin/Padding เป็น 20 px ตามสเปก
- [ ] Frame border ประมาณ 3 px และเป็นมุมฉาก
- [ ] Sticker ไม่ชน Frame border
- [ ] Sticker Sheet background เป็น transparent จริง
- [ ] White backing เป็นสีขาวทึบ 100%
- [ ] White backing ไม่มี transparent hole แม้ขนาดเล็ก
- [ ] ไม่มี pinhole / gap / void / internal cutout ใน white backing
- [ ] มีขอบขาวรอบ artwork ประมาณ 5 px สำหรับ die-cut
- [ ] ไม่มีหมายเลขกำกับบนสติ๊กเกอร์

## Rejection Criteria
ต้อง Reject และแก้ไขทันทีหากพบข้อใดข้อหนึ่ง:
- White backing มีช่องโปร่งใสภายในแม้เพียงจุดเดียว
- ใช้เฉพาะ white outline แต่ไม่มี solid white base
- สติ๊กเกอร์หรือ white backing ชนขอบ Frame
- พื้นหลัง Sticker Sheet ไม่โปร่งใส
- Frame ผิดขนาดอย่างมีนัยสำคัญ
- มีหมายเลขเฟรม/หมายเลขสติ๊กเกอร์บน artwork โดยไม่ได้รับคำสั่งเฉพาะ

## Locked Owner Requirement
Owner ยืนยันว่า **พื้นสีขาวรองรับสติ๊กเกอร์ห้ามมีช่องว่างใด ๆ แม้แต่รอยหรือรูขนาดเล็ก ต้องเป็นสีขาวทึบเต็มพื้นที่ภายใน die-cut backing** ข้อนี้ให้ถือเป็นข้อกำหนดระดับสูงของการผลิตและ QA
