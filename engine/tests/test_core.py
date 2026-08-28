from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

from line_sticker_pipeline.engine import EngineConfig, StickerEngine, border_connected_mask, final_edge_cleanup, inset_rect, resize_rgba_premultiplied, suppress_edge_spill
from line_sticker_pipeline.validator import StaticStickerValidator
from line_sticker_pipeline.jobdb import JobStore
from line_sticker_pipeline.locking import FileLock, FileLockError
from line_sticker_pipeline.scanner import scan_folder
from line_sticker_pipeline.parallel import ParallelBatchRunner
from line_sticker_pipeline.pipeline import ProductionPipeline, PipelineOptions
from line_sticker_pipeline.visualqa import VisualQaInspector


def test_border_connected_preserves_enclosed_candidate():
    candidate=np.ones((12,12),dtype=np.uint8); candidate[3:9,3:9]=0; candidate[5:7,5:7]=1
    outside=border_connected_mask(candidate)
    assert outside[0,0]==1 and outside[5,5]==0


def test_premultiplied_resize_neutralizes_transparent_rgb():
    rgba=np.zeros((16,16,4),dtype=np.uint8); rgba[...,1:3]=255
    rgba[4:12,4:12,:3]=255; rgba[4:12,4:12,3]=255
    out=resize_rgba_premultiplied(rgba,(31,31)); transparent=out[...,3]==0
    assert np.all(out[transparent,:3]==0)


def test_edge_spill_cleanup_targets_transparent_boundary_only():
    alpha=np.full((9,9),255,dtype=np.uint8)
    alpha[:,0]=0
    dist=np.full((9,9),180.0,dtype=np.float32)
    dist[:,1]=20.0
    dist[4,4]=20.0
    cleaned=suppress_edge_spill(alpha,dist,tolerance=96,radius=1)
    assert cleaned[4,1] < alpha[4,1]
    assert cleaned[4,4] == 255


def test_final_edge_cleanup_removes_chroma_fringe():
    rgba=np.zeros((12,12,4),dtype=np.uint8)
    rgba[3:9,3:9]=(255,255,255,255)
    rgba[2:10,2]=(120,230,210,180)
    cleaned=final_edge_cleanup(rgba,np.array([120,230,210],dtype=np.uint8),radius=1)
    assert cleaned[5,2,3] == 0
    assert cleaned[5,5,3] == 255


def test_validator_accepts_line_sized_png(tmp_path):
    p=tmp_path/'01.png'
    im=Image.new('RGBA',(370,320),(0,0,0,0))
    ImageDraw.Draw(im).rectangle((20,20,350,300),fill=(255,255,255,255))
    im.save(p,dpi=(72,72))
    assert StaticStickerValidator().validate(p).passed


def test_validator_rejects_content_touching_canvas_edge(tmp_path):
    p=tmp_path/'edge.png'
    im=Image.new('RGBA',(370,320),(0,0,0,0))
    ImageDraw.Draw(im).rectangle((0,20,350,300),fill=(255,255,255,255))
    im.save(p,dpi=(72,72))
    result=StaticStickerValidator().validate(p)
    assert not result.passed
    assert 'content_margin_below_10px' in result.issues


def test_job_state_and_lock(tmp_path):
    store=JobStore(tmp_path/'jobs.db'); jid=store.upsert_discovered('a.png','abc','out'); store.transition(jid,'COMPLETED','DONE',100); assert store.jobs()[0]['status']=='COMPLETED'; store.close()
    p=tmp_path/'x.lock'
    with FileLock(p):
        try: FileLock(p).acquire(); raise AssertionError('expected lock failure')
        except FileLockError: pass


def test_scanner_deduplicates(tmp_path):
    im=Image.new('RGB',(30,30),'white'); im.save(tmp_path/'a.png'); im.save(tmp_path/'b.png')
    result=scan_folder(tmp_path,stable_wait=0); assert len(result)==2 and result[1]['duplicate']


def _make_sheet(path: Path):
    cw,ch,gap,margin=220,190,10,10; w=margin*2+cw*5+gap*4; h=margin*2+ch*2+gap
    im=Image.new('RGB',(w,h),(120,230,210)); d=ImageDraw.Draw(im)
    for row in range(2):
        for col in range(5):
            x=margin+col*(cw+gap); y=margin+row*(ch+gap); d.rectangle((x,y,x+cw,y+ch),outline='black',width=4); d.rectangle((x+70,y+55,x+150,y+150),fill=(120,70,40))
    im.save(path)


def test_spawn_parallel_runner(tmp_path):
    src=tmp_path/'sheet.png'; _make_sheet(src); results=ParallelBatchRunner(workers=2).run([src],tmp_path/'out')
    assert len(results)==1 and results[0]['frames_detected']==10 and results[0]['stickers_exported']==10


def test_engine_reads_unicode_windows_paths(tmp_path):
    folder=tmp_path/'โฟลเดอร์ภาพ'
    folder.mkdir()
    src=folder/'ชีตทดสอบ.png'
    _make_sheet(src)
    result=StickerEngine().process_sheet(src,tmp_path/'out')
    assert result['frames_detected']==10


def test_engine_default_crops_frames_without_bg_removal_or_resize(tmp_path):
    src=tmp_path/'sheet.png'
    _make_sheet(src)
    result=StickerEngine().process_sheet(src,tmp_path/'out')
    first=result['stickers'][0]
    with Image.open(tmp_path/'out'/'01.png') as im:
        assert im.mode == 'RGB'
        assert im.size == tuple(first['output_size'])
        assert im.size != (370,320)
        edges=np.concatenate([
            np.asarray(im)[0,:,:],
            np.asarray(im)[-1,:,:],
            np.asarray(im)[:,0,:],
            np.asarray(im)[:,-1,:],
        ])
        assert not np.any(np.all(edges < 12, axis=1))


def test_inset_rect_removes_detected_frame_border():
    assert inset_rect(10,20,100,80,8,200,200) == (18,28,84,64)


def test_engine_places_stickers_on_transparent_canvas_with_safe_margin(tmp_path):
    src=tmp_path/'sheet.png'
    _make_sheet(src)
    StickerEngine(EngineConfig(output_mode='line_sticker')).process_sheet(src,tmp_path/'out')
    result=StaticStickerValidator().validate(tmp_path/'out'/'01.png')
    assert result.passed
    assert result.content_margin is not None
    assert min(result.content_margin) >= 10


def test_visual_qa_flags_invalid_submission_count(tmp_path):
    paths=[]
    for i in range(2):
        p=tmp_path/f'{i+1:02d}.png'
        im=Image.new('RGBA',(370,320),(0,0,0,0))
        ImageDraw.Draw(im).rectangle((40,40,330,280),fill=(255,255,255,255))
        im.save(p,dpi=(72,72))
        paths.append(p)
    report=VisualQaInspector().inspect_many(paths,tmp_path/'qa')
    assert report['status']=='REVIEW_REQUIRED'
    assert 'invalid_sticker_count:2' in report['issues']
    assert (tmp_path/'qa'/'visual_qa_report.json').exists()
    assert (tmp_path/'qa'/'visual_qa_sheet.png').exists()


def test_pipeline_blocks_package_when_count_is_not_line_ready(tmp_path):
    src=tmp_path/'input'
    src.mkdir()
    _make_sheet(src/'sheet.png')
    report=ProductionPipeline(options=PipelineOptions(workers=1)).run_folder(src,tmp_path/'out')
    assert report['stickers']==10
    assert report['package'] is None
    assert report['output_mode']=='frame_crop'
    assert report['output_folder']=='frames'
    assert 'frame_crop_mode_not_line_ready' in report['package_blockers']
    assert (tmp_path/'out'/'frames').exists()


def test_pipeline_line_sticker_mode_blocks_invalid_submission_count(tmp_path):
    src=tmp_path/'input'
    src.mkdir()
    _make_sheet(src/'sheet.png')
    report=ProductionPipeline(config=EngineConfig(output_mode='line_sticker'),options=PipelineOptions(workers=1)).run_folder(src,tmp_path/'out')
    assert report['stickers']==10
    assert report['package'] is None
    assert 'invalid_sticker_count:10' in report['package_blockers']
    assert (tmp_path/'out'/'visual_qa_report.json').exists()
