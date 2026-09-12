# Sticker Communication Standard

**Version:** 1.1  
**Status:** Mandatory production standard

## Principle
A LINE sticker is a **communication asset**, not merely an illustration. Every sticker must help a user communicate one clear intent, emotion, status, request, response, or action in chat.

## Communication-first hierarchy
1. Communication intent / use case
2. Caption meaning
3. Facial expression + gesture/action
4. Supporting prop / action cue
5. Character/style fidelity
6. Decorative detail

Decorative detail is subordinate. If it weakens message clarity, remove it.

## One sticker = one primary message
Before production, every sticker must define:
- **Caption** — exact approved wording
- **Sender intent** — what the sender means
- **Likely chat situation** — when the sticker is sent
- **Emotion/tone** — how it should feel
- **Visual cue** — pose/expression/action that communicates the meaning before the text is fully read
- **Required prop** — only if it improves comprehension
- **Forbidden distractions** — details/scenes that could dilute the message
- **Approved character reference**

Do not create an illustration first and force a caption onto it afterward.

## 1-second communication test
At chat-preview scale, the intended message should be understandable in approximately one second from the combined caption, expression, gesture/action, and key prop.

FAIL if:
- the viewer must inspect a scene to understand the point,
- props compete with the character or caption,
- the character is too small,
- the action is ambiguous,
- the image is visually attractive but the chat use case is unclear.

## Thumbnail / chat-size rule
At reduced size, the viewer should still identify:
- the character's main expression,
- the main gesture/action,
- the caption hierarchy,
- the key prop when needed.

Avoid scene-like compositions, excessive small props, weak contrast, tiny full-body figures, or decorative effects that slow communication.

## Caption-image relationship
The image must **add meaning to the caption**, not simply decorate it. Preferred relationships:
- confirms the action,
- strengthens emotion,
- adds controlled humor,
- clarifies status,
- makes the phrase faster to understand.

## Character reference rule
When a set has an approved Character Sheet, it is a mandatory active visual reference for every generation/revision pass. A candidate with wrong face, haircut, age, proportions, signature clothing, or key accessories is rejected even when the artwork is otherwise attractive.

A set may designate an approved prototype as a **Golden Reference** for rendering/composition consistency. Golden Reference complements, but never replaces, the Character Sheet.

## Production source rule
Create and approve **individual sticker masters** first. Contact/review sheets are QA artifacts and should preferably be assembled deterministically from approved individual masters.

Do not use a visually generated multi-frame sheet as the source of final stickers when exact frame geometry, transparent edges, typography, or per-frame QA cannot be guaranteed.

## Typography control
AI-generated Thai text is candidate-level until verified. Final text must be proofread 100%. If generation cannot reliably preserve exact wording, apply typography using a deterministic production layer.

## Production preflight
Before generating any candidate, confirm:
- [ ] exact caption is locked
- [ ] sender intent is written
- [ ] likely chat use case is written
- [ ] emotion/tone is defined
- [ ] visual cue is defined
- [ ] approved Character Sheet/reference is active
- [ ] required and forbidden visual traits are stated
- [ ] output type is standalone sticker art, not poster/infographic/scene
- [ ] background/export plan is compatible with transparent PNG
- [ ] expected small-size readability is considered

## Acceptance blockers
Any of these = FAIL:
- message/use case unclear
- image does not support caption
- fails 1-second test
- wrong character identity
- generic/chibi redesign when not approved
- scene or infographic instead of sticker asset
- caption typo or wrong wording
- poor readability at chat size
- non-transparent final background
- technical LINE noncompliance

## Official-platform alignment
Follow the latest LINE Creators Market creation and review guidelines before submission. Platform rules override internal working assumptions when they differ.

See `docs/project/CHARACTER_PRODUCT_DEVELOPMENT_FRAMEWORK.md`.
