"""Domain Actions for authoritative ``project_structure.toml`` changes.

This module intentionally has no Workflow Run, service-disposition, receipt, or
Journal implementation.  ``WORKFLOW_OPERATIONS/RUN_SUPPORT`` admits an outer
CA-D-527 request and invokes one of these bounded domain Actions after its own
preview/authorization checks.  Each Action here accepts only the route-owned
``parameters`` payload and returns a ``structural_result``.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
import tomllib
from typing import Any, Callable, Iterable, Mapping


CONTROL_ROOT = ".caprmedio_caprmedio"
STRUCTURE_RELATIVE_PATH = f"{CONTROL_ROOT}/project_structure.toml"
SETTINGS_CANDIDATES = (
    f"{CONTROL_ROOT}/caprmedio_framework_settings.toml",
    f"{CONTROL_ROOT}/caprmedio_project_settings.toml",
)
OPERATIONS = {"Create", "Rename", "Move", "Remove"}
STATES = {
    "completed",
    "no_op",
    "stale",
    "conflict",
    "permission_denied",
    "partial",
    "rolled_back",
}
DECLARATION_FIELDS = (
    "scope_unit_name",
    "parent",
    "scope_unit_type",
    "scope_unit_label",
    "structural_level",
    "local_order",
    "navigational_order_number",
    "authority_path",
    "delivery_path",
    "authority_mode",
)
REQUIRED_DECLARATION_FIELDS = set(DECLARATION_FIELDS) - {"local_order", "authority_mode"}
NAME = re.compile(r"^[A-Z0-9]+(?:_[A-Z0-9]+)*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


class StructuralConflict(ValueError):
    """A domain proposal is not a valid authoritative structural change."""


@dataclass(frozen=True)
class SourceChange:
    """One exact writable source member in an authorized recovery boundary."""

    path: Path
    relative_path: str
    before: str
    after: str

    @property
    def before_sha256(self) -> str:
        return _digest_text(self.before)

    @property
    def after_sha256(self) -> str:
        return _digest_text(self.after)


def _digest_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _relative_path(root: Path, raw: object, field: str, *, allow_control_root: bool = True) -> Path:
    if not isinstance(raw, str) or not raw or "\\" in raw or "\x00" in raw:
        raise StructuralConflict(f"{field} must be a nonempty forward-slash repository-relative path")
    pure = PurePosixPath(raw)
    if pure.is_absolute() or raw in {".", ".."} or ".." in pure.parts:
        raise StructuralConflict(f"{field} is not a safe repository-relative path")
    if not allow_control_root and CONTROL_ROOT in pure.parts:
        raise StructuralConflict(f"{field} cannot target a project control root")
    candidate = root.joinpath(*pure.parts)
    try:
        candidate.resolve(strict=False).relative_to(root.resolve())
    except ValueError as error:
        raise StructuralConflict(f"{field} escapes the project root") from error
    return candidate


def _require_mapping(value: object, field: str) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        raise StructuralConflict(f"{field} must be an object")
    return dict(value)


def _require_string(value: Mapping[str, Any], field: str) -> str:
    item = value.get(field)
    if not isinstance(item, str) or not item:
        raise StructuralConflict(f"{field} must be a nonempty string")
    return item


def _require_int(value: Mapping[str, Any], field: str, *, minimum: int = 0) -> int:
    item = value.get(field)
    if isinstance(item, bool) or not isinstance(item, int) or item < minimum:
        raise StructuralConflict(f"{field} must be an integer greater than or equal to {minimum}")
    return item


def _canonical_name(value: object, field: str) -> str:
    if not isinstance(value, str) or not NAME.fullmatch(value) or value == "PROJECT":
        raise StructuralConflict(f"{field} must be a non-Project canonical uppercase Scope Unit name")
    return value


def _normalise_declaration(value: object, root: Path) -> dict[str, Any]:
    row = _require_mapping(value, "declaration")
    unknown = set(row) - set(DECLARATION_FIELDS)
    missing = REQUIRED_DECLARATION_FIELDS - set(row)
    if unknown or missing:
        detail = []
        if missing:
            detail.append("missing " + ", ".join(sorted(missing)))
        if unknown:
            detail.append("unknown " + ", ".join(sorted(unknown)))
        raise StructuralConflict("invalid declaration fields: " + "; ".join(detail))
    name = _canonical_name(row.get("scope_unit_name"), "scope_unit_name")
    parent = row.get("parent")
    if not isinstance(parent, str) or not parent:
        raise StructuralConflict("parent must be a nonempty string")
    if parent != "PROJECT":
        _canonical_name(parent, "parent")
    scope_type = row.get("scope_unit_type")
    if scope_type not in {"Ordered", "Unordered"}:
        raise StructuralConflict("scope_unit_type must be Ordered or Unordered")
    label = row.get("scope_unit_label")
    if not isinstance(label, str) or not NAME.fullmatch(label):
        raise StructuralConflict("scope_unit_label must be a nonempty canonical uppercase Label")
    structural_level = _require_int(row, "structural_level", minimum=1)
    navigation = _require_int(row, "navigational_order_number", minimum=0)
    normalised: dict[str, Any] = {
        "scope_unit_name": name,
        "parent": parent,
        "scope_unit_type": scope_type,
        "scope_unit_label": label,
        "structural_level": structural_level,
        "navigational_order_number": navigation,
    }
    if scope_type == "Ordered":
        normalised["local_order"] = _require_int(row, "local_order", minimum=0)
    elif "local_order" in row:
        raise StructuralConflict("local_order is forbidden for an Unordered Scope Unit")
    for field in ("authority_path", "delivery_path"):
        raw = _require_string(row, field)
        _relative_path(root, raw, field)
        normalised[field] = raw.rstrip("/")
    if "authority_mode" in row:
        mode = row["authority_mode"]
        if mode not in {"strict", "casual"}:
            raise StructuralConflict("authority_mode must be strict or casual when specified")
        normalised["authority_mode"] = mode
    return normalised


def _default_authority_mode(root: Path) -> str:
    for relative in SETTINGS_CANDIDATES:
        settings = root / relative
        if not settings.is_file() or settings.is_symlink():
            continue
        try:
            parsed = tomllib.loads(settings.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
            raise StructuralConflict(f"cannot read Framework Instance Settings: {relative}") from error
        modes = parsed.get("authority_modes")
        if isinstance(modes, Mapping) and modes.get("default") in {"strict", "casual"}:
            return str(modes["default"])
    raise StructuralConflict("Framework Instance Settings lacks authority_modes.default")


def _validate_tree(rows: Iterable[Mapping[str, Any]], root: Path) -> dict[str, str]:
    names: set[str] = set()
    materialized: list[dict[str, Any]] = []
    for row in rows:
        candidate = _normalise_declaration(row, root)
        if candidate["scope_unit_name"] in names:
            raise StructuralConflict(f"duplicate Scope Unit name: {candidate['scope_unit_name']}")
        names.add(candidate["scope_unit_name"])
        materialized.append(candidate)
    by_name = {str(row["scope_unit_name"]): row for row in materialized}
    for row in materialized:
        parent = str(row["parent"])
        if parent != "PROJECT" and parent not in by_name:
            raise StructuralConflict(f"undeclared parent: {parent}")
        if parent == row["scope_unit_name"]:
            raise StructuralConflict(f"Scope Unit cannot parent itself: {parent}")
    depths: dict[str, int] = {}

    def depth(name: str, visiting: set[str]) -> int:
        if name in depths:
            return depths[name]
        if name in visiting:
            raise StructuralConflict("Scope Unit parentage contains a cycle")
        row = by_name[name]
        parent = str(row["parent"])
        result = 1 if parent == "PROJECT" else depth(parent, visiting | {name}) + 1
        if row["structural_level"] != result:
            raise StructuralConflict(
                f"structural_level for {name} is {row['structural_level']}, expected {result} from parentage"
            )
        depths[name] = result
        return result

    sibling_orders: set[tuple[str, int]] = set()
    for name, row in by_name.items():
        depth(name, set())
        if row["scope_unit_type"] == "Ordered":
            key = (str(row["parent"]), int(row["local_order"]))
            if key in sibling_orders:
                raise StructuralConflict(f"duplicate Ordered local_order under parent {key[0]}")
            sibling_orders.add(key)
    default_mode = _default_authority_mode(root)
    return {name: str(row.get("authority_mode", default_mode)) for name, row in by_name.items()}


def _parse_structure(path: Path, root: Path) -> tuple[str, list[dict[str, Any]]]:
    if not path.is_file() or path.is_symlink():
        raise StructuralConflict(f"authoritative Project Structure is unavailable: {STRUCTURE_RELATIVE_PATH}")
    try:
        source = path.read_text(encoding="utf-8")
        parsed = tomllib.loads(source)
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise StructuralConflict("authoritative Project Structure is not valid TOML") from error
    rows = parsed.get("scope_units", [])
    if not isinstance(rows, list):
        raise StructuralConflict("authoritative Project Structure scope_units must be an array")
    result = [_normalise_declaration(row, root) for row in rows]
    _validate_tree(result, root)
    return source, result


def _quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _render_declaration(row: Mapping[str, Any]) -> str:
    lines = ["[[scope_units]]"]
    for field in DECLARATION_FIELDS:
        if field not in row:
            continue
        value = row[field]
        encoded = _quote(value) if isinstance(value, str) else str(value)
        lines.append(f"{field} = {encoded}")
    return "\n".join(lines) + "\n"


def serialize_project_structure(rows: Iterable[Mapping[str, Any]]) -> str:
    """Return a canonical TOML fixture for independent golden tests."""
    return "schema_version = 1\n\n" + "\n".join(_render_declaration(row).rstrip() for row in rows) + "\n"


def _render_resulting_source(source: str, before: list[dict[str, Any]], after: list[dict[str, Any]]) -> str:
    """Retain byte-identical unaffected rows; replace only changed declarations."""
    markers = list(re.finditer(r"(?m)^\[\[scope_units\]\][ \t]*\n?", source))
    if not markers:
        if not after:
            return source
        return source.rstrip() + "\n\n" + "\n".join(_render_declaration(row).rstrip() for row in after) + "\n"
    prefix = source[: markers[0].start()]
    blocks: dict[str, str] = {}
    for index, marker in enumerate(markers):
        end = markers[index + 1].start() if index + 1 < len(markers) else len(source)
        block = source[marker.start() : end]
        try:
            parsed = tomllib.loads(block)
            rows = parsed.get("scope_units")
            if isinstance(rows, list) and len(rows) == 1 and isinstance(rows[0], Mapping):
                name = rows[0].get("scope_unit_name")
                if isinstance(name, str):
                    blocks[name] = block
        except tomllib.TOMLDecodeError:
            continue
    before_by_name = {str(row["scope_unit_name"]): row for row in before}
    rendered: list[str] = [prefix.rstrip()]
    for row in after:
        name = str(row["scope_unit_name"])
        original = blocks.get(name)
        if original is not None and before_by_name.get(name) == row:
            rendered.append(original.rstrip())
        else:
            rendered.append(_render_declaration(row).rstrip())
    return "\n\n".join(part for part in rendered if part) + "\n"


def _normalise_parameters(value: object, root: Path) -> dict[str, Any]:
    parameters = _require_mapping(value, "parameters")
    operation = parameters.get("operation")
    if operation not in OPERATIONS:
        raise StructuralConflict("operation must be exactly Create, Rename, Move, or Remove")
    allowed = {
        "operation",
        "expected_toml_revision",
        "target_name",
        "declaration",
        "reference_frontier",
        "goal_coverage_disposition",
        "preservation_disposition",
        "recovery_disposition",
        "authorization_revision",
    }
    unknown = set(parameters) - allowed
    if unknown:
        raise StructuralConflict("parameters contains unknown route fields: " + ", ".join(sorted(unknown)))
    revision = _require_string(parameters, "expected_toml_revision")
    if not SHA256.fullmatch(revision):
        raise StructuralConflict("expected_toml_revision must be a SHA-256 digest")
    references = parameters.get("reference_frontier")
    if not isinstance(references, list):
        raise StructuralConflict("reference_frontier must be an ordered array")
    parameters["reference_frontier"] = _normalise_reference_frontier(references, root)
    parameters["goal_coverage_disposition"] = _normalise_goal_disposition(
        parameters.get("goal_coverage_disposition"), operation
    )
    parameters["preservation_disposition"] = _normalise_preservation(parameters.get("preservation_disposition"), root)
    parameters["recovery_disposition"] = _normalise_recovery(parameters.get("recovery_disposition"))
    if operation == "Remove":
        parameters["target_name"] = _canonical_name(parameters.get("target_name"), "target_name")
        if "declaration" in parameters:
            raise StructuralConflict("Remove must not contain a replacement declaration")
    else:
        parameters["declaration"] = _normalise_declaration(parameters.get("declaration"), root)
        if operation in {"Rename", "Move"}:
            parameters["target_name"] = _canonical_name(parameters.get("target_name"), "target_name")
    if "authorization_revision" in parameters:
        _require_string(parameters, "authorization_revision")
    return parameters


def _normalise_reference_frontier(items: list[object], root: Path) -> list[dict[str, Any]]:
    seen: set[str] = set()
    result: list[dict[str, Any]] = []
    for raw in items:
        item = _require_mapping(raw, "reference_frontier entry")
        if set(item) != {"path", "expected_sha256", "replacements"}:
            raise StructuralConflict("each reference frontier entry must contain only path, expected_sha256, replacements")
        path = _relative_path(root, item["path"], "reference_frontier.path")
        relative = path.relative_to(root).as_posix()
        if relative == STRUCTURE_RELATIVE_PATH or relative in seen:
            raise StructuralConflict("reference frontier path is duplicate or targets Project Structure")
        seen.add(relative)
        expected = item["expected_sha256"]
        if not isinstance(expected, str) or not SHA256.fullmatch(expected):
            raise StructuralConflict("reference_frontier.expected_sha256 must be a SHA-256 digest")
        replacements = item["replacements"]
        if not isinstance(replacements, list):
            raise StructuralConflict("reference_frontier.replacements must be an ordered array")
        normalised_replacements: list[dict[str, str]] = []
        for replacement in replacements:
            pair = _require_mapping(replacement, "reference replacement")
            if set(pair) != {"old", "new"} or not isinstance(pair["old"], str) or not pair["old"] or not isinstance(pair["new"], str):
                raise StructuralConflict("reference replacement must contain nonempty old and string new values")
            normalised_replacements.append({"old": pair["old"], "new": pair["new"]})
        result.append({"path": path, "relative_path": relative, "expected_sha256": expected, "replacements": normalised_replacements})
    return result


def _normalise_goal_disposition(value: object, operation: str) -> dict[str, Any]:
    item = _require_mapping(value, "goal_coverage_disposition")
    state = item.get("state")
    if state not in {"present", "missing", "blocking"}:
        raise StructuralConflict("goal_coverage_disposition.state must be present, missing, or blocking")
    parent = item.get("parent")
    if not isinstance(parent, str) or not parent:
        raise StructuralConflict("goal_coverage_disposition.parent must be a nonempty string")
    if parent != "PROJECT":
        _canonical_name(parent, "goal_coverage_disposition.parent")
    if operation in {"Create", "Move"} and state == "missing":
        for key in ("gap_ref", "authorized_disposition"):
            if not isinstance(item.get(key), str) or not item[key]:
                raise StructuralConflict(f"missing Goal coverage requires {key}")
    if state == "blocking" and (not isinstance(item.get("reason"), str) or not item["reason"]):
        raise StructuralConflict("blocking Goal coverage requires reason")
    return dict(item)


def _normalise_preservation(value: object, root: Path) -> dict[str, Any]:
    item = _require_mapping(value, "preservation_disposition")
    if set(item) - {"preserved", "breakages", "history"} or not isinstance(item.get("preserved"), list):
        raise StructuralConflict("preservation_disposition must contain preserved and optional breakages/history")
    for field in ("preserved", "breakages", "history"):
        if field not in item:
            continue
        if not isinstance(item[field], list):
            raise StructuralConflict(f"preservation_disposition.{field} must be an array")
        for entry in item[field]:
            if not isinstance(entry, str) or not entry:
                raise StructuralConflict(f"preservation_disposition.{field} entries must be nonempty strings")
            _relative_path(root, entry, f"preservation_disposition.{field}")
    return dict(item)


def _normalise_recovery(value: object) -> dict[str, Any]:
    item = _require_mapping(value, "recovery_disposition")
    if set(item) != {"authorized", "boundary"} or item.get("authorized") is not True or not isinstance(item.get("boundary"), str) or not item["boundary"]:
        raise StructuralConflict("recovery_disposition must contain authorized=true and a named boundary")
    return dict(item)


def _reference_changes(root: Path, references: list[dict[str, Any]]) -> list[SourceChange]:
    changes: list[SourceChange] = []
    for entry in references:
        path = entry["path"]
        if not path.is_file() or path.is_symlink():
            raise StructuralConflict(f"reference frontier path is not a regular file: {entry['relative_path']}")
        try:
            before = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            raise StructuralConflict(f"reference frontier path cannot be read: {entry['relative_path']}") from error
        if _digest_text(before) != entry["expected_sha256"]:
            raise StructuralConflict(f"stale reference frontier: {entry['relative_path']}")
        after = before
        for replacement in entry["replacements"]:
            occurrences = after.count(replacement["old"])
            if occurrences != 1:
                raise StructuralConflict(
                    f"reference replacement must match exactly once in {entry['relative_path']}: {replacement['old']!r}"
                )
            after = after.replace(replacement["old"], replacement["new"], 1)
        if after != before:
            changes.append(SourceChange(path, entry["relative_path"], before, after))
    return changes


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".project-structure-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def _result(
    *,
    state: str,
    operation: str,
    pre_revision: str | None,
    post_revision: str | None,
    target_name: str | None = None,
    resulting: Mapping[str, Any] | None = None,
    parameters: Mapping[str, Any] | None = None,
    errors: list[str] | None = None,
    actual_effects: list[dict[str, str]] | None = None,
    repaired_references: list[str] | None = None,
    recovery_boundary: Mapping[str, Any] | None = None,
    unapplied_effects: list[dict[str, str]] | None = None,
) -> dict[str, Any]:
    if state not in STATES:
        raise AssertionError(f"unsupported structural state: {state}")
    preservation = parameters.get("preservation_disposition", {}) if parameters else {}
    payload: dict[str, Any] = {
        "state": state,
        "operation": operation,
        "requested_scope_unit": target_name,
        "pre_toml_revision": pre_revision,
        "post_toml_revision": post_revision,
        "resulting_scope_unit": dict(resulting) if resulting else None,
        "affected": {
            "scope_units": [target_name] if target_name else [],
            "references": repaired_references or [],
            "carriers": list(preservation.get("preserved", [])),
        },
        "repaired_references": repaired_references or [],
        "preserved_carriers": list(preservation.get("preserved", [])),
        "preserved_history": list(preservation.get("history", [])),
        "breakages": list(preservation.get("breakages", [])),
        "goal_coverage_disposition": dict(parameters.get("goal_coverage_disposition", {})) if parameters else {},
        "authorization_revision": parameters.get("authorization_revision") if parameters else None,
        "actual_effects": actual_effects or [],
        "unapplied_effects": unapplied_effects or [],
        "validation_errors": errors or [],
        "recovery_disposition": dict(parameters.get("recovery_disposition", {})) if parameters else {},
        "evidence_references": [],
    }
    if recovery_boundary is not None:
        payload["recovery_boundary"] = dict(recovery_boundary)
    return payload


def apply_scope_unit_action(
    project_root: Path | str,
    parameters: Mapping[str, Any],
    *,
    after_declaration: Callable[[], None] | None = None,
) -> dict[str, Any]:
    """Apply one already-admitted structural Action without owning a Workflow Run.

    ``after_declaration`` exists only for a caller's isolated failure injection;
    it is not a route parameter and cannot enlarge a production request.
    """
    root = Path(project_root).resolve()
    structure_path = root / STRUCTURE_RELATIVE_PATH
    operation = parameters.get("operation") if isinstance(parameters, Mapping) else "unknown"
    pre_revision: str | None = None
    normalised: dict[str, Any] | None = None
    try:
        normalised = _normalise_parameters(parameters, root)
        operation = normalised["operation"]
        source, before = _parse_structure(structure_path, root)
        pre_revision = _digest_text(source)
        if normalised["expected_toml_revision"] != pre_revision:
            return _result(
                state="stale", operation=operation, pre_revision=pre_revision, post_revision=pre_revision,
                parameters=normalised, errors=["authoritative Project Structure revision changed"],
            )
        after = [dict(row) for row in before]
        target_name: str | None = normalised.get("target_name")
        target_row: dict[str, Any] | None = None
        if operation == "Create":
            target_row = dict(normalised["declaration"])
            target_name = target_row["scope_unit_name"]
            matches = [row for row in before if row["scope_unit_name"] == target_name]
            if matches:
                if matches[0] != target_row:
                    raise StructuralConflict("Create target already exists with a different declaration")
                target_row = dict(matches[0])
            else:
                after.append(target_row)
        elif operation in {"Rename", "Move"}:
            target_name = normalised["target_name"]
            matches = [index for index, row in enumerate(before) if row["scope_unit_name"] == target_name]
            target_row = dict(normalised["declaration"])
            if not matches:
                existing = next((row for row in before if row["scope_unit_name"] == target_row["scope_unit_name"]), None)
                if existing != target_row:
                    raise StructuralConflict("Rename or Move predecessor is absent and target declaration is not already current")
                target_name = target_row["scope_unit_name"]
            else:
                if operation == "Rename" and target_row["scope_unit_name"] == target_name:
                    raise StructuralConflict("Rename requires a different resulting scope_unit_name")
                if operation == "Move" and target_row["scope_unit_name"] != target_name:
                    raise StructuralConflict("Move must retain the Scope Unit identity")
                after[matches[0]] = target_row
            target_name = target_row["scope_unit_name"]
        else:  # Remove
            target_name = normalised["target_name"]
            matches = [row for row in before if row["scope_unit_name"] == target_name]
            if matches:
                descendants = [row["scope_unit_name"] for row in before if row["parent"] == target_name]
                if descendants:
                    raise StructuralConflict("Remove cannot recursively delete descendants: " + ", ".join(descendants))
                after = [row for row in after if row["scope_unit_name"] != target_name]
        if operation in {"Create", "Move"}:
            goal = normalised["goal_coverage_disposition"]
            expected_parent = str(target_row["parent"])
            if goal["parent"] != expected_parent:
                raise StructuralConflict("Goal coverage disposition must identify the direct resulting parent")
            if goal["state"] == "blocking":
                return _result(
                    state="conflict", operation=operation, pre_revision=pre_revision, post_revision=pre_revision,
                    target_name=target_name, parameters=normalised,
                    errors=["direct-parent Goal coverage remains blocking"],
                )
        effective_modes = _validate_tree(after, root)
        if target_row is not None:
            target_row = dict(target_row)
            target_row["effective_authority_mode"] = effective_modes[str(target_row["scope_unit_name"])]
        reference_changes = _reference_changes(root, normalised["reference_frontier"])
        rendered = _render_resulting_source(source, before, after)
        toml_change = SourceChange(structure_path, STRUCTURE_RELATIVE_PATH, source, rendered)
        changes = ([toml_change] if toml_change.before != toml_change.after else []) + reference_changes
        if not changes:
            return _result(
                state="no_op", operation=operation, pre_revision=pre_revision, post_revision=pre_revision,
                target_name=target_name, resulting=target_row, parameters=normalised,
            )
        applied: list[SourceChange] = []
        try:
            _atomic_write(toml_change.path, toml_change.after)
            applied.append(toml_change)
            if after_declaration is not None:
                after_declaration()
            for change in reference_changes:
                _atomic_write(change.path, change.after)
                applied.append(change)
        except (OSError, RuntimeError) as error:
            recovery = {
                "authorized_boundary": normalised["recovery_disposition"]["boundary"],
                "toml": _boundary_entry(toml_change) if toml_change in applied else None,
                "references": [_boundary_entry(change) for change in applied if change.path != structure_path],
            }
            return _result(
                state="partial", operation=operation, pre_revision=pre_revision,
                post_revision=_digest_text(structure_path.read_text(encoding="utf-8")), target_name=target_name,
                resulting=target_row, parameters=normalised, errors=[str(error)],
                actual_effects=[_effect(change) for change in applied],
                repaired_references=[change.relative_path for change in applied if change.path != structure_path],
                recovery_boundary=recovery,
                unapplied_effects=[_effect(change) for change in changes if change not in applied],
            )
        post = _digest_text(structure_path.read_text(encoding="utf-8"))
        return _result(
            state="completed", operation=operation, pre_revision=pre_revision, post_revision=post,
            target_name=target_name, resulting=target_row, parameters=normalised,
            actual_effects=[_effect(change) for change in applied],
            repaired_references=[change.relative_path for change in reference_changes],
        )
    except StructuralConflict as error:
        post = None
        if structure_path.is_file():
            try:
                post = _digest_text(structure_path.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError):
                pass
        return _result(
            state="conflict", operation=str(operation), pre_revision=pre_revision, post_revision=post,
            target_name=normalised.get("target_name") if normalised else None,
            parameters=normalised, errors=[str(error)],
        )


def _boundary_entry(change: SourceChange) -> dict[str, str]:
    return {
        "path": change.relative_path,
        "before_sha256": change.before_sha256,
        "after_sha256": change.after_sha256,
        "before_text": change.before,
    }


def _effect(change: SourceChange) -> dict[str, str]:
    return {"path": change.relative_path, "before_sha256": change.before_sha256, "after_sha256": change.after_sha256}


def rollback_scope_unit_change(project_root: Path | str, recovery_boundary: Mapping[str, Any]) -> dict[str, Any]:
    """Restore only an exact, still-current partial cutover boundary."""
    root = Path(project_root).resolve()
    try:
        boundary = _require_mapping(recovery_boundary, "recovery_boundary")
        if not isinstance(boundary.get("authorized_boundary"), str) or not boundary["authorized_boundary"]:
            raise StructuralConflict("recovery boundary lacks authorized_boundary")
        candidates = [boundary.get("toml"), *boundary.get("references", [])]
        changes: list[SourceChange] = []
        for item in candidates:
            if item is None:
                continue
            record = _require_mapping(item, "recovery boundary member")
            if set(record) != {"path", "before_sha256", "after_sha256", "before_text"}:
                raise StructuralConflict("recovery boundary member has unsupported fields")
            path = _relative_path(root, record["path"], "recovery boundary path")
            if not path.is_file() or path.is_symlink():
                raise StructuralConflict("recovery boundary member is no longer a regular file")
            current = path.read_text(encoding="utf-8")
            if _digest_text(current) != record["after_sha256"]:
                raise StructuralConflict("recovery boundary is stale; concurrent source must not be overwritten")
            if _digest_text(record["before_text"]) != record["before_sha256"]:
                raise StructuralConflict("recovery boundary history is internally inconsistent")
            changes.append(SourceChange(path, str(record["path"]), current, str(record["before_text"])))
        if not changes:
            raise StructuralConflict("recovery boundary contains no applied source member")
        for change in changes:
            _atomic_write(change.path, change.after)
        structure = root / STRUCTURE_RELATIVE_PATH
        return {
            "state": "rolled_back",
            "operation": "Rollback",
            "pre_toml_revision": _digest_text(changes[0].before) if changes[0].path == structure else None,
            "post_toml_revision": _digest_text(structure.read_text(encoding="utf-8")) if structure.is_file() else None,
            "restored": [_effect(change) for change in changes],
            "remaining_breakages": [],
            "authorized_boundary": boundary["authorized_boundary"],
        }
    except (StructuralConflict, OSError, UnicodeDecodeError) as error:
        return {
            "state": "conflict",
            "operation": "Rollback",
            "validation_errors": [str(error)],
            "actual_effects": [],
        }


def create_scope_unit(project_root: Path | str, parameters: Mapping[str, Any]) -> dict[str, Any]:
    """CA-O-012/014 domain adapter for one declared Scope Unit Create."""
    return apply_scope_unit_action(project_root, parameters)


def rename_scope_unit(project_root: Path | str, parameters: Mapping[str, Any]) -> dict[str, Any]:
    """CA-O-012/014 domain adapter for one declared Scope Unit Rename."""
    return apply_scope_unit_action(project_root, parameters)


def move_scope_unit(project_root: Path | str, parameters: Mapping[str, Any]) -> dict[str, Any]:
    """CA-O-012/014 domain adapter for one declared Scope Unit Move."""
    return apply_scope_unit_action(project_root, parameters)


def remove_scope_unit(project_root: Path | str, parameters: Mapping[str, Any]) -> dict[str, Any]:
    """CA-O-012/014 domain adapter for one non-recursive Scope Unit Remove."""
    return apply_scope_unit_action(project_root, parameters)


_QUEUE_ROUTES = {
    "create_scope_unit": "Create",
    "rename_scope_unit": "Rename",
    "move_scope_unit": "Move",
    "remove_scope_unit": "Remove",
}


def queue_action_handlers(repository: Path | str) -> dict[str, Callable[[Mapping[str, Any]], dict[str, Any]]]:
    """Return O015-only handlers for a selected queue's frozen context.

    CA-O-004 and CA-O-005 are also used by the methodology compiler.  Their
    handlers therefore require the current O015 Workflow identity before they
    inspect structural parameters; a generic action-ID registry must compose
    handlers by Workflow/route context rather than treating those two IDs as a
    global domain selection.

    The shared selected-run service has already sealed preview/authorization
    admission before it invokes the graph.  The applying O014 adapter requires
    that fact as ``sealed_outer_admission is True`` and never creates a second
    receipt, Run, Journal event, or transition.
    """
    root = Path(repository).resolve()

    def candidate(context: Mapping[str, Any], *, shared_source_action: bool = False) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
        if not isinstance(context, Mapping):
            return None, {"result": "blocked", "effect_refs": [], "reason": "queue context is invalid"}
        if shared_source_action and context.get("workflow_definition_id") != "CA-O-015":
            return None, {"result": "blocked", "effect_refs": [], "reason": "action ID is not bound to O015"}
        route = context.get("route", context.get("operation_route"))
        parameters = context.get("parameters")
        if route not in _QUEUE_ROUTES or not isinstance(parameters, Mapping):
            return None, {"result": "blocked", "effect_refs": [], "reason": "context is not a PROJECT_STRUCTURE route"}
        if parameters.get("operation") != _QUEUE_ROUTES[route]:
            return None, {"result": "blocked", "effect_refs": [], "reason": "route and structural operation differ"}
        try:
            normalised = _normalise_parameters(parameters, root)
            source, _ = _parse_structure(root / STRUCTURE_RELATIVE_PATH, root)
            observed = _digest_text(source)
            if normalised["expected_toml_revision"] != observed:
                return None, {
                    "result": "stale", "effect_refs": [],
                    "native_result": {"state": "stale", "pre_toml_revision": observed},
                }
            return normalised, None
        except StructuralConflict as error:
            return None, {
                "result": "conflict", "effect_refs": [],
                "native_result": {"state": "conflict", "validation_errors": [str(error)]},
            }

    def select(context: Mapping[str, Any]) -> dict[str, Any]:
        normalised, failure = candidate(context, shared_source_action=True)
        if failure is not None:
            return failure
        return {
            "result": "selected",
            "effect_refs": [],
            "native_result": {
                "operation": normalised["operation"],
                "toml_revision": normalised["expected_toml_revision"],
            },
        }

    def prepare(context: Mapping[str, Any]) -> dict[str, Any]:
        normalised, failure = candidate(context)
        if failure is not None:
            return failure
        return {"result": "prepared", "effect_refs": [], "native_result": {"operation": normalised["operation"]}}

    def assess(context: Mapping[str, Any]) -> dict[str, Any]:
        normalised, failure = candidate(context, shared_source_action=True)
        if failure is not None:
            return failure
        return {"result": "accepted", "effect_refs": [], "native_result": {"operation": normalised["operation"]}}

    def authorize(context: Mapping[str, Any]) -> dict[str, Any]:
        normalised, failure = candidate(context)
        if failure is not None:
            return failure
        if context.get("sealed_outer_admission") is not True:
            return {"result": "blocked", "effect_refs": [], "reason": "D527 admission is absent"}
        return {"result": "authorized", "effect_refs": [], "native_result": {"operation": normalised["operation"]}}

    def apply(context: Mapping[str, Any]) -> dict[str, Any]:
        normalised, failure = candidate(context)
        if failure is not None:
            return failure
        if context.get("sealed_outer_admission") is not True:
            return {"result": "blocked", "effect_refs": [], "reason": "D527 admission is absent"}
        action = {
            "Create": create_scope_unit,
            "Rename": rename_scope_unit,
            "Move": move_scope_unit,
            "Remove": remove_scope_unit,
        }[normalised["operation"]]
        result = action(root, normalised)
        effects = [effect["path"] for effect in result["actual_effects"]]
        return {"result": result["state"], "effect_refs": effects, "native_result": result}

    return {
        "CA-O-004": select,
        "CA-O-012": prepare,
        "CA-O-005": assess,
        "CA-O-013": authorize,
        "CA-O-014": apply,
    }


__all__ = [
    "apply_scope_unit_action",
    "create_scope_unit",
    "move_scope_unit",
    "remove_scope_unit",
    "rename_scope_unit",
    "rollback_scope_unit_change",
    "queue_action_handlers",
    "serialize_project_structure",
]
