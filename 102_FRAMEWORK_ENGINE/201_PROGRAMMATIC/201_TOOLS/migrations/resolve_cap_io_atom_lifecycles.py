#!/usr/bin/env python3
"""Resolve Concern, Analysis, Plan, Implementation, and Ops Atom lifecycles.

Usage:
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/resolve_cap_io_atom_lifecycles.py
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/resolve_cap_io_atom_lifecycles.py --apply

The default mode is read-only. The migration adds role-specific META and GOV
authority, updates affected active authority, moves the resolved Question to
solved, and moves completed Analysis Atoms to done.
"""

from __future__ import annotations

import argparse
import os
import runpy
import sys
from pathlib import Path

_PROJECT_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402


META_REQUIREMENTS = Path(".caprmedio/100_LAYER_1_META/04_requirement")
GOV_REQUIREMENTS = Path(".caprmedio/200_LAYER_2_GOV/04_requirement")
QUESTION = Path(
    ".caprmedio/100_LAYER_1_META/01_concern/"
    "CAPRMEDIO-META-CONC-011--what-lifecycle-models-govern-cap-and-io-atoms.md"
)
QUESTION_STEM = "CAPRMEDIO-META-CONC-011--what-lifecycle-models-govern-cap-and-io-atoms"
SESSION_ID = "codex:019f591f-04f6-70f2-8de7-828b7cccc69d"
META_LIFECYCLE = "CAPRMEDIO-META-REQU-130--define-atom-admission-and-lifecycle"
META_ATOMICITY = "CAPRMEDIO-META-REQU-132--define-role-specific-atom-atomicity"
NORMALIZER = Path(__file__).resolve().parent / "normalize_core_requirement_carriers.py"
TOUCHED_EXISTING = (
    META_REQUIREMENTS / "CAPRMEDIO-META-REQU-112--role-specific-atom-occupancy.md",
    META_REQUIREMENTS / "CAPRMEDIO-META-REQU-130--define-atom-admission-and-lifecycle.md",
    META_REQUIREMENTS / "CAPRMEDIO-META-REQU-132--define-role-specific-atom-atomicity.md",
    GOV_REQUIREMENTS / "CAPRMEDIO-GOV-REQU-321--register-caprmedio-atom-type-surface.md",
    GOV_REQUIREMENTS / "CAPRMEDIO-GOV-REQU-481--use-flat-numbered-layer-feature-layout.md",
    GOV_REQUIREMENTS / "CAPRMEDIO-GOV-REQU-327--use-full-filename-stems-as-artifact-references.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="apply the migration")
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    return parser.parse_args()


def meta_carrier(
    number: int,
    summary: str,
    parent: str,
    claim: str,
    extra_parent: str | None = None,
) -> tuple[str, str]:
    stem = f"CAPRMEDIO-REQUIREMENT-META-{number:03d}-{summary}"
    parents = f"    - {parent}\n"
    if extra_parent is not None:
        parents += f"    - {extra_parent}\n"
    title = summary.replace("-", " ").capitalize().replace(" ops ", " Ops ")
    text = (
        "---\n"
        "subject_scopes:\n"
        "  - lifecycle-traceability\n"
        "llm_session_ids:\n"
        f"  - {SESSION_ID}\n"
        "relations:\n"
        "  child_of:\n"
        f"{parents}"
        "  resolution_of:\n"
        f"    - {QUESTION_STEM}\n"
        "---\n"
        f"# {title}\n\n"
        f"{claim}\n"
    )
    return stem, text


def gov_carrier(number: int, summary: str, parent: str, claim: str) -> tuple[str, str]:
    stem = f"CAPRMEDIO-REQUIREMENT-GOV-{number:03d}-{summary}"
    title = summary.replace("-", " ").capitalize().replace(" ops ", " Ops ")
    text = (
        "---\n"
        "subject_scopes:\n"
        "  - lifecycle\n"
        "llm_session_ids:\n"
        f"  - {SESSION_ID}\n"
        "relations:\n"
        "  child_of:\n"
        f"    - {parent}\n"
        "---\n"
        f"# {title}\n\n"
        f"{claim}\n"
    )
    return stem, text


def desired_files(root: Path) -> dict[Path, str]:
    meta_specs = (
        meta_carrier(
            204,
            "use-concern-atom-lifecycle",
            META_LIFECYCLE,
            "A Concern Atom uses exactly draft, active, solved, and archived lifecycle meanings: draft is not accepted for current work, active awaits disposition, solved has received its governed disposition, and archived is preserved outside current work without a solution.",
        ),
        meta_carrier(
            205,
            "use-analysis-atom-lifecycle",
            META_LIFECYCLE,
            "An Analysis Atom uses exactly draft, done, and archived lifecycle meanings: draft is unfinished, done is the completed bounded analysis product, and archived is preserved outside current use.",
        ),
        meta_carrier(
            206,
            "use-plan-atom-lifecycle",
            META_LIFECYCLE,
            "A Plan Atom uses exactly draft, active, done, and archived lifecycle meanings: draft is unaccepted planning, active coordinates current action points, done completed its action points, and archived was abandoned, absorbed, or otherwise removed from current execution.",
        ),
        meta_carrier(
            207,
            "prohibit-implementation-atoms",
            META_LIFECYCLE,
            "Implementation admits no Atom at any Governance locus because the native project is the Implementation; governed realization history and current realization views use Journals and Projections.",
            META_ATOMICITY,
        ),
        meta_carrier(
            208,
            "use-ops-atom-lifecycle",
            META_LIFECYCLE,
            "An Ops Atom uses exactly happened and handled lifecycle meanings: happened records an admitted enacted occurrence or observation, and handled records completion of its governed response or disposition.",
        ),
    )
    gov_specs = (
        gov_carrier(
            190,
            "map-concern-lifecycle-to-role-local-placement",
            meta_specs[0][0],
            "GOV derives Concern lifecycle from role-local placement: drafts contains draft Concerns, the Concern directory contains active Concerns, solved contains solved Concerns, and archive contains archived Concerns.",
        ),
        gov_carrier(
            191,
            "map-analysis-lifecycle-to-role-local-placement",
            meta_specs[1][0],
            "GOV derives Analysis lifecycle from role-local placement: drafts contains draft Analyses, done contains done Analyses, and archive contains archived Analyses.",
        ),
        gov_carrier(
            192,
            "map-plan-lifecycle-to-role-local-placement",
            meta_specs[2][0],
            "GOV derives Plan lifecycle from role-local placement: drafts contains draft Plans, the Plan directory contains active Plans, done contains done Plans, and archive contains archived Plans.",
        ),
        gov_carrier(
            193,
            "admit-no-implementation-atom-placement",
            meta_specs[3][0],
            "GOV registers no lifecycle carrier location for Implementation Atoms.",
        ),
        gov_carrier(
            194,
            "map-ops-lifecycle-to-role-local-placement",
            meta_specs[4][0],
            "GOV derives Ops lifecycle from role-local placement: happened contains happened Ops Atoms and handled contains handled Ops Atoms.",
        ),
    )
    desired: dict[Path, str] = {}
    for stem, text in meta_specs:
        desired[root / META_REQUIREMENTS / f"{stem}.md"] = text
    for stem, text in gov_specs:
        desired[root / GOV_REQUIREMENTS / f"{stem}.md"] = text
    return desired


def replace_once(text: str, old: str, new: str, path: Path) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"{path}: expected exactly one migration block")
    return text.replace(old, new, 1)


def update_meta_lifecycle(text: str, path: Path) -> str:
    old = (
        "- `active` means an accepted and admitted Atom participates in current authority when its Content role is authoritative;\n"
        "- `done` means a Plan's action points were completed; and\n"
        "- `archived` means a preserved Atom no longer participates in current authority.\n\n"
        "Acceptance, admission, commitment, activation, completion, and archival remain distinct."
    )
    new = (
        "- `active` means an admitted Atom participates in current governed work or authority under its Content role;\n"
        "- `solved` means an active Concern received its governed disposition;\n"
        "- `done` means an Analysis product or Plan execution package completed its role-specific work;\n"
        "- `happened` means an Ops occurrence or observation was admitted as fact;\n"
        "- `handled` means the governed response or disposition required for an Ops occurrence was completed; and\n"
        "- `archived` means a preserved Atom no longer participates in current authority.\n\n"
        "Acceptance, admission, commitment, activation, solution, completion, occurrence, handling, and archival remain distinct."
    )
    return replace_once(text, old, new, path)


def update_meta_atomicity(text: str, path: Path) -> str:
    text = replace_once(
        text,
        "| Implementation | Deferred. No Atom atomicity model is established; the internal Implementation remains the project outside `.caprmedio/`. |",
        "| Implementation | No Atom route is admitted; the native project remains the Implementation. |",
        path,
    )
    old = (
        "Plan uses its bounded execution-package model, and Implementation Atom\n"
        "atomicity remains deferred to CAPRMEDIO-QUESTION-META-006."
    )
    new = (
        "Plan uses its bounded execution-package model. Implementation occupancy is governed by "
        "CAPRMEDIO-REQUIREMENT-META-207-prohibit-implementation-atoms."
    )
    return replace_once(text, old, new, path)


def update_meta_occupancy(text: str, path: Path) -> str:
    old = (
        "Implementation does not require an\n"
        "internal Atom Type: the native project outside `.caprmedio/` is the actual\n"
        "Implementation, while Journals and Projections about that realization retain\n"
        "their own Artifact forms. Whether external or relation Governance-locus\n"
        "Implementation routes qualify as Atoms, and what atomicity model they use, is\n"
        "deferred to CAPRMEDIO-QUESTION-META-006."
    )
    new = "Implementation Atom occupancy is governed by CAPRMEDIO-REQUIREMENT-META-207-prohibit-implementation-atoms."
    return replace_once(text, old, new, path)


def update_gov_catalog(text: str, path: Path) -> str:
    text = replace_once(
        text,
        "| `implementation` | — | `external_git_commit` | `pull_request` |",
        "| `implementation` | — | — | — |",
        path,
    )
    old = (
        "The internal Implementation Atom route is not admitted because native project artifacts are the Implementation;\n"
        "Journals and Projections about them retain their own forms and Types. Existing\n"
        "external and relational Implementation routes remain admitted as governed claims\n"
        "about explicit outside or cross-boundary carriers."
    )
    new = (
        "No Implementation Atom route is admitted at any Governance locus because native project artifacts are the Implementation; "
        "Journals and Projections about realization retain their own forms and Types."
    )
    return replace_once(text, old, new, path)


def update_gov_layout(text: str, path: Path) -> str:
    old = (
        "Active Atoms live directly in their role directory, pre-admission candidates live under `drafts/`, and inactive Atoms live unchanged under `archive/`. Their placement is authoritative and is not repeated as embedded lifecycle metadata.\n\n"
    )
    return replace_once(text, old, "", path)


def update_gov_references(text: str, path: Path) -> str:
    old = (
        "Directory location\n"
        "is not part of the Artifact reference, so moving a carrier among its active,\n"
        "`drafts`, `done`, and `archive` locations preserves incoming relations."
    )
    new = (
        "Directory location is not part of the Artifact reference, so moving a carrier among its role-specific direct, "
        "`drafts`, `solved`, `done`, `happened`, `handled`, and `archive` locations preserves incoming relations."
    )
    return replace_once(text, old, new, path)


def updated_existing(root: Path) -> dict[Path, str]:
    paths = [root / path for path in TOUCHED_EXISTING]
    updates = (
        update_meta_occupancy,
        update_meta_lifecycle,
        update_meta_atomicity,
        update_gov_catalog,
        update_gov_layout,
        update_gov_references,
    )
    return {
        path: update(path.read_text(encoding="utf-8"), path)
        for path, update in zip(paths, updates, strict=True)
    }


def analysis_sources(root: Path) -> list[Path]:
    return sorted(
        path
        for directory in root.joinpath(".caprmedio").rglob("02_analysis")
        for path in directory.glob("*.md")
    )


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
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


def normalize_touched(root: Path, paths: list[Path]) -> None:
    module = runpy.run_path(str(NORMALIZER), run_name="carrier_normalizer")
    for path in paths:
        atomic_write(path, module["normalize_carrier"](path))


def detect_state(root: Path, desired: dict[Path, str]) -> str:
    question_active = (root / QUESTION).is_file()
    question_solved = (root / QUESTION.parent / "solved" / QUESTION.name).is_file()
    direct_analysis = analysis_sources(root)
    new_absent = all(not path.exists() for path in desired)
    new_present = all(path.is_file() for path in desired)
    marker = "CAPRMEDIO-REQUIREMENT-META-207-prohibit-implementation-atoms"
    existing_updated = marker in (root / TOUCHED_EXISTING[2]).read_text(encoding="utf-8")
    if question_active and not question_solved and new_absent and direct_analysis and not existing_updated:
        return "pending"
    if not question_active and question_solved and new_present and not direct_analysis and existing_updated:
        return "applied"
    raise RuntimeError("mixed or unexpected migration state")


def apply_migration(root: Path, desired: dict[Path, str]) -> None:
    existing = updated_existing(root)
    for path, text in {**desired, **existing}.items():
        atomic_write(path, text)
    question_target = root / QUESTION.parent / "solved" / QUESTION.name
    question_target.parent.mkdir(parents=True, exist_ok=True)
    os.replace(root / QUESTION, question_target)
    moved: list[Path] = []
    for source in analysis_sources(root):
        target = source.parent / "done" / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            raise RuntimeError(f"analysis target already exists: {target}")
        os.replace(source, target)
        moved.append(target)
    normalize_touched(root, [*desired, *existing])


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    desired = desired_files(root)
    state = detect_state(root, desired)
    direct_analysis = len(analysis_sources(root))
    changes = 0 if state == "applied" else len(desired) + len(TOUCHED_EXISTING) + direct_analysis + 1
    print(
        f"state={state} new_authority={len(desired)} existing_authority={len(TOUCHED_EXISTING)} "
        f"analysis_moves={direct_analysis} question_moves={0 if state == 'applied' else 1} changes={changes}"
    )
    if args.apply and state == "pending":
        apply_migration(root, desired)
        if detect_state(root, desired) != "applied":
            raise RuntimeError("post-apply verification failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
