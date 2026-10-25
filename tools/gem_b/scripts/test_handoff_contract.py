import sys,tempfile,hashlib,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from verify_a1_receipt import verify
with tempfile.TemporaryDirectory() as d:
 root=Path(d);p=root/'project';p.mkdir();(p/'project.json').write_text('document',encoding='utf-8')
 sha=hashlib.sha256((p/'project.json').read_bytes()).hexdigest()
 (p/'PACKAGE_MANIFEST.json').write_text(json.dumps({'files':[{'path':'project.json','sha256':sha}],'payload_file_count':1}))
 commit='a'*40
 r={'schema_version':'2.0','gate':'A1','status':'PASS','validator_executed':True,'validator_exit_code':0,'manifest_sha256_verified':True,'binary_delivery':'OWNER_TO_GEM_B_RUNTIME','validated_source_commit':commit,'manifest_payload_count':1}
 path=root/'receipt.json';path.write_text(json.dumps(r))
 assert verify(path,p,commit)['a1_verified'];print('PASS: valid A1 receipt + pinned manifest')
 assert not verify(path,p,'b'*40)['a1_verified'];print('PASS: changed source commit rejected')
 r['status']='FAIL';path.write_text(json.dumps(r))
 assert not verify(path,p,commit)['a1_verified'];print('PASS: FAIL receipt rejected')
 r['status']='PASS';path.write_text(json.dumps(r));(p/'project.json').write_text('tampered')
 assert not verify(path,p,commit)['a1_verified'];print('PASS: tampered document rejected')
print('B_HANDOFF_CONTRACT_TESTS_PASS: 4/4')
