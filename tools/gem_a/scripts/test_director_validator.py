"""Actual black-box regression tests for GEM A official validator."""
from pathlib import Path
import tempfile, shutil, subprocess, sys, json, hashlib
SOURCE=Path(__file__).with_name('validate_director_package.py')

def dump(path, data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n' if not isinstance(data,str) else data,encoding='utf-8')

def fixture(root):
    script=root/'plugin/scripts/validate_director_package.py'
    script.parent.mkdir(parents=True);shutil.copyfile(SOURCE,script)
    dump(root/'plugin/knowledge/OUTPUT_REGISTRY.json',{'documents':[{'path':p,'minimum_chars':10,'headings':[]} for p in ('01_PRODUCT/CAPTION_MASTER.md','02_CHARACTER/GLOBAL_CHARACTER_LOCKS.md','03_FRAMES/FRAME_COMMUNICATION_MATRIX.md','03_FRAMES/FRAME_TO_SHEET_MAPPING.md')], 'frame_documents':['01_PRODUCT/CAPTION_MASTER.md','03_FRAMES/FRAME_COMMUNICATION_MATRIX.md','03_FRAMES/FRAME_TO_SHEET_MAPPING.md']})
    pkg=root/'package'
    dump(pkg/'01_PRODUCT/CAPTION_MASTER.md','# Captions\n### F01\nกลับบ้านแล้ว OWNER_LOCKED\n')
    dump(pkg/'02_CHARACTER/GLOBAL_CHARACTER_LOCKS.md','# Locks\nLOCK-01 character identity')
    for p in ['03_FRAMES/FRAME_COMMUNICATION_MATRIX.md','03_FRAMES/FRAME_TO_SHEET_MAPPING.md']:
        dump(pkg/p,'# Records\n### F01\nA distinct and specific frame with a recognizable expression.\n')
    dump(pkg/'project.json',{'set_id':'TEST','package_revision':'1.0.0','frame_count':1,'caption_policy':'CAPTION','hero_ids':['F01'],'source_snapshot':{'repository':'x/y','ref':'main','commit':'a'*40},'dependencies':[]})
    dump(pkg/'frames.json',[{'id':'F01','caption':'กลับบ้านแล้ว','caption_policy':'CAPTION','caption_lock':'OWNER_LOCKED','intent':'returns home','chat_situation':'greeting','tone':'humorous','expression':'smiling','pose':'waving','composition':'half body','one_second_expectation':'happy cadet','sheet_id':'S01','row':1,'column':1,'hero':True,'props':[],'forbidden_distractions':[],'character_lock_ids':['LOCK-01']}])
    dump(pkg/'references.json',[{'id':'CHAR','roles':['IDENTITY'],'authority':'PRIMARY','authorization_evidence':'owner approved','availability':'EXTERNAL'}])
    dump(pkg/'approvals.json',{'decisions':[{'id':'OWNER-01','scope':'character','evidence':'approved'}],'character':{'approved':True,'role':'PRODUCT_OWNER','decision_ref':'OWNER-01','asset_sha256':'b'*64}})
    rebuild_manifest(pkg)
    return script,pkg

def rebuild_manifest(pkg):
    data=json.loads((pkg/'project.json').read_text())
    paths=sorted(x for x in pkg.rglob('*') if x.is_file() and x.name!='PACKAGE_MANIFEST.json')
    dump(pkg/'PACKAGE_MANIFEST.json',{'set_id':data['set_id'],'package_revision':data['package_revision'],'standard_version':'1.0.0','payload_file_count':len(paths),'total_archive_entry_count':len(paths)+1,'files':[{'path':p.relative_to(pkg).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]})

def check(script,pkg):
    run=subprocess.run([sys.executable,str(script),str(pkg),'--gate','a1'],capture_output=True,text=True)
    return run.returncode,json.loads(run.stdout)

with tempfile.TemporaryDirectory() as temp:
    script,pkg=fixture(Path(temp))
    code,result=check(script,pkg)
    assert code==0 and result['a1_ready'] and not result['errors'],result
    print('PASS: owner runtime EXTERNAL reference allowed at A1')
    p=pkg/'02_CHARACTER/GLOBAL_CHARACTER_LOCKS.md';p.write_text(p.read_text()+'\ntamper',encoding='utf-8')
    code,result=check(script,pkg)
    assert code!=0 and 'MANIFEST_FILE_HASH_INVALID' in [x['code'] for x in result['errors']],result
    print('PASS: tampered SHA rejected')
    p.write_text('# Locks\nLOCK-01 character identity',encoding='utf-8')
    (pkg/'03_FRAMES/FRAME_TO_SHEET_MAPPING.md').unlink()
    code,result=check(script,pkg)
    assert code!=0 and any(x['code']=='MISSING_DOCUMENT' for x in result['errors']),result
    print('PASS: missing document rejected')
print('A_VALIDATOR_INTEGRATION_TESTS_PASS: 3/3')
