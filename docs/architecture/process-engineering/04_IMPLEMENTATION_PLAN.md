# Implementation Plan — Two Private Plugins

Status: design; plugins not created by this document.

## Architecture
GEM A private plugin: responsible for evidence intake, product design, Character Bible and generation spec, 40-frame communication design, mapping, QA planning, versioned package and Gate A.

GEM B private plugin: consumes validated GEM A package and owner-approved Character, produces selected Hero candidates only first, enforces Hero owner approval, then produces batches, visual QA and engine handoff.

Shared contract/validators: schema, reference hashing, frame reconciliation, transition guards, approvals, retries and set-specific batch layout. Deterministic engine stays independent.

## Phases
1. Freeze current repository baseline and reconcile GEM A deploy version 2.6 vs earlier skill 2.5 and GEM B 2.3.
2. Implement versioned handoff schema, source registries and approval receipts.
3. Implement regression fixtures covering T01–T17.
4. Package and privately deploy GEM A; test evidence/doc completeness.
5. Package and privately deploy GEM B; test capability checks and scope guards.
6. Run GEM A to GEM B integration and full pilot for CHAICHAT #1.
7. Archive results, review P0 failures and release with rollback plan.

## P0 tasks
- Source and Character Sheet assets must be accessible and content-hashed.
- Full 40/40 matrix/mapping consistency.
- Owner approvals must bind the exact version.
- Respect set-specific five sheets of eight frames.
- Block unsafe stage transitions and preserve provenance.

## Open decisions
- CHAICHAT #1 publication name remains provisional.
- Need exact approved Character image binary and approval receipt committed/imported.
- Reconcile per-set 5x8 mapping against generic 4x10 production default.
- Confirm private plugin deployment after integration criteria pass.

This phase is documentation only. Do not modify current production engine or existing deployments.
