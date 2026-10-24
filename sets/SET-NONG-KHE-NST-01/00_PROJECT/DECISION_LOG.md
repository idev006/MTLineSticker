# DECISION_LOG — น้องเข้ นสต. v0.5.0

## Owner decisions
OWNER-01/02/03ให้ทำชุดเดิมและใช้GitHub; OWNER-04ปฏิเสธcandidateเดิมเพราะไม่ตรงต้นฉบับ; OWNER-05ยืนยันเสื้อขาวแขนยาวติดกระดุมถึงคอและไทน้ำเงินเข้ม; OWNER-06สั่งแก้SSOTแล้วสร้างภาพใหม่ หลักฐานตรงตัวอยู่approvals.json

## Assumptions
ชื่อชุดและcaption40ข้อยังเป็นข้อเสนอPROPOSED รองเท้าดำสำหรับส่วนที่ภาพไม่แสดงเป็นข้อเสนอเท่านั้น มุมหลัง/ข้างที่ภาพไม่แสดงต้องอนุมานแบบรักษาidentity ไม่อ้างว่าเป็นต้นฉบับที่มีภาพครบ

## Open dependencies
- DEP-001 [OPEN] ยังไม่มี Character Sheet ที่เจ้าของอนุมัติ ผูกกับ hash จึงไม่ปลด Gate A ผู้รับผิดชอบ Product Owner ร่วมกับผู้สร้าง Character candidate ขั้นต่อไป ใช้เอกสาร 02_CHARACTER สร้าง/แก้ candidate โดยอิง REF01 แล้วให้เจ้าของตรวจภาพและบันทึกการอนุมัติ
- DEP-002 [RESOLVED] เสื้อขาวแขนยาวติดกระดุมถึงคอ เนกไทน้ำเงินเข้ม เจ้าของยืนยันแล้ว ไม่ต้องเดาเสื้อกากีแขนสั้น ผู้รับผิดชอบ Product Owner และ GEM A ขั้นต่อไป ใช้ OWNER-05 เป็น authority ไม่เพิ่มตราหรืออินทรธนูที่ไม่ได้สั่ง
- DEP-003 [OPEN] validator ส่วนกลางรุ่นเดิมรับ contract 1.0.0 ไม่ตรง envelope 1.3.0 จึงห้ามส่งเข้าระบบนั้นโดยอ้างผ่าน ผู้รับผิดชอบ ผู้ดูแล integration A/B ขั้นต่อไป ตรวจ adapter/schema ที่รองรับ 1.3.0 ก่อน machine ingestion; ช่วงนี้รับเอกสารเชิงมนุษย์และเตรียม Character ได้

## Change impact
v0.5.0แก้ชุดให้ตรงownerและต้นฉบับ ปิดDEP-002 ยกเลิกสไตล์หัวโต3Dและภาพcandidateเดิม แก้CharacterBible/Sheet specification/prompts/locksและข้อมูลส่งต่อ รักษาcaption40ข้อและgeometryเดิม ไม่อนุมัติภาพแทนowner
