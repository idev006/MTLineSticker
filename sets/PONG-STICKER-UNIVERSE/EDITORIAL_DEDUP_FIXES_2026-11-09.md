# Global caption dedup fixes

All 13 sets read back at preceding snapshot and 7 exact normalized collisions discovered. Applied 7 candidate replacement texts in sets 09,10,11,12,13; affected frames.json, caption_master.json, CAPTION_MASTER.csv, FRAME_MATRIX.md updated as one Git tree. This is an editorial draft correction, NOT Product Owner G3 approval.

- PONG-SET-09 frame 14 → ตรวจมาตรฐานให้ครบ
- PONG-SET-10 frame 9 → ค้นหาข้อเท็จจริง
- PONG-SET-10 frame 33 → ประสานเพื่อความเป็นธรรม
- PONG-SET-11 frame 6 → รับฟังความเห็นต่าง
- PONG-SET-12 frame 7 → ผนึกกำลังทุกฝ่าย
- PONG-SET-13 frame 9 → ประชาชนต้องมาก่อน
- PONG-SET-13 frame 14 → แบ่งปันมุมมองใหม่

After commit, independent full 13-set readback and duplicate check is required before claiming zero duplicates.
