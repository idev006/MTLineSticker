# Sprint 01 — MTLineSticker AI Engineering Team

Date: 2026-10-21. Owner-approved seven specialist roles are a review framework, not separately provisioned agents.

## In-progress delivery
- DevOps/CI: GitHub Actions contract test workflow added; actual hosted run result must be checked before marking CI green.
- QA: existing v1 and v1.1 unit test suites selected by unittest discovery; no claim that the GitHub runner has passed until run evidence is available.
- Systems: existing v1.1 validator checks local hashes and gate guards, but does not verify real Product Owner identity. Approval authenticity remains a P0 item.
- Process: CHAICHAT #1 explicitly maps 5 sheets × 8 frames; generic GEM B 4 × 10 default requires set-specific override test and deployment update.
- Character/Art: approved concept is recorded in chat, but original approved visual and SHA256/approval receipt are not yet committed. Actual likeness check is pending verified assets.
- LINE release: official current sticker dimensions/format requirements must be rechecked before release; do not claim certification.

## Acceptance criteria
1. GitHub CI must show passing run for both contract test suites.
2. Any failing tests are defects to fix, not grounds to waive the gate.
3. Build a separate schema validation test that checks mandatory fields, format and rejected invalid objects.
4. Store approved character asset in controlled path with SHA256 and approval evidence.
5. Design signed/authorized approval control or require explicit operator verification.
6. Integrate set-specific 5x8 mapping into GEM B's actual configuration.
7. Run a controlled dry run from GEM A package to GEM B preflight before plugin packaging.

## No unverified claims
CI configuration committed is not equal to CI executed. No private plugins are created by this sprint file.
