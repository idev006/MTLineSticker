# Responsibility and Approval Matrix v1.0

Legend: A=accountable, R=responsible, C=consulted, I=informed. AI roles produce and review proposals; only human Product Owner gives owner approvals.

| Activity | PO | Lead | Process | Systems | QA | Character | Art | DevOps | LINE |
|---|---|---|---|---|---|---|---|---|---|---|
| Approve product brief | A | R | C | I | I | C | C | I | I |
| Design stage gates | A | C | R | C | C | I | I | I | I |
| Handoff contract | I | A | C | R | C | I | I | C | I |
| Automated validator/tests | I | A | C | C | R | I | I | C | I |
| Character sheet quality assessment | A | C | I | I | C | R | C | I | I |
| Character asset activation | A/R | C | I | I | C | C | C | I | I |
| Hero creation review | A | C | I | I | C | C | R | I | I |
| Hero approval | A/R | C | I | I | C | C | C | I | I |
| Batch release and QA | I | A | C | C | R | R | R | C | I |
| CI and reproducibility | I | A | I | C | C | I | I | R | I |
| LINE package requirements | I | A | I | I | C | I | C | C | R |
| Final submission approval | A/R | C | I | I | C | I | C | C | C |

## Stage gate checklist
G0 Brief: PO supplied sufficient requirements and role-authorized references.
G1 Documentation: 40/40 unique frames across matrix, caption metadata, mapping; maker-checker signoff.
G2 Character candidate: visual completeness and adherence to current identity reference.
G3 Character active: exact visual artifact approved explicitly by PO.
G4 GEM B ready: contract schema, assets/hashes, active Character and no blockers.
G5 Hero review: QA/Character/Art assessments attached.
G6 Full production unlock: exact Hero candidate set approved by PO.
G7 Batches: every frame inspected; no missing/duplicated frame.
G8 Export: machine validation plus platform-specific export checks.
G9 Release: final owner approval and submission evidence.

## Escalation
- Source/contract ambiguity -> Systems Architect + Product Owner.
- Frame IDs/mapping mismatch -> GEM A + QA.
- Character drift -> Character Specialist + Art Director; systemic issues return to Character approval.
- CI/test failures -> QA + DevOps.
- Platform specification conflict -> LINE Specialist; submission paused.
