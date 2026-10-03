#!/usr/bin/env python3
"""Replace Requirement-only Project Principles with role-specific RMEDO Principles.

Dry-run is the default. Pass --apply to:

1. back up every changed carrier under .caprmedio_runtime;
2. archive the 14 predecessor Requirement Principles;
3. create 14 CA-prefixed role-specific successor Principles;
4. rewrite active frontmatter references to the successor identities.

The unnumbered draft Principle candidate is intentionally outside this migration.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

_PROJECT_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402


CONTROL_ROOT = Path(".caprmedio")
RUNTIME_ROOT = Path(".caprmedio_runtime/migrations/rmedo_project_principles")
GOAL = "CAPRMEDIO-GOAL-001--enable-any-operator-to-build-a-working-system"


@dataclass(frozen=True)
class Principle:
    old_stem: str
    role_folder: str
    new_stem: str
    subject_scopes: tuple[str, ...]
    title: str
    body: str


PRINCIPLES = (
    Principle(
        "CAPRMEDIO-REQU-004--the-graph-is-the-operating-model",
        "04_requirement",
        "CA-R-001-PRINCIPLE-REQUIREMENT--the-graph-is-the-operating-model",
        ("principles",),
        "The graph is the operating model",
        "Every CAPRMEDIO governance operation must read or change the typed graph of "
        "operator-accepted meanings, realization bindings, and direct relations. "
        "The graph organizes authority but does not create it.",
    ),
    Principle(
        "CAPRMEDIO-REQU-005--necessary-complexity-only",
        "04_requirement",
        "CA-R-002-PRINCIPLE-REQUIREMENT--necessary-complexity-only",
        ("principles",),
        "Necessary complexity only",
        "CAPRMEDIO may admit or retain a mechanism only when existing mechanisms "
        "cannot preserve a required outcome or a material governed distinction.",
    ),
    Principle(
        "CAPRMEDIO-REQU-013--preserve-discipline-independent-semantics",
        "04_requirement",
        "CA-R-003-PRINCIPLE-REQUIREMENT--preserve-discipline-independent-semantics",
        ("principles",),
        "Preserve discipline-independent semantics",
        "CAPRMEDIO must maintain one discipline-independent canonical semantic model. "
        "Extensions and Project Adaptations may adapt terminology, Artifact Types, "
        "Methods, Evaluation, and Implementation only through declared mappings that "
        "preserve canonical meanings.",
    ),
    Principle(
        "CAPRMEDIO-REQU-042--preserve-operator-sovereignty",
        "04_requirement",
        "CA-R-004-PRINCIPLE-REQUIREMENT--operator-acceptance-establishes-project-authority",
        ("principles",),
        "Operator acceptance establishes project authority",
        "Only acceptance by the project's declared operator or operators can establish "
        "project authority. Large language models, Tools, evidence, tiers, and graph "
        "relations may propose, organize, or support project meaning, but cannot make "
        "it authoritative.",
    ),
    Principle(
        "CAPRMEDIO-REQU-044--organize-authority-as-a-hierarchical-graph",
        "04_requirement",
        "CA-R-005-PRINCIPLE-REQUIREMENT--organize-authority-as-a-hierarchical-graph",
        ("principles",),
        "Organize authority as a hierarchical graph",
        "CAPRMEDIO must organize tier-classified RMEDO authority through explicit, "
        "typed, and acyclic lineage relations. Atoms may be created before their "
        "upstream structure; completeness is governed separately by the applicable "
        "authority mode.",
    ),
    Principle(
        "CAPRMEDIO-REQU-002--apply-mece-to-canonical-decompositions",
        "05_method",
        "CA-M-001-PRINCIPLE-METHOD--mece-for-canonical-decompositions",
        ("principles",),
        "MECE for canonical decompositions",
        "CAPRMEDIO must use Mutually Exclusive, Collectively Exhaustive (MECE) "
        "canonical decompositions whenever a decomposition claims to cover a declared "
        "universe, within that universe and at that level of abstraction.",
    ),
    Principle(
        "CAPRMEDIO-REQU-003--apply-dry-across-caprmedio",
        "05_method",
        "CA-M-002-PRINCIPLE-METHOD--apply-dry-across-caprmedio",
        ("principles",),
        "Apply DRY across CAPRMEDIO",
        "CAPRMEDIO must apply Don't Repeat Yourself (DRY) to governed meaning: each "
        "meaning has one canonical owner capable of resolving it completely and "
        "unambiguously; every other use must reference, derive, generate, or explicitly "
        "adapt that owner without becoming a duplicate definition.",
    ),
    Principle(
        "CAPRMEDIO-REQU-034--scale-through-structure",
        "05_method",
        "CA-M-003-PRINCIPLE-METHOD--scale-through-structure",
        ("principles",),
        "Scale through structure",
        "CAPRMEDIO must preserve information required for a governed use and manage its "
        "visible volume through structure and selective exposure. Information hidden "
        "from the current view must remain recoverable.",
    ),
    Principle(
        "CAPRMEDIO-REQU-022--require-falsifiable-claims",
        "06_evaluation",
        "CA-E-001-PRINCIPLE-EVALUATION--make-accepted-requirements-checkable",
        ("authority",),
        "Make accepted Requirements checkable",
        "CAPRMEDIO must make every accepted Requirement checkable when it is used to "
        "govern work or evaluate a result. The check may be stated directly or supplied "
        "through linked Evaluation.",
    ),
    Principle(
        "CAPRMEDIO-REQU-023--require-explicit-reliance-boundaries",
        "06_evaluation",
        "CA-E-002-PRINCIPLE-EVALUATION--require-explicit-reliance-boundaries",
        ("authority",),
        "Require explicit reliance boundaries",
        "Every governed use of authority, Method, Implementation, Evaluation, Delivery, "
        "or Ops conclusions must state the evidence and material uncertainty under which "
        "reliance is permitted and the condition that stops, degrades, blocks, or reopens "
        "that reliance. A missing, unknown, or contradictory required input fails closed "
        "at the affected use.",
    ),
    Principle(
        "CAPRMEDIO-REQU-012--replaceable-substrates",
        "07_delivery",
        "CA-D-001-PRINCIPLE-DELIVERY--keep-realizations-replaceable-across-technical-substrates",
        ("principles",),
        "Keep realizations replaceable across technical substrates",
        "CAPRMEDIO must keep realization and Delivery portable across technical "
        "substrates without transferring specification authority to Implementation. "
        "A substrate change must preserve the governed meanings and observable acceptance "
        "conditions of its source specification.",
    ),
    Principle(
        "CAPRMEDIO-REQU-009--extensibility-adds-governed-capabilities",
        "09_ops",
        "CA-O-001-PRINCIPLE-OPS--govern-capability-evolution-through-extensions",
        ("principles",),
        "Govern capability evolution through Extensions",
        "CAPRMEDIO Ops must govern independently evolvable reusable capabilities as "
        "explicit Extensions whose extension points, authority boundaries, and "
        "compatibility conditions are declared.",
    ),
    Principle(
        "CAPRMEDIO-REQU-010--configurability-selects-available-capabilities",
        "09_ops",
        "CA-O-002-PRINCIPLE-OPS--govern-capability-selection-through-configuration",
        ("principles",),
        "Govern capability selection through Configuration",
        "CAPRMEDIO Ops must govern project-owned Configuration that selects, combines, "
        "parameterizes, or disables available optional canonical and Extension "
        "capabilities only within declared configuration boundaries and without "
        "redefining governed meanings.",
    ),
    Principle(
        "CAPRMEDIO-REQU-046--improve-from-observed-project-outcomes",
        "09_ops",
        "CA-O-003-PRINCIPLE-OPS--improve-from-observed-outcomes",
        ("principles",),
        "Improve from observed outcomes",
        "CAPRMEDIO Ops must use material observed project outcomes to propose and "
        "evaluate changes at the narrowest affected scope while preserving unaffected "
        "authority and returning change into CAP.",
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="apply the migration")
    return parser.parse_args()


def repository_root() -> Path:
    candidate = Path.cwd().resolve()
    if (candidate / CONTROL_ROOT).is_dir() and (
        candidate / "caprmedio_framework_settings.toml"
    ).is_file():
        return candidate
    raise RuntimeError("run from the CAPRMEDIO repository root")


def split_frontmatter(text: str, path: Path) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise RuntimeError(f"{path}: missing YAML frontmatter")
    boundary = text.find("\n---\n", 4)
    if boundary < 0:
        raise RuntimeError(f"{path}: unterminated YAML frontmatter")
    return text[4:boundary], text[boundary + 5 :]


def active_markdown(root: Path) -> list[Path]:
    paths: list[Path] = []
    for path in (root / CONTROL_ROOT).rglob("*.md"):
        relative = path.relative_to(root / CONTROL_ROOT)
        if "archive" in relative.parts:
            continue
        paths.append(path)
    return sorted(paths)


def render(principle: Principle, timestamp: str) -> str:
    scopes = "\n".join(f"  - {scope}" for scope in principle.subject_scopes)
    return (
        "---\n"
        "subject_scopes:\n"
        f"{scopes}\n"
        "version: 1\n"
        f"updated_at: {timestamp}\n"
        "relations:\n"
        "  replacement_of:\n"
        f"    - {principle.old_stem}\n"
        "  child_of:\n"
        f"    - {GOAL}\n"
        "---\n"
        f"# {principle.title}\n\n"
        f"{principle.body}\n"
    )


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
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
    source_exists = [
        (root / CONTROL_ROOT / "04_requirement" / f"{item.old_stem}.md").is_file()
        for item in PRINCIPLES
    ]
    target_exists = [
        (root / CONTROL_ROOT / item.role_folder / f"{item.new_stem}.md").is_file()
        for item in PRINCIPLES
    ]
    if all(source_exists) and not any(target_exists):
        return "before"
    if not any(source_exists) and all(target_exists):
        return "after"
    raise RuntimeError("mixed Principle migration state; stop for recovery")


def planned_reference_updates(root: Path) -> dict[Path, str]:
    mapping = {item.old_stem: item.new_stem for item in PRINCIPLES}
    source_paths = {
        root / CONTROL_ROOT / "04_requirement" / f"{item.old_stem}.md"
        for item in PRINCIPLES
    }
    updates: dict[Path, str] = {}
    for path in active_markdown(root):
        if path in source_paths:
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        frontmatter, body = split_frontmatter(text, path)
        revised = frontmatter
        for old_stem, new_stem in mapping.items():
            revised = revised.replace(old_stem, new_stem)
        if revised != frontmatter:
            updates[path] = f"---\n{revised}\n---\n{body}"
    return updates


def validate_after(root: Path) -> None:
    mapping = {item.old_stem: item.new_stem for item in PRINCIPLES}
    for item in PRINCIPLES:
        active_source = (
            root / CONTROL_ROOT / "04_requirement" / f"{item.old_stem}.md"
        )
        archived_source = (
            root / CONTROL_ROOT / "04_requirement" / "archive" / f"{item.old_stem}.md"
        )
        target = root / CONTROL_ROOT / item.role_folder / f"{item.new_stem}.md"
        if active_source.exists() or not archived_source.is_file() or not target.is_file():
            raise RuntimeError(f"incomplete migration for {item.old_stem}")
        frontmatter, body = split_frontmatter(target.read_text(encoding="utf-8"), target)
        if "tier:" in frontmatter:
            raise RuntimeError(f"{target}: duplicated tier metadata")
        if f"# {item.title}\n" not in body:
            raise RuntimeError(f"{target}: unexpected H1")
        if f"    - {item.old_stem}" not in frontmatter:
            raise RuntimeError(f"{target}: missing replacement lineage")
    for path in active_markdown(root):
        if path.name in {f"{item.new_stem}.md" for item in PRINCIPLES}:
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        frontmatter, _ = split_frontmatter(text, path)
        for old_stem in mapping:
            if old_stem in frontmatter:
                raise RuntimeError(f"{path}: stale active relation to {old_stem}")


def apply(root: Path, updates: dict[Path, str]) -> Path:
    timestamp = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
    backup_stamp = dt.datetime.now().astimezone().strftime("%Y%m%dT%H%M%S%z")
    backup_root = root / RUNTIME_ROOT / backup_stamp
    if backup_root.exists():
        raise RuntimeError(f"backup target already exists: {backup_root}")
    changed_paths = list(updates)
    changed_paths.extend(
        root / CONTROL_ROOT / "04_requirement" / f"{item.old_stem}.md"
        for item in PRINCIPLES
    )
    for path in changed_paths:
        relative = path.relative_to(root)
        destination = backup_root / "files" / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)
    manifest = {
        "created_at": timestamp,
        "migration": "distribute_project_principles_across_rmedo",
        "predecessors": [item.old_stem for item in PRINCIPLES],
        "successors": [item.new_stem for item in PRINCIPLES],
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
    archive = root / CONTROL_ROOT / "04_requirement" / "archive"
    archive.mkdir(parents=True, exist_ok=True)
    for item in PRINCIPLES:
        source = root / CONTROL_ROOT / "04_requirement" / f"{item.old_stem}.md"
        archived = archive / source.name
        if archived.exists():
            raise RuntimeError(f"archive collision: {archived}")
        os.replace(source, archived)
    for item in PRINCIPLES:
        target = root / CONTROL_ROOT / item.role_folder / f"{item.new_stem}.md"
        atomic_write(target, render(item, timestamp))
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
    print(
        f"state=before principles={len(PRINCIPLES)} "
        f"reference_files={len(updates)} apply={args.apply}"
    )
    for item in PRINCIPLES:
        print(f"{item.old_stem} -> {item.new_stem}")
    if not args.apply:
        return 0
    backup_root = apply(root, updates)
    print(f"backup={backup_root.relative_to(root)}")
    print("status=applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
