# SET-006 — พ่อบ้านสายงานบ้าน

**Product code:** SET-006-HOUSEHUSBAND-HOUSEWORK  
**Series:** พ่อบ้านสายวินัย Character IP  
**Product type:** LINE Static Sticker — Full Set 40 images  
**Status:** HERO CORRECTIVE PRODUCTION / H01 GOLDEN REFERENCE APPROVED  
**Framework:** Character Product Development Framework (CPDF) v1.1

## Product intent
ชุดนี้เป็นภาคต่อเฉพาะทางจาก “พ่อบ้านสายวินัย” โดยโฟกัสงานบ้านจริงในชีวิตประจำวัน ให้ผู้ใช้สามารถส่งแทนความหมายว่า “รับผิดชอบอยู่ / กำลังทำ / ทำเสร็จแล้ว / เดี๋ยวจัดการให้” ด้วยน้ำเสียงสุภาพ อบอุ่น และตลกแบบมีศักดิ์ศรี

## Product rule
สติ๊กเกอร์ทุกภาพคือ **communication asset** ไม่ใช่ภาพวาดประกอบเฉย ๆ ต้องมี caption + sender intent + chat use case + expression/action + minimal useful prop ก่อน generation และต้องผ่าน 1-second communication test ที่ขนาดแชต

## Approved inherited character identity
ชุดนี้ **ไม่สร้างตัวละครใหม่** แต่สืบทอด Character SSOT ของ “พ่อบ้านสายวินัย” และใช้ Character Sheet รองเท้าส้มเป็น mandatory visual reference:
- ชายวัยผู้ใหญ่ 30–40 ปี
- clean-shaven ไม่มีหนวดและเครา
- ผมสั้นเกรียนแบบตำรวจ/ทหาร ขอบหน้าผมคมและสะอาด
- เสื้อยืดกรมท่า
- กางเกงขาสั้นสีดำ
- รองเท้าสีส้มสด
- กระเป๋าสะพายข้างสีดำเมื่อไม่รบกวน action
- นาฬิกาสายลุยสีดำที่ข้อมือซ้าย
- แว่นตาดำ optional; facial readability สำคัญกว่า
- บุคลิก: มีวินัย พึ่งพาได้ รักครอบครัว ยอมช่วยเพราะรัก ไม่ใช่เพราะกลัว

## Golden Reference
**H01 / #01 “ล้างจานอยู่ครับ” = Owner Approved / Golden Reference**

H01 ใช้เป็น rendering/communication anchor สำหรับ H02–H06 แต่ Character Sheet ยังคงเป็น SSOT รูปลักษณ์หลัก

## Document map
1. `docs/01-project-brief.md`
2. `docs/02-goals-objectives-kpi.md`
3. `docs/03-market-positioning.md`
4. `docs/04-character-application-notes.md`
5. `docs/05-visual-style-application.md`
6. `docs/06-production-sheet-40.md`
7. `docs/07-hero-set-plan.md`
8. `docs/08-qa-checklist.md`
9. `docs/09-launch-plan.md`
10. `docs/10-post-launch-review.md`
11. `ssot/SET-006-PRODUCT-SSOT-v1.0.md`
12. `ssot/SET-006-PRODUCTION-SPEC-v1.2.md` **ACTIVE**
13. `reviews/HERO-FIT-GATE.md`
14. `reviews/DOCUMENTATION-READINESS-REVIEW.md`

## Production gate
**ห้ามผลิตครบ 40 ภาพก่อน Hero Fit Gate PASS**

Current sequence:
H01 PASS → H02 standalone → QA → H03 → QA → H04 → QA → H05 → QA → H06 → QA → deterministic Hero review sheet → Hero Fit Gate → full production.

Combined AI-generated Hero sheets are concept/review evidence only and are not final production masters.

## Repository integration
This set is the second product in the Househusband series but uses repository-global set ID **SET-006** to avoid collision with existing set IDs.
