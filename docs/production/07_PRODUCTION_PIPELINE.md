# Production Pipeline & Technical Requirements

## 1. Pipeline
Research → workflow map → caption shortlist → Character Bible → Character Sheet → caption-to-pose mapping → prototype 8 → target-user validation → revise → produce 40 → QA → package → submit → launch → measure.

## 2. Prototype 8
Initial recommended prototype coverage:
1. รับทราบครับ
2. รบกวนส่งข้อมูลครับ
3. ขอเชิญครับ
4. ขอติดตามครับ
5. ด่วนที่สุดครับ!
6. งานเข้าครับ!
7. ขอพักแป๊บ
8. รับทราบ...แต่ไม่รับเรื่อง

These span professional, request, meeting, follow-up, urgency, workload, human moment, and humor.

## 3. LINE Static Sticker Technical Baseline
Current official LINE Creators Market guidance (checked 2026-08-26):
- Sticker set quantity options include 8, 16, 24, 32, or 40
- Main image: 240 × 240 px
- Sticker image: up to 370 × 320 px
- Chat thumbnail: 96 × 74 px
- PNG format
- Sticker imagery should be easy to use in everyday conversation and easy to understand

Sources:
- https://creator.line.me/th/guideline/customsticker/
- https://creator.line.me/en/guideline/sticker/

Re-check official guidelines immediately before final submission in case platform requirements change.

## 4. Asset Naming
Recommended:
- `SET01-STK-001.png` … `SET01-STK-040.png`
- `SET01-MAIN.png`
- `SET01-TAB.png`

## 5. Asset Directory
- `assets/character-sheets/` canonical character references
- `assets/stickers/set01/working/` working images
- `assets/stickers/set01/final/` approved exports
- `assets/marketing/` store/launch promotional art

## 6. Caption-to-Pose Sheet
Before image generation, every sticker row must specify:
- sticker ID
- caption
- workflow domain
- relationship mode
- tone class
- facial expression
- pose
- prop
- text placement
- humor/safety note

## 7. Image Generation Rule
Generated images are candidates, not canonical assets until QA checks character consistency, text accuracy, platform size, transparency, and appropriateness.

## 8. Export Rules
- transparent background where required
- sufficient margin around art/text
- clean alpha edges
- no unintended artifacts
- text rendered exactly as approved
- verify Thai diacritics and glyph integrity

## 9. Submission Review
Review current official LINE review guidelines before submission. Platform may request evidence of rights for imagery or reject inappropriate content.
Source: https://creator.line.me/th/review_guideline/
