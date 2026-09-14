# Character Sheet Handoff Standard — MTLineSticker

**Document ID:** CH-HANDOFF-STD-001  
**Version:** 1.0  
**Status:** Active

## Purpose
When Character Sheet generation is the next stage, the current specialist must make the handoff executable. Naming the next stage is not enough.

## Required handoff artifacts
The current Production Package must provide:
- `CHARACTER_SHEET_RUNTIME_HANDOFF.md`
- `CHARACTER_SHEET_RUNTIME_PROMPT.txt`
- `CHARACTER_SHEET_HANDOFF_README.md`
- complete current `02_CHARACTER/` documents
- exact owner-confirmed identity/style reference list
- expected output state `READY_FOR_CHARACTER_OWNER_REVIEW`

When the environment supports file/archive creation, also create `CHARACTER_SHEET_HANDOFF.zip` containing the current Character documents, runtime handoff/prompt/readme and confirmed available reference assets.

## Runtime handoff content
`CHARACTER_SHEET_RUNTIME_HANDOFF.md` must summarize:
- package/set identity and revision,
- current roadmap/state,
- Character authority status,
- confirmed identity references,
- confirmed style references,
- active Character locks and lock IDs,
- unresolved items that still affect generation,
- expected output and owner review rule.

It is a navigation/execution aid, not a replacement for source documents.

## Runtime prompt
`CHARACTER_SHEET_RUNTIME_PROMPT.txt` must be ready to copy/paste without requiring the user to reconstruct internal requirements. It must instruct the image-generation stage to read the Character documents and current confirmed references, create only a Character Sheet Candidate, self-check against the approval checklist and return `READY_FOR_CHARACTER_OWNER_REVIEW`. It must not self-activate the sheet.

## Decision closure
When the Product Owner resolves an open decision, the specialist must apply it to the current package, update affected indexes/manifests/open items, recalculate state and continue to the next safe stage. The owner must not be asked to repeat already-known project inputs or manually edit generated package files.

## Reference authority
Only owner-confirmed references may be described as authoritative. Disputed references may remain packaged as evidence only when clearly marked unresolved and must not be promoted by convenience.

## Package accounting
`PACKAGE_MANIFEST.md` must distinguish:
- payload files listed/hashed,
- manifest self-accounting policy,
- total archive file entries,
- reference asset count where applicable.

If the manifest omits its own hash to avoid circular hashing, say so explicitly. Reported counts must match the produced archive.

## Maintainability
Repeated Character rules should be normalized into `GLOBAL_CHARACTER_LOCKS.md` with stable lock IDs. Frame-level documents may reference applicable lock IDs plus frame-specific exceptions instead of duplicating the same long paragraph in every row. This does not permit vague placeholders such as “same as above”.

## UX acceptance
A first-time user should be able to move from Gem A package to Character Sheet generation by following a short README and one copy-paste prompt, without opening the full package to discover which files to use.
