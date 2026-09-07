from pathlib import Path
import sys
REQUIRED=["README.md","SET_BRIEF.md","CAPTIONS.md","CAPTION_MATRIX.csv","STICKER_MANIFEST.csv","QA_REPORT.md"]
if len(sys.argv)!=2: raise SystemExit("usage: validate_set.py <set-directory>")
root=Path(sys.argv[1]); missing=[x for x in REQUIRED if not (root/x).exists()]
if missing: raise SystemExit("missing: "+", ".join(missing))
print("OK:",root)
