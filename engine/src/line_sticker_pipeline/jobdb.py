from __future__ import annotations
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

SCHEMA='''
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS jobs (
 id INTEGER PRIMARY KEY AUTOINCREMENT, source_path TEXT NOT NULL UNIQUE, source_sha256 TEXT,
 status TEXT NOT NULL, stage TEXT NOT NULL, progress REAL NOT NULL DEFAULT 0,
 output_dir TEXT, error TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS events (
 id INTEGER PRIMARY KEY AUTOINCREMENT, job_id INTEGER, level TEXT NOT NULL,
 event_type TEXT NOT NULL, message TEXT NOT NULL, created_at TEXT NOT NULL,
 FOREIGN KEY(job_id) REFERENCES jobs(id)
);
'''
VALID_STATES={'DISCOVERED','VALIDATING','READY','LOCKED','PROCESSING','QA_PENDING','PASSED','EXPORTING','COMPLETED','WARNING','FAILED','CANCELLED','PAUSED','RECOVERY_REQUIRED'}

class JobStore:
    def __init__(self,path:str|Path):
        self.path=Path(path); self.path.parent.mkdir(parents=True,exist_ok=True)
        self.con=sqlite3.connect(self.path); self.con.row_factory=sqlite3.Row; self.con.executescript(SCHEMA); self.con.commit()
    def close(self): self.con.close()
    def upsert_discovered(self,source_path:str,sha256:str|None=None,output_dir:str|None=None)->int:
        now=_now(); self.con.execute('''INSERT INTO jobs(source_path,source_sha256,status,stage,progress,output_dir,created_at,updated_at)
        VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(source_path) DO UPDATE SET source_sha256=excluded.source_sha256,output_dir=excluded.output_dir,updated_at=excluded.updated_at''',(source_path,sha256,'DISCOVERED','SCAN',0.0,output_dir,now,now)); self.con.commit()
        return int(self.con.execute('SELECT id FROM jobs WHERE source_path=?',(source_path,)).fetchone()['id'])
    def transition(self,job_id:int,status:str,stage:str,progress:float,error:str|None=None):
        if status not in VALID_STATES: raise ValueError(f'invalid status: {status}')
        progress=max(0.0,min(100.0,float(progress))); self.con.execute('UPDATE jobs SET status=?,stage=?,progress=?,error=?,updated_at=? WHERE id=?',(status,stage,progress,error,_now(),job_id)); self.con.commit()
    def event(self,job_id:int|None,level:str,event_type:str,message:str):
        self.con.execute('INSERT INTO events(job_id,level,event_type,message,created_at) VALUES(?,?,?,?,?)',(job_id,level,event_type,message,_now())); self.con.commit()
    def jobs(self): return [dict(r) for r in self.con.execute('SELECT * FROM jobs ORDER BY id')]

def _now()->str: return datetime.now(timezone.utc).isoformat()
