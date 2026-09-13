# Master Sticker Sheet & Frame Standard

**Version:** 1.0  
**Status:** Active production standard

## 1. Definitions
**Frame** = one sticker production unit inside a Master Sticker Sheet.

**Master Sticker Sheet** = one high-resolution image containing multiple equal-size Frames arranged in a deterministic Grid for generation, review, and downstream splitting.

A Master Sticker Sheet is not a LINE submission asset.

## 2. Default production profile
Unless a set-specific production spec overrides it:
- Frame size: **512 × 512 px**
- Grid: **5 columns × 2 rows**
- Frames per Sheet: **10**
- Logical Sheet size: **2560 × 1024 px**
- All Frames on a Sheet must have exactly equal dimensions.
- Frame order is row-major: left-to-right, then top-to-bottom.

The 512 × 512 profile is an internal high-resolution working master intended to preserve detail for downstream resize-down. It is not a statement of LINE upload size.

## 3. Master quality requirements
Each Frame must:
- have sufficient edge/detail quality for later reduction,
- keep the primary character/action/caption readable,
- preserve safe breathing room,
- contain one primary communication intent,
- avoid unnecessary scene density,
- keep all required content within its own Frame,
- not leak visual content into adjacent Frames.

## 4. Sheet geometry
When deterministic splitting is required:
- Grid dimensions must be declared before production,
- all cell boundaries must be mathematically equal,
- Frame order must be mapped to sticker IDs,
- no variable-width or variable-height cells,
- no overlapping artwork between cells,
- decorative sheet borders must not contaminate Frame content.

## 5. Background and transparency
Preferred final master behavior is transparent RGBA where generation supports it reliably.

If a removable temporary background is used during generation, it must be:
- uniform or safely removable,
- clearly distinct from foreground artwork,
- free of background gradients/shadows that complicate extraction.

The downstream Engine may perform approved alpha/background processing, but it must not be expected to repair poor foreground design.

## 6. Review overlays
Frame numbers, grid guides, labels, and review borders may exist on a review copy only.

They must not be baked into the production Frame assets unless explicitly intended as sticker content.

## 7. Master Sheet acceptance
A Master Sheet passes only when:
- declared row/column count is correct,
- total Frame count is correct,
- all Frames are equal size,
- frame order mapping is documented,
- content stays inside Frame boundaries,
- image quality is adequate for resize-down,
- Visual QA has passed,
- no blocking caption/Character/communication defects remain.

## 8. Production handoff
The approved Master Sheet is handed to the deterministic Engine together with:
- Sheet ID,
- Set ID,
- Grid dimensions,
- Frame size,
- frame-to-sticker mapping,
- expected output naming,
- any approved processing notes.

The Engine may split/normalize/resize/validate/package. It must not redefine the visual content.
