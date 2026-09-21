# SET-008 — Kind Retired Lady

สถานะ: **Project Definition / Pre-Production**

ชุดสติกเกอร์ LINE สำหรับผู้หญิงวัยหลังเกษียณ บุคลิกใจดี มีเมตตา อบอุ่น สุภาพ และส่งต่อคำอวยพรให้เพื่อน ลูกหลาน และคนใกล้ชิด

## Product Goal
- Static LINE Sticker จำนวน 40 ภาพ
- ใช้ได้จริงในชีวิตประจำวัน
- เน้นคำอวยพร ความห่วงใย การทักทาย อารมณ์ และกิจกรรมหลังเกษียณ
- ภาพเป็นการ์ตูนกึ่งสมจริงเล็กน้อย แต่ยังดูเป็นผู้ใหญ่ สุภาพ และสง่างาม
- เครื่องแต่งกายเป็นชุดไทยหลายแบบ/หลายสี โดยรักษา character identity ให้คงที่

## Source of Truth
เอกสารในโฟลเดอร์ `ssot/` เป็นแหล่งอ้างอิงหลักของโครงการนี้

ลำดับอำนาจ:
1. OWNER-LOCKED requirements
2. CHARACTER-BIBLE
3. CAPTION-PRODUCTION-TABLE
4. PRODUCTION-SPEC
5. HERO-STICKER-PLAN
6. QA-CHECKLIST
7. Prompt documents

## Workflow
Project Brief → Character Bible → Character Sheet Candidate → Owner Approval → Hero Set → Owner Approval → Full 40 → QA → Export → LINE Creators Market

> ห้ามผลิต Full 40 ก่อน Character Sheet และ Hero Set ได้รับอนุมัติ

## Automation Safety
โครงการนี้ **ห้ามแก้ไขโปรแกรม auto-crop Python ที่มีอยู่ใน repository** เว้นแต่ Product Owner สั่งโดยตรง

## Branch
Initial project documents prepared on branch `set-008-kind-retired-lady`.
