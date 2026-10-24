# AUTO REJECT RULES — น้องเข้ นสต. v0.6.0

## Critical failures
ปฏิเสธแพ็กเมื่อไม่มีเอกสารบังคับหรือมีเนื้อหาเปล่า; frame IDขาด/ซ้ำ/จับคู่ผิด; captionเคลื่อน; hashไม่ตรง; อ้าง approvalโดยไม่มีหลักฐาน; ภาพไม่มีREF01; หัวสั้นเปลี่ยนidentity; ร่างสัตว์มีหาง; ยศ/ตราสมมติ; productionมีพื้นทึบ crop หรือไดคัทไม่ครบ

## Recovery routing
รายงาน defectพร้อม frame/file/path, expected/actual, source revision และ ownerของงาน แก้ที่ต้นทางเล็กที่สุด ตรวจผลกระทบที่เกี่ยวข้อง จากนั้นออกrevisionและhashใหม่ หากยังไม่มีข้อมูลให้บันทึก DEPแทนเดา GEM B ไม่เปลี่ยน captionหรือหลักหัวเอง

## Reapproval triggers
เปลี่ยนหัว กะโหลก ชุดหลัก สัดส่วน หรือ rendering style หลัง Character approval ต้องขออนุมัติภาพใหม่; เปลี่ยน Heroหลังapprovalต้องอนุมัติHeroใหม่; เปลี่ยนcaptionที่ownerล็อกต้องบันทึกคำสั่งใหม่; การแก้metaเล็กน้อยยังต้องทำmanifestและcross-check
