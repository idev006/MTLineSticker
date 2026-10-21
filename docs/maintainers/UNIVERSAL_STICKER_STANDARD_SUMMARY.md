# Universal Sticker Standards — Maintainer Quick Reference

**Applies to every newly produced set**, unless Product Owner formally approves a new global standard and both plugins are migrated.

| Attribute | Mandatory rule |
|---|---|
| Sheet layout | 4 columns × 2 rows, exactly 8 artwork frames |
| 40-frame set | 5 distinct sheets, F01–F40 each used exactly once |
| Frame aspect | Exact `width*512 == height*592` (nominal frame 592×512 px) |
| Frame border | Separate solid black #000000 opaque rectangular cutter marker, nominal approx. 3px, inward |
| Gutter | Nominal 15px, ±5%; truly alpha0, no overdraw |
| Safe-zone | Owner-selected nominal 15–30px, recommended 20px; ±5% of selected value, measured from INNER border. Includes die-cut and FX |
| Nominal full sheet | 2413×1039 px at 592×512 + 15px gap, zero exterior margin; scaling allowed when exact frame ratio and geometry verified |
| Encoded format | Saved PNG true RGBA, real alpha channel |
| Empty pixels | `alpha=0` **100% transparent** inside frames and in gutters |
| Character/sticker art | Preserve intentional opacity/antialiasing and identity; no generated checkerboard |
| White shaped die-cut | Opaque #FFFFFF, alpha255 underlay extending approx. 3–5px beyond COMPLETE artwork contour; not a white rectangle or the frame border |
| Cutter | Black frame for sheet slicing is removed; die-cut remains attached to each sticker |
| Technical certification | Actual binary pixel tests + cutter interoperability evidence, not vision-only claims |

Clarifications:
1. “Transparent background 100%” means empty *background* pixels alpha0; it does not mean the entire sheet's alpha channel is zero. Character, black frame, white die-cut are intentionally visible.
2. A PNG filename is insufficient proof; RGB PNG can embed a white-gray checkerboard image with NO transparency.
3. Pixel-radius 3–5 is interpreted at nominal 592×512 frame size. Scale consistently where alternate frame dimensions are approved.
4. A white die-cut is not a white halo of the rectangular frame; create a silhouette mask from all intentional art/props/effects, dilate smoothly, composite white *behind* art and inspect for disconnected islands/holes.
5. Keep white edge and all effects within the safe zone; touching black frame fails.
6. Floating icons/icons beyond the base subject should be included in the intentional mask and reviewed for cuttable components.
7. Geometry tolerance is measured against the selected nominal, not an arbitrary cumulative rounding allowance. Keep measured integer coordinates and document acceptance policy.

Refer to live plugin sources `knowledge/GEOMETRY_TOLERANCE_V1_2.md`, `knowledge/WHITE_DIECUT_STANDARD_V1_3.md`, and for GEM B `knowledge/TRUE_ALPHA_EXPORT_STANDARD_V1_4.md`.
