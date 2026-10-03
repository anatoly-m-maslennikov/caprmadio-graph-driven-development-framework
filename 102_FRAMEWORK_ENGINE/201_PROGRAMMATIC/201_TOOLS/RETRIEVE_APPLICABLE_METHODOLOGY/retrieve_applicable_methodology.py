#!/usr/bin/env python3
"""Retrieve source-backed Applicable Methodology authority by Subject Path."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import deque
from dataclasses import dataclass
from pathlib import Path


APPLICABLE_RELATIVE = Path(".caprmedio_framework/00_APPLICABLE_METHODOLOGY")
SOURCES_RELATIVE = APPLICABLE_RELATIVE / "000_APPLICABLE_MTHD_sources"
TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from artifact_metadata import SETTINGS_PATH, project_identity  # noqa: E402
ROLES = ("04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations")
SCHEMA = "caprmedio.retrieve_applicable_methodology.v1"
TEMPORAL_FORMS = ("continuant", "occurrent")

# The source Superlayer and its direct children are structural Scope Units.
# Their legacy human-readable paths remain accepted query aliases until source
# carriers use only the canonical uppercase names.
SOURCE_SCOPE_ALIASES = {
    "METHODOLOGY_SOURCES": "METHODOLOGY_SOURCES",
    "Applicable Methodology/Sources": "METHODOLOGY_SOURCES",
    "CORE_META_MODEL": "CORE_META_MODEL",
    "Core Meta-Model": "CORE_META_MODEL",
    "Applicable Methodology/Sources/Core Meta-Model": "CORE_META_MODEL",
    "INSTALLED_EXTENSIONS": "INSTALLED_EXTENSIONS",
    "Installed Extensions": "INSTALLED_EXTENSIONS",
    "Applicable Methodology/Sources/Installed Extensions": "INSTALLED_EXTENSIONS",
    "PROJECT_CONFIGURATION": "PROJECT_CONFIGURATION",
    "Project Configuration": "PROJECT_CONFIGURATION",
    "Applicable Methodology/Sources/Project Configuration": "PROJECT_CONFIGURATION",
    "Project": "PROJECT",
}
SOURCE_SCOPE_CHILDREN = {
    "METHODOLOGY_SOURCES": ("CORE_META_MODEL", "INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION"),
    "CORE_META_MODEL": (),
    "INSTALLED_EXTENSIONS": (),
    "PROJECT_CONFIGURATION": (),
}


class RetrievalError(Exception):
    """A stable retrieval validation failure."""

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
class Carrier:
    order: int
    atom_id: str
    version: int
    projected_path: str
    projected_sha256: str
    source_path: str
    source_sha256: str
    governs: tuple[tuple[str, str], ...]
    depends_on: tuple[tuple[str, str], ...]

    def record(self, reasons: list[dict[str, str]]) -> dict[str, object]:
        return {
            "atom_id": self.atom_id,
            "version": self.version,
            "projected_carrier_path": self.projected_path,
            "projected_carrier_sha256": self.projected_sha256,
            "source_carrier_path": self.source_path,
            "source_carrier_sha256": self.source_sha256,
            "selection_reasons": reasons,
        }


@dataclass(frozen=True)
class ScopeResolution:
    """One non-Atom structural Scope Unit retrieval result."""

    subject_path: str
    scope_unit: str
    current_scope: str
    project_settings_carrier: str | None
    source: str

    def record(self, *, reason_kind: str, temporal_form: str, required_by_atom_id: str | None) -> dict[str, str]:
        record = {
            "category": "scope_unit",
            "reason_kind": reason_kind,
            "temporal_form": temporal_form,
            "subject_path": self.subject_path,
            "scope_unit": self.scope_unit,
            "current_scope": self.current_scope,
            "source": self.source,
        }
        if self.project_settings_carrier is not None:
            record["project_settings_carrier"] = self.project_settings_carrier
        if required_by_atom_id is not None:
            record["required_by_atom_id"] = required_by_atom_id
        return record


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def split_frontmatter(data: bytes, path: str) -> tuple[str, bytes]:
    if not data.startswith(b"---\n"):
        raise RetrievalError("frontmatter-missing", "Projected Carrier requires YAML frontmatter", path=path)
    boundary = data.find(b"\n---\n", 4)
    if boundary < 0:
        raise RetrievalError("frontmatter-unterminated", "Projected Carrier frontmatter is unterminated", path=path)
    try:
        frontmatter = data[4:boundary].decode("utf-8")
        data.decode("utf-8")
    except UnicodeDecodeError as error:
        raise RetrievalError("carrier-not-utf8", "Projected Carrier must be UTF-8", path=path) from error
    return frontmatter, data[boundary + 5 :]


def scalar_optional(frontmatter: str, key: str, path: str) -> str | None:
    matches = re.findall(rf"(?m)^{re.escape(key)}:\s*([^\n]+?)\s*$", frontmatter)
    if len(matches) > 1:
        raise RetrievalError(
            "frontmatter-scalar-cardinality",
            "Projected Carrier permits at most one scalar",
            path=path,
            key=key,
            count=len(matches),
        )
    return matches[0].strip().strip("'\"") if matches else None


def scalar(frontmatter: str, key: str, path: str) -> str:
    value = scalar_optional(frontmatter, key, path)
    if value is None:
        raise RetrievalError(
            "frontmatter-scalar-missing",
            "Projected Carrier requires one scalar",
            path=path,
            key=key,
        )
    return value


def subject_values(frontmatter: str, relation: str) -> tuple[tuple[str, str], ...]:
    lines = frontmatter.splitlines()
    in_subjects = False
    current_relation: str | None = None
    current_form: str | None = None
    values: list[tuple[str, str]] = []
    for line in lines:
        if line == "subjects:":
            in_subjects = True
            current_relation = None
            current_form = None
            continue
        if in_subjects and line and not line[0].isspace():
            break
        if not in_subjects:
            continue
        relation_match = re.fullmatch(r"  ([A-Za-z_][A-Za-z0-9_-]*):\s*", line)
        if relation_match:
            current_relation = relation_match.group(1)
            current_form = None
            continue
        form_match = re.fullmatch(r"    (continuant|occurrent):\s*", line)
        if form_match:
            current_form = form_match.group(1) if current_relation == relation else None
            continue
        item_match = re.fullmatch(r"      -\s+(.+?)\s*", line)
        if item_match and current_relation == relation and current_form:
            value = item_match.group(1).strip().strip("'\"")
            if value:
                values.append((current_form, value))
    return tuple(values)


def projection_source(frontmatter: str, path: str) -> str:
    lines = frontmatter.splitlines()
    in_projection = False
    values: list[str] = []
    for line in lines:
        if line == "projection:":
            in_projection = True
            continue
        if in_projection and line and not line[0].isspace():
            break
        match = re.fullmatch(r"  source_carrier_path:\s*(.+?)\s*", line)
        if in_projection and match:
            values.append(match.group(1).strip().strip("'\""))
    if len(values) != 1:
        raise RetrievalError(
            "projection-source-cardinality",
            "Projected Carrier requires exactly one relative Source Carrier path",
            path=path,
            count=len(values),
        )
    return values[0]


def source_payload(projected: bytes, source_relative: str, path: str) -> bytes:
    addition = f"\nprojection:\n  source_carrier_path: {source_relative}".encode("utf-8")
    if projected.count(addition) != 1:
        raise RetrievalError("projection-payload-invalid", "Projection metadata is not canonical", path=path)
    return projected.replace(addition, b"", 1)


def repo_relative(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise RetrievalError("path-outside-project", "Carrier is outside the Project root", path=path.as_posix()) from error


def find_project_root(start: Path) -> Path:
    resolved = start.resolve()
    for candidate in (resolved, *resolved.parents):
        if (candidate / APPLICABLE_RELATIVE).is_dir():
            return candidate
    raise RetrievalError("project-root-not-found", "Cannot find the Applicable Methodology root", start=resolved.as_posix())


def discover(root: Path) -> list[Carrier]:
    applicable = (root / APPLICABLE_RELATIVE).resolve()
    sources = (root / SOURCES_RELATIVE).resolve()
    if not sources.is_dir():
        raise RetrievalError("source-root-missing", "Applicable Methodology Source root is missing", path=repo_relative(root, sources))
    carriers: list[Carrier] = []
    order = 0
    for role in ROLES:
        role_root = applicable / role
        if not role_root.is_dir():
            raise RetrievalError("role-root-missing", "Applicable Methodology role root is missing", role=role)
        unexpected = [path for path in role_root.iterdir() if not path.is_file() or path.suffix != ".md" or path.is_symlink()]
        if unexpected:
            raise RetrievalError(
                "role-root-non-carrier",
                "Applicable Methodology role root contains a non-Carrier entry",
                paths=[repo_relative(root, path) for path in sorted(unexpected)],
            )
        for projected_path in sorted(role_root.glob("*.md")):
            projected_data = projected_path.read_bytes()
            projected_relative = repo_relative(root, projected_path)
            frontmatter, _ = split_frontmatter(projected_data, projected_relative)
            relative_source = projection_source(frontmatter, projected_relative)
            candidate_source = (projected_path.parent / relative_source).resolve()
            try:
                candidate_source.relative_to(sources)
            except ValueError as error:
                raise RetrievalError(
                    "projection-source-outside-sources",
                    "Projected Carrier Source path escapes the governed Source root",
                    path=projected_relative,
                    source_carrier_path=relative_source,
                ) from error
            if not candidate_source.is_file() or candidate_source.is_symlink():
                raise RetrievalError(
                    "projection-source-missing",
                    "Projected Carrier Source is not a regular current Carrier",
                    path=projected_relative,
                    source_carrier_path=repo_relative(root, candidate_source),
                )
            source_data = candidate_source.read_bytes()
            if source_payload(projected_data, relative_source, projected_relative) != source_data:
                raise RetrievalError(
                    "projection-source-mismatch",
                    "Projected Carrier differs from its exact Source Carrier after Projection metadata removal",
                    path=projected_relative,
                    source_carrier_path=repo_relative(root, candidate_source),
                )
            atom_id = scalar_optional(frontmatter, "atom_id", projected_relative)
            if atom_id is None:
                atom_id = projected_path.stem.split("--", 1)[0]
            if not atom_id:
                raise RetrievalError("atom-id-missing", "Cannot derive Projected Atom identity", path=projected_relative)
            version_raw = scalar(frontmatter, "version", projected_relative)
            if not re.fullmatch(r"[1-9][0-9]*", version_raw):
                raise RetrievalError("version-invalid", "Projected Atom revision requires a positive integer version", path=projected_relative)
            carriers.append(
                Carrier(
                    order=order,
                    atom_id=atom_id,
                    version=int(version_raw),
                    projected_path=projected_relative,
                    projected_sha256=sha256(projected_data),
                    source_path=repo_relative(root, candidate_source),
                    source_sha256=sha256(source_data),
                    governs=subject_values(frontmatter, "governs"),
                    depends_on=subject_values(frontmatter, "depends_on"),
                )
            )
            order += 1
    identities = [carrier.atom_id for carrier in carriers]
    duplicates = sorted({atom_id for atom_id in identities if identities.count(atom_id) > 1})
    if duplicates:
        raise RetrievalError("duplicate-atom-identity", "Applicable Methodology contains duplicate Atom identities", atom_ids=duplicates)
    return carriers


def project_scope_name(root: Path) -> str:
    """Read the Project name from authoritative Project Settings, never a Projection."""
    try:
        return str(project_identity(root)["project"]["name"])
    except ValueError as error:
        raise RetrievalError(
            "project-settings-invalid", str(error), path=SETTINGS_PATH.as_posix()
        ) from error


def resolve_scope_unit(root: Path, subject_path: str) -> ScopeResolution | None:
    """Resolve one exact structural Scope Unit without synthesizing Atom authority."""

    scope_unit = SOURCE_SCOPE_ALIASES.get(subject_path)
    if scope_unit is None:
        return None
    if scope_unit == "PROJECT":
        project_name = project_scope_name(root)
        return ScopeResolution(
            subject_path=subject_path,
            scope_unit=project_name,
            current_scope=project_name,
            project_settings_carrier=SETTINGS_PATH.as_posix(),
            source="project_settings",
        )
    return ScopeResolution(
        subject_path=subject_path,
        scope_unit=scope_unit,
        current_scope="METHODOLOGY_SOURCES",
        project_settings_carrier=None,
        source="applicable_methodology_source_structure",
    )


def is_lowercase_general_subject(subject_path: str) -> bool:
    """Return whether a path is an explicitly terminal General Subject."""

    return bool(subject_path) and subject_path[0].islower()


def retrieve(
    root: Path,
    carriers: list[Carrier],
    subject_paths: list[str],
    process_paths: list[str],
) -> tuple[list[Carrier], dict[int, list[dict[str, str]]], list[dict[str, str]], list[dict[str, str]]]:
    governors: dict[tuple[str, str], list[int]] = {}
    for index, carrier in enumerate(carriers):
        for subject in carrier.governs:
            governors.setdefault(subject, []).append(index)

    reasons: dict[int, list[dict[str, str]]] = {}
    queue: deque[int] = deque()
    resolutions: list[dict[str, str]] = []
    recorded_resolutions: set[tuple[object, ...]] = set()

    def record_resolution(record: dict[str, str]) -> None:
        key = tuple(sorted(record.items()))
        if key not in recorded_resolutions:
            recorded_resolutions.add(key)
            resolutions.append(record)

    def select_governors(
        temporal_form: str,
        subject_path: str,
        *,
        reason_kind: str,
        required_by_atom_id: str | None,
    ) -> bool:
        indexes = governors.get((temporal_form, subject_path), [])
        if not indexes:
            return False
        record_resolution(
            {
                "category": "exact_governor",
                "reason_kind": reason_kind,
                "temporal_form": temporal_form,
                "subject_path": subject_path,
                **({"required_by_atom_id": required_by_atom_id} if required_by_atom_id is not None else {}),
            }
        )
        for index in indexes:
            reason = {"kind": reason_kind, "temporal_form": temporal_form, "subject_path": subject_path}
            if required_by_atom_id is not None:
                reason["required_by_atom_id"] = required_by_atom_id
            if reason not in reasons.setdefault(index, []):
                reasons[index].append(reason)
            queue.append(index)
        return True

    def resolve_non_governor(
        temporal_form: str,
        subject_path: str,
        *,
        reason_kind: str,
        required_by_atom_id: str | None,
    ) -> bool:
        scope_resolution = resolve_scope_unit(root, subject_path)
        if scope_resolution is not None:
            record_resolution(
                scope_resolution.record(
                    reason_kind=reason_kind,
                    temporal_form=temporal_form,
                    required_by_atom_id=required_by_atom_id,
                )
            )
            return True
        if is_lowercase_general_subject(subject_path):
            record = {
                "category": "general_subject",
                "reason_kind": reason_kind,
                "temporal_form": temporal_form,
                "subject_path": subject_path,
                "terminal": "true",
            }
            if required_by_atom_id is not None:
                record["required_by_atom_id"] = required_by_atom_id
            record_resolution(record)
            return True
        return False

    unresolved: set[tuple[str, str]] = set()
    for query_kind, temporal_forms, values in (
        ("subject", TEMPORAL_FORMS, subject_paths),
        ("process", ("occurrent",), process_paths),
    ):
        for value in values:
            resolved = False
            for temporal_form in temporal_forms:
                if select_governors(
                    temporal_form,
                    value,
                    reason_kind=query_kind,
                    required_by_atom_id=None,
                ):
                    resolved = True
                    continue
                if resolve_non_governor(
                    temporal_form,
                    value,
                    reason_kind=query_kind,
                    required_by_atom_id=None,
                ):
                    resolved = True
                    continue
            if not resolved:
                unresolved.add((temporal_forms[0], value))

    expanded: set[int] = set()
    while queue:
        index = queue.popleft()
        if index in expanded:
            continue
        expanded.add(index)
        for temporal_form, subject_path in carriers[index].depends_on:
            if select_governors(
                temporal_form,
                subject_path,
                reason_kind="prerequisite",
                required_by_atom_id=carriers[index].atom_id,
            ):
                continue
            if not resolve_non_governor(
                temporal_form,
                subject_path,
                reason_kind="prerequisite",
                required_by_atom_id=carriers[index].atom_id,
            ):
                unresolved.add((temporal_form, subject_path))

    selected = [carrier for index, carrier in enumerate(carriers) if index in reasons]
    diagnostics = [
        {"code": "unresolved-prerequisite", "temporal_form": temporal_form, "subject_path": subject_path}
        for temporal_form, subject_path in sorted(unresolved)
    ]
    return selected, reasons, diagnostics, resolutions


def canonical_digest(carriers: list[Carrier]) -> str:
    records = [
        {
            "atom_id": carrier.atom_id,
            "version": carrier.version,
            "projected_carrier_path": carrier.projected_path,
            "projected_carrier_sha256": carrier.projected_sha256,
            "source_carrier_path": carrier.source_path,
            "source_carrier_sha256": carrier.source_sha256,
        }
        for carrier in carriers
    ]
    data = json.dumps(records, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256(data)


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="CAPRMEDIO Project root")
    parser.add_argument("--subject", action="append", default=[], help="exact Subject Path; may repeat")
    parser.add_argument("--process", action="append", default=[], help="exact occurrent Subject Path; may repeat")
    args = parser.parse_args(argv)
    try:
        if not args.subject and not args.process:
            raise RetrievalError("query-missing", "At least one --subject or --process query is required")
        root = args.root.resolve() if args.root else find_project_root(Path.cwd())
        carriers = discover(root)
        selected, reasons, diagnostics, resolutions = retrieve(root, carriers, args.subject, args.process)
        by_identity = {carrier.atom_id: index for index, carrier in enumerate(carriers)}
        report = {
            "schema": SCHEMA,
            "authority": "non_authoritative_on_demand_projection",
            "query": {"subject_paths": args.subject, "process_paths": args.process},
            "applicable_methodology_carrier_count": len(carriers),
            "selected_atom_count": len(selected),
            "selected_frontier_digest": canonical_digest(selected),
            "complete": not diagnostics,
            "persistent_subject_index_created": False,
            "selected_atoms": [carrier.record(reasons[by_identity[carrier.atom_id]]) for carrier in selected],
            "resolution_outcomes": resolutions,
            "diagnostics": diagnostics,
        }
        print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
        return 0 if report["complete"] else 2
    except RetrievalError as error:
        print(
            json.dumps(
                {
                    "schema": SCHEMA,
                    "authority": "non_authoritative_on_demand_projection",
                    "complete": False,
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
