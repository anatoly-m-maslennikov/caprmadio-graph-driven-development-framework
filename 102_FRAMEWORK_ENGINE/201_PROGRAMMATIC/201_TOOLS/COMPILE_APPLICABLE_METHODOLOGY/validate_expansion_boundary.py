#!/usr/bin/env python3
"""Validate that methodology sources expand, rather than mutate, Core authority."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path


TOOL_DIRECTORY = Path(__file__).resolve().parent
COMPILER_PATH = TOOL_DIRECTORY / "compile_applicable_methodology.py"
SPEC = importlib.util.spec_from_file_location("caprmedio_compiler", COMPILER_PATH)
assert SPEC and SPEC.loader
compiler = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compiler
SPEC.loader.exec_module(compiler)


SCHEMA = "caprmedio.validate_methodology_expansion_boundary.v1"
BOUNDARY_ATOM_ID = "CA-R-1375"
LAYER_DIRECTORIES = (
    ("CORE_META_MODEL", "001_CORE_META_MODEL"),
    ("INSTALLED_EXTENSIONS", "002_INSTALLED_EXTENSIONS"),
    ("PROJECT_CONFIGURATION", "003_PROJECT_CONFIGURATION"),
)
EXTERNAL_LAYERS = frozenset({"INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION"})
MUTATING_RELATIONS = frozenset({"replacement_of", "replaces", "override_of", "overrides"})
INACTIVE_DIRECTORY_NAMES = frozenset({"archive", "drafts", "done", "canceled"})


@dataclass(frozen=True)
class AtomRecord:
    atom_id: str
    layer: str
    active: bool
    path: str
    sha256: str
    cce_form: str | None
    mutating_targets: tuple[str, ...]
    definition_term: str | None


def repo_relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def is_active(path: Path) -> bool:
    return not any(part in INACTIVE_DIRECTORY_NAMES for part in path.parts)


def normalized_atom_id(target: str) -> str:
    return target.split("--", 1)[0].strip()


def read_record(root: Path, layer: str, path: Path) -> AtomRecord:
    data = path.read_bytes()
    frontmatter, _ = compiler.split_frontmatter(data, repo_relative(root, path))
    atom_id = compiler.derive_atom_id(path, frontmatter)
    active = is_active(path)
    definition_term: str | None = None
    if active and (compiler.top_scalar(frontmatter, "cce_form") or "").lower() == "definition":
        definition_term, _ = compiler.definition_subject(frontmatter, repo_relative(root, path))
    targets = compiler.relation_targets(frontmatter, set(MUTATING_RELATIONS))
    return AtomRecord(
        atom_id=atom_id,
        layer=layer,
        active=active,
        path=repo_relative(root, path),
        sha256=hashlib.sha256(data).hexdigest(),
        cce_form=compiler.top_scalar(frontmatter, "cce_form"),
        mutating_targets=tuple(sorted(normalized_atom_id(target) for target in targets if target.strip())),
        definition_term=definition_term,
    )


def discover_records(root: Path) -> list[AtomRecord]:
    source_root = root / compiler.SOURCE_RELATIVE
    records: list[AtomRecord] = []
    for layer, directory in LAYER_DIRECTORIES:
        layer_root = source_root / directory
        if not layer_root.is_dir():
            raise compiler.CompileError(
                "source-layer-missing",
                "Methodology Source Layer is missing",
                layer=layer,
                path=repo_relative(root, layer_root),
            )
        for path in sorted(layer_root.rglob("*.md")):
            try:
                records.append(read_record(root, layer, path))
            except compiler.CompileError:
                if is_active(path):
                    raise
    return records


def record_receipt(record: AtomRecord) -> dict[str, object]:
    return {
        "atom_id": record.atom_id,
        "cce_form": record.cce_form,
        "source_layer": record.layer,
        "source_carrier_path": record.path,
        "source_carrier_sha256": record.sha256,
    }


def validate(root: Path, included_layers: frozenset[str] | None = None) -> dict[str, object]:
    records = discover_records(root)
    selected_layers = included_layers or frozenset(layer for layer, _ in LAYER_DIRECTORIES)
    active = [record for record in records if record.active and record.layer in selected_layers]
    active_by_id: dict[str, list[AtomRecord]] = {}
    all_by_id: dict[str, list[AtomRecord]] = {}
    for record in records:
        all_by_id.setdefault(record.atom_id, []).append(record)
        if record.active:
            active_by_id.setdefault(record.atom_id, []).append(record)

    active_core = active_by_id.get(BOUNDARY_ATOM_ID, [])
    violations: list[dict[str, object]] = []
    if len(active_core) != 1 or active_core[0].layer != "CORE_META_MODEL":
        violations.append(
            {
                "type": "core_expansion_boundary_missing",
                "details": {
                    "required_atom_id": BOUNDARY_ATOM_ID,
                    "observed": [record_receipt(record) for record in active_core],
                },
            }
        )

    core_records = [record for record in active if record.layer == "CORE_META_MODEL"]
    core_ids = {record.atom_id for record in core_records}
    core_terms = {record.definition_term for record in core_records if record.definition_term}
    source_counts = {layer: sum(1 for record in active if record.layer == layer) for layer, _ in LAYER_DIRECTORIES}
    members: list[dict[str, object]] = []
    lineage_gaps: list[dict[str, object]] = []

    for record in sorted((item for item in active if item.layer in EXTERNAL_LAYERS), key=lambda item: (item.layer, item.path)):
        member = record_receipt(record)
        direct_core_targets = sorted(set(record.mutating_targets).intersection(core_ids))
        if direct_core_targets:
            violations.append(
                {
                    "type": "external_source_mutates_active_core_authority",
                    "details": {"source": member, "core_target_atom_ids": direct_core_targets},
                }
            )
        missing_targets = sorted(target for target in record.mutating_targets if target not in all_by_id)
        for target in missing_targets:
            lineage_gaps.append(
                {
                    "type": "unresolved_legacy_mutation_lineage",
                    "details": {"source": member, "target_atom_id": target},
                }
            )
        if record.definition_term and record.definition_term in core_terms:
            violations.append(
                {
                    "type": "external_source_redefines_core_term",
                    "details": {"source": member, "term": record.definition_term},
                }
            )
        member["classification"] = (
            "EXPANSION_CANDIDATE_WITH_LINEAGE_GAP" if missing_targets else "EXPANSION_CANDIDATE"
        )
        members.append(member)

    duplicate_external_ids = sorted(
        atom_id
        for atom_id, atom_records in active_by_id.items()
        if {record.layer for record in atom_records}.intersection(EXTERNAL_LAYERS)
        and "CORE_META_MODEL" in {record.layer for record in atom_records}
    )
    for atom_id in duplicate_external_ids:
        violations.append(
            {
                "type": "external_source_duplicates_active_core_atom_identity",
                "details": {"atom_id": atom_id, "records": [record_receipt(record) for record in active_by_id[atom_id]]},
            }
        )

    return {
        "schema": SCHEMA,
        "authority": "non_authoritative_validation_projection",
        "boundary_atom_id": BOUNDARY_ATOM_ID,
        "selected_source_layers": [layer for layer, _ in LAYER_DIRECTORIES if layer in selected_layers],
        "source_counts": source_counts,
        "external_member_count": len(members),
        "external_members": members,
        "hard_violation_count": len(violations),
        "hard_violations": violations,
        "stable_lineage_gap_count": len(lineage_gaps),
        "stable_lineage_gaps": lineage_gaps,
        "semantic_limit": (
            "The validation checks active Carrier identity, explicit mutation relations, and governed Definition Terms. "
            "It reports missing legacy lineage for later disposition and does not infer Claim equivalence."
        ),
        "can_conform": not violations,
    }


def find_project_root(start: Path) -> Path:
    resolved = start.resolve()
    for candidate in (resolved, *resolved.parents):
        if (candidate / compiler.SOURCE_RELATIVE).is_dir():
            return candidate
    raise compiler.CompileError("project-root-not-found", "Cannot find CAPRMEDIO Project root", start=resolved.as_posix())


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="CAPRMEDIO Project root")
    parser.add_argument(
        "--include-layer",
        action="append",
        choices=[layer for layer, _ in LAYER_DIRECTORIES],
        help="validate this selected source layer; repeat to validate a source combination",
    )
    arguments = parser.parse_args(argv)
    try:
        root = arguments.root.resolve() if arguments.root else find_project_root(Path.cwd())
        report = validate(root, frozenset(arguments.include_layer) if arguments.include_layer else None)
        print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
        return 0 if report["can_conform"] else 2
    except compiler.CompileError as error:
        print(
            json.dumps(
                {"schema": SCHEMA, "authority": "non_authoritative_validation_projection", "can_conform": False, "diagnostics": [error.record()]},
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            )
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(run())
