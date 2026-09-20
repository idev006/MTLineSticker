# SET-008 — CHARACTER SHEET GENERATION PROMPT v1.0

ใช้เอกสารนี้ร่วมกับภาพอ้างอิงบุคคลและเอกสาร SSOT ของ SET-008

## Primary Prompt
สร้าง Character Sheet Candidate สำหรับ LINE Sticker ชุด **พงศธร** จากภาพอ้างอิงบุคคลจริง โดยรักษาความคล้ายของใบหน้า รูปศีรษะ ทรงผม อายุโดยประมาณ และรูปร่างให้จดจำได้ แต่ stylize เป็น polished semi-realistic cartoon ที่เหมาะกับ LINE Sticker

ตัวละครเป็นชายวัยผู้ใหญ่ บุคลิกผู้บังคับบัญชาระดับสูง สุขุม มั่นคง มีภาวะผู้นำ สุภาพ และเป็นมิตร ไม่ทำให้ดูเป็นตัวตลก

ชุดหลักต้องยึดภาพอ้างอิงล่าสุด: แจ็กเก็ตกีฬาเทาเข้ม แถบสีขาวตามแขน เสื้อด้านในสีดำ กางเกงโทนเข้มที่เข้าชุด ไม่มีตรา ยศ เครื่องหมาย หรือโลโก้ราชการ

สร้าง sheet ที่มี front, 3/4 left, 3/4 right, side, back, full-body neutral และ expression/gesture panel ตาม `CHARACTER-SHEET-SPECIFICATION-v1.0.md`

Expression ต้อง controlled และอ่านง่ายแม้ย่อภาพ โดยเฉพาะ neutral, mild smile, serious, worried, surprised, controlled anger, proud/pleased, sad/regretful

Gesture samples: greeting, thumbs up, OK hand, palm stop/reject, arms crossed/thinking, point/explain, hold document, meeting/listening

ห้ามมีข้อความ caption ในภาพ ห้ามใช้ธีม badminton ห้ามใส่ไม้แบดหรือลูกขนไก่

## Rendering Direction
- clean professional illustration
- semi-realistic cartoon
- consistent facial identity across every pose
- proportionate body, healthy and sturdy
- slightly simplified details for sticker readability
- clean white/neutral review background
- clear spacing between views

## Output Intent
ผลลัพธ์นี้เป็น Candidate เท่านั้น ยังไม่ถือเป็น `CHARACTER_SHEET_ACTIVE` จนกว่า Product Owner จะอนุมัติ
