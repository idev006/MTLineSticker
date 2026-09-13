# Character Product Development Framework (CPDF)

**Version:** 1.4  
**Status:** Active project framework  
**Purpose:** Govern end-to-end development of character-based LINE sticker products from concept to submission-ready individual files.

## 1. North Star and core principle
The governing outcome is defined in `docs/project/PROJECT_NORTH_STAR_AND_SUCCESS_CRITERIA.md`.

A LINE sticker is a communication product. The system exists to produce sticker products that match the user's approved intent, communicate effectively in real chat, preserve Character/Style quality, satisfy current LINE Creators Market requirements at submission time, and are commercially ready to sell.

Quality combines communication clarity, user usefulness, Character consistency, small-size readability, master quality, platform compliance, visual distinctiveness, commercial relevance, and controlled handoff quality.

Process artifacts, Gems, Gates and reports are means to that outcome, not ends in themselves.

## 2. End-to-end flow
`IDEA → PRODUCT BRIEF → CHARACTER/STYLE SSOT → CAPTION/USE-CASE ARCHITECTURE → HERO PLAN → HERO GATE → FRAME BRIEFS → MASTER FRAMES/SHEETS → VISUAL GATE → PROGRAM/ENGINE → INDIVIDUAL TECHNICAL FILES → FINAL HUMAN QA → LINE SUBMISSION READY`

A downstream stage must not begin while a blocking upstream Gate is unresolved.

## 3. Specialist architecture
- **Gem A — Sticker Product Architect:** owns concept, product meaning, caption/use-case architecture, Character/Style requirements, Hero plan, Frame briefs, Sheet plan, QA criteria, and the Production Document Package.
- **Gem B — Sticker Visual Producer:** owns high-resolution visual Master Frame / Master Sticker Sheet production from locked documents.
- **Program / Engine:** owns deterministic splitting, approved alpha/background processing, resize/normalize, naming, technical validation, manifest, export and packaging.
- **Product Owner / Human QA:** owns material decisions and final acceptance.

No specialist may silently take over another specialist's responsibility.

## 4. Blackbox rule
Every specialist component is a controlled Blackbox with:
1. Input Contract
2. Definition of Ready
3. Responsibility / authority boundary
4. Internal quality controls
5. Exit Gate / Definition of Done
6. Output Contract
7. Defect return path

Internal methods may evolve, but contracts and ownership boundaries must remain explicit.

## 5. Quality at Source
Each stage completes and verifies its own work before handoff. Downstream stages are not repair stations for upstream defects.

Examples: weak caption → Gem A; Character drift/clutter → Gem B; invalid split/dimensions/package → Program/Engine.

## 6. Canonical handoff states
Use destination-specific states:
- Gem A → Gem B: `READY_FOR_GEM_B`
- Gem B Hero review → Product Owner: `READY_FOR_VISUAL_OWNER_REVIEW`
- Hero approval → Gem B full production: `FULL_PRODUCTION_UNLOCKED`
- Gem B → Program/Engine: `READY_FOR_ENGINE`
- Program/Engine → Final Human QA: `READY_FOR_FINAL_QA`
- Final Human QA → submission: `LINE_SUBMISSION_READY`

`READY_FOR_HANDOFF` is a generic concept only.

## 7. Communication-first Frame design
Every Frame requires: exact caption, sender intent, likely chat situation, tone, expression, gesture/action, minimum useful props, camera/composition guidance when material, forbidden drift, and Character reference.

**One Frame = one primary communication intent.**

## 8. 1-second test
At chat-preview scale, the primary intent should be understandable quickly from expression, action, caption and key prop. Scene density, tiny characters, weak hierarchy or unclear use case = FAIL.

## 9. Character governance
Approved Character Sheets are mandatory active references. Locked identity traits must be preserved. A Golden Reference may calibrate later production but never replaces the Character Sheet.

## 10. Hero Gate
Full-set production is blocked until representative Hero Frames pass when Hero gating is required. Hero output exists to let the user/Product Owner confirm the visual direction before scale-up. If an anchor Hero fails, correct it before expanding the affected batch.

## 11. Frame / Master Sticker Sheet model
**Frame** = one sticker production unit.  
**Master Sticker Sheet** = one high-resolution image containing multiple equal-size Frames in a deterministic Grid.

Default working profile unless set SSOT overrides it:
- Frame: **512 × 512 px**
- Grid: **5 columns × 2 rows**
- 10 Frames per Sheet
- logical Sheet size: **2560 × 1024 px**

The master is intentionally larger than final LINE output for high-quality resize-down. Cells must be equal, ordered, documented, independently readable, and free of cross-frame bleed.

## 12. Stage-specific SSOT
The project has different authoritative artifacts by lifecycle stage:
- **Planning SSOT:** active Framework + set Product/Production documents.
- **Visual SSOT:** approved Master Frame / Master Sticker Sheet package plus mapping and Visual QA evidence.
- **Technical SSOT:** Program/Engine-produced individual submission files plus manifest/validation evidence.

A later-stage SSOT does not authorize changes to locked upstream meaning or Character identity.

## 13. Responsibility boundary
AI/Designer owns meaning, Character fidelity, composition, communication clarity and master visual quality. Program/Engine owns deterministic technical preparation. Technical PASS never substitutes for Visual QA PASS.

## 14. Gate model
1. Gate A — Product / Documentation Readiness
2. Hero Gate — Visual Direction Approval when required
3. Gate B — Visual / Master Asset Readiness
4. Gate C — Technical Submission Readiness
5. Gate D — Final Human Acceptance

See `docs/project/QUALITY_GATE_STANDARD.md`, `docs/project/HERO_TO_FULL_PRODUCTION_GATE.md`, and `docs/project/HANDOFF_STATUS_ADDENDUM.md`.

## 15. Typography
AI-rendered Thai text is candidate-level until verified exactly. Final wording must be proofread 100%. Deterministic typography may be used when exact text cannot be guaranteed by generation.

## 16. Authority / SSOT precedence
When instructions conflict, use this order:
1. current official platform requirements,
2. latest explicit Product Owner decision that does not conflict with platform requirements,
3. active CPDF / global standards,
4. Character / Style SSOT,
5. Product / Set SSOT,
6. approved handoff package,
7. compiled Gem knowledge pack,
8. current execution notes/task.

A lower layer may specialize a higher layer but must not contradict it.

## 17. Corrective learning
When a Gate failure exposes a systemic weakness: reject the artifact, record root cause, fix the owning stage, update the Framework/standard when needed, update set documents, then re-enter at the correct Gate.

## 18. Traceability
Every final sticker should trace backward through:
`final individual file → manifest/validation → Master Frame or Sheet cell → Frame ID → Frame brief → caption/use case → Product Brief → Character/Style SSOT`.

## 19. Gem deployment architecture
Gem Instructions are orchestrators, not full knowledge stores. Stable specialist rules are compiled from repository SSOT into Knowledge Packs. Runtime project context is attached separately within the platform attachment budget.

Repository SSOT remains authoritative over compiled Knowledge Packs.

## 20. North-Star test for process changes
Before adding a new mandatory document, rule, Gem behavior or production step, ask whether it measurably improves the chance that the user receives the sticker product they actually want, that the stickers communicate well, and that the final package can be submitted and sold on LINE.

If not, simplify it, remove it, or keep it optional.

## 21. Software boundary
Framework, Gem, Knowledge Pack and documentation work must not modify the existing Python application, `engine/`, `scripts/`, validators, packagers or deterministic processing logic unless the Product Owner explicitly opens a separate software-development task.

## 22. Related standards
- `docs/project/PROJECT_NORTH_STAR_AND_SUCCESS_CRITERIA.md`
- `docs/project/MULTI_AGENT_STICKER_PRODUCTION_ARCHITECTURE.md`
- `docs/project/HANDOFF_CONTRACT_STANDARD.md`
- `docs/project/HANDOFF_STATUS_ADDENDUM.md`
- `docs/project/QUALITY_GATE_STANDARD.md`
- `docs/project/HERO_TO_FULL_PRODUCTION_GATE.md`
- `docs/project/GEM_B_OUTPUT_CONTRACT.md`
- `docs/project/GEM_INSTRUCTION_ARCHITECTURE.md`
- `docs/gems/GEM_KNOWLEDGE_PACKAGING_STANDARD.md`
- `docs/standards/STICKER_COMMUNICATION_STANDARD.md`
- `docs/standards/MASTER_SHEET_FRAME_STANDARD.md`
- `docs/standards/LINE_STICKER_SPEC.md`
- `docs/standards/QA_STANDARD.md`
- `docs/standards/VISUAL_STYLE_GUIDE.md`
