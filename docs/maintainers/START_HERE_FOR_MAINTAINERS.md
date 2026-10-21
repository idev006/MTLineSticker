# START HERE — MT Sticker GEM A / GEM B
> Last validated 2026-10-21. **Canonical maintainer entry point.** For humans and successor AIs. This document is not proof that production image QA has passed.

## 60-second overview
GitHub repository: https://github.com/idev006/MTLineSticker (documents/decisions/SSOT).
**GEM A** plans and locks character references, frame IDs, exact communicative intent, sheet map, approvals, and package handoff.
**GEM B** consumes a valid handoff, renders candidate assets, creates real RGBA sheets with white shaped die-cut and precise geometry using deterministic compositing, performs pixel-level QA, and hands verified images to a cutter.
**Product Owner alone** approves identity, Hero and release. GEM A cannot certify B's image pixels; GEM B cannot silently rewrite approved frame intent.

## Live release snapshot
- GEM A v0.4.0: https://chatgpt.com/plugins/plugins_6ad844f4cd8c8191aa0282099b84bb14
- GEM B v0.6.0: https://chatgpt.com/plugins/plugins_6ad84507f928819180ee48d94c5a06be
- Shared handoff envelope contract_version **1.3.0**; geometry policy **v1.2.0**; white die-cut policy **v1.3.0**; true alpha export policy **v1.4.0** (GEM B).
- These are plugin **instruction releases**, NOT evidence that deterministic masking/cutter integration is implemented, tested, or production-ready.

## Read next, in order
1. [System architecture](UNIFIED_PLUGIN_OVERVIEW.md) — roles, interfaces, gates, authority.
2. [Current sticker specifications](UNIVERSAL_STICKER_STANDARD_SUMMARY.md) — practical acceptance rules.
3. [Maintenance guide](PLUGIN_MAINTENANCE_GUIDE.md) — how to change, release, test, roll back.
4. [Integration test guide](INTEGRATION_TEST_GUIDE.md) — PASS/FAIL/NOT_RUN requirements.
5. [Decision and change log](DECISION_AND_CHANGE_LOG.md) — supersession/version history.
Then inspect real plugin source with Plugin Creator; the docs summarize, not substitute for the deployed code/instructions.

## Current project
CHAICHAT #1: [set README](../../sets/SET-CHAICHAT-001/README.md), [40-frame map](../../sets/SET-CHAICHAT-001/STICKER_MASTER_40.md), [Character Bible](../../sets/SET-CHAICHAT-001/CHARACTER_BIBLE.md). Runtime character image authority is a specific user-supplied reference, not an arbitrary GitHub image. Never infer approved likeness from a public photo or hallucinate missing binary assets.

## Unresolved
No passing image-binary transparent-alpha / die-cut / cutter integration evidence for newly generated CHAICHAT sheets is yet documented. Do not relabel visual previews as sticker master files.
