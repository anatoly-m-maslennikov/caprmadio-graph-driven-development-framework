"""Shared no-mutation lifecycle-intent support for CA-R-1041 and CA-R-1042."""

from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import re
import subprocess
import sys
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from authoritative_status_models import StatusModelError, resolve_status_model
from atom_operations import (
    Atom,
    ToolError as AtomToolError,
    archive_atom_revision,
    atom_digest,
    atom_from_path,
    atom_version,
    canonical_json,
    control_root,
    create_atom_revision,
    demote_atom_to_draft,
    draft_revision_lineage,
    frontmatter_scalar,
    migrate_atom_identity_revision,
    move_atom_revision,
    prepare_create_atom_revision,
    prepare_draft_promotion,
    preserve_atom_revision,
    project_identity_prefix,
    promote_draft_atom,
    replace_draft_revision_lineage,
    replace_frontmatter_scalar,
    resolve_repository,
    resolve_selector,
    safe_path,
    scan_atoms,
    split_frontmatter,
    write_atom_revision,
)


ATOM_ID = re.compile(r"^CA-[A-Z]+-[0-9]{3,}$")
INACTIVE_LIFECYCLE_SEGMENTS = frozenset({"archive", "drafts", "done", "solved", "resolved", "canceled", "cancelled"})


class IntentError(RuntimeError):
    """Return one deterministic lifecycle-intent diagnostic."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


class LifecycleError(IntentError):
    """A route-local lifecycle diagnostic for the shared selected-run caller."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(code, f"{code}: {message}")


def load_payload(source: str) -> dict[str, Any]:
    """Read one JSON request for CA-M-128 or CA-M-129."""
    try:
        raw = sys.stdin.read() if source == "-" else Path(source).read_text(encoding="utf-8")
        payload = json.loads(raw)
    except OSError as error:
        raise IntentError("input-unreadable", "--input must name a readable JSON object") from error
    except json.JSONDecodeError as error:
        raise IntentError("input-json-invalid", "--input must contain one JSON object") from error
    if not isinstance(payload, dict):
        raise IntentError("input-json-invalid", "--input must contain one JSON object")
    return payload


def active_atoms(root: Path) -> dict[str, list[Atom]]:
    """Index active Atom IDs without rejecting unrelated duplicate identities."""
    try:
        atoms = scan_atoms(root)
    except AtomToolError as error:
        raise IntentError(error.code, str(error)) from error
    result: dict[str, list[Atom]] = {}
    for atom in atoms:
        if atom.atom_id is None or any(part.casefold() in INACTIVE_LIFECYCLE_SEGMENTS for part in atom.path.parts):
            continue
        result.setdefault(atom.atom_id, []).append(atom)
    return result


def required_atom_id(payload: Mapping[str, Any], field: str) -> str:
    """Read one canonical Atom ID supplied by the operator."""
    value = payload.get(field)
    if not isinstance(value, str) or not ATOM_ID.fullmatch(value):
        raise IntentError("atom-id-invalid", f"{field} must be an exact Atom ID such as CA-R-1041")
    return value


def required_context(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Preserve explicit action context without giving it graph meaning."""
    value = payload.get("action_context")
    if not isinstance(value, Mapping):
        raise IntentError("action-context-required", "action_context must be a JSON object")
    return dict(value)


def optional_active_ids(payload: Mapping[str, Any], field: str, atoms: Mapping[str, list[Atom]]) -> list[str]:
    """Resolve supplied Atom IDs without inferring omitted participants."""
    value = payload.get(field, [])
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise IntentError("atom-id-list-invalid", f"{field} must be an array of exact Atom IDs")
    if len(value) != len(set(value)):
        raise IntentError("atom-id-list-duplicate", f"{field} must not repeat one Atom ID")
    for item in value:
        if not ATOM_ID.fullmatch(item):
            raise IntentError("active-atom-required", f"{field} contains no active Atom: {item}")
        active_atom(item, atoms)
    return list(value)


def active_atom(atom_id: str, atoms: Mapping[str, list[Atom]]) -> Atom:
    """Return one requested active carrier and reject only its duplicate identity."""
    matches = atoms.get(atom_id, [])
    if not matches:
        raise IntentError("active-atom-required", f"no active Atom has ID {atom_id}")
    if len(matches) != 1:
        raise IntentError("active-atom-id-ambiguous", f"more than one active Atom has ID {atom_id}")
    return matches[0]


def carrier(atom: Atom) -> dict[str, str]:
    """Project the minimal carrier locator needed for a later handoff."""
    assert atom.atom_id is not None
    return {"atom_id": atom.atom_id, "path": atom.relative, "lifecycle": atom.lifecycle}


def deferred_handoff(tool_id: str, operation: str, atom_ids: Mapping[str, Any], action_context: Mapping[str, Any]) -> dict[str, Any]:
    """Describe the explicit non-executable pipeline handoff boundary."""
    return {
        "contract_version": 1,
        "producer": tool_id,
        "operation": operation,
        "atom_ids": dict(atom_ids),
        "action_context": dict(action_context),
        "relation_inference": "not_performed",
        "status": "deferred",
        "reason": "COMMIT_CONTEXT has no admitted lifecycle-intent input contract",
    }


def envelope(tool_id: str, *, ok: bool, mode: str, result: Mapping[str, Any] | None = None, error: BaseException | None = None) -> dict[str, Any]:
    """Produce the common machine-readable Tool envelope."""
    value: dict[str, Any] = {"schema_version": 1, "tool": {"capability_id": tool_id, "kind": "doer"}, "ok": ok, "mode": mode, "diagnostics": []}
    if error is not None:
        value["diagnostics"] = [{"code": getattr(error, "code", "operation-failed"), "message": str(error)}]
    if result is not None:
        value["result"] = dict(result)
    return value


def run_cli(tool_id: str, input_schema: Mapping[str, Any], build_intent: Callable[[Path, Mapping[str, Any]], dict[str, Any]]) -> int:
    """Run one lifecycle Doer as describe, dry-run, or blocked apply."""
    parser = argparse.ArgumentParser(prog=tool_id.lower().replace("_", "-"))
    parser.add_argument("--repository", default=".", help="CAPRMEDIO repository root")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("describe", help="print capability and input contract")
    run = commands.add_parser("run", help="validate and describe one lifecycle intent")
    run.add_argument("--input", required=True, metavar="JSON_FILE_OR_DASH")
    run.add_argument("--apply", action="store_true", help="currently blocked before all mutation")
    args = parser.parse_args()
    if args.command == "describe":
        print(json.dumps(envelope(tool_id, ok=True, mode="describe", result={"input_schema": dict(input_schema), "mutation_default": "dry-run", "apply_status": "blocked"}), sort_keys=True, separators=(",", ":")))
        return 0
    try:
        result = build_intent(resolve_repository(args.repository), load_payload(args.input))
        if args.apply:
            error = IntentError("apply-blocked", "lifecycle-intent serialization is not admitted by the commit pipeline")
            print(json.dumps(envelope(tool_id, ok=False, mode="apply-blocked", result=result, error=error), sort_keys=True, separators=(",", ":")))
            return 2
        print(json.dumps(envelope(tool_id, ok=True, mode="dry-run", result=result), sort_keys=True, separators=(",", ":")))
        return 0
    except (IntentError, AtomToolError, OSError) as error:
        print(json.dumps(envelope(tool_id, ok=False, mode="apply-blocked" if args.apply else "dry-run", error=error), sort_keys=True, separators=(",", ":")))
        return 2


# CA-D-531 action API -------------------------------------------------------
#
# These are deliberately route-local effects.  The shared selected-run support
# owns the outer request, receipt, authorization seal, Run/Event identities,
# recording state, and retry.  A caller reaches an actual mutation only after
# it has admitted the outer request and passes execute=True, authorized=True.

_DESCRIPTOR_FIELDS = frozenset({"atom_id", "path", "filename", "version", "digest", "lifecycle", "status", "updated_at", "content_role", "type"})
_CARRIER_FIELDS = frozenset({"path", "frontmatter", "content"})
_UPDATE_CLASSES = frozenset({"carrier_only", "equivalent_refinement", "semantic_revision"})
_ATOM_REFERENCE = re.compile(r"\bCA-[A-Z]+-[0-9]+\b")


def _mapping(value: object, name: str) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        raise LifecycleError("mapping-required", f"{name} must be one object")
    return dict(value)


def _exact_fields(value: Mapping[str, Any], fields: frozenset[str], name: str) -> None:
    missing = sorted(fields - value.keys())
    unknown = sorted(value.keys() - fields)
    if missing or unknown:
        detail = ", ".join(([f"missing {item}" for item in missing] + [f"unknown {item}" for item in unknown]))
        raise LifecycleError("carrier-fields-invalid", f"{name} must carry exactly its complete fields ({detail})")


def _translate(error: AtomToolError) -> LifecycleError:
    return LifecycleError(error.code, error.message)


def carrier_descriptor(root: Path, selector: str | Atom) -> dict[str, Any]:
    """Return the complete, serializable current Carrier seal for one Atom."""

    root = root.resolve()
    try:
        atom = selector if isinstance(selector, Atom) else resolve_selector(root, selector)
        return {
            "atom_id": atom.atom_id,
            "path": atom.relative,
            "filename": atom.filename,
            "version": atom_version(atom),
            "digest": atom_digest(atom),
            "lifecycle": atom.lifecycle,
            "status": frontmatter_scalar(atom.frontmatter, "status"),
            "updated_at": frontmatter_scalar(atom.frontmatter, "updated_at"),
            "content_role": frontmatter_scalar(atom.frontmatter, "content_role"),
            "type": frontmatter_scalar(atom.frontmatter, "type"),
        }
    except AtomToolError as error:
        raise _translate(error) from error


def _resolve_descriptor(root: Path, value: object, *, name: str, active: bool = True) -> Atom:
    if not isinstance(value, Mapping) and name in {"target", "predecessor"}:
        raise LifecycleError("one-target-required", f"{name} must name exactly one complete carrier set")
    descriptor = _mapping(value, name)
    _exact_fields(descriptor, _DESCRIPTOR_FIELDS, name)
    if not isinstance(descriptor["path"], str):
        raise LifecycleError("carrier-path-invalid", f"{name}.path must be a repository-relative string")
    try:
        atom = atom_from_path(root, safe_path(root, descriptor["path"], must_exist=True))
        observed = carrier_descriptor(root, atom)
    except AtomToolError as error:
        raise _translate(error) from error
    for field in _DESCRIPTOR_FIELDS:
        if descriptor[field] != observed[field]:
            raise LifecycleError("stale-carrier", f"{name} {field} no longer matches the observed carrier")
    if active and atom.lifecycle != "active":
        raise LifecycleError("active-carrier-required", f"{name} must resolve one active carrier")
    return atom


def _resolve_legacy_descriptor(root: Path, value: object, proof_value: object, *, mapped_identity: str | None = None) -> Atom:
    """Read one explicitly sealed historical carrier, never a lookup fallback.

    Only Update accepts this migration input.  The assigned filename identity
    must already exist in the exact committed bytes supplied by the caller;
    this cannot assign an identity to a draft or repair a colliding identity.
    An explicit mapping may encode an assigned pre-current-format identity;
    it never renumbers an already canonical assigned identity.
    """
    descriptor = _mapping(value, "target")
    _exact_fields(descriptor, _DESCRIPTOR_FIELDS, "target")
    proof = _mapping(proof_value, "legacy_identity_proof")
    _exact_fields(proof, frozenset({"atom_id", "commit", "path", "digest"}), "legacy_identity_proof")
    if (not isinstance(proof["commit"], str) or not re.fullmatch(r"[0-9a-f]{40}", proof["commit"])
            or not isinstance(proof["digest"], str) or not re.fullmatch(r"[0-9a-f]{64}", proof["digest"])
            or proof["path"] != descriptor["path"] or proof["atom_id"] != descriptor["atom_id"]):
        raise LifecycleError("legacy-proof-invalid", "historical proof must bind the exact target identity, path and bytes")
    try:
        path = safe_path(root, descriptor["path"], must_exist=True)
        try:
            atom_from_path(root, path)
        except AtomToolError as error:
            if error.code != "atom-frontmatter-id-required":
                raise
        else:
            raise LifecycleError("legacy-proof-inapplicable", "target already carries an explicit identity")
        raw = path.read_bytes()
        frontmatter, content = split_frontmatter(raw.decode("utf-8"))
        relative = path.relative_to(control_root(root))
        if any(part.casefold() in INACTIVE_LIFECYCLE_SEGMENTS | {"archived", "resolved"} for part in relative.parts):
            raise LifecycleError("legacy-proof-inapplicable", "migration requires a current carrier, not a draft or history")
        matches = re.findall(r"(?:^|-)(CA-[CAPRMEDO]-[0-9]+)(?=-|$)", path.stem)
        old_id = str(proof["atom_id"])
        if mapped_identity is None:
            identity_matches = matches == [old_id]
        else:
            identity_matches = (not matches and not ATOM_ID.fullmatch(old_id)
                                and re.fullmatch(r"[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+-[0-9]+", old_id) is not None
                                and path.stem.partition("--")[0].startswith(old_id + "-"))
        if not identity_matches or hashlib.sha256(raw).hexdigest() != proof["digest"]:
            raise LifecycleError("legacy-proof-invalid", "historical assigned identity or present bytes differ")
        committed = subprocess.run(
            ["git", "-c", f"safe.directory={root}", "-C", str(root), "show", f"{proof['commit']}:{proof['path']}"],
            capture_output=True, check=False,
        )
        ancestor = subprocess.run(
            ["git", "-c", f"safe.directory={root}", "-C", str(root), "merge-base", "--is-ancestor", proof["commit"], "HEAD"],
            capture_output=True, check=False,
        )
        if committed.returncode != 0 or ancestor.returncode not in {0, 1}:
            raise LifecycleError("legacy-history-unavailable", "cannot read the explicitly scoped repository history")
        if ancestor.returncode != 0 or committed.stdout != raw:
            raise LifecycleError("legacy-proof-invalid", "exact assigned carrier is not backed by the current Git history")
        role = next(part for part in reversed(relative.parts[:-1]) if re.fullmatch(r"0[1-9]_[a-z0-9_]+", part))
        roles = {"C": "01_concern", "A": "02_analysis", "P": "03_plan", "R": "04_requirement",
                 "M": "05_method", "E": "06_evaluation", "D": "07_delivery", "O": "09_operations"}
        identity_letter = (mapped_identity or old_id).split("-")[1]
        if role != roles.get(identity_letter):
            raise LifecycleError("legacy-proof-invalid", "assigned identity differs from the carrier Content Role")
        old_status = frontmatter_scalar(frontmatter, "status")
        if old_status is not None and old_status.casefold() != "active":
            raise LifecycleError("legacy-proof-inapplicable", "migration cannot activate a draft or inactive Atom")
        role_values = {"C": "Concern", "A": "Analysis", "P": "Plan", "R": "Requirement", "M": "Method",
                       "E": "Evaluation", "D": "Delivery", "O": "Operations"}
        old_role = frontmatter_scalar(frontmatter, "content_role")
        if old_role is not None and old_role != role_values[identity_letter]:
            raise LifecycleError("legacy-proof-invalid", "migration cannot replace an explicitly different Content Role")
        atom = Atom(path, path.relative_to(root).as_posix(), path.name, str(proof["atom_id"]),
                    "active", role, frontmatter, content)
        observed = carrier_descriptor(root, atom)
        if any(descriptor[field] != observed[field] for field in _DESCRIPTOR_FIELDS):
            raise LifecycleError("stale-carrier", "legacy target no longer matches its complete sealed descriptor")
        for candidate in control_root(root).rglob(f"*{atom.atom_id}*.md"):
            if candidate == path or any(part.casefold() in INACTIVE_LIFECYCLE_SEGMENTS | {"archived", "resolved"}
                                        for part in candidate.relative_to(control_root(root)).parts):
                continue
            try:
                other = atom_from_path(root, candidate)
            except AtomToolError as error:
                same_legacy_identity = (candidate.stem.partition("--")[0].startswith(old_id + "-")
                                        if mapped_identity is not None else
                                        re.findall(r"(?:^|-)(CA-[CAPRMEDO]-[0-9]+)(?=-|$)", candidate.stem) == [atom.atom_id])
                if error.code == "atom-frontmatter-id-required" and same_legacy_identity:
                    raise LifecycleError("active-atom-id-ambiguous", "legacy identity has another unnormalized owner") from error
            else:
                if other.atom_id == atom.atom_id:
                    raise LifecycleError("active-atom-id-ambiguous", "legacy identity already has another current owner")
        return atom
    except AtomToolError as error:
        raise _translate(error) from error


def _legacy_summary(content: str) -> str:
    headings = re.findall(r"(?m)^# (.+?)\s*$", content)
    if len(headings) != 1 or headings[0] == "Summary":
        raise LifecycleError("legacy-summary-ambiguous", "legacy migration requires one exact first-H1 Summary")
    return headings[0]


def _summary(content: str) -> str:
    match = re.search(r"(?m)^# Summary\s*$\n(?P<tail>.*?)(?=^#|\Z)", content, re.DOTALL)
    if match is None:
        raise LifecycleError("summary-missing", "the complete carrier content must contain # Summary")
    for line in match.group("tail").splitlines():
        value = line.strip()
        if value:
            return value
    raise LifecycleError("summary-missing", "# Summary must carry a non-empty value")


def _refresh_frontmatter(frontmatter: str, *, version: int | None = None) -> str:
    result = frontmatter
    if version is not None:
        result = replace_frontmatter_scalar(result, "version", str(version))
    stamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    return replace_frontmatter_scalar(result, "updated_at", f'"{stamp}"')


def _effect(state: str, *, carrier: Mapping[str, Any], reason: str | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"carrier": dict(carrier), "state": state}
    if reason is not None:
        result["reason"] = reason
    return result


def _execute_allowed(*, execute: bool, authorized: bool) -> bool:
    if execute and not authorized:
        raise LifecycleError("authorization-required", "the caller has not admitted an authorized mutation")
    return execute


def _complete_carrier(value: object) -> dict[str, str]:
    carrier = _mapping(value, "carrier")
    _exact_fields(carrier, _CARRIER_FIELDS, "carrier")
    if any(not isinstance(carrier[field], str) for field in _CARRIER_FIELDS):
        raise LifecycleError("carrier-properties-invalid", "carrier path, frontmatter, and content must be strings")
    if not carrier["path"] or not carrier["frontmatter"]:
        raise LifecycleError("carrier-properties-invalid", "carrier path and frontmatter must be non-empty")
    return {field: carrier[field] for field in _CARRIER_FIELDS}


def _proposal(value: object) -> dict[str, str]:
    proposed = _mapping(value, "proposed")
    _exact_fields(proposed, frozenset({"frontmatter", "content"}), "proposed")
    if not all(isinstance(proposed[field], str) for field in ("frontmatter", "content")):
        raise LifecycleError("carrier-properties-invalid", "proposed frontmatter and content must be strings")
    return {"frontmatter": proposed["frontmatter"], "content": proposed["content"]}


def _proposed_successors(root: Path, value: object, predecessor: Atom) -> list[dict[str, str]]:
    """Validate future successor carriers without requiring present carriers."""

    if not isinstance(value, list) or not value:
        raise LifecycleError("successor-set-required", "Replace requires one or more complete successor carrier sets")
    successors: list[dict[str, str]] = []
    atom_ids: list[str | None] = []
    paths: list[str] = []
    for index, item in enumerate(value):
        successor = _complete_carrier(item)
        try:
            destination, _, atom_id = prepare_create_atom_revision(root, successor["path"], successor["frontmatter"])
        except AtomToolError as error:
            raise _translate(error) from error
        if atom_id == predecessor.atom_id:
            raise LifecycleError("replacement-self-reference", "predecessor cannot be one of its successors")
        successors.append(successor)
        atom_ids.append(atom_id)
        paths.append(destination.relative_to(root).as_posix())
    if len(atom_ids) != len(set(atom_ids)) or len(paths) != len(set(paths)):
        raise LifecycleError("successor-set-duplicate", "complete successor set must not repeat an Atom or destination")
    return successors


def _status_destination(root: Path, atom: Atom, status: str) -> str:
    """Resolve the current role-local status carrier location without inference."""

    control = control_root(root)
    try:
        relative = atom.path.relative_to(control)
        index = next(index for index, part in enumerate(relative.parts[:-1]) if re.fullmatch(r"0[1-9]_[a-z0-9_]+", part))
    except (ValueError, StopIteration) as error:
        raise LifecycleError("status-location-missing", "target has no content-role status location") from error
    role = control.joinpath(*relative.parts[:index + 1])
    if frontmatter_scalar(atom.frontmatter, "content_role") == "Plan":
        local = atom.path.parent
        if local.name in {"001_backlog", "done", "canceled", "archived"}:
            local = local.parent
        folders = {"Active": None, "Backlog": "001_backlog", "Done": "done", "Canceled": "canceled"}
        if status in folders:
            target = local / folders[status] / atom.filename if folders[status] else local / atom.filename
            return target.relative_to(root).as_posix()
    if status == "Active":
        target = role / atom.filename
    else:
        folder = status.casefold()
        if re.fullmatch(r"[a-z0-9][a-z0-9_-]*", folder) is None:
            raise LifecycleError("status-location-invalid", "admitted status cannot name a safe carrier subfolder")
        target = role / folder / atom.filename
    return target.relative_to(root).as_posix()


def _status_model(value: object, atom: Atom, requested_status: str) -> dict[str, Any]:
    model = _mapping(value, "status_model")
    required = frozenset({"model_ref", "model_revision", "content_role", "statuses", "transitions"})
    missing = sorted(required - model.keys())
    if missing:
        raise LifecycleError("status-model-incomplete", f"status_model is missing {', '.join(missing)}")
    if not isinstance(model["model_ref"], str) or not model["model_ref"]:
        raise LifecycleError("status-model-invalid", "status_model.model_ref must be non-empty")
    if not isinstance(model["model_revision"], (str, int)):
        raise LifecycleError("status-model-invalid", "status_model.model_revision must be a scalar")
    if not isinstance(model["content_role"], str) or not model["content_role"]:
        raise LifecycleError("status-model-invalid", "status_model.content_role must be non-empty")
    model_type = model.get("type")
    if model_type is not None and (not isinstance(model_type, str) or not model_type):
        raise LifecycleError("status-model-invalid", "status_model.type must be an optional non-empty string")
    if frontmatter_scalar(atom.frontmatter, "content_role") != model["content_role"]:
        raise LifecycleError("status-model-unqualified", "status_model does not qualify the target Content Role")
    if model_type is not None and frontmatter_scalar(atom.frontmatter, "type") != model_type:
        raise LifecycleError("status-model-unqualified", "status_model type does not qualify the target")
    statuses = model["statuses"]
    if not isinstance(statuses, list) or not statuses or any(not isinstance(item, str) or not item for item in statuses):
        raise LifecycleError("status-model-invalid", "status_model.statuses must be a non-empty string list")
    if len(statuses) != len(set(statuses)) or requested_status not in statuses:
        raise LifecycleError("status-unadmitted", "requested status is not admitted by the qualified status model")
    transitions = model["transitions"]
    if not isinstance(transitions, Mapping):
        raise LifecycleError("status-model-invalid", "status_model.transitions must map exact statuses to destinations")
    current = frontmatter_scalar(atom.frontmatter, "status")
    if current is None or current not in statuses:
        raise LifecycleError("status-current-unadmitted", "target current status is not admitted by the qualified status model")
    allowed = transitions.get(current, [])
    if not isinstance(allowed, list) or any(not isinstance(item, str) for item in allowed):
        raise LifecycleError("status-model-invalid", "status_model transition destinations must be string lists")
    if requested_status != current and requested_status not in allowed:
        raise LifecycleError("status-transition-unadmitted", "qualified status model does not admit the requested transition")
    archive_status = model.get("archive_status")
    if archive_status is not None and (not isinstance(archive_status, str) or archive_status not in statuses):
        raise LifecycleError("status-model-invalid", "status_model.archive_status must be one admitted status")
    return {
        "model_ref": model["model_ref"],
        "model_revision": str(model["model_revision"]),
        "content_role": model["content_role"],
        "type": model_type,
        "statuses": list(statuses),
        "transitions": {str(key): list(item) for key, item in transitions.items()},
        "archive_status": archive_status,
    }


def preflight_atom_lifecycle(root: Path, operation: str, parameters: Mapping[str, Any]) -> dict[str, Any]:
    """Purely observe one model-governed status operation before any effect."""
    root = root.resolve()
    request = _mapping(parameters, "parameters")
    if operation != "change_status":
        raise LifecycleError("operation-unadmitted", "preflight supports change_status only")
    allowed = frozenset({"target", "status"})
    if set(request) - allowed or not {"target", "status"}.issubset(request):
        raise LifecycleError("carrier-fields-invalid", "parameters must carry target and status only")
    requested = request["status"]
    if not isinstance(requested, str) or not requested:
        raise LifecycleError("status-invalid", "status must be a non-empty source-admitted value")
    target = _resolve_descriptor(root, request["target"], name="target", active=False)
    prior = carrier_descriptor(root, target)
    role = frontmatter_scalar(target.frontmatter, "content_role")
    atom_type = frontmatter_scalar(target.frontmatter, "type")
    if role is None:
        raise LifecycleError("status-model-unqualified", "target lacks a carried Content Role")
    try:
        model = resolve_status_model(root, {"content_role": role, "type": atom_type}, requested)
    except StatusModelError as error:
        raise LifecycleError(error.code, str(error)) from error
    current = frontmatter_scalar(target.frontmatter, "status")
    if current is None or current not in model["statuses"]:
        raise LifecycleError("status-current-unadmitted", "target current status is not admitted by the current source model")
    archive = requested == "Archived"
    return {"operation": operation, "target": target, "prior": prior, "requested_status": requested,
            "current_status": current, "status_model": model, "archive": archive}


def _draft_promotion_head(root: Path, target: Atom) -> tuple[dict[str, str], dict[str, Any]]:
    """Resolve the sole trusted, still-live retained Draft head."""
    from draft_history import DraftHistoryError, validate_current_draft_head

    lineage = draft_revision_lineage(target.frontmatter)
    if not isinstance(lineage, Mapping) or set(lineage) != {"history_entry_ref"}:
        raise LifecycleError("draft-lineage-missing", "Draft has no authoritative revision_lineage")
    try:
        head = dict(lineage["history_entry_ref"])
        entry = validate_current_draft_head(root, target.relative, head)
    except (DraftHistoryError, KeyError, TypeError) as error:
        raise LifecycleError("draft-lineage-invalid", "Draft has no current trusted retained-history head") from error
    return head, entry


def _draft_promotion_identity(root: Path, target: Atom, *, head_entry: Mapping[str, Any] | None = None) -> str:
    """Allocate only after recovery has found no sealed transition for this head."""
    if head_entry is None:
        _, head_entry = _draft_promotion_head(root, target)
    role = frontmatter_scalar(target.frontmatter, "content_role")
    predecessor = head_entry.get("direct_predecessor")
    if predecessor is None:
        if not role:
            raise LifecycleError("draft-lineage-invalid", "Draft lacks Content Role")
        prefix, letter = project_identity_prefix(root), role[0].upper()
        used = [int(match.group(1)) for atom in scan_atoms(root) if atom.atom_id
                for match in [re.fullmatch(rf"{prefix}-{letter}-(\d+)", atom.atom_id)] if match]
        return f"{prefix}-{letter}-{max(used, default=0) + 1}"
    if _summary(target.content) != predecessor.get("summary") or frontmatter_scalar(target.frontmatter, "content_role") != predecessor.get("content_role"):
        raise LifecycleError("draft-lineage-stale", "Draft direct predecessor no longer proves identity continuity")
    return str(predecessor["atom_id"])


def _pending_request_digest(parameters: Mapping[str, Any]) -> str:
    """Match the public pending-reservation request seal without caller evidence."""
    try:
        return hashlib.sha256(canonical_json(dict(parameters)).encode("utf-8")).hexdigest()
    except (TypeError, ValueError) as error:
        raise LifecycleError("request-invalid", "Draft promotion request is not canonical JSON") from error


def _pending_promotion_result(
    root: Path,
    parameters: Mapping[str, Any],
    *,
    prior: Mapping[str, Any],
    draft_path: str,
    head: Mapping[str, Any],
    status_model: Mapping[str, Any],
    prior_status: str,
    live_draft: Atom | None,
) -> tuple[Atom | None, dict[str, Any] | None]:
    """Recover an exact sealed promotion before identity or output preparation.

    ``None, None`` means that this head has no reservation, so the caller may
    begin one fresh transition.  A sealed request is always recovered or
    refused here; its planned ID is never compared to a newly allocated ID.
    """
    from draft_promotion_pending import (
        PendingPromotionError,
        lookup_pending_promotion,
        match_promotion_successor,
        recover_pending_promotion,
    )

    try:
        sealed = lookup_pending_promotion(root, draft_path=draft_path, head=head)
        if sealed is None:
            return None, None
        reservation = sealed["reservation"]
        if reservation["request_digest"] != _pending_request_digest(parameters):
            raise LifecycleError("promotion-request-conflict", "pending Draft promotion belongs to a different sealed request")
        recovered = recover_pending_promotion(root, draft_path=draft_path, head=head)
        if recovered is None or recovered["disposition"] != "finalized":
            return None, {
                "operation": "change_status",
                "outcome": "pending",
                "prior_status": prior_status,
                "observed": dict(prior),
                "status_model": dict(status_model),
                "effects": [_effect("unchanged", carrier=prior, reason="pending-promotion-recovery")],
                "pending_promotion": recovered if recovered is not None else sealed,
            }
        reservation = recovered["reservation"]
        output = safe_path(root, reservation["output"]["path"], must_exist=True)
        observed = atom_from_path(root, output)
        if (observed.atom_id != reservation["planned_atom_id"]
                or atom_digest(observed) != reservation["output"]["digest"]):
            raise LifecycleError("promotion-output-conflict", "finalized Draft promotion output no longer matches its sealed reservation")
        successor = match_promotion_successor(
            root, head=head, output_path=reservation["output"]["path"], output_digest=reservation["output"]["digest"],
        )
        if successor != recovered["successor"]:
            raise LifecycleError("promotion-history-conflict", "finalized Draft promotion successor does not match its sealed output")
        if live_draft is not None:
            live_draft.path.unlink(missing_ok=True)
        return observed, None
    except PendingPromotionError as error:
        raise LifecycleError(error.code, str(error)) from error


def _missing_draft_promotion_retry(root: Path, parameters: Mapping[str, Any]) -> dict[str, Any] | None:
    """Recover a terminal retry from retained history, never runtime files or caller identity maps."""
    request = _mapping(parameters, "parameters")
    if set(request) != {"target", "status"}:
        return None
    descriptor = _mapping(request["target"], "target")
    _exact_fields(descriptor, _DESCRIPTOR_FIELDS, "target")
    if descriptor["atom_id"] is not None or descriptor["lifecycle"] != "draft" or not isinstance(descriptor["path"], str):
        return None
    try:
        carrier_path = safe_path(root, descriptor["path"], must_exist=False)
    except AtomToolError as error:
        raise _translate(error) from error
    if carrier_path.exists():
        return None
    requested = request["status"]
    if not isinstance(requested, str) or not requested:
        raise LifecycleError("status-invalid", "status must be a non-empty source-admitted value")
    try:
        model = resolve_status_model(root, {"content_role": descriptor["content_role"], "type": descriptor["type"]}, requested)
    except StatusModelError as error:
        raise LifecycleError(error.code, str(error)) from error
    if descriptor["status"] not in model["statuses"]:
        raise LifecycleError("status-current-unadmitted", "target current status is not admitted by the current source model")
    if requested == descriptor["status"]:
        raise LifecycleError("draft-promotion-retry-missing", "the missing Draft has no terminal promotion retry")

    from draft_history import DraftHistoryError, history_entry_ref, load_history_entry

    history_directory = control_root(root) / "archive" / "_draft_history"
    if not history_directory.exists() or history_directory.is_symlink() or not history_directory.is_dir():
        raise LifecycleError("draft-promotion-retry-missing", "the missing Draft has no trusted retained-history head")
    expected_output = {"path": descriptor["path"], "digest": descriptor["digest"]}
    matches: list[dict[str, str]] = []
    try:
        for path in sorted(history_directory.glob("*.json")):
            reference = history_entry_ref(root, path.stem, path.relative_to(root).as_posix())
            entry = load_history_entry(root, reference)
            if entry.get("draft_output") == expected_output and entry.get("origin", {}).get("kind") in {
                "never_identified", "demoted_identified", "draft_update",
            }:
                matches.append(dict(reference))
    except (DraftHistoryError, OSError, ValueError) as error:
        raise LifecycleError("draft-lineage-invalid", "missing Draft retained history cannot be trusted") from error
    if len(matches) != 1:
        raise LifecycleError("draft-promotion-retry-missing", "the missing Draft does not resolve one trusted retained-history head")
    observed, pending = _pending_promotion_result(
        root, parameters, prior=descriptor, draft_path=descriptor["path"], head=matches[0],
        status_model=model, prior_status=descriptor["status"], live_draft=None,
    )
    if pending is not None:
        return pending
    if observed is None:
        raise LifecycleError("draft-promotion-retry-missing", "the missing Draft has no sealed terminal promotion")
    return {
        "operation": "change_status",
        "outcome": "applied",
        "prior_status": descriptor["status"],
        "observed": carrier_descriptor(root, observed),
        "status_model": model,
        "effects": [_effect("unchanged", carrier=carrier_descriptor(root, observed), reason="terminal-promotion-retry")],
        "broken_references": [],
    }


def _broken_references(root: Path, atom: Atom) -> list[dict[str, Any]]:
    """Report active relation endpoints; never change or retarget them."""

    assert atom.atom_id is not None
    result: list[dict[str, Any]] = []
    for reference in sorted(set(_ATOM_REFERENCE.findall(atom.frontmatter)) - {atom.atom_id}):
        result.append({
            "direction": "outgoing",
            "relation_owner": atom.atom_id,
            "referenced_atom_id": reference,
            "reason": "target-status-becomes-inactive",
            "active_referrer": True,
        })
    try:
        atoms = scan_atoms(root, lifecycle="active")
    except AtomToolError as error:
        raise _translate(error) from error
    for candidate in atoms:
        if candidate.atom_id is None or candidate.atom_id == atom.atom_id:
            continue
        if atom.atom_id in _ATOM_REFERENCE.findall(candidate.frontmatter):
            result.append({
                "direction": "inbound",
                "relation_owner": candidate.atom_id,
                "referenced_atom_id": atom.atom_id,
                "reason": "target-status-becomes-inactive",
                "active_referrer": True,
            })
    return result


def create_atom_action(root: Path, parameters: Mapping[str, Any], *, execute: bool = False, authorized: bool = False) -> dict[str, Any]:
    """Apply or preview one complete Create carrier, without any outer Run policy."""

    root = root.resolve()
    request = _mapping(parameters, "parameters")
    _exact_fields(request, frozenset({"carrier"}), "parameters")
    carrier = _complete_carrier(request["carrier"])
    try:
        destination, _, _ = prepare_create_atom_revision(root, carrier["path"], carrier["frontmatter"])
        if destination.exists():
            existing = atom_from_path(root, destination)
            return {"operation": "create", "outcome": "duplicate", "requested": carrier,
                    "effects": [_effect("unchanged", carrier=carrier_descriptor(root, existing), reason="destination-already-exists")]}
    except AtomToolError as error:
        raise _translate(error) from error
    if not _execute_allowed(execute=execute, authorized=authorized):
        return {"operation": "create", "outcome": "preview", "requested": carrier,
                "effects": [_effect("unchanged", carrier=carrier, reason="preview")]}
    try:
        created = create_atom_revision(root, carrier["path"], carrier["frontmatter"], carrier["content"])
    except AtomToolError as error:
        if error.code in {"destination-collision", "atom-id-collision"}:
            return {"operation": "create", "outcome": "duplicate", "requested": carrier,
                    "effects": [_effect("unchanged", carrier=carrier, reason=error.code)]}
        raise _translate(error) from error
    observed = carrier_descriptor(root, created)
    return {"operation": "create", "outcome": "applied", "requested": carrier, "observed": observed,
            "effects": [_effect("changed", carrier=observed)], "history": {"prior": None}}


def update_atom_action(root: Path, parameters: Mapping[str, Any], *, execute: bool = False, authorized: bool = False) -> dict[str, Any]:
    """Apply one assessed identity-preserving Update or return a terminal handoff."""

    root = root.resolve()
    request = _mapping(parameters, "parameters")
    allowed = frozenset({"target", "proposed", "change_class", "successors", "legacy_identity_proof", "legacy_identity_mapping"})
    unknown = sorted(request.keys() - allowed)
    if unknown or not {"target", "proposed", "change_class"}.issubset(request):
        raise LifecycleError("update-parameters-invalid", "update requires target, complete proposed carrier, and change_class only")
    legacy = "legacy_identity_proof" in request
    mapping = None
    if "legacy_identity_mapping" in request:
        if not legacy:
            raise LifecycleError("identity-mapping-invalid", "explicit legacy mapping requires an exact historical proof")
        mapping = _mapping(request["legacy_identity_mapping"], "legacy_identity_mapping")
        _exact_fields(mapping, frozenset({"legacy_atom_id", "atom_id", "destination"}), "legacy_identity_mapping")
        if (not isinstance(mapping["atom_id"], str) or re.fullmatch(r"CA-[CAPRMEDO]-[0-9]{3,}", mapping["atom_id"]) is None
                or mapping["legacy_atom_id"] != _mapping(request["target"], "target").get("atom_id")
                or not isinstance(mapping["destination"], str)):
            raise LifecycleError("identity-mapping-invalid", "mapping must bind one exact legacy identity to a canonical identity and destination")
    target = (_resolve_legacy_descriptor(root, request["target"], request["legacy_identity_proof"],
                                        mapped_identity=mapping["atom_id"] if mapping else None)
              if legacy else _resolve_descriptor(root, request["target"], name="target", active=False))
    prior = carrier_descriptor(root, target)
    proposed = _proposal(request["proposed"])
    change_class = request["change_class"]
    if change_class not in _UPDATE_CLASSES:
        raise LifecycleError("change-class-unadmitted", "update change_class is not identity-preserving")
    expected_identity = mapping["atom_id"] if mapping else target.atom_id
    if frontmatter_scalar(proposed["frontmatter"], "atom_id") != expected_identity:
        raise LifecycleError("atom-identity-changed", "same-identity update must retain the current atom_id")
    if legacy:
        expected_role = {"C": "Concern", "A": "Analysis", "P": "Plan", "R": "Requirement", "M": "Method",
                         "E": "Evaluation", "D": "Delivery", "O": "Operations"}[expected_identity.split("-")[1]]
        if frontmatter_scalar(proposed["frontmatter"], "content_role") != expected_role:
            raise LifecycleError("atom-identity-changed", "legacy migration must retain the assigned Content Role")
    old_status = frontmatter_scalar(target.frontmatter, "status")
    new_status = frontmatter_scalar(proposed["frontmatter"], "status")
    if new_status != old_status and not (legacy and old_status is None and new_status == "Active"):
        raise LifecycleError("status-change-requires-change-status", "Update cannot carry a status transition")
    prior_summary = _legacy_summary(target.content) if legacy else _summary(target.content)
    if _summary(proposed["content"]) != prior_summary:
        if mapping:
            raise LifecycleError("legacy-summary-changed", "identity encoding migration must preserve the exact Summary")
        proposed_successors = _proposed_successors(root, request.get("successors"), target)
        return {
            "operation": "update",
            "outcome": "replace_handoff",
            "predecessor": prior,
            "replace_handoff": {"predecessor": prior, "successors": proposed_successors},
            "effects": [_effect("unchanged", carrier=prior, reason="summary-change-requires-separate-replace")],
            "history": {"prior": prior, "preserved": True},
        }
    if mapping:
        try:
            destination, _, destination_id = prepare_create_atom_revision(root, mapping["destination"], proposed["frontmatter"])
        except AtomToolError as error:
            raise _translate(error) from error
        if destination.parent != target.path.parent or destination_id != expected_identity:
            raise LifecycleError("identity-mapping-invalid", "canonical destination must preserve the source scope and Content Role")
        if destination.exists():
            raise LifecycleError("destination-collision", "canonical destination already exists")
        if any(atom.atom_id == expected_identity for atom in scan_atoms(root)):
            raise LifecycleError("atom-id-collision", "canonical identity was already used")
        for candidate in control_root(root).rglob("*.md"):
            if re.search(rf"(?:^|-){re.escape(expected_identity)}(?=-|@|\.)", candidate.name):
                raise LifecycleError("atom-id-collision", "canonical identity was already used by a historical or unnormalized carrier")
    if proposed["frontmatter"] == target.frontmatter and proposed["content"] == target.content and not mapping:
        return {"operation": "update", "outcome": "no-op", "observed": prior,
                "effects": [_effect("unchanged", carrier=prior, reason="equivalent-carrier")], "history": {"prior": prior, "preserved": True}}
    if not _execute_allowed(execute=execute, authorized=authorized):
        return {"operation": "update", "outcome": "preview", "observed": prior,
                "effects": [_effect("unchanged", carrier=prior, reason="preview")], "history": {"prior": prior}}
    next_version = atom_version(target) + 1 if change_class == "semantic_revision" else atom_version(target)
    prior_revision: Atom | None = None
    try:
        frontmatter = _refresh_frontmatter(proposed["frontmatter"], version=next_version)
        draft_history: tuple[dict[str, str], dict[str, Any], dict[str, Any] | None] | None = None
        if target.lifecycle == "draft":
            from draft_history import DraftHistoryError, append_draft_entry, reserve_history_entry, validate_current_draft_head

            prior_lineage = draft_revision_lineage(target.frontmatter)
            if not isinstance(prior_lineage, Mapping) or set(prior_lineage) != {"history_entry_ref"}:
                raise LifecycleError("draft-lineage-invalid", "Draft Update requires one retained-history head")
            parent = dict(prior_lineage["history_entry_ref"])
            try:
                # Validate this exact current carrier before reserving a child:
                # an otherwise-valid entry for another Draft is never a parent.
                parent_entry = validate_current_draft_head(root, target.relative, parent)
            except DraftHistoryError as error:
                raise LifecycleError("draft-lineage-invalid", "Draft Update requires its own current retained-history head") from error
            history_ref = reserve_history_entry(root)
            frontmatter = replace_draft_revision_lineage(frontmatter, {"history_entry_ref": history_ref})
            draft_history = (history_ref, parent, parent_entry.get("direct_predecessor"))
        if change_class == "semantic_revision" or legacy:
            prior_revision = preserve_atom_revision(root, target)
        if mapping:
            observed_atom = migrate_atom_identity_revision(root, target, mapping["destination"], frontmatter, proposed["content"])
        else:
            write_atom_revision(target, frontmatter, proposed["content"])
            observed_atom = atom_from_path(root, target.path)
            if draft_history is not None:
                history_ref, parent, predecessor = draft_history
                append_draft_entry(root, observed_atom.relative, reference=history_ref,
                                   origin={"kind": "draft_update"}, parent_history_entry_ref=parent,
                                   direct_predecessor=predecessor)
    except BaseException as error:
        if prior_revision is not None:
            prior_revision.path.unlink(missing_ok=True)
        if isinstance(error, AtomToolError):
            raise _translate(error) from error
        raise
    observed = carrier_descriptor(root, observed_atom)
    history: dict[str, Any] = {"prior": prior, "revision_class": change_class}
    if prior_revision is not None:
        history["prior_revision"] = carrier_descriptor(root, prior_revision)
    if mapping:
        history["identity_mapping"] = dict(mapping)
    effects = [_effect("changed", carrier=observed)]
    if mapping and prior_revision is not None:
        effects.extend([_effect("changed", carrier=carrier_descriptor(root, prior_revision)),
                        {"state": "changed", "carrier": prior, "operation": "relocated_to_canonical_encoding"}])
    return {"operation": "update", "outcome": "applied", "observed": observed,
            "effects": effects,
            "history": history}


def change_status_atom_action(root: Path, parameters: Mapping[str, Any], *, execute: bool = False, authorized: bool = False) -> dict[str, Any]:
    """Apply one source-model-derived status change; callers cannot supply a model."""

    root = root.resolve()
    missing_retry = _missing_draft_promotion_retry(root, parameters)
    if missing_retry is not None:
        return missing_retry
    preflight = preflight_atom_lifecycle(root, "change_status", parameters)
    target, prior = preflight["target"], preflight["prior"]
    requested, current_status = preflight["requested_status"], preflight["current_status"]
    model, archive = preflight["status_model"], preflight["archive"]
    if requested == current_status:
        return {"operation": "change_status", "outcome": "no-op", "prior_status": current_status,
                "observed": prior, "status_model": model,
                "effects": [_effect("unchanged", carrier=prior, reason="status-already-current")], "broken_references": []}
    promotion_head = _draft_promotion_head(root, target) if target.atom_id is None else None
    # An ID-free Draft may have a sealed pending promotion.  Its request/head
    # binding must refuse or recover before archive diagnostics dereference an
    # identity that deliberately does not exist yet.
    diagnostics = _broken_references(root, target) if archive and target.atom_id is not None else []
    if not _execute_allowed(execute=execute, authorized=authorized):
        return {"operation": "change_status", "outcome": "preview", "prior_status": current_status, "observed": prior,
                "status_model": model,
                "effects": [_effect("unchanged", carrier=prior, reason="preview")], "broken_references": diagnostics}
    refreshed = preflight_atom_lifecycle(root, "change_status", parameters)
    if refreshed["status_model"] != model:
        raise LifecycleError("status-model-stale", "authoritative status-model source changed after preflight")
    prior_revision: Atom | None = None
    try:
        frontmatter = replace_frontmatter_scalar(target.frontmatter, "status", requested)
        frontmatter = _refresh_frontmatter(frontmatter)
        if requested.casefold() == "draft":
            from draft_history import append_draft_entry, reserve_history_entry

            prior_revision = preserve_atom_revision(root, target, allow_nonactive=True)
            prior_seal = carrier_descriptor(root, prior_revision)
            predecessor = {"atom_id": target.atom_id, "version": atom_version(target),
                           "content_role": frontmatter_scalar(target.frontmatter, "content_role"),
                           "summary": _summary(target.content), "digest": atom_digest(target),
                           "immutable_locator": {"history_revision": atom_version(target), "path": prior_seal["path"]}}
            history_ref = reserve_history_entry(root)
            frontmatter = replace_draft_revision_lineage(frontmatter, {"history_entry_ref": history_ref})
            observed_atom = demote_atom_to_draft(root, target, frontmatter, target.content)
            append_draft_entry(root, observed_atom.relative, reference=history_ref,
                               origin={"kind": "demoted_identified"}, direct_predecessor=predecessor)
        elif promotion_head is not None:
            from draft_promotion_pending import PendingPromotionError, finalize_pending_promotion, reserve_pending_promotion

            head, head_entry = promotion_head
            recovered_atom, pending = _pending_promotion_result(
                root, parameters, prior=prior, draft_path=target.relative, head=head,
                status_model=model, prior_status=current_status, live_draft=target,
            )
            if pending is not None:
                return pending
            if recovered_atom is not None:
                observed_atom = recovered_atom
            else:
                # No pending reservation exists for this trusted head.  This is
                # the one path permitted to select an identity and prepare bytes.
                promotion_identity = _draft_promotion_identity(root, target, head_entry=head_entry)
                destination, _, output_bytes = prepare_draft_promotion(root, target, promotion_identity, frontmatter, target.content)
                try:
                    reservation_result = reserve_pending_promotion(
                        root, draft_path=target.relative, head=head, request=dict(parameters), planned_atom_id=promotion_identity,
                        output_path=destination.relative_to(root).as_posix(), output_digest=hashlib.sha256(output_bytes).hexdigest(),
                    )
                except PendingPromotionError as error:
                    raise LifecycleError(error.code, str(error)) from error
                if reservation_result["disposition"] == "finalized":
                    recovered_atom, pending = _pending_promotion_result(
                        root, parameters, prior=prior, draft_path=target.relative, head=head,
                        status_model=model, prior_status=current_status, live_draft=target,
                    )
                    if pending is not None:
                        return pending
                    if recovered_atom is None:
                        raise LifecycleError("promotion-history-conflict", "finalized pending promotion did not resolve its output")
                    observed_atom = recovered_atom
                else:
                    observed_atom = promote_draft_atom(root, target, promotion_identity, frontmatter, target.content, consume_draft=False)
                    try:
                        finalization = finalize_pending_promotion(root, reservation_result["reservation"])
                    except PendingPromotionError as error:
                        raise LifecycleError(error.code, str(error)) from error
                    if finalization["disposition"] != "finalized":
                        return {"operation": "change_status", "outcome": "pending", "prior_status": current_status,
                                "observed": carrier_descriptor(root, observed_atom), "status_model": model,
                                "effects": [_effect("changed", carrier=carrier_descriptor(root, observed_atom))],
                                "pending_promotion": finalization}
                    recovered_atom, pending = _pending_promotion_result(
                        root, parameters, prior=prior, draft_path=target.relative, head=head,
                        status_model=model, prior_status=current_status, live_draft=target,
                    )
                    if pending is not None:
                        return pending
                    if recovered_atom is None:
                        raise LifecycleError("promotion-history-conflict", "finalized promotion did not resolve its output")
                    observed_atom = recovered_atom
        else:
            observed_atom = (
                archive_atom_revision(root, target, frontmatter, target.content)
                if archive
                else move_atom_revision(root, target, _status_destination(root, target, requested), frontmatter, target.content)
            )
    except AtomToolError as error:
        if prior_revision is not None:
            prior_revision.path.unlink(missing_ok=True)
        raise _translate(error) from error
    observed = carrier_descriptor(root, observed_atom)
    result: dict[str, Any] = {
        "operation": "change_status",
        "outcome": "applied",
        "prior_status": current_status,
        "observed": observed,
        "status_model": model,
        "effects": [_effect("changed", carrier=observed)],
        "broken_references": diagnostics,
    }
    if archive:
        result["repair_handoff"] = {"operation": "repair_relations", "broken_references": diagnostics,
                                    "automatic_repair": False}
    if requested.casefold() == "draft":
        assert prior_revision is not None
        result["history"] = {"prior": prior, "prior_revision": carrier_descriptor(root, prior_revision)}
    return result


def replace_atom_action(root: Path, parameters: Mapping[str, Any], *, execute: bool = False, authorized: bool = False) -> dict[str, Any]:
    """Publish supplied successors before archiving one predecessor."""

    root = root.resolve()
    request = _mapping(parameters, "parameters")
    _exact_fields(request, frozenset({"predecessor", "successors", "status_model"}), "parameters")
    predecessor = _resolve_descriptor(root, request["predecessor"], name="predecessor")
    prior = carrier_descriptor(root, predecessor)
    successors = _proposed_successors(root, request["successors"], predecessor)
    try:
        existing_ids = {atom.atom_id for atom in scan_atoms(root) if atom.atom_id is not None}
        for successor in successors:
            destination, _, atom_id = prepare_create_atom_revision(root, successor["path"], successor["frontmatter"])
            if destination.exists():
                raise AtomToolError("destination-collision", f"Atom destination already exists: {destination.relative_to(root)}")
            if atom_id is not None and atom_id in existing_ids:
                raise AtomToolError("atom-id-collision", f"Atom ID already exists: {atom_id}")
    except AtomToolError as error:
        raise _translate(error) from error
    supplied_model = _mapping(request["status_model"], "status_model")
    supplied_archive_status = supplied_model.get("archive_status")
    if not isinstance(supplied_archive_status, str) or not supplied_archive_status:
        raise LifecycleError("archive-status-unavailable", "qualified status model does not define an Archive shortcut")
    model = _status_model(supplied_model, predecessor, supplied_archive_status)
    archive_status = model["archive_status"]
    if archive_status is None:
        raise LifecycleError("archive-status-unavailable", "qualified status model does not define an Archive shortcut")
    if not _execute_allowed(execute=execute, authorized=authorized):
        return {"operation": "replace", "outcome": "preview", "predecessor": prior, "successors": successors,
                "effects": [_effect("unchanged", carrier=prior, reason="preview")], "history": {"predecessor": prior}}
    published: list[dict[str, Any]] = []
    try:
        for successor in successors:
            created = create_atom_revision(root, successor["path"], successor["frontmatter"], successor["content"])
            published.append(carrier_descriptor(root, created))
        frontmatter = replace_frontmatter_scalar(predecessor.frontmatter, "status", archive_status)
        frontmatter = _refresh_frontmatter(frontmatter)
        archived = archive_atom_revision(root, predecessor, frontmatter, predecessor.content)
    except AtomToolError as error:
        if not published:
            raise _translate(error) from error
        phase = "archive_predecessor" if len(published) == len(successors) else "publish_successor"
        effects = [_effect("changed", carrier=carrier) for carrier in published]
        effects.append({"state": "unknown", "phase": phase, "reason": error.code})
        return {
            "operation": "replace",
            "outcome": "partial",
            "predecessor": prior,
            "successors": published,
            "effects": effects,
            "unknown_remainder": [{"phase": phase, "code": error.code, "message": error.message}],
            "history": {"predecessor": prior, "successors": published},
        }
    observed = carrier_descriptor(root, archived)
    return {"operation": "replace", "outcome": "applied", "predecessor": observed, "successors": published,
            "effects": [_effect("changed", carrier=carrier) for carrier in [*published, observed]],
            "history": {"predecessor": prior, "successors": published}}
