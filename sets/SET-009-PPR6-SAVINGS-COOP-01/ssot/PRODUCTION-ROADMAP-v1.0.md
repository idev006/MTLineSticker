# PRODUCTION ROADMAP v1.0 — SET-009

## Phase 0 — Foundation
สถานะ: **IN PROGRESS**

งาน:
- ล็อก Product SSOT
- ล็อก Character Bible
- ยืนยัน Character Sheet Active
- กำหนด scope 40 stickers
- กำหนดวัตถุประสงค์การใช้งานในกิจกรรมสหกรณ์

Gate: ห้ามเริ่ม Full Production ก่อนผ่าน Hero Review

## Phase 1 — Content Architecture
เป้าหมาย: สร้างรายการ 40 intents ที่ไม่ซ้ำหรือใกล้เคียงกันเกินไป

งาน:
- แบ่งหมวด everyday / service / savings / activity / warm relationship
- เขียน caption สั้น อ่านเร็ว
- ออกแบบ pose + facial expression + prop ต่อเฟรม
- ตรวจ duplicate intent และ duplicate silhouette

Deliverable:
- `FULL-STICKER-PRODUCTION-TABLE-v1.0.md`

## Phase 2 — Hero Development
เป้าหมาย: ทดสอบระบบภาพก่อนผลิตครบชุด

จำนวนแนะนำ: 8–12 Hero stickers

ต้องครอบคลุม:
- pose ยืน
- pose เคลื่อนไหว
- prop การออม
- prop งานบริการ
- emotion อบอุ่น
- hoodie look
- secondary outfit อย่างน้อย 1 แบบ

Review criteria:
- character fidelity
- readability at chat size
- caption hierarchy
- silhouette uniqueness
- brand fit
- merchandise potential

## Phase 3 — Full Production
เมื่อ Hero ผ่านแล้วจึงขยายเป็น 40 stickers

แนวทาง batch:
- Sheet 1: 01–10
- Sheet 2: 11–20
- Sheet 3: 21–30
- Sheet 4: 31–40

ทุก batch ต้อง QC ก่อนเริ่ม batch ถัดไปเพื่อหยุด style drift ตั้งแต่ต้น

## Phase 4 — QA
QA 5 ชั้น:
1. Character QA
2. Communication QA
3. Duplicate QA
4. Technical / crop QA
5. Brand & merchandise QA

Reject เมื่อ:
- สัดส่วน/ใบหน้า drift
- หางขาวผิดรูปหรือหาย
- pose สื่อไม่ชัด
- caption ซ้ำ/ใกล้กันเกินไป
- ข้อความอ่านยากเมื่อย่อ
- detail บางเกินไปสำหรับของชำร่วย

## Phase 5 — LINE Export
เตรียม:
- sticker PNG transparent
- main image
- tab image
- metadata/caption audit
- naming convention

Technical spec ของ export ให้ล็อกใน `PRODUCTION-SPEC-v1.0.md` ก่อน export จริง โดยตรวจ requirement ล่าสุดของ LINE Creators Market ณ เวลาส่ง

## Phase 6 — Merchandise Adaptation
เลือกอย่างน้อย 10 key poses มาทำ master merchandise views:
- plush toy
- acrylic/PVC keychain
- ceramic mug
- tumbler
- tote bag
- die-cut sticker
- enamel pin
- T-shirt / polo graphic

หลักการ: merchandise adaptation ต้องอิง master character เดิม ไม่ redesign ตัวละครใหม่ตามสินค้าแต่ละชนิด

## Approval Flow
**Documents → Character lock → Hero → Owner approval → 40 production → QA → LINE export → Merchandise masters**
