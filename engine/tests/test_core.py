from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

from line_sticker_pipeline.engine import border_connected_mask, resize_rgba_premultiplied
from line_sticker_pipeline.validator import StaticStickerValidator
from line_sticker_pipeline.jobdb import JobStore
from line_sticker_pipeline.locking import FileLock, FileLockError
from line_sticker_pipeline.scanner import scan_folder
from line_sticker_pipeline.parallel import ParallelBatchRunner


def test_border_connected_preserves_enclosed_candidate():
    candidate=np.ones((12,12),dtype=np.uint8); candidate[3:9,3:9]=0; candidate[5:7,5:7]=1
    outside=border_connected_mask(candidate)
    assert outside[0,0]==1 and outside[5,5]==0


def test_premultiplied_resize_neutralizes_transparent_rgb():
    rgba=np.zeros((16,16,4),dtype=np.uint8); rgba[...,1:3]=255
    rgba[4:12,4:12,:3]=255; rgba[4:12,4:12,3]=255
    out=resize_rgba_premultiplied(rgba,(31,31)); transparent=out[...,3]==0
    assert np.all(out[transparent,:3]==0)


def test_validator_accepts_line_sized_png(tmp_path):
    p=tmp_path/'01.png'; Image.new('RGBA',(370,320),(255,255,255,255)).save(p,dpi=(72,72))
    assert StaticStickerValidator().validate(p).passed


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
