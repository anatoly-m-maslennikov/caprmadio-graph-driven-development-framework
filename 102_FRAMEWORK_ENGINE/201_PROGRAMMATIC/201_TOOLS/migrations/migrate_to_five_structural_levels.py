#!/usr/bin/env python3
"""Retire the parallel REALIZATION, RELEASES, and FIELD structural branches.

Parameters:
    root: repository root; defaults to the current directory.
    --apply: persist the migration; omission is a dry run.
    --session-id: required provenance for an applied migration.

The migration preserves retired carriers under project-level lifecycle archives,
removes only verified-empty obsolete scope directories, and creates the new
SPEC RELEASES Feature directory. Semantic authority changes remain in RMED
Atoms and are intentionally outside this mechanical migration.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPOSITORY_ROOT = next(parent for parent in SCRIPT_PATH.parents if (parent / ".git").exists())
sys.pycache_prefix = str(REPOSITORY_ROOT / ".caprmedio_tmp/cache/python")
TOOLS_ROOT = SCRIPT_PATH.parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from artifact_metadata import repository_root  # noqa: E402
from work_journal import append_record, event_record  # noqa: E402


FILE_MOVES = (
    (
        Path(".caprmedio/04_requirement/CAPRMEDIO-REQU-039--define-the-six-layer-project-structure.md"),
        Path(".caprmedio/04_requirement/archive/CAPRMEDIO-REQU-039--define-the-six-layer-project-structure.md"),
    ),
    (
        Path(".caprmedio/04_requirement/CAPRMEDIO-REQU-606--define-realization-layer-scope.md"),
        Path(".caprmedio/04_requirement/archive/CAPRMEDIO-REQU-606--define-realization-layer-scope.md"),
    ),
    (
        Path(".caprmedio/04_requirement/CAPRMEDIO-REQU-607--define-releases-layer-scope.md"),
        Path(".caprmedio/04_requirement/archive/CAPRMEDIO-REQU-607--define-releases-layer-scope.md"),
    ),
    (
        Path(".caprmedio/04_requirement/CAPRMEDIO-REQU-608--define-field-layer-scope.md"),
        Path(".caprmedio/04_requirement/archive/CAPRMEDIO-REQU-608--define-field-layer-scope.md"),
    ),
    (
        Path(".caprmedio/04_requirement/CAPRMEDIO-CNTR-013--supply-cumulative-authority-to-releases.md"),
        Path(".caprmedio/04_requirement/archive/CAPRMEDIO-CNTR-013--supply-cumulative-authority-to-releases.md"),
    ),
    (
        Path(".caprmedio/04_requirement/CAPRMEDIO-CNTR-014--supply-cumulative-authority-to-field.md"),
        Path(".caprmedio/04_requirement/archive/CAPRMEDIO-CNTR-014--supply-cumulative-authority-to-field.md"),
    ),
    (
        Path(".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-089--current-layer-handoffs.md"),
        Path(".caprmedio/100_LAYER_1_META/04_requirement/archive/CAPRMEDIO-META-REQU-089--current-layer-handoffs.md"),
    ),
    (
        Path(".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-610--keep-applied-realization-layer-flat.md"),
        Path(".caprmedio/200_LAYER_2_GOV/04_requirement/archive/CAPRMEDIO-GOV-REQU-610--keep-applied-realization-layer-flat.md"),
    ),
    (
        Path(".caprmedio/200_LAYER_2_GOV/06_evaluation/CAPRMEDIO-GOV-EVAL-004--current-scope-and-layer-distinction.md"),
        Path(".caprmedio/200_LAYER_2_GOV/06_evaluation/archive/CAPRMEDIO-GOV-EVAL-004--current-scope-and-layer-distinction.md"),
    ),
    (
        Path(".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-CATL-003--methodology-projection-set.md"),
        Path(".caprmedio/200_LAYER_2_GOV/04_requirement/archive/CAPRMEDIO-GOV-CATL-003--methodology-projection-set.md"),
    ),
    (
        Path(".caprmedio/CAPRMEDIO-CONTROL-HUB.md"),
        Path(".caprmedio/08_implementation/archive/CAPRMEDIO-CONTROL-HUB.md"),
    ),
    (
        Path(".caprmedio/08_implementation/CAPRMEDIO-CATL-001--project-settings.md"),
        Path(".caprmedio/08_implementation/archive/CAPRMEDIO-CATL-001--project-settings.md"),
    ),
)

DIRECTORY_MOVES = (
    (
        Path(".caprmedio/400_LAYER_4_REALIZATION"),
        Path(".caprmedio/08_implementation/archive/400_LAYER_4_REALIZATION"),
    ),
    (
        Path(".caprmedio/600_LAYER_6_FIELD"),
        Path(".caprmedio/09_ops/archive/600_LAYER_6_FIELD"),
    ),
)

EMPTY_DIRECTORIES = (
    Path(".caprmedio/401_FEATURE_METHODOLOGY"),
    Path(".caprmedio/402_FEATURE_TOOLS"),
    Path(".caprmedio/403_FEATURE_SKILLS"),
    Path(".caprmedio/404_FEATURE_PROFILES"),
    Path(".caprmedio/405_FEATURE_ADAPTERS"),
    Path(".caprmedio/406_FEATURE_EVALUATION"),
    Path(".caprmedio/407_FEATURE_DOCUMENTATION"),
    Path(".caprmedio/500_LAYER_5_RELEASES"),
)

CREATED_DIRECTORIES = (Path(".caprmedio/308_FEATURE_RELEASES"),)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--session-id")
    return parser.parse_args()


def pending_moves(
    root: Path, moves: tuple[tuple[Path, Path], ...]
) -> list[tuple[Path, Path]]:
    pending: list[tuple[Path, Path]] = []
    for relative_source, relative_destination in moves:
        source = root / relative_source
        destination = root / relative_destination
        if source.exists() and destination.exists():
            raise RuntimeError(
                f"both source and destination exist: {relative_source}, "
                f"{relative_destination}"
            )
        if source.exists():
            pending.append((source, destination))
        elif not destination.exists():
            raise RuntimeError(
                f"missing source and destination: {relative_source}, "
                f"{relative_destination}"
            )
    return pending


def verify_empty_directories(root: Path) -> list[Path]:
    pending: list[Path] = []
    for relative in EMPTY_DIRECTORIES:
        path = root / relative
        if not path.exists():
            continue
        children = list(path.iterdir())
        if children:
            raise RuntimeError(f"refusing to remove non-empty directory: {relative}")
        pending.append(path)
    return pending


def main() -> int:
    args = parse_args()
    root = repository_root(Path(args.root))
    if args.apply and not args.session_id:
        raise RuntimeError("--session-id is required with --apply")

    file_moves = pending_moves(root, FILE_MOVES)
    directory_moves = pending_moves(root, DIRECTORY_MOVES)
    empty_directories = verify_empty_directories(root)
    created_directories = [
        root / path for path in CREATED_DIRECTORIES if not (root / path).is_dir()
    ]

    print(f"file_moves={len(file_moves)}")
    print(f"directory_moves={len(directory_moves)}")
    print(f"empty_directories_removed={len(empty_directories)}")
    print(f"directories_created={len(created_directories)}")
    for source, destination in (*file_moves, *directory_moves):
        print(
            f"move {source.relative_to(root)} -> "
            f"{destination.relative_to(root)}"
        )

    if not args.apply:
        return 0

    for source, destination in file_moves:
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.rename(destination)
    for source, destination in directory_moves:
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.rename(destination)
    for path in empty_directories:
        path.rmdir()
    for path in created_directories:
        path.mkdir(parents=True)

    record = event_record(
        root=root,
        event="completed",
        action_id="migrate-to-five-structural-levels-20260818",
        kind="structural_migration",
        scope="project",
        operation="migrate_to_five_structural_levels",
        session_id=args.session_id,
        subjects=[
            source.relative_to(root).as_posix()
            for source, _ in (*file_moves, *directory_moves)
        ],
        outputs=[
            destination.relative_to(root).as_posix()
            for _, destination in (*file_moves, *directory_moves)
        ],
        preceding_event=None,
        details={
            "file_moves": str(len(file_moves)),
            "directory_moves": str(len(directory_moves)),
            "empty_directories_removed": str(len(empty_directories)),
            "directories_created": str(len(created_directories)),
        },
    )
    journal = append_record(root, record)
    print(f"journal={journal.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
