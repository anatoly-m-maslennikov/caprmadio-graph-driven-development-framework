#!/usr/bin/env python3
"""Compile a current, non-authoritative Applicable Methodology projection.

The module is deliberately an Action adapter, not a workflow executor.  The
source graph invokes its six exported adapters; shared run support owns run and
Journal lifecycle evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artifact_metadata import SETTINGS_PATH, atom_identifier


DEFAULT_CONTROL_ROOT = SETTINGS_PATH.parent
FRAMEWORK_APPLICABLE_RELATIVE = Path("000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY")
OUTPUT_RELATIVE = DEFAULT_CONTROL_ROOT / FRAMEWORK_APPLICABLE_RELATIVE
SOURCE_RELATIVE = OUTPUT_RELATIVE / "000_APPLICABLE_MTHD_sources"
APPROVAL_RELATIVE = SOURCE_RELATIVE / "003_PROJECT_CONFIGURATION/applicable_methodology_conflict_approvals.toml"
STRUCTURE_RELATIVE = SETTINGS_PATH.parent / "project_structure.toml"
LAYERS = (
    ("CORE_META_MODEL", "001_CORE_META_MODEL", 0, True),
    ("INSTALLED_EXTENSIONS", "002_INSTALLED_EXTENSIONS", 1, True),
    ("PROJECT_CONFIGURATION", "003_PROJECT_CONFIGURATION", 2, True),
)
ROLES = (
    ("REQUIREMENT", "04_requirement"),
    ("METHOD", "05_method"),
    ("EVALUATION", "06_evaluation"),
    ("DELIVERY", "07_delivery"),
    ("OPERATIONS", "09_operations"),
)
ROLE_BY_DIRECTORY = {directory: role for role, directory in ROLES}
ROLE_ORDER = {directory: index for index, (_, directory) in enumerate(ROLES)}
IGNORED_INSTALLED_EXTENSION_FILES = {".gitkeep"}
RELATION_KINDS = {
    "replacement": {"replacement_of", "replaces"},
    "incompatible": {"incompatible_with", "incompatibility_with"},
}
SCHEMA = "caprmedio.compile_applicable_methodology.v2"
WORKFLOW_ID = "CA-O-011"
ACTION_IDS = ("CA-O-004", "CA-O-005", "CA-O-006", "CA-O-007", "CA-O-008", "CA-O-009")
OPERATIONS = frozenset({"dry_run", "apply", "recover_publication"})
REQUEST_FIELDS = frozenset({
    "operation", "project_root", "governed_bindings", "expected_source_frontier_digest",
    "decision_refs", "failed_publication_ref", "run_receipt_refs",
})
FORBIDDEN_REQUEST_FIELDS = frozenset({
    "source_root", "output_path", "edit_source", "source_patch", "selected_candidate",
    "approval_text", "approval", "journal_event", "run_event", "journal_payload",
})
SETTINGS_FILENAMES = (
    Path("001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"),
    Path("003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml"),
)


@dataclass(frozen=True)
class MethodologyPaths:
    source: Path = SOURCE_RELATIVE
    output: Path = OUTPUT_RELATIVE
    structure_sha256: str | None = None
    control_root: Path = DEFAULT_CONTROL_ROOT

    @property
    def approvals(self) -> Path:
        return self.source / "003_PROJECT_CONFIGURATION/applicable_methodology_conflict_approvals.toml"


def configured_control_root(root: Path) -> Path:
    """Resolve the one Project-local control root from Project Settings."""
    settings_path = root / SETTINGS_PATH
    if not settings_path.is_file() or settings_path.is_symlink():
        raise CompileError("project-settings-missing", "Project Settings Carrier is required", path=SETTINGS_PATH.as_posix())
    try:
        settings = tomllib.loads(settings_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise CompileError("project-settings-invalid", "Project Settings Carrier must be valid UTF-8 TOML", path=SETTINGS_PATH.as_posix()) from error
    value = settings.get("paths", {}).get("control_root") if isinstance(settings.get("paths"), dict) else None
    if not isinstance(value, str) or not value:
        raise CompileError("project-control-root-missing", "Project Settings requires paths.control_root")
    control = Path(value)
    if control.is_absolute() or ".." in control.parts or control == Path(".") or not (root / control).resolve().is_relative_to(root.resolve()):
        raise CompileError("project-control-root-invalid", "paths.control_root must be a safe repository-relative path", value=value)
    return control


def methodology_paths(root: Path) -> MethodologyPaths:
    """Resolve source and delivery places from the configured Project Structure.

    Applicable Methodology is the Projection-location exception: its default
    lives in the Project's Framework folder, not the general ``_projection``
    directory.  An explicit source-unit delivery binding remains authoritative.
    """
    control = configured_control_root(root)
    output = control / FRAMEWORK_APPLICABLE_RELATIVE
    structure = root / control / "project_structure.toml"
    if not structure.exists():
        return MethodologyPaths(source=output / "000_APPLICABLE_MTHD_sources", output=output, control_root=control)
    try:
        raw = structure.read_bytes()
        data = tomllib.loads(raw.decode("utf-8"))
        declared = data.get("scope_units", [])
        if not isinstance(declared, list) or any(not isinstance(unit, dict) for unit in declared):
            raise ValueError("scope_units must be an array of tables")
        units = [unit for unit in declared
                 if unit.get("scope_unit_name") == "METHODOLOGY_SOURCES"]
    except (OSError, ValueError, AttributeError) as error:
        raise CompileError("project-structure-invalid", "Cannot resolve methodology places from Project Structure") from error
    if len(units) != 1:
        raise CompileError("source-unit-cardinality", "Project Structure must declare exactly one METHODOLOGY_SOURCES unit")
    value = units[0].get("authority_path")
    if not isinstance(value, str) or not value:
        raise CompileError("source-unit-place-missing", "Methodology source unit has no declared authority place", property="authority_path")
    source = Path(value)
    if source.is_absolute() or ".." in source.parts or source == Path("."):
        raise CompileError("source-unit-place-invalid", "Methodology source place must be repository-relative", property="authority_path")
    output_value = units[0].get("delivery_path", output.as_posix())
    if not isinstance(output_value, str) or not output_value:
        raise CompileError("output-unit-place-invalid", "Methodology delivery place must be a non-empty repository-relative path", property="delivery_path")
    output = Path(output_value)
    if output.is_absolute() or ".." in output.parts or output == Path("."):
        raise CompileError("output-unit-place-invalid", "Methodology delivery place must be repository-relative", property="delivery_path")
    source_place = (root / source).resolve()
    output_place = (root / output).resolve()
    if not source_place.is_relative_to(root.resolve()):
        raise CompileError("source-unit-place-invalid", "Methodology source place resolves outside the Project", property="authority_path")
    if not output_place.is_relative_to(root.resolve()):
        raise CompileError("output-unit-place-invalid", "Methodology delivery place resolves outside the Project", property="delivery_path")
    if output_place.is_relative_to(source_place) or any(
        source_place.is_relative_to((output_place / role_directory).resolve())
        for _, role_directory in ROLES
    ):
        raise CompileError("source-output-overlap", "Generated output cannot replace the authoritative source place")
    return MethodologyPaths(source, output, sha256_bytes(raw), control)


class CompileError(Exception):
    """A stable compilation validation failure."""

    def __init__(self, code: str, message: str, **details: object) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details

    def record(self) -> dict[str, object]:
        result: dict[str, object] = {"code": self.code, "message": self.message}
        if self.details:
            result["details"] = self.details
        return result


@dataclass(frozen=True)
class Candidate:
    layer: str
    layer_order: int
    role: str
    role_directory: str
    atom_id: str
    version: int
    source_path: str
    source_sha256: str
    basename: str
    priority: str | None
    priority_group: str | None
    replacements: tuple[str, ...]
    incompatibilities: tuple[str, ...]
    definition_term: str | None
    definition_subject_path: str | None
    output_relative: str = OUTPUT_RELATIVE.as_posix()
    extension_id: str | None = None
    extension_revision: str | None = None
    original_relations_sha256: str = ""

    def frontier_record(self) -> dict[str, object]:
        return {
            "source_layer": self.layer,
            "atom_id": self.atom_id,
            "source_atom_id": self.atom_id,
            "atom_revision": self.version,
            "source_atom_revision": self.version,
            "source_carrier_path": self.source_path,
            "source_carrier_sha256": self.source_sha256,
            "original_relations_sha256": self.original_relations_sha256,
            **({"extension_id": self.extension_id, "extension_revision": self.extension_revision}
               if self.extension_id is not None else {}),
        }

    def report_record(self) -> dict[str, object]:
        record = {
            **self.frontier_record(),
            "content_role": self.role,
            "output_path": f"{self.output_relative}/{self.role_directory}/{self.basename}",
        }
        if self.definition_term is not None:
            record["definition_term"] = self.definition_term
            record["definition_subject_path"] = self.definition_subject_path
        return record


@dataclass(frozen=True)
class Approval:
    conflict_id: str
    source_frontier_digest: str
    selected_source_carrier_path: str
    operator: str
    carrier_path: str


def relations_digest(frontmatter: str) -> str:
    """Digest authored Relations without normalizing or rewriting them."""
    return sha256_bytes("\n".join(top_block(frontmatter, "relations")).encode("utf-8"))


def parse_toml(path: Path, code: str) -> dict[str, object]:
    try:
        value = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise CompileError(code, "Framework Settings must be valid UTF-8 TOML", path=path.as_posix()) from error
    if not isinstance(value, dict):
        raise CompileError(code, "Framework Settings must decode to a table", path=path.as_posix())
    return value


def framework_settings(root: Path, places: MethodologyPaths) -> tuple[dict[str, object], dict[str, str]]:
    """Read only governed settings Carriers, retaining their byte bindings."""
    merged: dict[str, object] = {}
    bindings: dict[str, str] = {}
    for relative in SETTINGS_FILENAMES:
        path = root / places.source / relative
        if not path.exists():
            continue
        if not path.is_file() or path.is_symlink():
            raise CompileError("framework-settings-invalid", "Framework Settings Carrier must be a regular file", path=repo_relative(root, path))
        raw = path.read_bytes()
        parsed = parse_toml(path, "framework-settings-invalid")
        merged.update(parsed)
        bindings[repo_relative(root, path)] = sha256_bytes(raw)
    return merged, bindings


def extension_selections(settings: Mapping[str, object]) -> dict[str, str]:
    """Return explicit enabled Extension identity/revision selections.

    The source authority only fixes the semantics (enabled plus revision).  The
    small reader accepts the two TOML table forms needed by instance settings;
    it never infers activation from installation or retained configuration.
    """
    selections: dict[str, str] = {}
    raw_sections = [settings.get(name) for name in ("extensions", "installed_extensions", "extension_selections")]
    for section in raw_sections:
        records: list[tuple[str | None, Mapping[str, object]]] = []
        if isinstance(section, Mapping):
            for identity, value in section.items():
                if isinstance(value, Mapping):
                    records.append((str(identity), value))
        elif isinstance(section, list):
            for value in section:
                if isinstance(value, Mapping):
                    identity = value.get("id", value.get("extension_id", value.get("name")))
                    records.append((identity if isinstance(identity, str) else None, value))
        for fallback_identity, record in records:
            enabled = record.get("enabled", record.get("active"))
            identity = record.get("id", record.get("extension_id", fallback_identity))
            revision = record.get("revision", record.get("selected_revision"))
            if enabled is not True:
                continue
            if not isinstance(identity, str) or not identity or not isinstance(revision, (str, int)) or not str(revision):
                raise CompileError("extension-selection-invalid", "Enabled Extension requires an identity and selected revision")
            rendered_revision = str(revision)
            if identity in selections and selections[identity] != rendered_revision:
                raise CompileError("extension-selection-ambiguous", "Extension has more than one active selected revision", extension_id=identity)
            selections[identity] = rendered_revision
    return dict(sorted(selections.items()))


def source_state_snapshot(root: Path, places: MethodologyPaths | None = None) -> dict[str, str]:
    """Capture every governed source/settings byte so new input also invalidates staging."""
    places = places or methodology_paths(root)
    source_root = root / places.source
    if not source_root.is_dir():
        raise CompileError("source-root-missing", "Applicable Methodology source root is missing", path=places.source.as_posix())
    snapshot: dict[str, str] = {}
    for path in sorted(source_root.rglob("*")):
        if path.is_file() and not path.is_symlink():
            snapshot[repo_relative(root, path)] = sha256_bytes(path.read_bytes())
    structure = root / places.control_root / "project_structure.toml"
    if structure.is_file() and not structure.is_symlink():
        snapshot[repo_relative(root, structure)] = sha256_bytes(structure.read_bytes())
    project_settings = root / SETTINGS_PATH
    if project_settings.is_file() and not project_settings.is_symlink():
        snapshot[SETTINGS_PATH.as_posix()] = sha256_bytes(project_settings.read_bytes())
    return snapshot


def source_snapshot_is_current(root: Path, snapshot: dict[str, str], places: MethodologyPaths | None = None) -> bool:
    try:
        return source_state_snapshot(root, places) == snapshot
    except CompileError:
        return False


def governed_bindings(root: Path, places: MethodologyPaths | None = None) -> dict[str, str]:
    places = places or methodology_paths(root)
    structure = root / places.control_root / "project_structure.toml"
    if not structure.is_file() or structure.is_symlink():
        raise CompileError("project-structure-missing", "Project Structure is required for governed bindings", path=repo_relative(root, structure))
    _, settings = framework_settings(root, places)
    configuration_root = root / places.source / "003_PROJECT_CONFIGURATION"
    configuration_records = {
        repo_relative(root, path): sha256_bytes(path.read_bytes())
        for path in sorted(configuration_root.rglob("*"))
        if path.is_file() and not path.is_symlink()
    }
    return {
        "project_structure_sha256": sha256_bytes(structure.read_bytes()),
        "framework_settings_sha256": sha256_bytes(canonical_json(settings)),
        "project_configuration_sha256": sha256_bytes(canonical_json(configuration_records)),
        "projection_target": places.output.as_posix(),
    }


def canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def scalar_value(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value


def split_frontmatter(data: bytes, path: str) -> tuple[str, bytes]:
    if not data.startswith(b"---\n"):
        raise CompileError("source-frontmatter-missing", "Source Carrier requires YAML frontmatter", path=path)
    boundary = data.find(b"\n---\n", 4)
    if boundary < 0:
        raise CompileError("source-frontmatter-unterminated", "Source Carrier frontmatter is unterminated", path=path)
    try:
        frontmatter = data[4:boundary].decode("utf-8")
        data.decode("utf-8")
    except UnicodeDecodeError as error:
        raise CompileError("source-not-utf8", "Source Carrier must be UTF-8", path=path) from error
    return frontmatter, data[boundary + 5 :]


def top_scalar(frontmatter: str, key: str) -> str | None:
    matches = re.findall(rf"(?m)^{re.escape(key)}:\s*([^\n]+?)\s*$", frontmatter)
    if len(matches) > 1:
        raise CompileError("source-frontmatter-duplicate-key", "Source Carrier has duplicate scalar", key=key)
    if not matches:
        return None
    return scalar_value(matches[0])


def top_block(frontmatter: str, key: str) -> list[str]:
    lines = frontmatter.splitlines()
    start = next((index for index, line in enumerate(lines) if re.fullmatch(rf"{re.escape(key)}:\s*", line)), None)
    if start is None:
        return []
    block: list[str] = []
    for line in lines[start + 1 :]:
        if line and not line[0].isspace():
            break
        block.append(line)
    return block


def relation_targets(frontmatter: str, kinds: set[str]) -> tuple[str, ...]:
    block = top_block(frontmatter, "relations")
    if not block:
        return ()
    found: set[str] = set()
    current_mapping_kind: str | None = None
    current_list_kind: str | None = None
    collecting_list_targets = False
    for line in block:
        mapping = re.fullmatch(r"  ([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)", line)
        if mapping:
            key, raw = mapping.groups()
            current_mapping_kind = key if key in kinds else None
            current_list_kind = None
            collecting_list_targets = False
            if current_mapping_kind and raw and raw != "[]":
                found.add(scalar_value(raw))
            continue
        list_type = re.fullmatch(r"  -\s*type:\s*(.+?)\s*", line)
        if list_type:
            kind = scalar_value(list_type.group(1))
            current_list_kind = kind if kind in kinds else None
            current_mapping_kind = None
            collecting_list_targets = False
            continue
        list_target_key = re.fullmatch(r"    (?:target|targets):\s*(.*?)\s*", line)
        if list_target_key and current_list_kind:
            raw = list_target_key.group(1)
            collecting_list_targets = not raw
            if raw and raw != "[]":
                found.add(scalar_value(raw))
            continue
        mapping_item = re.fullmatch(r"    -\s*(.+?)\s*", line)
        if mapping_item and current_mapping_kind:
            found.add(scalar_value(mapping_item.group(1)))
            continue
        list_item = re.fullmatch(r"      -\s*(.+?)\s*", line)
        if list_item and current_list_kind and collecting_list_targets:
            found.add(scalar_value(list_item.group(1)))
    return tuple(sorted(value for value in found if value))


def derive_atom_id(path: Path, frontmatter: str) -> str:
    explicit = top_scalar(frontmatter, "atom_id")
    identity = atom_identifier(path.name, explicit)
    if not identity:
        raise CompileError("source-atom-identity-missing", "Cannot derive Source Atom identity", path=path.as_posix())
    return identity


def terminal_term(subject_path: str) -> str:
    parts = re.split(r"\s*[/:]\s*", subject_path.strip())
    if not parts or any(not part for part in parts):
        raise CompileError("source-subject-path-invalid", "Definition Subject Path is invalid", subject_path=subject_path)
    return parts[-1]


def definition_subject(frontmatter: str, path: str) -> tuple[str | None, str | None]:
    if (top_scalar(frontmatter, "cce_form") or "").lower() != "definition":
        return None, None
    block = top_block(frontmatter, "subjects")
    current_kind: str | None = None
    governed: list[str] = []
    for line in block:
        kind = re.fullmatch(r"  ([a-z_]+):\s*(.*?)\s*", line)
        if kind:
            current_kind = kind.group(1)
            raw = kind.group(2)
            if raw and current_kind in {"governs", "declared"}:
                governed.append(scalar_value(raw))
            continue
        item = re.fullmatch(r"(?:    |      )-\s*(.+?)\s*", line)
        if item and current_kind in {"governs", "declared"}:
            governed.append(scalar_value(item.group(1)))
    if len(governed) != 1:
        raise CompileError(
            "definition-term-cardinality",
            "A Definition Atom must identify exactly one Term through GOVERNS",
            path=path,
            governs_count=len(governed),
        )
    return terminal_term(governed[0]), governed[0]


def candidate_sort_key(candidate: Candidate) -> tuple[object, ...]:
    return (candidate.layer_order, candidate.atom_id, candidate.version, candidate.source_path)


def selected_sort_key(candidate: Candidate) -> tuple[object, ...]:
    return (ROLE_ORDER[candidate.role_directory], candidate.atom_id, candidate.source_path)


def proposal_sort_key(candidate: Candidate) -> tuple[object, ...]:
    priority_rank = priority_value(candidate.priority)
    return (-candidate.version, -priority_rank, candidate.layer_order, candidate.source_path)


def priority_value(value: str | None) -> int:
    if value is None:
        return 0
    labels = {"low": 10, "medium": 20, "high": 30, "critical": 40}
    if value.lower() in labels:
        return labels[value.lower()]
    try:
        return int(value)
    except ValueError:
        return 0


def repo_relative(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise CompileError("path-outside-project", "Carrier is outside the Project root", path=path.as_posix()) from error


def discover_candidates(root: Path, places: MethodologyPaths | None = None) -> tuple[list[Candidate], list[dict[str, object]], dict[str, str]]:
    """Read the complete governed frontier without deriving activation from files."""
    places = places or methodology_paths(root)
    source_root = root / places.source
    diagnostics: list[dict[str, object]] = []
    if not source_root.is_dir():
        raise CompileError("source-root-missing", "Applicable Methodology source root is missing", path=places.source.as_posix())
    root_role_directories = {directory for _, directory in ROLES}
    observed_layers = sorted(path.name for path in source_root.iterdir() if path.is_dir() and path.name not in root_role_directories)
    expected_layers = [directory for _, directory, _, _ in LAYERS]
    if observed_layers != expected_layers:
        raise CompileError("source-layer-topology-mismatch", "Structural Source Layers differ from the governed topology", expected=expected_layers, observed=observed_layers)

    settings, _ = framework_settings(root, places)
    selected_extensions = extension_selections(settings)
    candidates: list[Candidate] = []
    snapshot = source_state_snapshot(root, places)

    def exclude(path: Path, reason: str, **details: object) -> None:
        diagnostics.append({"code": "source-excluded", "source_carrier_path": repo_relative(root, path), "reason": reason, **details})

    def collect(layer: str, order: int, role_root: Path, extension_id: str | None = None, extension_revision: str | None = None) -> None:
        if not role_root.exists():
            return
        if not role_root.is_dir() or role_root.is_symlink():
            raise CompileError("source-role-not-directory", "Source role Carrier must be a directory", path=repo_relative(root, role_root))
        for path in sorted(role_root.rglob("*.md")):
            relative_within_role = path.relative_to(role_root)
            relative = repo_relative(root, path)
            if {"archive", "drafts", "done", "canceled"}.intersection(relative_within_role.parts):
                exclude(path, "inactive-location")
                continue
            if not path.is_file() or path.is_symlink():
                exclude(path, "not-regular")
                continue
            try:
                data = path.read_bytes()
                frontmatter, _ = split_frontmatter(data, relative)
                if re.search(r"(?m)^projection:\s*(?:$|\{)", frontmatter):
                    raise CompileError("source-projection-metadata-present", "Authoritative Source Carrier cannot contain projection metadata", path=relative)
                status = top_scalar(frontmatter, "status")
                if status != "Active":
                    exclude(path, "inactive" if status else "status-missing", status=status)
                    continue
                version_raw = top_scalar(frontmatter, "version")
                if version_raw is None or not re.fullmatch(r"[1-9][0-9]*", version_raw):
                    raise CompileError("source-version-invalid", "Selected Source Atom revision requires a positive integer version", path=relative)
                defined_term, definition_subject_path = definition_subject(frontmatter, relative)
                candidates.append(Candidate(
                    layer=layer, layer_order=order, role=ROLE_BY_DIRECTORY[role_root.name], role_directory=role_root.name,
                    atom_id=derive_atom_id(path, frontmatter), version=int(version_raw), source_path=relative,
                    source_sha256=sha256_bytes(data), basename=path.name, priority=top_scalar(frontmatter, "priority"),
                    priority_group=top_scalar(frontmatter, "applicable_methodology_priority_group"),
                    replacements=relation_targets(frontmatter, RELATION_KINDS["replacement"]),
                    incompatibilities=relation_targets(frontmatter, RELATION_KINDS["incompatible"]),
                    definition_term=defined_term, definition_subject_path=definition_subject_path,
                    output_relative=places.output.as_posix(), extension_id=extension_id, extension_revision=extension_revision,
                    original_relations_sha256=relations_digest(frontmatter),
                ))
            except CompileError as error:
                diagnostics.append({**error.record(), "path": relative})

    for layer, directory, order, _ in (LAYERS[0], LAYERS[2]):
        for _, role_directory in ROLES:
            collect(layer, order, source_root / directory / role_directory)

    installed = source_root / "002_INSTALLED_EXTENSIONS"
    observed_revisions: set[tuple[str, str]] = set()
    for extension_root in sorted(path for path in installed.iterdir() if path.is_dir() and not path.is_symlink()):
        extension_id = extension_root.name
        for revision_root in sorted(path for path in extension_root.iterdir() if path.is_dir() and not path.is_symlink()):
            revision = revision_root.name
            observed_revisions.add((extension_id, revision))
            selected_revision = selected_extensions.get(extension_id)
            for _, role_directory in ROLES:
                role_root = revision_root / role_directory
                if selected_revision != revision:
                    for path in sorted(role_root.rglob("*.md")) if role_root.is_dir() else []:
                        exclude(path, "extension-revision-unselected", extension_id=extension_id, extension_revision=revision)
                    continue
                collect("INSTALLED_EXTENSIONS", 1, role_root, extension_id, revision)
    for extension_id, revision in selected_extensions.items():
        if (extension_id, revision) not in observed_revisions:
            diagnostics.append({"code": "activated-extension-revision-missing", "extension_id": extension_id, "extension_revision": revision})
        elif not any(candidate.extension_id == extension_id and candidate.extension_revision == revision for candidate in candidates):
            diagnostics.append({"code": "activated-extension-has-no-current-carriers", "extension_id": extension_id, "extension_revision": revision})

    candidates.sort(key=candidate_sort_key)
    if not candidates:
        diagnostics.append({"code": "empty-source-frontier", "message": "No eligible current active RMEDO Source Atom revisions were found"})
    return candidates, diagnostics, snapshot


def frontier_digest(candidates: Iterable[Candidate]) -> str:
    records = [candidate.frontier_record() for candidate in sorted(candidates, key=candidate_sort_key)]
    return sha256_bytes(canonical_json(records))


def conflict_record(kind: str, candidates: Iterable[Candidate], proposal: Candidate, **details: object) -> dict[str, object]:
    ordered = sorted(set(candidates), key=candidate_sort_key)
    identity = {
        "type": kind,
        "candidate_source_carrier_paths": [candidate.source_path for candidate in ordered],
        "details": details,
    }
    return {
        "conflict_id": sha256_bytes(canonical_json(identity)),
        "type": kind,
        "candidate_source_carrier_paths": identity["candidate_source_carrier_paths"],
        "details": details,
        "proposed_resolution": {"selected_source_carrier_path": proposal.source_path},
    }


def candidate_aliases(candidate: Candidate) -> set[str]:
    stem = Path(candidate.basename).stem
    return {candidate.atom_id, stem, stem.split("--", 1)[0]}


def detect_conflicts(candidates: list[Candidate]) -> list[dict[str, object]]:
    conflicts: list[dict[str, object]] = []
    by_identity: dict[str, list[Candidate]] = {}
    alias_index: dict[str, list[Candidate]] = {}
    by_output: dict[tuple[str, str], list[Candidate]] = {}
    by_priority_group: dict[str, list[Candidate]] = {}
    by_definition_term: dict[str, list[Candidate]] = {}
    for candidate in candidates:
        by_identity.setdefault(candidate.atom_id, []).append(candidate)
        by_output.setdefault((candidate.role_directory, candidate.basename), []).append(candidate)
        if candidate.priority_group:
            by_priority_group.setdefault(candidate.priority_group, []).append(candidate)
        if candidate.definition_term:
            by_definition_term.setdefault(candidate.definition_term, []).append(candidate)
        for alias in candidate_aliases(candidate):
            alias_index.setdefault(alias, []).append(candidate)

    replacement_pairs: set[tuple[str, str]] = set()
    incompatibility_pairs: set[tuple[str, str]] = set()
    for candidate in candidates:
        for target in candidate.replacements:
            for replaced in alias_index.get(target, []):
                if replaced.source_path != candidate.source_path:
                    replacement_pairs.add((candidate.source_path, replaced.source_path))
        for target in candidate.incompatibilities:
            for incompatible in alias_index.get(target, []):
                if incompatible.source_path != candidate.source_path:
                    incompatibility_pairs.add(tuple(sorted((candidate.source_path, incompatible.source_path))))

    lookup = {candidate.source_path: candidate for candidate in candidates}
    involved_pairs = {frozenset(pair) for pair in replacement_pairs}.union(frozenset(pair) for pair in incompatibility_pairs)
    involved_priority = {candidate.source_path for group in by_priority_group.values() if len(group) > 1 for candidate in group}

    for atom_id, group in sorted(by_identity.items()):
        if len(group) <= 1:
            continue
        group_paths = {candidate.source_path for candidate in group}
        if any(pair.issubset(group_paths) for pair in involved_pairs) or group_paths.intersection(involved_priority):
            continue
        proposal = sorted(group, key=proposal_sort_key)[0]
        conflicts.append(conflict_record("duplicate_selected_atom_identity", group, proposal, atom_id=atom_id))

    for term, group in sorted(by_definition_term.items()):
        if len(group) <= 1:
            continue
        group_paths = {candidate.source_path for candidate in group}
        if any(pair.issubset(group_paths) for pair in involved_pairs) or group_paths.intersection(involved_priority):
            continue
        proposal = sorted(group, key=proposal_sort_key)[0]
        conflicts.append(
            conflict_record(
                "duplicate_governed_term_definition",
                group,
                proposal,
                term=term,
                definition_subject_paths={
                    candidate.source_path: candidate.definition_subject_path
                    for candidate in sorted(group, key=candidate_sort_key)
                },
            )
        )

    for replacer_path, replaced_path in sorted(replacement_pairs):
        replacer = lookup[replacer_path]
        replaced = lookup[replaced_path]
        conflicts.append(
            conflict_record(
                "unresolved_replacement",
                (replacer, replaced),
                replacer,
                replacer_source_carrier_path=replacer_path,
                replaced_source_carrier_path=replaced_path,
            )
        )

    for first_path, second_path in sorted(incompatibility_pairs):
        group = (lookup[first_path], lookup[second_path])
        proposal = sorted(group, key=proposal_sort_key)[0]
        conflicts.append(conflict_record("incompatible_retained_candidates", group, proposal))

    for group_name, group in sorted(by_priority_group.items()):
        if len(group) <= 1:
            continue
        proposal = sorted(group, key=proposal_sort_key)[0]
        conflicts.append(
            conflict_record(
                "unresolved_priority",
                group,
                proposal,
                priority_group=group_name,
                observed_priorities={candidate.source_path: candidate.priority for candidate in sorted(group, key=candidate_sort_key)},
            )
        )

    for (role_directory, basename), group in sorted(by_output.items()):
        if len(group) <= 1:
            continue
        proposal = sorted(group, key=proposal_sort_key)[0]
        conflicts.append(
            conflict_record(
                "output_path_collision",
                group,
                proposal,
                output_path=f"{group[0].output_relative}/{role_directory}/{basename}",
            )
        )

    conflicts.sort(key=lambda item: (str(item["type"]), str(item["conflict_id"])))
    return conflicts


def discover_approvals(root: Path, candidates: list[Candidate], places: MethodologyPaths | None = None) -> list[Approval]:
    del candidates
    approval_relative = (places or methodology_paths(root)).approvals.as_posix()
    path = root / approval_relative
    if not path.exists():
        return []
    if not path.is_file() or path.is_symlink():
        raise CompileError("approval-carrier-invalid", "Project Configuration approval Carrier must be a regular TOML file", path=approval_relative)
    try:
        document = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise CompileError("approval-carrier-invalid", "Project Configuration approval Carrier is not valid UTF-8 TOML", path=approval_relative) from error
    if document.get("schema") != "caprmedio.applicable_methodology_conflict_approvals.v1":
        raise CompileError("approval-schema-invalid", "Project Configuration approval Carrier schema is invalid", path=approval_relative)
    records = document.get("approvals", [])
    if not isinstance(records, list) or any(not isinstance(record, dict) for record in records):
        raise CompileError("approval-record-invalid", "Project Configuration approvals must be an array of tables", path=approval_relative)
    required = {"conflict_id", "source_frontier_digest", "selected_source_carrier_path", "operator"}
    approvals: list[Approval] = []
    for record in records:
        missing = sorted(required.difference(record))
        if missing:
            raise CompileError(
                "approval-record-incomplete",
                "Project Configuration approval record is incomplete",
                carrier_path=approval_relative,
                missing=missing,
            )
        if any(not isinstance(record[key], str) for key in required):
            raise CompileError(
                "approval-record-invalid",
                "Project Configuration approval fields must be strings",
                carrier_path=approval_relative,
            )
        approvals.append(
            Approval(
                conflict_id=record["conflict_id"],
                source_frontier_digest=record["source_frontier_digest"],
                selected_source_carrier_path=record["selected_source_carrier_path"],
                operator=record["operator"],
                carrier_path=approval_relative,
            )
        )
    return approvals


def resolve_conflicts(
    candidates: list[Candidate], conflicts: list[dict[str, object]], approvals: list[Approval], digest: str
) -> tuple[list[Candidate], list[dict[str, object]], list[dict[str, object]]]:
    approval_results: list[dict[str, object]] = []
    selected_paths = {candidate.source_path for candidate in candidates}
    rejected_paths: set[str] = set()
    unresolved: list[dict[str, object]] = []
    for conflict in conflicts:
        conflict_id = str(conflict["conflict_id"])
        candidate_paths = set(str(path) for path in conflict["candidate_source_carrier_paths"])
        matches = [approval for approval in approvals if approval.conflict_id == conflict_id]
        status = "missing"
        selected: str | None = None
        carrier: str | None = None
        if len(matches) > 1:
            status = "ambiguous"
        elif len(matches) == 1:
            approval = matches[0]
            carrier = approval.carrier_path
            selected = approval.selected_source_carrier_path
            if not approval.operator:
                status = "operator_missing"
            elif approval.source_frontier_digest != digest:
                status = "stale_source_frontier_digest"
            elif selected not in candidate_paths:
                status = "selected_candidate_mismatch"
            else:
                status = "approved"
                rejected = candidate_paths.difference({selected})
                if selected in rejected_paths or selected not in selected_paths:
                    status = "approval_resolution_conflict"
                else:
                    rejected_paths.update(rejected)
                    selected_paths.difference_update(rejected)
        approval_results.append(
            {
                "conflict_id": conflict_id,
                "status": status,
                "approval_carrier_path": carrier,
                "selected_source_carrier_path": selected,
            }
        )
        if status != "approved":
            unresolved.append(conflict)
    selected_candidates = [candidate for candidate in candidates if candidate.source_path in selected_paths]
    selected_candidates.sort(key=selected_sort_key)
    return selected_candidates, approval_results, unresolved


def output_plan(candidates: list[Candidate]) -> list[dict[str, object]]:
    return [candidate.report_record() for candidate in sorted(candidates, key=selected_sort_key)]


def projection_bytes(source: bytes, source_relative_from_output: str, candidate: Candidate) -> bytes:
    path = candidate.source_path
    frontmatter, _ = split_frontmatter(source, path)
    if re.search(r"(?m)^projection:\s*(?:$|\{)", frontmatter):
        raise CompileError("source-projection-metadata-present", "Authoritative Source Carrier cannot contain projection metadata", path=path)
    boundary = source.find(b"\n---\n", 4)
    addition = (
        "\nprojection:\n"
        f"  source_carrier_path: {source_relative_from_output}\n"
        f"  source_atom_id: {candidate.atom_id}\n"
        f"  source_atom_revision: {candidate.version}\n"
        f"  source_sha256: {candidate.source_sha256}\n"
        f"  original_relations_sha256: {candidate.original_relations_sha256}"
    ).encode("utf-8")
    return source[:boundary] + addition + source[boundary:]


def validate_existing_output_ownership(output_root: Path) -> None:
    for _, role_directory in ROLES:
        target = output_root / role_directory
        if not target.exists():
            continue
        if not target.is_dir() or target.is_symlink():
            raise CompileError("output-role-not-owned", "Generated output role path is not a replaceable directory", path=target.as_posix())
        for path in target.rglob("*"):
            if path.is_dir() and not path.is_symlink():
                continue
            if not path.is_file() or path.is_symlink() or path.suffix != ".md":
                raise CompileError("output-role-not-owned", "Generated output contains a non-projected Carrier", path=path.as_posix())
            frontmatter, _ = split_frontmatter(path.read_bytes(), path.as_posix())
            if not re.search(r"(?m)^projection:\s*$", frontmatter):
                raise CompileError("output-role-not-owned", "Generated output Carrier lacks projection ownership metadata", path=path.as_posix())


def stage_outputs(root: Path, candidates: list[Candidate], source_snapshot: dict[str, str], places: MethodologyPaths | None = None) -> Path:
    output_root = root / (places or methodology_paths(root)).output
    temporary_staging = root / ".caprmedio_runtime/compile_applicable_methodology"
    temporary_staging.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix="transaction-", dir=temporary_staging))
    new_root = staging / "new"
    for _, role_directory in ROLES:
        (new_root / role_directory).mkdir(parents=True)
    try:
        for candidate in candidates:
            source_path = root / candidate.source_path
            target_parent = output_root / candidate.role_directory
            relative_source = Path(os.path.relpath(source_path, start=target_parent)).as_posix()
            projected = projection_bytes(source_path.read_bytes(), relative_source, candidate)
            target = new_root / candidate.role_directory / candidate.basename
            target.write_bytes(projected)
        _, current_diagnostics, current_snapshot = discover_candidates(root, places)
        if any(item.get("code") not in {"source-excluded"} for item in current_diagnostics) or current_snapshot != source_snapshot:
            raise CompileError("source-frontier-changed", "Source frontier changed while outputs were staged")
        return staging
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise


def replace_outputs_atomically(root: Path, staging: Path, places: MethodologyPaths | None = None) -> None:
    output_root = root / (places or methodology_paths(root)).output
    new_root = staging / "new"
    output_root.mkdir(parents=True, exist_ok=True)
    existing: dict[Path, bytes] = {}
    expected: set[Path] = set()
    for _, role_directory in ROLES:
        target_directory = output_root / role_directory
        target_directory.mkdir(parents=True, exist_ok=True)
        existing.update({path: path.read_bytes() for path in target_directory.rglob("*.md") if path.is_file()})
        expected.update(target_directory / path.name for path in (new_root / role_directory).iterdir() if path.is_file())
    installed: list[Path] = []
    try:
        for _, role_directory in ROLES:
            target_directory = output_root / role_directory
            for replacement in sorted((new_root / role_directory).iterdir()):
                target = target_directory / replacement.name
                os.replace(replacement, target)
                installed.append(target)
        for stale in sorted(set(existing).difference(expected)):
            stale.unlink()
    except Exception as error:
        rollback_failed = False
        for target in reversed(installed):
            if target.exists() and target not in existing:
                try:
                    target.unlink()
                except OSError:
                    rollback_failed = True
        for target, data in existing.items():
            temporary = target.with_name(f".{target.name}.rollback.tmp")
            try:
                temporary.write_bytes(data)
                os.replace(temporary, target)
            except OSError:
                rollback_failed = True
                temporary.unlink(missing_ok=True)
        for target in set(expected).difference(existing):
            if target.exists():
                try:
                    target.unlink()
                except OSError:
                    rollback_failed = True
        raise CompileError(
            "atomic-replacement-uncertain" if rollback_failed else "atomic-replacement-failed",
            "Generated RMEDO output replacement has an uncertain recovery state" if rollback_failed else "Generated RMEDO output replacement rolled back",
            error=type(error).__name__,
        ) from error
    finally:
        shutil.rmtree(staging, ignore_errors=True)


def generated_tree_digest(root: Path, places: MethodologyPaths | None = None) -> str:
    output_root = root / (places or methodology_paths(root)).output
    records: list[dict[str, str]] = []
    for _, role_directory in ROLES:
        role_root = output_root / role_directory
        if not role_root.is_dir():
            raise CompileError("generated-role-missing", "Generated RMEDO role directory is missing", role_directory=role_directory)
        for path in sorted(role_root.rglob("*")):
            if path.is_file():
                records.append(
                    {
                        "path": repo_relative(root, path),
                        "sha256": sha256_bytes(path.read_bytes()),
                    }
                )
    return sha256_bytes(canonical_json(records))


def compile_report(root: Path, places: MethodologyPaths | None = None) -> tuple[dict[str, object], list[Candidate], dict[str, str]]:
    places = places or methodology_paths(root)
    candidates, diagnostics, source_snapshot = discover_candidates(root, places)
    digest = frontier_digest(candidates)
    conflicts = detect_conflicts(candidates)
    # A Project Configuration TOML carrier is only a non-authoritative index.
    # The public request path resolves decisions against canonical Journal
    # references below; this compatibility report intentionally leaves every
    # conflict unresolved.
    selected, approval_results, unresolved = resolve_conflicts(candidates, conflicts, [], digest)
    report: dict[str, object] = {
        "schema": SCHEMA,
        "authority": "non_authoritative_dry_run",
        "structural_source_layers": [name for name, _, _, _ in LAYERS],
        "contributing_source_layers": ["CORE_META_MODEL", "INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION"],
        "source_frontier_digest": digest,
        "eligible_candidate_count": len(candidates),
        "conflict_count": len(conflicts),
        "unresolved_conflict_count": len(unresolved),
        "conflicts": conflicts,
        "approval_results": approval_results,
        "diagnostics": diagnostics,
        "excluded_candidates": [item for item in diagnostics if item.get("code") == "source-excluded"],
        "selected_candidate_count": len(selected),
        "output_plan": output_plan(selected),
        "persistent_subject_indexes": False,
        "can_apply": not any(
            item.get("code") not in {"source-excluded"} for item in diagnostics
        ) and not unresolved,
    }
    return report, selected, source_snapshot


def find_project_root(start: Path) -> Path:
    resolved = start.resolve()
    for candidate in (resolved, *resolved.parents):
        if (candidate / methodology_paths(candidate).source).is_dir():
            return candidate
    raise CompileError("project-root-not-found", "Cannot find CAPRMEDIO Project root", start=resolved.as_posix())


def request_error(code: str, message: str, **details: object) -> CompileError:
    return CompileError(code, message, **details)


def validate_request(request: Mapping[str, object]) -> tuple[Path, MethodologyPaths, str]:
    fields = set(request)
    prohibited = sorted(fields.intersection(FORBIDDEN_REQUEST_FIELDS))
    if prohibited:
        raise request_error("request-field-forbidden", "Request contains a caller-controlled authority field", fields=prohibited)
    unknown = sorted(fields.difference(REQUEST_FIELDS))
    if unknown:
        raise request_error("request-field-unknown", "Request contains an unknown field", fields=unknown)
    operation = request.get("operation")
    if operation not in OPERATIONS:
        raise request_error("request-operation-invalid", "Request operation must be exactly one supported operation")
    root_value = request.get("project_root")
    if not isinstance(root_value, str) or not root_value:
        raise request_error("request-project-root-invalid", "Request requires a Project root reference")
    root = Path(root_value).resolve()
    if not root.is_dir():
        raise request_error("request-project-root-invalid", "Request Project root is unavailable", project_root=root_value)
    places = methodology_paths(root)
    expected = request.get("governed_bindings")
    if not isinstance(expected, Mapping) or any(not isinstance(key, str) or not isinstance(value, str) for key, value in expected.items()):
        raise request_error("request-governed-bindings-invalid", "Request requires exact governed digest bindings")
    actual = governed_bindings(root, places)
    if dict(expected) != actual:
        raise request_error("request-governed-bindings-stale", "Request bindings do not match current governed inputs", expected=actual)
    if operation in {"apply", "recover_publication"}:
        expected_frontier = request.get("expected_source_frontier_digest")
        if not isinstance(expected_frontier, str) or not expected_frontier:
            raise request_error("request-frontier-binding-missing", "Publication requires an expected assessed frontier digest")
    if operation == "recover_publication":
        failed = request.get("failed_publication_ref")
        if not isinstance(failed, str) or not failed:
            raise request_error("request-recovery-evidence-missing", "Recovery requires an existing failed-publication reference")
    receipt_refs = request.get("run_receipt_refs", [])
    if not isinstance(receipt_refs, list) or any(not isinstance(reference, Mapping) for reference in receipt_refs):
        raise request_error("request-run-receipt-references-invalid", "Shared Run receipt references must be a list of reference objects")
    return root, places, str(operation)


def journal_record(root: Path, reference: str, digest: str | None, places: MethodologyPaths | None = None) -> dict[str, object]:
    """Resolve a canonical immutable Journal record by path#event-id reference."""
    path_text, marker, event_id = reference.partition("#")
    if not marker or not event_id:
        raise request_error("decision-journal-reference-invalid", "Decision requires path#event-id canonical Journal reference")
    path = Path(path_text)
    journal_root = root / (places or methodology_paths(root)).control_root / "_journal"
    if path.is_absolute() or ".." in path.parts:
        raise request_error("decision-journal-reference-invalid", "Journal reference must be repository-relative")
    absolute = root / path
    if not absolute.is_file() or absolute.is_symlink() or not absolute.resolve().is_relative_to(journal_root.resolve()):
        raise request_error("decision-journal-reference-invalid", "Journal reference is outside the configured canonical _journal", reference=reference)
    for line in absolute.read_text(encoding="utf-8").splitlines():
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(record, dict) and record.get("event_id") == event_id:
            if digest is not None and record.get("event_digest") != digest:
                raise request_error("decision-journal-digest-mismatch", "Canonical Journal record digest differs from decision reference", reference=reference)
            return record
    raise request_error("decision-journal-record-missing", "Canonical Journal record is not present", reference=reference)


def failed_publication_evidence(root: Path, reference: str, digest: str, places: MethodologyPaths) -> dict[str, object]:
    """Require an existing canonical failed-publication event before retrying.

    The compiler only reads the shared Journal reference.  It does not create a
    replacement event, receipt, or Run when an earlier publication failed.
    """
    record = journal_record(root, reference, None, places)
    details = record.get("details")
    if not isinstance(details, Mapping):
        raise request_error("recovery-journal-incomplete", "Failed-publication evidence lacks bound details", reference=reference)
    if details.get("source_frontier_digest") != digest:
        raise request_error("recovery-source-frontier-stale", "Failed-publication evidence names a different source frontier", reference=reference)
    event = record.get("event")
    outcome = record.get("outcome")
    if event not in {"failed", "interrupted"} and outcome not in {"failed", "partial", "uncertain", "interrupted_pending"}:
        raise request_error("recovery-publication-not-failed", "Recovery evidence is not a failed or uncertain publication", reference=reference)
    return {
        "failed_publication_ref": reference,
        "event_id": record.get("event_id"),
        "event_digest": record.get("event_digest"),
        "source_frontier_digest": digest,
    }


def journal_decisions(root: Path, decision_refs: object, conflicts: list[dict[str, object]], digest: str, places: MethodologyPaths | None = None) -> tuple[list[Approval], list[dict[str, object]]]:
    if decision_refs is None:
        return [], []
    if not isinstance(decision_refs, list):
        raise request_error("decision-reference-invalid", "Decision references must be a list")
    allowed = {"conflict_id", "journal_record_ref", "journal_record_digest"}
    approvals: list[Approval] = []
    evidence: list[dict[str, object]] = []
    conflict_ids = {str(item["conflict_id"]) for item in conflicts}
    for reference in decision_refs:
        if not isinstance(reference, Mapping) or set(reference).difference(allowed) or set(reference) != allowed:
            raise request_error("decision-reference-invalid", "Decision reference contains unsupported or missing fields")
        conflict_id = reference["conflict_id"]
        path = reference["journal_record_ref"]
        record_digest = reference["journal_record_digest"]
        if not all(isinstance(value, str) and value for value in (conflict_id, path, record_digest)):
            raise request_error("decision-reference-invalid", "Decision reference fields must be non-empty strings")
        if conflict_id not in conflict_ids:
            raise request_error("decision-conflict-mismatch", "Decision reference does not name an assessed conflict", conflict_id=conflict_id)
        record = journal_record(root, path, record_digest, places)
        details = record.get("details")
        if not isinstance(details, Mapping):
            raise request_error("decision-journal-incomplete", "Canonical Journal decision lacks bound details", reference=path)
        selected = details.get("selected_source_carrier_path")
        recorded_digest = details.get("source_frontier_digest")
        operator = record.get("operator", record.get("author"))
        if record.get("outcome") not in {"approved", "selected"}:
            raise request_error("decision-journal-not-approved", "Canonical Journal decision is not approved", reference=path)
        if recorded_digest != digest:
            raise request_error("decision-source-frontier-stale", "Canonical Journal decision names a stale source frontier", reference=path)
        if details.get("conflict_id") != conflict_id or not isinstance(selected, str) or not isinstance(operator, str) or not operator:
            raise request_error("decision-journal-incomplete", "Canonical Journal decision is not exactly bound to the assessed frontier", reference=path)
        approvals.append(Approval(conflict_id, digest, selected, operator, path))
        evidence.append({
            "conflict_id": conflict_id,
            "operator": operator,
            "selected_source_carrier_path": selected,
            "journal_record_ref": path,
            "journal_record_digest": record_digest,
            "source_frontier_digest": digest,
        })
    return approvals, evidence


def publication_state(root: Path, places: MethodologyPaths) -> str:
    return "preserved" if (root / places.output).exists() else "not_started"


def run_request(request: Mapping[str, object]) -> dict[str, object]:
    """Execute one compiler operation at the strict governed boundary.

    Caller input contains only references and expected digests.  It cannot
    provide source/output locations, source edits, selection results, or event
    payloads.  Shared run support supplies any receipt references unchanged.
    """
    prior = "not_started"
    try:
        root, places, operation = validate_request(request)
        prior = publication_state(root, places)
        report, candidates, snapshot = compile_report(root, places)
        digest = str(report["source_frontier_digest"])
        approvals, decision_evidence = journal_decisions(root, request.get("decision_refs"), list(report["conflicts"]), digest, places)
        recovery_evidence = (
            failed_publication_evidence(root, str(request["failed_publication_ref"]), digest, places)
            if operation == "recover_publication" else None
        )
        selected, decision_statuses, unresolved = resolve_conflicts(candidates, list(report["conflicts"]), approvals, digest)
        blocking = [item for item in report["diagnostics"] if item.get("code") != "source-excluded"]
        if unresolved:
            blocking.extend({"code": "conflict-unresolved", "conflict_id": item["conflict_id"]} for item in unresolved)
        result: dict[str, object] = {
            "schema": SCHEMA,
            "operation": operation,
            "source_frontier_digest": digest,
            "source_frontier": [candidate.frontier_record() for candidate in candidates],
            "excluded_candidates": report["excluded_candidates"],
            "conflicts": report["conflicts"],
            "proposals": [item["proposed_resolution"] for item in report["conflicts"]],
            "decision_provenance": decision_evidence,
            "decision_statuses": decision_statuses,
            "evidence_refs": {
                "governed_bindings": governed_bindings(root, places),
                **({"failed_publication": recovery_evidence} if recovery_evidence is not None else {}),
            },
            "run_receipt_refs": list(request.get("run_receipt_refs", [])),
            "publication": {"prior_output_state": prior},
            # Compatibility observables retained for callers of the original CLI.
            "authority": "non_authoritative_dry_run",
            "eligible_candidate_count": len(candidates),
            "conflict_count": len(report["conflicts"]),
            "unresolved_conflict_count": len(unresolved),
            "selected_candidate_count": len(selected),
            "output_plan": output_plan(selected),
            "diagnostics": report["diagnostics"],
            "can_apply": not blocking,
        }
        if operation == "dry_run":
            result["outcome"] = "assessed" if not blocking else "blocked"
            result["publishable"] = not blocking
            if blocking:
                result["blocking_findings"] = blocking
            return result
        if request["expected_source_frontier_digest"] != digest:
            result.update(outcome="blocked", apply_status="BLOCKED", blocking_findings=[{"code": "assessment-frontier-stale"}], publishable=False, can_apply=False)
            return result
        if blocking:
            result.update(outcome="blocked", apply_status="BLOCKED", blocking_findings=blocking, publishable=False, can_apply=False)
            return result
        validate_existing_output_ownership(root / places.output)
        staging = stage_outputs(root, selected, snapshot, places)
        replace_outputs_atomically(root, staging, places)
        if not source_snapshot_is_current(root, snapshot, places):
            raise CompileError("source-frontier-changed", "Source frontier changed during output replacement")
        result["publication"] = {
            "prior_output_state": prior,
            "transaction_id": sha256_bytes(canonical_json({"source_frontier_digest": digest, "output": places.output.as_posix()})),
            "output_digest": generated_tree_digest(root, places),
            "output_plan": output_plan(selected),
        }
        # Run support owns the canonical action/publication receipt.  Retain
        # supplied shared references as context, but never turn a caller's
        # reference-shaped data into a completed Journal publication here.
        result.update(outcome="pending_recording", apply_status="APPLIED", generated_tree_digest=result["publication"]["output_digest"], publishable=True)
        return result
    except CompileError as error:
        if error.code == "atomic-replacement-uncertain":
            prior = "uncertain"
        return {
            "schema": SCHEMA, "outcome": "blocked", "publishable": False,
            "blocking_findings": [error.record()], "publication": {"prior_output_state": prior},
            "source_frontier": None, "conflicts": [], "decision_provenance": [], "run_receipt_refs": [],
            "apply_status": "BLOCKED", "can_apply": False, "diagnostics": [error.record()],
        }


def select_sources_action(request: Mapping[str, object]) -> dict[str, object]:
    return run_request({**request, "operation": "dry_run"})


def assess_sources_action(request: Mapping[str, object]) -> dict[str, object]:
    return run_request({**request, "operation": "dry_run"})


def propose_corrections_action(request: Mapping[str, object]) -> dict[str, object]:
    result = run_request({**request, "operation": "dry_run"})
    return {**result, "outcome": "reassess_required" if result.get("conflicts") else result["outcome"], "source_edit_supported": False}


def obtain_decision_action(request: Mapping[str, object]) -> dict[str, object]:
    return run_request({**request, "operation": "dry_run"})


def apply_corrections_action(request: Mapping[str, object]) -> dict[str, object]:
    result = run_request({**request, "operation": "dry_run"})
    handoff = {
        "kind": "source_owner_correction_request",
        "source_edit_supported": False,
        "required_follow_up_actions": ["CA-O-004", "CA-O-005"],
    }
    if result.get("outcome") == "blocked":
        return {**result, "source_edit_supported": False, "correction_request_or_receipt": handoff}
    return {
        **result,
        "outcome": "reassess_required",
        "source_edit_supported": False,
        "correction_request_or_receipt": handoff,
        "reselection_required": True,
        "reassessment_required": True,
    }


def publish_action(request: Mapping[str, object]) -> dict[str, object]:
    result = run_request({**request, "operation": "apply"})
    return {
        **result,
        "action_handoff": {
            "workflow_id": WORKFLOW_ID,
            "action_id": "CA-O-009",
            "operation": "apply",
            "run_receipt_behavior": "shared_passthrough_pending_canonical_recording",
        },
    }


ACTION_ADAPTERS = {
    "CA-O-004": select_sources_action,
    "CA-O-005": assess_sources_action,
    "CA-O-006": propose_corrections_action,
    "CA-O-007": obtain_decision_action,
    "CA-O-008": apply_corrections_action,
    "CA-O-009": publish_action,
}


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="CAPRMEDIO Project root")
    parser.add_argument("--apply", action="store_true", help="replace generated RMEDO output directories")
    parser.add_argument("--recover-publication-ref", help="canonical failed-publication reference for recovery")
    parser.add_argument("--request", type=Path, help="strict JSON request Carrier")
    args = parser.parse_args(argv)
    try:
        if args.request:
            if args.root or args.apply or args.recover_publication_ref:
                raise request_error("request-mixed-cli-modes", "--request cannot be mixed with compatibility flags")
            raw = json.loads(args.request.read_text(encoding="utf-8"))
            if not isinstance(raw, dict):
                raise request_error("request-invalid", "Strict request Carrier must contain one object")
            result = run_request(raw)
        else:
            root = args.root.resolve() if args.root else find_project_root(Path.cwd())
            places = methodology_paths(root)
            operation = "recover_publication" if args.recover_publication_ref else ("apply" if args.apply else "dry_run")
            request: dict[str, object] = {
                "operation": operation,
                "project_root": root.as_posix(),
                "governed_bindings": governed_bindings(root, places),
            }
            if operation != "dry_run":
                report, _, _ = compile_report(root, places)
                request["expected_source_frontier_digest"] = report["source_frontier_digest"]
            if args.recover_publication_ref:
                request["failed_publication_ref"] = args.recover_publication_ref
            result = run_request(request)
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0 if result.get("outcome") in {"assessed", "pending_recording", "published"} else 2
    except CompileError as error:
        print(
            json.dumps(
                {
                    "schema": SCHEMA,
                    "authority": "non_authoritative_dry_run",
                    "can_apply": False,
                    "diagnostics": [error.record()],
                },
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            )
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(run())
