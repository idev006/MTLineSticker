# Decision Log

## 2026-09-12 — Communication-first corrective framework upgrade
- SET-006 Hero round 1 exposed a process defect: visually attractive outputs could still drift into chibi/infographic/scene illustration and fail as LINE communication assets.
- Root cause: character lock existed, but the project framework did not make communication intent, chat use case, 1-second readability, individual-master production and Golden Reference control explicit enough.
- Corrective action: CPDF upgraded to v1.1; Sticker Communication Standard and QA Standard upgraded; SET-006 Hero/QA/Visual/Production documents revised.
- New mandatory rule: **one sticker = one primary communication intent** with exact caption, sender intent, likely chat situation, expression/action, minimum useful prop and active character reference defined before generation.
- New mandatory test: **1-second communication test** at chat-preview scale.
- New production rule: approved **individual sticker masters are SSOT**; multi-panel/contact sheets are QA artifacts and must not substitute for individual production approval.
- New typography rule: AI-rendered Thai is candidate-level only until verified; deterministic typography is required when exact wording cannot be guaranteed.
- Character correction rule: unapproved adult-to-chibi conversion is a blocking defect.
- Owner approved H01 / “ล้างจานอยู่ครับ” as SET-006 Hero Golden Reference. H02–H06 must now be produced sequentially as standalone stickers and pass QA individually before the full Hero Gate can pass.
- Full 40-sticker production remains blocked until Hero Fit Gate = PASS.

## 2026-08-27 — Caption review v0.9
- Set 01 remains focused on Thai police administrative/work-support personnel and everyday work communication.
- The 40-caption list was re-reviewed for workflow relevance, redundancy, practical frequency, clarity, emotional value, brand distinctiveness, and safety.
- Replaced overlapping or weaker phrases with higher-value utility phrases including “เดี๋ยวแจ้งกลับครับ”, “รบกวนตรวจสอบครับ”, and “ขอบคุณครับ”.
- “ติดประชุมครับ” replaces “เข้าประชุมครับ” because it communicates availability more usefully in chat.
- “กำลังติดตามครับ” replaces “ตามให้อยู่นะครับ” for broader professional use.
- “ขอเชิญประชุมครับ” replaces “เชิญประชุมครับ” for tone consistency.
- Urgency trio remains: “ด่วนครับ!”, “ด่วนมากครับ!”, “ด่วนที่สุดครับ!” and should form a visual escalation trilogy.
- Signature humor “รับทราบ...แต่ไม่รับเรื่อง” remains, but must be visually framed as peer-context deadpan humor and not as dereliction of duty.
- Status: Content Candidate v0.9. Not final production lock.
- Full 40-sticker production remains blocked until Character Master Sheet + Prop Sheet + material/readability gates pass.

## 2026-08-27 — Paper-Tear Character Direction
- Generic chibi police directions were rejected for weak distinctiveness and low memorability.
- The project moved to “พี่พร้อม: Paper-Tear Mascot”.
- The character itself must be built from deliberately rough torn-paper collage; torn paper is not merely a background treatment.
- Character identity must survive removal of uniform, text and props.
- Working character hook: “ตัวเล็ก งานใหญ่ หน้านิ่ง แต่เอาอยู่”.
- Internal brand DNA: “พร้อมครับ...ประมาณหนึ่ง”.
- Full sticker production is blocked until the character passes silhouette, de-uniform, face-crop, behavior and tiny-size recognition tests.

## 2026-08-27 — Repository Destination
- GitHub SSOT destination confirmed as `idev006/MTLineSticker`.
- Project documents and future approved reference artifacts should be stored in this repository.
