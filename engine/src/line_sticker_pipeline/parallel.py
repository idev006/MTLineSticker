from __future__ import annotations
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict
from pathlib import Path
from typing import Iterable, Callable, Any
import os, multiprocessing as mp
from .engine import StickerEngine, EngineConfig


def _process_one_sheet(args: tuple[str, str, dict, int]) -> dict:
    src,out_dir,config_dict,start_index=args
    return StickerEngine(EngineConfig(**config_dict)).process_sheet(src,out_dir,start_index=start_index)


class ProcessingCancelled(RuntimeError): pass


class ParallelBatchRunner:
    def __init__(self, config: EngineConfig | None=None, workers: int|None=None):
        self.config=config or EngineConfig(); auto=max(1,(os.cpu_count() or 2)-1)
        self.requested_workers=workers if workers is not None else auto
        self.effective_workers=max(1,min(int(self.requested_workers),32))

    def run(self, sheets: Iterable[str|Path], output_dir: str|Path,
            progress: Callable[[int,int,str],Any]|None=None,
            should_cancel: Callable[[],bool]|None=None) -> list[dict]:
        sheets=sorted(Path(s) for s in sheets); output_dir=Path(output_dir); output_dir.mkdir(parents=True,exist_ok=True)
        cfg=asdict(self.config); tasks=[]
        for i,sheet in enumerate(sheets): tasks.append((str(sheet),str(output_dir/sheet.stem),cfg,i*10+1))
        if not tasks: return []
        results=[]; ctx=mp.get_context('spawn')
        with ProcessPoolExecutor(max_workers=self.effective_workers,mp_context=ctx) as pool:
            futs={pool.submit(_process_one_sheet,t):t[0] for t in tasks}; total=len(futs); done=0
            try:
                for fut in as_completed(futs):
                    if should_cancel and should_cancel():
                        for pending in futs: pending.cancel()
                        raise ProcessingCancelled('processing cancelled by user')
                    result=fut.result(); results.append(result); done+=1
                    if progress: progress(done,total,futs[fut])
            except BaseException:
                for pending in futs: pending.cancel()
                raise
        return sorted(results,key=lambda r:r['sheet'])
