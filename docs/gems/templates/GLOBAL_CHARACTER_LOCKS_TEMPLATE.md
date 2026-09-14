# GLOBAL_CHARACTER_LOCKS

Use stable IDs for repeated Character rules so Frame-level documents can reference them without duplicating long text.

Example structure:

| Lock ID | Category | Rule | Source / authority |
|---|---|---|---|
| GCL-IDENTITY-01 | Identity | [locked visible identity rule] | [owner/reference/SSOT] |
| GCL-HAIR-01 | Hair | [locked haircut/hairline rule] | [owner/reference/SSOT] |
| GCL-BODY-01 | Proportion | [locked body/proportion rule] | [owner/reference/SSOT] |
| GCL-WARDROBE-01 | Wardrobe | [locked default wardrobe rule] | [owner/reference/SSOT] |
| GCL-ACCESSORY-01 | Accessory | [mandatory/optional placement rule] | [owner/reference/SSOT] |
| GCL-STYLE-01 | Style | [active rendering/style rule] | [owner/reference/SSOT] |

Frame Communication Matrix usage:
- `Applicable locks`: list exact GCL IDs.
- `Frame-specific constraints/exceptions`: state only what differs or matters for that Frame.

Do not use vague placeholders such as “same as above”. The lock IDs must resolve to explicit rules in this file.
