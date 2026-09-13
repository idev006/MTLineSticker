# Project North Star & Success Criteria

**Version:** 1.0  
**Status:** Active project-level governing document  
**Applies to:** All sticker products, Gems, visual-production stages, quality gates, deterministic processing, and final human review.

## 1. North Star
The project exists to produce LINE sticker products that:

> **match the user's approved intent, communicate effectively in real chat, maintain coherent Character/Style quality, satisfy current LINE Creators Market requirements at submission time, and are commercially ready to sell.**

Process artifacts, Gems, documents, Hero Sheets, Master Sticker Sheets, QA reports and technical packages are means to this outcome; none is an end in itself.

## 2. Definition of Product Success
A sticker product is successful only when all four dimensions pass together.

### A. User Intent Fit
- Product concept reflects the user's approved objective.
- Character identity and style match the approved references.
- Captions, tone, use cases and visual direction are accepted by the Product Owner/user.
- Material changes require explicit approval rather than silent reinterpretation.

### B. Communication & Visual Quality
- Each Frame has one primary communication intent.
- Meaning is quickly understandable at chat-preview scale.
- Caption, expression, action and props reinforce one another.
- Character identity remains consistent across the set.
- Artwork remains readable after reduction and avoids unnecessary scene clutter.
- Hero review is used when required to validate visual direction before scale-up.

### C. Platform & Technical Compliance
- Current official LINE Creators Market requirements are verified at the technical/submission stage.
- Required file count, dimensions, format, transparency/background behavior, naming, size limits and package integrity pass the current technical checks.
- Main image, chat-tab image and other required submission assets are present when applicable.
- Current official platform requirements override stale internal assumptions.

### D. Commercial Readiness
- The set is useful enough to be sent in realistic chat situations.
- The product has a coherent audience, positioning and communication territory.
- The full set has sufficient message/pose/use-case variety and avoids excessive redundancy.
- Final store assets and metadata are complete enough for actual submission and sale.

## 3. End-to-End Success Chain

`USER NEED / IDEA → GEM A DOCUMENTATION → CHARACTER/STYLE REFERENCES → GEM B HERO REVIEW → OWNER APPROVAL → GEM B FULL VISUAL PRODUCTION → PROGRAM/ENGINE TECHNICAL PREPARATION → FINAL HUMAN QA → LINE SUBMISSION READY → SALE / LEARNING`

Every stage must protect the North Star rather than optimize its own local output in isolation.

## 4. Stage Contribution

### Gem A — Sticker Product Architect
Success means Gem B can execute without guessing product intent. Gem A converts user needs and references into a complete, coherent, production-ready document package.

### Character/Style Reference Creation
Character Sheet imagery may be created by an approved visual tool/workflow from Gem A's Character Bible / Character Sheet specification. The approved image becomes the active Character visual reference.

### Gem B — Sticker Visual Producer
Success means the user can verify the visual direction through Hero output and, after approval, receive complete visual Master Sticker Sheets/Frames that match the approved documents and Character reference.

### Program / Engine
Success means approved visual masters are transformed deterministically into technically valid submission assets without changing product meaning or visual intent.

### Product Owner / Human QA
Success means the final package is both faithful to the desired product and acceptable for real LINE submission.

## 5. Gate Principle
A Gate is useful only if it prevents a defect from escaping downstream.

- Gate A protects product/document truth.
- Hero Review protects user-intent and visual-direction fit before scale-up.
- Gate B protects visual master quality.
- Gate C protects technical/platform readiness.
- Gate D protects final human acceptance and commercial submission readiness.

Passing one Gate never compensates for failing another.

## 6. Hero-to-Full-Production Principle
When Hero gating is required, full-set visual production is blocked until representative Hero output has been reviewed and approved by the user/Product Owner.

For a typical 40-sticker static set, the standard production pattern is:
- Hero Sticker Sheet: one review Sheet containing the approved Hero subset defined by the Production Document Package.
- After Hero approval: four standard Master Sticker Sheets, 10 Frames each, unless a set-specific approved plan defines another deterministic layout.

## 7. Quality-at-Source Rule
Defects are corrected by the stage that owns them:
- product/caption/use-case/document defects → Gem A,
- Character/composition/visual defects → Gem B,
- deterministic split/resize/naming/package defects → Program/Engine,
- unresolved preference/commercial acceptance decisions → Product Owner.

Downstream stages must not silently repair upstream SSOT.

## 8. Release Success Criteria
Before a product may be declared `LINE_SUBMISSION_READY`, all of the following must be true:
- user/Product Owner has approved the intended product and visual direction,
- all required sticker Frames are present and correctly mapped,
- Character/Style consistency has passed visual QA,
- captions/content have been proofread and accepted,
- current LINE technical requirements have been checked and passed,
- required submission assets and package evidence are complete,
- no unresolved P0/P1 defect remains,
- final human review has approved the submission package.

## 9. Learning Loop
Commercial readiness does not end at submission. After release, capture observed user feedback, usage patterns, store performance and production lessons. Feed validated learning back into Product Architecture, communication standards and future sets without rewriting historical truth.

## 10. Authority and Boundaries
- Current official LINE requirements take priority for platform compliance.
- Latest explicit Product Owner decisions control product intent when they do not conflict with platform/legal requirements.
- Repository SSOT governs project execution.
- This document defines outcome priorities and does not authorize modifications to existing Python software, `engine/`, `scripts/`, validators, packagers or deterministic processing logic.

## 11. North-Star Test
When considering any new document, rule, Gem behavior, visual step or technical process, ask:

> **Does this measurably improve the chance that the user receives the sticker product they actually want, that the stickers communicate well, and that the final package can be submitted and sold on LINE?**

If the answer is no, the process should be simplified, removed, or treated as optional rather than becoming mandatory bureaucracy.
