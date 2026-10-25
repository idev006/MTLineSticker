# Cross-GEM Handoff Protocol v2.0

## Source of truth
GitHub stores DOCUMENTS only. The Product Owner supplies approved Character Sheet, briefcase photographs and other images directly to GEM B. Absence of binaries in GitHub is never a Gate A1 defect.

## Gate A1 owner GEM A
Complete all Output Registry documents, generate SHA-256 manifest, execute the official GEM A --gate a1 validator against actual documents and read back a pinned GitHub source commit. Publishing a workflow or updating a plugin does NOT constitute a PASS.

## Canonical receipt
External path: gate-reports/SET-KHE-NOI-FIRST-HOME-001/A1_LATEST.json.
Required fields: schema_version=2.0, set_id, gate=A1, status=PASS|FAIL, validated_source_commit, validator_version, validator_executed=true, validator_exit_code, manifest_sha256_verified, manifest_payload_count, caption_master_version=0.4.0, caption_exact_count=40, character_approval_recorded, binary_delivery=OWNER_TO_GEM_B_RUNTIME, a2_status=AWAITING_OWNER_ASSETS, errors, timestamp_utc.
The validated_source_commit points to exact validated package bytes; the subsequent receipt commit is a separate immutable commit.

## Gate A2 owner GEM B
Before inspecting binaries, fetch the A1 receipt, verify PASS/exit 0/manifest integrity and independently re-read all documents at validated_source_commit. A1 missing or unverified: return only document issues to GEM A. If A1 passed, inspect user's runtime images and check identity, SHA when available, anatomical LEFT hand on case, fidelity and quality. No requirement to upload binaries to GitHub.

## Hero production
Only after A1 and A2 PASS, plus applicable owner authorization. Initial Hero order F09, F01, F17, F29. Never modify approved forty captions. Visual and pixel QA belongs to GEM B.

## Current evidence
As of source commit 628850936c2669f0dc9c78f3c65b99ce3c19b0f5, GitHub had NO confirmed A1_LATEST.json report. Therefore A1_BLOCKED, NOT A1_READY. This policy file does not certify a validator run.
