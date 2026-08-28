from __future__ import annotations
from pathlib import Path
import os, json, time

class FileLockError(RuntimeError): pass

class FileLock:
    def __init__(self,path:str|Path,stale_seconds:int=86400):
        self.path=Path(path); self.stale_seconds=stale_seconds; self.owned=False
    def acquire(self):
        self.path.parent.mkdir(parents=True,exist_ok=True)
        if self.path.exists():
            try:
                meta=json.loads(self.path.read_text(encoding='utf-8')); age=time.time()-float(meta.get('created_epoch',0))
                if age>self.stale_seconds: self.path.unlink(missing_ok=True)
            except Exception: pass
        try: fd=os.open(self.path,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
        except FileExistsError: raise FileLockError(f'lock already held: {self.path}')
        with os.fdopen(fd,'w',encoding='utf-8') as f: json.dump({'pid':os.getpid(),'created_epoch':time.time()},f)
        self.owned=True; return self
    def release(self):
        if self.owned: self.path.unlink(missing_ok=True); self.owned=False
    def __enter__(self): return self.acquire()
    def __exit__(self,exc_type,exc,tb): self.release()
