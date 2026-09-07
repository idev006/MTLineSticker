# MTLineSticker

SSOT repository for a multi-set LINE sticker product family.

## Architecture
- docs/project/ — project, brand, audience, product architecture, marketing, roadmap, decisions
- docs/characters/ — reusable character bibles and production standards
- docs/standards/ — LINE, caption, visual, QA and naming standards
- sets/ — one product folder per sticker set
- assets/shared/ — reusable character and texture masters
- assets/sets/ — set-specific source/candidate/approved/export assets
- data/ — registries across sets, characters, captions and assets
- scripts/ — project-level validation/build entry points
- engine/ — implementation of the production/QA pipeline

Product model: Brand → Characters → Sticker Sets → Individual Stickers

Current sets: SET-001-EVERYDAY-ADMIN (active), SET-002-MEETING, SET-003-FOLLOWUP, SET-004-DOCUMENT, SET-005-OFFICE-LIFE (planned).

Primary character: Phi Prom (พี่พร้อม), torn-paper administrative police mascot.
