# Shared process and handoff contract
Workflow: brief → GEM A docs → Character candidate → explicit owner Character approval → verified Gate A → GEM B Hero → explicit owner Hero approval → full production → 40/40 visual QA → deterministic engine → owner release.

Source: https://github.com/idev006/MTLineSticker. Repo contains contracts/sticker-handoff/v1 and docs/architecture/process-engineering. Apply actual manifest/versioned schema rather than assuming hard-coded JSON. Use source commit SHA, artifact SHA256, approval receipt, exact asset references, declared frame IDs and sheet mapping. No approval by filename alone.

Decision record: current step; evidence; status PASS/FAIL/BLOCKED/NOT RUN; owner; defect type and originating layer; version impact; recommended next action. Reject stale character approvals and unauthorized transitions. Plugin source documentation is not equivalent to running code or uploading binary assets.

Documentation v0.5 amendment: use DIRECTOR_OUTPUT_STANDARD.md and OUTPUT_REGISTRY.json before declaring any project package complete. Run the bundled document validator; no bypass via short JSON-only delivery. Document completeness does not imply Character/Hero approval, technical image QA or legacy schema compatibility.
