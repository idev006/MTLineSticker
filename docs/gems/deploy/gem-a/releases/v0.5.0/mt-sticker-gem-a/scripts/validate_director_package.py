#!/usr/bin/env python3
"""Offline GEM A document/integrity checks. Does not certify semantic or visual quality."""
from pathlib import Path
import argparse, hashlib, json, re

REGISTRY = Path(__file__).resolve().parents[1] / 'knowledge' / 'OUTPUT_REGISTRY.json'
SHA = re.compile(r'^[0-9a-f]{64}$', re.I)
COMMIT = re.compile(r'^[0-9a-f]{40}$', re.I)
PLACEHOLDER = re.compile(r'\b(?:TODO|TBD|FIXME|lorem ipsum|same as above)\b|ใส่ข้อมูลที่นี่|เหมือนข้างต้น', re.I)
FRAME_HEADING = re.compile(r'^#{1,6}\s+(F\d{2,})\s*$', re.M)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def contained(root, value):
    if not isinstance(value, str) or not value or '\\' in value:
        return None
    rel = Path(value)
    if rel.is_absolute() or '..' in rel.parts:
        return None
    candidate = root / rel
    if any(part.is_symlink() for part in [candidate, *candidate.parents] if part != root.parent):
        return None
    return candidate if candidate.resolve().is_relative_to(root.resolve()) else None

def validate(root):
    root = Path(root).resolve()
    registry = json.loads(REGISTRY.read_text(encoding='utf-8'))
    errors, blockers = [], []
    texts = {}
    def err(code, path='', detail=''):
        errors.append({'code':code, 'path':path, 'detail':str(detail)})
    def block(code):
        if code not in blockers:
            blockers.append(code)
    def load(name, kind):
        p = contained(root, name)
        if p is None or not p.is_file():
            err('MISSING_FILE', name)
            return kind()
        try:
            value = json.loads(p.read_text(encoding='utf-8-sig'))
            if not isinstance(value, kind):
                raise ValueError('wrong top-level type')
            return value
        except (ValueError, OSError) as ex:
            err('INVALID_JSON', name, ex)
            return kind()
    for spec in registry['documents']:
        name = spec['path']; path = contained(root, name)
        if path is None or not path.is_file():
            err('MISSING_DOCUMENT', name); continue
        try:
            text = path.read_text(encoding='utf-8-sig')
        except (OSError, UnicodeError) as ex:
            err('UNREADABLE_DOCUMENT', name, ex); continue
        texts[name] = text
        if len(text.strip()) < spec['minimum_chars']:
            err('DOCUMENT_TOO_SHORT', name)
        if PLACEHOLDER.search(text):
            err('PLACEHOLDER_CONTENT', name)
        headings = list(re.finditer(r'^#{1,6}\s+(.+?)\s*$', text, re.M))
        for title in spec['headings']:
            found = [i for i,h in enumerate(headings) if h.group(1) == title]
            if len(found) != 1:
                err('REQUIRED_HEADING_MISSING_OR_DUPLICATE', name, title); continue
            i = found[0]; start = headings[i].end(); end = headings[i+1].start() if i+1 < len(headings) else len(text)
            # Parent sections may contain child headings, but must contain concrete prose somewhere.
            tail = text[start:end]
            if not tail.strip() and i+1 < len(headings) and len(headings[i+1].group(0).split()[0]) > len(headings[i].group(0).split()[0]):
                j=i+1
                while j<len(headings) and len(headings[j].group(0).split()[0])>len(headings[i].group(0).split()[0]):
                    j+=1
                tail=text[start:headings[j].start() if j<len(headings) else len(text)]
                tail=re.sub(r'^#{1,6}.*$', '', tail, flags=re.M)
            if len(tail.strip()) < 20:
                err('EMPTY_OR_THIN_SECTION', name, title)
    project = load('project.json', dict)
    frames = load('frames.json', list)
    refs = load('references.json', list)
    approvals = load('approvals.json', dict)
    manifest = load('PACKAGE_MANIFEST.json', dict)
    for k in ['set_id','package_revision','frame_count','caption_policy','hero_ids','source_snapshot','dependencies']:
        if k not in project:
            err('PROJECT_FIELD_MISSING','project.json',k)
    for key in ['set_id','package_revision']:
        if not isinstance(project.get(key),str) or not project[key].strip():
            err('PROJECT_IDENTITY_INVALID','project.json',key)
    n = project.get('frame_count')
    if not isinstance(n,int) or isinstance(n,bool) or n < 1 or n > 999:
        err('INVALID_FRAME_COUNT','project.json'); n=0
    expected = [f'F{i:02d}' for i in range(1,n+1)]
    if project.get('caption_policy') not in ['CAPTION','NO_CAPTION','MIXED']:
        err('INVALID_CAPTION_POLICY','project.json')
    actual, slots, hero_flags = [], [], []
    captions={}
    required_text = ['id','intent','chat_situation','tone','expression','pose','composition','one_second_expectation','sheet_id']
    lock_text=texts.get('02_CHARACTER/GLOBAL_CHARACTER_LOCKS.md','')
    for i,f in enumerate(frames):
        if not isinstance(f,dict):
            err('INVALID_FRAME','frames.json',i); continue
        fid=f.get('id'); actual.append(fid)
        if not isinstance(fid,str):
            err('FRAME_ID_INVALID','frames.json',i); continue
        for k in required_text:
            v=f.get(k)
            if not isinstance(v,str) or not v.strip() or PLACEHOLDER.search(v):
                err('FRAME_FIELD_INVALID',str(fid),k)
        for k in ['props','forbidden_distractions','character_lock_ids']:
            v=f.get(k)
            if not isinstance(v,list) or any(not isinstance(x,str) or not x.strip() for x in v) or (k=='character_lock_ids' and not v):
                err('FRAME_LIST_INVALID',str(fid),k)
        for lock in f.get('character_lock_ids',[]) if isinstance(f.get('character_lock_ids'),list) else []:
            if isinstance(lock,str) and not re.search(r'(?<![\w-])'+re.escape(lock)+r'(?![\w-])',lock_text):
                err('UNKNOWN_CHARACTER_LOCK',str(fid),lock)
        policy=f.get('caption_policy'); caption=f.get('caption'); state=f.get('caption_lock')
        if policy=='NO_CAPTION':
            if caption is not None or state!='NO_CAPTION':
                err('NO_CAPTION_CONFLICT',str(fid))
        elif policy=='CAPTION':
            if not isinstance(caption,str) or not caption.strip() or state not in ['OWNER_LOCKED','PROPOSED']:
                err('CAPTION_INVALID',str(fid))
            elif caption in captions and not f.get('repetition_rationale'):
                err('UNEXPLAINED_REPEATED_CAPTION',str(fid))
            else:
                captions[caption]=fid
        else:
            err('FRAME_CAPTION_POLICY_INVALID',str(fid))
        if project.get('caption_policy') in ['CAPTION','NO_CAPTION'] and policy!=project['caption_policy']:
            err('GLOBAL_CAPTION_POLICY_CONFLICT',str(fid))
        row,col=f.get('row'),f.get('column')
        if type(row) is not int or type(col) is not int or row not in (1,2) or col not in (1,2,3,4):
            err('INVALID_SLOT',str(fid))
        slot=(f.get('sheet_id'),row,col)
        if slot in slots:
            err('DUPLICATE_SLOT',str(fid))
        slots.append(slot)
        wanted=(f'S{i//8+1:02d}',(i%8)//4+1,i%4+1)
        if slot!=wanted:
            err('MAPPING_ORDER_MISMATCH',str(fid),wanted)
        if type(f.get('hero')) is not bool:
            err('HERO_FLAG_INVALID',str(fid))
        elif f['hero']:
            hero_flags.append(fid)
    if actual != expected:
        err('FRAME_IDS_COUNT_OR_ORDER_MISMATCH','frames.json')
    hero_ids=project.get('hero_ids')
    if not isinstance(hero_ids,list) or not hero_ids or hero_ids!=hero_flags:
        err('HERO_MAPPING_MISMATCH','project.json')
    for name in registry['frame_documents']:
        text=texts.get(name,'')
        if FRAME_HEADING.findall(text)!=expected:
            err('FRAME_DOCUMENT_IDS_MISMATCH',name)
    captext=texts.get('01_PRODUCT/CAPTION_MASTER.md','')
    sections={}
    matches=list(FRAME_HEADING.finditer(captext))
    for i,m in enumerate(matches):
        sections[m.group(1)]=captext[m.end():matches[i+1].start() if i+1<len(matches) else len(captext)]
    for f in frames:
        if not isinstance(f,dict) or not isinstance(f.get('id'),str): continue
        text=sections.get(f.get('id'),'')
        value=f.get('caption') if f.get('caption_policy')=='CAPTION' else 'NO_CAPTION'
        if not isinstance(value,str) or value not in text or str(f.get('caption_lock')) not in text:
            err('CAPTION_MASTER_MISMATCH',str(f.get('id')))
    ref_ids=[]
    for r in refs:
        if not isinstance(r,dict):
            err('INVALID_REFERENCE','references.json');continue
        rid=r.get('id');ref_ids.append(rid)
        if not isinstance(rid,str) or not rid:
            err('REFERENCE_ID_INVALID','references.json')
        roles=r.get('roles')
        if not isinstance(roles,list) or not roles or any(x not in ['IDENTITY','STYLE','WARDROBE','ACCESSORY','POSE','ENVIRONMENT','OTHER'] for x in roles):
            err('REFERENCE_ROLE_INVALID',str(rid))
        if r.get('authority') not in ['PRIMARY','SECONDARY','OPTIONAL','EXCLUDED','UNRESOLVED']:
            err('REFERENCE_AUTHORITY_INVALID',str(rid))
        if not isinstance(r.get('authorization_evidence'),str) or not r['authorization_evidence'].strip():
            err('REFERENCE_AUTHORIZATION_MISSING',str(rid))
        availability=r.get('availability')
        if availability=='PACKAGED':
            path=contained(root,r.get('path'))
            if path is None or not path.is_file(): err('REFERENCE_FILE_MISSING',str(rid))
            elif digest(path)!=r.get('sha256'): err('REFERENCE_HASH_MISMATCH',str(rid))
        elif availability not in ['EXTERNAL','MISSING']:
            err('REFERENCE_AVAILABILITY_INVALID',str(rid))
        if r.get('authority')=='UNRESOLVED' or (availability!='PACKAGED' and r.get('authority') in ['PRIMARY','SECONDARY']):
            block('REFERENCE_UNRESOLVED_OR_UNAVAILABLE:'+str(rid))
    if len(set(str(x) for x in ref_ids))!=len(ref_ids):
        err('DUPLICATE_REFERENCE_ID','references.json')
    decisions=approvals.get('decisions')
    if not isinstance(decisions,list):
        err('DECISIONS_INVALID','approvals.json');decisions=[]
    decision_ids=[]
    for d in decisions:
        if not isinstance(d,dict) or any(not isinstance(d.get(k),str) or not d[k].strip() for k in ['id','evidence','scope']):
            err('DECISION_EVIDENCE_INVALID','approvals.json');continue
        decision_ids.append(d['id'])
    if len(set(decision_ids))!=len(decision_ids): err('DUPLICATE_DECISION_ID','approvals.json')
    char_ok=False
    for stage in ['character','hero','release']:
        if stage not in approvals:
            err('APPROVAL_STAGE_MISSING','approvals.json',stage)
        a=approvals.get(stage)
        if a is None: continue
        if not isinstance(a,dict):
            err('APPROVAL_INVALID','approvals.json',stage);continue
        file=contained(root,a.get('asset_path'))
        ok=(a.get('approved') is True and a.get('role')=='PRODUCT_OWNER' and a.get('decision_ref') in decision_ids and isinstance(a.get('asset_sha256'),str) and SHA.fullmatch(a['asset_sha256']) and file is not None and file.is_file() and digest(file)==a['asset_sha256'])
        if ok:
            if file.suffix.lower() not in ['.png','.jpg','.jpeg','.webp']:
                ok=False
            else:
                try:
                    from PIL import Image
                    with Image.open(file) as im:
                        if min(im.size)<16: ok=False
                        im.verify()
                except ImportError:
                    ok=False; block('PILLOW_REQUIRED_TO_VERIFY_APPROVAL_IMAGE')
                except Exception:
                    ok=False
        if not ok: err('APPROVAL_MISSING_OR_STALE_ASSET',stage)
        if stage=='character': char_ok=bool(ok)
    if not char_ok: block('CHARACTER_APPROVAL_REQUIRED')
    snap=project.get('source_snapshot',{})
    if not isinstance(snap,dict):
        err('SOURCE_SNAPSHOT_INVALID','project.json');snap={}
    if not all(k in snap for k in ['repository','ref','commit']):
        err('SOURCE_SNAPSHOT_FIELDS_MISSING','project.json')
    if not isinstance(snap.get('commit'),str) or not COMMIT.fullmatch(snap['commit']):
        block('SOURCE_COMMIT_NOT_PINNED')
    deps=project.get('dependencies')
    if not isinstance(deps,list):
        err('DEPENDENCIES_INVALID','project.json');deps=[]
    for d in deps:
        if not isinstance(d,dict) or any(not d.get(k) for k in ['id','status','impact','owner','next_action']):
            err('DEPENDENCY_INVALID','project.json');continue
        if d['status'] not in ['OPEN','RESOLVED']:
            err('DEPENDENCY_STATUS_INVALID','project.json')
        if d['status']=='OPEN': block('DEPENDENCY_OPEN:'+str(d['id']))
    if n%8:
        policy=project.get('partial_sheet_policy')
        if not isinstance(policy,dict) or policy.get('owner_approved') is not True or policy.get('decision_ref') not in decision_ids or not policy.get('strategy'):
            block('PARTIAL_SHEET_POLICY_REQUIRED')
    paths=[]
    records=manifest.get('files')
    if not isinstance(records,list):
        err('MANIFEST_FILES_INVALID','PACKAGE_MANIFEST.json');records=[]
    for item in records:
        if not isinstance(item,dict):
            err('MANIFEST_ENTRY_INVALID');continue
        name=item.get('path');paths.append(name);file=contained(root,name)
        if name=='PACKAGE_MANIFEST.json' or file is None or not file.is_file():
            err('MANIFEST_PATH_INVALID',str(name))
        elif digest(file)!=item.get('sha256'):
            err('MANIFEST_HASH_MISMATCH',str(name))
    actual_paths=[]
    if root.is_dir():
        for f in root.rglob('*'):
            if f.is_symlink(): err('SYMLINK_FORBIDDEN',str(f.relative_to(root)))
            elif f.is_file() and f.name!='PACKAGE_MANIFEST.json': actual_paths.append(f.relative_to(root).as_posix())
    if len(set(str(x) for x in paths))!=len(paths) or set(str(x) for x in paths)!=set(actual_paths):
        err('MANIFEST_INVENTORY_MISMATCH','PACKAGE_MANIFEST.json')
    if manifest.get('payload_file_count')!=len(actual_paths) or manifest.get('total_archive_entry_count')!=len(actual_paths)+1:
        err('MANIFEST_COUNTS_MISMATCH','PACKAGE_MANIFEST.json')
    if manifest.get('standard_version')!='1.0.0' or any(manifest.get(k)!=project.get(k) for k in ['set_id','package_revision']):
        err('MANIFEST_METADATA_MISMATCH','PACKAGE_MANIFEST.json')
    required_count=len(registry['documents'])+len(registry['structured_files'])
    return {'validator_version':'1.0.0','set_id':project.get('set_id'),'required_file_count':required_count,'payload_file_count':len(actual_paths),'document_complete':not errors,'ready_for_gem_b':not errors and not blockers,'errors':errors,'readiness_blockers':blockers,'semantic_review':'NOT_CERTIFIED','image_pixel_qa':'NOT_RUN','legacy_contract_compatibility':'NOT_CERTIFIED'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('package',type=Path);parser.add_argument('--report',type=Path);parser.add_argument('--require',choices=['documents','ready'],default='documents')
    args=parser.parse_args()
    if args.report and args.report.resolve().is_relative_to(args.package.resolve()):
        parser.error('--report must be outside package to avoid circular manifests')
    report=validate(args.package)
    text=json.dumps(report,ensure_ascii=False,indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(text+'\n',encoding='utf-8')
    print(text)
    return 0 if report['ready_for_gem_b' if args.require=='ready' else 'document_complete'] else 1

if __name__=='__main__':
    raise SystemExit(main())
