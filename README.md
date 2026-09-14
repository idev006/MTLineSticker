# MTLineSticker

SSOT repository for a multi-set LINE sticker product family.

## Start Here
If you want to create a sticker set and do not want to read the whole repository first:

- [START HERE — simple user roadmap](docs/workflow/START_HERE.md)
- [Copy-paste Prompt Library](docs/workflow/COPY_PASTE_PROMPT_LIBRARY.md)

These two documents are the recommended entry point for normal operators.

## Architecture
- docs/project/ — project, brand, audience, product architecture, marketing, roadmap, decisions
- docs/characters/ — reusable character bibles and production standards
- docs/standards/ — LINE, caption, visual, QA and naming standards
- docs/workflow/ — user roadmap, end-to-end production pipeline, AI/tool usage guide, gates and operator runbook
- sets/ — one product folder per sticker set
- assets/shared/ — reusable character and texture masters
- assets/sets/ — set-specific source/candidate/approved/export assets
- data/ — registries across sets, characters, captions and assets
- scripts/ — project-level validation/build entry points
- engine/ — implementation of the production/QA pipeline

## Production Workflow
For deeper detail:

- [Workflow index](docs/workflow/README.md)
- [End-to-end LINE Sticker Pipeline](docs/workflow/LINE_STICKER_END_TO_END_PIPELINE.md)
- [AI & Tool Usage Guide](docs/workflow/AI_TOOL_USAGE_GUIDE.md)
- [Production Runbook & Gates](docs/workflow/PRODUCTION_RUNBOOK_AND_GATES.md)
- [Gem Operational Playbook](docs/gems/GEM_OPERATIONAL_PLAYBOOK.md)

Product model: Brand → Characters → Sticker Sets → Individual Stickers

Current sets:
- SET-001-EVERYDAY-ADMIN (active)
- SET-002-MEETING (planned)
- SET-003-FOLLOWUP (planned)
- SET-004-DOCUMENT (planned)
- SET-005-OFFICE-LIFE (planned)
- SET-006-HOUSEHUSBAND-HOUSEWORK (documentation complete / ready for hero production)

Primary existing character family: Phi Prom (พี่พร้อม), torn-paper administrative police mascot.

Additional character IP in development: พ่อบ้านสายวินัย / Disciplined Househusband.
