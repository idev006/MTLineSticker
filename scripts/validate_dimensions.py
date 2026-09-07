from pathlib import Path
import sys
from PIL import Image
if len(sys.argv)<2: raise SystemExit("usage: validate_dimensions.py <png> [...]")
bad=0
for raw in sys.argv[1:]:
    p=Path(raw)
    with Image.open(p) as im:
        ok=im.width<=370 and im.height<=320
        print("OK" if ok else "FAIL",p,im.size)
        bad += 0 if ok else 1
raise SystemExit(1 if bad else 0)
