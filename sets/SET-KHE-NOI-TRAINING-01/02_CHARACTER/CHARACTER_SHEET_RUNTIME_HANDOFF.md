# CHARACTER_SHEET_RUNTIME_HANDOFF — เข้น้อย อยู่ระหว่างฝึก

## Inputs
ใช้approvedPNGCHAR04ในassetsซึ่งcopybytesเดียวกับต้นฉบับ อ่านreferenceindex/hashและsourceownerreceipt ต้องอ่านCharacterBible/Locks/upperbodycaptionpolicyก่อนrenderHero ไม่ต้องสร้างCharacterSheetใหม่

## Instructions
คงidentityเดิม เปลี่ยนเฉพาะสถานการณ์สีหน้าท่ามือตามmatrixใหม่ ให้BทดสอบHeroF01แบบupperbodyไทยใหญ่ การใช้คำฝึกไม่ได้อนุญาตเปลี่ยนชุดหรือเพิ่มpropsทหาร ตรวจheadlikenessก่อนshowowner

## Expected outputs
ขั้นถัดไปคือHeroหนึ่งภาพพร้อมprompt/provenance/hashและภาพpreviewให้ownerตรวจ ถ้าไม่สามารถเปิดPNGsourceให้รายงานmissingasset ไม่สร้างหัวใหม่จากข้อความ ประหยัดโควต้าโดยไม่สร้างturnaroundซ้ำ

## Approval boundary
ตัวละครมีexistingidentityapprovalเท่านั้น ชุดใหม่ยังไม่มีHeroapproval fullproductionรอHero เมื่อเปลี่ยนidentityหรือwardrobeจากที่approvedต้องย้อนownerก่อน ต่อให้ไม่มีเทคนิคfailก็ไม่ถือว่าownerapprove
