# GEM-A Release Notes

## Version 2.6
Dynamic Reference Intake release.

Changes:
- supports up to 10 current reference images per intake unless the active platform/tool limit is lower,
- introduces role-based `07_REFERENCES/REFERENCE_INDEX.md`,
- separates reference role from authority,
- prevents false `REFERENCE_COUNT_CONFLICT` caused by mixed identity/style/wardrobe/accessory/pose references,
- makes Character Sheet runtime handoff/prompt enumerate resolved reference roles dynamically,
- closes owner reference decisions back into the package automatically,
- adds Reference Intake & Authority Standard and Reference Index template,
- preserves v2.5 executable Character Sheet handoff, global lock normalization, commercial analysis and approval gates.

## Version 2.5
Added executable Character Sheet handoff, decision closure, global Character-lock IDs, and explicit manifest accounting.
