# FMEA and Verification Test Plan

Status: proposed risk estimates, not measured incidents.

Severity/Occurrence/Detection ranked 1..5; risk score is the three values multiplied.

| Risk | Failure | S/O/D | RPN | Required control |
|---|---|---|---|---|
| R01 | Old/wrong identity reference | 5/3/4 | 60 | Reference role index and source hash |
| R02 | Character identity/style drifts between batches | 5/4/3 | 60 | Approved Character lock and visual QA |
| R03 | Hero approval bypassed | 5/3/2 | 30 | Transition guard and owner receipt |
| R04 | Missing/duplicate frame | 5/3/1 | 15 | 40/40 deterministic reconciliation |
| R05 | Unwanted captions in no-text set | 4/3/3 | 36 | Content and thumbnail inspection |
| R06 | Generic 4x10 supersedes set 5x8 | 4/4/2 | 32 | Explicit mapping and override validation |
| R07 | Stale version of inputs | 5/3/3 | 45 | Immutable commit and asset hashes |
| R08 | Missing image reference binary | 5/3/2 | 30 | Asset availability and checksum |
| R09 | Invalid transparency/dimensions | 4/3/1 | 12 | Technical engine validation |
| R10 | AI edits approved source without review | 5/2/4 | 40 | Protected source and diff review |

## Acceptance Tests
- T01: correct 40 IDs across three sources -> PASS.
- T02: omit F17 in mapping -> FAIL with missing ID.
- T03: duplicate F07 -> FAIL with duplicate ID.
- T04: validated 5x8 set override -> PASS.
- T05: conflicting 4x10 against 5x8 -> FAIL.
- T06: no approved Character binary -> block Hero rendering.
- T07: changed Character file hash -> invalidate approval.
- T08: request Hero before Gate A -> block.
- T09: request all 40 before Hero approval -> block.
- T10: words appearing in no-caption output -> reject.
- T11: wrong photo source -> reject.
- T12: duplicate retry with same input digest -> no duplicate output.
- T13: updated Character master -> require downstream review.
- T14: bad export dimensions/alpha -> reject and repair at export stage.
- T15: 40 reviewed assets -> pass full reconciliation.
- T16: unauthorized approval attempt -> block and record.
- T17: GEM A 2.6 / GEM B 2.3 interoperability -> pass contract tests.

Definition of Done: all critical gates are enforced, T01–T17 have recorded evidence, and a pilot produces 40 validated outputs with owner approvals. This document does not assert tests have run.
