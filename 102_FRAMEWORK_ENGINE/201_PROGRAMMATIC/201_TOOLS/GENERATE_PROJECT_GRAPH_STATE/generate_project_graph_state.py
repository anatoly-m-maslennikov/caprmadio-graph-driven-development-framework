#!/usr/bin/env python3
"""Generate a bounded, non-authoritative view of the live CAPRMEDIO control root."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
import tomllib


SCRIPT = Path(__file__).resolve()
ROOT = next(parent for parent in SCRIPT.parents if (parent / ".git").exists())
CONTROL = ROOT / ".caprmedio_caprmedio"
TOOLS_ROOT = SCRIPT.parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from framework_installation import InstallationError, installation_status  # noqa: E402
from artifact_metadata import SETTINGS_PATH, atom_identifier, project_identity  # noqa: E402
from project_runtime import atomic_tempfile  # noqa: E402


OUTPUT = CONTROL / "project_scope_unit_graph.projection.toml"
SOURCE_MAP = CONTROL / "project_scope_unit_graph_sources.projection.toml"
CANONICAL_GENERATOR_CARRIER = Path(
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_PROJECT_GRAPH_STATE/"
    "generate_project_graph_state.py"
)
CANONICAL_GENERATOR = ROOT / CANONICAL_GENERATOR_CARRIER
CONFIG = (
    ROOT
    / ".caprmedio_framework"
    / "00_APPLICABLE_METHODOLOGY"
    / "000_APPLICABLE_MTHD_sources"
    / "003_PROJECT_CONFIGURATION"
    / "caprmedio_framework_settings.toml"
)
METHODOLOGY_SOURCES = CONFIG.parent.parent
METHODOLOGY_SOURCE_SCOPE_UNITS = (
    ("CORE_META_MODEL", METHODOLOGY_SOURCES / "001_CORE_META_MODEL"),
    ("INSTALLED_EXTENSIONS", METHODOLOGY_SOURCES / "002_INSTALLED_EXTENSIONS"),
    ("PROJECT_CONFIGURATION", METHODOLOGY_SOURCES / "003_PROJECT_CONFIGURATION"),
)
JOURNAL = CONTROL / "work_journal"
INACTIVE_FOLDERS = frozenset({"archive", "drafts", "done", "solved", "handled", "canceled", "cancelled"})
SCOPE_UNIT_NAME = re.compile(
    r"(?P<numeric_prefix>[0-9]+)_(?P<unit_type>LAYER|FEATURE)_(?:(?P<local_order>[1-9][0-9]*)_)?(?P<name>[A-Z][A-Z0-9_]*)\Z"
)
SCOPE_UNIT_CANDIDATE = re.compile(r"[0-9]+_(?:LAYER|FEATURE)_")
EPIC_DIRECTORY = re.compile(
    r"[0-9]+-CA-Epic-[0-9]+-[A-Z][A-Z0-9_]*-[a-z0-9][a-z0-9-]*\Z"
)
TIMESTAMP = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\Z")
TIMESTAMP_WITH_OFFSET = re.compile(
    r"([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})(?: [+-][0-9]{4})\Z"
)
ISO_TIMESTAMP = re.compile(r"([0-9]{4}-[0-9]{2}-[0-9]{2})T([0-9]{2}:[0-9]{2}:[0-9]{2})(?:Z|[+-][0-9]{2}:[0-9]{2})\Z")


def sha(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def quote(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def project_relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def normalise_timestamp(value: object) -> str:
    if not isinstance(value, str):
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '\"'}:
        value = value[1:-1]
    if TIMESTAMP.fullmatch(value):
        return value
    local_match = TIMESTAMP_WITH_OFFSET.fullmatch(value)
    if local_match:
        return local_match.group(1)
    match = ISO_TIMESTAMP.fullmatch(value)
    return f"{match.group(1)} {match.group(2)}" if match else ""


def canonical_json_digest(value: object) -> str:
    """Return the Work Journal canonical digest for one JSON-compatible value."""

    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def generator_metadata(executed_generator: Path | None = None) -> dict[str, str]:
    """Describe canonical source authority separately from this execution carrier."""

    if not CANONICAL_GENERATOR.is_file():
        raise SystemExit("canonical Project Scope Unit Graph Generator source is missing")
    executed_path = SCRIPT if executed_generator is None else executed_generator.resolve()
    try:
        executed = project_relative(executed_path)
    except ValueError as error:
        raise SystemExit("executed Project Scope Unit Graph Generator is outside the repository") from error
    return {
        "canonical_generator": CANONICAL_GENERATOR_CARRIER.as_posix(),
        "canonical_generator_sha256": sha(CANONICAL_GENERATOR),
        "executed_generator": executed,
        "executed_generator_sha256": sha(executed_path),
    }


def canonical_projection_bytes(payload: str) -> bytes:
    """Return the execution-independent canonical bytes of one graph Projection."""

    return "\n".join(
        line
        for line in payload.splitlines()
        if not line.startswith("executed_generator")
    ).encode("utf-8") + b"\n"


def journal_records(journal: Path) -> list[tuple[Path, int, dict[str, object]]]:
    """Return parseable Work Journal records in canonical carrier and line order."""

    records: list[tuple[Path, int, dict[str, object]]] = []
    for carrier in sorted(journal.glob("*.ndjson")):
        with carrier.open(encoding="utf-8") as source:
            for number, line in enumerate(source, 1):
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(record, dict):
                    records.append((carrier, number, record))
    return records


def configuration_binding(config_sha: str, carrier: Path | None = None) -> dict[str, str]:
    """Resolve the one completed receipt for the canonical native carrier."""

    matches: list[dict[str, str]] = []
    carrier = CONFIG if carrier is None else carrier
    configuration_path = project_relative(carrier)
    for carrier in sorted(JOURNAL.glob("*.ndjson")):
        for number, line in enumerate(carrier.read_text(encoding="utf-8").splitlines(), 1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(record, dict):
                continue
            result = record.get("result")
            if (
                record.get("kind") != "governed_project_change"
                or record.get("event") != "completed"
                or record.get("subject_kind") != "file"
                or not isinstance(result, dict)
                or result.get("path") != configuration_path
                or result.get("sha256") != config_sha
                or not isinstance(result.get("version"), int)
            ):
                continue
            updated_at = normalise_timestamp(record.get("occurred_at"))
            if not updated_at:
                continue
            matches.append(
                {
                    "revision": str(result["version"]),
                    "journal_carrier": project_relative(carrier),
                    "journal_line": str(number),
                    "journal_event_id": str(record.get("event_id", "unknown")),
                    "updated_at": updated_at,
                }
            )
    if len(matches) == 1:
        return {"identifier": carrier.stem, "status": "resolved", **matches[0]}
    return {
        "identifier": carrier.stem,
        "status": "unresolved" if not matches else "ambiguous",
        "revision": "unknown",
        "journal_carrier": "",
        "journal_line": "",
        "journal_event_id": "",
        "updated_at": "",
    }


def settings_bindings() -> dict[str, dict[str, str]]:
    """Bind both authoritative Settings Carriers independently."""
    bindings = {}
    for kind, carrier in (("project_settings", ROOT / SETTINGS_PATH), ("framework_settings", CONFIG)):
        digest = sha(carrier)
        bindings[kind] = {
            **configuration_binding(digest, carrier),
            "carrier": project_relative(carrier),
            "sha256": digest,
        }
    return bindings


def configuration() -> dict[str, object]:
    try:
        identity = project_identity(ROOT)
        if not CONFIG.is_file() or CONFIG.is_symlink():
            raise ValueError("Framework Instance Settings Carrier is missing or invalid")
        framework = tomllib.loads(CONFIG.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError) as error:
        raise SystemExit(str(error)) from error
    artifacts = framework.get("artifacts")
    if "project" in framework or (isinstance(artifacts, dict) and "identity" in artifacts):
        raise SystemExit("Project identity belongs only in Project Settings, not Framework Instance Settings")
    modes = framework.get("authority_modes")
    if not isinstance(modes, dict):
        raise SystemExit("Framework Instance Settings lacks authority_modes")
    for key in ("default", "governance", "metamodel", "project", "semantics"):
        if not isinstance(modes.get(key), str) or not modes[key]:
            raise SystemExit(f"Framework Instance Settings lacks authority_modes.{key}")
    return {
        "project": identity["project"],
        "artifacts": {"identity": identity["identity"]},
        "authority_modes": modes,
    }


def active_path(path: Path, control: Path) -> bool:
    return not INACTIVE_FOLDERS.intersection(path.relative_to(control).parts)


def parse_scope_unit_name(name: str) -> dict[str, object] | None:
    match = SCOPE_UNIT_NAME.fullmatch(name)
    if match is None:
        if SCOPE_UNIT_CANDIDATE.match(name):
            raise SystemExit(f"invalid Scope Unit Directory Carrier name: {name}")
        return None
    scope_unit_label = match["unit_type"]
    local_order = match["local_order"]
    if (scope_unit_label == "LAYER") != (local_order is not None):
        raise SystemExit(f"invalid Local Order for Scope Unit Directory Carrier: {name}")
    return {
        "scope_unit_name": match["name"],
        "scope_unit_label": scope_unit_label,
        # A Scope Unit's Type value is determined by Local Order participation,
        # not by the independent Operator-controlled Label.
        "scope_unit_type": "Ordered" if local_order is not None else "Unordered",
        "numeric_prefix": match["numeric_prefix"],
        "local_order": int(local_order) if local_order is not None else None,
    }


def navigational_order_number(
    numeric_prefix: str, structural_level: int, structural_level_width: int
) -> int:
    """Validate the dynamic prefix allocation and return its Navigational Order Number."""

    if structural_level < 1 or structural_level_width < 1:
        raise SystemExit("invalid derived Scope Unit Structural Level")
    if len(numeric_prefix) <= structural_level_width:
        raise SystemExit(f"numeric prefix lacks Navigational Order Number: {numeric_prefix}")
    level_digits = numeric_prefix[:structural_level_width]
    navigational_order_digits = numeric_prefix[structural_level_width:]
    if int(level_digits) != structural_level:
        raise SystemExit(
            "numeric prefix Structural Level does not match typed Scope Unit ancestry: "
            f"{numeric_prefix}"
        )
    navigational_order = int(navigational_order_digits)
    if navigational_order < 1:
        raise SystemExit(f"numeric prefix has invalid Navigational Order Number: {numeric_prefix}")
    return navigational_order


def scope_units(control: Path, root: Path, modes: dict[str, object]) -> list[dict[str, object]]:
    """Discover active typed Scope Units and link each to its nearest typed parent."""

    try:
        project_name = project_identity(root)["project"]["name"]
    except ValueError as error:
        raise SystemExit(str(error)) from error
    default_mode = modes.get("default")
    if not isinstance(default_mode, str) or not default_mode:
        raise SystemExit("Project Configuration lacks authority_modes.default")
    rows: list[dict[str, object]] = []
    for carrier in sorted((path for path in control.rglob("*") if path.is_dir()), key=lambda path: path.as_posix()):
        if not active_path(carrier, control):
            continue
        if EPIC_DIRECTORY.fullmatch(carrier.name):
            continue
        parsed = parse_scope_unit_name(carrier.name)
        if parsed is None:
            continue
        relative_to_control = carrier.relative_to(control).as_posix()
        rows.append(
            {
                "node_id": relative_to_control,
                "scope_unit_name": parsed["scope_unit_name"],
                "project_boundary_position": "PROJECT",
                "scope_unit_type": parsed["scope_unit_type"],
                "authority_path": carrier.relative_to(root).as_posix(),
                "authority_materialized": True,
                "numeric_prefix": parsed["numeric_prefix"],
                "scope_unit_label": parsed["scope_unit_label"],
                "authority_mode": default_mode,
                "local_order": parsed["local_order"],
                "parent": project_name,
                "structural_parent": project_name,
            }
        )
    if not rows:
        raise SystemExit("no active typed Scope Unit Directory Carriers found")
    by_path = {control / str(row["node_id"]): row for row in rows}
    for row in rows:
        parent = (control / str(row["node_id"])).parent
        parent_row: dict[str, object] | None = None
        while parent != control:
            parent_row = by_path.get(parent)
            if parent_row is not None:
                row["parent"] = parent_row["node_id"]
                row["structural_parent"] = parent_row["node_id"]
                break
            parent = parent.parent
        row["structural_level"] = 1 if parent_row is None else int(parent_row["structural_level"]) + 1
    structural_level_width = len(str(max(int(row["structural_level"]) for row in rows)))
    for row in rows:
        row["navigational_order_number"] = navigational_order_number(
            str(row["numeric_prefix"]),
            int(row["structural_level"]),
            structural_level_width,
        )
    for row in rows:
        children = [child for child in rows if child["parent"] == row["node_id"]]
        child_types = {str(child["scope_unit_type"]) for child in children}
        if not child_types:
            row["child_composition"] = "NONE"
        elif child_types == {"Ordered"}:
            row["child_composition"] = "ORDERED"
        elif child_types == {"Unordered"}:
            row["child_composition"] = "UNORDERED"
        else:
            row["child_composition"] = "MIXED"
    return rows


def current_directory_entries(directory: Path) -> list[dict[str, str]]:
    """Return the exact Git-admitted current file frontier of one Directory Carrier."""

    relative = project_relative(directory)
    completed = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard", "--", relative],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise SystemExit("cannot resolve the Git-admitted Scope Unit Directory Carrier frontier")
    entries: list[dict[str, str]] = []
    for value in completed.stdout.splitlines():
        path = ROOT / value
        if not path.is_file():
            raise SystemExit(f"Scope Unit Directory Carrier contains an unresolved entry: {value}")
        entries.append({"path": value, "sha256": sha(path)})
    return sorted(entries, key=lambda entry: entry["path"])


def directory_receipt(directory: Path) -> dict[str, str]:
    """Resolve the one completed Work Journal receipt for a current Directory Carrier."""

    relative = project_relative(directory)
    current_entries = current_directory_entries(directory)
    if not current_entries:
        raise SystemExit(f"Scope Unit Directory Carrier is empty: {relative}")
    relative_entries = [
        {"path": Path(entry["path"]).relative_to(relative).as_posix(), "sha256": entry["sha256"]}
        for entry in current_entries
    ]
    expected_digest = canonical_json_digest(relative_entries)
    matches: list[dict[str, str]] = []
    for carrier, number, record in journal_records(JOURNAL):
        result = record.get("result")
        if (
            record.get("kind") != "governed_project_change"
            or record.get("event") != "completed"
            or record.get("subject_kind") != "folder"
            or not isinstance(result, dict)
            or result.get("path") != relative
            or result.get("sha256") != expected_digest
            or not isinstance(result.get("version"), int)
            or result.get("entries") != current_entries
        ):
            continue
        updated_at = normalise_timestamp(record.get("occurred_at"))
        event_id = record.get("event_id")
        if not updated_at or not isinstance(event_id, str) or not event_id:
            continue
        matches.append(
            {
                "carrier": relative,
                "revision": str(result["version"]),
                "sha256": expected_digest,
                "journal_carrier": project_relative(carrier),
                "journal_line": str(number),
                "journal_event_id": event_id,
                "updated_at": updated_at,
            }
        )
    if len(matches) != 1:
        state = "unresolved" if not matches else "ambiguous"
        raise SystemExit(f"{state} exact Work Journal receipt for Scope Unit Directory Carrier: {relative}")
    return matches[0]


def atom_frontmatter(path: Path) -> tuple[str, str]:
    """Return frontmatter and body from one governed Markdown Atom carrier."""

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit(f"Delivery Atom lacks frontmatter: {project_relative(path)}")
    boundary = text.find("\n---\n", 4)
    if boundary < 0:
        raise SystemExit(f"Delivery Atom has unterminated frontmatter: {project_relative(path)}")
    return text[4:boundary], text[boundary + len("\n---\n") :]


DELIVERY_BINDING = re.compile(
    r"(?m)^[A-Z][A-Z0-9_]* uses authority path `(?P<authority_path>[^`]+)` "
    r"and Delivery path `(?P<delivery_path>[^`]+)`\.$"
)
DELIVERY_ATOM_ID = re.compile(r"(?P<atom_id>CA-D-[0-9]+)-")


def delivery_atom_binding(directory: Path, receipt: dict[str, str]) -> dict[str, str]:
    """Resolve the sole active Delivery Atom which binds one Scope Unit's places."""

    delivery_directory = directory / "07_delivery"
    if not delivery_directory.is_dir():
        raise SystemExit(f"Scope Unit lacks a Delivery directory: {project_relative(directory)}")
    authority_path = project_relative(directory) + "/"
    candidates: list[dict[str, str]] = []
    receipt_entries = {
        entry["path"]: entry["sha256"] for entry in current_directory_entries(directory)
    }
    for path in sorted(delivery_directory.glob("*.md")):
        frontmatter, body = atom_frontmatter(path)
        matches = list(DELIVERY_BINDING.finditer(body))
        if len(matches) != 1 or matches[0]["authority_path"] != authority_path:
            continue
        versions = re.findall(r"(?m)^version:\s*([1-9][0-9]*)\s*$", frontmatter)
        updated_ats = re.findall(r"(?m)^updated_at:\s*([^\n]+)\s*$", frontmatter)
        atom_id_match = DELIVERY_ATOM_ID.match(path.name)
        updated_at = normalise_timestamp(updated_ats[0]) if len(updated_ats) == 1 else ""
        if len(versions) != 1 or not atom_id_match or not updated_at:
            raise SystemExit(f"Delivery Atom lacks an exact revision: {project_relative(path)}")
        digest = sha(path)
        path_relative = project_relative(path)
        if receipt_entries.get(path_relative) != digest:
            raise SystemExit(
                "Scope Unit Directory Carrier receipt does not bind its active Delivery Atom: "
                f"{path_relative}"
            )
        candidates.append(
            {
                "atom_id": atom_id_match["atom_id"],
                "carrier": path_relative,
                "revision": versions[0],
                "sha256": digest,
                "authority_path": authority_path,
                "delivery_path": matches[0]["delivery_path"],
                "journal_carrier": receipt["journal_carrier"],
                "journal_line": receipt["journal_line"],
                "journal_event_id": receipt["journal_event_id"],
                "updated_at": updated_at,
            }
        )
    if len(candidates) != 1:
        state = "missing" if not candidates else "ambiguous"
        raise SystemExit(
            f"{state} active Delivery Atom binding for Scope Unit Directory Carrier: "
            f"{project_relative(directory)}"
        )
    return candidates[0]


def delivery_path_from_scope_unit(row: dict[str, object]) -> str:
    """Derive one Delivery path from the typed Scope Unit directory coordinate."""

    segments: list[str] = []
    for segment in str(row["node_id"]).split("/"):
        parsed = parse_scope_unit_name(segment)
        if parsed is None:
            raise SystemExit(f"Scope Unit Directory Carrier is not typed: {segment}")
        segments.append(str(parsed["numeric_prefix"]) + "_" + str(parsed["scope_unit_name"]))
    return "/".join(segments) + "/"


def bind_scope_unit_structure(scope_unit_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    """Attach deterministic Delivery paths without treating Project folders as authority."""

    for row in scope_unit_rows:
        row["delivery_path"] = delivery_path_from_scope_unit(row)
        row["structure_sha256"] = canonical_json_digest(
            {key: row[key] for key in SCOPE_UNIT_GRAPH_FIELDS if key != "delivery_path"}
        )
    return scope_unit_rows


def active_source_atoms() -> list[dict[str, str]]:
    """Return the deterministic active Atom frontier of every configured source Scope Unit."""

    atoms: list[dict[str, str]] = []
    atom_ids: set[str] = set()
    for source_scope_unit, directory in METHODOLOGY_SOURCE_SCOPE_UNITS:
        if not directory.is_dir():
            raise SystemExit(f"configured Methodology Source Scope Unit is missing: {project_relative(directory)}")
        for path in sorted(directory.rglob("*.md")):
            relative = path.relative_to(directory)
            if INACTIVE_FOLDERS.intersection(relative.parts):
                continue
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---\n"):
                continue
            boundary = text.find("\n---\n", 4)
            if boundary < 0:
                raise SystemExit(f"unterminated source Atom frontmatter: {project_relative(path)}")
            frontmatter = text[4:boundary]
            declared_atom_id = re.findall(r"(?m)^atom_id:\s*([^\n]+)\s*$", frontmatter)
            version = re.findall(r"(?m)^version:\s*([1-9][0-9]*)\s*$", frontmatter)
            updated_at = re.findall(r"(?m)^updated_at:\s*([^\n]+)\s*$", frontmatter)
            filename_atom_id = path.stem.partition("--")[0]
            if len(declared_atom_id) > 1 or not filename_atom_id or len(version) != 1 or len(updated_at) != 1:
                raise SystemExit(f"source Atom lacks one identity and revision: {project_relative(path)}")
            atom_id = atom_identifier(path.name, declared_atom_id[0] if declared_atom_id else None)
            if atom_id in atom_ids:
                raise SystemExit(f"duplicate active source Atom identity: {atom_id}")
            timestamp = normalise_timestamp(updated_at[0])
            if not timestamp:
                raise SystemExit(f"source Atom lacks a valid timestamp: {project_relative(path)}")
            atom_ids.add(atom_id)
            atoms.append(
                {
                    "source_scope_unit": source_scope_unit,
                    "carrier": project_relative(path),
                    "atom_id": atom_id,
                    "atom_id_source": "frontmatter" if declared_atom_id else "filename",
                    "version": version[0],
                    "updated_at": timestamp,
                    "sha256": sha(path),
                }
            )
    if not atoms:
        raise SystemExit("configured Methodology Source Scope Units contain no active Atoms")
    return atoms


def source_updated_at(
    bindings: dict[str, dict[str, str]],
    source_atoms: list[dict[str, str]],
) -> str:
    candidates = [*(item["updated_at"] for item in bindings.values()), *(item["updated_at"] for item in source_atoms)]
    valid = [value for value in candidates if TIMESTAMP.fullmatch(value)]
    if not valid:
        raise SystemExit("no valid source revision timestamp")
    return max(valid)


SCOPE_UNIT_GRAPH_FIELDS = (
    "node_id",
    "scope_unit_name",
    "project_boundary_position",
    "scope_unit_type",
    "scope_unit_label",
    "child_composition",
    "structural_level",
    "local_order",
    "navigational_order_number",
    "parent",
    "structural_parent",
    "authority_path",
    "delivery_path",
    "authority_materialized",
    "numeric_prefix",
    "authority_mode",
)


def settings_binding_lines(bindings: dict[str, dict[str, str]]) -> list[str]:
    lines = []
    for kind, binding in bindings.items():
        lines += [f"[settings.{kind}]"]
        lines += [f"{key} = {quote(value)}" for key, value in binding.items()]
        lines.append("")
    return lines


def project_scope_unit_graph(
    updated_at: str,
    config: dict[str, object],
    bindings: dict[str, dict[str, str]],
    scope_unit_rows: list[dict[str, object]],
    source_atoms: list[dict[str, str]],
    executed_generator: Path | None = None,
) -> str:
    project = config["project"]
    identity = config["artifacts"]["identity"]
    modes = config["authority_modes"]
    assert isinstance(project, dict) and isinstance(identity, dict) and isinstance(modes, dict)
    generator = generator_metadata(executed_generator)
    lines = [
        "# Generated projection. Delete and regenerate; do not edit directly.",
        "[projection]",
        'schema_version = "4"',
        'kind = "project_scope_unit_graph"',
        "non_authoritative = true",
        f"currentness = {quote('exact_source_bound' if all(item['status'] == 'resolved' for item in bindings.values()) else 'unknown')}",
        f"updated_at = {quote(updated_at)}",
        *[f"{key} = {quote(value)}" for key, value in generator.items()],
        "",
        *settings_binding_lines(bindings),
        "[project]",
        f"key = {quote(project['key'])}",
        f"name = {quote(project['name'])}",
        f"repository_slug = {quote(project['repository_slug'])}",
        f"obsolete_names = {quote(project['obsolete_names'])}",
        "",
        "[artifacts.identity]",
        f"project_prefix = {quote(identity['project_prefix'])}",
        "",
        "[authority_modes]",
        *[f"{key} = {quote(modes[key])}" for key in sorted(modes)],
        "",
        "[repository]",
        f"control_root = {quote(project_relative(CONTROL))}",
        f"scope_unit_count = {len(scope_unit_rows)}",
        "",
        "[methodology_source_frontier]",
        f"source_scope_unit_count = {len(METHODOLOGY_SOURCE_SCOPE_UNITS)}",
        f"atom_count = {len(source_atoms)}",
        f"digest = {quote(canonical_json_digest(source_atoms))}",
    ]
    for row in scope_unit_rows:
        lines += ["", "[[scope_units]]"]
        for key in SCOPE_UNIT_GRAPH_FIELDS:
            value = row[key]
            if value is None:
                continue
            encoded = str(value).lower() if isinstance(value, bool) else value if isinstance(value, int) else quote(value)
            lines.append(f"{key} = {encoded}")
    for source_atom in source_atoms:
        lines += ["", "[[methodology_source_atoms]]"] + [
            f"{key} = {quote(value)}" for key, value in source_atom.items()
        ]
    return "\n".join(lines) + "\n"


def project_scope_unit_graph_sources(
    updated_at: str,
    bindings: dict[str, dict[str, str]],
    scope_unit_rows: list[dict[str, object]],
    source_atoms: list[dict[str, str]],
    executed_generator: Path | None = None,
) -> str:
    generator = generator_metadata(executed_generator)
    lines = [
        "# Generated source bindings. Delete and regenerate; do not edit directly.",
        "[projection]",
        'schema_version = "4"',
        'kind = "project_scope_unit_graph_sources"',
        "non_authoritative = true",
        f"currentness = {quote('exact_source_bound' if all(item['status'] == 'resolved' for item in bindings.values()) else 'unknown')}",
        f"updated_at = {quote(updated_at)}",
        f"graph_projection = {quote(project_relative(OUTPUT))}",
        *[f"{key} = {quote(value)}" for key, value in generator.items()],
    ]

    def append_binding(
        output_path: str,
        source_kind: str,
        source_carrier: str,
        source_revision: str,
        source_sha256: str,
        journal_binding: dict[str, str] | None = None,
    ) -> None:
        lines.extend(
            [
                "",
                "[[bindings]]",
                f"output_path = {quote(output_path)}",
                f"source_kind = {quote(source_kind)}",
                f"source_carrier = {quote(source_carrier)}",
                f"source_revision = {quote(source_revision)}",
                f"source_sha256 = {quote(source_sha256)}",
            ]
        )
        if journal_binding is not None:
            lines.extend(
                [
                    f"journal_carrier = {quote(journal_binding['journal_carrier'])}",
                    f"journal_line = {quote(journal_binding['journal_line'])}",
                    f"journal_event_id = {quote(journal_binding['journal_event_id'])}",
                ]
            )

    for output_path in (
        "project.key", "project.name", "project.repository_slug", "project.obsolete_names",
        "artifacts.identity.project_prefix", "authority_modes",
    ):
        kind = "framework_settings" if output_path == "authority_modes" else "project_settings"
        binding = bindings[kind]
        append_binding(
            output_path, kind, binding["carrier"],
            f"{binding['identifier']}@{binding['revision']}", binding["sha256"], binding,
        )
    for row in scope_unit_rows:
        node_path = "scope_units." + str(row["node_id"])
        structure_carrier = str(row["authority_path"])
        structure_revision = "observed_scope_unit_structure"
        structure_sha256 = str(row["structure_sha256"])
        for field in SCOPE_UNIT_GRAPH_FIELDS:
            if row[field] is None:
                continue
            if field == "authority_mode":
                kind = "framework_settings"
            elif field in {"parent", "structural_parent"} and row[field] not in {item["node_id"] for item in scope_unit_rows}:
                kind = "project_settings"
            else:
                kind = None
            if kind is not None:
                binding = bindings[kind]
                append_binding(
                    node_path + "." + field, kind, binding["carrier"],
                    f"{binding['identifier']}@{binding['revision']}", binding["sha256"], binding,
                )
                continue
            append_binding(
                node_path + "." + field,
                "scope_unit_directory_structure",
                structure_carrier,
                structure_revision,
                structure_sha256,
            )
    for source_atom in source_atoms:
        revision = source_atom["atom_id"] + "@" + source_atom["version"] + "," + source_atom["updated_at"]
        append_binding(
            "methodology_source_atoms." + source_atom["atom_id"],
            "methodology_source_atom",
            source_atom["carrier"],
            revision,
            source_atom["sha256"],
        )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write both generated Projections")
    parser.add_argument("--describe", action="store_true", help="describe the Tool without reading sources")
    return parser.parse_args()


def installed_generator() -> None:
    try:
        installed = installation_status(ROOT)
    except InstallationError as error:
        raise SystemExit(f"{error.code}: {error.message}") from error
    expected = ROOT / str(installed["package_root"]) / "GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py"
    if SCRIPT != expected.resolve():
        raise SystemExit("run the selected installed GENERATE_PROJECT_GRAPH_STATE Tool")


def write_output(path: Path, payload: str) -> None:
    descriptor, temporary_name = atomic_tempfile(path, "generate_project_graph_state")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def main() -> None:
    args = parse_args()
    if args.describe:
        print(json.dumps({"kind": "project_scope_unit_graph", "outputs": [project_relative(OUTPUT), project_relative(SOURCE_MAP)], "writes_only_with_apply": True}, sort_keys=True))
        return
    if not CONTROL.is_dir() or not CONFIG.is_file():
        raise SystemExit("required control root or Project Configuration is missing")
    config = configuration()
    bindings = settings_bindings()
    if any(item["status"] != "resolved" for item in bindings.values()):
        raise SystemExit("Settings current revision binding is unresolved or ambiguous")
    source_atoms = active_source_atoms()
    modes = config["authority_modes"]
    assert isinstance(modes, dict)
    rows = bind_scope_unit_structure(scope_units(CONTROL, ROOT, modes))
    updated_at = source_updated_at(bindings, source_atoms)
    graph_payload = project_scope_unit_graph(updated_at, config, bindings, rows, source_atoms)
    sources_payload = project_scope_unit_graph_sources(updated_at, bindings, rows, source_atoms)
    changed = (not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != graph_payload) or (
        not SOURCE_MAP.is_file() or SOURCE_MAP.read_text(encoding="utf-8") != sources_payload
    )
    print(json.dumps({"apply": args.apply, "changed": changed, "methodology_source_atoms": len(source_atoms), "outputs": [project_relative(OUTPUT), project_relative(SOURCE_MAP)], "scope_units": len(rows)}, sort_keys=True))
    if not args.apply:
        return
    installed_generator()
    write_output(OUTPUT, graph_payload)
    write_output(SOURCE_MAP, sources_payload)


if __name__ == "__main__":
    main()
