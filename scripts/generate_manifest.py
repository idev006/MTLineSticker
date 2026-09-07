from pathlib import Path
import csv,sys
if len(sys.argv)!=3: raise SystemExit("usage: generate_manifest.py <approved-dir> <output.csv>")
src,out=Path(sys.argv[1]),Path(sys.argv[2])
with out.open("w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["filename","path","status"])
    for p in sorted(src.glob("*.png")): w.writerow([p.name,str(p),"approved"])
print(out)
