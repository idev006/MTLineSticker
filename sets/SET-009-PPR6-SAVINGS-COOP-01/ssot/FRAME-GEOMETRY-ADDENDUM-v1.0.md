# FRAME GEOMETRY ADDENDUM v1.0 — SET-009

## Status
**ACTIVE / NORMATIVE / BLOCKING**

เอกสารนี้ขยายความ `PRODUCTION-SPEC-v1.0.md` เฉพาะด้าน Frame geometry เพื่อให้ทั้งมนุษย์, AI และโปรแกรม downstream ตีความตรงกัน

## Purpose
Sticker Sheet ของ SET-009 ถูกออกแบบเป็น machine-handoff artifact ไม่ใช่เพียงภาพรวมสำหรับดูสวย โปรแกรม downstream จะนำ Sheet ไปตัดเป็น Frame รายตัว ดังนั้นเส้นแบ่ง Frame, safe spacing และ geometry ต้องอ่านได้ชัดและสม่ำเสมอ

## Locked Frame Geometry
- Frame effective size: **512 × 512 px**
- Frame shape: **square / 90-degree corners**
- Frame border nominal thickness: **ประมาณ 3 px**
- Preferred border color: **dark black / near-black** เพื่อให้แบ่งขอบ Frame ได้ชัด
- Margin nominal: **20 px**
- Padding nominal: **20 px**
- Sticker Artwork และ White Backing **ห้ามแตะหรือชน Frame Border**
- ห้ามมีองค์ประกอบสำคัญล้ำเข้า extraction-safe zone

## Interpretation of Margin and Padding
สำหรับงานนี้ให้ตีความดังนี้:
- **Frame Border** = เส้นขอบที่กำหนดขอบเขตของ Frame 512 × 512 px
- **Padding ~20 px** = safe area ภายใน Frame จากแนว Frame Border เข้าหา artwork; artwork/white backing ต้องอยู่พ้นเขตนี้
- **Margin ~20 px** = ระยะจัดวาง/spacing ที่ช่วยให้ Frame boundaries และการแยก Frame อ่านได้ง่ายใน Sheet assembly; implementation ต้องไม่ทำให้ effective Frame 512 × 512 px เปลี่ยนไป

หากระบบ downstream ใช้ crop rectangle จาก grid metadata เป็นหลัก Border และ Margin ต้องไม่ทำให้ตำแหน่ง crop ของ Frame เปลี่ยนจาก contract ที่กำหนด

## Border Rendering Rule
- ใช้เส้นสีดำเข้มหรือ near-black เป็นค่าเริ่มต้น
- ความหนาเป้าหมายประมาณ 3 px และต้องสม่ำเสมอทุก Frame
- ห้ามใช้ rounded corners
- ห้ามใช้ gradient, glow หรือ decorative border ที่ทำให้ขอบ Frame กำกวม
- Border มีหน้าที่เป็น production guide / visual separator ไม่ใช่ส่วนหนึ่งของ Sticker Artwork

## Downstream Extraction Requirement
Sheet ต้องสามารถส่งต่อให้ extractor แล้ว:
1. ระบุ grid ได้แน่นอน
2. คำนวณ crop rectangle ได้แบบ deterministic
3. ตัดแต่ละ Frame โดยไม่ต้อง OCR
4. ไม่ต้องเดาขอบจาก artwork
5. ไม่ต้องซ่อมภาพก่อน crop
6. ไม่สูญเสีย pixel content ของ sticker ภายใน Frame

## QA Acceptance Criteria
- [ ] ทุก Frame = 512 × 512 px
- [ ] Border ≈ 3 px ทุกช่อง
- [ ] Border เป็นสีดำเข้ม/near-black และมองเห็นชัด
- [ ] มุม Frame เป็น 90°
- [ ] Padding ≈ 20 px ถูกคงไว้รอบ artwork
- [ ] Margin/spacing ไม่ทำลาย deterministic crop contract
- [ ] Artwork และ White Backing ไม่แตะ Border
- [ ] ไม่มี crop-risk element อยู่ใน safe zone
- [ ] 5 × 8 full sheet สามารถแยก 40 Frame ได้ตาม row-major mapping

## Immediate Rejection Criteria
Reject หากพบข้อใดข้อหนึ่ง:
- ไม่มี Frame Border หรือ Border อ่านไม่ชัด
- Border หนา/บางไม่สม่ำเสมอจน boundary กำกวม
- ใช้ขอบมนแทนมุมฉาก
- Sticker หรือ White Backing ชน Border
- safe padding หายไป
- geometry ทำให้ downstream ต้องเดาตำแหน่ง crop
- การเพิ่ม margin ทำให้ effective Frame ไม่ใช่ 512 × 512 px

## Owner Lock
Owner ยืนยันว่า **Frame Border ประมาณ 3 px, สีดำเข้มได้, และแต่ละ Frame ต้องมี Margin/Padding ประมาณ 20 px เพื่อให้การตัดแยก Frame ทำได้ง่ายและแม่นยำ** ข้อนี้เป็น blocking production requirement
