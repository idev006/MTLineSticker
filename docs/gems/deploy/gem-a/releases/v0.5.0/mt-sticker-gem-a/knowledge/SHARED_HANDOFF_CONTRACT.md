# MT Sticker A/B Shared Handoff Contract v1.2 (universal)

Owner-approved global policy, 2026-10-21; applies to every set, with change via formal owner approval and plugin release.

## Boundaries
GEM A owns requirements, frame identities and communication intents, approved Character/Style authority, references, manifests, exact mapping and Gate A. GEM B reads and validates, creates Hero and approved batch visuals, pixel-accurate sheet masters, actual image QA and cutter handoff. Neither rewrites the other's approved domain. Product Owner exclusively authorizes Character, Hero and final release.

## Universal technical output (mandatory for both)
8 frames/sheet, 4 columns x 2 rows; each frame nominal 592x512px with REQUIRED exact aspect ratio 592/512 (width*512 == height*592). Every rectangular frame has a separate inward approximately 3px pure black opaque border (#000000, alpha255); 15px nominal completely transparent gutter with +/-5% tolerance between outer frame edges; internal sticker safe-zone selectable 15-30px nominal (target 20px), permitted +/-5% relative to selected value, measured from inner edge of border. True RGBA PNG, alpha0 for background and gutters. For full 8-frame sheet with zero outside margin: nominal width=2413, height=1039; recompute actual pixels from frame dimensions and actual accepted gutters. Sheet contains cutter source assets and is not a LINE submission image. Empty or partially filled last sheet requires explicit owner-approved layout policy; do not invent placeholders. No visible sticker content/white die-cut/FX intrudes on safe zone. Do not rely on generative model for exact pixel geometry or guaranteed alpha; deterministic compositor and pixel-level QA required.

## Handoff envelope (JSON or equivalent documented manifest)
contract_version: 1.3.0; set_id; package_revision; git_source_commit; run_id; owner_approval_refs; current_character_reference and source availability; character_locks; reference_index (role/authority); frame_count; frames[] (unique ID, intent, exact caption/no-caption, pose, expressions, props); hero_ids[]; batch_map[]; global_sheet_spec_version='1.2.0'; gates (Gate A, Character, Hero, Full Production); unresolved_blockers[]; provenance and QA evidence with PASS/FAIL/NOT_RUN.
Every 40-frame set must have exactly 40 unique frame IDs and five 8-frame sheets. Cross-check all mappings and never fake a verified approval, hash, uploaded binary or test.

## Handshake
GEM A emits HANDOFF_DRAFT until actual source authority, decisions and references verified. On verified Gate A, set READY_FOR_GEM_B (or documented owner-approved runtime attachment exception limited to Hero). GEM B checks contract version and identity, verifies all required attachments and can return RETURN_TO_GEM_A with precise defect. Hero generated first; wait explicit owner Hero approval; only then full production. Geometry QA, alpha QA, cutter test and visual QA separate. No READY_FOR_ENGINE until validated outputs and evidence; no LINE_SUBMISSION_READY without cutter/export and platform checks.

## Cross-version failures
Halt with CONTRACT_MISMATCH if GEM A hands obsolete 4x10/5x2/5px borders or omitted approved gutter/tolerance policy. Legacy documents are history, not current global defaults. Historical already-produced files are not silently rewritten. Use latest owner decisions and current global contract unless owner formally changes policy.

## Seven expert lenses
R01 process and handoff, R02 architecture/schema, R03 regression/QA, R04 identity, R05 art direction, R06 CI/versioning, R07 LINE release. These are review roles/capabilities, not autonomous staff. Maker/checker evidence and Product Owner authority required.


## Owner approved geometry tolerance amendment 2026-10-21
See GEOMETRY_TOLERANCE_V1_2.md. Latest policy supersedes hardcoded exact frame size/gap claims above when in conflict. All sets universally use 4x2 and independent black rectangular borders. Exact aspect ratio is not subject to tolerance.


## Die-cut contract amendment v1.3.0 — ALL SETS
Mandatory field diecut_standard_version: 1.3.0. Each sticker has an opaque white #FFFFFF alpha=255 underlay extending ~3–5px beyond sticker silhouette, following outer contour, behind artwork; alpha=0 outside final die-cut. Include die-cut in all safe-zone measurements. GEM A specifies/locks, GEM B generates and validates masks; cutter must preserve die-cut while removing black frame. Earlier instructions lacking die-cut are superseded for newly produced output.
