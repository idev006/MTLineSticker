#!/usr/bin/env python3
"""Fail-closed B-side handoff verification; no network required, package must be pinned checkout."""
import argparse,hashlib,json,re
from pathlib import Path

def verify(receipt_path, package, source_commit):
    errors=[]
    try:r=json.loads(Path(receipt_path).read_text(encoding='utf-8'))
    except (OSError,ValueError) as e:return {'a1_verified':False,'errors':['RECEIPT_UNREADABLE: '+str(e)]}
    expected={'schema_version':'2.0','gate':'A1','status':'PASS','validator_executed':True,'validator_exit_code':0,'manifest_sha256_verified':True,'binary_delivery':'OWNER_TO_GEM_B_RUNTIME'}
    for k,v in expected.items():
        if type(r.get(k)) is not type(v) or r.get(k)!=v:errors.append('RECEIPT_FIELD_INVALID:'+k)
    if not re.fullmatch('[0-9a-fA-F]{40}',str(source_commit)):errors.append('SOURCE_COMMIT_INVALID')
    if r.get('validated_source_commit')!=source_commit:errors.append('SOURCE_COMMIT_MISMATCH')
    root=Path(package).resolve()
    try:manifest=json.loads((root/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
    except (OSError,ValueError) as e:return {'a1_verified':False,'errors':errors+['MANIFEST_UNREADABLE: '+str(e)]}
    if r.get('manifest_payload_count')!=manifest.get('payload_file_count'):errors.append('COUNT_MISMATCH')
    actual=set(p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='PACKAGE_MANIFEST.json')
    covered=set()
    entries=manifest.get('files')
    if not isinstance(entries,list):entries=[];errors.append('MANIFEST_ENTRIES_INVALID')
    for e in entries:
        if not isinstance(e,dict) or not isinstance(e.get('path'),str):errors.append('ENTRY_INVALID');continue
        name=e['path']
        if name.startswith('/') or '\\' in name or '..' in Path(name).parts:errors.append('UNSAFE_PATH:'+name);continue
        if name in covered:errors.append('DUPLICATE_PATH:'+name)
        covered.add(name)
        p=root/name
        if not p.is_file():errors.append('MISSING_FILE:'+name)
        elif hashlib.sha256(p.read_bytes()).hexdigest()!=e.get('sha256'):errors.append('HASH_MISMATCH:'+name)
    if actual!=covered:errors.append('INVENTORY_MISMATCH')
    if manifest.get('payload_file_count')!=len(actual):errors.append('MANIFEST_COUNT_INVALID')
    return {'a1_verified':not errors,'errors':errors,'validated_source_commit':source_commit}

def main():
    p=argparse.ArgumentParser();p.add_argument('receipt');p.add_argument('package');p.add_argument('--source-commit',required=True);p.add_argument('--report')
    a=p.parse_args();result=verify(a.receipt,a.package,a.source_commit)
    output=json.dumps(result,ensure_ascii=False,indent=2)
    if a.report:Path(a.report).write_text(output+'\n',encoding='utf-8')
    print(output)
    return 0 if result['a1_verified'] else 1
if __name__=='__main__':raise SystemExit(main())
