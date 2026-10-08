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
    "atom_id": "CA-D-572", "version": 28, "source_path": AUTHORITY_REF,
    "digest": "474581112d2e88d5c5d9d5d96d2df5ea5dd4cbd3ab179f6b0c7a57eb784a81b1",
}
_PIN_FIELDS = frozenset({"atom_id", "version", "source_path", "digest"})
_ADMISSION_FIELDS = frozenset({"route", "acceptance_frontier", "workflow", "ordered_steps",
                               "ordered_actions", "rmed_frontier", "mutation_capable",
                               "native_action_calls"})
_ATOM = re.compile(r"CA-[A-Z]+-[0-9]+")
_DIGEST = re.compile(r"[0-9a-f]{64}")
_MAX_SOURCE_BYTES = 1024 * 1024
_RELEASE_STOP_RESULT = "any missing, stale, unauthorized, failed, partial, recording-blocked, unsafe, or unmatched result"
_RELEASE_STOP_OUTCOME = "stop with its actual evidence; do not promote, retire, retry, or recurse implicitly"
_GENERIC_STOP_CONTRACT = (
    "The record serializes no catch-all transition, outcome, or execution policy: "
    "CA-O-164@6 and the generic executor retain the existing catch-all stop behavior."
)


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


def _read_pin(root: Path, value: Any, *, atom_source: bool = True) -> bytes:
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
    if atom_source and _metadata(raw) != (pin["atom_id"], pin["version"]):
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


def _route_serialization_metadata(text: str) -> dict[str, Any]:
    """Read D572's one typed route-serialization declaration, fail closed."""
    matches = re.findall(r"^## Route serialization metadata\n+```json\n(.*?)\n```$", text, re.MULTILINE | re.DOTALL)
    if len(matches) != 1:
        _reject("D572 must define exactly one typed Release route serialization metadata block",
                code="release-authority-invalid")
    try:
        metadata = json.loads(matches[0])
    except json.JSONDecodeError as error:
        raise ReleaseSourceAdmissionError(
            "release-authority-invalid", "D572 Release route serialization metadata is not JSON"
        ) from error
    if (not isinstance(metadata, dict)
            or set(metadata) != {"mutation_capable", "native_action_calls"}
            or type(metadata["mutation_capable"]) is not bool
            or metadata["native_action_calls"] != []):
        _reject("D572 Release route serialization metadata is not the closed typed declaration",
                code="release-authority-invalid")
    if text.count(_GENERIC_STOP_CONTRACT) != 1:
        _reject("D572 does not retain the generic executor catch-all stop contract",
                code="release-authority-invalid")
    return metadata


def _private_carriers(text: str) -> list[dict[str, str]]:
    """D572-only source-byte pins; these add no manifest or request fields."""
    matches = re.findall(r"^## Private implementation carriers\n+```json\n(.*?)\n```$",
                         text, re.MULTILINE | re.DOTALL)
    if len(matches) != 1:
        _reject("D572 must declare exactly one private implementation carrier block",
                code="release-authority-invalid")
    try:
        rows = json.loads(matches[0])
    except json.JSONDecodeError as error:
        raise ReleaseSourceAdmissionError("release-authority-invalid", "D572 private carriers are not JSON") from error
    if not isinstance(rows, list) or not rows:
        _reject("D572 private carriers must be a nonempty ordered source-pin list", code="release-authority-invalid")
    paths = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"source_path", "sha256"}:
            _reject("D572 private carrier fields are not closed", code="release-authority-invalid")
        _pin_shape({**AUTHORITY_PIN, "source_path": row["source_path"], "digest": row["sha256"]})
        if (not row["source_path"].startswith("102_FRAMEWORK_ENGINE/")
                or row["source_path"] in {
                    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/release_source_admission.py",
                    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_routes.py"}):
            _reject("D572 private carrier creates an authority cycle or leaves the implementation boundary",
                    code="release-authority-invalid")
        paths.append(row["source_path"])
    if paths != sorted(set(paths)):
        _reject("D572 private carrier paths must be unique and source-path sorted", code="release-authority-invalid")
    return rows


def derive_release_private_carriers(project_root: str | Path) -> list[dict[str, str]]:
    """Reopen the D572-only carrier declarations without changing admission serialization."""
    root = _project_root(project_root)
    text = _read_pin(root, AUTHORITY_PIN).decode("utf-8")
    rows = _private_carriers(text)
    for row in rows:
        _read_pin(root, {**AUTHORITY_PIN, "source_path": row["source_path"], "digest": row["sha256"]},
                  atom_source=False)
    return copy.deepcopy(rows)


def derive_unknown_effect_resolver_authority(project_root: str | Path) -> list[dict[str, Any]]:
    """Read the separate closed recovery-control pins; never extend Release admission."""
    root = _project_root(project_root)
    text = _read_pin(root, AUTHORITY_PIN).decode("utf-8")
    matches = re.findall(
        r"^## Unknown-effect resolver authority\n+\x60\x60\x60json\n(.*?)\n\x60\x60\x60$",
        text, re.MULTILINE | re.DOTALL,
    )
    if len(matches) != 1:
        _reject("D572 must carry exactly one unknown-effect resolver authority block",
                code="release-resolver-authority-invalid")
    try:
        rows = json.loads(matches[0])
    except json.JSONDecodeError as error:
        raise ReleaseSourceAdmissionError(
            "release-resolver-authority-invalid", "resolver authority is not closed JSON"
        ) from error
    ids = ("CA-R-1895", "CA-M-351", "CA-E-594", "CA-D-589")
    if not isinstance(rows, list) or len(rows) != len(ids):
        _reject("resolver authority must contain exactly four ordered pins",
                code="release-resolver-authority-invalid")
    pins = [_pin_shape(row) for row in rows]
    if tuple(pin["atom_id"] for pin in pins) != ids:
        _reject("resolver authority identities or order differ",
                code="release-resolver-authority-invalid")
    derive_release_private_carriers(root)
    for pin in pins:
        _read_pin(root, pin)
    return copy.deepcopy(pins)


def derive_release_source_admission(project_root: str | Path) -> dict[str, Any]:
    """Derive the one accepted record from pinned actual D572@13, read-only.

    This reads the defining authority and its private implementation carriers.
    The validator separately observes all unique Atom pins on each admission;
    no source-currentness cache is used. Returned records share no mutable
    dictionaries with another call.
    """
    root = _project_root(project_root)
    text = _read_pin(root, AUTHORITY_PIN).decode("utf-8")
    matches = re.findall(r"CA-P-1622@([1-9][0-9]*) at `([^`]+)`, SHA-256 `([0-9a-f]{64})`", text)
    if len(matches) != 1:
        _reject("D572 must state exactly one accepted frontier", code="release-authority-invalid")
    tables = _tables(text)
    if len(tables[0]) != 3 or len(tables[1]) != 14 or len(tables[2]) < 3:
        _reject("D572 must define one Workflow, twelve occurrences and a nonempty RMED frontier", code="release-authority-invalid")
    derive_release_private_carriers(root)
    steps = []
    for ordinal, row in enumerate(tables[1][2:], 1):
        if len(row) != 3 or row[0] != str(ordinal):
            _reject("D572 Step occurrence order is invalid", code="release-authority-invalid")
        steps.append({"step": _occurrence_pin(row[1]), "action": _occurrence_pin(row[2])})
    metadata = _route_serialization_metadata(text)
    return {"route": "release_version",
            "acceptance_frontier": _pin_shape({"atom_id": "CA-P-1622", "version": int(matches[0][0]),
                                               "source_path": matches[0][1], "digest": matches[0][2]}),
            "workflow": _table_pin(tables[0][2]), "ordered_steps": steps,
            "ordered_actions": [copy.deepcopy(row["action"]) for row in steps],
            "rmed_frontier": [_table_pin(row) for row in tables[2][2:]], **metadata}


def _release_workflow_graph(raw: bytes, admission: Mapping[str, Any]) -> dict[str, Any]:
    """Extract the closed route graph from the accepted O164 Workflow source."""
    try:
        text = raw.decode("utf-8")
        sections: dict[str, list[str]] = {"Steps": [], "Transitions": []}
        current: str | None = None
        for line in text.splitlines():
            if line in {"## Steps", "## Transitions"}:
                current = line.removeprefix("## ")
            elif current is not None and line.startswith("## "):
                current = None
            elif current is not None:
                sections[current].append(line)

        def rows(section: str, header: list[str]) -> list[list[str]]:
            table = [[cell.strip() for cell in line.strip("|").split("|")]
                     for line in sections[section] if line.startswith("|")]
            if len(table) < 2 or table[0] != header or not all(set(cell) <= {"-", " ", ":"} for cell in table[1]):
                raise ValueError(f"{section} table header is invalid")
            return table[2:]

        step_rows = rows("Steps", ["Step", "Action", "Bound phase"])
        expected_pairs = [(row["step"]["atom_id"], row["action"]["atom_id"])
                          for row in admission["ordered_steps"]]
        if (len(step_rows) != len(expected_pairs)
                or [(row[0], row[1]) for row in step_rows] != expected_pairs):
            raise ValueError("Steps do not match the accepted occurrence sequence")
        transition_rows = rows("Transitions", ["Step result", "Next step or outcome"])
        if (len(transition_rows) != len(expected_pairs) + 1
                or transition_rows[-1] != [_RELEASE_STOP_RESULT, _RELEASE_STOP_OUTCOME]):
            raise ValueError("Transitions omit or alter the required unmatched-result stop")
        transitions = []
        for event, target in transition_rows[:-1]:
            if not event.startswith("CA-O-"):
                raise ValueError("Transitions contain an unrepresentable non-Step edge")
            source, condition = event.split(" ", 1)
            transitions.append({"from": source, "condition": condition, "to": target})
        step_ids = [step for step, _ in expected_pairs]
        if (len(transitions) != len(expected_pairs)
                or [edge["from"] for edge in transitions] != step_ids
                or any(edge["to"] not in {*step_ids, "complete"} for edge in transitions)):
            raise ValueError("Transitions do not define the accepted Release graph")
    except (UnicodeDecodeError, KeyError, TypeError, ValueError) as error:
        raise ReleaseSourceAdmissionError(
            "release-authority-invalid", "accepted O164 Workflow graph cannot be parsed"
        ) from error
    return {"entry_step": step_ids[0], "on_result": transitions}


def derive_release_route_graph(project_root: str | Path) -> dict[str, Any]:
    """Derive the exact Release route graph for a future manifest publisher.

    D572 pins O164 and its twelve Step/Action occurrences; this helper reads that
    pinned Workflow source and returns the remaining route fields which a
    publisher must serialize unchanged.  It has no manifest or registry side
    effects.
    """
    return derive_release_graph_admission(project_root)[0]


def derive_release_graph_admission(project_root: str | Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """Return the source-derived closed Release route and its D572 admission.

    The pair is intended for a future publisher.  It is read-only and preserves
    the existing eight-field route schema; the O164 unmatched-result stop is
    validated here rather than serialized as a non-schema route member.
    """
    root = _project_root(project_root)
    admission = derive_release_source_admission(root)
    workflow_raw = _read_pin(root, admission["workflow"])
    graph = _release_workflow_graph(workflow_raw, admission)
    route = {"route": "release_version", "workflow": copy.deepcopy(admission["workflow"]),
             "ordered_steps": copy.deepcopy(admission["ordered_steps"]),
             "ordered_actions": copy.deepcopy(admission["ordered_actions"]), **graph,
             "mutation_capable": admission["mutation_capable"],
             "native_action_calls": copy.deepcopy(admission["native_action_calls"])}
    return route, copy.deepcopy(admission)


def _record_shape(record: Any) -> dict[str, Any]:
    if not isinstance(record, Mapping) or set(record) != _ADMISSION_FIELDS or record["route"] != "release_version":
        _reject("Release admission has unknown, absent or unsupported fields")
    _pin_shape(record["acceptance_frontier"])
    _pin_shape(record["workflow"])
    if type(record["mutation_capable"]) is not bool or record["native_action_calls"] != []:
        _reject("Release admission typed route metadata is invalid")
    for field, count in (("ordered_steps", 12), ("ordered_actions", 12)):
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
    graph, _ = derive_release_graph_admission(root)
    route_shape = {**expected, **{field: release[0].get(field)
                                  for field in ("workflow", "ordered_steps", "ordered_actions")}}
    _record_shape(route_shape)
    for field in ("workflow", "ordered_steps", "ordered_actions"):
        if release[0].get(field) != expected[field]:
            _reject(f"Release admission {field} differs from the selected route")
    for field in ("entry_step", "on_result"):
        if release[0].get(field) != graph[field]:
            _reject(f"Release route {field} differs from the accepted Workflow graph")
    for field in ("native_action_calls", "mutation_capable"):
        if release[0].get(field) != expected[field]:
            _reject(f"Release route {field} differs from the accepted source admission")
    pins = [expected["acceptance_frontier"], expected["workflow"],
            *[pin for row in expected["ordered_steps"] for pin in (row["step"], row["action"])],
            *expected["ordered_actions"], *expected["rmed_frontier"]]
    # This is the current D572 table's unique coverage, not a separately
    # maintained cardinality. Equality above keeps every occurrence and pin
    # exact; the mapping only avoids rereading intentionally repeated Actions.
    for pin in {pin["source_path"]: pin for pin in pins}.values():
        _read_pin(root, pin)
    return [expected]
