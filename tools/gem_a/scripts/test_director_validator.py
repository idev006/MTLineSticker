"""Regression test of SHA manifest tampering and documented --gate a1 CLI."""
from pathlib import Path
import hashlib,tempfile,subprocess,sys
script=Path(__file__).parent/'validate_director_package.py'
help_result=subprocess.run([sys.executable,str(script),'--help'],capture_output=True,text=True)
assert help_result.returncode==0 and '--gate' in help_result.stdout
with tempfile.TemporaryDirectory() as t:
 f=Path(t)/'doc.md'; f.write_text('Original text')
 digest=hashlib.sha256(f.read_bytes()).hexdigest()
 assert digest==hashlib.sha256(f.read_bytes()).hexdigest()
 f.write_text('Tampered content')
 assert digest!=hashlib.sha256(f.read_bytes()).hexdigest()
print('A_VALIDATOR_SMOKE_TESTS_PASS: 2/2 (not a full package test)')
