"""Source-bound handlers for the seven current CA-O-016 Actions.

The graph executor owns transitions.  These handlers validate one supplied
packet, call a replaceable Agent adapter, and return a truthful envelope.
"""
from __future__ import annotations

import hashlib
import json
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
    if not isinstance(packet.get("requirements_delivery"), (list, tuple)):
        raise ValueError("missing selected R/D targets")
    if not isinstance(packet.get("evaluations"), (list, tuple)):
        raise ValueError("missing separate E checks")
    try:
        if selected_project_root is None:
            expected_paths = [row["path"] for row in projection["sources"]]
        else:
            expected_paths = [row["path"] for row in current_source_bindings(selected_project_root)
                              if row["atom_id"].startswith("CA-M-")]
        expected = prepare_method_projection(expected_paths, selected_project_root)
    except (KeyError, OSError, UnicodeDecodeError, ValueError) as error:
        raise ValueError(f"invalid active-M projection: {error}") from error
    if projection != expected:
        raise ValueError("active-M projection content, source, digest, or currentness mismatch")
    return expected


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
    expected = current_source_bindings(selected_project_root)
    if source_references != expected:
        raise ValueError("selected Project source references are stale or mismatched")
    _validate_workspace_capability(packet)


def _validate_workspace_capability(packet: Mapping[str, Any]) -> None:
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
    if resolved != path:
        raise ValueError("selected Project workspace must be an absolute non-symlink directory")
    permissions = packet.get("permissions")
    capability = permissions.get("implementation_workspace") if isinstance(permissions, Mapping) else None
    expected = {"kind": "disposable_workspace", "path": workspace, "allow_write": True}
    if capability != expected:
        raise ValueError("selected Project workspace capability is missing or mismatched")


def _validate(step: str, packet: Mapping[str, Any], agent: Callable[..., Any] | None,
              selected_project_root: str | Path | None = None) -> str | None:
    _, context = ACTION_BY_STEP[step]
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
    if not bindings_current or not isinstance(permissions, Mapping) or not permissions.get("allowed"):
        return "current source bindings or permission are missing"
    try:
        compile_active_methods(packet, selected_project_root)
    except ValueError as error:
        return str(error)
    if context == "Isolated":
        item = packet.get("plan_item", {})
        if agent is None or not packet.get("handoff_complete") or item.get("estimated_minutes", 15) >= 15:
            return "isolated dispatch needs an Agent, complete handoff, and P subtask below fifteen minutes"
    if step == "CA-O-092" and (not packet.get("golden_e2e") or not packet.get("baseline_command")):
        return "golden E2E cases and runnable baseline are required before implementation"
    if step == "CA-O-096":
        retry = packet.get("retry", {})
        if retry.get("consumed", 0) >= retry.get("limit", 0):
            return "retry allowance is exhausted"
    return None


def _performed_success(step: str, response: Mapping[str, Any]) -> bool:
    result, outputs, evidence = response.get("result"), response.get("outputs"), response.get("evidence")
    if not isinstance(outputs, Mapping) or not isinstance(evidence, list) or not evidence:
        return False
    if result == "prepared":
        return bool(outputs.get("golden_e2e") and outputs.get("commands") and outputs.get("expected_outcomes"))
    if result == "implemented":
        return bool(outputs.get("candidate") and outputs.get("changed_paths"))
    if result == "passed":
        checks = outputs.get("checks")
        return bool(outputs.get("commands") and isinstance(checks, list) and checks and
                    all(isinstance(check, Mapping) and check.get("returncode") == 0 for check in checks))
    if result == "repaired":
        return bool(outputs.get("candidate") and outputs.get("changed_paths") and outputs.get("recheck_commands"))
    return True


def implement_selected_queue(step: str, packet: Mapping[str, Any], agent: Callable[..., Any] | None = None,
                             implement_run_support: Any = None, *,
                             selected_project_root: str | Path | None = None) -> dict[str, Any]:
    """Invoke one current Action; no MCP server or successor dispatch is needed."""
    if step not in ACTION_BY_STEP:
        raise ValueError(f"unknown current implementation Step: {step}")
    blocker = _validate(step, packet, agent, selected_project_root)
    if blocker:
        return _blocked(step, blocker, packet)
    prompt = (HERE / f"{step}.prompt.md").read_text(encoding="utf-8")
    response = agent(prompt, packet) if agent is not None else {}
    if not isinstance(response, Mapping) or response.get("result") not in RESULTS[step]:
        return _blocked(step, "Agent returned no admitted result", packet)
    if not _performed_success(step, response):
        return _blocked(step, "Agent result lacks required performed-work outputs or evidence", packet)
    result = _envelope(step, str(response["result"]), packet,
                       outputs=response.get("outputs", {}),
                       evidence=[*packet.get("evidence", []), *response.get("evidence", [])],
                       blockers=list(response.get("blockers", [])))
    if implement_run_support is not None:
        result["run_support"] = "supplied"
    return result


def _handler(step: str) -> Callable[..., dict[str, Any]]:
    return lambda packet, agent=None, implement_run_support=None, selected_project_root=None: implement_selected_queue(
        step, packet, agent, implement_run_support, selected_project_root=selected_project_root)


for _step, _action in ACTION_BY_STEP.items():
    ACTION_HANDLERS[_action[0]] = _handler(_step)
