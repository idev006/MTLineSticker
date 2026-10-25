# A1 Offline Validation Runbook — GitHub Actions Optional

## Authority
- GitHub is the Single Source of Truth for documents, source code, manifest and signed-off text reports.
- The Product Owner sends approved Character Sheet and bag photos to GEM B directly; no image is required in GitHub or in Gate A1.
- GEM A owns complete document QA. GEM B independently verifies A1 receipt and handles owner-supplied image Gate A2.
- Real A1 PASS requires Official Validator exit=0, a1_ready=true, errors=[], exact committed SHA256 manifest and immutable validated source commit. Smoke tests are insufficient.

## Offline path (any Python-equipped checkout; never relies on GitHub Actions)
```bash
git clone https://github.com/idev006/MTLineSticker.git
cd MTLineSticker
python tools/gem_a/validate_without_actions.py --repo . --write-manifest
git add sets/SET-KHE-NOI-FIRST-HOME-001/PACKAGE_MANIFEST.json
git commit -m 'qa(khe-home): synchronize SHA256 manifest'
python tools/gem_a/validate_without_actions.py --repo .
```
The first step does not certify A1 and is intentionally separated from the validation step to guarantee a GitHub-source SHA for the committed manifest. After a real PASS, publish the generated receipt:
```bash
git add gate-reports/SET-KHE-NOI-FIRST-HOME-001/A1_LATEST.json
git commit -m 'qa(khe-home): publish offline official A1 validation receipt'
git push origin main
```
If validation fails, inspect each `errors[].code`, fix and rerun without marking PASS.
The locally created receipt always identifies `execution_mode=OFFLINE_LOCAL_PYTHON_NO_ACTIONS`. GitHub Actions is a second optional verification channel, not a prerequisite.

## GEM B entry requirements
Read receipt from GitHub then compare `validated_source_commit` with document snapshot. Require PASS, validator_executed true, validator_exit_code 0, sha256_verified true. On project A1 FAIL, return precise document defects to GEM A, not the owner. At A2 request user runtime image attachments.

## Current state
Standalone runner committed, independently retrieved from GitHub. At publication of this runbook, there is **no observed successful official Python execution on the complete repository package** from this chat runtime; the mounted workspace has no direct GitHub network checkout and the connected GitHub tool provides file APIs, not a remote Python runner. Thus do not promote A1 to PASS on the basis of this runbook alone.
