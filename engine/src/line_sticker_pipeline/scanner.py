from __future__ import annotations
from pathlib import Path
import hashlib, time

SUPPORTED={'.png','.jpg','.jpeg','.webp'}

def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def scan_folder(folder: str|Path, recursive: bool=False, stable_wait: float=0.05):
    root=Path(folder)
    it=root.rglob('*') if recursive else root.iterdir()
    files=[]; seen_hash=set()
    for p in sorted(it):
        if not p.is_file() or p.suffix.lower() not in SUPPORTED or p.name.startswith(('~','$','.')): continue
        s1=p.stat().st_size; time.sleep(stable_wait); s2=p.stat().st_size
        if s1!=s2: continue
        digest=sha256_file(p)
        duplicate=digest in seen_hash
        seen_hash.add(digest)
        files.append({'path':p,'sha256':digest,'duplicate':duplicate,'bytes':s2})
    return files
