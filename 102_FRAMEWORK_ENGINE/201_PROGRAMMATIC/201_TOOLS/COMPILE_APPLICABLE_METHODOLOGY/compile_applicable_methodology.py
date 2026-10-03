#!/usr/bin/env python3
"""Compile the non-authoritative Applicable Methodology Atom Carrier tree."""

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
from typing import Iterable

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artifact_metadata import atom_identifier


SOURCE_RELATIVE = Path(
    ".caprmedio_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources"
)
OUTPUT_RELATIVE = Path(".caprmedio_framework/00_APPLICABLE_METHODOLOGY")
APPROVAL_RELATIVE = SOURCE_RELATIVE / "003_PROJECT_CONFIGURATION/applicable_methodology_conflict_approvals.toml"
LAYERS = (
    ("CORE_META_MODEL", "001_CORE_META_MODEL", 0, True),
    ("INSTALLED_EXTENSIONS", "002_INSTALLED_EXTENSIONS", 1, False),
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
SCHEMA = "caprmedio.compile_applicable_methodology.dry_run.v1"


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

    def frontier_record(self) -> dict[str, object]:
        return {
            "source_layer": self.layer,
            "atom_id": self.atom_id,
            "atom_revision": self.version,
            "source_carrier_path": self.source_path,
            "source_carrier_sha256": self.source_sha256,
        }

    def report_record(self) -> dict[str, object]:
        record = {
            **self.frontier_record(),
            "content_role": self.role,
            "output_path": f"{OUTPUT_RELATIVE.as_posix()}/{self.role_directory}/{self.basename}",
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


def discover_candidates(root: Path) -> tuple[list[Candidate], list[dict[str, object]], dict[str, str]]:
    source_root = root / SOURCE_RELATIVE
    diagnostics: list[dict[str, object]] = []
    if not source_root.is_dir():
        raise CompileError("source-root-missing", "Applicable Methodology source root is missing", path=SOURCE_RELATIVE.as_posix())

    root_role_directories = {directory for _, directory in ROLES}
    observed_layers = sorted(
        path.name
        for path in source_root.iterdir()
        if path.is_dir() and path.name not in root_role_directories
    )
    expected_layers = [directory for _, directory, _, _ in LAYERS]
    if observed_layers != expected_layers:
        raise CompileError(
            "source-layer-topology-mismatch",
            "Structural Source Layers differ from the governed topology",
            expected=expected_layers,
            observed=observed_layers,
        )

    installed = source_root / "002_INSTALLED_EXTENSIONS"
    unexpected_installed = sorted(
        repo_relative(root, path)
        for path in installed.rglob("*")
        if path.is_file() and path.name not in IGNORED_INSTALLED_EXTENSION_FILES
    )
    if unexpected_installed:
        raise CompileError(
            "installed-extensions-not-empty",
            "INSTALLED_EXTENSIONS must be empty and non-contributing",
            carriers=unexpected_installed,
        )

    candidates: list[Candidate] = []
    source_snapshot: dict[str, str] = {}
    for layer, layer_directory, layer_order, contributes in LAYERS:
        layer_root = source_root / layer_directory
        if not contributes:
            continue
        for role, role_directory in ROLES:
            role_root = layer_root / role_directory
            if not role_root.exists():
                continue
            if not role_root.is_dir():
                raise CompileError("source-role-not-directory", "Source role Carrier must be a directory", path=repo_relative(root, role_root))
            for path in sorted(role_root.rglob("*.md")):
                relative_within_role = path.relative_to(role_root)
                if {"archive", "drafts"}.intersection(relative_within_role.parts):
                    continue
                if not path.is_file() or path.is_symlink():
                    raise CompileError("source-carrier-not-regular", "Selected Source Carrier must be a regular file", path=repo_relative(root, path))
                relative = repo_relative(root, path)
                data = path.read_bytes()
                digest = sha256_bytes(data)
                source_snapshot[relative] = digest
                frontmatter, _ = split_frontmatter(data, relative)
                if re.search(r"(?m)^projection:\s*(?:$|\{)", frontmatter):
                    raise CompileError("source-projection-metadata-present", "Authoritative Source Carrier cannot contain projection metadata", path=relative)
                version_raw = top_scalar(frontmatter, "version")
                if version_raw is None or not re.fullmatch(r"[1-9][0-9]*", version_raw):
                    raise CompileError("source-version-invalid", "Selected Source Atom revision requires a positive integer version", path=relative)
                defined_term, definition_subject_path = definition_subject(frontmatter, relative)
                candidates.append(
                    Candidate(
                        layer=layer,
                        layer_order=layer_order,
                        role=role,
                        role_directory=role_directory,
                        atom_id=derive_atom_id(path, frontmatter),
                        version=int(version_raw),
                        source_path=relative,
                        source_sha256=digest,
                        basename=path.name,
                        priority=top_scalar(frontmatter, "priority"),
                        priority_group=top_scalar(frontmatter, "applicable_methodology_priority_group"),
                        replacements=relation_targets(frontmatter, RELATION_KINDS["replacement"]),
                        incompatibilities=relation_targets(frontmatter, RELATION_KINDS["incompatible"]),
                        definition_term=defined_term,
                        definition_subject_path=definition_subject_path,
                    )
                )
    candidates.sort(key=candidate_sort_key)
    if not candidates:
        diagnostics.append({"code": "empty-source-frontier", "message": "No eligible current active RMEDO Source Atom revisions were found"})
    return candidates, diagnostics, source_snapshot


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
                output_path=f"{OUTPUT_RELATIVE.as_posix()}/{role_directory}/{basename}",
            )
        )

    conflicts.sort(key=lambda item: (str(item["type"]), str(item["conflict_id"])))
    return conflicts


def discover_approvals(root: Path, candidates: list[Candidate]) -> list[Approval]:
    del candidates
    path = root / APPROVAL_RELATIVE
    if not path.exists():
        return []
    if not path.is_file() or path.is_symlink():
        raise CompileError("approval-carrier-invalid", "Project Configuration approval Carrier must be a regular TOML file", path=APPROVAL_RELATIVE.as_posix())
    try:
        document = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise CompileError("approval-carrier-invalid", "Project Configuration approval Carrier is not valid UTF-8 TOML", path=APPROVAL_RELATIVE.as_posix()) from error
    if document.get("schema") != "caprmedio.applicable_methodology_conflict_approvals.v1":
        raise CompileError("approval-schema-invalid", "Project Configuration approval Carrier schema is invalid", path=APPROVAL_RELATIVE.as_posix())
    records = document.get("approvals", [])
    if not isinstance(records, list) or any(not isinstance(record, dict) for record in records):
        raise CompileError("approval-record-invalid", "Project Configuration approvals must be an array of tables", path=APPROVAL_RELATIVE.as_posix())
    required = {"conflict_id", "source_frontier_digest", "selected_source_carrier_path", "operator"}
    approvals: list[Approval] = []
    for record in records:
        missing = sorted(required.difference(record))
        if missing:
            raise CompileError(
                "approval-record-incomplete",
                "Project Configuration approval record is incomplete",
                carrier_path=APPROVAL_RELATIVE.as_posix(),
                missing=missing,
            )
        if any(not isinstance(record[key], str) for key in required):
            raise CompileError(
                "approval-record-invalid",
                "Project Configuration approval fields must be strings",
                carrier_path=APPROVAL_RELATIVE.as_posix(),
            )
        approvals.append(
            Approval(
                conflict_id=record["conflict_id"],
                source_frontier_digest=record["source_frontier_digest"],
                selected_source_carrier_path=record["selected_source_carrier_path"],
                operator=record["operator"],
                carrier_path=APPROVAL_RELATIVE.as_posix(),
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


def source_snapshot_is_current(root: Path, snapshot: dict[str, str]) -> bool:
    return all((root / path).is_file() and sha256_bytes((root / path).read_bytes()) == digest for path, digest in snapshot.items())


def projection_bytes(source: bytes, source_relative_from_output: str, path: str) -> bytes:
    frontmatter, _ = split_frontmatter(source, path)
    if re.search(r"(?m)^projection:\s*(?:$|\{)", frontmatter):
        raise CompileError("source-projection-metadata-present", "Authoritative Source Carrier cannot contain projection metadata", path=path)
    boundary = source.find(b"\n---\n", 4)
    addition = f"\nprojection:\n  source_carrier_path: {source_relative_from_output}".encode("utf-8")
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


def stage_outputs(root: Path, candidates: list[Candidate], source_snapshot: dict[str, str]) -> Path:
    output_root = root / OUTPUT_RELATIVE
    output_root.mkdir(parents=True, exist_ok=True)
    temporary_staging = root / ".caprmedio_tmp/compile_applicable_methodology"
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
            projected = projection_bytes(source_path.read_bytes(), relative_source, candidate.source_path)
            target = new_root / candidate.role_directory / candidate.basename
            target.write_bytes(projected)
        if not source_snapshot_is_current(root, source_snapshot):
            raise CompileError("source-frontier-changed", "Source frontier changed while outputs were staged")
        return staging
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise


def replace_outputs_atomically(root: Path, staging: Path) -> None:
    output_root = root / OUTPUT_RELATIVE
    new_root = staging / "new"
    existing: dict[Path, bytes] = {}
    expected: set[Path] = set()
    for _, role_directory in ROLES:
        target_directory = output_root / role_directory
        target_directory.mkdir(parents=True, exist_ok=True)
        existing.update({path: path.read_bytes() for path in target_directory.iterdir() if path.is_file()})
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
        for target in reversed(installed):
            if target.exists() and target not in existing:
                target.unlink()
        for target, data in existing.items():
            temporary = target.with_name(f".{target.name}.rollback.tmp")
            temporary.write_bytes(data)
            os.replace(temporary, target)
        raise CompileError("atomic-replacement-failed", "Generated RMEDO output replacement rolled back", error=type(error).__name__) from error
    finally:
        shutil.rmtree(staging, ignore_errors=True)


def generated_tree_digest(root: Path) -> str:
    output_root = root / OUTPUT_RELATIVE
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


def compile_report(root: Path) -> tuple[dict[str, object], list[Candidate], dict[str, str]]:
    candidates, diagnostics, source_snapshot = discover_candidates(root)
    digest = frontier_digest(candidates)
    conflicts = detect_conflicts(candidates)
    approvals = discover_approvals(root, candidates)
    selected, approval_results, unresolved = resolve_conflicts(candidates, conflicts, approvals, digest)
    report: dict[str, object] = {
        "schema": SCHEMA,
        "authority": "non_authoritative_dry_run",
        "structural_source_layers": [name for name, _, _, _ in LAYERS],
        "contributing_source_layers": [name for name, _, _, contributes in LAYERS if contributes],
        "source_frontier_digest": digest,
        "eligible_candidate_count": len(candidates),
        "conflict_count": len(conflicts),
        "unresolved_conflict_count": len(unresolved),
        "conflicts": conflicts,
        "approval_results": approval_results,
        "diagnostics": diagnostics,
        "selected_candidate_count": len(selected),
        "output_plan": output_plan(selected),
        "persistent_subject_indexes": False,
        "can_apply": not diagnostics and not unresolved,
    }
    return report, selected, source_snapshot


def find_project_root(start: Path) -> Path:
    resolved = start.resolve()
    for candidate in (resolved, *resolved.parents):
        if (candidate / SOURCE_RELATIVE).is_dir():
            return candidate
    raise CompileError("project-root-not-found", "Cannot find CAPRMEDIO Project root", start=resolved.as_posix())


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="CAPRMEDIO Project root")
    parser.add_argument("--apply", action="store_true", help="replace generated RMEDO output directories")
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve() if args.root else find_project_root(Path.cwd())
        report, selected, source_snapshot = compile_report(root)
        if not args.apply:
            print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
            return 0 if report["can_apply"] else 2
        if not report["can_apply"]:
            report["apply_status"] = "BLOCKED"
            print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
            return 2
        validate_existing_output_ownership(root / OUTPUT_RELATIVE)
        staging = stage_outputs(root, selected, source_snapshot)
        replace_outputs_atomically(root, staging)
        if not source_snapshot_is_current(root, source_snapshot):
            raise CompileError("source-frontier-changed", "Source frontier changed during output replacement")
        report["apply_status"] = "APPLIED"
        report["generated_tree_digest"] = generated_tree_digest(root)
        print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
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
