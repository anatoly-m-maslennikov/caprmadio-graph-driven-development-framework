#!/usr/bin/env python3
"""Move the tier -1 Project Goal carrier to the CAPRMEDIO control root.

Dry-run is the default. The migration preserves the Goal carrier bytes and
identity, updates the governing semantic and placement Requirements, and
removes the obsolete empty ``00_goal`` directory.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from uuid import uuid4

_PROJECT_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402


SESSION_ID = "codex:019f591f-04f6-70f2-8de7-828b7cccc69d"
GOAL_NAME = "CAPRMEDIO-GOAL-001--enable-any-operator-to-build-a-working-system.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--updated-at", help="YYYY-MM-DD HH:MM:SS; defaults to local time")
    parser.add_argument("--session-id", default=SESSION_ID)
    return parser.parse_args()


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "migrations")
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise


def replace_once(text: str, old: str, new: str, path: Path) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new)
    if count == 0 and new in text:
        return text
    raise ValueError(f"{path}: expected one old value, found {count}: {old!r}")


def set_revision(text: str, version: int, updated_at: str, path: Path) -> str:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise ValueError(f"{path}: expected YAML frontmatter")
    closing = next((index for index, line in enumerate(lines[1:], 1) if line.rstrip("\r\n") == "---"), None)
    if closing is None:
        raise ValueError(f"{path}: unterminated YAML frontmatter")
    version_indices = [index for index in range(1, closing) if lines[index].startswith("version:")]
    updated_indices = [index for index in range(1, closing) if lines[index].startswith("updated_at:")]
    if len(version_indices) != 1 or len(updated_indices) != 1:
        raise ValueError(f"{path}: expected one version and one updated_at")
    newline = "\r\n" if lines[version_indices[0]].endswith("\r\n") else "\n"
    lines[version_indices[0]] = f"version: {version}{newline}"
    lines[updated_indices[0]] = f"updated_at: {updated_at}{newline}"
    return "".join(lines)


def update_carrier(root: Path, relative: str, old: str, new: str, version: int, updated_at: str) -> tuple[Path, str] | None:
    path = root / relative
    original = path.read_text(encoding="utf-8")
    updated = replace_once(original, old, new, path)
    updated = set_revision(updated, version, updated_at, path)
    if updated == original:
        return None
    return path, updated


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    updated_at = args.updated_at or datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
    datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S")

    source = root / ".caprmedio/04_requirement" / GOAL_NAME
    destination = root / ".caprmedio" / GOAL_NAME
    obsolete_directory = root / ".caprmedio/00_goal"
    if source.exists() and destination.exists():
        raise ValueError("both source and destination Goal carriers exist")
    if not source.exists() and not destination.exists():
        raise ValueError("Goal carrier is missing")

    changes: dict[Path, str] = {}
    updates = [
        (
            ".caprmedio/04_requirement/CAPRMEDIO-REQU-609--assign-project-global-rmed-tier-numbers.md",
            "as Goal `-1`; Project Principle `0`",
            "as Goal `-1` outside Project structural level `0`; Project Principle `0`",
            2,
        ),
        (
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-155--classify-rmed-atoms-by-applicability-tier.md",
            "The Project Goal is a Requirement subtype outside the ordered applicability-tier catalog and occupies global tier `-1`.",
            "The Project Goal is a Requirement subtype outside both the ordered applicability-tier catalog and the Project structural hierarchy, and it occupies global tier `-1`.",
            7,
        ),
        (
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-321--register-caprmedio-atom-type-surface.md",
            "A Goal states the end the current Project exists to achieve, occupies Project scope, and resolves to global tier `-1`.",
            "A Goal states the end the current Project exists to achieve, precedes and sits outside Project structural scope, and resolves to global tier `-1`.",
            4,
        ),
    ]
    for relative, old, new, version in updates:
        change = update_carrier(root, relative, old, new, version, updated_at)
        if change:
            changes[change[0]] = change[1]

    placement_requirement = root / ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-615--place-project-goal-at-control-root.md"
    placement_text = f"""---
subject_scopes:
  - layout
version: 1
updated_at: {updated_at}
llm_session_ids:
  - {args.session_id}
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
    - CAPRMEDIO-GOV-REQU-348--use-canonical-carrier-address-as-authority
---
# Place the Project Goal at the control root

The singular active `requirement:goal` Atom must live directly in `.caprmedio`, outside every Project Content-role, Layer, and Feature directory.
"""
    if placement_requirement.exists():
        if placement_requirement.read_text(encoding="utf-8") != placement_text:
            raise ValueError(f"{placement_requirement}: existing Requirement differs from expected content")
    else:
        changes[placement_requirement] = placement_text

    hub = root / ".caprmedio/CAPRMEDIO-CONTROL-HUB.md"
    hub_original = hub.read_text(encoding="utf-8")
    hub_updated = replace_once(
        hub_original,
        "## Start here\n\n- `caprmedio_project_settings.toml` — generated Project settings.",
        f"## Start here\n\n- `{GOAL_NAME}` — tier `-1` Goal outside Project structural level `0`.\n- `caprmedio_project_settings.toml` — generated Project settings.",
        hub,
    )
    if hub_updated != hub_original:
        changes[hub] = hub_updated

    removable_obsolete_directory = obsolete_directory.exists() and not any(obsolete_directory.iterdir())
    if obsolete_directory.exists() and not removable_obsolete_directory:
        raise ValueError(f"{obsolete_directory}: expected an empty obsolete directory")

    summary = {
        "mode": "apply" if args.apply else "dry-run",
        "updated_at": updated_at,
        "file_changes": len(changes),
        "goal_move": source.exists(),
        "remove_empty_00_goal": removable_obsolete_directory,
    }
    print(json.dumps(summary, sort_keys=True))
    for path in sorted(changes):
        print(path.relative_to(root))
    if not args.apply:
        return 0
    if not changes and not source.exists() and not removable_obsolete_directory:
        return 0

    for path, text in changes.items():
        atomic_write(path, text)
    if source.exists():
        source.replace(destination)
    if removable_obsolete_directory:
        obsolete_directory.rmdir()

    journal = root / ".caprmedio/010_journals/src-work-journal-2026-08-18.ndjson"
    event = {
        "action_id": "move-project-goal-to-control-root-20260818",
        "event": "completed",
        "event_id": str(uuid4()),
        "governed_subjects": [
            "CAPRMEDIO-GOAL-001--enable-any-operator-to-build-a-working-system",
            "CAPRMEDIO-GOV-REQU-615--place-project-goal-at-control-root",
        ],
        "kind": "carrier_migration",
        "occurred_at": updated_at,
        "operation": "move_project_goal_to_control_root",
        "produced_outputs": [f".caprmedio/{GOAL_NAME}"],
        "schema_version": 1,
        "session_id": args.session_id,
        "structural_scope": "project",
    }
    with journal.open("a", encoding="utf-8", newline="") as handle:
        handle.write(json.dumps(event, separators=(",", ":"), sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
