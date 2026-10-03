#!/usr/bin/env python3
"""Consolidate five narrow SPEC Cores beneath two complete behavior Cores.

Usage:
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/consolidate_spec_behavior_cores.py
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/consolidate_spec_behavior_cores.py --apply

The default mode is read-only. The migration is fail-closed, atomic per file,
and idempotent.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

_PROJECT_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402


SPEC_REQUIREMENTS = Path(".caprmedio/300_LAYER_3_SPEC/04_requirement")
SESSION_ID = "codex:019f591f-04f6-70f2-8de7-828b7cccc69d"
DISCIPLINE_PRINCIPLE = "CAPRMEDIO-REQU-013--preserve-discipline-independent-semantics"
SUBSTRATE_PRINCIPLE = "CAPRMEDIO-REQU-012--replaceable-substrates"
DISCIPLINE_CORE = "CAPRMEDIO-SPEC-REQU-505--govern-discipline-profile-applicability"
SUBSTRATE_CORE = "CAPRMEDIO-SPEC-REQU-506--govern-substrate-neutral-framework-behavior"
REPARENT = {
    "CAPRMEDIO-SPEC-REQU-492--default-to-software-application-development.md": (
        DISCIPLINE_PRINCIPLE,
        DISCIPLINE_CORE,
    ),
    "CAPRMEDIO-SPEC-REQU-493--support-portable-execution-platforms.md": (
        SUBSTRATE_PRINCIPLE,
        SUBSTRATE_CORE,
    ),
    "CAPRMEDIO-SPEC-REQU-494--support-any-operator-language.md": (
        SUBSTRATE_PRINCIPLE,
        SUBSTRATE_CORE,
    ),
    "CAPRMEDIO-SPEC-REQU-495--support-any-implementation-language.md": (
        SUBSTRATE_PRINCIPLE,
        SUBSTRATE_CORE,
    ),
    "CAPRMEDIO-SPEC-REQU-496--keep-llm-operation-provider-neutral.md": (
        SUBSTRATE_PRINCIPLE,
        SUBSTRATE_CORE,
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="apply the migration")
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    return parser.parse_args()


def core_carrier(subject_scope: str, title: str, parent: str, claim: str) -> str:
    return (
        "---\n"
        "subject_scopes:\n"
        f"  - {subject_scope}\n"
        "tier: core\n"
        "llm_session_ids:\n"
        f"  - {SESSION_ID}\n"
        "relations:\n"
        "  child_of:\n"
        f"    - {parent}\n"
        "---\n"
        f"# {title}\n\n"
        f"{claim}\n"
    )


def desired_cores(root: Path) -> dict[Path, str]:
    directory = root / SPEC_REQUIREMENTS
    return {
        directory / f"{DISCIPLINE_CORE}.md": core_carrier(
            "applicability",
            "Govern discipline profile applicability",
            DISCIPLINE_PRINCIPLE,
            "SPEC governs how a selected discipline Profile adapts canonical CAPRMEDIO semantics without redefining those semantics.",
        ),
        directory / f"{SUBSTRATE_CORE}.md": core_carrier(
            "portability",
            "Govern substrate neutral framework behavior",
            SUBSTRATE_PRINCIPLE,
            "SPEC governs CAPRMEDIO behavior across replaceable execution platforms, operator languages, Implementation languages, LLM providers, models, and agent hosts.",
        ),
    }


def migrated_standard(text: str, old_parent: str, new_parent: str, path: Path) -> str:
    tier_line = "tier: core\n"
    old_line = f"    - {old_parent}\n"
    new_line = f"    - {new_parent}\n"
    if text.count(tier_line) != 1:
        raise RuntimeError(f"{path}: expected exactly one Core tier")
    if text.count(old_line) != 1:
        raise RuntimeError(f"{path}: expected exactly one old parent")
    return text.replace(tier_line, "", 1).replace(old_line, new_line, 1)


def desired_standards(root: Path) -> dict[Path, str]:
    desired: dict[Path, str] = {}
    for filename, (old_parent, new_parent) in REPARENT.items():
        path = root / SPEC_REQUIREMENTS / filename
        if not path.is_file():
            raise RuntimeError(f"missing source carrier: {path}")
        desired[path] = migrated_standard(path.read_text(encoding="utf-8"), old_parent, new_parent, path)
    return desired


def detect_state(root: Path, cores: dict[Path, str]) -> str:
    core_state = [path.read_text(encoding="utf-8") == text if path.is_file() else False for path, text in cores.items()]
    standards = [root / SPEC_REQUIREMENTS / filename for filename in REPARENT]
    old_state = all("\ntier: core\n" in path.read_text(encoding="utf-8") for path in standards)
    new_state = all("\ntier: core\n" not in path.read_text(encoding="utf-8") for path in standards)
    new_parents = all(
        f"    - {new_parent}\n" in (root / SPEC_REQUIREMENTS / filename).read_text(encoding="utf-8")
        for filename, (_, new_parent) in REPARENT.items()
    )
    if not any(core_state) and old_state:
        return "pending"
    if all(core_state) and new_state and new_parents:
        return "applied"
    raise RuntimeError("mixed or unexpected migration state")


def atomic_write(path: Path, text: str) -> None:
    descriptor, temporary_name = atomic_tempfile(path, "migrations")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def apply_migration(root: Path, cores: dict[Path, str]) -> None:
    standards = desired_standards(root)
    for path, text in {**cores, **standards}.items():
        atomic_write(path, text)


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    cores = desired_cores(root)
    state = detect_state(root, cores)
    changes = 0 if state == "applied" else len(cores) + len(REPARENT)
    print(f"state={state} new_cores={len(cores)} standards={len(REPARENT)} changes={changes}")
    if args.apply and state == "pending":
        apply_migration(root, cores)
        if detect_state(root, cores) != "applied":
            raise RuntimeError("post-apply verification failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
