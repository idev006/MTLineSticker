# AUTO_REJECT_RULES — เข้น้อย อยู่ระหว่างฝึก

## Critical failures
ปฏิเสธไฟล์เอกสารขาด/placeholder IDซ้ำ/ขาด captionผิดไฟล์sourcehashไม่ตรงหรืออ้างapprovalไม่จริง ภาพเต็มตัวจนหน้าเล็ก captionเล็ก/บังตาปาก มือหาย หัวคนละตัว เครื่องแต่งกายเปลี่ยน alphaทึบ และdiecutไม่ครบ

## Recovery routing
ระบุset/revision/frame/file expected/actualและรูปหลักฐาน ข้อมูลต้นทางผิดให้Aแก้พร้อมversion/manifest ภาพผิดBแก้ TechnicalFAILหยุดexport ไม่แก้specให้ผ่านเงียบๆ ถ้าขาดassetให้reportmissingไม่เดาจากชุดอื่น

## Reapproval triggers
หัวหรือชุดหลักเปลี่ยนต้องownerCharacterapprovalใหม่ Heroเปลี่ยนหลังอนุมัติต้องreviewHeroใหม่ captionที่ownerล็อกเปลี่ยนต้องdecisionใหม่ การแก้เล็กน้อยยังต้องrecomputehashและทดสอบผลกระทบ
