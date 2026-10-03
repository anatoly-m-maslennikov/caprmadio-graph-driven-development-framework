#!/usr/bin/env python3
"""Inventory and seal a proposed legacy-REQU-to-current RMEDO migration.

This is a read-only preparation tool, not an Atom editor.  It inventories every
active authoritative RMEDO carrier, emits a complete decision template, and
checks an operator-reviewed batch against the unchanged source frontier.  CCE
Claim conversion, identity assignment, relation rebinding, Journal writes, and
Git commits remain governed operations outside this script.

Examples (from the repository root):

    python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/migrations/prepare_active_rmedo_migration.py inventory
    python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/migrations/prepare_active_rmedo_migration.py template > /tmp/rmedo-decisions.json
    python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/migrations/prepare_active_rmedo_migration.py validate --decisions /tmp/rmedo-decisions.json

No command has an apply mode.  A validated result is a reviewable input to the
governed BULK_CHANGE/MIGRATE_ATOM_IDENTITY and CCE migration flow, not permission
to mutate carriers directly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tomllib
from pathlib import Path
from typing import Any


ROLES = {
    "04_requirement": "R",
    "05_method": "M",
    "06_evaluation": "E",
    "07_delivery": "D",
    "09_operations": "O",
}
INACTIVE = frozenset({"archive", "drafts", "canceled", "cancelled", "done", "solved"})
CANONICAL_FILENAME = re.compile(
    r"^(?P<id>CA-(?P<role>[RMEDO])-[0-9]{3,})(?:-[A-Z0-9_]+)+--[a-z0-9][a-z0-9-]*\.md$"
)
LEGACY_ID = re.compile(r"^(.+?-(?:REQU|METH|EVAL|DELV|OPS|CNTR|[RMEDO])-[0-9]{3,})(?=-|$)")
LEGACY_ROLE_TOKEN = re.compile(r"-(REQU|METH|EVAL|DELV|OPS)-[0-9]{3,}(?=-|$)")
TOP_LEVEL = re.compile(r"^([a-z][a-z0-9_]*):(?:[ \t]*(.*))?$")
SAFE_ATOM_ID = re.compile(r"^CA-([RMEDO])-([0-9]{3,})$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


class MigrationPreparationError(ValueError):
    """A source or approval precondition failed; no Atom was changed."""


def _settings(repository: Path, settings_path: Path | None) -> tuple[Path, str]:
    path = settings_path or Path(".caprmedio_caprmedio/caprmedio_project_settings.toml")
    if not path.is_absolute():
        path = repository / path
    path = path.resolve()
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise MigrationPreparationError(f"cannot read Project Settings: {path}: {error}") from error
    declared = data.get("paths", {}).get("control_root")
    prefix = data.get("artifacts", {}).get("identity", {}).get("project_prefix")
    if not isinstance(declared, str) or not declared or not isinstance(prefix, str):
        raise MigrationPreparationError("Project Settings lack paths.control_root or artifacts.identity.project_prefix")
    control = (repository / declared).resolve()
    if path.parent != control or not control.is_dir() or prefix != "CA":
        raise MigrationPreparationError("Project Settings location, control root, or CA identity prefix is inconsistent")
    try:
        control.relative_to(repository)
    except ValueError as error:
        raise MigrationPreparationError("control root escapes repository") from error
    return control, declared


def _frontmatter(source: bytes, path: str) -> dict[str, str]:
    try:
        text = source.decode("utf-8")
    except UnicodeDecodeError as error:
        raise MigrationPreparationError(f"non-UTF-8 active carrier: {path}") from error
    if not text.startswith("---\n"):
        raise MigrationPreparationError(f"missing YAML frontmatter: {path}")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise MigrationPreparationError(f"unclosed YAML frontmatter: {path}")
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = TOP_LEVEL.fullmatch(line)
        if match:
            if match.group(1) in result:
                raise MigrationPreparationError(f"duplicate frontmatter field in {path}: {match.group(1)}")
            result[match.group(1)] = (match.group(2) or "").strip().strip('"\'')
    return result


def _is_source(path: Path, control: Path) -> bool:
    relative = path.relative_to(control)
    parts = relative.parts
    if path.parent.name not in ROLES or any(part.casefold() in INACTIVE for part in parts[:-1]):
        return False
    # Applicable Methodology is a projection.  Its nested source tree is not.
    if "00_APPLICABLE_METHODOLOGY" in parts and "000_APPLICABLE_MTHD_sources" not in parts:
        return False
    return True


def _record(path: Path, repository: Path) -> dict[str, Any]:
    relative = path.relative_to(repository).as_posix()
    if path.is_symlink():
        raise MigrationPreparationError(f"symlink active carrier requires review: {relative}")
    source = path.read_bytes()
    frontmatter = _frontmatter(source, relative)
    role = ROLES[path.parent.name]
    stem = path.stem.partition("--")[0]
    canonical = CANONICAL_FILENAME.fullmatch(path.name)
    legacy = LEGACY_ID.match(stem)
    identity = canonical.group("id") if canonical else legacy.group(1) if legacy else None
    legacy_role = LEGACY_ROLE_TOKEN.search(identity) if identity else None
    try:
        version = int(frontmatter["version"])
    except (KeyError, ValueError) as error:
        raise MigrationPreparationError(f"missing or invalid version: {relative}") from error
    if version < 1:
        raise MigrationPreparationError(f"nonpositive version: {relative}")
    flags: list[str] = []
    if not canonical or canonical.group("role") != role:
        flags.append("noncanonical_filename_identity")
    if frontmatter.get("atom_id") and frontmatter["atom_id"] != identity:
        flags.append("frontmatter_identity_disagrees_with_filename")
    if not frontmatter.get("cce_version") or not frontmatter.get("cce_form"):
        flags.append("cce_metadata_incomplete")
    if "subjects" not in frontmatter:
        flags.append("subjects_absent")
    if not identity:
        flags.append("unrecognized_filename_identity")
    return {
        "source_path": relative,
        "source_sha256": hashlib.sha256(source).hexdigest(),
        "role": role,
        "version": version,
        "filename_identity": identity,
        "legacy_role_token": legacy_role.group(1) if legacy_role else None,
        "frontmatter_identity": frontmatter.get("atom_id") or None,
        "cce_version": frontmatter.get("cce_version") or None,
        "cce_form": frontmatter.get("cce_form") or None,
        "flags": flags,
    }


def inventory(repository: Path, settings_path: Path | None = None) -> dict[str, Any]:
    repository = repository.resolve()
    control, declared = _settings(repository, settings_path)
    records = [
        _record(path, repository)
        for path in sorted(control.rglob("*.md"))
        if _is_source(path, control)
    ]
    if not records:
        raise MigrationPreparationError("no active authoritative RMEDO carriers found")
    frontier = [f"{item['source_path']}\0{item['source_sha256']}" for item in records]
    digest = hashlib.sha256("\n".join(frontier).encode("utf-8")).hexdigest()
    candidates = [item for item in records if item["flags"]]
    return {
        "schema_version": 1,
        "mode": "read-only",
        "control_root": declared,
        "frontier_sha256": digest,
        "active_rmedo_count": len(records),
        "candidate_count": len(candidates),
        "semantic_claims_verified": False,
        "legacy_role_token_count": sum(bool(item["legacy_role_token"]) for item in records),
        "counts_by_role": {role: sum(item["role"] == role for item in records) for role in "RMEDO"},
        "counts_by_flag": {flag: sum(flag in item["flags"] for item in records)
                           for flag in sorted({flag for item in records for flag in item["flags"]})},
        "carriers": records,
    }


def decision_template(report: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "frontier_sha256": report["frontier_sha256"],
        "decisions": [
            {
                "source_path": item["source_path"],
                "source_sha256": item["source_sha256"],
                "new_atom_id": None,
                "destination_path": None,
                "cce_disposition": None,
                "relation_disposition": None,
            }
            for item in report["carriers"] if item["flags"]
        ],
    }


def validate_decisions(report: dict[str, Any], decisions: dict[str, Any], repository: Path) -> dict[str, Any]:
    if set(decisions) != {"schema_version", "frontier_sha256", "decisions"} or decisions["schema_version"] != 1:
        raise MigrationPreparationError("decision file must use the exact schema-version-1 keys")
    if decisions["frontier_sha256"] != report["frontier_sha256"]:
        raise MigrationPreparationError("source frontier changed since the decision template was generated")
    rows = decisions["decisions"]
    if not isinstance(rows, list):
        raise MigrationPreparationError("decisions must be a list")
    expected = {item["source_path"]: item for item in report["carriers"] if item["flags"]}
    seen: set[str] = set()
    target_ids: set[str] = set()
    target_paths: set[str] = set()
    existing_ids = {
        identity for item in report["carriers"]
        for identity in (item["filename_identity"], item["frontmatter_identity"]) if identity
    }
    plan: list[dict[str, Any]] = []
    keys = {"source_path", "source_sha256", "new_atom_id", "destination_path", "cce_disposition", "relation_disposition"}
    for row in rows:
        if not isinstance(row, dict) or set(row) != keys:
            raise MigrationPreparationError("every decision must contain exactly the template fields")
        source_path = row["source_path"]
        if not isinstance(source_path, str) or source_path not in expected or source_path in seen:
            raise MigrationPreparationError(f"unexpected or duplicate source: {source_path}")
        seen.add(source_path)
        item = expected[source_path]
        if row["source_sha256"] != item["source_sha256"]:
            raise MigrationPreparationError(f"source digest mismatch: {source_path}")
        if "frontmatter_identity_disagrees_with_filename" in item["flags"]:
            raise MigrationPreparationError(f"conflicting source identities need separate review: {source_path}")
        identity_change = "noncanonical_filename_identity" in item["flags"]
        if identity_change and not item["filename_identity"]:
            raise MigrationPreparationError(f"legacy identity is unrecognized; explicit source repair needed: {source_path}")
        new_id = row["new_atom_id"]
        destination = row["destination_path"]
        if identity_change:
            match = SAFE_ATOM_ID.fullmatch(new_id) if isinstance(new_id, str) else None
            if not match or match.group(1) != item["role"] or new_id in existing_ids or new_id in target_ids:
                raise MigrationPreparationError(f"invalid or colliding approved Atom ID: {source_path}")
            if not isinstance(destination, str) or not destination.endswith(".md"):
                raise MigrationPreparationError(f"destination path missing: {source_path}")
            destination_value = Path(destination)
            if destination_value.is_absolute() or ".." in destination_value.parts or destination_value.as_posix() != destination:
                raise MigrationPreparationError(f"destination must be a normalized repository-relative path: {source_path}")
            target = (repository / destination_value).resolve()
            control = (repository / report["control_root"]).resolve()
            try:
                target_relative = target.relative_to(control)
            except ValueError as error:
                raise MigrationPreparationError(f"destination escapes control root: {source_path}") from error
            if target.parent.name not in ROLES or ROLES[target.parent.name] != item["role"]:
                raise MigrationPreparationError(f"destination content role differs: {source_path}")
            if any(part.casefold() in INACTIVE for part in target_relative.parts[:-1]) or not target.parent.is_dir():
                raise MigrationPreparationError(f"destination is inactive or parent is absent: {source_path}")
            if "00_APPLICABLE_METHODOLOGY" in target_relative.parts and "000_APPLICABLE_MTHD_sources" not in target_relative.parts:
                raise MigrationPreparationError(f"destination is a projection: {source_path}")
            parsed = CANONICAL_FILENAME.fullmatch(target.name)
            if not parsed or parsed.group("id") != new_id or target.exists() or destination in target_paths:
                raise MigrationPreparationError(f"destination filename is invalid or occupied: {source_path}")
            target_ids.add(new_id)
            target_paths.add(destination)
        elif new_id is not None or destination is not None:
            raise MigrationPreparationError(f"identity is already canonical; target fields must be null: {source_path}")
        cce = row["cce_disposition"]
        needs_cce = "cce_metadata_incomplete" in item["flags"] or "subjects_absent" in item["flags"]
        if needs_cce and cce != "separate_one_atom_cce_migration":
            raise MigrationPreparationError(f"legacy CCE needs a separate one-Atom migration: {source_path}")
        if not needs_cce and cce not in ("reviewed_current", "separate_one_atom_cce_migration"):
            raise MigrationPreparationError(f"CCE Claim needs an explicit review disposition: {source_path}")
        if identity_change and row["relation_disposition"] != "review_and_rebind":
            raise MigrationPreparationError(f"identity change requires relation review: {source_path}")
        if not identity_change and row["relation_disposition"] is not None:
            raise MigrationPreparationError(f"relation disposition is unnecessary: {source_path}")
        plan.append({
            "source_path": source_path,
            "source_sha256": item["source_sha256"],
            "expected_version": item["version"],
            "approved_old_identity": item["filename_identity"],
            "new_atom_id": new_id,
            "destination_path": destination,
            "cce_disposition": cce,
            "relation_disposition": row["relation_disposition"],
            "flags": item["flags"],
        })
    if seen != set(expected):
        raise MigrationPreparationError(f"decision coverage incomplete: {len(set(expected) - seen)} candidate(s) missing")
    return {
        "schema_version": 1,
        "mode": "review-only",
        "frontier_sha256": report["frontier_sha256"],
        "active_rmedo_count": report["active_rmedo_count"],
        "candidate_count": len(plan),
        "governed_execution_required": True,
        "apply_supported": False,
        "semantic_claims_verified": False,
        "items": plan,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("inventory", "template", "validate"))
    parser.add_argument("--repository", type=Path, default=Path.cwd())
    parser.add_argument("--settings", type=Path)
    parser.add_argument("--decisions", type=Path, help="required with validate")
    args = parser.parse_args(argv)
    if args.command == "validate" and args.decisions is None:
        parser.error("validate requires --decisions")
    if args.command != "validate" and args.decisions is not None:
        parser.error("--decisions is only valid with validate")
    try:
        report = inventory(args.repository, args.settings)
        if args.command == "inventory":
            result = report
        elif args.command == "template":
            result = decision_template(report)
        else:
            decisions = json.loads(args.decisions.read_text(encoding="utf-8"))
            result = validate_decisions(report, decisions, args.repository.resolve())
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    except (MigrationPreparationError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"migration preparation refused: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
