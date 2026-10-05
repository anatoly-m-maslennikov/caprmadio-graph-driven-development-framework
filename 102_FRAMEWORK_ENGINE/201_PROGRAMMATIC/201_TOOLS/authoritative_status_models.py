"""Read-only resolution of current, source-declared Atom status domains."""
from __future__ import annotations

from collections.abc import Mapping
import hashlib
from pathlib import Path
import re
import tomllib
from typing import Any

from FIND_AND_FETCH_ARTIFACTS.find_and_fetch_artifacts import _load_frontmatter

_DEFAULT_CONTROL_ROOT = Path(".caprmedio_caprmedio")
_SOURCE_TAIL = Path(
    "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"
)
_VALUES = re.compile(r"(?:(?:the\s+)?Core\s+allowed values of|Core)\s+(?:`?Atom/Content Role:\s*)?([^/`\n]+?)(?:/Status|\s+Status)(?:\s+values)?`?\s*\*\*must\*\* be exactly\s*\(([^)]*)\)", re.I)
_ROLE = re.compile(r"Atom/Content Role:\s*([^/`\n]+)")
_TYPE = re.compile(
    r"Atom/Content Role:\s*[^/`\n]+/Type:\s*`?([A-Za-z][A-Za-z0-9 _-]*)`?"
)


class StatusModelError(ValueError):
    """A status model cannot be derived from current authoritative sources."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


def _configured_control_root(root: Path) -> Path:
    """Resolve the one Project-declared control root without following links."""
    settings_paths = sorted(
        path for path in root.glob(".caprmedio_*/caprmedio_project_settings.toml")
        if path.is_file() and not path.is_symlink() and not path.parent.is_symlink()
    )
    if not settings_paths:
        return root / _DEFAULT_CONTROL_ROOT
    if len(settings_paths) != 1:
        raise StatusModelError("source-invalid", "Project settings carrier is ambiguous")
    settings_path = settings_paths[0]
    try:
        settings = tomllib.loads(settings_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise StatusModelError("source-invalid", "Project settings carrier is invalid") from error
    paths = settings.get("paths")
    default = settings_path.parent.relative_to(root)
    configured = paths.get("control_root", default.as_posix()) if isinstance(paths, dict) else None
    if not isinstance(configured, str) or not configured:
        raise StatusModelError("source-invalid", "paths.control_root is invalid")
    candidate = Path(configured)
    control = root / candidate
    if (candidate.is_absolute() or candidate == Path(".") or ".." in candidate.parts
            or control.is_symlink() or not control.is_dir()):
        raise StatusModelError("source-invalid", "paths.control_root is unsafe or unavailable")
    try:
        control.resolve().relative_to(root)
    except ValueError as error:
        raise StatusModelError("source-invalid", "paths.control_root escapes the Project") from error
    return control


def _methodology_source_root(root: Path) -> Path:
    """Use the METHODOLOGY_SOURCES Scope Unit when the Structure declares it."""
    control = _configured_control_root(root)
    structure_path = control / "project_structure.toml"
    if not structure_path.exists():
        return control / _SOURCE_TAIL
    if structure_path.is_symlink() or not structure_path.is_file():
        raise StatusModelError("source-invalid", "Project Structure authority is unavailable")
    try:
        structure = tomllib.loads(structure_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise StatusModelError("source-invalid", "Project Structure authority is invalid") from error
    scope_units = structure.get("scope_units")
    matches = [
        row for row in scope_units if isinstance(row, Mapping)
        and row.get("scope_unit_name") == "METHODOLOGY_SOURCES"
    ] if isinstance(scope_units, list) else []
    if not matches:
        return control / _SOURCE_TAIL
    if len(matches) != 1 or not isinstance(matches[0].get("authority_path"), str):
        raise StatusModelError("source-invalid", "METHODOLOGY_SOURCES authority is ambiguous or invalid")
    candidate = Path(matches[0]["authority_path"])
    source = root / candidate
    if (candidate.is_absolute() or candidate == Path(".") or ".." in candidate.parts
            or source.is_symlink() or not source.is_dir()):
        raise StatusModelError("source-invalid", "METHODOLOGY_SOURCES authority is unsafe or unavailable")
    try:
        source.resolve().relative_to(root)
    except ValueError as error:
        raise StatusModelError("source-invalid", "METHODOLOGY_SOURCES authority escapes the Project") from error
    return source


def _source_snapshot(path: Path, root: Path) -> dict[str, Any] | None:
    """Read one potential status authority once; ignore unrelated Markdown."""
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise StatusModelError("source-invalid", f"unreadable methodology source: {path}") from error
    if not text.startswith("---\n"):
        return None
    closing = text.find("\n---\n", 4)
    if closing < 0:
        return None
    frontmatter, body = text[4:closing], text[closing + 5:]
    declarations = list(_VALUES.finditer(body))
    if not declarations:
        return None
    if len(declarations) != 1:
        raise StatusModelError("source-invalid", f"ambiguous status-domain declarations: {path}")
    match = declarations[0]
    try:
        meta = _load_frontmatter(frontmatter)
    except Exception as error:
        duplicate_atom_id = len(re.findall(r"(?m)^atom_id\s*:", frontmatter)) > 1
        detail = "duplicate atom_id" if duplicate_atom_id else "malformed YAML"
        raise StatusModelError("source-invalid", f"invalid status-model authority ({detail}): {path}") from error
    atom_id, definition_role = meta.get("atom_id"), meta.get("content_role")
    status, version = meta.get("status"), meta.get("version")
    subjects = meta.get("subjects")
    if (not isinstance(atom_id, str) or not atom_id
            or not isinstance(definition_role, str) or not definition_role
            or status != "Active"
            or isinstance(version, bool)
            or not isinstance(version, int) or version <= 0
            or not isinstance(subjects, Mapping)
            or not isinstance(subjects.get("governs"), str)):
        raise StatusModelError("source-invalid", f"invalid status-model authority: {path}")
    declared_role = match.group(1).strip()
    governed = subjects["governs"].strip()
    role_match = _ROLE.search(governed)
    if role_match is None or role_match.group(1).strip() != declared_role:
        raise StatusModelError("source-invalid", f"status-model authority does not govern its declared role: {path}")
    values = [item.strip().strip("`\"'") for item in match.group(2).split(",")]
    if not values or any(not item for item in values) or len(values) != len(set(values)):
        raise StatusModelError("source-invalid", f"invalid status domain in {path}")
    type_match = _TYPE.search(governed)
    return {
        "role": declared_role,
        "statuses": values,
        "type": type_match.group(1).strip() if type_match else None,
        "source": {
            "atom_id": atom_id,
            "revision": int(version),
            "path": path.relative_to(root).as_posix(),
            "sha256": hashlib.sha256(raw).hexdigest(),
        },
    }


def _atom_value(atom: object, name: str) -> str | None:
    if isinstance(atom, Mapping):
        value = atom.get(name)
        if isinstance(value, str):
            return value
        front = atom.get("frontmatter")
    else:
        value = getattr(atom, name, None)
        if isinstance(value, str):
            return value
        front = getattr(atom, "frontmatter", None)
    if not isinstance(front, str):
        return None
    matches = re.findall(rf"(?m)^{name}:\s*(.*?)\s*$", front)
    if len(matches) != 1:
        return None
    return matches[0].strip().strip("\"'")


def _models(root: Path, role: str, atom_type: str | None) -> list[dict[str, Any]]:
    base = _methodology_source_root(root)
    if not base.is_dir():
        raise StatusModelError("source-missing", "current methodology source root is unavailable")
    found: list[dict[str, Any]] = []
    for path in base.rglob("*.md"):
        if "archive" in path.parts:
            continue
        snapshot = _source_snapshot(path, root)
        if snapshot is None or snapshot["role"] != role:
            continue
        declared_type = snapshot["type"]
        if declared_type is not None and declared_type != atom_type:
            continue
        found.append({"statuses": snapshot["statuses"], "type": declared_type, "source": snapshot["source"]})
    return found


def resolve_status_model(root: str | Path, atom: object, requested_status: str,
                         supplied_model: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Resolve one current Role/Type domain; supplied input may only match it."""
    project = Path(root).resolve()
    role, atom_type = _atom_value(atom, "content_role"), _atom_value(atom, "type")
    if not role:
        raise StatusModelError("target-invalid", "target lacks carried content_role")
    if not isinstance(requested_status, str) or not requested_status:
        raise StatusModelError("status-invalid", "requested_status must be a non-empty string")
    candidates = _models(project, role, atom_type)
    specific = [row for row in candidates if row["type"] is not None]
    selected = specific if specific else [row for row in candidates if row["type"] is None]
    if not selected:
        raise StatusModelError("model-missing", f"no current status model for {role!r}")
    if len(selected) != 1:
        raise StatusModelError("model-ambiguous", f"ambiguous current status model for {role!r}")
    model = {"content_role": role, "type": atom_type, "statuses": selected[0]["statuses"],
             "model_sources": [selected[0]["source"]], "requested_status": requested_status}
    if requested_status not in model["statuses"]:
        raise StatusModelError("status-unadmitted", "requested status is not admitted by the current model")
    if supplied_model is not None:
        allowed = {"content_role", "type", "statuses", "model_sources", "requested_status"}
        if set(supplied_model) != allowed or dict(supplied_model) != model:
            raise StatusModelError("model-forged", "supplied status model differs from authoritative current sources")
    return model
