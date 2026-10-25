# GEM A / GEM B Gate Contract v2.1 — Approved workflow stabilization

Date: 2026-10-25
GEM A 0.15.0 release: pluginrel_6add91383ba48191a74c0e1397cbc5d6
GEM B 0.14.0 release: pluginrel_6add9145150c8191b0a316198bd4ff1c

## Root cause fixed
Previous GEM A v0.14.0 instructions required the Python validator while project A1 receipt recorded real GitHub connector-native SHA256/documentary inspection. GEM B v0.13.0 only described an "official" gate and lacked explicit connector-method evidence semantics. The plugins could disagree despite documentary evidence. v2.1 standardizes documented proof of either method.

## Supported validator execution methods
- OFFICIAL_PYTHON_VALIDATOR / OFFLINE_LOCAL_PYTHON_NO_ACTIONS: run actual official Python validator against pinned source; preserve exit and errors.
- CONNECTED_GITHUB_DOC_READBACK_AND_JS_SHA256: fetch pinned project files; independently compute SHA256 for every manifest target; verify full inventory, 26/26 registry records, 40/40 literal owner-locked captions and 40/40 mappings, approvals; log exact validated commit, full test coverage and any errors. Record `official_python_validator_executed=false`. Python and GitHub Actions are NOT prerequisites.

## Machine-readable receipt and consumer verification
Use canonical `gate-reports/SET-KHE-NOI-FIRST-HOME-001/A1_LATEST.json`. Require `status=PASS`, `validator_executed=true`, `validator_exit_code=0` (gate-check result for connector method), `manifest_sha256_verified=true`, `validated_source_commit`, `errors=[]`, `validation_method`, and `check_summary`. The connector-mode receipt is accepted only with exact `PASS_37_OF_37`, `PASS_26_OF_26`, and two `PASS_40_OF_40` claims. GEM B independently rehashes pinned package rather than trusting the claims, and rejects missing evidence or manipulated inputs. B's executable checker added negative regression tests for missing coverage and document tampering.

**Scope:** Gate A1 authorizes only B Gate A2 intake; no Hero rendering until owner-provided runtime images are examined and applicable Product Owner Hero authorization is obtained. Character Sheet and black hard briefcase images are sent by Owner directly to GEM B, NOT GitHub; do not request reapproval or ZIP. Maintain approved Caption Master v0.4.0 and no duplicate gags.

## Observed test results
- GEM A real-project connector-native documentary checks published previously: SHA256 37/37, registry 26/26, captions 40/40, sheet mapping 40/40 (validated source commit `086b8589f156306e30d3d6becaebc2faedc1093e`).
- GEM A official Python synthetic tests 3/3 passed.
- GEM B baseline receipt tests 4/4 passed.
- GEM B connector acceptance + missing coverage rejection + tampered manifest payload rejection: 3/3 passed.
- GEM B PNG smoke tests 3/3 passed.
- Total fixture/contract checks 13/13. No actual owner image pixels validated, no artwork generated, and no complete 40-sticker production test claimed.

## Future rule
Do not change A1 acceptance policy in one plugin only. Both GEM A and GEM B must share identical gate method definitions and negative tests; never block A1 solely because GitHub Actions was not run.
