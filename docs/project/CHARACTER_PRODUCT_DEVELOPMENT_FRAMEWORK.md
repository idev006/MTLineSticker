# Character Product Development Framework (CPDF)

**Version:** 1.2  
**Status:** Active project framework  
**Purpose:** Govern end-to-end development of character-based LINE sticker products from concept to submission-ready individual files.

## 1. Core principle
A LINE sticker is a communication product. Quality combines communication clarity, user usefulness, character consistency, small-size readability, master quality, platform compliance, visual distinctiveness, commercial relevance, and controlled handoff quality.

## 2. End-to-end flow
`IDEA → PRODUCT BRIEF → CHARACTER/STYLE SSOT → CAPTION/USE-CASE ARCHITECTURE → HERO PLAN → HERO GATE → FRAME BRIEFS → MASTER FRAMES/SHEETS → VISUAL GATE → ENGINE → SPLIT/RESIZE/VALIDATE/MANIFEST/PACKAGE → FINAL HUMAN QA → LINE SUBMISSION READY`

A downstream stage must not begin while a blocking upstream Gate is unresolved.

## 3. Specialist architecture
- **Gem A — Sticker Product Architect:** owns concept, product meaning, caption/use-case architecture, Character/Style requirements, Hero plan, Frame briefs, Sheet plan, QA criteria, and the Production Document Package.
- **Gem B — Sticker Visual Producer:** owns high-resolution visual master production from locked documents.
- **Program / Engine:** owns deterministic splitting, approved alpha/background processing, resize/normalize, naming, technical validation, manifest, and packaging.
- **Product Owner / Human QA:** owns final acceptance.

See `docs/project/MULTI_AGENT_STICKER_PRODUCTION_ARCHITECTURE.md`.

## 4. Blackbox rule
Every specialist component is a Blackbox with seven controls:
1. Input Contract
2. Definition of Ready
3. Responsibility / authority boundary
4. Internal quality controls
5. Exit Gate / Definition of Done
6. Output Contract
7. Defect return path

Internal methods may evolve, but contracts must remain stable.

## 5. Quality at Source
Each stage must complete and verify its own work before handoff. Downstream components are not repair stages for upstream defects.

Examples: weak caption → Gem A; Character drift/clutter → Gem B; invalid dimensions/package → Engine.

## 6. Contract-based handoff
A receiver may start only when the upstream package is complete, its Exit Gate has passed, and status is `READY_FOR_HANDOFF`. No downstream stage may silently change locked upstream SSOT.

See `docs/project/HANDOFF_CONTRACT_STANDARD.md`.

## 7. Communication-first Frame design
Every Frame requires: exact caption, sender intent, chat situation, tone, expression, gesture/action, useful props, camera/composition guidance when material, forbidden drift, and Character reference.

**One Frame = one primary communication intent.**

## 8. 1-second test
At chat-preview scale, the primary intent should be understandable quickly from expression, action, caption and key prop. Scene density, tiny characters, weak hierarchy or unclear use case = FAIL.

## 9. Character governance
Approved Character Sheets are mandatory active references. Locked face, haircut, proportions, wardrobe, palette, signature accessories and age language must be preserved. A Golden Reference may guide later production but does not replace the Character Sheet.

## 10. Hero Gate
Full-set production is blocked until representative Hero Frames pass. If an anchor Hero fails, correct it before generating the rest of the batch.

## 11. Frame / Master Sticker Sheet model
**Frame** = one sticker production unit.  
**Master Sticker Sheet** = one high-resolution image containing multiple equal-size Frames in a deterministic Grid.

Default working profile unless set SSOT overrides it:
- Frame: **512 × 512 px**
- Grid: **5 columns × 2 rows**
- 10 Frames per Sheet
- logical Sheet size: **2560 × 1024 px**

The working master is intentionally larger than final LINE output for high-quality resize-down. Cells must be equal, ordered, documented, and free of bleed.

See `docs/standards/MASTER_SHEET_FRAME_STANDARD.md`.

## 12. Responsibility boundary
AI/Designer owns meaning, Character fidelity, composition, communication clarity and source/master quality. Program/Engine owns deterministic technical preparation. Technical PASS never substitutes for Visual QA PASS.

## 13. Gate model
1. Gate A — Product / Documentation Readiness
2. Gate B — Visual / Master Asset Readiness
3. Gate C — Technical Submission Readiness
4. Gate D — Final Human Acceptance

See `docs/project/QUALITY_GATE_STANDARD.md`.

## 14. Typography
AI-rendered Thai text is candidate-level until verified exactly. Final wording must be proofread 100%; deterministic typography may be used when exact text cannot be guaranteed by generation.

## 15. SSOT precedence
1. current official platform requirements
2. active CPDF / global standards
3. Character SSOT
4. Product / Set SSOT
5. locked Production Document Package
6. current execution task

## 16. Corrective learning
When a Gate failure reveals a systemic weakness: reject the artifact, record root cause, fix the owning stage, update the Framework/standard when needed, update set documents, then re-enter at the correct Gate.

## 17. Traceability
Every final sticker should trace backward through:
`final file → master frame → sheet/frame ID → frame brief → caption/use case → product brief → Character/Style SSOT`.

## 18. Specialist Gem instructions
The Framework is intended to be converted into separate specialist Gem instructions rather than one all-purpose agent. See `docs/project/GEM_INSTRUCTION_ARCHITECTURE.md`.

## 19. Related standards
- `docs/project/MULTI_AGENT_STICKER_PRODUCTION_ARCHITECTURE.md`
- `docs/project/HANDOFF_CONTRACT_STANDARD.md`
- `docs/project/QUALITY_GATE_STANDARD.md`
- `docs/project/GEM_INSTRUCTION_ARCHITECTURE.md`
- `docs/standards/STICKER_COMMUNICATION_STANDARD.md`
- `docs/standards/MASTER_SHEET_FRAME_STANDARD.md`
- `docs/standards/LINE_STICKER_SPEC.md`
- `docs/standards/QA_STANDARD.md`
- `docs/standards/VISUAL_STYLE_GUIDE.md`
