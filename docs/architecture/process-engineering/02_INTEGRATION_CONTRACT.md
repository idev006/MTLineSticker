# Integration Contract v1.0 — Design Proposal

Status: Proposed, not implemented.

## Authority and identity
A handoff must pin set_id, run_id, git commit SHA, package SHA256, character asset SHA256, approval receipt IDs, approved source reference roles, declared frame IDs, hero IDs, and batch mapping. No approval without owner decision and exact asset fingerprint.

## Envelope fields
- contract_version: 1.0.0
- set_id; run_id; stage; status; source_commit
- package_manifest_sha256
- reference_manifest: asset identifier, role, authority, hash
- character: active asset hash, Character Sheet approval receipt, lock version
- frames: full list F01 through F40, caption state, intended action, mapping
- hero_ids; batch_map; blocking_issues; validation_result
- producer/version/creation date and output hashes

## Invariants
1. Caption Master, Communication Matrix, and Frame Mapping must contain the same 40 unique IDs without omissions or duplicates.
2. GEM B may execute but not change approved Character or frame intents.
3. Only Product Owner approval grants Character activation and Hero unlock.
4. Character changes invalidate related downstream approvals.
5. A handoff with missing source/reference/Character files is not ready.
6. Attempting to resume the same run and input hash must not duplicate outputs.
7. On version conflict, stop and report precise source and expected/current revision.

## Process-state transitions
Brief -> GEM A internal QA -> Character candidate -> Owner-approved active Character -> Gate A pass -> READY_FOR_GEM_B -> Hero candidates -> Owner Hero approval -> FULL_PRODUCTION_UNLOCKED -> Batches and QA -> READY_FOR_ENGINE -> Export and Final QA -> LINE_SUBMISSION_READY.

Each GEM keeps its existing component-local state vocabulary; implement mapping in an orchestrator.

## CHAICHAT #1 exception
The currently documented set-specific mapping is five sheets of eight frames. Generic GEM B defaults to four sheets of ten. Set-level mapping takes precedence only after contract validation and owner acceptance; otherwise return SHEET_LAYOUT_DEFAULT_CONFLICT.

Source image and active Character Sheet binaries are not verified in GitHub. Do not mark the current set READY_FOR_GEM_B until validated.

## Versioning
Use semantic versioning for contract schemas and immutable SHA256 content hashes for approvals and visual assets. Preserve the previous approved artifact on every revision. Every output records input commit and version lineage.
