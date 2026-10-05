"""Shared no-mutation lifecycle-intent support for CA-R-1041 and CA-R-1042."""

from __future__ import annotations

import argparse
from datetime import datetime
import json
import re
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
    control_root,
    create_atom_revision,
    demote_atom_to_draft,
    frontmatter_scalar,
    move_atom_revision,
    prepare_create_atom_revision,
    preserve_atom_revision,
    replace_frontmatter_scalar,
    resolve_repository,
    resolve_selector,
    safe_path,
    scan_atoms,
    write_atom_revision,
)


ATOM_ID = re.compile(r"^CA-[A-Z]+-[0-9]{3,}$")
INACTIVE_LIFECYCLE_SEGMENTS = frozenset({"archive", "drafts", "done", "solved", "canceled", "cancelled"})


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
    _exact_fields(request, frozenset({"target", "status"}), "parameters")
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
    allowed = frozenset({"target", "proposed", "change_class", "successors"})
    unknown = sorted(request.keys() - allowed)
    if unknown or not {"target", "proposed", "change_class"}.issubset(request):
        raise LifecycleError("update-parameters-invalid", "update requires target, complete proposed carrier, and change_class only")
    target = _resolve_descriptor(root, request["target"], name="target")
    prior = carrier_descriptor(root, target)
    proposed = _proposal(request["proposed"])
    change_class = request["change_class"]
    if change_class not in _UPDATE_CLASSES:
        raise LifecycleError("change-class-unadmitted", "update change_class is not identity-preserving")
    if frontmatter_scalar(proposed["frontmatter"], "atom_id") != target.atom_id:
        raise LifecycleError("atom-identity-changed", "same-identity update must retain the current atom_id")
    if frontmatter_scalar(proposed["frontmatter"], "status") != frontmatter_scalar(target.frontmatter, "status"):
        raise LifecycleError("status-change-requires-change-status", "Update cannot carry a status transition")
    if _summary(proposed["content"]) != _summary(target.content):
        proposed_successors = _proposed_successors(root, request.get("successors"), target)
        return {
            "operation": "update",
            "outcome": "replace_handoff",
            "predecessor": prior,
            "replace_handoff": {"predecessor": prior, "successors": proposed_successors},
            "effects": [_effect("unchanged", carrier=prior, reason="summary-change-requires-separate-replace")],
            "history": {"prior": prior, "preserved": True},
        }
    if proposed["frontmatter"] == target.frontmatter and proposed["content"] == target.content:
        return {"operation": "update", "outcome": "no-op", "observed": prior,
                "effects": [_effect("unchanged", carrier=prior, reason="equivalent-carrier")], "history": {"prior": prior, "preserved": True}}
    if not _execute_allowed(execute=execute, authorized=authorized):
        return {"operation": "update", "outcome": "preview", "observed": prior,
                "effects": [_effect("unchanged", carrier=prior, reason="preview")], "history": {"prior": prior}}
    next_version = atom_version(target) + 1 if change_class == "semantic_revision" else atom_version(target)
    prior_revision: Atom | None = None
    try:
        frontmatter = _refresh_frontmatter(proposed["frontmatter"], version=next_version)
        if change_class == "semantic_revision":
            prior_revision = preserve_atom_revision(root, target)
        write_atom_revision(target, frontmatter, proposed["content"])
        observed_atom = atom_from_path(root, target.path)
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
    return {"operation": "update", "outcome": "applied", "observed": observed,
            "effects": [_effect("changed", carrier=observed)],
            "history": history}


def change_status_atom_action(root: Path, parameters: Mapping[str, Any], *, execute: bool = False, authorized: bool = False) -> dict[str, Any]:
    """Apply one source-model-derived status change; callers cannot supply a model."""

    root = root.resolve()
    preflight = preflight_atom_lifecycle(root, "change_status", parameters)
    target, prior = preflight["target"], preflight["prior"]
    requested, current_status = preflight["requested_status"], preflight["current_status"]
    model, archive = preflight["status_model"], preflight["archive"]
    if requested == current_status:
        return {"operation": "change_status", "outcome": "no-op", "prior_status": current_status,
                "observed": prior, "status_model": model,
                "effects": [_effect("unchanged", carrier=prior, reason="status-already-current")], "broken_references": []}
    if target.atom_id is None:
        raise LifecycleError("draft-promotion-identity-unavailable", "leaving Draft requires separately admitted identity assignment")
    diagnostics = _broken_references(root, target) if archive else []
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
            prior_revision = preserve_atom_revision(root, target, allow_nonactive=True)
            observed_atom = demote_atom_to_draft(root, target, frontmatter, target.content)
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
