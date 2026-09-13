# Gemini Gem Knowledge Packaging Standard

**Version:** 1.1  
**Status:** Active  
**Scope:** Packaging repository SSOT into Gemini Gem instructions and attached knowledge files.

## 1. Architectural principle
A Gem Instruction is an **orchestrator**, not the entire knowledge base.

Use four layers:
1. **Gem Instruction** — role, mission, routing, loading policy, stop conditions, gates and outputs.
2. **Knowledge Pack** — compiled specialist knowledge used by that Gem.
3. **Repository SSOT** — authoritative project documents from which Knowledge Packs are derived.
4. **Runtime Project Context** — current Character/Product/Production Package/Golden Reference material.

Repository SSOT remains authoritative. Knowledge Packs are deployment views optimized for AI use.

## 2. Knowledge-file budget
Deployment constraint recorded by Product Owner: **maximum 10 attached knowledge files per Gem**.

Project policy:
- target: **5 fixed knowledge files** per Gem,
- reserve: **5 runtime/project-specific attachment slots**,
- do not consume reserved slots merely because capacity exists,
- consolidate related standards instead of mirroring repository documents one-to-one,
- if the platform limit changes, update this standard before changing deployment packs.

The budget is a deployment constraint, not a reason to omit mandatory knowledge.

## 3. Fixed versus runtime knowledge
### Fixed knowledge
Stable specialist knowledge reused across products: governance, communication, Character/style rules, quality/gates, handoff, Frame/Sheet rules, and package schema.

### Runtime/project knowledge
Changes by sticker set, for example:
- Character Sheet / Character SSOT,
- Style SSOT when separate,
- approved Production Document Package,
- Golden Reference material,
- set-specific owner decision/correction package.

Where practical, combine runtime text documents into one traceable set package so visual/reference attachments retain available slots.

## 4. Compilation rule
A Knowledge Pack may combine normalized rules from multiple repository SSOT documents.

Every compiled file must contain:
- `DOCUMENT_ID`
- `VERSION`
- `STATUS`
- `APPLIES_TO`
- `SOURCE_SSOT`
- `AUTHORITY_NOTE`

Compiled knowledge must not silently contradict, supersede, or invent rules beyond its source SSOT.

## 5. Loading policy
The Orchestrator must:
1. identify the current specialist/stage,
2. load all mandatory fixed knowledge,
3. load only runtime/project files relevant to the active set,
4. validate Definition of Ready,
5. execute the specialist Blackbox,
6. apply internal QA and Exit Gate,
7. emit the destination-specific readiness state only after PASS.

Do not load unrelated knowledge merely because slots remain available.

## 6. Authority and conflict policy
Priority:
1. current official platform requirements,
2. latest explicit Product Owner decision that does not conflict with platform requirements,
3. active project Framework / global standards,
4. Character / Style SSOT,
5. set Product / Production SSOT,
6. approved handoff package,
7. compiled Knowledge Pack,
8. current execution notes/task.

If compiled knowledge conflicts with source SSOT, source SSOT wins and the Knowledge Pack must be corrected before the next deployment baseline.

## 7. Version and freshness policy
A Knowledge Manifest must record the version of every fixed file. Before deployment, confirm that its `SOURCE_SSOT` versions are still active. Do not mix superseded and active compiled rules in one Gem.

## 8. Quality-at-source rule
Each Gem is responsible for its own output quality. A downstream Gem must not be used to repair upstream defects.

## 9. Software boundary
Gem instructions and knowledge packaging must not modify existing Python software, `engine/`, `scripts/`, validators, packagers or deterministic production logic unless the Product Owner explicitly opens a separate software-development task.

## 10. Naming convention
Recommended deployment naming:
- `INSTRUCTION.txt`
- `01_...txt` through `05_...txt` for fixed knowledge
- runtime files use clear set-specific names, e.g. `SET-006-PRODUCTION-PACKAGE.txt`

## 11. Deployment acceptance
A Gem deployment is ready only when:
- Instruction is concise and orchestration-focused,
- fixed knowledge is normally <= 5 files,
- runtime capacity remains available,
- mandatory knowledge is present,
- source SSOT references and versions are traceable,
- role boundary and destination-specific handoff states are explicit,
- no contradictory or superseded rule remains,
- no software code is modified as part of Gem packaging.
