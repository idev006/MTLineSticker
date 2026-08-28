# Process Control Plan v1

## Purpose
Define process-engineering controls for the four-stage sticker production line.

| Stage | Input | Output | Mandatory Gate |
|---|---|---|---|
| S1 Frame Extraction | Contact sheet image(s) | Raw frame masters | Frame integrity |
| S2 Background Removal | Raw frame folder | Transparent masters | Visual/alpha quality |
| S3 LINE Normalization | Transparent master folder | LINE-ready PNGs | LINE technical preflight |
| S4 Submission | LINE-ready folder | Submission package | Count/package/final QA |

## Core rules
1. Source artifacts are immutable.
2. Each stage writes transactionally to a new destination.
3. Stage manifests are required.
4. Jobs may be retried from the failed stage without rerunning prior successful stages.
5. Worker count is configurable; results must remain deterministic.
6. A warning/review-required state cannot be promoted to PASS without explicit QA approval.
7. UI progress is derived from real stage events, never a timer animation.

## States
DISCOVERED -> VALIDATING -> READY -> PROCESSING -> QA_PENDING -> PASSED -> COMPLETED

Exception states: WARNING, REVIEW_REQUIRED, FAILED, CANCELLED, RECOVERY_REQUIRED.

## Folder contracts
- S1 never removes backgrounds or resizes frames.
- S2 never changes pixel dimensions except optional lossless trimming only when explicitly enabled; default is dimension-preserving transparent output.
- S3 is the only stage that performs LINE canvas resizing/fitting.
- S4 does not alter sticker artwork.

## Control metrics
- input/output counts
- corruption/unsupported rate
- duplicate rate
- stage duration
- worker utilization
- foreground preservation score
- edge contamination score
- technical validation failure count
- retry count

## Traceability
Every output manifest must include source file, SHA-256, module version, configuration snapshot, output file SHA-256, status and warnings.
