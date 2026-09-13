# SET-006 CPDF 1.3 Migration Note

**Status:** Active addendum
**Date:** 2026-09-13

SET-006 now follows CPDF 1.3 and `SET-006-PRODUCTION-SPEC-v1.3.md` for current production decisions.

Key migration decisions:
- Master Sticker Sheets may be approved upstream Visual Master artifacts.
- default logical Frame size is 512x512 px.
- default production Sheet is 5x2 Frames unless the approved package declares another deterministic layout.
- the six-Hero sheet may use a declared equal-cell 3x2 layout for calibration/approval.
- visual masters must have explicit Frame mapping, no cross-frame bleed, Character consistency, communication clarity, and sufficient quality for resize-down.
- the existing Program/Engine performs deterministic splitting, resize/normalization, validation, naming, manifest generation and packaging.
- after technical processing, the individual output files plus validation/manifest become the Technical SSOT.

The older standalone-first language in earlier SET-006 documents is superseded where it conflicts with this addendum and Production Spec v1.3.

Gate state:
- H01 remains owner-approved Golden Reference.
- six-Hero visual direction may be used as calibration reference.
- Gate B still requires a usable Visual Master Package before `READY_FOR_ENGINE`.
- full 40 production remains blocked until the Hero/Gate B criteria are satisfied.

This addendum does not authorize changes to Python, engine, scripts, validators, packagers, or other deterministic software.
