#!/usr/bin/env python3
"""Place the Principle tier before the Type in Project Principle filenames.

Dry-run is the default. Pass --apply to back up affected files, rename the
15 active Project Principles, and rewrite active frontmatter references.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import sys
from pathlib import Path

_PROJECT_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402


CONTROL_ROOT = Path(".caprmedio")
RUNTIME_ROOT = Path(
    ".caprmedio_runtime/migrations/reorder_project_principle_filename_segments"
)

ENTRIES = (
    ("04_requirement", "CA-R-001-REQUIREMENT-PRINCIPLE--the-graph-is-the-operating-model", "CA-R-001-PRINCIPLE-REQUIREMENT--the-graph-is-the-operating-model"),
    ("04_requirement", "CA-R-002-REQUIREMENT-PRINCIPLE--necessary-complexity-only", "CA-R-002-PRINCIPLE-REQUIREMENT--necessary-complexity-only"),
    ("04_requirement", "CA-R-003-REQUIREMENT-PRINCIPLE--preserve-discipline-independent-semantics", "CA-R-003-PRINCIPLE-REQUIREMENT--preserve-discipline-independent-semantics"),
    ("04_requirement", "CA-R-004-REQUIREMENT-PRINCIPLE--operator-acceptance-establishes-project-authority", "CA-R-004-PRINCIPLE-REQUIREMENT--operator-acceptance-establishes-project-authority"),
    ("04_requirement", "CA-R-005-REQUIREMENT-PRINCIPLE--organize-authority-as-a-hierarchical-graph", "CA-R-005-PRINCIPLE-REQUIREMENT--organize-authority-as-a-hierarchical-graph"),
    ("04_requirement", "CA-R-006-REQUIREMENT-PRINCIPLE--make-governed-meaning-humanly-understandable", "CA-R-006-PRINCIPLE-REQUIREMENT--make-governed-meaning-humanly-understandable"),
    ("05_method", "CA-M-001-METHOD-PRINCIPLE--mece-for-canonical-decompositions", "CA-M-001-PRINCIPLE-METHOD--mece-for-canonical-decompositions"),
    ("05_method", "CA-M-002-METHOD-PRINCIPLE--apply-dry-across-caprmedio", "CA-M-002-PRINCIPLE-METHOD--apply-dry-across-caprmedio"),
    ("05_method", "CA-M-003-METHOD-PRINCIPLE--scale-through-structure", "CA-M-003-PRINCIPLE-METHOD--scale-through-structure"),
    ("06_evaluation", "CA-E-001-EVALUATION-PRINCIPLE--make-accepted-requirements-checkable", "CA-E-001-PRINCIPLE-EVALUATION--make-accepted-requirements-checkable"),
    ("06_evaluation", "CA-E-002-EVALUATION-PRINCIPLE--require-explicit-reliance-boundaries", "CA-E-002-PRINCIPLE-EVALUATION--require-explicit-reliance-boundaries"),
    ("07_delivery", "CA-D-001-DELIVERY-PRINCIPLE--keep-realizations-replaceable-across-technical-substrates", "CA-D-001-PRINCIPLE-DELIVERY--keep-realizations-replaceable-across-technical-substrates"),
    ("09_ops", "CA-O-001-OPS-PRINCIPLE--govern-capability-evolution-through-extensions", "CA-O-001-PRINCIPLE-OPS--govern-capability-evolution-through-extensions"),
    ("09_ops", "CA-O-002-OPS-PRINCIPLE--govern-capability-selection-through-configuration", "CA-O-002-PRINCIPLE-OPS--govern-capability-selection-through-configuration"),
    ("09_ops", "CA-O-003-OPS-PRINCIPLE--improve-from-observed-outcomes", "CA-O-003-PRINCIPLE-OPS--improve-from-observed-outcomes"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="apply the migration")
    return parser.parse_args()


def repository_root() -> Path:
    root = Path.cwd().resolve()
    if (root / CONTROL_ROOT).is_dir() and (
        root / "caprmedio_framework_settings.toml"
    ).is_file():
        return root
    raise RuntimeError("run from the CAPRMEDIO repository root")


def split_frontmatter(text: str, path: Path) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise RuntimeError(f"{path}: missing YAML frontmatter")
    boundary = text.find("\n---\n", 4)
    if boundary < 0:
        raise RuntimeError(f"{path}: unterminated YAML frontmatter")
    return text[4:boundary], text[boundary + 5 :]


def active_markdown(root: Path) -> list[Path]:
    paths = []
    for path in (root / CONTROL_ROOT).rglob("*.md"):
        relative = path.relative_to(root / CONTROL_ROOT)
        if "archive" in relative.parts:
            continue
        paths.append(path)
    return sorted(paths)


def atomic_write(path: Path, text: str) -> None:
    descriptor, temporary = atomic_tempfile(path, "migrations")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def migration_state(root: Path) -> str:
    old_exists = [
        (root / CONTROL_ROOT / folder / f"{old}.md").is_file()
        for folder, old, _ in ENTRIES
    ]
    new_exists = [
        (root / CONTROL_ROOT / folder / f"{new}.md").is_file()
        for folder, _, new in ENTRIES
    ]
    if all(old_exists) and not any(new_exists):
        return "before"
    if not any(old_exists) and all(new_exists):
        return "after"
    raise RuntimeError("mixed Principle filename migration state; stop for recovery")


def planned_reference_updates(root: Path) -> dict[Path, str]:
    mapping = {old: new for _, old, new in ENTRIES}
    updates = {}
    for path in active_markdown(root):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        frontmatter, body = split_frontmatter(text, path)
        revised = frontmatter
        for old, new in mapping.items():
            revised = revised.replace(old, new)
        if revised != frontmatter:
            updates[path] = f"---\n{revised}\n---\n{body}"
    return updates


def validate_after(root: Path) -> None:
    old_stems = {old for _, old, _ in ENTRIES}
    for folder, old, new in ENTRIES:
        old_path = root / CONTROL_ROOT / folder / f"{old}.md"
        new_path = root / CONTROL_ROOT / folder / f"{new}.md"
        if old_path.exists() or not new_path.is_file():
            raise RuntimeError(f"incomplete rename: {old} -> {new}")
    for path in active_markdown(root):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        frontmatter, _ = split_frontmatter(text, path)
        for old in old_stems:
            if old in frontmatter:
                raise RuntimeError(f"{path}: stale active reference to {old}")


def apply(root: Path, updates: dict[Path, str]) -> Path:
    timestamp = dt.datetime.now().astimezone()
    backup_root = root / RUNTIME_ROOT / timestamp.strftime("%Y%m%dT%H%M%S%z")
    if backup_root.exists():
        raise RuntimeError(f"backup target already exists: {backup_root}")

    source_paths = [
        root / CONTROL_ROOT / folder / f"{old}.md"
        for folder, old, _ in ENTRIES
    ]
    for path in sorted(set(source_paths) | set(updates)):
        destination = backup_root / "files" / path.relative_to(root)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)

    manifest = {
        "created_at": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "migration": "reorder_project_principle_filename_segments",
        "renames": [
            {"from": old, "to": new} for _, old, new in ENTRIES
        ],
        "reference_files": [
            str(path.relative_to(root)) for path in sorted(updates)
        ],
    }
    atomic_write(
        backup_root / "manifest.json",
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
    )

    for path, text in updates.items():
        atomic_write(path, text)
    for folder, old, new in ENTRIES:
        source = root / CONTROL_ROOT / folder / f"{old}.md"
        target = root / CONTROL_ROOT / folder / f"{new}.md"
        if target.exists():
            raise RuntimeError(f"target collision: {target}")
        os.replace(source, target)

    validate_after(root)
    return backup_root


def main() -> int:
    args = parse_args()
    root = repository_root()
    state = migration_state(root)
    if state == "after":
        validate_after(root)
        print("state=after status=valid action=none")
        return 0

    updates = planned_reference_updates(root)
    print(f"state=before principles={len(ENTRIES)} reference_files={len(updates)}")
    if not args.apply:
        print("status=dry-run action=rerun-with---apply")
        return 0

    backup_root = apply(root, updates)
    print(f"status=applied backup={backup_root.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
