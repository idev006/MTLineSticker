"""Fixture tests for handoff validator v1.1. Run: python -m unittest discover -s tests/contracts"""
import hashlib,importlib.util,tempfile,unittest
from pathlib import Path
SOURCE=Path(__file__).resolve().parents[2]/"contracts/sticker-handoff/v1/validator_v11.py"
spec=importlib.util.spec_from_file_location("mt_validator_v11",SOURCE)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class ContractV11Tests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
  for n in ("character.png","package.zip","hero.png"):(self.root/n).write_bytes(n.encode())
  f=[f"F{i:02}" for i in range(1,41)]
  ch=digest(self.root/"character.png")
  self.d={"contract_version":"1.0.0","source_commit":"a"*40,"status":"READY_FOR_GEM_B","package_path":"package.zip","package_manifest_sha256":digest(self.root/"package.zip"),"frames":f,"sheets":[{"id":str(i),"frame_ids":f[i*8:(i+1)*8]} for i in range(5)],"hero_ids":["F01","F06","F18","F19"],"blocking_issues":[],"assets":[],"character":{"asset_path":"character.png","sha256":ch,"state":"CHARACTER_SHEET_ACTIVE","approval":{"approval_id":"test","role":"PRODUCT_OWNER","approved":True,"asset_sha256":ch}}}
 def check(self,**kw):return module.validate_v11(self.d,self.root,**kw)
 def test_valid(self):self.assertEqual(self.check(),[])
 def test_missing_frame(self):self.d["sheets"][2]["frame_ids"].pop();self.assertIn("FRAME_MAPPING_MISMATCH",self.check())
 def test_duplicate_frame(self):self.d["sheets"][0]["frame_ids"].append("F09");self.assertIn("DUPLICATE_FRAME_MAPPING",self.check())
 def test_character_missing(self):(self.root/"character.png").unlink();self.assertIn("CHARACTER_ASSET_MISSING",self.check())
 def test_character_hash(self):(self.root/"character.png").write_bytes(b"changed");self.assertIn("CHARACTER_ASSET_HASH_MISMATCH",self.check())
 def test_package_hash(self):(self.root/"package.zip").write_bytes(b"changed");self.assertIn("PACKAGE_HASH_MISMATCH",self.check())
 def test_hero_gate(self):self.d["status"]="FULL_PRODUCTION_UNLOCKED";self.assertIn("HERO_APPROVAL_REQUIRED",self.check())
 def test_hero_approval(self):
  self.d["status"]="FULL_PRODUCTION_UNLOCKED";self.d["hero_approval"]={"approval_id":"h","role":"PRODUCT_OWNER","approved":True,"asset_path":"hero.png","asset_sha256":digest(self.root/"hero.png")};self.assertEqual(self.check(),[])
 def test_path_traversal(self):self.d["assets"]=[{"path":"../secret","sha256":"a"*64}];self.assertIn("ASSET_UNSAFE_PATH",self.check())
 def test_missing_asset(self):self.d["assets"]=[{"path":"missing.png","sha256":"a"*64}];self.assertIn("ASSET_MISSING",self.check())
 def test_version_conflict(self):self.assertIn("SSOT_VERSION_CONFLICT",self.check(expected_commit="b"*40))
 def test_transition_skip(self):self.assertIn("ILLEGAL_STATE_TRANSITION",self.check(previous={"status":"NOT_READY","character":self.d["character"]}) if False else module.validate_v11(dict(self.d,status="READY_FOR_ENGINE"),self.root,previous=self.d))
 def test_changed_character(self):self.assertIn("CHARACTER_CHANGED_REAPPROVAL_REQUIRED",self.check(previous={"status":"READY_FOR_GEM_B","character":{"sha256":"0"*64}}))
 def test_unapproved(self):self.d["character"]["approval"]=None;self.assertIn("CHARACTER_APPROVAL_MISSING_OR_STALE",self.check())
if __name__=="__main__":unittest.main()
