"""MTLineSticker handoff semantic checks; use JSON Schema alongside this validator."""
import json, re, sys
from pathlib import Path
H=lambda x: bool(re.fullmatch('[0-9a-fA-F]{64}',str(x or '')))
S=lambda x: bool(re.fullmatch('[0-9a-fA-F]{40}',str(x or '')))
def validate(d):
    e=[]
    if d.get('contract_version')!='1.0.0': e.append('UNSUPPORTED_VERSION')
    if not S(d.get('source_commit')): e.append('SOURCE_COMMIT_INVALID')
    if not H(d.get('package_manifest_sha256')): e.append('PACKAGE_HASH_INVALID')
    f=d.get('frames',[])
    if not isinstance(f,list) or not f or len(f)!=len(set(f)): e.append('FRAME_IDS_INVALID')
    f=f if isinstance(f,list) else []
    sheets=d.get('sheets',[])
    assigned=[i for s in sheets for i in s.get('frame_ids',[])]
    if len(assigned)!=len(set(assigned)): e.append('DUPLICATE_FRAME_MAPPING')
    if set(assigned)!=set(f): e.append('FRAME_MAPPING_MISMATCH')
    if len({s.get('id') for s in sheets})!=len(sheets): e.append('DUPLICATE_SHEET_ID')
    if not set(d.get('hero_ids',[])).issubset(set(f)): e.append('HERO_FRAME_NOT_DECLARED')
    c=d.get('character',{})
    a=c.get('approval')
    active=c.get('state')=='CHARACTER_SHEET_ACTIVE' and H(c.get('sha256')) and isinstance(a,dict) and a.get('role')=='PRODUCT_OWNER' and a.get('approved') is True and a.get('asset_sha256')==c.get('sha256')
    ready={'READY_FOR_GEM_B','READY_FOR_VISUAL_OWNER_REVIEW','FULL_PRODUCTION_UNLOCKED','READY_FOR_ENGINE'}
    if d.get('status') in ready and not active: e.append('CHARACTER_APPROVAL_MISSING_OR_STALE')
    if d.get('status') in ready and d.get('blocking_issues'): e.append('BLOCKING_ISSUES_PRESENT')
    if d.get('status') in {'FULL_PRODUCTION_UNLOCKED','READY_FOR_ENGINE'}:
        h=d.get('hero_approval')
        if not isinstance(h,dict) or h.get('role')!='PRODUCT_OWNER' or h.get('approved') is not True or not H(h.get('asset_sha256')): e.append('HERO_APPROVAL_REQUIRED')
    return sorted(set(e))
if __name__=='__main__':
    result=validate(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8')))
    print(json.dumps({'passed':not bool(result),'errors':result},indent=2))
    sys.exit(bool(result))
