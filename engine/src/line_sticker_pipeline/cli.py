from __future__ import annotations
import argparse, json
from .engine import EngineConfig
from .pipeline import ProductionPipeline, PipelineOptions

def main(argv=None):
    p=argparse.ArgumentParser(prog='mt-line-sticker'); p.add_argument('input_folder'); p.add_argument('output_folder'); p.add_argument('--workers',type=int,default=2); p.add_argument('--recursive',action='store_true')
    p.add_argument('--mode',choices=('frame-crop','line-sticker'),default='frame-crop')
    p.add_argument('--fit-margin',type=int,default=20)
    p.add_argument('--bg-tolerance',type=int,default=42)
    p.add_argument('--bg-softness',type=int,default=18)
    p.add_argument('--edge-spill-tolerance',type=int,default=150)
    p.add_argument('--edge-spill-radius',type=int,default=8)
    p.add_argument('--final-edge-cleanup-radius',type=int,default=4)
    p.add_argument('--no-package',action='store_true')
    p.add_argument('--allow-package-without-visual-qa-pass',action='store_true')
    ns=p.parse_args(argv)
    def progress(stage,pct,msg): print(f'[{stage:10}] {pct:6.1f}% {msg}',flush=True)
    config=EngineConfig(output_mode=ns.mode.replace('-','_'),fit_margin=ns.fit_margin,bg_tolerance=ns.bg_tolerance,bg_softness=ns.bg_softness,
                        edge_spill_tolerance=ns.edge_spill_tolerance,edge_spill_radius=ns.edge_spill_radius,
                        final_edge_cleanup_radius=ns.final_edge_cleanup_radius)
    options=PipelineOptions(workers=ns.workers,recursive=ns.recursive,package_when_valid_count=not ns.no_package,
                            require_visual_qa_pass_for_package=not ns.allow_package_without_visual_qa_pass)
    report=ProductionPipeline(config=config,options=options).run_folder(ns.input_folder,ns.output_folder,progress)
    print(json.dumps({k:v for k,v in report.items() if k!='jobs'},ensure_ascii=False,indent=2)); return 0

if __name__=='__main__': raise SystemExit(main())
