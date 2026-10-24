# APPROVAL REGISTRY — น้องเข้ นสต. v0.6.0

## Decisions
OWNER-01อนุญาตงานGEM A; OWNER-02กำหนดSSOT/ชุด/หัว; OWNER-03ยืนยันใช้ภาพแนบล่าสุดเป็นนายแบบและเก็บเอกสารGitHub ถ้อยคำตรงตัวอยู่approvals.json การเลือกแผนโดยAIต้องไม่เปลี่ยนเป็นownerreceipt

## Character approval
ยังไม่มี owner approval ของไฟล์ Character Sheet ในชุดนักเรียนที่ตรงต้นฉบับ character=null DEP-001/002ยังเปิด หลังownerอนุมัติให้เก็บexact image, hash, decision_refและscopeก่อนactive ไม่ถือคำสั่งให้นำภาพอ้างอิงมาใช้เป็นอนุมัติภาพcandidateก่อนหน้า

## Hero approval
hero=null ยังไม่มีHeroที่สร้างจากCharacter active ฮีโร่ที่เสนอคือF18 Ownerต้องเห็นและอนุมัติไฟล์จริงหลังGEM Bสร้าง ถ้าภาพเปลี่ยนhashต้องreviewใหม่ ไม่ใช้คำชมรูปอื่นแทน

## Release approval
release=null ยังไม่มีชุดภาพ40ภาพหรือexport/cutterให้เจ้าของตรวจ ไม่ปล่อยขายหรือส่งLINEอัตโนมัติ การอนุมัติเอกสารไม่เท่ากับอนุมัติภาพหรือเผยแพร่

## Owner wardrobe and identity correction
OWNER-04/05/06 supersede earlier proposals: เสื้อเชิ้ตสีขาวแขนยาว ติดกระดุมครบทุกเม็ดรวมเม็ดบนสุดที่คอ ผูกเนกไทสีน้ำเงินเข้ม กางเกงขายาวสี สนว.01 เข็มขัดสีดำ หัวและร่างตามREF01 ไม่หัวโต3D ไม่เสื้อกากีแขนสั้น candidateเดิมREJECTED DEP-002RESOLVED รอcandidate04และownerimageapprovalตามDEP-001 ส่วนเนื้อหาที่กล่าวถึงการเปลี่ยนจากเสื้อขาวหรือรอชุดเดิมเป็นประวัติที่ไม่ใช้กำกับการสร้างรอบนี้

## Active approval and current handoff — supersedes historical pending statements
OWNER-08 อนุมัติCharacter Sheet Candidate04ไฟล์ 02_CHARACTER/assets/CHARACTER_SHEET_APPROVED_04.png SHA256 1aa56774a94923cac4c16c69506dc11a18ce754f58b7a51edc003c743853f5c6 สถานะCHARACTER_SHEET_ACTIVE; Gate Aพร้อมส่งGEM BทำHero F18เท่านั้น Heroยังไม่อนุมัติและfullproductionยังLOCKED consumer GEM B0.6.0รองรับcontract1.3.0โดยตรง ไม่ใช้legacyvalidator1.0.0 engineเก่ายังไม่ซ่อมและต้องตรวจexportภายหลัง
