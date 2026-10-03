#!/usr/bin/env python3
"""Rename CAPRMEDIO structural units without renaming Content roles.

Parameters:
    root: repository root; defaults to the current directory.
    --apply: persist the migration; omission is a dry run.
    --session-id: required provenance for an applied migration.

The migration renames the three structural directories, migrates structural
scope prefixes in carrier filenames, and rewrites exact filename/path
references outside append-only Journals. It deliberately leaves the Delivery,
Implementation, and Ops Content-role vocabulary unchanged.
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPOSITORY_ROOT = next(parent for parent in SCRIPT_PATH.parents if (parent / ".git").exists())
sys.pycache_prefix = str(REPOSITORY_ROOT / ".caprmedio_tmp/cache/python")
TOOLS_ROOT = SCRIPT_PATH.parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from artifact_metadata import repository_root  # noqa: E402
from work_journal import append_record, event_record  # noqa: E402


TEXT_SUFFIXES = {
    ".cfg", ".ini", ".json", ".jsonl", ".md", ".py", ".sh",
    ".toml", ".txt", ".yaml", ".yml",
}
EXCLUDED_TEXT_PARTS = {".git", ".f4f", ".caprmedio_runtime", "010_journals"}
THIS_SCRIPT = Path("002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/rename_caprmedio_structural_units.py")


@dataclass(frozen=True)
class StructuralRename:
    source: Path
    destination: Path
    scope_prefixes: tuple[str, ...]
    destination_scope_prefix: str


STRUCTURAL_RENAMES = (
    StructuralRename(
        Path(".caprmedio/400_LAYER_4_IMPLEMENTATION"),
        Path(".caprmedio/400_LAYER_4_REALIZATION"),
        ("CAPRMEDIO-IMPLEMENTATION-", "CAPRMEDIO-IMPL-"),
        "CAPRMEDIO-REALIZATION-",
    ),
    StructuralRename(
        Path(".caprmedio/500_LAYER_5_DELIVERY"),
        Path(".caprmedio/500_LAYER_5_RELEASES"),
        ("CAPRMEDIO-DELIVERY-",),
        "CAPRMEDIO-RELEASES-",
    ),
    StructuralRename(
        Path(".caprmedio/600_LAYER_6_OPS"),
        Path(".caprmedio/600_LAYER_6_FIELD"),
        ("CAPRMEDIO-OPS-",),
        "CAPRMEDIO-FIELD-",
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--session-id")
    return parser.parse_args()


def renamed_filename(name: str, rename: StructuralRename) -> str:
    for prefix in rename.scope_prefixes:
        if name.startswith(prefix):
            return rename.destination_scope_prefix + name[len(prefix):]
    return name


def discover_carrier_renames(
    root: Path,
) -> tuple[list[tuple[Path, Path]], dict[str, str]]:
    moves: list[tuple[Path, Path]] = []
    identity_replacements: dict[str, str] = {}
    for rename in STRUCTURAL_RENAMES:
        source_root = root / rename.source
        destination_root = root / rename.destination
        if source_root.exists() and destination_root.exists():
            raise RuntimeError(
                f"both structural directories exist: {rename.source}, {rename.destination}"
            )
        active_root = source_root if source_root.exists() else destination_root
        if not active_root.exists():
            raise RuntimeError(f"missing structural directory: {rename.source}")
        for source in sorted(path for path in active_root.rglob("*") if path.is_file()):
            new_name = renamed_filename(source.name, rename)
            if new_name == source.name:
                continue
            destination = source.with_name(new_name)
            if destination.exists():
                raise RuntimeError(
                    f"carrier destination already exists: {destination.relative_to(root)}"
                )
            moves.append((source, destination))
            identity_replacements[source.stem] = destination.stem
    if len(identity_replacements) != len(moves):
        raise RuntimeError("duplicate structural identity replacement")
    return moves, identity_replacements


def text_candidates(root: Path) -> list[Path]:
    candidates: list[Path] = []
    for path in sorted(root.rglob("*")):
        if (
            not path.is_file()
            or path.is_symlink()
            or path.suffix.lower() not in TEXT_SUFFIXES
        ):
            continue
        relative = path.relative_to(root)
        if relative == THIS_SCRIPT:
            continue
        if any(part in EXCLUDED_TEXT_PARTS for part in relative.parts):
            continue
        candidates.append(path)
    return candidates


def rewrite_text(text: str, identity_replacements: dict[str, str]) -> str:
    revised = text
    for old, new in sorted(
        identity_replacements.items(), key=lambda item: -len(item[0])
    ):
        revised = revised.replace(old, new)
    for rename in STRUCTURAL_RENAMES:
        revised = revised.replace(rename.source.as_posix(), rename.destination.as_posix())
    return revised


def atomic_write(path: Path, text: str) -> None:
    temporary = path.with_name(f".{path.name}.caprmedio-rename.tmp")
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, path)


def migrated_path(
    path: Path,
    directory_moves: list[tuple[Path, Path]],
    carrier_moves: list[tuple[Path, Path]],
) -> Path:
    for source, destination in carrier_moves:
        if path == source:
            path = destination
            break
    for source, destination in directory_moves:
        try:
            relative = path.relative_to(source)
        except ValueError:
            continue
        return destination / relative
    return path


def main() -> int:
    args = parse_args()
    root = repository_root(Path(args.root))
    if args.apply and not args.session_id:
        raise RuntimeError("--session-id is required with --apply")

    carrier_moves, identity_replacements = discover_carrier_renames(root)
    text_changes: dict[Path, str] = {}
    for path in text_candidates(root):
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        revised = rewrite_text(original, identity_replacements)
        if revised != original:
            text_changes[path] = revised

    directory_moves = [
        (root / rename.source, root / rename.destination)
        for rename in STRUCTURAL_RENAMES
        if (root / rename.source).exists()
    ]
    print(f"directory_moves={len(directory_moves)}")
    print(f"carrier_moves={len(carrier_moves)}")
    print(f"text_changes={len(text_changes)}")
    for source, destination in directory_moves:
        print(f"directory {source.relative_to(root)} -> {destination.relative_to(root)}")
    for source, destination in carrier_moves[:20]:
        print(f"carrier {source.relative_to(root)} -> {destination.relative_to(root)}")

    if not args.apply:
        return 0

    for source, destination in carrier_moves:
        source.rename(destination)
    for source, destination in directory_moves:
        source.rename(destination)
    for original_path, revised in text_changes.items():
        atomic_write(migrated_path(original_path, directory_moves, carrier_moves), revised)

    record = event_record(
        root=root,
        event="completed",
        action_id="rename-caprmedio-structural-units-20260818",
        kind="structural_migration",
        scope="project",
        operation="rename_structural_units",
        session_id=args.session_id,
        subjects=[rename.source.as_posix() for rename in STRUCTURAL_RENAMES],
        outputs=[rename.destination.as_posix() for rename in STRUCTURAL_RENAMES],
        preceding_event=None,
        details={
            "carrier_moves": str(len(carrier_moves)),
            "text_changes": str(len(text_changes)),
        },
    )
    journal = append_record(root, record)
    print(f"journal={journal.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
