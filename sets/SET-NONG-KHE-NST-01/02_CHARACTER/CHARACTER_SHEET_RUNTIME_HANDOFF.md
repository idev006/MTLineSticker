# CHARACTER_SHEET_RUNTIME_HANDOFF — น้องเข้ นสต. v0.5.0

## Inputs
ใช้REF01 JPEGใน07_REFERENCES/assets พร้อมhashในreferences.json และCharacter Bible/Locks/Specification/prompt revision0.5.0 ห้ามใช้candidate01/02ที่ถูกปฏิเสธแทนreference

## Instructions
อ่านOWNER-04/05/06ก่อน เอกสารนี้คือบรีฟที่ปรับตามคำแก้ล่าสุด Ownerอนุญาตสร้างหลังแก้SSOTแล้ว เปิดREF01ใช้หัวและสัดส่วนตรงภาพบน สร้างชุดขาวแขนยาวไทน้ำเงินเข้มตามคำยืนยัน ไม่ขอภาพชุดใหม่หรือเดายศเพิ่ม

## Expected outputs
Character candidate04หนึ่งแผ่น ภาพหลักกางแขนและมุมหน้า/สามส่วน/ข้าง/หลังในชุดเดียวกัน ไม่มีแถวอารมณ์ใหม่ เก็บprompt/tool/hashของผลจริงในreceiptภายนอกแพ็ก แล้วให้เจ้าของตรวจความเหมือน ไม่อ้างapprovedก่อนคำยืนยัน

## Approval boundary
DEP-002รายละเอียดชุดRESOLVEDจากOWNER-05; DEP-001ภาพCharacterยังOPEN; DEP-003integrationยังOPEN คงHANDOFF_DRAFTจนผ่านเกณฑ์จริง ภาพที่ไม่ตรงให้คืนแก้identityไม่ปรับBibleตามภาพผิด
