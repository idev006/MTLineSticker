#!/usr/bin/env python3
"""Run the official GEM A A1 validator locally; GitHub Actions is optional.
Usage:
  python tools/gem_a/validate_without_actions.py --repo . --write-manifest
  git add sets/SET-KHE-NOI-FIRST-HOME-001/PACKAGE_MANIFEST.json && git commit -m "qa: manifest"
  python tools/gem_a/validate_without_actions.py --repo .
  git add gate-reports/SET-KHE-NOI-FIRST-HOME-001/A1_LATEST.json && git commit -m "qa: A1 evidence"
Run in a clean checkout. Never upload owner image binaries to GitHub.
"""
import argparse, datetime, hashlib, json, pathlib, subprocess, sys
SET="SET-KHE-NOI-FIRST-HOME-001"
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def git(repo,*args):
    return subprocess.run(["git","-C",str(repo),*args],capture_output=True,text=True)
def emit(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def main():
    a=argparse.ArgumentParser()
    a.add_argument("--repo",type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[2])
    a.add_argument("--write-manifest",action="store_true",help="Explicitly rebuild manifest, then commit before validation")
    args=a.parse_args();repo=args.repo.resolve();pkg=repo/"sets"/SET;receipt=repo/"gate-reports"/SET/"A1_LATEST.json"
    official=repo/"tools/gem_a/scripts/validate_director_package.py"
    if not (pkg/"project.json").is_file() or not official.is_file():
        print("MISSING_PROJECT_OR_OFFICIAL_VALIDATOR",file=sys.stderr);return 2
    paths=sorted(x for x in pkg.rglob("*") if x.is_file() and x.name!="PACKAGE_MANIFEST.json")
    if args.write_manifest:
        p=json.loads((pkg/"project.json").read_text(encoding="utf-8"))
        emit(pkg/"PACKAGE_MANIFEST.json",dict(standard_version="1.0.0",set_id=p["set_id"],package_revision=p["package_revision"],payload_file_count=len(paths),total_archive_entry_count=len(paths)+1,files=[dict(path=x.relative_to(pkg).as_posix(),sha256=sha(x)) for x in paths],binary_delivery_policy="OWNER_TO_GEM_B_RUNTIME",binary_in_github_required=False))
        print("MANIFEST_REGENERATED_COMMIT_BEFORE_VALIDATION",len(paths))
        return 0
    head=git(repo,"rev-parse","HEAD")
    if head.returncode!=0 or len(head.stdout.strip())!=40:
        print("GIT_HEAD_REQUIRED",file=sys.stderr);return 2
    dirty=git(repo,"status","--porcelain","--",str(pkg.relative_to(repo)))
    if dirty.returncode or dirty.stdout.strip():
        print("PROJECT_HAS_UNCOMMITTED_CHANGES",file=sys.stderr);return 2
    current=git(repo,"rev-parse","HEAD").stdout.strip()
    v=subprocess.run([sys.executable,str(official),str(pkg),"--gate","a1"],capture_output=True,text=True)
    try:result=json.loads(v.stdout)
    except json.JSONDecodeError:result={"a1_ready":False,"errors":[{"code":"VALIDATOR_CRASH","detail":(v.stdout+" "+v.stderr)[-3000:]}]}
    m=json.loads((pkg/"PACKAGE_MANIFEST.json").read_text(encoding="utf-8"))
    f=json.loads((pkg/"frames.json").read_text(encoding="utf-8"))
    ap=json.loads((pkg/"approvals.json").read_text(encoding="utf-8"))
    pass_gate=v.returncode==0 and result.get("a1_ready") is True and not result.get("errors")
    receipt_data={"schema_version":"2.0","set_id":SET,"gate":"A1","status":"PASS" if pass_gate else "FAIL",
      "validated_source_commit":current,"validator_version":result.get("validator_version","UNKNOWN"),
      "validator_executed":True,"validator_exit_code":v.returncode,
      "manifest_sha256_verified":pass_gate,"manifest_payload_count":m.get("payload_file_count"),
      "caption_master_version":"0.4.0","caption_exact_count":len(f),
      "character_approval_recorded":ap.get("character",{}).get("approved") is True,
      "binary_delivery":"OWNER_TO_GEM_B_RUNTIME","a2_status":"AWAITING_OWNER_ASSETS",
      "errors":result.get("errors",[]),"timestamp_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
      "handoff_authorized":pass_gate,"execution_mode":"OFFLINE_LOCAL_PYTHON_NO_ACTIONS"}
    emit(receipt,receipt_data)
    print(json.dumps({"gate":"A1","status":receipt_data["status"],"source_commit":current,"errors":len(receipt_data["errors"]),"receipt":str(receipt)},ensure_ascii=False))
    return 0 if pass_gate else 1
if __name__=="__main__":sys.exit(main())
