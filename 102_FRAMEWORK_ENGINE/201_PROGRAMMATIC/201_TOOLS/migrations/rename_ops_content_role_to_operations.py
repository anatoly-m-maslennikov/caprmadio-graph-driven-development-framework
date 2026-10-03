#!/usr/bin/env python3
"""Rename the current Ops Content Role to Operations.

The migration is deliberately narrow:

* revise active Markdown Atom carriers that use the retired role name;
* preserve each previous active revision in the nearest role archive;
* rename only current ``09_ops`` role directories;
* leave archives, Plans, Analysis, Concerns, drafts, Journals, generated
  Applicable Methodology copies, and Implementation evidence unchanged.

Atom IDs and the Content Role identity letter ``O`` are preserved.
"""

from __future__ import annotations

import argparse
import os
import re
from datetime import datetime
from pathlib import Path


CONTROL_ROOT = Path(".caprmedio_caprmedio")
METHODOLOGY_ROOT = CONTROL_ROOT / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
SOURCE_ROOT = METHODOLOGY_ROOT / "000_APPLICABLE_MTHD_sources"
EXCLUDED_PARTS = {
    "archive",
    "drafts",
    "01_concern",
    "02_analysis",
    "03_plan",
    "08_implementation",
    "work_journal",
    "done",
    "canceled",
    "cancelled",
}
ROLE_DIRECTORY = re.compile(r"^0[1-9]_[a-z0-9_]+$")
VERSION = re.compile(r"(?m)^version:\s*([0-9]+)\s*$")
UPDATED_AT = re.compile(r"(?m)^updated_at:\s*.*$")
ATOM_ID = re.compile(r"(?m)^atom_id:\s*(.+?)\s*$")
RETIRED_TERM = re.compile(r"\b(?:Ops|OPS|ops)\b|09_ops|ops:")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--apply", action="store_true")
    return parser.parse_args()


def repository_root(start: Path) -> Path:
    resolved = start.resolve()
    for candidate in (resolved, *resolved.parents):
        if (candidate / ".git").exists():
            return candidate
    raise RuntimeError(f"cannot find repository root from {start}")


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def is_generated_projection(path: Path) -> bool:
    try:
        relative = path.relative_to(METHODOLOGY_ROOT)
    except ValueError:
        return False
    return not relative.parts or relative.parts[0] != "000_APPLICABLE_MTHD_sources"


def active_atom_candidates(root: Path) -> list[Path]:
    control = root / CONTROL_ROOT
    candidates: list[Path] = []
    for path in sorted(control.rglob("*.md")):
        relative = path.relative_to(root)
        if is_excluded(relative) or is_generated_projection(relative):
            continue
        text = path.read_text(encoding="utf-8")
        has_role_directory = any(ROLE_DIRECTORY.fullmatch(part) for part in relative.parts)
        if text.startswith("---\n") and has_role_directory and VERSION.search(text) and RETIRED_TERM.search(text):
            candidates.append(path)
    return candidates


def role_archive(path: Path) -> Path:
    role = next((parent for parent in path.parents if ROLE_DIRECTORY.fullmatch(parent.name)), None)
    if role is None:
        raise RuntimeError(f"active Atom has no Content Role directory: {path}")
    return role / "archive"


def renamed_summary(name: str) -> str:
    head, separator, summary = name.partition("--")
    if not separator:
        raise RuntimeError(f"Atom filename has no summary separator: {name}")
    summary = re.sub(r"(?<![a-z])ops(?![a-z])", "operations", summary)
    return head + separator + summary


def revised_text(text: str, timestamp: str) -> tuple[str, int]:
    matches = VERSION.findall(text)
    if len(matches) != 1:
        raise RuntimeError("active Atom must have exactly one integer version")
    old_version = int(matches[0])
    atom_id = ATOM_ID.search(text)
    revised = text.replace("09_ops", "09_operations")
    revised = re.sub(r"\bOps\b", "Operations", revised)
    revised = re.sub(r"\bOPS\b", "OPERATIONS", revised)
    revised = re.sub(r"\bops\b", "operations", revised)
    revised = revised.replace("Operations (Operations, identity letter O)", "Operations (identity letter O)")
    if atom_id:
        revised = ATOM_ID.sub(f"atom_id: {atom_id.group(1)}", revised, count=1)
    revised = VERSION.sub(f"version: {old_version + 1}", revised, count=1)
    if len(UPDATED_AT.findall(revised)) != 1:
        raise RuntimeError("active Atom must have exactly one updated_at")
    revised = UPDATED_AT.sub(f"updated_at: {timestamp}", revised, count=1)
    return revised, old_version


def current_role_directories(root: Path) -> list[Path]:
    control = root / CONTROL_ROOT
    return sorted(
        (
            path
            for path in control.rglob("09_ops")
            if path.is_dir()
            and not is_excluded(path.relative_to(root).parent)
            and any(child.is_file() and child.name != ".DS_Store" for child in path.rglob("*"))
        ),
        key=lambda path: len(path.parts),
        reverse=True,
    )


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.operations-migration.tmp")
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, path)


def main() -> int:
    args = parse_args()
    root = repository_root(Path(args.root))
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
    atom_plans: list[tuple[Path, Path, Path, str, str]] = []
    for source in active_atom_candidates(root):
        original = source.read_text(encoding="utf-8")
        revised, old_version = revised_text(original, timestamp)
        archive = role_archive(source) / f"{source.stem}@{old_version}{source.suffix}"
        destination = source.with_name(renamed_summary(source.name))
        if archive.exists():
            raise RuntimeError(f"archive revision already exists: {archive.relative_to(root)}")
        if destination != source and destination.exists():
            raise RuntimeError(f"renamed active carrier already exists: {destination.relative_to(root)}")
        atom_plans.append((source, destination, archive, original, revised))

    directory_plans = [(path, path.with_name("09_operations")) for path in current_role_directories(root)]
    for source, destination in directory_plans:
        for path in source.rglob("*"):
            if path.is_file() and (destination / path.relative_to(source)).exists():
                raise RuntimeError(
                    "role directory destination already contains source path: "
                    f"{(destination / path.relative_to(source)).relative_to(root)}"
                )

    print(f"atom_revisions={len(atom_plans)}")
    print(f"role_directory_renames={len(directory_plans)}")
    for source, destination, _, _, _ in atom_plans:
        print(f"atom {source.relative_to(root)} -> {destination.relative_to(root)}")
    for source, destination in directory_plans:
        print(f"directory {source.relative_to(root)} -> {destination.relative_to(root)}")
    if not args.apply:
        return 0

    for source, destination, archive, original, revised in atom_plans:
        atomic_write(archive, original)
        atomic_write(destination, revised)
        if destination != source:
            source.unlink()
    for source, destination in directory_plans:
        destination.mkdir(parents=True, exist_ok=True)
        for directory in sorted((path for path in source.rglob("*") if path.is_dir()), key=lambda path: len(path.parts)):
            (destination / directory.relative_to(source)).mkdir(parents=True, exist_ok=True)
        for path in sorted(path for path in source.rglob("*") if path.is_file()):
            path.rename(destination / path.relative_to(source))
        for directory in sorted((path for path in source.rglob("*") if path.is_dir()), key=lambda path: len(path.parts), reverse=True):
            try:
                directory.rmdir()
            except OSError:
                pass
        try:
            source.rmdir()
        except OSError:
            # Some macOS hosts retain an empty provenance-protected directory.
            # Git has no directory object, so the repository migration is still
            # complete once every tracked carrier moved to the destination.
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
