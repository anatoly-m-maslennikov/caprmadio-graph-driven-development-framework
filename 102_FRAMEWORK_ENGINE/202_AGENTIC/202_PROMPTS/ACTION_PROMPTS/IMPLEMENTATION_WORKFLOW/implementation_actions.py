"""Source-bound handlers for the seven current CA-O-016 Actions.

The graph executor owns transitions.  These handlers validate one supplied
packet, call a replaceable Agent adapter, and return a truthful envelope.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path
from typing import Any, Callable, Mapping


HERE = Path(__file__).parent
ROOT = HERE.parents[4]
ACTION_BY_STEP = {
    "CA-O-091": ("CA-O-017", "Integrated"),
    "CA-O-092": ("CA-O-018", "Isolated"),
    "CA-O-093": ("CA-O-019", "Isolated"),
    "CA-O-094": ("CA-O-020", "Integrated"),
    "CA-O-095": ("CA-O-089", "Isolated"),
    "CA-O-096": ("CA-O-024", "Integrated"),
    "CA-O-099": ("CA-O-021", "Isolated"),
}
RESULTS = {
    "CA-O-091": {"evaluation_ready", "requirement_ready", "evaluation_runnable", "complete", "blocked"},
    "CA-O-092": {"prepared", "blocked"}, "CA-O-093": {"implemented", "blocked"},
    "CA-O-094": {"passed", "failed", "blocked"},
    "CA-O-095": {"expected_initial_failure", "implementation_defect", "test_implementation_defect", "authority_change_required", "environment_blocker", "unresolved"},
    "CA-O-096": {"retry_permitted", "retry_blocked"},
    "CA-O-099": {"repaired", "authority_change_required", "blocked"},
}
ACTION_HANDLERS: dict[str, Callable[..., dict[str, Any]]] = {}
SELECTED_PROJECT_SOURCE_ROOT = ".caprmedio_caprmedio"
_BINDING_FIELDS = frozenset({"atom_id", "version", "path", "sha256"})
_SELECTED_PROJECT_FIELDS = frozenset({"kind", "source_root", "source_references"})
_INPUT_BINDING_FIELDS = _BINDING_FIELDS | {"content"}
_E_REQUIRED_STEPS = frozenset({"CA-O-092", "CA-O-094"})
_RED_REQUIRED_STEPS = frozenset({"CA-O-092", "CA-O-093", "CA-O-094", "CA-O-095", "CA-O-096", "CA-O-099"})
_WORK_BOUNDARY_STEPS = frozenset({"CA-O-092", "CA-O-093", "CA-O-094", "CA-O-095", "CA-O-099"})
_IDENTITY_KEYS = ("id", "identity", "name", "ref", "candidate_id", "phase_id")
_AUTHORIZATION_FIELDS = frozenset({
    "authorization_ref", "authorization_freshness", "request_id", "operation_route",
    "proposal_receipt_digest", "parameters_digest", "target_frontier_digest", "effects_digest",
    "definition_manifest", "source_freshness",
})
_DIGEST = re.compile(r"[0-9a-f]{64}")


def _trusted_project_root(selected_project_root: str | Path | None) -> Path:
    """Return a root supplied by the graph owner, never by a packet field."""
    if selected_project_root is None:
        return ROOT.resolve(strict=True)
    root = Path(selected_project_root)
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise ValueError("trusted selected Project root must be an absolute, non-symlink directory")
    return root.resolve(strict=True)


def _safe_source_path(value: object) -> Path:
    if not isinstance(value, str) or not value:
        raise ValueError("selected Project source path is missing")
    path = Path(value)
    source_root = Path(SELECTED_PROJECT_SOURCE_ROOT)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("selected Project source path must be safe and relative")
    try:
        path.relative_to(source_root)
    except ValueError as error:
        raise ValueError("selected Project source path escapes its source root") from error
    return path


def _read_bound_source(root: Path, path: object) -> bytes:
    relative = _safe_source_path(path)
    candidate = root / relative
    try:
        resolved = candidate.resolve(strict=True)
    except OSError as error:
        raise ValueError(f"selected Project source is missing: {relative}") from error
    if candidate.is_symlink() or resolved != candidate or not resolved.is_relative_to(root) or not resolved.is_file():
        raise ValueError(f"selected Project source is outside its frozen root: {relative}")
    return resolved.read_bytes()


def _reviewed_binding_rows() -> list[dict[str, Any]]:
    payload = json.loads((HERE / "source_bindings.json").read_text(encoding="utf-8"))
    rows = payload.get("sources") if isinstance(payload, Mapping) else None
    if not isinstance(rows, list) or not rows:
        raise ValueError("reviewed source bindings are missing")
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    checked: list[dict[str, Any]] = []
    for row in rows:
        if not isinstance(row, Mapping) or set(row) != _BINDING_FIELDS:
            raise ValueError("reviewed source binding has an invalid shape")
        atom_id, version, path, digest = row["atom_id"], row["version"], row["path"], row["sha256"]
        if (not isinstance(atom_id, str) or not isinstance(version, int) or version < 1 or
                not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest)):
            raise ValueError("reviewed source binding has an invalid identity")
        _safe_source_path(path)
        if atom_id in seen_ids or path in seen_paths:
            raise ValueError("reviewed source binding is duplicated")
        seen_ids.add(atom_id)
        seen_paths.add(path)
        checked.append(dict(row))
    return checked


def current_source_bindings(selected_project_root: str | Path | None = None) -> list[dict[str, Any]]:
    """Read the reviewed prompt-authority frontier used by every invocation."""
    root = _trusted_project_root(selected_project_root)
    rows = _reviewed_binding_rows()
    for row in rows:
        raw = _read_bound_source(root, row["path"])
        version = re.search(r'^version: ?["\']?(\d+)', raw.decode("utf-8"), re.M)
        if not version or hashlib.sha256(raw).hexdigest() != row["sha256"] or int(version[1]) != row["version"]:
            raise ValueError(f"stale reviewed source binding: {row['atom_id']}")
    return rows


def prepare_input_bindings(atom_ids: list[str],
                           selected_project_root: str | Path | None = None) -> list[dict[str, Any]]:
    """Build complete invocation bindings for selected R/D/E source Atoms."""
    root = _trusted_project_root(selected_project_root)
    current = {row["atom_id"]: row for row in current_source_bindings(selected_project_root)}
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    for atom_id in atom_ids:
        if not isinstance(atom_id, str) or atom_id in seen:
            raise ValueError("invocation source Atoms must have unique identities")
        row = current.get(atom_id)
        if row is None:
            raise ValueError(f"invocation source Atom is not current: {atom_id}")
        raw = _read_bound_source(root, row["path"])
        result.append({**row, "content": raw.decode("utf-8")})
        seen.add(atom_id)
    return result


def prepare_method_projection(method_paths: list[str | Path],
                              selected_project_root: str | Path | None = None) -> dict[str, Any]:
    """Build a verified, full-content active-M input distinct from selected R/D/E."""
    root = _trusted_project_root(selected_project_root)
    selected_project = selected_project_root is not None
    entries = []
    for supplied in (Path(p) for p in method_paths):
        if selected_project:
            if supplied.is_absolute():
                raise ValueError("selected Project Method path must be relative")
            raw = _read_bound_source(root, supplied.as_posix())
            path = root / supplied
        else:
            path = supplied if supplied.is_absolute() else root / supplied
            raw = path.read_bytes()
        text = raw.decode("utf-8")
        atom = re.search(r'^atom_id: ?["\']?([^"\'\n]+)', text, re.M)
        version = re.search(r'^version: ?["\']?(\d+)', text, re.M)
        if not atom or not version or "content_role: \"Method\"" not in text and "content_role: Method" not in text or not re.search(r'^status: ?["\']?Active', text, re.M):
            raise ValueError(f"not a current active Method: {supplied}")
        relative = path.resolve().relative_to(root).as_posix()
        entries.append((atom[1], int(version[1]), relative, raw, text))
    entries.sort(key=lambda entry: (entry[0], entry[1]))
    rows = [{"atom_id": atom, "version": version, "path": relative,
             "sha256": hashlib.sha256(raw).hexdigest()}
            for atom, version, relative, raw, _ in entries]
    parts = [text for _, _, _, _, text in entries]
    if not rows:
        raise ValueError("empty active-M projection")
    return {"content": "\n\n".join(parts), "sources": rows}


def compile_active_methods(packet: Mapping[str, Any],
                           selected_project_root: str | Path | None = None) -> Mapping[str, Any]:
    """Return the supplied verified M projection without mixing it with RED."""
    projection = packet.get("method_projection")
    if not isinstance(projection, Mapping) or not projection.get("content") or not isinstance(projection.get("sources"), list):
        raise ValueError("missing verified active-M projection")
    try:
        expected_paths = [row["path"] for row in current_source_bindings(selected_project_root)
                          if row["atom_id"].startswith("CA-M-")]
        expected = prepare_method_projection(expected_paths, selected_project_root)
    except (KeyError, OSError, UnicodeDecodeError, ValueError) as error:
        raise ValueError(f"invalid active-M projection: {error}") from error
    if projection != expected:
        raise ValueError("active-M projection content, source, digest, or currentness mismatch")
    return expected


def _nonempty(value: object) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, (list, tuple, set)):
        return bool(value)
    return value is not None


def _number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{label} must be a finite number")
    return float(value)


def _first(mapping: Mapping[str, Any], *keys: str) -> object:
    for key in keys:
        if key in mapping:
            return mapping[key]
    return None


def _identity_token(value: object) -> object:
    if isinstance(value, Mapping):
        return _first(value, *_IDENTITY_KEYS)
    return value


def _validate_input_bindings(value: object, role: str, current: Mapping[str, Mapping[str, Any]],
                             root: Path, *, required: bool) -> None:
    if value is None:
        if required:
            raise ValueError(f"selected {role} input bindings are missing")
        return
    if not isinstance(value, list):
        raise ValueError(f"selected {role} input bindings must be a list")
    if required and not value:
        raise ValueError(f"selected {role} input bindings are required")
    seen: set[str] = set()
    for reference in value:
        if not isinstance(reference, Mapping) or set(reference) != _INPUT_BINDING_FIELDS:
            raise ValueError(f"selected {role} input binding must include full content and source identity")
        atom_id = reference.get("atom_id")
        if not isinstance(atom_id, str) or atom_id in seen or not atom_id.startswith(f"CA-{role}-"):
            raise ValueError(f"selected {role} input binding has an invalid or duplicate identity")
        expected = current.get(atom_id)
        if expected is None or any(reference.get(field) != expected[field] for field in _BINDING_FIELDS):
            raise ValueError(f"selected {role} input binding is stale or not in the reviewed frontier")
        content = reference.get("content")
        if not isinstance(content, str) or not content:
            raise ValueError(f"selected {role} input binding content is missing")
        raw = _read_bound_source(root, expected["path"])
        if content != raw.decode("utf-8") or hashlib.sha256(raw).hexdigest() != reference["sha256"]:
            raise ValueError(f"selected {role} input binding content is stale")
        seen.add(atom_id)


def _validate_red(packet: Mapping[str, Any], step: str) -> None:
    if step not in _RED_REQUIRED_STEPS:
        return
    red = packet.get("red")
    if not isinstance(red, Mapping):
        raise ValueError("complete RED input is missing")
    expectation = _first(red, "expectation", "expected", "assertion")
    fixtures = _first(red, "fixtures", "inputs", "test_inputs")
    commands = _first(red, "commands", "reproduction", "reproducer")
    if not _nonempty(expectation):
        raise ValueError("RED expectation is missing")
    if not isinstance(fixtures, (list, tuple)) or not fixtures:
        raise ValueError("RED fixtures are missing")
    if not isinstance(commands, (list, tuple)) or not commands:
        raise ValueError("RED reproduction commands are missing")


def _validate_plan_and_scope(packet: Mapping[str, Any], step: str) -> None:
    plan_item = packet.get("plan_item")
    if not isinstance(plan_item, Mapping):
        raise ValueError("selected P/Plan item is missing")
    item_id = _first(plan_item, "item_id", "id", "plan_item_id")
    dod = _first(plan_item, "dod", "definition_of_done")
    if not _nonempty(item_id) or not _nonempty(dod):
        raise ValueError("selected P/Plan item and Definition of Done are incomplete")
    if isinstance(dod, (list, tuple)) and not all(_nonempty(item) for item in dod):
        raise ValueError("selected Definition of Done contains an empty condition")
    estimated = plan_item.get("estimated_minutes")
    if isinstance(estimated, bool) or not isinstance(estimated, (int, float)) or estimated <= 0:
        raise ValueError("selected P/Plan item estimate is missing or invalid")
    if step in _WORK_BOUNDARY_STEPS:
        owned_paths = packet.get("owned_paths", plan_item.get("owned_paths"))
        if not isinstance(owned_paths, (list, tuple)) or not owned_paths or not all(
                isinstance(path, str) and path.strip() for path in owned_paths):
            raise ValueError("owned implementation boundary is missing")
    candidate = packet.get("candidate")
    phase = packet.get("phase")
    if not _nonempty(candidate) or not _nonempty(phase):
        raise ValueError("current candidate and execution phase are missing")
    if isinstance(candidate, Mapping) and not _nonempty(_first(candidate, *_IDENTITY_KEYS)):
        raise ValueError("current candidate identity is missing")
    if isinstance(phase, Mapping) and not _nonempty(_first(phase, *_IDENTITY_KEYS)):
        raise ValueError("execution phase identity is missing")


def _validate_confidence(packet: Mapping[str, Any]) -> None:
    confidence = packet.get("confidence")
    if not isinstance(confidence, Mapping):
        raise ValueError("effective confidence binding is missing")
    effective = _first(confidence, "effective", "threshold", "effective_threshold")
    observed = _first(confidence, "observed", "value", "confidence")
    source = _first(confidence, "source", "source_ref", "provenance")
    effective_value = _number(effective, "effective confidence")
    observed_value = _number(observed, "observed confidence")
    if not _nonempty(source):
        raise ValueError("effective confidence source is missing")
    if observed_value < effective_value:
        raise ValueError("observed confidence is below the effective threshold")


def _validate_authorization(packet: Mapping[str, Any]) -> Mapping[str, Any]:
    """Require the existing sealed execution authorization, never a caller boolean."""
    authorization = packet.get("operator_authorization")
    if not isinstance(authorization, Mapping) or set(authorization) != _AUTHORIZATION_FIELDS:
        raise ValueError("current Operator authorization evidence is missing or incomplete")
    if not _nonempty(authorization.get("authorization_ref")):
        raise ValueError("current Operator authorization reference is missing")
    freshness = authorization.get("authorization_freshness")
    if (not isinstance(freshness, Mapping) or set(freshness) != {"state", "digest"}
            or freshness.get("state") != "current"
            or not isinstance(freshness.get("digest"), str)
            or not _DIGEST.fullmatch(freshness["digest"])):
        raise ValueError("current Operator authorization freshness is invalid")
    for field in ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                  "target_frontier_digest", "effects_digest"):
        value = authorization.get(field)
        if field.endswith("_digest"):
            if not isinstance(value, str) or not _DIGEST.fullmatch(value):
                raise ValueError(f"current Operator authorization {field} is invalid")
        elif not _nonempty(value):
            raise ValueError(f"current Operator authorization {field} is missing")
    manifest = authorization.get("definition_manifest")
    if (not isinstance(manifest, Mapping) or not _nonempty(manifest.get("manifest_ref"))
            or not isinstance(manifest.get("manifest_digest"), str)
            or not _DIGEST.fullmatch(manifest["manifest_digest"])):
        raise ValueError("current Operator authorization definition binding is invalid")
    if not isinstance(authorization.get("source_freshness"), Mapping) or not authorization["source_freshness"]:
        raise ValueError("current Operator authorization source freshness is missing")
    return authorization


def _validate_retry(packet: Mapping[str, Any], step: str,
                    trusted_execution_authorization: Mapping[str, Any] | None = None) -> None:
    retry = packet.get("retry")
    if not isinstance(retry, Mapping):
        raise ValueError("effective retry setting is missing")
    consumed = retry.get("consumed")
    limit = _first(retry, "effective_limit", "limit")
    source = _first(retry, "source", "source_ref", "provenance")
    if isinstance(consumed, bool) or not isinstance(consumed, int) or consumed < 0:
        raise ValueError("retained retry consumption is missing or invalid")
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("effective retry limit is missing or invalid")
    if not _nonempty(source):
        raise ValueError("effective retry source is missing")
    if step == "CA-O-096":
        if retry.get("remaining_failure") is not True:
            raise ValueError("remaining implementation failure is not admitted")
        if consumed >= limit:
            raise ValueError("retry allowance is exhausted")
        permissions = packet.get("permissions")
        retry_permission = permissions.get("retry") if isinstance(permissions, Mapping) else None
        authorization = _validate_authorization(packet)
        if trusted_execution_authorization is None:
            raise ValueError("retry requires retained selected-execution authorization evidence")
        trusted_packet = {"operator_authorization": trusted_execution_authorization}
        trusted = _validate_authorization(trusted_packet)
        if dict(authorization) != dict(trusted):
            raise ValueError("retry authorization differs from retained selected-execution evidence")
        if (not isinstance(retry_permission, Mapping)
                or not _nonempty(_first(retry_permission, "source", "source_ref", "provenance"))
                or retry_permission.get("authorization_ref") != authorization["authorization_ref"]):
            raise ValueError("retry permission is not bound to current Operator authorization")
    if step == "CA-O-099" and retry.get("admitted") is not True:
        raise ValueError("repair retry has not been admitted")


def _validate_coverage(packet: Mapping[str, Any], step: str) -> None:
    if step != "CA-O-094":
        return
    coverage = packet.get("coverage")
    if not isinstance(coverage, Mapping):
        raise ValueError("implementation Evaluation coverage is missing")
    required = coverage.get("required")
    if not isinstance(required, (list, tuple)) or not required or not all(_nonempty(item) for item in required):
        raise ValueError("required Evaluation coverage is missing")
    if "candidate" in coverage and coverage["candidate"] != packet.get("candidate"):
        raise ValueError("coverage is bound to a different candidate")
    if "phase" in coverage and coverage["phase"] != packet.get("phase"):
        raise ValueError("coverage is bound to a different phase")


def _path_is_owned(path_value: object, packet: Mapping[str, Any]) -> bool:
    if not isinstance(path_value, str) or not path_value or ".." in Path(path_value).parts:
        return False
    owned = packet.get("owned_paths", packet.get("plan_item", {}).get("owned_paths", []))
    if not isinstance(owned, (list, tuple)):
        return False
    path = Path(path_value)
    workspace_value = packet.get("workspace")
    workspace = Path(workspace_value) if isinstance(workspace_value, str) and workspace_value else None
    if path.is_absolute():
        if workspace is not None:
            try:
                path.resolve(strict=False).relative_to(workspace.resolve(strict=False))
                return True
            except ValueError:
                return any(Path(item).is_absolute() and path.resolve(strict=False).is_relative_to(
                    Path(item).resolve(strict=False)) for item in owned if isinstance(item, str))
        return any(item == "." for item in owned)
    return any(item == "." or path == Path(item) or path.is_relative_to(Path(item))
               for item in owned if isinstance(item, str) and not Path(item).is_absolute())


def _observed_change_path(value: object) -> object:
    """Extract a path from an observed change record without trusting its digest."""
    return value.get("path") if isinstance(value, Mapping) else value


def _identity_matches(observed: object, admitted: object) -> bool:
    """Compare the admitted candidate/phase identity, not arbitrary output labels."""
    if not _nonempty(observed) or not _nonempty(admitted):
        return False
    return _identity_token(observed) == _identity_token(admitted)


def _blocked(step: str, reason: str, packet: Mapping[str, Any]) -> dict[str, Any]:
    label = "retry_blocked" if step == "CA-O-096" else ("unresolved" if step == "CA-O-095" else "blocked")
    return _envelope(step, label, packet, blockers=[reason])


def _envelope(step: str, result: str, packet: Mapping[str, Any], **extra: Any) -> dict[str, Any]:
    action, context = ACTION_BY_STEP[step]
    return {
        "step": step, "action": action, "context": context, "result": result,
        "source_bindings": packet.get("source_bindings", []),
        "retained_state": packet.get("retained_state", {}),
        "evidence": packet.get("evidence", []), "blockers": [], **extra,
    }


def _validate_selected_project(packet: Mapping[str, Any], selected_project_root: str | Path) -> None:
    binding = packet.get("selected_project")
    if not isinstance(binding, Mapping) or set(binding) != _SELECTED_PROJECT_FIELDS:
        raise ValueError("selected Project binding is missing or malformed")
    if binding.get("kind") != "selected_project" or binding.get("source_root") != SELECTED_PROJECT_SOURCE_ROOT:
        raise ValueError("selected Project binding has an invalid authority root")
    source_references = binding.get("source_references")
    if not isinstance(source_references, list):
        raise ValueError("selected Project source references are missing")
    root = _trusted_project_root(selected_project_root)
    expected = current_source_bindings(root)
    if source_references != expected:
        raise ValueError("selected Project source references are stale or mismatched")
    _validate_workspace_capability(packet, root)


def _overlaps(left: Path, right: Path) -> bool:
    return left == right or left.is_relative_to(right) or right.is_relative_to(left)


def _validate_workspace_capability(packet: Mapping[str, Any], selected_project_root: Path) -> None:
    workspace = packet.get("workspace")
    if not isinstance(workspace, str) or not workspace:
        raise ValueError("selected Project workspace is missing")
    path = Path(workspace)
    if not path.is_absolute() or path.is_symlink() or not path.is_dir():
        raise ValueError("selected Project workspace must be an absolute non-symlink directory")
    try:
        resolved = path.resolve(strict=True)
    except OSError as error:
        raise ValueError("selected Project workspace is not readable") from error
    # A lexical absolute path may legitimately cross a platform-owned ancestor
    # alias (for example macOS /var -> /private/var).  The workspace leaf
    # itself was rejected above when it is a symlink; use its canonical path
    # only for the authority-overlap checks below.
    source_root = selected_project_root / SELECTED_PROJECT_SOURCE_ROOT
    protected_locations = (source_root, selected_project_root / ".git")
    if selected_project_root.is_relative_to(resolved) or any(_overlaps(resolved, protected)
                                                               for protected in protected_locations):
        raise ValueError("selected Project workspace overlaps protected Project authority")
    permissions = packet.get("permissions")
    capability = permissions.get("implementation_workspace") if isinstance(permissions, Mapping) else None
    expected = {"kind": "disposable_workspace", "path": workspace, "allow_write": True}
    if capability != expected:
        raise ValueError("selected Project workspace capability is missing or mismatched")


def validate_packet(step: str, packet: Mapping[str, Any], agent: Callable[..., Any] | None,
                    selected_project_root: str | Path | None = None,
                    trusted_execution_authorization: Mapping[str, Any] | None = None) -> str | None:
    """Admit one complete current Step packet before Agent dispatch.

    This is the single implementation-packet validator.  The selected
    executor supplies the frozen Step packet and this adapter owns the
    source/input, scope, gate, and cardinality checks before invoking an
    Agent; no caller assertion is treated as a substitute for them.
    """
    _, context = ACTION_BY_STEP[step]
    if not isinstance(packet, Mapping):
        return "implementation Step packet must be a mapping"
    if packet.get("context") != context:
        return "supplied Step context is missing or mismatched"
    try:
        if selected_project_root is None:
            if "selected_project" in packet:
                return "selected invocation needs a trusted selected Project root"
        else:
            _validate_selected_project(packet, selected_project_root)
        bindings_current = packet.get("source_bindings") == current_source_bindings(selected_project_root)
    except (KeyError, OSError, UnicodeDecodeError, ValueError, TypeError):
        bindings_current = False
    permissions = packet.get("permissions")
    if (not bindings_current or not isinstance(permissions, Mapping)
            or permissions.get("allowed") is not True):
        return "current source bindings or permission are missing"
    try:
        compile_active_methods(packet, selected_project_root)
        current = {row["atom_id"]: row for row in current_source_bindings(selected_project_root)}
        root = _trusted_project_root(selected_project_root)
        requirements = packet.get("requirements")
        legacy_requirements = packet.get("requirements_delivery")
        if requirements is not None and legacy_requirements is not None:
            raise ValueError("conflicting R input aliases are present")
        if requirements is None:
            requirements = legacy_requirements
        delivery = packet.get("delivery")
        if delivery is not None and legacy_requirements is not None:
            raise ValueError("conflicting R/D input aliases are present")
        if delivery is None and isinstance(requirements, list):
            requirements, delivery = ([row for row in requirements
                                       if isinstance(row, Mapping) and str(row.get("atom_id", "")).startswith("CA-R-")],
                                      [row for row in requirements
                                       if isinstance(row, Mapping) and str(row.get("atom_id", "")).startswith("CA-D-")])
        _validate_input_bindings(requirements, "R", current, root, required=True)
        _validate_input_bindings(delivery, "D", current, root, required=False)
        _validate_input_bindings(packet.get("evaluations"), "E", current, root,
                                 required=step in _E_REQUIRED_STEPS)
        _validate_red(packet, step)
        _validate_plan_and_scope(packet, step)
        _validate_confidence(packet)
        _validate_retry(packet, step, trusted_execution_authorization)
        _validate_coverage(packet, step)
    except ValueError as error:
        return str(error)
    if context == "Isolated":
        item = packet.get("plan_item", {})
        if agent is None or not packet.get("handoff_complete") or item.get("estimated_minutes", 15) >= 15:
            return "isolated dispatch needs an Agent, complete handoff, and P subtask below fifteen minutes"
    if step in {"CA-O-092", "CA-O-093", "CA-O-094"} and (
            not isinstance(packet.get("golden_e2e"), (list, tuple)) or not packet.get("golden_e2e")
            or not _nonempty(packet.get("baseline_command"))):
        return "golden E2E cases and runnable baseline are required before implementation"
    return None


def _performed_success(step: str, packet: Mapping[str, Any], response: Mapping[str, Any]) -> bool:
    result, outputs, evidence = response.get("result"), response.get("outputs"), response.get("evidence")
    if not isinstance(outputs, Mapping) or not isinstance(evidence, list) or not evidence:
        return False
    if result == "prepared":
        return (isinstance(outputs.get("golden_e2e"), (list, tuple)) and bool(outputs.get("golden_e2e"))
                and isinstance(outputs.get("commands"), (list, tuple)) and bool(outputs.get("commands"))
                and isinstance(outputs.get("expected_outcomes"), (list, tuple))
                and bool(outputs.get("expected_outcomes")))
    if result == "implemented":
        changed_paths = outputs.get("changed_paths")
        return (_identity_matches(outputs.get("candidate"), packet.get("candidate"))
                and _identity_matches(outputs.get("phase"), packet.get("phase"))
                and isinstance(changed_paths, (list, tuple))
                and bool(changed_paths)
                and all(_path_is_owned(_observed_change_path(path), packet) for path in changed_paths))
    if result == "passed":
        checks = outputs.get("checks")
        coverage = outputs.get("coverage")
        required = packet.get("coverage", {}).get("required", [])
        checked = coverage.get("checked") if isinstance(coverage, Mapping) else None
        return (isinstance(outputs.get("commands"), (list, tuple)) and bool(outputs.get("commands"))
                and _identity_token(outputs.get("candidate")) == _identity_token(packet.get("candidate"))
                and isinstance(checks, list) and checks
                and all(isinstance(check, Mapping) and check.get("returncode") == 0 for check in checks)
                and isinstance(coverage, Mapping) and coverage.get("complete") is True
                and isinstance(checked, (list, tuple))
                and set(required).issubset(set(checked)))
    if result == "failed":
        checks = outputs.get("checks")
        return (isinstance(outputs.get("commands"), (list, tuple)) and bool(outputs.get("commands"))
                and isinstance(checks, list) and checks
                and any(isinstance(check, Mapping) and check.get("returncode") != 0 for check in checks))
    if result == "repaired":
        changed_paths = outputs.get("changed_paths")
        return (_identity_matches(outputs.get("candidate"), packet.get("candidate"))
                and _identity_matches(outputs.get("phase"), packet.get("phase"))
                and isinstance(changed_paths, (list, tuple))
                and bool(changed_paths)
                and all(_path_is_owned(_observed_change_path(path), packet) for path in changed_paths)
                and isinstance(outputs.get("recheck_commands"), (list, tuple))
                and bool(outputs.get("recheck_commands"))
                and isinstance(outputs.get("issue_evidence"), list)
                and isinstance(outputs.get("regression_evidence"), list))
    if result in {"implementation_defect", "test_implementation_defect", "expected_initial_failure",
                  "authority_change_required", "environment_blocker", "unresolved"}:
        return _nonempty(outputs.get("cause") or outputs.get("diagnosis") or outputs.get("reason"))
    if result in {"retry_permitted", "retry_blocked"}:
        retry = packet.get("retry", {})
        return (_nonempty(outputs.get("decision"))
                and _nonempty(outputs.get("limit_provenance"))
                and outputs.get("consumed") == retry.get("consumed"))
    return True


def implement_selected_queue(step: str, packet: Mapping[str, Any], agent: Callable[..., Any] | None = None,
                             implement_run_support: Any = None, *,
                             selected_project_root: str | Path | None = None,
                             trusted_execution_authorization: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Invoke one current Action; no MCP server or successor dispatch is needed."""
    if step not in ACTION_BY_STEP:
        raise ValueError(f"unknown current implementation Step: {step}")
    blocker = validate_packet(step, packet, agent, selected_project_root,
                              trusted_execution_authorization)
    if blocker:
        return _blocked(step, blocker, packet)
    prompt = (HERE / f"{step}.prompt.md").read_text(encoding="utf-8")
    response = agent(prompt, packet) if agent is not None else {}
    if not isinstance(response, Mapping) or response.get("result") not in RESULTS[step]:
        return _blocked(step, "Agent returned no admitted result", packet)
    if not _performed_success(step, packet, response):
        return _blocked(step, "Agent result lacks required performed-work outputs or evidence", packet)
    result = _envelope(step, str(response["result"]), packet,
                       outputs=response.get("outputs", {}),
                       evidence=[*packet.get("evidence", []), *response.get("evidence", [])],
                       blockers=list(response.get("blockers", [])))
    if implement_run_support is not None:
        result["run_support"] = "supplied"
    return result


def _handler(step: str) -> Callable[..., dict[str, Any]]:
    return lambda packet, agent=None, implement_run_support=None, selected_project_root=None, \
        trusted_execution_authorization=None: implement_selected_queue(
            step, packet, agent, implement_run_support, selected_project_root=selected_project_root,
            trusted_execution_authorization=trusted_execution_authorization)


for _step, _action in ACTION_BY_STEP.items():
    ACTION_HANDLERS[_action[0]] = _handler(_step)
