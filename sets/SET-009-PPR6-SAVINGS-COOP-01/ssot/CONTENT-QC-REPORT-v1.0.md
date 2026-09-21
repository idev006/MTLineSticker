# CONTENT QC REPORT v1.0 — SET-009

ชุด: **สหกรณ์ออมทรัพย์ตำรวจภูธรภาค 6 หมายเลข 1**  
ตรวจตาม `CONTENT-QC-PROTOCOL-v1.0.md`  
ขอบเขต: 40 captions + intents + poses + facial expressions + props + usage scenarios

## Result Summary
- Total frames reviewed: **40**
- KEEP: **40**
- REWORK blocking: **0**
- REPLACE blocking: **0**
- Duplicate caption: **0**
- Exact duplicate intent: **0**
- Blocking pose/silhouette duplicate: **0**
- Blocking prop duplicate: **0**
- Audience coverage: **PASS** — เจ้าหน้าที่สหกรณ์ + สมาชิกสหกรณ์
- Overall internal QC: **PASS — READY FOR OWNER REVIEW**

## QC Review by Dimension

### 1. Caption Duplicate Review — PASS
ไม่พบ caption ซ้ำตรงตัว และได้แก้ draft ที่มีความเสี่ยงใกล้กัน เช่น:
- ตัด `เจอกันครับ` ออกจาก Everyday เพราะใกล้กับ `พบกันที่สหกรณ์ครับ` และ `เจอกันที่กิจกรรมครับ`
- ไม่ใช้ `ขอบคุณจากใจครับ` เพิ่ม เพราะใกล้กับ `ขอบคุณครับ`; เปลี่ยน warm slot เป็น `สุขภาพแข็งแรงนะครับ`

### 2. Semantic / Intent Overlap — PASS
คู่ที่มีความหมายอยู่ในกลุ่มเดียวกันแต่ยังใช้งานคนละสถานการณ์ชัดเจน:
- `รับทราบครับ` = acknowledge received information/order
- `ได้เลยครับ` = accept and commit to action
- `เอกสารครบแล้วครับ` = document completeness
- `ดำเนินการเรียบร้อยครับ` = process completion
- `สู้ ๆ ครับ` = energetic encouragement
- `ส่งกำลังใจให้ครับ` = compassionate support
- `ออมก่อน ใช้ทีหลัง` = behavioral reminder
- `เติมกระปุกกันครับ` = immediate saving action
- `ออมวันนี้ เพื่อวันหน้าที่มั่นคง` = long-term saving mindset
- `มีเงินออม อุ่นใจกว่า` = emotional reassurance from having savings

### 3. Pose / Gesture Review — PASS
กำหนด silhouette ที่แตกต่างกัน เช่น โบกมือ, ไหว้, วันทยหัตถ์, thumbs-up, ก้มขอโทษ, โบกปฏิเสธเบา ๆ, ดูนาฬิกา, วิ่ง, double thumbs-up, ช่อดอกไม้, กำหมัด, กอดหัวใจ, นั่งพัก, นอน, กางแขน, โบกลาพร้อมกระเป๋า, โค้งต้อนรับ, ตรวจเอกสาร, ชู checklist, ชี้ form, รับซอง, กอดแฟ้ม, ปั๊มตรา, โทรศัพท์, ชี้อาคาร, ถือกระปุก, หยอดเหรียญ, เรียงเหรียญ, ชี้ planner, ปลูกต้นกล้า, กอดกระปุกใต้ร่ม, สะพายเป้, teamwork gesture, ถือปฏิทิน, เต้น, เดินไปด้วยกัน, ถือเค้ก, ยื่นดอกไม้, ยื่นหัวใจ, ยืดเส้นพร้อมขวดน้ำ

ข้อควบคุม: thumbs-up ไม่ใช้เป็น gesture หลักเกิน 2 เฟรม และการไหว้มีเฉพาะ intent ขอบคุณหลักเท่านั้น

### 4. Facial Expression Review — PASS
กระจายอารมณ์ครบทั้ง:
- สดใส/ทักทาย
- สุภาพ/ขอบคุณ
- มั่นใจ/รับทราบ
- สำนึกผิด
- ปลอบใจ
- ตั้งใจ/โฟกัส
- ตื่นเต้น
- ภูมิใจ
- อบอุ่น/ห่วงใย
- ง่วง/พักผ่อน
- มีความหวัง
- เห็นอกเห็นใจ
- เฉลิมฉลอง

ไม่มีการใช้ “ยิ้มแบบเดียวกันทุกเฟรม” เป็นค่า default โดยไม่สัมพันธ์กับ intent

### 5. Prop Review — PASS
Prop ถูกกำหนดตามหน้าที่ เช่น เอกสาร/clipboard/ตรายางใช้ใน workflow เจ้าหน้าที่, กระปุก/เหรียญ/ต้นกล้าใช้ใน savings, เค้ก/ดอกไม้/หัวใจใช้ใน emotional/celebration และกระเป๋า/ปฏิทิน/ป้ายกิจกรรมใช้ใน movement/activity

อนุญาตให้ prop family เดียวกันซ้ำได้เมื่อ intent ต่างกันจริง เช่น `กระปุกหมู` ใน 26/27/31 แต่ action และความหมายต่างกันชัดเจน

### 6. Usage Coverage — PASS
โครงสร้าง 40 เฟรม:
- Everyday Communication: 16
- Cooperative Service: 9
- Savings & Financial Wellbeing: 6
- Activity & Community: 5
- Warm / Celebration: 4

ครอบคลุมทั้ง:
- เจ้าหน้าที่ → สมาชิก
- สมาชิก → เจ้าหน้าที่
- สมาชิก ↔ สมาชิก
- งานกิจกรรม/ประชาสัมพันธ์แบบเป็นมิตร

## Hero Calibration Check
Hero 6 ที่ใช้ตรวจมาตรฐานภาพ:
1. สวัสดีครับ
2. ขอบคุณครับ
3. รับทราบครับ
4. สู้ ๆ ครับ
5. ยินดีให้บริการครับ
6. ออมก่อน ใช้ทีหลัง

Hero ทั้ง 6 ครอบคลุม greeting, gratitude, acknowledgment, encouragement, cooperative service และ savings ซึ่งเพียงพอสำหรับ calibration ด้าน character consistency, typography, expression, gesture, prop และ die-cut white backing ก่อน Full Production

## Non-blocking Watch Items for Image Production
- ระวัง 12 `ดูแลตัวเองด้วยครับ`, 15 `คิดถึงนะครับ`, 39 `ส่งกำลังใจให้ครับ` ไม่ให้ภาพออกมาเป็น “กอดหัวใจเหมือนกัน” ต้องรักษา pose ตามตาราง
- ระวัง 19 `เอกสารครบแล้วครับ`, 22 `ได้รับเอกสารแล้วครับ`, 23 `ดำเนินการเรียบร้อยครับ` ให้ prop/action ต่างกันชัดเจน
- ระวัง 26–31 กลุ่มการออมไม่ให้ทุกเฟรมเต็มไปด้วยกองเหรียญและกระปุกหมูจน silhouette ซ้ำ
- ชุดตำรวจใช้เป็น accent ไม่ใช่ default เพื่อคงความเป็นมิตรของมาสคอตสหกรณ์

## Final Gate
Internal Content QC: **PASS**  
Next gate: **Product Owner review / approve captions + visual directions**  
หลังอนุมัติแล้วจึงผลิต Full Sticker Sheets 40 เฟรมตาม `PRODUCTION-SPEC-v1.0.md`
