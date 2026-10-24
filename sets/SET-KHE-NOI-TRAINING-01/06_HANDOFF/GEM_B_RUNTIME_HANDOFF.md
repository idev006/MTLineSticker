# GEM_B_RUNTIME_HANDOFF — เข้น้อย อยู่ระหว่างฝึก

## Source snapshot
ชุดใหม่ SET-KHE-NOI-TRAINING-01 rev0.1.0 baseline f4995f5942408d2b2407adbaaa39222c7d38a0e6; sourceCharacterมาจากSET-NONG-KHE-NST-01แต่production/captionsอยู่setใหม่นี้ deliverycommitจะระบุในreceiptภายนอกแพ็ก ห้ามใช้mappingชุดก่อน

## Inputs
อ่านREADME_FIRST project/handoff/manifest approvals/reference และทั้งCharacter/Frames/Production เปิดCHAR04 PNGในassetsตรวจhashactualแล้วใช้คนเดิม captionmaster/matrix/mappingใหม่40รายการไม่ใช่เอกสารชื่อเดียวกันของsetก่อน

## Execution sequence
preflightcurrentcontract1.3.0และowneridentityscope→สร้างHeroF01อยู่ระหว่างฝึกแบบครึ่งบนcaptionไทยใหญ่→showowner→บันทึกHeroapproval→ผลิต5ชีทละ8→visual40/40→pixels/alpha/diecut→cutter→ownerrelease ห้ามข้ามHeroapprovalและห้ามเรียกภาพเดี่ยว40ครั้งโดยไม่จำเป็น

## Return protocol
RETURN_TO_GEM_Aพร้อมset/revision/frameID defectexpected/actualและevidenceหากข้อมูลไม่ตรง Bไม่มีสิทธิ์แก้caption/authorityเอง หากหาPNGไม่ได้ให้materializeจากGitHubหรือรายงานmissinginput ไม่สร้างหัวใหม่แทน

## Readiness
พร้อมเตรียมและทำHeroหลังBตรวจpreflightตามcontract1.3.0 ใช้existingunchangedCharacterapproval ไม่ใช่fullproductionunlock Hero/release=null รูปภาพในชุดนี้ยังไม่สร้างและpixelQAยังNOT_RUN enginelegacyvalidation1.0.0ไม่ใช่ตัวรับcontractใหม่ อย่าdowngradeเพื่อให้ผ่าน
