#!/usr/bin/env python3
"""Basic fail-closed frame PNG check; excludes subjective and cutter certification."""
import argparse,json
from pathlib import Path
from PIL import Image

def validate(path):
    errors=[]
    try:
        with Image.open(path) as img:
            mode=img.mode;w,h=img.size
            if mode!='RGBA':errors.append('NOT_RGBA')
            if w<=0 or h<=0 or w*512!=h*592:errors.append('FRAME_RATIO_INVALID')
            rgba=img.convert('RGBA');a=rgba.getchannel('A')
            lo,hi=a.getextrema()
            if lo!=0:errors.append('NO_TRUE_TRANSPARENT_PIXELS')
            if hi!=255:errors.append('NO_OPAQUE_PIXELS')
            for pt in ((0,0),(w-1,0),(0,h-1),(w-1,h-1)):
                if rgba.getpixel(pt)[3]!=0:errors.append('OPAQUE_CORNER');break
            if a.getbbox() is None:errors.append('EMPTY_FRAME')
    except Exception as ex:errors.append('UNREADABLE_IMAGE:'+type(ex).__name__)
    return {'file':str(path),'checks':'RGBA/dimensions/alpha only','passed':not errors,'errors':errors,'white_diecut':'NOT_TESTED','thai_caption':'NOT_TESTED','character_consistency':'NOT_TESTED','cutter_compatibility':'NOT_TESTED'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('file',type=Path);ap.add_argument('--report',type=Path);args=ap.parse_args()
    result=validate(args.file);out=json.dumps(result,ensure_ascii=False,indent=2)
    if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(out+'\n')
    print(out);return 0 if result['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
