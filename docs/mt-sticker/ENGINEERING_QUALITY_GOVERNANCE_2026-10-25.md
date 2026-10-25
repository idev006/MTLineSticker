# MT Sticker A/B Engineering & Quality Governance — 2026-10-25

## Ownership model
The user approved twelve logical specialist responsibilities under four workstreams. These are responsibilities assumed by the assistant/tools, not claims that twelve independent humans were hired.
- System Architecture and Project Management: AI Systems Architect, Technical Project Manager, Prompt/Context Engineer
- GEM A Creative and Document Engineering: Creative Director, Python Backend Engineer, Thai Humor Specialist
- Platform & Visual Production: GitHub DevOps Engineer, Integration/Protocol Engineer, Computer Vision Engineer, Character Consistency Specialist
- Independent quality functions: QA Automation Engineer, Independent Quality Auditor

## Interfaces
- GitHub is canonical SSOT for document metadata, source code, QA evidence and handoff receipts. Owner attaches runtime photos/images directly to GEM B, never GitHub.
- Gate A1: official validator against exact commit, sha256 manifest, 40 exact captions, named PASS receipt; an uploaded workflow/updated plugin alone is never proof.
- Gate A2: GEM B reads A1 PASS independently then checks owner's attached imagery. No owner image means A2_AWAITING_OWNER_ASSETS, not RETURN_TO_GEM_A.
- Hero production requires both stages PASS and applicable Product Owner authorization. No fabricated approvals.

## v0.10.0 smoke checks executed
- GEM A script: test_director_validator.py — two smoke checks PASS (CLI supports --gate, SHA detects file mutation). This is **not** full project validation.
- GEM B script: test_image_qa.py — three synthetic tests PASS (valid transparent RGBA, RGB rejected, wrong aspect rejected). Not a test of a real character image.
- GEM B PNG checks cannot certify Thai captions, border, diecut or character identity and must report these as NOT_TESTED.

## Open acceptance blockers
- Official Gate A1 project report at gate-reports/SET-KHE-NOI-FIRST-HOME-001/A1_LATEST.json was last observed FAIL with validator_executed:false.
- GitHub Actions execution and full end-to-end A1->A2 production remain unverified. Do not label READY based on smoke tests.
- The shared default prompts still contain a legacy contract v1.1 reference; current higher-priority skills explicitly supersede it. Preserve defaults under plugin update policy; later reconcile only if allowed.

## Required release evidence
Source commit, actual validator exit code/report, manifest full SHA check, owner approvals in ledger, A1 receipt, B-side A2 asset inspection report, Hero approval, and real pixel QA.
