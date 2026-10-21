import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'contracts/sticker-handoff/v1'))
from validator import validate
H='a'*64
def sample():
    frames=['F%02d'%i for i in range(1,41)]
    return dict(contract_version='1.0.0',set_id='SET-CHAICHAT-001',run_id='TEST',status='READY_FOR_GEM_B',source_commit='b'*40,package_manifest_sha256=H,character={'asset_path':'character.png','sha256':H,'state':'CHARACTER_SHEET_ACTIVE','approval':{'approval_id':'APP-01','role':'PRODUCT_OWNER','asset_sha256':H,'approved':True}},frames=frames,sheets=[{'id':str(i+1),'frame_ids':frames[i*8:i*8+8]} for i in range(5)],hero_ids=['F01','F06','F18','F19'],blocking_issues=[])
class ValidatorTests(unittest.TestCase):
    def test_valid(self): self.assertEqual(validate(sample()),[])
    def test_missing(self):
        x=sample();x['sheets'][2]['frame_ids'].remove('F17');self.assertIn('FRAME_MAPPING_MISMATCH',validate(x))
    def test_duplicate(self):
        x=sample();x['sheets'][2]['frame_ids'].append('F01');self.assertIn('DUPLICATE_FRAME_MAPPING',validate(x))
    def test_character(self):
        x=sample();x['character']['approval']=None;self.assertIn('CHARACTER_APPROVAL_MISSING_OR_STALE',validate(x))
    def test_stale_character(self):
        x=sample();x['character']['sha256']='c'*64;self.assertIn('CHARACTER_APPROVAL_MISSING_OR_STALE',validate(x))
    def test_hero_gate(self):
        x=sample();x['status']='FULL_PRODUCTION_UNLOCKED';self.assertIn('HERO_APPROVAL_REQUIRED',validate(x))
    def test_hero_approved(self):
        x=sample();x['status']='FULL_PRODUCTION_UNLOCKED';x['hero_approval']={'role':'PRODUCT_OWNER','approved':True,'asset_sha256':H};self.assertEqual(validate(x),[])
    def test_blocking(self):
        x=sample();x['blocking_issues']=['ASSET_MISSING'];self.assertIn('BLOCKING_ISSUES_PRESENT',validate(x))
    def test_hero_outside(self):
        x=sample();x['hero_ids']=['F41'];self.assertIn('HERO_FRAME_NOT_DECLARED',validate(x))
    def test_commit(self):
        x=sample();x['source_commit']='main';self.assertIn('SOURCE_COMMIT_INVALID',validate(x))
if __name__=='__main__':unittest.main()
