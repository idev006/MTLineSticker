# Handoff Status Addendum

**Version:** 1.1  
**Status:** Active

Canonical cross-stage states are:
- Gem A → Gem B: `READY_FOR_GEM_B`
- Gem B Hero → Product Owner: `READY_FOR_VISUAL_OWNER_REVIEW`
- Product Owner Hero approval → Gem B full production: `FULL_PRODUCTION_UNLOCKED`
- Gem B → Program/Engine: `READY_FOR_ENGINE`
- Program/Engine → Final Human QA: `READY_FOR_FINAL_QA`
- Final Human QA → submission: `LINE_SUBMISSION_READY`

Gem A internal non-ready states include `DRAFT`, `INTERNAL_QA`, `OWNER_DECISION_REQUIRED`, `SSOT_CONFLICT`, and `BLOCKED`.

If required Character Sheet creation/approval is pending, Gem A remains non-ready and must not emit `READY_FOR_GEM_B`.

The phrase `READY_FOR_HANDOFF` is generic architectural wording only and must not replace a destination-specific state.