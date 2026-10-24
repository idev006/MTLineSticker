# CHARACTER SHEET RUNTIME HANDOFF — น้องเข้ นสต. v0.3.0

## Inputs
ไฟล์จำเป็น: CHARACTER_BIBLE.md, GLOBAL_CHARACTER_LOCKS.md, CHARACTER_SHEET_SPECIFICATION.md, NEGATIVE_CONSTRAINTS.md, APPROVAL_CHECKLIST.md และ REF01 JPEG พร้อม SHA256 ใน references.json ทุกไฟล์รวมอยู่ในแพ็กนี้ ห้ามใช้ต้นแบบจากอีกชุดหรือจากชื่อไฟล์โดยไม่อ่านภาพ

## Instructions
อ่าน owner decisions ก่อน เปิด REF01 ตรวจภาพบนเพื่อรักษาหัว จากนั้นใช้ GENERATION_PROMPT สร้าง candidate ตามข้อกำหนด หากมี candidate ก่อนหน้าจะใช้เทียบประวัติได้แต่ไม่แทนต้นฉบับ อย่าเปิด Hero/batch ในขั้นนี้ ประเด็นเครื่องหมาย DEP-002 แสดงเป็นสิ่งรอ review แทนการเดา

## Expected outputs
Character candidate หนึ่งแผ่นครบสี่มุมและสี่อารมณ์ บันทึก prompt/reference/model/tool และ hash ของภาพจริง พร้อมสรุปจุดใกล้และต่างจาก REF01 ถ้าหัวเพี้ยนให้แก้ candidate ก่อนส่งเจ้าของ ไม่บันทึกว่า PASS เพราะเพียงสร้างภาพสำเร็จ

## Approval boundary
ผู้สร้างภาพไม่อนุมัติเอง Owner ต้องเห็นภาพจริงและให้คำสั่งชัดเจน ระหว่างนี้ใช้ HANDOFF_DRAFT หากการอนุมัติมีข้อยกเว้นเช่นยอมรับหัวแต่ยังแก้ชุด ให้แยกบันทึก scope ไม่ปลด Gate A ทั้งภาพ
