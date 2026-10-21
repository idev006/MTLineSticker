# Unified GEM A/B Plugin Architecture

## Workflow
```text
Product Owner + approved references
   -> GEM A (character bible, 40-frame intentions, approvals, 5x8 mapping)
   -> shared handoff contract v1.3.0 + asset references and gate evidence
   -> GEM B (preflight / owner Hero gate / frame artwork generation)
   -> deterministic alpha segmentation + white die-cut + 4x2 composer
   -> saved-file RGBA pixel QA + visual QA
   -> downstream cutter integration test
   -> eight independent stickers per sheet / eventual LINE export review
```

## Ownership and non-overlap
| Component | Owns | Must not invent |
|---|---|---|
| Product Owner | Character/Hero/final approvals, business decisions | — |
| GEM A | intent/mapping, style lock, character reference authority, contract and stage-gate proof | technical pass without binary inspection |
| GEM B | image generation, deterministic composer, PNG alpha/die-cut/geometry validation, cutter evidence | unapproved captions, changed frame ID/meaning, approvals |
| Cutter | cropping/export of each artwork and preservation of shaped white die-cut | content not supplied by A/B |
| GitHub | documentation, versioned standards and evidence | automatically available runtime image files |

For seven expert review **roles** see [team charter](../architecture/process-engineering/team/TEAM_CHARTER.md). These are review lenses, not independently active workers.

## Interface version rules
The handoff envelope must declare `contract_version: 1.3.0`, set ID, package revision, source commit, run ID, approval references, authoritative runtime character image availability, frame IDs and complete descriptions, exact sheet mapping, gate states, unresolved blockers, evidence. Additionally require `diecut_standard_version: 1.3.0`. A historical title may say v1.2 while the active envelope states v1.3; trust the current explicit contract fields and record conflicts for correction, never silently downgrade.

Each of 40 unique frame IDs occurs once in five 4x2 sheets. If references/approvals unavailable mark BLOCKED or RETURN_TO_GEM_A; a history of conversation is not proof of a runtime binary asset.

## Stage gates
Gate A: source and contract verified -> Hero generation only when authorized -> owner Hero approval -> full batch rendering -> visual + pixel QA -> cutter test -> owner final decision. Use PASS / FAIL / NOT_RUN / BLOCKED distinctly. The absence of evidence is never PASS.

## Exact canonical references
- [Current summary](UNIVERSAL_STICKER_STANDARD_SUMMARY.md)
- [White die-cut deployment record](../standards/UNIVERSAL_WHITE_DIECUT_RELEASE_2026-10-21.md)
- [True Alpha GEM B record](../standards/GEM_B_TRUE_ALPHA_RELEASE_2026-10-21.md)
- Live deployed plugin source via Plugin Creator is authoritative for its actual implementation.
