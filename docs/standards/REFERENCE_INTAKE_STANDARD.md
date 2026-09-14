# Reference Intake & Authority Standard — MTLineSticker

**Document ID:** REF-INTAKE-STD-001
**Version:** 1.0
**Status:** Active
**Applies to:** Gem A, Gem B, Character Sheet generation handoff

## Purpose
Reference handling is role-based and authority-aware. Raw attachment count alone is not meaning.

## Intake capacity
For one production intake, support up to 10 current reference images unless the active platform/tool limit is lower.

## Roles
A reference may have one or more evidence-backed roles: `IDENTITY_REFERENCE`, `STYLE_REFERENCE`, `WARDROBE_REFERENCE`, `ACCESSORY_REFERENCE`, `POSE_REFERENCE`, `ENVIRONMENT_REFERENCE`, `OTHER/UNCLASSIFIED`.

## Authority
Record one authority level per reference: `PRIMARY`, `SECONDARY`, `OPTIONAL`, `EXCLUDED`, `UNRESOLVED`. Authority is separate from role.

## Required Reference Index
When references are supplied, the package contains `07_REFERENCES/REFERENCE_INDEX.md` with at least: `Ref ID | Source file | Role(s) | Authority | Intended use | Included downstream? | Notes/open issue`.

## Conflict rule
Do not create `REFERENCE_COUNT_CONFLICT` merely because more images are attached than an informal statement, different role types coexist, style references depict people, or some references are supplemental.
Use `REFERENCE_COUNT_CONFLICT` only when the Product Owner explicitly declared an authoritative count or exact set and the actual/proposed authoritative set materially differs.
For non-material ambiguity classify conservatively and continue; for ambiguity that can change Character identity or production style, request one owner decision.

## Dynamic runtime handoff
Runtime handoff files derive reference lists from the current REFERENCE_INDEX and never hard-code a numeric reference count. A STYLE_REFERENCE does not become identity evidence merely because it contains a person; an IDENTITY_REFERENCE does not automatically control rendering style; wardrobe/accessory/pose/environment references control only their declared scope.

## Decision closure
After an owner reference decision: update REFERENCE_INDEX, affected Character/Style docs, package/open-item/handoff manifests, regenerate runtime handoff/prompt, recalculate readiness, and continue to the next safe stage. The owner should not manually edit the package.
