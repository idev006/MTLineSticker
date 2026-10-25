# GEM A / GEM B v0.12.0 — Input/Output Release Record

## Official plugin releases
- GEM A v0.12.0: plugins_6ad844f4cd8c8191aa0282099b84bb14 — source release pluginrel_6add7d4712e08191a3397e7c36aaf844
- GEM B v0.12.0: plugins_6ad84507f928819180ee48d94c5a06be — source release pluginrel_6add7d548134819189a5c8d48525aabb

## Owner instructions
GitHub is the sole SSOT for documents, code, manifests and receipts. Only the Product Owner supplies Character Sheet / bag photographs as runtime image attachments directly to GEM B. Binary assets are NOT an A1 prerequisite and must not be requested for GitHub. Approved caption master v0.4.0 / 40 frames cannot be changed without approval.

## GEM A
Input: set ID, GitHub path and source commit, approved captions, 40 frame plans, reference/approval metadata. Output: complete validated documents + SHA256 manifest + machine-verifiable A1 receipt pinned to source SHA. Official validator must run against the real project and exit 0 before A1_PASS. Document failure -> GEM A.

## GEM B
Input: verified GitHub A1 PASS receipt, matching source commit and manifest, owner runtime images attached at A2. Output: A2 image approval/evidence, authorized Hero previews, 40 PNG frames, five 4x2 sheets, pixel and visual QA. Image absence -> A2_AWAITING_OWNER_ASSETS, never A1 fail.

## Executed local regression test evidence on 2026-10-25
- GEM A test_director_validator.py: PASS 3/3 — external runtime images allowed in A1; tampered SHA detected; missing document rejected.
- GEM B test_handoff_contract.py: PASS 4/4 — valid receipt; wrong source SHA rejected; FAIL receipt rejected; modified document rejected.
- GEM B test_image_qa.py: PASS 3/3 — RGBA frame; RGB image rejected; incorrect aspect rejected.
- Tests are synthetic fixtures: **NOT** a successful GitHub Actions run, whole-set character visual review, or real project A1 certification.

## Live project blocker
SET-KHE-NOI-FIRST-HOME-001 latest A1 receipt remains FAIL / validator_executed:false on last confirmed readback. No A1 PASS claim or Hero production authorization until the official validator executes on a GitHub-pinned real package. 
