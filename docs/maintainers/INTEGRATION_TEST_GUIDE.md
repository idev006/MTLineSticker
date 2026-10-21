# Integration & Acceptance Tests — GEM A → GEM B → Cutter

## Test objects required
- Actual deployed GEM A/B source and plugin version readback
- Contract envelope and locked frame mapping
- Owner-approved source Character Sheet binary available at runtime
- A candidate master-sheet PNG binary and expected geometry manifest
- Actual downstream cutter (ChatGPT Work or equivalent) and its exported sticker binaries

## Checkpoints (mark PASS/FAIL/NOT_RUN/BLOCKED individually)
| ID | Test | PASS evidence |
|---|---|---|
| C01 | Handoff schema | `contract_version=1.3.0`, all required IDs/revisions/references |
| C02 | Mapping | 40 distinct frames, no missing/duplicate, 5 sheets × 8 |
| C03 | Authority | Character image and owner gate approvals verifiably accessible |
| V01 | Visual identity | Face age, features, cap/jacket/brand consistent with authoritative primary figure |
| V02 | Frame intent | Each sticker matches approved per-frame expression/gesture/props |
| P01 | File | Saved binary opens PNG with explicit RGBA mode/alpha channel |
| P02 | Background | Pixel alpha=0 for ALL expected empty frame regions |
| P03 | Gutters | Pixel alpha=0 for ALL inter-frame gutter regions |
| P04 | False transparency | No painted checkerboard, white full-frame canvas, or RGB export |
| P05 | White die-cut | Opaque white 3–5px silhouette underlay behind artwork; actual mask comparison and contour inspection |
| P06 | Safe zone | All art, effects and white underlay maintain selected clearance from inner black frame boundary |
| P07 | Frame/gutter math | 4x2, frame exact ratio, black border, tolerances and actual pixel dimensions |
| P08 | Artifact integrity | Image exported/reopened and sampled; include checksum, dimensions, failing coordinates |
| E01 | Cutter extraction | Removes frame, keeps white die-cut, extracts 8 usable individual stickers |
| E02 | LINE export | Final individual PNGs checked against CURRENT official LINE submission requirements |

## Evidence format per test
```json
{"test_id":"P02","status":"NOT_RUN","artifact_sha256":null,"measurements":{},"tool":null,"checked_at":null,"defects":[]}
```
Don't fabricate `PASS`, hashes, dates, specific measurements or source availability. Report actual measured artifacts and code/tool used.

## Minimal deterministic QA idea (pseudocode)
```python
from PIL import Image
im=Image.open(sheet_path)
assert im.format=="PNG" and im.mode=="RGBA"
alpha=im.getchannel("A")
# derive exact frame/gutter coordinates from manifest, not from model guesses
for gutter_box in manifest.gutter_boxes:
    assert alpha.crop(gutter_box).getextrema()==(0,0)
# validate empty areas using an explicit expected artwork-mask and frame-border mask
# compare die-cut outline with dilated intent-mask and safe-zone boundaries
# save and reopen to verify real serialized PNG, not the UI preview
```
No generic assertion of all interior alpha0: artwork is supposed to be visible! White die-cut/black frame are allowed opaque. Automated tests may need anti-aliased-edge tolerance and explicit approved mask geometry, but empty regions/gutters must remain alpha0.

## Required reporting
Separate `visual_review`, `pixel_qa`, `cutter_integration`, and `line_submission_review`. Only report `READY_FOR_ENGINE` when required relevant tests pass, and `LINE_SUBMISSION_READY` only after platform-format/export validation. If not run, output NOT_RUN.
