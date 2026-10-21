# Universal Sticker Sheet Geometry Tolerance — Coordinated Release
Date: 2026-10-21
Status: OWNER_APPROVED; PLUGINS_RELEASED; CUTTER_INTEGRATION_NOT_RUN

## Global change (all sticker sets)
- 8 frames/sheet, 4 columns x 2 rows, PNG RGBA transparent sheet backgrounds.
- Nominal frame size 592x512px; actual frame sizes can vary with REQUIRED exact aspect ratio 592/512, tested by width*512==height*592.
- Between-frame transparent gutter nominal 15px, numeric tolerance +/-5% = [14.25, 15.75] pixels. Since raster pixels are integers, accepted measured gap is 15px at this nominal value.
- Internal sticker safe clearance nominal 15..30px; user-selectable target, default 20px; tolerance +/-5% of chosen nominal. Example at 20px, actual [19,21]px.
- Black #000000 fully opaque rectangular frame border at approximately 3px, square 90-degree corners, no shared borders; cutter removes border.
- A nominal 592x512 frame and 15px gutters give 2413x1039px 4x2 sheet with zero outer margin. Scaling changes actual sheet dimensions; cutter must use actual measured pixel geometry.
- Only real alpha=0 background/gap is accepted, not simulated transparency.
- These rules override old universal contract v1.1.0 hard-exact nominal geometry across all newly produced sets.

## Shared Plugin Contract
- Contract version 1.2.0 in BOTH plugins; updated shared documents and geometry tolerance instructions.
- GEM A v0.3.0, private release: pluginrel_6ad8669151a48191864c09510a63c2fb
- GEM B v0.4.0, private release: pluginrel_6ad8669f6a088191af5f2ee995d97dc9
- Releases confirmed successful by Plugin Creator and contents of both installed releases re-read and checked.
- Specialist team R01-R07 remains role-based maker/checker and not autonomous humans/agents.

## Verification limitations
- Plugin archive validity checked. Both plugin releases deployed and document contract check passed.
- Actual 8-frame image generation and deterministic binary alpha/border tests NOT RUN by this update.
- Integration with legacy ChatGPT Work sticker cutting program NOT RUN; do not claim cutter-ready/LINE-ready output without actual integration test.
