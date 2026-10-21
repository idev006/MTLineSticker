# Plugin Maintenance, Release and Recovery Guide

## Before editing
1. Open [START HERE](START_HERE_FOR_MAINTAINERS.md); read [architecture](UNIFIED_PLUGIN_OVERVIEW.md), [standard](UNIVERSAL_STICKER_STANDARD_SUMMARY.md), [tests](INTEGRATION_TEST_GUIDE.md).
2. Read deployed GEM A and GEM B file lists and actual contents via Plugin Creator's `get_plugin_files`. Do not guess source files from GitHub; the plugin payload is a separately deployed artifact.
3. Record plugin IDs, current release IDs, version numbers, relevant source hashes/changes, and document the intended policy change. Check owner authorization for any breaking global standard.
4. Preserve the original full plugin archive and metadata before editing; never replace unrelated files or delete knowledge files inadvertently.

## Plugin locations and responsibility
**GEM A** plugin ID `plugins_6ad844f4cd8c8191aa0282099b84bb14` v0.4.0 (snapshot). Key source: `skills/start-sticker-project/SKILL.md`, `knowledge/SHARED_HANDOFF_CONTRACT.md`, `knowledge/GEOMETRY_TOLERANCE_V1_2.md`, `knowledge/WHITE_DIECUT_STANDARD_V1_3.md`, plugin manifests.

**GEM B** plugin ID `plugins_6ad84507f928819180ee48d94c5a06be` v0.6.0 (snapshot). Key source: `skills/produce-stickers/SKILL.md`, `knowledge/SHARED_HANDOFF_CONTRACT.md`, `knowledge/UNIVERSAL_SHEET_STANDARD.md`, `knowledge/GEOMETRY_TOLERANCE_V1_2.md`, `knowledge/WHITE_DIECUT_STANDARD_V1_3.md`, `knowledge/TRUE_ALPHA_EXPORT_STANDARD_V1_4.md`, plugin manifests.

## Change procedure
1. Create a decision/change record (why, exact expected behavior, scope, owner approval, acceptance checks, compatibility risk).
2. Edit one canonical standard; explicitly version it. Update the affected GEM A planning/handoff instructions and GEM B rendering/QA instructions **together** for interface changes. Update the shared contract and every duplicated contradictory heading/skill line; historical docs remain annotated as history.
3. Keep the exact Character and per-frame intent locked, unless Product Owner approves modifications.
4. Version plugin manifests consistently (`plugin.json`, `.codex-plugin/plugin.json` if present) and skill headings; increment plugin version.
5. Check source archives and release with Plugin Creator `update_plugin` guarded by `expected_release_id` to prevent overwriting concurrent edits. If release IDs changed, stop and reconcile.
6. Call `get_plugin_files` **after** deployment; verify each new required policy file, full skill references, version, current release ID. Treat update API success alone as insufficient.
7. Record both plugin versions/release IDs, source paths, any GitHub commit, PASS/FAIL/NOT_RUN tests, owner decisions. Keep this START HERE snapshot current.
8. Run [integration checklist](INTEGRATION_TEST_GUIDE.md), including actual saved PNG pixel tests and cutter. No release-readback alone qualifies output as production-ready.

## Rollback and incidents
- Preserve last known-good plugin release/archive. Re-deploy a vetted prior archive only after checking current_release_id and getting required authorization; do not assume `git revert` automatically rolls back a plugin.
- For alpha failure: inspect saved file's image mode and alpha plane; isolate generation, mask extraction, white underlay, composer and image export; reject RGB/checkerboard.
- For subject drift: return to approved runtime Character Sheet, inspect largest standing subject, lock facial anatomy and age; do not use an arbitrary previous generation as new authority.
- For frame-map mismatch: stop B, return specific frame IDs to A; do not handwave mismatched expressive poses as approved.
- For cutter failure: compare actual frame geometry/alpha with cutter parsing and test extracted individual stickers.

## Definition of Done for *maintenance documentation*
A new maintainer can identify exact versions, live locations, policy priority, update operation, QA status and escalation path without chat history. This does NOT prove image-production functionality.
