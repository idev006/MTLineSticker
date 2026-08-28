# Modular Processing Architecture v1

Status: IMPLEMENTATION BASELINE

## Goal
Separate the sticker production flow into independent, testable stages while keeping the desktop UI and processing engine decoupled and coordinated through stable in-process contracts.

## Stage model
1. Frame Extraction: contact sheets -> raw frame masters. No resize, no background removal, no alpha manipulation.
2. Background Removal: raw frame folder -> transparent master folder. No LINE resize.
3. LINE Normalization: transparent masters -> LINE-ready 370x320 canvas assets with preserved aspect ratio and safe margin.
4. Submission: validate allowed count, dimensions, alpha, file size, Main/Tab assets and build final package.

## Architectural boundaries
- UI owns interaction, presentation and user settings only.
- Engine owns image processing, validation, manifests, state transitions and file transactions.
- Each stage has an explicit input/output contract.
- A stage never overwrites artifacts produced by a previous stage.
- All stage outputs are reproducible from their inputs plus versioned settings.
- Background-removal implementation is a provider/plugin contract so classical, AI and hybrid providers can be swapped.

## Canonical workspace
```
workspace/
  01_raw_frames/
  02_transparent_master/
  03_line_ready/
  04_submission/
  manifests/
  logs/
```

## Engine packages
```
line_sticker_pipeline/
  contracts.py
  modules/
    frame_extractor.py
    background_remover.py
    line_normalizer.py
    submission.py
  orchestrator.py
```

Existing legacy-compatible Engine/Pipeline APIs remain temporarily available while callers migrate.

## Quality gates
- Gate 1 Frame integrity: expected frames detected, crop readable, source dimensions preserved.
- Gate 2 Background quality: transparent background, foreground preservation, edge quality, visual QA.
- Gate 3 LINE readiness: dimensions, aspect fit, safe margin, alpha, file size.
- Gate 4 Submission: allowed sticker count, package completeness and final report.

## Process-engineering controls
Every stage records status, input hashes, output hashes, settings version, warnings, failures and timestamps. Failed or review-required artifacts do not silently advance to the next stage.
