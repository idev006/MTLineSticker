# GEM A / GEM B — Test execution receipt 2026-10-25

## Versions
- GEM A: 0.14.0
- GEM B: 0.13.0

## Local executable script tests (performed this turn in Python container)
- `python /mnt/data/sticker_upgrade/a/scripts/test_director_validator.py`: PASS 3/3
  - owner runtime EXTERNAL reference accepted at A1
  - tampered SHA rejected
  - missing document rejected
- `python /mnt/data/sticker_upgrade/b/scripts/test_handoff_contract.py`: PASS 4/4
  - valid A1 fixture receipt accepted
  - wrong commit rejected
  - FAIL receipt rejected
  - modified document rejected
- `python /mnt/data/sticker_upgrade/b/scripts/test_image_qa.py`: PASS 3/3
  - valid RGBA geometry accepted
  - non-RGBA rejected
  - wrong ratio rejected

These tests use synthetic fixtures. The latest published plugin code inventory and version were separately retrieved by Plugin Creator; the executable local copies are not evidence of a full published-plugin invocation with real owner assets.

## Real project JSON cross-check via GitHub connector
Checked HEAD `d945e850ff2a03af8f296300404123a470058e69`.
- frames.json: 40/40 records, 40 unique IDs and captions, all owner-locked
- exactly 5 sheet ids and 40 unique occupied sheet cells
- Hero F01, F09, F17, F29
- Manifest: 37 entries matching stated count (content SHA256 recomputation for all 37 files NOT performed during this check)
- approvals.json records approved character and owner-to-GEM-B image delivery
- handoff.json is still HANDOFF_DRAFT
- canonical A1_LATEST.json: FAIL, validator_executed=false

## Decision
Plugin regression smoke suite PASS (10/10). A/B end-to-end acceptance NOT PASSED. Canonical project A1 BLOCKED (official real-package validator not executed). GEM B image Gate A2 NOT TESTED (owner provides approved Character Sheet and bag at runtime). No actual sticker frames verified or generated as part of this test. No production authorization.
