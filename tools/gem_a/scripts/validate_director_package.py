#!/usr/bin/env python3
"""MT Sticker GEM A validator 1.1 — document-only Gate A1. Image bytes checked at GEM B A2."""
from pathlib import Path
import argparse, hashlib, json, re

REGISTRY = Path(__file__).resolve().parents[1] / 'knowledge/OUTPUT_REGISTRY.json'
FRAME = re.compile(r'^#{1,6}\s+(F\d{2})\s*$', re.M)
SHA256 = re.compile(r'^[a-fA-F0-9]{64}$')
SHA40 = re.compile(r'^[a-fA-F0-9]{40}$')

def checksum(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def safe(root, name):
    if not isinstance(name,str) or not name or '\\' in name: return None
    rel=Path(name)
    if rel.is_absolute() or '..' in rel.parts: return None
    p=root/rel
    if not p.resolve().is_relative_to(root.resolve()): return None
    return p

def validate(root, gate='a1'):
    root=Path(root).resolve()
    reg=json.loads(REGISTRY.read_text(encoding='utf8'))
    issues=[]; texts={}
    def error(code, path='', detail=''): issues.append({'code':code,'path':path,'detail':str(detail)})
    def load(name, typ):
        p=safe(root,name)
        if p is None or not p.is_file(): error('MISSING_FILE',name); return typ()
        try:
            obj=json.loads(p.read_text(encoding='utf-8-sig'))
            if not isinstance(obj,typ): raise ValueError('unexpected JSON type')
            return obj
        except (ValueError,UnicodeError) as ex:
            error('INVALID_JSON',name,ex);return typ()
    for item in reg['documents']:
        name=item['path']; p=safe(root,name)
        if p is None or not p.is_file(): error('MISSING_DOCUMENT',name);continue
        text=p.read_text(encoding='utf-8-sig');texts[name]=text
        if len(text.strip())<item['minimum_chars']:error('DOCUMENT_TOO_SHORT',name)
        headings=[m.group(1) for m in re.finditer(r'^#{1,6}\s+(.+?)\s*$',text,re.M)]
        for h in item['headings']:
            if headings.count(h)!=1:error('REQUIRED_HEADING_MISSING_OR_DUPLICATE',name,h)
    p=load('project.json',dict); f=load('frames.json',list); refs=load('references.json',list)
    appr=load('approvals.json',dict); manifest=load('PACKAGE_MANIFEST.json',dict)
    n=p.get('frame_count')
    if not isinstance(n,int) or n<1:error('FRAME_COUNT_INVALID','project.json');n=0
    expected=[f'F{i:02d}' for i in range(1,n+1)]
    if [x.get('id') for x in f if isinstance(x,dict)]!=expected:error('FRAME_IDS_INVALID','frames.json')
    if p.get('caption_policy')!='CAPTION':error('CAPTION_POLICY_INVALID','project.json')
    master=texts.get('01_PRODUCT/CAPTION_MASTER.md','')
    matches=list(FRAME.finditer(master))
    sections={x.group(1):master[x.end():(matches[i+1].start() if i+1<len(matches) else len(master))] for i,x in enumerate(matches)}
    locks=texts.get('02_CHARACTER/GLOBAL_CHARACTER_LOCKS.md','')
    heros=[];caption_seen=set();slots=set()
    for i,item in enumerate(f):
        if not isinstance(item,dict):error('INVALID_FRAME','frames.json',i);continue
        fid=item.get('id',str(i)); cap=item.get('caption')
        required=['intent','chat_situation','tone','expression','pose','composition','one_second_expectation','sheet_id']
        for k in required:
            if not isinstance(item.get(k),str) or not item[k].strip():error('FRAME_FIELD_INVALID',fid,k)
        for k in ['props','forbidden_distractions','character_lock_ids']:
            a=item.get(k)
            if not isinstance(a,list) or (k=='character_lock_ids' and not a):error('FRAME_LIST_INVALID',fid,k)
        for lk in item.get('character_lock_ids',[]):
            if lk not in locks:error('UNKNOWN_CHARACTER_LOCK',fid,lk)
        if item.get('caption_policy')!='CAPTION' or item.get('caption_lock')!='OWNER_LOCKED' or not isinstance(cap,str):error('CAPTION_LOCK_INVALID',fid)
        if isinstance(cap,str):
            if cap in caption_seen:error('CAPTION_DUPLICATED',fid)
            caption_seen.add(cap)
            if cap not in sections.get(fid,'') or 'OWNER_LOCKED' not in sections.get(fid,''):error('CAPTION_MASTER_MISMATCH',fid)
        expected_slot=(f'S{i//8+1:02d}',(i%8)//4+1,i%4+1)
        actual_slot=(item.get('sheet_id'),item.get('row'),item.get('column'))
        if expected_slot!=actual_slot:error('SHEET_MAPPING_INVALID',fid)
        if actual_slot in slots:error('SLOT_DUPLICATED',fid)
        slots.add(actual_slot)
        if item.get('hero') is True:heros.append(fid)
    if heros!=p.get('hero_ids'):error('HERO_MAPPING_INVALID','project.json')
    for name in reg['frame_documents']:
        if FRAME.findall(texts.get(name,''))!=expected:error('FRAME_DOCUMENT_IDS_INVALID',name)
    snap=p.get('source_snapshot',{})
    if not isinstance(snap,dict) or not all(snap.get(x) for x in ['repository','ref','commit']) or not SHA40.fullmatch(str(snap.get('commit',''))):error('SOURCE_COMMIT_INVALID','project.json')
    for dependency in p.get('dependencies',[]):
        if not isinstance(dependency,dict) or any(not dependency.get(k) for k in ['id','status','impact','owner','next_action']):error('DEPENDENCY_SCHEMA_INVALID','project.json')
        elif dependency['status']=='OPEN' and dependency['owner']=='GEM_A':error('UNRESOLVED_A1_DEPENDENCY','project.json')
    decisions=appr.get('decisions',[])
    ids={d.get('id') for d in decisions if isinstance(d,dict)}
    if not isinstance(decisions,list) or len(ids)!=len(decisions):error('DECISIONS_INVALID','approvals.json')
    ch=appr.get('character',{})
    if not isinstance(ch,dict) or ch.get('approved') is not True or ch.get('role')!='PRODUCT_OWNER' or ch.get('decision_ref') not in ids or not SHA256.fullmatch(str(ch.get('asset_sha256',''))):error('CHARACTER_LEDGER_INVALID','approvals.json')
    for item in refs:
        if not isinstance(item,dict) or not item.get('id') or not item.get('roles') or not item.get('authorization_evidence') or item.get('authority') not in ['PRIMARY','SECONDARY','OPTIONAL','EXCLUDED','UNRESOLVED']:error('REFERENCE_METADATA_INVALID','references.json');continue
        if item.get('availability')=='PACKAGED':
            path=safe(root,item.get('path'))
            if path is None or not path.is_file() or checksum(path)!=item.get('sha256'):error('PACKAGED_REFERENCE_INVALID','references.json',item['id'])
        elif item.get('availability')!='EXTERNAL':error('REFERENCE_AVAILABILITY_INVALID','references.json',item['id'])
        # EXTERNAL binaries are explicitly the owner's attachments for GEM B A2.
    listed={}
    for entry in manifest.get('files',[]):
        if not isinstance(entry,dict) or not isinstance(entry.get('path'),str) or not SHA256.fullmatch(str(entry.get('sha256',''))):error('MANIFEST_ENTRY_INVALID','PACKAGE_MANIFEST.json');continue
        name=entry['path']; file=safe(root,name)
        if name in listed:error('MANIFEST_DUPLICATED',name)
        listed[name]=entry['sha256']
        if file is None or not file.is_file() or checksum(file)!=entry['sha256']:error('MANIFEST_FILE_HASH_INVALID',name)
    actual=sorted(x.relative_to(root).as_posix() for x in root.rglob('*') if x.is_file() and x.name!='PACKAGE_MANIFEST.json')
    if sorted(listed)!=actual:error('MANIFEST_INVENTORY_INVALID','PACKAGE_MANIFEST.json')
    if manifest.get('payload_file_count')!=len(actual) or manifest.get('total_archive_entry_count')!=len(actual)+1:error('MANIFEST_COUNT_INVALID','PACKAGE_MANIFEST.json')
    if manifest.get('set_id')!=p.get('set_id') or manifest.get('package_revision')!=p.get('package_revision'):error('MANIFEST_METADATA_INVALID','PACKAGE_MANIFEST.json')
    return {'validator_version':'1.1.0','gate':'A1_DOCUMENT_READINESS','set_id':p.get('set_id'),'a1_ready':not issues,'a2_status':'DEFERRED_TO_GEM_B','errors':issues,'semantic_review':'NOT_CERTIFIED','pixel_qa':'NOT_RUN','runtime_binaries':'NOT_REQUIRED_FOR_A1'}

def main():
    a=argparse.ArgumentParser()
    a.add_argument('package',type=Path);a.add_argument('--gate',choices=['a1'],default='a1');a.add_argument('--report',type=Path);a.add_argument('--require',choices=['documents','ready'],default='documents')
    args=a.parse_args()
    if args.report and args.report.resolve().is_relative_to(args.package.resolve()):a.error('report must be outside package')
    result=validate(args.package,args.gate)
    s=json.dumps(result,ensure_ascii=False,indent=2)
    if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(s+'\n',encoding='utf8')
    print(s);return 0 if result['a1_ready'] else 1
if __name__=='__main__':raise SystemExit(main())
