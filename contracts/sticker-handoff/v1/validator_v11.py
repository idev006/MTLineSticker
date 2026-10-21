"""MTLineSticker Handoff Validator v1.1: strict offline evidence checks."""
import hashlib,json,re,sys
from pathlib import Path
SHA40=re.compile(r"^[0-9a-fA-F]{40}$")
SHA64=re.compile(r"^[0-9a-fA-F]{64}$")
READY={"READY_FOR_GEM_B","READY_FOR_VISUAL_OWNER_REVIEW","FULL_PRODUCTION_UNLOCKED","READY_FOR_ENGINE"}
FULL={"FULL_PRODUCTION_UNLOCKED","READY_FOR_ENGINE"}
NEXT={"NOT_READY":{"NOT_READY","READY_FOR_GEM_B"},"READY_FOR_GEM_B":{"READY_FOR_GEM_B","READY_FOR_VISUAL_OWNER_REVIEW"},"READY_FOR_VISUAL_OWNER_REVIEW":{"READY_FOR_VISUAL_OWNER_REVIEW","FULL_PRODUCTION_UNLOCKED","READY_FOR_GEM_B"},"FULL_PRODUCTION_UNLOCKED":{"FULL_PRODUCTION_UNLOCKED","READY_FOR_ENGINE"},"READY_FOR_ENGINE":{"READY_FOR_ENGINE"}}
def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for block in iter(lambda:f.read(1048576),b""):h.update(block)
    return h.hexdigest()
def local(root,path):
    if not isinstance(path,str) or not path or Path(path).is_absolute() or "\\" in path:return None
    p=(root/path).resolve()
    return p if p.is_relative_to(root.resolve()) else None
def validate_v11(d,root,previous=None,expected_commit=None):
    root=Path(root).resolve();errors=[]
    def fail(code):errors.append(code)
    if d.get("contract_version")!="1.0.0":fail("CONTRACT_VERSION_UNSUPPORTED")
    if not SHA40.fullmatch(str(d.get("source_commit",""))):fail("SOURCE_COMMIT_INVALID")
    if expected_commit is not None and d.get("source_commit")!=expected_commit:fail("SSOT_VERSION_CONFLICT")
    frames=d.get("frames",[]);sheets=d.get("sheets",[])
    if not isinstance(frames,list) or not frames or len(frames)!=len(set(map(str,frames))):fail("FRAME_IDS_INVALID");frames=frames if isinstance(frames,list) else []
    if not isinstance(sheets,list):fail("SHEETS_INVALID");sheets=[]
    actual=[];ids=[]
    for item in sheets:
        if not isinstance(item,dict) or not isinstance(item.get("frame_ids"),list):fail("SHEET_INVALID");continue
        ids.append(item.get("id"));actual.extend(item["frame_ids"])
    if len(ids)!=len(set(ids)):fail("DUPLICATE_SHEET_ID")
    if len(actual)!=len(set(map(str,actual))):fail("DUPLICATE_FRAME_MAPPING")
    if set(map(str,frames))!=set(map(str,actual)):fail("FRAME_MAPPING_MISMATCH")
    if not set(d.get("hero_ids",[])).issubset(set(frames)):fail("HERO_FRAME_NOT_DECLARED")
    for asset in d.get("assets",[]):
        p=local(root,asset.get("path"))
        if p is None:fail("ASSET_UNSAFE_PATH")
        elif not p.is_file():fail("ASSET_MISSING")
        elif sha256(p)!=asset.get("sha256"):fail("ASSET_HASH_MISMATCH")
    c=d.get("character",{});approval=c.get("approval") if isinstance(c.get("approval"),dict) else {}
    ok=c.get("state")=="CHARACTER_SHEET_ACTIVE" and SHA64.fullmatch(str(c.get("sha256",""))) and approval.get("role")=="PRODUCT_OWNER" and approval.get("approved") is True and bool(approval.get("approval_id")) and approval.get("asset_sha256")==c.get("sha256")
    if d.get("status") in READY:
        if not ok:fail("CHARACTER_APPROVAL_MISSING_OR_STALE")
        p=local(root,c.get("asset_path"))
        if p is None or not p.is_file():fail("CHARACTER_ASSET_MISSING")
        elif sha256(p)!=c.get("sha256"):fail("CHARACTER_ASSET_HASH_MISMATCH")
        p=local(root,d.get("package_path"))
        if p is None or not p.is_file():fail("PACKAGE_ASSET_MISSING")
        elif sha256(p)!=d.get("package_manifest_sha256"):fail("PACKAGE_HASH_MISMATCH")
        if d.get("blocking_issues"):fail("BLOCKING_ISSUES_PRESENT")
    if d.get("status") in FULL:
        h=d.get("hero_approval") if isinstance(d.get("hero_approval"),dict) else {}
        if not (h.get("role")=="PRODUCT_OWNER" and h.get("approved") is True and bool(h.get("approval_id")) and SHA64.fullmatch(str(h.get("asset_sha256","")))):fail("HERO_APPROVAL_REQUIRED")
        p=local(root,h.get("asset_path"))
        if p is None or not p.is_file():fail("HERO_ASSET_MISSING")
        elif sha256(p)!=h.get("asset_sha256"):fail("HERO_ASSET_HASH_MISMATCH")
    if previous is not None:
        if d.get("status") not in NEXT.get(previous.get("status"),set()):fail("ILLEGAL_STATE_TRANSITION")
        if previous.get("character",{}).get("sha256")!=c.get("sha256") and d.get("status") in READY:fail("CHARACTER_CHANGED_REAPPROVAL_REQUIRED")
    return sorted(set(errors))
if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser();p.add_argument("handoff");p.add_argument("--root",default=".");p.add_argument("--previous");p.add_argument("--expected-commit");args=p.parse_args()
    d=json.loads(Path(args.handoff).read_text(encoding="utf-8"))
    previous=json.loads(Path(args.previous).read_text(encoding="utf-8")) if args.previous else None
    errors=validate_v11(d,args.root,previous=previous,expected_commit=args.expected_commit)
    print(json.dumps({"passed":not errors,"errors":errors},indent=2))
    sys.exit(bool(errors))
