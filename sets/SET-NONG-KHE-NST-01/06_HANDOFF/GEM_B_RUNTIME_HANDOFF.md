# GEM B RUNTIME HANDOFF — น้องเข้ นสต. v0.3.0

## Source snapshot
ชุด SET-NONG-KHE-NST-01 revision0.3.0 อ่าน baseline GitHub 2110a1ca520e4365ee48cba6ce383322c633bbbd ก่อนจัดทำแพ็กนี้ ผลส่งมอบจริงจะตรึง commitใน delivery receiptนอกแพ็ก เพื่อหลีกเลี่ยง self-reference ให้ consumerอ่าน canonical revisionและตรวจmanifestก่อนทุกครั้ง

## Inputs
อ่าน README_FIRST, project, frames, references, approvals, Character Bible/Locks และแผนHero/Sheet ไฟล์ REF01 JPEGอยู่ในแพ็กพร้อมhash ให้เปิดภาพตรวจจริงก่อนสร้าง ห้ามยืม Characterจากชุดอื่นหรือเอาภาพcandidateที่ไม่อนุมัติเป็นmaster

## Execution sequence
ขณะนี้เตรียมข้อมูลได้และดำเนิน Character candidateตามคำสั่งเจ้าของได้; ห้าม full batch ขั้นตอน: สร้าง/ปรับ Character→ownerตรวจหัว/ชุด→บันทึกhash/receipt→แก้ DEP-003 compatibility→ตรวจGate A→GEM Bสร้างF18→ownerอนุมัติHero→ผลิตS01–S05→visual40/40+pixels+cutter→ownerrelease

## Return protocol
หากข้อมูลต้นทางผิดให้ส่ง RETURN_TO_GEM_A ระบุ set/revision/file/frame ID สาเหตุ expected/actual และหลักฐาน กรณีภาพผิดGEM Bแก้ภายใต้locks ห้ามแก้source captionsหรืออนุมัติแทนowner การคืนงานต้องลงdecision/defectและเปลี่ยนrevisionที่เกี่ยวข้อง

## Readiness
HANDOFF_DRAFT ไม่ใช่ READY_FOR_GEM_B เพราะ DEP-001/002/003 ยังOPEN Character/Hero/releaseเป็นnull เอกสารสร้างครบเพื่อreviewและเตรียมงาน การส่งให้Bอ่านเอกสารไม่ใช่การปลดล็อกผลิต ห้ามใช้legacyvalidatorแล้วเปลี่ยนcontractลงเพื่อให้ผ่าน
