# คุณยายของเรา No.1 — Gemstone Jewelry Addendum v1.0

**Decision:** Product Owner directed (2026-11-06 Asia/Bangkok), in this conversation, that Grandma wears a necklace with a **large gemstone pendant**, with **bright, sparkling matching gemstone jewelry** coordinated with the color of her Thai sabai outfit in each frame. This direction supplements existing owner-approved Character Sheet and owner-locked Sticker Table; it does **not** overwrite their source bytes or texts.

## Invariant design
- One consistent gold-toned necklace, featuring a **large faceted gemstone pendant centrally on the chest**, immediately readable at sticker size.
- Matching bright, sparkling gemstone earrings; tasteful bracelets and optional gold ornamentation. Keep the silhouette charming, not overloaded.
- Fully opaque white highlights / bright specular facets; no semitransparent glitter/glow. Alpha for sticker art 0 or 255 only.
- Pendant must fit and remain legible without covering face, glasses, hands, locked pose/props, Thai lettering, or 40px minimum Safe Area. If obscured by gesture or prop, flag for image review instead of pretending a pass.

## Frame-bound gemstone and wardrobe mapping (from existing locked Sticker Table)
| Frame | Wardrobe | Large pendant / gem jewelry |
|---|---|---|
| F01 | เหลือง | บุษราคัมสีเหลือง |
| F02 | ชมพู | แซฟไฟร์สีชมพู |
| F03 | เขียว | มรกต |
| F04 | ส้ม | โกเมนสีส้ม |
| F05 | น้ำเงิน | ไพลิน |
| F06 | ม่วง | อเมทิสต์ |
| F07 | แดง | ทับทิม |
| F08 | เขียว | มรกต |

All other frames follow their own existing locked `wardrobe_color` and `gemstone` fields, not a newly invented day mapping.

## Approval / QA boundaries
- Status: **OWNER_DIRECTIVE_ACCEPTED_AS_ACCESSORY_ADDENDUM**; no claim that the approved one-page Character Sheet has changed or been reapproved.
- Owner-approved Character Sheet version 0.1 visual SHA-256: `45526a3c7e1fb10ae98ccb7a1817c2e65fb589040a4b68fd5c8dacc9673613f7` remains mandatory actual image input at every render; no substitution by these textual instructions.
- Canonical Sticker Table and Caption Master version 1.0.0 remain unchanged and owner locked.
- Per-frame visual jewelry QA records actual necklace, large pendant, correct gem/color, matching accessories, real opacity, unobstructed caption/pose, and Safe Area. Technical alpha PASS cannot replace semantic visual review.
- Owner has not yet approved new S01 artwork with these accessories; no release-ready claim.
- Preset implementation: MT Sticker GEM A v0.39.0, `JEWEL_GRANDMA_VIVID_SPARKLE` in `BUNDLE_GRANDMA_WOW`.
