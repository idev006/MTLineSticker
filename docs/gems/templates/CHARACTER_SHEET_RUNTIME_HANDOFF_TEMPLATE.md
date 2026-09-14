# CHARACTER_SHEET_RUNTIME_HANDOFF

Set: `[SET NAME / ID]`  
Package revision: `[VERSION]`  
Current state: `[OWNER_DECISION_REQUIRED | BLOCKED | READY_FOR_CHARACTER_OWNER_REVIEW preparation]`

## Character authority
- Character Sheet status: NOT ACTIVE / CANDIDATE / ACTIVE
- Identity references: `[confirmed refs only]`
- Style references: `[confirmed refs only]`
- Global Character locks: `[lock IDs / summary]`

## Required source documents
- `CHARACTER_BIBLE.md`
- `GLOBAL_CHARACTER_LOCKS.md`
- `CHARACTER_SHEET_SPECIFICATION.md`
- `CHARACTER_SHEET_GENERATION_PROMPT.md`
- `CHARACTER_SHEET_NEGATIVE_CONSTRAINTS.md`
- `CHARACTER_SHEET_APPROVAL_CHECKLIST.md`

## Open items affecting generation
`[NONE or exact unresolved items]`

## Expected output
Create a Character Sheet Candidate only. Do not create Hero or Full Production artwork. After self-check, return state:

`READY_FOR_CHARACTER_OWNER_REVIEW`

Only the Product Owner may activate the result as `CHARACTER_SHEET_ACTIVE`.
