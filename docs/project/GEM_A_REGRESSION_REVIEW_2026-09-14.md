# Gem A Regression Review — 2026-09-14

## Scope
Docs-only review of Gem A package behavior. No Python, engine, scripts, validators, packagers, desktop application or deterministic production logic changed.

## Evidence reviewed
Two runtime packages were compared:
- `Disciplined_Househusband_Package(2).zip` — defective package exhibiting the reported failure modes.
- `phorban_sai_winai_GemA_v1.0(3).zip` — newer Gem A output showing substantial improvement after PR #12.

Repository baseline before this review: `main` at `6133be1e5008b05ac2366db979bbe1d312bb6610`.

## Confirmed defects in the defective package
1. Unsupported invention
   - Character Bible introduced `mid-40s`.
   - Character Sheet generation prompt introduced `Thai man in his 40s`.
   - Neither age nor nationality/ethnicity was established by the owner input for this pilot.

2. Context contamination
   - Character Sheet negative constraints introduced `NO savanna watercolor style (strictly forbidden across all design projects)` despite no current-task basis.

3. False matrix completeness
   - `FRAME_COMMUNICATION_MATRIX.md` asserted all 40 frames were mapped but only supplied concrete detail for F01 and F40.

4. Non-explicit frame mapping
   - `FRAME_TO_SHEET_MAPPING.md` used range summaries such as `Sheet 1: F01-F10` rather than one concrete Frame -> Sheet -> Row -> Column mapping for every Frame.

5. Thin Character Sheet specification
   - The specification listed only front, 3/4 and side views plus a generic purpose statement, insufficient for robust visual SSOT approval.

## Evidence from the newer package
The newer package demonstrates that PR #12 materially improved behavior:
- exact age and ethnicity are explicitly UNSPECIFIED,
- unrelated `savanna watercolor` contamination is absent,
- CAPTION_MASTER contains F01-F40,
- FRAME_COMMUNICATION_MATRIX contains 40 concrete entries,
- FRAME_TO_SHEET_MAPPING contains explicit positions for all 40 frames,
- Character Sheet Specification includes turnaround, face detail, body, wardrobe, accessory, expression and action coverage,
- handoff state remains `OWNER_DECISION_REQUIRED` because `CHARACTER_SHEET_ACTIVE` is missing.

## Root cause
The remaining architectural weakness was not user-prompt complexity. The contract said what complete output should look like, but it did not make four failure modes sufficiently non-negotiable at execution time:

1. Source scope was implicit.
   The model was told not to invent or add unrelated constraints, but there was no explicit current-task context firewall requiring provenance for set-specific facts. This allowed stale conversational examples or old-set constraints to leak into a new package.

2. Completeness was descriptive rather than saturating.
   The contract required all frames, but did not define `N/N concrete entries` as the proof of completeness. A prose claim such as `all 40 mapped` could therefore masquerade as completion.

3. Reconciliation counts were not explicitly evidence-derived.
   A package could state `40/40 PASS` independently of whether 40 populated entries actually existed.

4. Character Sheet sufficiency lacked an explicit floor.
   Required dimensions were named generally, but there was no hard minimum that made a short three-view specification invalid.

## Correction implemented
Gem A v2.2 hardening adds:
- `CURRENT-TASK SOURCE BOUNDARY` / context firewall,
- provenance classes `CURRENT_USER`, `CURRENT_ATTACHMENT`, `ACTIVE_SSOT`, `FIXED_GOVERNANCE`,
- explicit `CARDINALITY / SATURATION` rules,
- mandatory N/N concrete entries for frame-owned artifacts,
- evidence-derived reconciliation counts,
- explicit rejection of example-only/range-only false completeness,
- a minimum Character Sheet Specification coverage floor,
- stronger pre-package audit language that a self-declared PASS is not evidence.

## Regression acceptance criteria
A concise pilot prompt must produce a package where:
- unsupported age/ethnicity/nationality is absent or UNSPECIFIED,
- unrelated prior-context constraints are absent,
- CAPTION_MASTER = 40 concrete entries,
- FRAME_COMMUNICATION_MATRIX = 40 concrete populated entries,
- FRAME_TO_SHEET_MAPPING = 40 explicit mappings,
- all three artifacts reconcile by actual IDs with no missing/duplicate Frame,
- Character Sheet Specification is sufficient for visual SSOT approval,
- optional traits remain optional,
- no placeholder or cross-file deflection substitutes for owned content,
- pre-Character-Sheet handoff remains `OWNER_DECISION_REQUIRED`,
- `READY_FOR_GEM_B` appears only after Character Sheet approval and Gate A PASS.

## Review result
Architecture correction is docs-only and preserves the simple user-prompt principle. Software boundaries remain unchanged.