from __future__ import annotations
import argparse, json
from .pipeline import ProductionPipeline, PipelineOptions

def main(argv=None):
    p=argparse.ArgumentParser(prog='mt-line-sticker'); p.add_argument('input_folder'); p.add_argument('output_folder'); p.add_argument('--workers',type=int,default=2); p.add_argument('--recursive',action='store_true')
    ns=p.parse_args(argv)
    def progress(stage,pct,msg): print(f'[{stage:10}] {pct:6.1f}% {msg}',flush=True)
    report=ProductionPipeline(options=PipelineOptions(workers=ns.workers,recursive=ns.recursive)).run_folder(ns.input_folder,ns.output_folder,progress)
    print(json.dumps({k:v for k,v in report.items() if k!='jobs'},ensure_ascii=False,indent=2)); return 0

if __name__=='__main__': raise SystemExit(main())
