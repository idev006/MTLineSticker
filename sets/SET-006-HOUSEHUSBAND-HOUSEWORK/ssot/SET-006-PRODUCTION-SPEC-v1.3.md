# SET-006 Production Spec v1.3

**Status:** Active production specification  
**Set:** SET-006-HOUSEHUSBAND-HOUSEWORK

This version aligns SET-006 with CPDF 1.3 and the current Gem A → Gem B → Program/Engine architecture.

## 1. Core production principle
SET-006 is a LINE sticker communication product. Visual production may be delivered as high-resolution Master Sticker Sheets containing multiple independent Frames. The existing Program/Engine is responsible for deterministic splitting, resize/normalization, validation, naming and packaging.

## 2. Frame preflight
Before visual generation, every Frame must have:
- Frame/sticker ID
- exact caption
- sender intent
- likely chat situation
- emotion/tone
- primary expression
- primary gesture/action
- minimum useful props
- camera/composition guidance when material
- forbidden distractions/drift
- approved Character Sheet reference
- relevant Golden Reference

No visual generation begins with unresolved blocking fields.

## 3. Visual Master Package — visual SSOT
After Gate B PASS, the visual source of truth is the approved **Visual Master Package** containing:
- one or more Master Sticker Sheets and/or approved Master Frames,
- deterministic Frame order mapping,
- Sheet/Grid geometry,
- exact caption mapping,
- Character/Golden Reference record,
- Visual QA evidence,
- handoff status `READY_FOR_ENGINE`.

The Program/Engine then creates the individual technical files. Those individual outputs become the Technical SSOT after Gate C.

## 4. Master Frame / Sticker Sheet profile
Default visual production profile:
- logical Frame size: **512 × 512 px**
- equal-size Frames within each Sheet
- preferred production Sheet: **5 columns × 2 rows**
- 10 Frames per standard Sheet
- logical standard Sheet size: **2560 × 1024 px**
- row-major Frame order unless a Sheet manifest states otherwise
- no artwork, typography or props may cross Frame boundaries
- high-detail clean source suitable for resize-down

A 6-Hero calibration Sheet may use a declared 3×2 layout with equal 512×512 logical Frames. Its mapping must be explicit.

## 5. Character / Golden Reference
H01 / #01 “ล้างจานอยู่ครับ” remains an owner-approved visual Golden Reference together with the approved Character Sheet.

Locked identity includes adult proportions, very-short military/police-inspired haircut, navy shirt, black shorts where visible, orange-shoe signature where visible, black tactical watch on the left wrist, and restrained use of the black crossbody bag.

## 6. Communication and clutter control
Each Frame must pass the 1-second communication test. Character/action/caption dominate; props are limited to what improves meaning. Do not turn a Frame into a room scene, poster or infographic.

## 7. Typography
Exact Thai wording is mandatory. AI-rendered Thai remains candidate-level until verified. If the downstream workflow applies deterministic typography, visual composition must reserve suitable space without changing the approved caption.

## 8. Hero Gate
Hero Frames:
- H01 / #01 — ล้างจานอยู่ครับ
- H02 / #05 — กำลังถูพื้นครับ
- H03 / #15 — พับผ้าอยู่ครับ
- H04 / #21 — ทำกับข้าวอยู่ครับ
- H05 / #31 — กำลังจัดบ้านครับ
- H06 / #40 — พ่อบ้านพร้อมลุยงานบ้านครับ!

The owner-approved six-Hero visual direction may be used as a concept/style calibration reference. Gate B still requires a usable Visual Master Package with declared equal Frame geometry, mapping, readable communication, Character consistency, and sufficient source quality.

Hero PASS unlocks full 40 production. Failed Hero Frames are corrected at Gem B; product/caption defects return to Gem A.

## 9. Full 40 production
After Hero Gate PASS:
- create 4 standard Master Sticker Sheets of 10 Frames each unless the approved package defines another deterministic mapping,
- maintain equal 512×512 logical cells,
- run visual QA per Frame and per Sheet,
- correct failed Frames/Sheets without redefining passed upstream product decisions,
- hand off only an approved Visual Master Package with status `READY_FOR_ENGINE`.

## 10. Program/Engine boundary
The existing Program/Engine owns downstream deterministic processing, including splitting, resize/normalization, approved alpha/background processing, naming, technical validation, manifest generation, export and packaging.

This document does not authorize modification of that software.

## 11. Final technical files
After Program/Engine processing, Gate C must produce the individual technically prepared sticker files and required submission package evidence with status `READY_FOR_FINAL_QA`.

Official LINE requirements are checked at the technical/submission stage and override internal assumptions when changed.

## 12. Blocking visual defects
Gate B blocks on wrong Character identity, unapproved chibi drift, wrong/altered caption, unclear primary intent, excessive scene clutter, unreadable text/action, important crop, inconsistent Frame geometry, cross-frame bleed, insufficient source quality, or incomplete Frame mapping.

## 13. Traceability
Each final file must trace to:
`final file → manifest → Sheet/Frame ID → Frame brief → caption/use case → Product Brief → Character/Style SSOT`.

## 14. References
- `../../../docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`
- `../../../docs/project/QUALITY_GATE_STANDARD.md`
- `../../../docs/gems/GEM_KNOWLEDGE_PACKAGING_STANDARD.md`
- `../../../docs/standards/MASTER_SHEET_FRAME_STANDARD.md`
- `../docs/08-qa-checklist.md`
- `../reviews/HERO-FIT-GATE.md`
