# Gate A1 acceptance — Connector-native validation

**Project:** SET-KHE-NOI-FIRST-HOME-001 (เข้น้อย กลับบ้านครั้งแรก)

**Validated immutable GitHub snapshot:** `086b8589f156306e30d3d6becaebc2faedc1093e`

**Decision:** A1 DOCUMENT READINESS **PASS** by executed GEM A connector-native verifier; this is an alternative validation runtime to Python, not a claim that the old Python CLI ran. `official_python_validator_executed=false`. No GitHub Actions were required.

## Actual checked evidence
- Fetched GitHub source documents pinned to the immutable commit, then compared SHA-256 calculated in the connector-side JavaScript process against `PACKAGE_MANIFEST.json`: **37/37 MATCH**. JavaScript SHA-256 was self-checked against the well-known `abc` reference vector. Two changed files, `project.json` and `handoff.json`, were re-read and independently checked against the updated manifest after the source commit.
- All **26/26** required document registry entries have the required unique headings and minimum lengths.
- Exact owner-locked Caption Master v0.4.0: **40/40** captions exist under exact F01–F40 headings in the master, and match `frames.json`; no caption edits were made.
- Frame schema mandatory fields, 40 IDs, five 4×2 sheet mappings, 40 unique cell positions, and designated four Hero IDs checked; no errors observed.
- Character approval metadata and reference records valid. Character binaries not required in A1 and were **not** inspected. Product Owner personally supplies the approved Character Sheet and bag images to GEM B at runtime.
- 40 unique expression labels and 40 unique visual-gag labels. **Semantic similarity/visual originality beyond exact labels not certified.**
- No image pixel QA, alpha, cutter, or Hero generation claimed.

## Validation runtime and source integrity
The old Python validator was NOT executed. The actual connector-native JavaScript verifier performed equivalent manifest hashing, registry headings, structural frame/caption tests, metadata/approval and inventory checks. This report is explicit about the execution method so its evidence is independently auditable; a Python run is not a prerequisite to GEM B A2 intake in this rebuilt protocol.

## Handoff limits
A1 PASS authorizes **GEM B to begin Gate A2 only**. GEM B must re-fetch the receipt and validate manifest hashes at the pinned source SHA. GEM B must examine the owner-provided Character Sheet and briefcase imagery before any Hero work. Hero authorization remains subject to applicable Product Owner approval. GitHub stores no owner image binaries.
