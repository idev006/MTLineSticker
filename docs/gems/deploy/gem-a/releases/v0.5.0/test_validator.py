import unittest,tempfile,json,hashlib,importlib.util,copy
from pathlib import Path
P=Path(__file__).parent/'mt-sticker-gem-a'
spec=importlib.util.spec_from_file_location('validator',P/'scripts/validate_director_package.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
registry=json.loads((P/'knowledge/OUTPUT_REGISTRY.json').read_text())
def write(root,name,data):
 p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2) if not isinstance(data,str) else data)
def seal(root):
 m={'standard_version':'1.0.0','set_id':'SET-TEST','package_revision':'1.0.0','files':[]}
 for f in sorted(root.rglob('*')):
  if f.is_file() and f.name!='PACKAGE_MANIFEST.json':m['files'].append({'path':f.relative_to(root).as_posix(),'sha256':v.digest(f)})
 m['payload_file_count']=len(m['files']);m['total_archive_entry_count']=len(m['files'])+1;write(root,'PACKAGE_MANIFEST.json',m)
def fixture(root):
 for d in registry['documents']:
  content='# Fixture for structural contract testing\n'
  for h in d['headings']:content+='\n## '+h+'\nConcrete fixture evidence for this section describes its scoped input, intended outcome and verification responsibility.\n'
  if not d['headings']:content+='Create a consistent character candidate from the supplied identity references, matching the proportions and specified views. Preserve the uniform and neutral background.'
  if d['path']=='02_CHARACTER/GLOBAL_CHARACTER_LOCKS.md':content+='\nLOCK-01: Preserve the character head anatomy in every frame.\n'
  if d['path'] in registry['frame_documents']:
   for i in range(1,41):content+=f'\n### F{i:02d}\nConcrete fixture frame {i} expresses a unique situation with text Message {i} and PROPOSED caption lock.\n'
  write(root,d['path'],content)
 frames=[{'id':f'F{i:02d}','caption':f'Message {i}','caption_policy':'CAPTION','caption_lock':'PROPOSED','intent':f'Intent {i}','chat_situation':f'Situation {i}','tone':'friendly','expression':'smiling','pose':'standing','props':[],'composition':'full body','forbidden_distractions':[],'one_second_expectation':'understand the reaction','character_lock_ids':['LOCK-01'],'hero':i==1,'sheet_id':f'S{(i-1)//8+1:02d}','row':((i-1)%8)//4+1,'column':(i-1)%4+1} for i in range(1,41)]
 write(root,'frames.json',frames)
 write(root,'project.json',{'set_id':'SET-TEST','package_revision':'1.0.0','frame_count':40,'caption_policy':'CAPTION','hero_ids':['F01'],'source_snapshot':{'repository':'test','ref':'fixture','commit':'a'*40},'dependencies':[]})
 write(root,'references.json',[]);write(root,'approvals.json',{'decisions':[],'character':None,'hero':None,'release':None});seal(root)
class Tests(unittest.TestCase):
 def setUp(self):self.temp=tempfile.TemporaryDirectory();self.r=Path(self.temp.name);fixture(self.r)
 def tearDown(self):self.temp.cleanup()
 def read(self,n):return json.loads((self.r/n).read_text())
 def check(self,code):self.assertIn(code,[e['code'] for e in v.validate(self.r)['errors']])
 def test_complete_docs_do_not_approve_character(self):
  result=v.validate(self.r);self.assertTrue(result['document_complete'],result);self.assertFalse(result['ready_for_gem_b']);self.assertIn('CHARACTER_APPROVAL_REQUIRED',result['readiness_blockers'])
 def test_missing_document(self):
  (self.r/'02_CHARACTER/CHARACTER_BIBLE.md').unlink();seal(self.r);self.check('MISSING_DOCUMENT')
 def test_empty_section(self):
  write(self.r,'00_PROJECT/STATUS.md','# Fixture\n## Document completeness\n\n## Character gate\nEnough concrete fixture text for gate.\n## Hero gate\nEnough concrete fixture text for gate.\n## Production gate\nEnough concrete fixture text for gate.');seal(self.r);self.check('EMPTY_OR_THIN_SECTION')
 def test_placeholder(self):
  with (self.r/'00_PROJECT/STATUS.md').open('a') as f:f.write('\nTODO fill details\n')
  seal(self.r);self.check('PLACEHOLDER_CONTENT')
 def test_duplicate_id(self):
  f=self.read('frames.json');f[2]['id']='F01';write(self.r,'frames.json',f);seal(self.r);self.check('FRAME_IDS_COUNT_OR_ORDER_MISMATCH')
 def test_duplicate_slot(self):
  f=self.read('frames.json');f[1]['column']=1;write(self.r,'frames.json',f);seal(self.r);self.check('DUPLICATE_SLOT')
 def test_missing_communication_field(self):
  f=self.read('frames.json');del f[0]['chat_situation'];write(self.r,'frames.json',f);seal(self.r);self.check('FRAME_FIELD_INVALID')
 def test_caption_drift(self):
  f=self.read('frames.json');f[0]['caption']='Changed exact words';write(self.r,'frames.json',f);seal(self.r);self.check('CAPTION_MASTER_MISMATCH')
 def test_missing_frame_in_doc(self):
  p=self.r/'03_FRAMES/FRAME_COMMUNICATION_MATRIX.md';p.write_text(p.read_text().replace('### F13','### OMITTED'));seal(self.r);self.check('FRAME_DOCUMENT_IDS_MISMATCH')
 def test_unknown_character_lock(self):
  f=self.read('frames.json');f[0]['character_lock_ids']=['LOCK-99'];write(self.r,'frames.json',f);seal(self.r);self.check('UNKNOWN_CHARACTER_LOCK')
 def test_hash_tampering(self):
  with (self.r/'README_FIRST.md').open('a') as f:f.write('modified after manifest')
  self.check('MANIFEST_HASH_MISMATCH')
 def test_external_reference_blocks_readiness(self):
  write(self.r,'references.json',[{'id':'R1','roles':['IDENTITY'],'authority':'PRIMARY','authorization_evidence':'Fixture owner supplied image','availability':'EXTERNAL','path':None,'sha256':None}]);seal(self.r);self.assertIn('REFERENCE_UNRESOLVED_OR_UNAVAILABLE:R1',v.validate(self.r)['readiness_blockers'])
 def test_stale_approval(self):
  write(self.r,'approvals.json',{'decisions':[{'id':'D1','evidence':'Fixture owner approval only for tests','scope':'Character fixture'}],'character':{'approved':True,'role':'PRODUCT_OWNER','decision_ref':'D1','asset_path':'absent.png','asset_sha256':'b'*64},'hero':None,'release':None});seal(self.r);self.check('APPROVAL_MISSING_OR_STALE_ASSET')
 def test_fully_pinned_fixture_is_structurally_ready(self):
  # Synthetic image and receipt are unit-test fixtures, not real owner approvals.
  from PIL import Image
  (self.r/'assets').mkdir()
  Image.new('RGBA',(32,32),(70,90,50,255)).save(self.r/'assets/character.png')
  write(self.r,'approvals.json',{'decisions':[{'id':'D1','evidence':'Synthetic owner receipt for unit-test only','scope':'Fixture Character'}],'character':{'approved':True,'role':'PRODUCT_OWNER','decision_ref':'D1','asset_path':'assets/character.png','asset_sha256':v.digest(self.r/'assets/character.png')},'hero':None,'release':None});seal(self.r);result=v.validate(self.r);self.assertTrue(result['ready_for_gem_b'],result);self.assertEqual(result['semantic_review'],'NOT_CERTIFIED')
 def test_path_traversal(self):
  write(self.r,'references.json',[{'id':'R1','roles':['IDENTITY'],'authority':'PRIMARY','authorization_evidence':'Fixture','availability':'PACKAGED','path':'../outside.png','sha256':'b'*64}]);seal(self.r);self.check('REFERENCE_FILE_MISSING')
 def test_no_caption_policy_conflict(self):
  f=self.read('frames.json');f[0]['caption_policy']='NO_CAPTION';write(self.r,'frames.json',f);seal(self.r);self.check('NO_CAPTION_CONFLICT')
 def test_malformed_json(self):write(self.r,'project.json','not json');seal(self.r);self.check('INVALID_JSON')
if __name__=='__main__':unittest.main(verbosity=2)
