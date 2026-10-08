"""Read the current D567 admission for a recorded predecessor copy."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

from release_contract import ReleaseContractError, canonical_json
from release_handoff import DERIVED_SOURCE_COPY_RELATIVE, tree_sha256
from release_inventory import ReleaseInventoryError, _is_ephemeral_directory, _is_ephemeral_file, refuse_secret_path
from work_journal import event_digest

_D567 = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-567-TOOLS-DELIVERY--bind-validated-compiler-and-package-handoff.md"
_RECORD = {"registration_id", "basis", "authorization_ref", "registered_at", "journal_path", "event_id", "event_digest", "effect_ref", "action_result_path", "action_result_sha256", "checkpoint_path", "checkpoint_sha256", "candidate_snapshot_manifest_sha256", "executing_release", "source_copy_root", "expected_derived_source_copy_sha256", "actual_derived_source_copy_sha256", "persistent_inventory_sha256"}
_MAX_SOURCE_BYTES = 256 * 1024
_MAX_REGISTRATIONS = 8
_MAX_CARRIER_BYTES = 64 * 1024 * 1024


def _pairs(pairs):
    value = dict(pairs)
    if len(value) != len(pairs): raise ValueError("duplicate JSON member")
    return value


def _safe(root: Path, ref: str) -> Path:
    p = Path(ref)
    if not isinstance(ref, str) or p.is_absolute() or not p.parts or ".." in p.parts: raise ValueError("unsafe path")
    cursor = root
    for part in p.parts:
        cursor /= part
        if cursor.is_symlink() or (os.path.lexists(cursor) and cursor != root / p and not cursor.is_dir()): raise ValueError("unsafe carrier")
    return cursor


def _bytes(root: Path, ref: str) -> bytes:
    p = _safe(root, ref)
    if p.is_symlink() or not p.is_file(): raise ValueError("missing carrier")
    if p.stat().st_size > _MAX_CARRIER_BYTES: raise ValueError("carrier is oversized")
    return p.read_bytes()


def _digest(data: bytes) -> str: return hashlib.sha256(data).hexdigest()


def _registration(root: Path) -> dict[str, str]:
    source = _bytes(root, _D567)
    if len(source) > _MAX_SOURCE_BYTES: raise ValueError("registration source is oversized")
    text = source.decode("utf-8")
    heading = "### Current predecessor trust registrations"
    if text.count(heading) != 1 or text.count("```json") != 1: raise ValueError("registration carrier is ambiguous")
    start, end = text.index("```json") + len("```json"), text.index("```", text.index("```json") + len("```json"))
    if text.find("```", end + 3) != -1: raise ValueError("registration carrier has extra fence")
    value = json.loads(text[start:end], object_pairs_hook=_pairs)
    if not isinstance(value, dict) or set(value) != {"schema_version", "registrations"} or type(value["schema_version"]) is not int or value["schema_version"] != 1 or not isinstance(value["registrations"], list) or len(value["registrations"]) != 1 or len(value["registrations"]) > _MAX_REGISTRATIONS: raise ValueError("registration envelope")
    record = value["registrations"][0]
    if not isinstance(record, dict) or set(record) != _RECORD: raise ValueError("registration members")
    if record["basis"] != "current admission of historical delivery evidence" or record["authorization_ref"] != ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations.md" or record["source_copy_root"] != DERIVED_SOURCE_COPY_RELATIVE: raise ValueError("registration fixed fields")
    if any(not isinstance(v, str) for v in record.values()) or any(len(record[k]) != 64 or set(record[k]) - set("0123456789abcdef") for k in ("event_digest", "action_result_sha256", "checkpoint_sha256", "candidate_snapshot_manifest_sha256", "executing_release", "expected_derived_source_copy_sha256", "actual_derived_source_copy_sha256", "persistent_inventory_sha256")): raise ValueError("registration digest")
    return record


def _authorization(root: Path, ref: str) -> bool:
    try:
        data = _bytes(root, ref)
        if len(data) > _MAX_SOURCE_BYTES: return False
        text = data.decode("utf-8")
    except (OSError, UnicodeDecodeError, ValueError):
        return False
    if not text.startswith("---\n"):
        return False
    try:
        frontmatter, body = text[4:].split("\n---\n", 1)
    except ValueError:
        return False
    fields = {}
    for line in frontmatter.splitlines():
        if not line or line.startswith((" ", "-")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        if key in fields:
            return False
        fields[key] = value.strip().strip('"')
    return (fields.get("atom_id") == "CA-P-1117" and fields.get("content_role") == "Plan"
            and fields.get("status") == "Active" and "Complete this Epic autonomously" in body)


def _inventory(root: Path, target: Path) -> str:
    if target.is_symlink() or not target.is_dir(): raise ValueError("target unsafe")
    _safe(root, target.relative_to(root).as_posix())
    dirs, files = [{"path": ".", "mode": target.stat().st_mode & 0o777}], []
    for base, names, file_names in os.walk(target, topdown=True, followlinks=False):
        folder = Path(base)
        kept = []
        for name in sorted(names):
            p, rel = folder / name, (folder / name).relative_to(target).as_posix()
            if p.is_symlink() or not p.is_dir(): raise ValueError("unsafe topology")
            refuse_secret_path(rel)
            if not _is_ephemeral_directory(name):
                dirs.append({"path": rel, "mode": p.stat().st_mode & 0o777}); kept.append(name)
        names[:] = kept
        for name in sorted(file_names):
            p, rel = folder / name, (folder / name).relative_to(target).as_posix()
            if p.is_symlink() or not p.is_file(): raise ValueError("unsafe topology")
            refuse_secret_path(rel)
            if not _is_ephemeral_file(name): files.append({"path": rel, "mode": p.stat().st_mode & 0o777, "sha256": _digest(p.read_bytes())})
    payload = {"directories": sorted(dirs, key=lambda x:x["path"]), "files": sorted(files, key=lambda x:x["path"])}
    return _digest(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode())


def verify_recorded_source_predecessor(root: Path, executing_release: str, destination: Path) -> bool:
    """Reopen D567's single current registration; callers cannot supply proof."""
    try:
        root = root.resolve(strict=True); rec = _registration(root)
        if not rec["journal_path"].startswith(".caprmedio_caprmedio/_journal/") or not rec["action_result_path"].startswith(".caprmedio_install/workflow_orchestrator/runs/") or Path(rec["checkpoint_path"]).name != "release_action_run.json" or Path(rec["action_result_path"]).parent != Path(rec["checkpoint_path"]).parent: return False
        if rec["executing_release"] != executing_release or destination.relative_to(root).as_posix() != DERIVED_SOURCE_COPY_RELATIVE or not _authorization(root, rec["authorization_ref"]): return False
        actual, inventory = tree_sha256(root, destination), _inventory(root, destination)
        if rec["expected_derived_source_copy_sha256"] != actual or rec["actual_derived_source_copy_sha256"] != actual or rec["persistent_inventory_sha256"] != inventory or rec["effect_ref"] != f"{DERIVED_SOURCE_COPY_RELATIVE}#sha256={actual}": return False
        action_b, checkpoint_b = _bytes(root, rec["action_result_path"]), _bytes(root, rec["checkpoint_path"])
        if _digest(action_b) != rec["action_result_sha256"] or _digest(checkpoint_b) != rec["checkpoint_sha256"]: return False
        action = json.loads(action_b, object_pairs_hook=_pairs); checkpoint = json.loads(checkpoint_b, object_pairs_hook=_pairs)
        journal = _bytes(root, rec["journal_path"]).decode().splitlines(); events = [json.loads(x, object_pairs_hook=_pairs) for x in journal]
        found = [e for e in events if isinstance(e, dict) and e.get("event_id") == rec["event_id"] and e.get("event_digest") == rec["event_digest"] and event_digest(e) == rec["event_digest"]]
        if len(found) != 1 or found[0].get("event") != "completed" or found[0].get("outcome") != "completed" or found[0].get("result_ref") != rec["action_result_path"] or found[0].get("effect_refs") != [rec["effect_ref"]]: return False
        from release_checkpoint import restore_release_action_checkpoint
        sealed = restore_release_action_checkpoint(canonical_json(checkpoint)); copy = sealed.source_copy; native = action.get("native_result")
        run = found[0].get("run", {}); run_id = run.get("run_id") if isinstance(run, dict) else None
        output = native.get("output") if isinstance(native, dict) else None
        return bool(copy and isinstance(native, dict) and run.get("kind") == "action" and run.get("definition", {}).get("atom_id") == "CA-O-166" and isinstance(run_id, str) and action.get("action_run_id") == run_id and native.get("action_atom_id") == "CA-O-166" and native.get("action_run_id") == run_id and native.get("outcome") == "completed" and isinstance(output, dict) and output.get("actual_derived_source_copy_sha256") == actual and sealed.workflow_run_id == run_id.rsplit(":step:", 1)[0] and copy.candidate.project_root == str(root) and copy.candidate.authority.executing_release == executing_release and copy.source_copy_root == DERIVED_SOURCE_COPY_RELATIVE and copy.actual_derived_source_copy_sha256 == actual and copy.candidate.manifest.expected_derived_source_copy_sha256 == actual and copy.candidate.manifest.sha256 == rec["candidate_snapshot_manifest_sha256"] and native.get("candidate_snapshot_manifest_sha256") == rec["candidate_snapshot_manifest_sha256"] and native.get("effect_evidence_refs") == [rec["effect_ref"]])
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError, TypeError, KeyError, AttributeError, ReleaseInventoryError, ReleaseContractError): return False


__all__ = ["verify_recorded_source_predecessor"]
