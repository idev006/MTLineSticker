# MTLineSticker Process Engineering Blueprint v1.0

**Date:** 2026-10-21  
**Status:** DESIGN_BASELINE — not yet implemented or acceptance-tested  
**Applies to:** Gem A (repo deploy v2.6), Gem B (repo deploy v2.3), visual-generation runtime, owner approval, QA Engine, release.  
**Source:** docs/workflow/LINE_STICKER_END_TO_END_PIPELINE.md; docs/workflow/PRODUCTION_RUNBOOK_AND_GATES.md; docs/gems/GEM_OPERATIONAL_PLAYBOOK.md; docs/gems/deploy/gem-a/INSTRUCTION.txt; docs/gems/deploy/gem-b/INSTRUCTION.txt.

This blueprint is additive and does not overwrite existing Gem instructions, engine, scripts, validators or set assets. Before plugin implementation, reconcile this blueprint with deployment definitions and approve contract schema.

## Navigation
1. [01_PROCESS_BLUEPRINT.md](01_PROCESS_BLUEPRINT.md): SIPOC, AS-IS, TO-BE, stage gates and RACI.
2. [02_INTEGRATION_CONTRACT.md](02_INTEGRATION_CONTRACT.md): SSOT, schemas, invariants, states, versioning, rollback.
3. [03_FMEA_AND_TEST_PLAN.md](03_FMEA_AND_TEST_PLAN.md): risks, failure modes, QA and acceptance tests.
4. [04_IMPLEMENTATION_PLAN.md](04_IMPLEMENTATION_PLAN.md): plugin split, phases, ownership, controlled rollout.

## Evidence-backed discoveries
- The repository already specifies 10 stages from brief through LINE submission and explicit Character + Hero owner approvals.
- Repo deployment instruction GEM A is **2.6** and GEM B **2.3** (historical plugin skill loaded elsewhere stated GEM A 2.5; therefore deploy source version needs explicit reconciliation before packaging).
- Generic 40-frame default in existing GEM B is **4 sheets × 10**, but active CHAICHAT #1 set mapping calls for **5 sheets × 8**. **Set-specific approved frame-to-sheet mapping must override generic defaults**, after schema and owner decision review.
- Latest character for CHAICHAT #1 is adult male from recent couple photo (white backward cap, navy outerwear). Assets/Character Sheet binaries are not committed to GitHub; **do not claim ready-for-GEM-B** until provenance and file availability are verified.
- Owner approval for Character concept does not automatically mean repository has validated CHARACTER_SHEET_ACTIVE asset/approval receipt; distinguish concept approval from artifact activation.

## Governance decision
This is a process proposal, not authorization to publish two plugins. No plugin has been created by this documentation update. Private plugin installation/deployment follows separate release gate.
