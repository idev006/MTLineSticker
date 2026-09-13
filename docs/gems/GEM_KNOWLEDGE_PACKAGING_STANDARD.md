# Gemini Gem Knowledge Packaging Standard

**Version:** 1.0  
**Status:** Active  
**Scope:** Packaging repository SSOT into Gemini Gem instructions and attached knowledge files.

## 1. Architectural principle
A Gem Instruction is an **orchestrator**, not the entire knowledge base.

Use four layers:
1. **Gem Instruction** — role, mission, routing, loading policy, stop conditions, gates and outputs.
2. **Knowledge Pack** — compiled specialist knowledge used by that Gem.
3. **Repository SSOT** — authoritative project documents from which knowledge packs are derived.
4. **Runtime Project Context** — current Character/Product/Production Package/Golden Reference.

The repository SSOT remains the source of truth. Knowledge packs are deployment views optimized for AI use.

## 2. Knowledge-file budget
Platform constraint recorded by Product Owner: **maximum 10 attached knowledge files per Gem**.

Project policy:
- design target: **5 fixed knowledge files** per Gem,
- reserve: **5 runtime/project-specific slots**,
- never require all 10 fixed slots,
- consolidate closely related standards instead of mirroring repository files 1:1.

## 3. Fixed versus runtime knowledge
### Fixed knowledge
Stable specialist knowledge reused across products, such as framework, communication, quality, handoff and frame/sheet standards.

### Runtime/project knowledge
Changes by sticker set, such as:
- Character Sheet / Character SSOT,
- Style SSOT,
- Production Document Package,
- Golden Reference,
- set-specific correction or owner-approved decision package.

## 4. Compilation rule
A Knowledge Pack may combine relevant excerpts or normalized rules from multiple repository SSOT documents.

Every compiled file must contain:
- `DOCUMENT_ID`
- `VERSION`
- `STATUS`
- `APPLIES_TO`
- `SOURCE_SSOT`
- `AUTHORITY_NOTE`

Compiled knowledge must not silently contradict or supersede its source SSOT.

## 5. Loading policy
The Orchestrator must:
1. identify current stage,
2. load all mandatory fixed knowledge,
3. load only relevant runtime/project files,
4. validate Definition of Ready,
5. execute the specialist Blackbox,
6. apply Exit Gate,
7. hand off only validated output.

Do not load unrelated knowledge merely because attachment slots remain available.

## 6. Authority and conflict policy
Priority:
1. latest explicit Product Owner decision,
2. active project Framework / standards,
3. Character / Style SSOT,
4. set-specific Product / Production SSOT,
5. approved handoff package,
6. compiled knowledge pack,
7. current working notes.

If a compiled knowledge file conflicts with its source SSOT, the source SSOT wins and the knowledge pack must be corrected.

## 7. Quality-at-source rule
Each Gem is responsible for its own output quality. A downstream Gem must not be used to repair upstream defects.

## 8. Software boundary
Gem instructions and knowledge packaging must not modify existing Python software, `engine/`, `scripts/`, validators, packagers or deterministic production logic unless the Product Owner explicitly opens a separate software-development task.

## 9. Naming convention
Recommended deployment naming:
- `INSTRUCTION.txt`
- `01_...txt` through `05_...txt` for fixed knowledge
- runtime files retain clear project names, e.g. `SET-006-PRODUCTION-PACKAGE.txt`

## 10. Deployment acceptance
A Gem deployment is ready only when:
- Instruction is concise and orchestration-focused,
- fixed knowledge <= 5 files unless explicitly justified,
- runtime capacity remains available,
- source SSOT references are traceable,
- role boundary and handoff status values are explicit,
- no software code is modified as part of Gem packaging.
