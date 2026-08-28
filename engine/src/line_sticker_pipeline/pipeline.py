from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
from typing import Callable, Any
import shutil, json

from .engine import EngineConfig
from .parallel import ParallelBatchRunner, ProcessingCancelled
from .scanner import scan_folder
from .jobdb import JobStore
from .locking import FileLock
from .validator import StaticStickerValidator
from .packaging import LineStaticPackageBuilder


@dataclass
class PipelineOptions:
    workers: int = 2
    recursive: bool = False
    package_when_valid_count: bool = True


class ProductionPipeline:
    def __init__(self, config: EngineConfig | None=None, options: PipelineOptions | None=None):
        self.config=config or EngineConfig(); self.options=options or PipelineOptions()

    def run_folder(self, input_dir: str|Path, output_dir: str|Path,
                   progress: Callable[[str,float,str],Any]|None=None,
                   should_cancel: Callable[[],bool]|None=None) -> dict:
        input_dir=Path(input_dir); output_dir=Path(output_dir); output_dir.mkdir(parents=True,exist_ok=True)
        work=output_dir/'.work'; work.mkdir(exist_ok=True); store=JobStore(work/'jobs.sqlite3')
        lock=FileLock(work/'project.lock',stale_seconds=12*3600)
        jobs: dict[str,int]={}
        def cancelled() -> bool: return bool(should_cancel and should_cancel())
        def check_cancel():
            if cancelled(): raise ProcessingCancelled('processing cancelled by user')
        try:
            with lock:
                check_cancel()
                if progress: progress('SCAN',0,'Scanning input folder')
                scanned=scan_folder(input_dir,recursive=self.options.recursive)
                unique=[x for x in scanned if not x['duplicate']]
                if not unique: raise RuntimeError('no supported input images found')
                for item in unique:
                    jid=store.upsert_discovered(str(item['path']),item['sha256'],str(output_dir/item['path'].stem))
                    store.transition(jid,'READY','QUEUE',0); jobs[str(item['path'])]=jid
                if progress: progress('SCAN',100,f'{len(unique)} unique image(s) ready')
                check_cancel()

                for p,jid in jobs.items(): store.transition(jid,'PROCESSING','FRAME_PROCESSING',5)
                runner=ParallelBatchRunner(self.config,workers=self.options.workers)
                def cb(done,total,src):
                    jid=jobs[src]; pct=5+80*(done/total)
                    store.transition(jid,'QA_PENDING','FRAME_PROCESSING',pct)
                    if progress: progress('PROCESS',pct,f'Processed {done}/{total}: {Path(src).name}')
                results=runner.run([x['path'] for x in unique],work/'processed',progress=cb,should_cancel=cancelled)
                check_cancel()

                sticker_paths=[]
                for result in results:
                    sheet_dir=work/'processed'/Path(result['sheet']).stem
                    src=next(x['path'] for x in unique if x['path'].name==result['sheet'])
                    jid=jobs[str(src)]
                    for item in result['stickers']: sticker_paths.append(sheet_dir/item['output_file'])
                    store.transition(jid,'PASSED','TECHNICAL_QA',90)

                if progress: progress('QA',90,f'Validating {len(sticker_paths)} sticker(s)')
                failed=[v for v in StaticStickerValidator().validate_many(sticker_paths) if not v.passed]
                if failed:
                    for jid in jobs.values(): store.transition(jid,'FAILED','TECHNICAL_QA',90,error='technical validation failed')
                    raise RuntimeError(f'{len(failed)} sticker(s) failed technical validation')
                check_cancel()

                if progress: progress('EXPORT',94,'Committing final sticker files')
                final_stickers=output_dir/'stickers'; temp_final=work/'final_stickers.tmp'
                if temp_final.exists(): shutil.rmtree(temp_final)
                temp_final.mkdir(parents=True)
                for idx,p in enumerate(sticker_paths,1): shutil.copy2(p,temp_final/f'{idx:02d}.png')
                if final_stickers.exists(): shutil.rmtree(final_stickers)
                temp_final.replace(final_stickers)

                package=None
                if self.options.package_when_valid_count and len(sticker_paths) in (8,16,24,32,40):
                    if progress: progress('PACKAGE',97,'Building LINE submission package')
                    package_dir=output_dir/'package'; package_dir.mkdir(exist_ok=True)
                    package=LineStaticPackageBuilder().build(sorted(final_stickers.glob('*.png')),package_dir)

                for jid in jobs.values(): store.transition(jid,'COMPLETED','DONE',100)
                report={'input_images':len(unique),'duplicate_images':sum(1 for x in scanned if x['duplicate']),
                        'stickers':len(sticker_paths),'workers_requested':self.options.workers,
                        'workers_effective':runner.effective_workers,'technical_failures':0,
                        'package':package,'jobs':store.jobs()}
                (output_dir/'production_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
                if progress: progress('DONE',100,f'Completed: {len(sticker_paths)} stickers')
                return report
        except ProcessingCancelled:
            for jid in jobs.values():
                try: store.transition(jid,'CANCELLED','CANCELLED',0,error='cancelled by user')
                except Exception: pass
            if progress: progress('CANCELLED',0,'Processing cancelled')
            raise
        finally:
            store.close()
