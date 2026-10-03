#!/usr/bin/env python3
"""Backfill version and updated_at on every CAPRMEDIO Markdown Atom.

Usage:
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/backfill_atom_revision_metadata.py
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/backfill_atom_revision_metadata.py --apply

The default mode is read-only. The migration preflights every selected carrier,
fails closed on ambiguity, writes atomically, and is idempotent.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPOSITORY_ROOT = next(parent for parent in SCRIPT_PATH.parents if (parent / ".git").exists())
sys.pycache_prefix = str(REPOSITORY_ROOT / ".caprmedio_tmp/cache/python")
TOOLS_ROOT = SCRIPT_PATH.parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from artifact_metadata import (  # noqa: E402
    YAML_DELIMITER,
    TOML_DELIMITER,
    atomic_write,
    current_timestamp,
    insert_properties,
    one_value,
    property_line,
    replace_property,
    split_frontmatter,
)


CONTROL_ROOT = Path(".caprmedio")
ROLE_DIRECTORIES = {
    "01_concern",
    "02_analysis",
    "03_plan",
    "04_requirement",
    "05_method",
    "06_evaluation",
    "07_delivery",
    "09_ops",
}
ATOM_TYPES = {
    "analysis",
    "analysis_report",
    "evaluation",
    "atomic",
    "atomic_record",
    "concern",
    "constraint",
    "contract",
    "evaluation_case",
    "evaluation_plan",
    "evidence_record",
    "implementation_decision",
    "integration_decision",
    "method",
    "plan",
    "problem",
    "question",
    "requirement",
    "test_case",
    "test_plan",
    "version",
}
PROJECTION_TYPES = {
    "catalog",
    "development_backlog",
    "evergreen",
    "hub",
    "implementation_record",
    "maintained",
    "map",
    "specification",
}


@dataclass(frozen=True)
class Revision:
    path: Path
    desired: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="apply the migration")
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    return parser.parse_args()


def scalar(frontmatter: str, delimiter: str, name: str) -> str | None:
    value = one_value(frontmatter, delimiter, name)
    if value is None:
        return None
    return value.split("#", 1)[0].strip().strip('"')


def role_directory(path: Path) -> str | None:
    return next((part for part in path.parts if part in ROLE_DIRECTORIES), None)


def is_atom(path: Path, delimiter: str, frontmatter: str) -> bool:
    artifact_type = scalar(frontmatter, delimiter, "artifact_type")
    if artifact_type in PROJECTION_TYPES:
        return False
    if artifact_type in ATOM_TYPES:
        return True
    if artifact_type is not None:
        raise RuntimeError(f"{path}: unclassified artifact_type {artifact_type!r}")
    return path.name.startswith("CAPRMEDIO-") and role_directory(path) is not None


def is_legacy_atom_without_frontmatter(path: Path) -> bool:
    role = role_directory(path)
    return role in {"02_analysis", "05_method"} and any(
        token in path.name for token in ("-ANALYSIS-", "-DECISION-")
    )


def revised_frontmatter(frontmatter: str, delimiter: str, timestamp: str) -> str:
    version = one_value(frontmatter, delimiter, "version")
    updated_at = one_value(frontmatter, delimiter, "updated_at")
    if version is not None and updated_at is not None:
        return frontmatter
    if version is not None:
        if not version.isdigit() or int(version) < 1:
            raise RuntimeError(f"invalid Atom version: {version}")
        revised = replace_property(frontmatter, delimiter, "version", int(version) + 1)
        return insert_properties(revised, [property_line(delimiter, "updated_at", timestamp)])
    if updated_at is not None:
        revised = replace_property(frontmatter, delimiter, "updated_at", timestamp)
        return insert_properties(revised, [property_line(delimiter, "version", 1)])
    return insert_properties(
        frontmatter,
        [
            property_line(delimiter, "version", 1),
            property_line(delimiter, "updated_at", timestamp),
        ],
    )


def plan_revision(path: Path, timestamp: str) -> Revision | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith((f"{YAML_DELIMITER}\n", f"{TOML_DELIMITER}\n")):
        if not is_legacy_atom_without_frontmatter(path):
            return None
        desired = (
            f"{YAML_DELIMITER}\n"
            f"version: 1\n"
            f"updated_at: {timestamp}\n"
            f"{YAML_DELIMITER}\n"
            f"{text}"
        )
        return Revision(path, desired)
    delimiter, frontmatter, body = split_frontmatter(text, path)
    if delimiter not in {YAML_DELIMITER, TOML_DELIMITER} or not is_atom(path, delimiter, frontmatter):
        return None
    revised = revised_frontmatter(frontmatter, delimiter, timestamp)
    if revised == frontmatter:
        return None
    desired = f"{delimiter}\n{revised}\n{delimiter}\n{body}"
    return Revision(path, desired)


def candidate_paths(root: Path) -> list[Path]:
    control_root = root / CONTROL_ROOT
    paths = [
        path
        for path in control_root.rglob("CAPRMEDIO-*.md")
        if "000_caprmedio_framework" not in path.parts
    ]
    return sorted(paths)


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    timestamp = current_timestamp(root)
    revisions = [revision for path in candidate_paths(root) if (revision := plan_revision(path, timestamp))]
    print(f"atom_updates={len(revisions)} timestamp={timestamp} state={'pending' if revisions else 'applied'}")
    if args.apply:
        for revision in revisions:
            atomic_write(revision.path, revision.desired)
        remaining = [path for path in candidate_paths(root) if plan_revision(path, timestamp)]
        if remaining:
            raise RuntimeError(f"post-apply verification failed for {len(remaining)} carriers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
