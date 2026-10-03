#!/usr/bin/env python3
"""Apply the REALIZATION, RELEASES, and FIELD structural authority migration.

Dry-run is the default. Use ``--apply`` only from the repository root. The
script accepts only the exact pre-migration carrier shapes encoded below and
stops on unexpected content instead of guessing.
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
OLD_FEATURE_CONTRACT = "CAPRMEDIO-CNTR-001--map-spec-features-to-implementation-realizations"
NEW_FEATURE_CONTRACT = "CAPRMEDIO-CNTR-011--map-spec-features-to-realization-features"
OLD_REALIZATION_TOPOLOGY = "CAPRMEDIO-REALIZATION-REQU-590--govern-complete-implementation-feature-topology"
NEW_REALIZATION_TOPOLOGY = "CAPRMEDIO-REALIZATION-REQU-612--govern-complete-realization-feature-topology"


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


def exact_replace(text: str, old: str, new: str, path: Path) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new)
    if count == 0 and new in text:
        return text
    raise ValueError(f"{path}: expected exactly one old value, found {count}: {old!r}")


def set_revision(text: str, version: int, updated_at: str, path: Path) -> str:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise ValueError(f"{path}: expected YAML frontmatter")
    closing = next((index for index, line in enumerate(lines[1:], 1) if line.rstrip("\r\n") == "---"), None)
    if closing is None:
        raise ValueError(f"{path}: unterminated YAML frontmatter")

    version_indices = [index for index in range(1, closing) if lines[index].startswith("version:")]
    updated_indices = [index for index in range(1, closing) if lines[index].startswith("updated_at:")]
    if len(version_indices) > 1 or len(updated_indices) > 1:
        raise ValueError(f"{path}: duplicate revision properties")

    newline = "\r\n" if any(line.endswith("\r\n") for line in lines) else "\n"
    if version_indices:
        lines[version_indices[0]] = f"version: {version}{newline}"
    else:
        insertion = 1
        while insertion < closing and (
            lines[insertion].startswith("subject_scopes:")
            or lines[insertion].startswith("  - ")
            or lines[insertion].startswith("tier:")
        ):
            insertion += 1
        lines.insert(insertion, f"version: {version}{newline}")
        closing += 1

    if updated_indices:
        index = updated_indices[0]
        if not version_indices and index >= insertion:
            index += 1
        lines[index] = f"updated_at: {updated_at}{newline}"
    else:
        version_index = next(index for index in range(1, closing) if lines[index].startswith("version:"))
        lines.insert(version_index + 1, f"updated_at: {updated_at}{newline}")
    return "".join(lines)


def update_file(root: Path, relative: str, replacements: list[tuple[str, str]], version: int | None, updated_at: str) -> tuple[Path, str] | None:
    path = root / relative
    text = path.read_text(encoding="utf-8")
    updated = text
    for old, new in replacements:
        updated = exact_replace(updated, old, new, path)
    if version is not None:
        updated = set_revision(updated, version, updated_at, path)
    if updated == text:
        return None
    return path, updated


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    updated_at = args.updated_at or datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
    datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S")

    changes: dict[Path, str] = {}

    exact_updates: list[tuple[str, list[tuple[str, str]], int | None]] = [
        (
            ".caprmedio/04_requirement/CAPRMEDIO-REQU-606--define-realization-layer-scope.md",
            [("actual source, documentation, configuration, tests, evaluations, and other", "actual source code, configuration, tests, evaluations, skills, tools, documentation, and other")],
            2,
        ),
        (
            ".caprmedio/04_requirement/CAPRMEDIO-REQU-039--define-the-six-layer-project-structure.md",
            [("META, GOV, SPEC, IMPLEMENTATION, DELIVERY, and OPS", "META, GOV, SPEC, REALIZATION, RELEASES, and FIELD")],
            2,
        ),
        (
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-089--current-layer-handoffs.md",
            [
                (
                    "| SPEC → IMPLEMENTATION | Complete applicable `RMED` Specification | Concrete realization and its traceability |\n| IMPLEMENTATION → DELIVERY | Assured realization and distributable outputs | Environment-specific package, deployment, release, or publication |\n| DELIVERY → OPS | Released and supportable output | Operable, observable, and diagnosable service or product |",
                    "| SPEC → REALIZATION | Complete applicable `RMED` Specification | Concrete realization and its traceability |\n| REALIZATION → RELEASES | Assured realization and releasable outputs | Versioned release publications and views |\n| RELEASES → FIELD | Published release output | Actual use, support, telemetry, incidents, and outcomes |",
                )
            ],
            2,
        ),
        (
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-176--derive-global-tier-number-from-structure-and-applicability.md",
            [
                (
                    "CAPRMEDIO must derive each RMED Atom's global tier number by adding its configured structural-level number to the configured position of its readable applicability-tier name.",
                    "CAPRMEDIO must derive each RMED Atom's global tier number from its configured structural-authority depth and readable applicability-tier name, with distinct ordered depths receiving non-overlapping numbers while peer scopes at the same depth may share them.",
                )
            ],
            4,
        ),
        (
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-329--encode-rmed-applicability-tiers.md",
            [
                (
                    "Applicability-tier position is the zero-based position of its name in the ordered catalog and is never duplicated in an Atom. The registered default tier may be omitted and resolved from settings. Validators reject unknown or duplicated names, duplicate positions, role-ineligible tiers, numeric tier values in Atoms, and `priority` on tier-classified RMED Atoms.",
                    "Project settings register the ordered readable tier catalog and the global number assigned to every admitted structural-authority-depth and tier-name coordinate; the registered default tier may be omitted and resolved from settings. Validators reject unknown names, duplicate coordinate assignments across ordered depths, role-ineligible tiers, numeric tier values in Atoms, and `priority` on tier-classified RMED Atoms.",
                )
            ],
            6,
        ),
        (
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-379--derive-one-global-rmed-tier-number.md",
            [
                (
                    "GOV must derive each tier-classified RMED Atom's global tier number from its structural level and registered applicability-tier position without storing that derived number in the Atom frontmatter.",
                    "GOV must derive each tier-classified RMED Atom's global tier number from its registered structural-authority-depth and readable tier-name coordinate without storing that derived number in the Atom frontmatter.",
                )
            ],
            2,
        ),
        (
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-381--register-feature-realization-relation-kind.md",
            [("distinct IMPLEMENTATION Feature scope", "distinct REALIZATION Feature scope")],
            2,
        ),
        (
            ".caprmedio/200_LAYER_2_GOV/06_evaluation/CAPRMEDIO-GOV-EVAL-004--current-scope-and-layer-distinction.md",
            [("META → GOV → SPEC → PROFILES → IMPL → OPS", "META → GOV → SPEC → REALIZATION → RELEASES → FIELD")],
            2,
        ),
        (
            ".caprmedio/CAPRMEDIO-CONTROL-HUB.md",
            [("`100_LAYER_1_META`, `200_LAYER_2_GOV`, `300_LAYER_3_SPEC`, `400_LAYER_4_IMPLEMENTATION`, and `600_LAYER_6_OPS`", "`100_LAYER_1_META`, `200_LAYER_2_GOV`, `300_LAYER_3_SPEC`, `400_LAYER_4_REALIZATION`, `500_LAYER_5_RELEASES`, and `600_LAYER_6_FIELD`")],
            None,
        ),
        (
            ".caprmedio/caprmedio_project_settings.toml",
            [
                (
                    "[authority.tiers]\n# Array positions participate in derived global tier numbers.\nexternal_root = \"goal\"\nordered = [\"principle\", \"core\", \"standard\"]\ndefault = \"standard\"",
                    "[authority.tiers]\nexternal_root = \"goal\"\nordered = [\"principle\", \"core\", \"standard\"]\ndefault = \"standard\"\n\n[authority.global_tier_numbers]\ngoal = -1\nproject_principle = 0\nproject_core = 1\nproject_standard = 2\nmeta_core = 3\nmeta_standard = 4\ngov_core = 5\ngov_standard = 6\nspec_core = 7\nspec_standard = 8\nspec_feature_core = 9\nspec_feature_standard = 10",
                ),
                (
                    "layers = [\"meta\", \"gov\", \"spec\", \"implementation\", \"delivery\", \"ops\"]",
                    "layers = [\"meta\", \"gov\", \"spec\", \"realization\", \"releases\", \"field\"]",
                ),
                (
                    "implementation = [\"methodology\", \"tools\", \"skills\", \"profiles\", \"adapters\", \"evaluation\", \"documentation\"]",
                    "realization = [\"methodology\", \"tools\", \"skills\", \"profiles\", \"adapters\", \"evaluation\", \"documentation\"]",
                ),
            ],
            None,
        ),
        (
            ".caprmedio/400_LAYER_4_REALIZATION/CAPRMEDIO-REALIZATION-METH-058--canonical-health-path-order.md",
            [("so IMPL owns it", "so REALIZATION owns it")],
            None,
        ),
        (
            ".caprmedio/400_LAYER_4_REALIZATION/CAPRMEDIO-REALIZATION-METH-061--deterministic-git-fixture-bytes.md",
            [("belongs in IMPL rather than the post-implementation OPS layer", "belongs in REALIZATION rather than the post-release FIELD Layer")],
            None,
        ),
        (
            ".caprmedio/400_LAYER_4_REALIZATION/CAPRMEDIO-REALIZATION-REQU-582--local-python-tools-profile.md",
            [("OPS owns runtime", "FIELD owns runtime")],
            None,
        ),
    ]

    for relative, replacements, version in exact_updates:
        change = update_file(root, relative, replacements, version, updated_at)
        if change:
            changes[change[0]] = change[1]

    spec_children = [
        f".caprmedio/300_LAYER_3_SPEC/04_requirement/CAPRMEDIO-SPEC-REQU-{number:03d}--define-{name}-feature-scope.md"
        for number, name in zip(range(498, 505), ["methodology", "tools", "skills", "profiles", "adapters", "evaluation", "documentation"], strict=True)
    ]
    realization_children = [
        f".caprmedio/400_LAYER_4_REALIZATION/CAPRMEDIO-REALIZATION-REQU-{number:03d}--define-{name}-feature-scope.md"
        for number, name in zip(range(591, 598), ["methodology", "tools", "skills", "profiles", "adapters", "evaluation", "documentation"], strict=True)
    ]
    for relative in spec_children:
        change = update_file(root, relative, [(OLD_FEATURE_CONTRACT, NEW_FEATURE_CONTRACT)], 2, updated_at)
        if change:
            changes[change[0]] = change[1]
    for relative in realization_children:
        change = update_file(
            root,
            relative,
            [
                (OLD_REALIZATION_TOPOLOGY, NEW_REALIZATION_TOPOLOGY),
                (OLD_FEATURE_CONTRACT, NEW_FEATURE_CONTRACT),
                ("# Define the IMPLEMENTATION", "# Define the REALIZATION"),
                ("The IMPLEMENTATION", "The REALIZATION"),
            ],
            2,
            updated_at,
        )
        if change:
            changes[change[0]] = change[1]

    old_topology = root / ".caprmedio/400_LAYER_4_REALIZATION/CAPRMEDIO-REALIZATION-REQU-590--govern-complete-implementation-feature-topology.md"
    archived_topology = root / ".caprmedio/400_LAYER_4_REALIZATION/archive/CAPRMEDIO-REALIZATION-REQU-590--govern-complete-implementation-feature-topology.md"
    new_topology = root / ".caprmedio/400_LAYER_4_REALIZATION/CAPRMEDIO-REALIZATION-REQU-612--govern-complete-realization-feature-topology.md"
    new_topology_text = f"""---
subject_scopes:
  - scope-topology
tier: core
version: 1
updated_at: {updated_at}
llm_session_ids:
  - {args.session_id}
relations:
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
    - CAPRMEDIO-META-REQU-159--allow-scope-sets-to-vary-by-structural-owner
  replacement_of:
    - {OLD_REALIZATION_TOPOLOGY}
---
# Govern complete REALIZATION Feature topology

REALIZATION maintains one explicit, complete, and mutually exclusive Feature partition for Feature-owned realized artifacts while retaining genuinely Layer-wide realization at REALIZATION scope.
"""
    if new_topology.exists():
        if new_topology.read_text(encoding="utf-8") != new_topology_text:
            raise ValueError(f"{new_topology}: existing successor differs from expected content")
    else:
        changes[new_topology] = new_topology_text
    if old_topology.exists() and archived_topology.exists():
        raise ValueError("both active and archived old topology carriers exist")
    if not old_topology.exists() and not archived_topology.exists():
        raise ValueError("old topology carrier is missing")

    overbroad_name_rule = root / ".caprmedio/04_requirement/CAPRMEDIO-REQU-613--separate-structural-names-from-artifact-vocabulary.md"
    archived_overbroad_name_rule = root / ".caprmedio/04_requirement/archive/CAPRMEDIO-REQU-613--separate-structural-names-from-artifact-vocabulary.md"
    layer_name_rule = root / ".caprmedio/04_requirement/CAPRMEDIO-REQU-614--separate-layer-names-from-artifact-vocabulary.md"
    layer_name_text = f"""---
subject_scopes:
  - scope-topology
version: 1
updated_at: {updated_at}
llm_session_ids:
  - {args.session_id}
relations:
  child_of:
    - CAPRMEDIO-REQU-045--separate-hierarchy-dimensions
  replacement_of:
    - CAPRMEDIO-REQU-613--separate-structural-names-from-artifact-vocabulary
---
# Separate Layer names from artifact vocabulary

Every Layer name must be distinct from every enabled Content-role, Type, and subtype name so a Layer name identifies only the structural dimension.
"""
    if layer_name_rule.exists():
        if layer_name_rule.read_text(encoding="utf-8") != layer_name_text:
            raise ValueError(f"{layer_name_rule}: existing Requirement differs from expected content")
    else:
        changes[layer_name_rule] = layer_name_text
    if overbroad_name_rule.exists() and archived_overbroad_name_rule.exists():
        raise ValueError("both active and archived overbroad name Requirements exist")
    if not overbroad_name_rule.exists() and not archived_overbroad_name_rule.exists():
        raise ValueError("overbroad name Requirement is missing")

    print(json.dumps({"mode": "apply" if args.apply else "dry-run", "updated_at": updated_at, "file_changes": len(changes), "archive_moves": int(old_topology.exists()) + int(overbroad_name_rule.exists())}, sort_keys=True))
    for path in sorted(changes):
        print(path.relative_to(root))
    if not args.apply:
        return 0
    if not changes and not old_topology.exists() and not overbroad_name_rule.exists():
        return 0

    for path, text in changes.items():
        atomic_write(path, text)
    if old_topology.exists():
        archived_topology.parent.mkdir(parents=True, exist_ok=True)
        old_topology.replace(archived_topology)
    if overbroad_name_rule.exists():
        archived_overbroad_name_rule.parent.mkdir(parents=True, exist_ok=True)
        overbroad_name_rule.replace(archived_overbroad_name_rule)

    journal = root / ".caprmedio/010_journals/src-work-journal-2026-08-18.ndjson"
    event = {
        "action_id": "apply-realization-releases-field-authority-20260818",
        "event": "completed",
        "event_id": str(uuid4()),
        "governed_subjects": [
            "CAPRMEDIO-REQU-039--define-the-six-layer-project-structure",
            "CAPRMEDIO-REQU-609--assign-project-global-rmed-tier-numbers",
            "CAPRMEDIO-REQU-614--separate-layer-names-from-artifact-vocabulary",
        ],
        "kind": "authority_migration",
        "occurred_at": updated_at,
        "operation": "apply_realization_releases_field_authority",
        "produced_outputs": ["REALIZATION", "RELEASES", "FIELD"],
        "schema_version": 1,
        "session_id": args.session_id,
        "structural_scope": "project",
    }
    with journal.open("a", encoding="utf-8", newline="") as handle:
        handle.write(json.dumps(event, separators=(",", ":"), sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
