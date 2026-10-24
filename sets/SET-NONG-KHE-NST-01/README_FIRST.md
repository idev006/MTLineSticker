# README FIRST — น้องเข้ นสต. v0.3.0

## Project identity
SET-NONG-KHE-NST-01 — ชื่อทำงาน “น้องเข้ นสต. — เก๊กได้…ครูฝึกอย่าเห็น!” revision 0.3.0 จัดทำตาม GEM A v0.5.0 จำนวน 40 ภาพ ใช้ REF01 ซึ่งเจ้าของแนบล่าสุดเป็นอัตลักษณ์หัวจระเข้ ร่างกายเป็นคนสวมชุดนักเรียนนายสิบตำรวจระหว่างศึกษา ไม่ถือชื่อชุดและ caption ที่ AI เสนอว่าเจ้าของล็อกแล้ว

## Read order
อ่าน project.json และ DECISION_LOG ก่อน ตามด้วย CHARACTER_BIBLE, GLOBAL_CHARACTER_LOCKS, REFERENCE_INDEX, CAPTION_MASTER, FRAME_COMMUNICATION_MATRIX, FRAME_TO_SHEET_MAPPING แล้วจึงอ่าน HERO_PLAN, SHEET_PLAN และ GEM_B_RUNTIME_HANDOFF ข้อมูลทั้งหมดใน revision นี้ต้องใช้ร่วมกัน PACKAGE_MANIFEST ไม่ hash ตัวเองเพื่อหลีกเลี่ยงวงจร; จำนวน archive entries เท่ากับ payload+manifest ไม่มี directory entries; SHA256SUMS.txt ไม่รวมตัวเองและ PACKAGE_MANIFEST เพื่อไม่เกิด hash วงจร ตัว manifest เป็น inventory หลัก

## Current stage
เอกสารทุกหมวดมีเนื้อหาเฉพาะชุด ตรวจโครงสร้างด้วย validator จริงก่อนรายงานผลใน delivery receipt ภายนอกแพ็ก ไม่ฝัง PASS ล่วงหน้า สถานะการผลิต HANDOFF_DRAFT: DEP-001 ภาพ Character ยังไม่อนุมัติ, DEP-002 รายละเอียดชุดยังไม่มี reference, DEP-003 legacy integration mismatch ภาพตัวอย่างก่อนหน้านี้ไม่เป็น authority แทน REF01

## Next action
ผู้สร้าง Character อ่านเอกสาร 02_CHARACTER พร้อมไฟล์ REF01 สร้าง/ปรับ candidate ให้ตรงหัวต้นฉบับและชุดนักเรียน แล้วนำภาพจริงให้เจ้าของพิจารณา บันทึก hash และ receipt ก่อนเปิด Gate A GEM B ยังเตรียมงานได้แต่ไม่ผลิต batch ในระหว่างรอ
