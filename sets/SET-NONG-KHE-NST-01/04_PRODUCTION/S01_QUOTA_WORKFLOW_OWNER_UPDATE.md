# S01 generation workflow owner correction

Owner objects to generating every sticker as a separate image because of quota use. Current instruction supersedes skill default individual-image rendering for this task. Stop further separate sticker generation. Generate ONE combined eight-sticker image in a 4x2 matrix, then use deterministic segmentation/compositing for frame dimensions, black borders, alpha0 gutters, 3px shaped white diecut and pixel QA. Do not claim AI-generated geometry is exact without binary checks.

This changes rendering workflow only; F01..F08 captions, intents, character identity, wardrobe locks and S01 geometry remain unchanged. No existing quota use can be undone. S01 still PENDING_OWNER_REVIEW after actual output.
