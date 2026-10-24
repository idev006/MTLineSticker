# GEM B RUNTIME HANDOFF — น้องเข้ นสต. v0.6.0

## Source snapshot
ชุด SET-NONG-KHE-NST-01 revision0.6.0 อ่าน baseline GitHub 2110a1ca520e4365ee48cba6ce383322c633bbbd ก่อนจัดทำแพ็กนี้ ผลส่งมอบจริงจะตรึง commitใน delivery receiptนอกแพ็ก เพื่อหลีกเลี่ยง self-reference ให้ consumerอ่าน canonical revisionและตรวจmanifestก่อนทุกครั้ง

## Inputs
อ่าน README_FIRST, project, frames, references, approvals, Character Bible/Locks และแผนHero/Sheet ไฟล์ REF01 JPEGอยู่ในแพ็กพร้อมhash ให้เปิดภาพตรวจจริงก่อนสร้าง ห้ามยืม Characterจากชุดอื่นหรือเอาภาพcandidateที่ไม่อนุมัติเป็นmaster

## Execution sequence
ขณะนี้เตรียมข้อมูลได้และดำเนิน Character candidateตามคำสั่งเจ้าของได้; ห้าม full batch ขั้นตอน: สร้าง/ปรับ Character→ownerตรวจหัว/ชุด→บันทึกhash/receipt→แก้ DEP-003 compatibility→ตรวจGate A→GEM Bสร้างF18→ownerอนุมัติHero→ผลิตS01–S05→visual40/40+pixels+cutter→ownerrelease

## Return protocol
หากข้อมูลต้นทางผิดให้ส่ง RETURN_TO_GEM_A ระบุ set/revision/file/frame ID สาเหตุ expected/actual และหลักฐาน กรณีภาพผิดGEM Bแก้ภายใต้locks ห้ามแก้source captionsหรืออนุมัติแทนowner การคืนงานต้องลงdecision/defectและเปลี่ยนrevisionที่เกี่ยวข้อง

## Readiness
HANDOFF_DRAFT ไม่ใช่ READY_FOR_GEM_B เพราะ DEP-001/002/003 ยังOPEN Character/Hero/releaseเป็นnull เอกสารสร้างครบเพื่อreviewและเตรียมงาน การส่งให้Bอ่านเอกสารไม่ใช่การปลดล็อกผลิต ห้ามใช้legacyvalidatorแล้วเปลี่ยนcontractลงเพื่อให้ผ่าน

## Owner wardrobe and identity correction
OWNER-04/05/06 supersede earlier proposals: เสื้อเชิ้ตสีขาวแขนยาว ติดกระดุมครบทุกเม็ดรวมเม็ดบนสุดที่คอ ผูกเนกไทสีน้ำเงินเข้ม กางเกงขายาวสี สนว.01 เข็มขัดสีดำ หัวและร่างตามREF01 ไม่หัวโต3D ไม่เสื้อกากีแขนสั้น candidateเดิมREJECTED DEP-002RESOLVED รอcandidate04และownerimageapprovalตามDEP-001 ส่วนเนื้อหาที่กล่าวถึงการเปลี่ยนจากเสื้อขาวหรือรอชุดเดิมเป็นประวัติที่ไม่ใช้กำกับการสร้างรอบนี้

## Active approval and current handoff — supersedes historical pending statements
OWNER-08 อนุมัติCharacter Sheet Candidate04ไฟล์ 02_CHARACTER/assets/CHARACTER_SHEET_APPROVED_04.png SHA256 1aa56774a94923cac4c16c69506dc11a18ce754f58b7a51edc003c743853f5c6 สถานะCHARACTER_SHEET_ACTIVE; Gate Aพร้อมส่งGEM BทำHero F18เท่านั้น Heroยังไม่อนุมัติและfullproductionยังLOCKED consumer GEM B0.6.0รองรับcontract1.3.0โดยตรง ไม่ใช้legacyvalidator1.0.0 engineเก่ายังไม่ซ่อมและต้องตรวจexportภายหลัง

## Current executable next step
Readproject/handoff/manifest/approvals and materialize CHAR04 fromGitHub. Verify SHA256 above. UseCharacterBible/Locks andframes.json F18 “เก๊กก่อน”. ProduceoneHero only, preservingapproved head/body/white longsleeves fully closedcollar/navytie/SNW.01trousers/blackbelt. Showowner inchat thenstopforHeroapproval. Donotproduce40framesyet. Refuseunavailableimagebytes ratherthanreconstructingfromtext.
