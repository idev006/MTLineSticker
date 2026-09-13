# Handoff Contract Standard

**Version:** 1.0  
**Status:** Active

## Principle
A handoff is an explicit quality contract between production stages. The sender must provide complete, verified output; the receiver must not guess missing intent or repair upstream decisions silently.

## Mandatory contract fields
Every handoff package should define:
- source stage / owner,
- destination stage,
- artifact/package ID,
- version,
- status,
- required inputs consumed,
- outputs produced,
- locked decisions,
- allowed adaptations,
- forbidden adaptations,
- QA evidence,
- unresolved non-blocking notes,
- acceptance result,
- return route on failure.

## Definition of Ready
The receiving stage may start only when:
- all mandatory artifacts exist,
- required SSOT references are resolvable,
- all blocking decisions are locked,
- source Exit Gate is PASS,
- package status is READY_FOR_HANDOFF.

If any condition fails, the receiver returns `NOT_READY_FOR_HANDOFF` with missing items rather than improvising.

## Definition of Done
A stage is done only when:
- all required deliverables exist,
- internal QA is complete,
- all blocking defects are closed,
- Exit Gate is PASS,
- evidence is recorded,
- Output Contract is complete.

## Gem A → Gem B contract
Minimum Production Document Package:
- Set ID / product name / version,
- product concept and target user,
- communication territory / JTBD,
- Character and Style SSOT references,
- total frame count,
- exact caption list,
- frame-by-frame intent and chat situation,
- expression / gesture / prop guidance,
- camera/composition guidance where material,
- forbidden drift / negative constraints,
- Hero frame selection and Golden References,
- Sticker Sheet plan,
- default Frame size and Grid layout,
- QA checklist and Exit Gate criteria.

Gem B must not begin full production when this package is incomplete.

## Gem B → Engine contract
Minimum Visual Master Package:
- Set ID / Sheet ID,
- frame order mapping,
- expected rows / columns,
- expected Frame size,
- approved high-resolution Master Sheet(s) and/or individual Master Frames,
- no unintended frame bleed,
- visual QA result,
- caption/frame mapping,
- expected downstream processing notes.

The Engine may transform technical properties but must not reinterpret visual meaning.

## Engine → Final QA contract
Minimum Technical Output Package:
- individual prepared sticker files,
- deterministic naming,
- validation report,
- manifest,
- main/tab assets when in scope,
- package/build report,
- list of warnings or failures.

## Reject / return format
A rejected handoff records:

```text
STATUS: NOT_READY_FOR_HANDOFF
DEFECT_OWNER: <stage>
ARTIFACT: <id/path>
BLOCKER: <what failed>
EVIDENCE: <reference>
REQUIRED_ACTION: <specific correction>
RETURN_TO: <stage>
REENTRY_GATE: <gate name>
```

## No silent correction rule
A downstream stage may make only transformations explicitly allowed by contract. Changes to meaning, caption, Character identity, product strategy, or locked visual direction require upstream approval and a new package version.
