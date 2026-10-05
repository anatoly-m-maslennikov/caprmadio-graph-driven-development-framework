"""Read-only D572-derived Release admission for a canonical manifest loader.

This module does not load/write a manifest, validate its self-digest, register a
route, inspect an Operator approval, or create any Run/effect. The owning loader
retains those existing boundaries and calls this check before shared support.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from typing import Any, Mapping


AUTHORITY_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "201_FEATURE_TOOLS/07_delivery/CA-D-572-TOOLS-DELIVERY--serialize-additive-release-route-source-admission.md"
)
AUTHORITY_PIN = {
    "atom_id": "CA-D-572", "version": 5, "source_path": AUTHORITY_REF,
    "digest": "f310863886274866401a52a0611660de2be8f05c1ab61bc7591da53752e1e969",
}
_PIN_FIELDS = frozenset({"atom_id", "version", "source_path", "digest"})
_ADMISSION_FIELDS = frozenset({"route", "acceptance_frontier", "workflow", "ordered_steps",
                               "ordered_actions", "rmed_frontier"})
_ATOM = re.compile(r"CA-[A-Z]+-[0-9]+")
_DIGEST = re.compile(r"[0-9a-f]{64}")
_MAX_SOURCE_BYTES = 1024 * 1024


class ReleaseSourceAdmissionError(ValueError):
    """A closed Release source record cannot be admitted without new authority."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


def _reject(message: str, *, code: str = "release-source-admission-invalid") -> None:
    raise ReleaseSourceAdmissionError(code, message)


def _project_root(root: str | Path) -> Path:
    try:
        project = Path(root).resolve(strict=True)
    except (OSError, ValueError, TypeError) as error:
        raise ReleaseSourceAdmissionError("release-project-unavailable", "Project root is unavailable") from error
    if not project.is_dir():
        _reject("Project root must be a directory", code="release-project-unavailable")
    return project


def _pin_shape(pin: Any) -> dict[str, Any]:
    if not isinstance(pin, Mapping) or set(pin) != _PIN_FIELDS:
        _reject("each source pin must have exactly atom_id, version, source_path and digest")
    atom_id, version, relative, digest = (pin[field] for field in ("atom_id", "version", "source_path", "digest"))
    if not isinstance(atom_id, str) or _ATOM.fullmatch(atom_id) is None:
        _reject("source pin identity is invalid")
    if type(version) is not int or version < 1:
        _reject("source pin version must be a positive integer")
    if not isinstance(digest, str) or _DIGEST.fullmatch(digest) is None:
        _reject("source pin digest must be lowercase SHA-256")
    if not isinstance(relative, str) or not relative or "\\" in relative or ":" in relative:
        _reject("source pin path must be a safe Project-relative file")
    path = PurePosixPath(relative)
    if not path.parts or path.is_absolute() or relative != path.as_posix() or any(part in {".", ".."} for part in path.parts):
        _reject("source pin path must be a canonical safe Project-relative file")
    return dict(pin)


def _metadata(raw: bytes) -> tuple[str, int]:
    try:
        lines = raw.decode("utf-8").splitlines()
        if not lines or lines[0] != "---":
            raise ValueError("frontmatter is absent")
        end = lines.index("---", 1)
        values = {}
        for field in ("atom_id", "version"):
            matches = [line.split(":", 1)[1].strip() for line in lines[1:end]
                       if line.startswith(f"{field}:")]
            if len(matches) != 1:
                raise ValueError(f"{field} must occur exactly once")
            value = matches[0]
            if value.startswith('"'):
                value = json.loads(value)
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            values[field] = value
        atom_id, version = values["atom_id"], values["version"]
        if not isinstance(atom_id, str) or _ATOM.fullmatch(atom_id) is None:
            raise ValueError("Atom identity is invalid")
        if not isinstance(version, str) or re.fullmatch(r"[1-9][0-9]*", version) is None:
            raise ValueError("Revision Version is not a positive integer")
        return atom_id, int(version)
    except (UnicodeDecodeError, ValueError, TypeError, IndexError) as error:
        raise ReleaseSourceAdmissionError("release-source-identity-invalid", "source identity/version frontmatter is invalid") from error


def _read_pin(root: Path, value: Any) -> bytes:
    pin = _pin_shape(value)
    relative = PurePosixPath(pin["source_path"])
    cursor = root
    for part in relative.parts:
        cursor /= part
        if cursor.is_symlink():
            _reject(f"source symlinks are not admitted: {relative}", code="release-source-path-unsafe")
    try:
        if not cursor.is_file() or cursor.stat().st_size > _MAX_SOURCE_BYTES:
            raise OSError("source file is absent or exceeds the bounded read")
        raw = cursor.read_bytes()
    except OSError as error:
        raise ReleaseSourceAdmissionError("release-source-unavailable", f"source pin is unavailable: {relative}") from error
    if len(raw) > _MAX_SOURCE_BYTES:
        _reject(f"source exceeds the bounded read: {relative}", code="release-source-unavailable")
    if hashlib.sha256(raw).hexdigest() != pin["digest"]:
        _reject(f"source pin is stale: {relative}", code="release-source-pin-stale")
    if _metadata(raw) != (pin["atom_id"], pin["version"]):
        _reject(f"source identity/version differs: {relative}", code="release-source-identity-invalid")
    return raw


def _tables(text: str) -> list[list[list[str]]]:
    tables, current = [], []
    for line in text.splitlines():
        if line.startswith("|"):
            current.append([cell.strip() for cell in line.strip("|").split("|")])
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    if len(tables) != 3 or [table[0] for table in tables] != [
            ["Atom", "Version", "Source path", "SHA-256"],
            ["Order", "Step pin", "Action pin"],
            ["Atom", "Version", "Source path", "SHA-256"]]:
        _reject("accepted D572 pin tables cannot be parsed", code="release-authority-invalid")
    return tables


def _table_pin(row: list[str]) -> dict[str, Any]:
    if len(row) != 4 or re.fullmatch(r"[1-9][0-9]*", row[1]) is None:
        _reject("D572 source pin table row is malformed", code="release-authority-invalid")
    return _pin_shape({"atom_id": row[0], "version": int(row[1]),
                       "source_path": row[2].strip("`"), "digest": row[3].strip("`")})


def _occurrence_pin(value: str) -> dict[str, Any]:
    match = re.fullmatch(r"(CA-O-[0-9]+)@([1-9][0-9]*) `([^`]+)` `([0-9a-f]{64})`", value)
    if match is None:
        _reject("D572 ordered occurrence is malformed", code="release-authority-invalid")
    return _pin_shape({"atom_id": match[1], "version": int(match[2]),
                       "source_path": match[3], "digest": match[4]})


def derive_release_source_admission(project_root: str | Path) -> dict[str, Any]:
    """Derive the one accepted record from pinned actual D572@5, read-only.

    Only this defining authority is read here. The validator separately observes
    all unique referenced pins on each admission; no source-currentness cache is
    used. Returned records share no mutable dictionaries with another call.
    """
    root = _project_root(project_root)
    text = _read_pin(root, AUTHORITY_PIN).decode("utf-8")
    matches = re.findall(r"CA-P-1622@([1-9][0-9]*) at `([^`]+)`, SHA-256 `([0-9a-f]{64})`", text)
    if len(matches) != 1:
        _reject("D572 must state exactly one accepted frontier", code="release-authority-invalid")
    tables = _tables(text)
    if len(tables[0]) != 3 or len(tables[1]) != 12 or len(tables[2]) < 3:
        _reject("D572 must define one Workflow, ten occurrences and a nonempty RMED frontier", code="release-authority-invalid")
    steps = []
    for ordinal, row in enumerate(tables[1][2:], 1):
        if len(row) != 3 or row[0] != str(ordinal):
            _reject("D572 Step occurrence order is invalid", code="release-authority-invalid")
        steps.append({"step": _occurrence_pin(row[1]), "action": _occurrence_pin(row[2])})
    return {"route": "release_version",
            "acceptance_frontier": _pin_shape({"atom_id": "CA-P-1622", "version": int(matches[0][0]),
                                               "source_path": matches[0][1], "digest": matches[0][2]}),
            "workflow": _table_pin(tables[0][2]), "ordered_steps": steps,
            "ordered_actions": [copy.deepcopy(row["action"]) for row in steps],
            "rmed_frontier": [_table_pin(row) for row in tables[2][2:]]}


def _record_shape(record: Any) -> dict[str, Any]:
    if not isinstance(record, Mapping) or set(record) != _ADMISSION_FIELDS or record["route"] != "release_version":
        _reject("Release admission has unknown, absent or unsupported fields")
    _pin_shape(record["acceptance_frontier"])
    _pin_shape(record["workflow"])
    for field, count in (("ordered_steps", 10), ("ordered_actions", 10)):
        if not isinstance(record[field], list) or len(record[field]) != count:
            _reject(f"Release admission {field} must contain exactly {count} ordered entries")
    if not isinstance(record["rmed_frontier"], list) or not record["rmed_frontier"]:
        _reject("Release admission rmed_frontier must contain the D572-defined ordered entries")
    for item in record["ordered_steps"]:
        if not isinstance(item, Mapping) or set(item) != {"step", "action"}:
            _reject("Release Step occurrence must have exactly step and action")
        _pin_shape(item["step"])
        _pin_shape(item["action"])
    for pin in [*record["ordered_actions"], *record["rmed_frontier"]]:
        _pin_shape(pin)
    return dict(record)


def validate_release_source_admissions(project_root: str | Path, manifest: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Validate the optional file-level additive record before shared support.

    ``manifest`` is the owner's parsed canonical manifest, not D527's two-field
    request ``definition_manifest``. Overall manifest schema/digest, registry,
    other routes and query admissions remain the existing loader's obligation.
    No Release route means the field must be absent and D572 need not be present.
    """
    if not isinstance(manifest, Mapping) or not isinstance(manifest.get("routes"), list):
        _reject("a parsed canonical manifest route list is required")
    routes = manifest["routes"]
    if len(routes) > 16 or any(not isinstance(route, Mapping) or not isinstance(route.get("route"), str) for route in routes):
        _reject("canonical route identities are malformed or exceed the additive portfolio")
    release = [route for route in routes if route["route"] == "release_version"]
    if not release:
        if "release_source_admissions" in manifest:
            _reject("a manifest without release_version must omit Release admission")
        return []
    if len(release) != 1:
        _reject("canonical manifest must contain exactly one Release route")
    admissions = manifest.get("release_source_admissions")
    if not isinstance(admissions, list) or len(admissions) != 1:
        _reject("Release route requires exactly one source admission")
    actual = _record_shape(admissions[0])
    root = _project_root(project_root)
    expected = derive_release_source_admission(root)
    if actual != expected:
        _reject("Release admission differs from the accepted D572 source frontier")
    # Python considers True == 1; route pins must retain the same strict types
    # as admission pins even when this helper is called before the route loader.
    route_shape = {**expected, **{field: release[0].get(field)
                                 for field in ("workflow", "ordered_steps", "ordered_actions")}}
    _record_shape(route_shape)
    for field in ("workflow", "ordered_steps", "ordered_actions"):
        if release[0].get(field) != expected[field]:
            _reject(f"Release admission {field} differs from the selected route")
    pins = [expected["acceptance_frontier"], expected["workflow"],
            *[pin for row in expected["ordered_steps"] for pin in (row["step"], row["action"])],
            *expected["ordered_actions"], *expected["rmed_frontier"]]
    # This is the current D572 table's unique coverage, not a separately
    # maintained cardinality. Equality above keeps every occurrence and pin
    # exact; the mapping only avoids rereading intentionally repeated Actions.
    for pin in {pin["source_path"]: pin for pin in pins}.values():
        _read_pin(root, pin)
    return [expected]
