#!/usr/bin/env python3
"""Deterministic two-phase GEM A Gate A1 document verification (no image files)."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "sets/SET-KHE-NOI-FIRST-HOME-001"
RECEIPT = ROOT / "gate-reports/SET-KHE-NOI-FIRST-HOME-001/A1_LATEST.json"
VALIDATOR = ROOT / "tools/gem_a/scripts/validate_director_package.py"

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_manifest():
    project = json.loads((PACKAGE / "project.json").read_text(encoding="utf-8"))
    paths = sorted(p for p in PACKAGE.rglob("*") if p.is_file() and p.name != "PACKAGE_MANIFEST.json")
    payload = {
        "standard_version": "1.0.0",
        "set_id": project["set_id"],
        "package_revision": project["package_revision"],
        "payload_file_count": len(paths),
        "total_archive_entry_count": len(paths)+1,
        "files": [{"path": p.relative_to(PACKAGE).as_posix(), "sha256": sha(p)} for p in paths],
        "binary_delivery_policy": "OWNER_TO_GEM_B_RUNTIME",
        "binary_in_github_required": False,
    }
    (PACKAGE / "PACKAGE_MANIFEST.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"MANIFEST_GENERATED: {len(paths)} entries")

def validate_source():
    source_commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if subprocess.run(["git", "diff", "--quiet", "HEAD", "--", str(PACKAGE)],
                      cwd=ROOT).returncode != 0:
        raise SystemExit("PACKAGE_DIRTY: commit the generated manifest before validation")
    run = subprocess.run(
        [sys.executable, str(VALIDATOR), str(PACKAGE), "--gate", "a1"],
        cwd=ROOT, text=True, capture_output=True)
    try:
        report = json.loads(run.stdout)
    except (ValueError, TypeError):
        report = {"a1_ready": False,
                  "errors": [{"code": "VALIDATOR_RUNTIME_ERROR",
                              "detail": (run.stderr + run.stdout)[-4000:]}]}
    manifest = json.loads((PACKAGE / "PACKAGE_MANIFEST.json").read_text(encoding="utf-8"))
    frame_data = json.loads((PACKAGE / "frames.json").read_text(encoding="utf-8"))
    decisions = json.loads((PACKAGE / "approvals.json").read_text(encoding="utf-8"))
    passed = run.returncode == 0 and report.get("a1_ready") is True and not report.get("errors")
    receipt = {
        "schema_version": "2.0",
        "set_id": "SET-KHE-NOI-FIRST-HOME-001",
        "gate": "A1",
        "status": "PASS" if passed else "FAIL",
        "validated_source_commit": source_commit,
        "validator_version": report.get("validator_version", "unavailable"),
        "validator_executed": True,
        "validator_exit_code": run.returncode,
        "manifest_sha256_verified": passed,
        "manifest_payload_count": manifest.get("payload_file_count"),
        "caption_master_version": "0.4.0",
        "caption_exact_count": len(frame_data),
        "character_approval_recorded": decisions.get("character", {}).get("approved") is True,
        "binary_delivery": "OWNER_TO_GEM_B_RUNTIME",
        "a2_status": "AWAITING_OWNER_ASSETS",
        "errors": report.get("errors", []),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "handoff_authorized": passed,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"], "errors": len(receipt["errors"]),
                      "source_commit": source_commit}, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"manifest", "validate"}:
        raise SystemExit("Usage: finalize_khe_a1.py manifest|validate")
    if sys.argv[1] == "manifest": write_manifest()
    else: validate_source()
