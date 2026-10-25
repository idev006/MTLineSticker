#!/usr/bin/env python3
"""Regenerate a cryptographic document manifest, run GEM A's real A1 validator and publish only observed results."""
from pathlib import Path
import hashlib, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'sets/SET-KHE-NOI-FIRST-HOME-001'
OUT=ROOT/'gate-reports/SET-KHE-NOI-FIRST-HOME-001/A1_LATEST.json'
def manifest():
    files=sorted(f for f in P.rglob('*') if f.is_file() and f.name!='PACKAGE_MANIFEST.json')
    project=json.loads((P/'project.json').read_text(encoding='utf-8'))
    data=dict(standard_version='1.0.0',set_id=project['set_id'],package_revision=project['package_revision'],payload_file_count=len(files),total_archive_entry_count=len(files)+1,files=[dict(path=f.relative_to(P).as_posix(),sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in files],binary_delivery_policy='OWNER_TO_GEM_B_RUNTIME',binary_in_github_required=False)
    (P/'PACKAGE_MANIFEST.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def run():
    cmd=[sys.executable,str(ROOT/'tools/gem_a/scripts/validate_director_package.py'),str(P),'--gate','a1']
    r=subprocess.run(cmd,capture_output=True,text=True,check=False)
    try:result=json.loads(r.stdout)
    except json.JSONDecodeError:result=dict(a1_ready=False,errors=[dict(code='VALIDATOR_EXECUTION_ERROR',path='',detail=r.stdout+' '+r.stderr)])
    return result
manifest()
result=run()
if result.get('a1_ready') is True:
    project=json.loads((P/'project.json').read_text(encoding='utf-8'))
    handoff=json.loads((P/'handoff.json').read_text(encoding='utf-8'))
    project['status']='A1_READY'
    handoff['status']='A1_READY_A2_DEFERRED_TO_GEM_B'
    handoff['blockers']=['RUNTIME_APPROVED_ASSETS_NOT_YET_VERIFIED_BY_GEM_B']
    (P/'project.json').write_text(json.dumps(project,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (P/'handoff.json').write_text(json.dumps(handoff,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    manifest()
    result=run()
OUT.parent.mkdir(parents=True,exist_ok=True)
result['source']='repository GitHub Actions executing plugin GEM A v0.8.0 validator 1.1'
result['reference_assets']='Owner will attach binaries directly to GEM B at Gate A2'
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
# Commit report even when validator fails; the GitHub Action does the git push.
