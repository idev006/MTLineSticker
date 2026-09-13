# Character Sheet Lifecycle

**Version:** 1.0  
**Status:** Active

## Purpose
The Character Sheet is the canonical visual reference used to preserve Character identity across sticker production. It bridges Gem A documentation and Gem B visual execution.

## Authority
The approved active Character Sheet is identified as `CHARACTER_SHEET_ACTIVE`.

It is a visual SSOT for identity and continuity, but it does not replace:
- Product Owner decisions,
- Character Bible semantics,
- Product/Production SSOT,
- current platform requirements.

If a conflict exists, stop and resolve it through the documented SSOT precedence instead of silently choosing a source.

## Lifecycle
1. User supplies concept plus text/image/video references as available.
2. Gem A analyzes those inputs and produces `CHARACTER_BIBLE.md`, `CHARACTER_SHEET_SPECIFICATION.md`, `CHARACTER_SHEET_GENERATION_PROMPT.md`, negative constraints and approval checklist.
3. Character Sheet image creation occurs outside Gem A using the approved specification/prompt and relevant references.
4. Product Owner reviews the resulting Character Sheet against the approval checklist.
5. On approval, the image is recorded as `CHARACTER_SHEET_ACTIVE` with version/identity metadata.
6. Gem A may then close Gate A and emit `READY_FOR_GEM_B` if all other requirements pass.
7. Gem B must use `CHARACTER_SHEET_ACTIVE` as a mandatory visual reference for Hero and full production.
8. If a replacement Character Sheet is approved, the prior version becomes inactive and downstream production must explicitly adopt the new active version.

## Approval minimum
Before activation, verify:
- identity resemblance / intended design identity,
- apparent age language,
- face and hair rules,
- body proportions,
- wardrobe logic,
- signature accessories and their side/location when material,
- optional vs mandatory traits,
- style/rendering direction,
- prohibited drift,
- sufficient views/expressions/poses for production continuity.

## No premature handoff
Raw image/video references alone do not equal an approved Character Sheet.

A Character Sheet specification alone does not equal `CHARACTER_SHEET_ACTIVE`.

Unless a Product Owner exception is explicitly documented, Gem A must not emit `READY_FOR_GEM_B` and Gem B must not start Hero production until the active approved Character Sheet exists.

## Change control
Any material identity change requires:
- reason for change,
- updated Character Bible/specification when needed,
- new Character Sheet candidate,
- Product Owner approval,
- explicit version activation.

Gem B must not self-authorize Character redesign.
