#!/usr/bin/env python3
"""Move current Project Settings values into their governing RMED Atoms.

The migration reads the legacy generated Map only to recover its existing
source assignments. It fails closed on unexpected structures, prepares every
carrier before writing, and is intentionally one-shot: an existing
``project_settings`` block is rejected.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tomllib
from pathlib import Path
from typing import Any

_PROJECT_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402


CONTROL_ROOT = Path(".caprmedio")
SETTINGS = CONTROL_ROOT / "caprmedio_project_settings.toml"
SOURCE_MAP = CONTROL_ROOT / "08_implementation/CAPRMEDIO-MAPS-001--project-settings-source-map.yaml"
IGNORED_STATES = {"archive", "drafts", "done", "solved", "handled"}
TIMESTAMP = "2026-08-18 20:19:17"


TYPE_SURFACE = [
    "concern", "external_problem", "conflict", "analysis",
    "external_analysis_report", "conflict_analysis", "plan", "requirement",
    "constraint", "contract", "method", "external_method", "method_binding",
    "evaluation", "evaluation_standard", "review_protocol", "delivery",
    "implementation", "external_git_commit", "pull_request", "ops",
    "external_evidence_record", "verification_record",
]

SPECIAL_CONTRIBUTIONS: dict[str, dict[str, Any]] = {
    "artifacts.enabled_types": {
        "CAPRMEDIO-GOV-REQU-321--register-caprmedio-atom-type-surface": TYPE_SURFACE,
        "CAPRMEDIO-GOV-REQU-313--govern-catalog-map-and-hub-projections": ["catalog", "map", "hub"],
        "CAPRMEDIO-GOV-REQU-322--register-implementation-record-projection": ["implementation_record"],
        "CAPRMEDIO-GOV-REQU-338--register-the-project-work-journal": ["work_journal"],
    },
    "artifacts.enabled_subtypes": {
        "CAPRMEDIO-GOV-REQU-321--register-caprmedio-atom-type-surface": ["requirement:goal", "analysis:analysis_report"],
        "CAPRMEDIO-GOV-REQU-318--register-concern-atom-subtypes": [
            "concern:question", "concern:problem", "concern:risk", "concern:opportunity",
        ],
        "CAPRMEDIO-GOV-REQU-324--register-rationale-analysis-subtype": ["analysis:rationale"],
        "CAPRMEDIO-GOV-REQU-343--register-plan-subtypes": [
            "plan:development_backlog", "plan:version_plan", "plan:change_plan", "plan:refactoring_plan",
        ],
        "CAPRMEDIO-GOV-REQU-357--register-implementation-decision-method-subtype": ["method:implementation_decision"],
        "CAPRMEDIO-GOV-REQU-317--register-evaluation-atom-subtypes": [
            "evaluation:qa_case", "evaluation:evaluation_control",
        ],
        "CAPRMEDIO-GOV-REQU-331--register-delivery-subtypes": [
            "delivery:release_definition", "delivery:environment_definition",
        ],
        "CAPRMEDIO-GOV-REQU-332--register-ops-subtypes": [
            "ops:release_record", "ops:deployment_record", "ops:environment_state",
            "ops:health_record", "ops:incident_record",
        ],
    },
    "artifacts.identity.project_prefix": {
        "CAPRMEDIO-REQU-051--use-caprmedio-as-the-canonical-project-name": "CAPRMEDIO",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("root", nargs="?", default=".")
    return parser.parse_args()


def yaml_scalar(value: str) -> Any:
    if value == "true":
        return True
    if value == "false":
        return False
    if re.fullmatch(r"-?[0-9]+", value):
        return int(value)
    return value


def parse_yaml_block(lines: list[str], index: int, indent: int) -> tuple[dict[str, Any] | list[Any], int]:
    list_mode = lines[index][indent:].startswith("- ")
    container: dict[str, Any] | list[Any] = [] if list_mode else {}
    while index < len(lines):
        line = lines[index]
        actual = len(line) - len(line.lstrip(" "))
        if actual < indent:
            break
        if actual != indent or actual % 2:
            raise RuntimeError(f"invalid YAML indentation at source-map line {index + 1}")
        content = line[indent:]
        if list_mode:
            if not content.startswith("- ") or not content[2:]:
                raise RuntimeError(f"invalid YAML list item at source-map line {index + 1}")
            assert isinstance(container, list)
            container.append(yaml_scalar(content[2:]))
            index += 1
            continue
        if content.startswith("- ") or ":" not in content:
            raise RuntimeError(f"invalid YAML mapping at source-map line {index + 1}")
        key, value = content.split(":", 1)
        if not re.fullmatch(r"[a-z0-9_]+", key) or (value and not value.startswith(" ")):
            raise RuntimeError(f"unsupported YAML key at source-map line {index + 1}")
        assert isinstance(container, dict)
        if key in container:
            raise RuntimeError(f"duplicate YAML key at source-map line {index + 1}")
        index += 1
        if value:
            container[key] = yaml_scalar(value[1:])
            continue
        if index >= len(lines):
            raise RuntimeError(f"missing YAML child for {key}")
        child_indent = len(lines[index]) - len(lines[index].lstrip(" "))
        if child_indent != indent + 2:
            raise RuntimeError(f"invalid YAML child indentation for {key}")
        child, index = parse_yaml_block(lines, index, child_indent)
        container[key] = child
    return container, index


def flatten(node: dict[str, Any], prefix: tuple[str, ...] = ()) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in node.items():
        path = (*prefix, key)
        if isinstance(value, dict):
            result.update(flatten(value, path))
        else:
            result[".".join(path)] = value
    return result


def load_bindings(root: Path) -> dict[str, list[str]]:
    lines = (root / SOURCE_MAP).read_text(encoding="utf-8").splitlines()
    document, index = parse_yaml_block(lines, 0, 0)
    if index != len(lines) or not isinstance(document, dict) or not isinstance(document.get("bindings"), dict):
        raise RuntimeError("legacy source Map has an unexpected structure")
    flattened = flatten(document["bindings"])
    if any(not isinstance(value, list) or not value for value in flattened.values()):
        raise RuntimeError("legacy source Map has a non-list or empty binding")
    return flattened


def load_values(root: Path) -> dict[str, Any]:
    document = tomllib.loads((root / SETTINGS).read_text(encoding="utf-8"))
    document.pop("projection", None)
    return flatten(document)


def active_atom(root: Path, stem: str) -> Path:
    matches = [
        path for path in (root / CONTROL_ROOT).rglob(f"{stem}.md")
        if not IGNORED_STATES.intersection(path.parts)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"expected one active Atom for {stem}, found {len(matches)}")
    return matches[0]


def assign_path(target: dict[str, Any], dotted: str, value: Any) -> None:
    cursor = target
    parts = dotted.split(".")
    for part in parts[:-1]:
        existing = cursor.setdefault(part, {})
        if not isinstance(existing, dict):
            raise RuntimeError(f"setting path collision at {dotted}")
        cursor = existing
    if parts[-1] in cursor:
        raise RuntimeError(f"duplicate contribution at {dotted}")
    cursor[parts[-1]] = value


def contributions(root: Path) -> dict[str, dict[str, Any]]:
    bindings = load_bindings(root)
    values = load_values(root)
    if set(bindings) != set(values):
        raise RuntimeError(f"Map/settings coverage mismatch: map_only={sorted(set(bindings) - set(values))} settings_only={sorted(set(values) - set(bindings))}")
    by_source: dict[str, dict[str, Any]] = {}
    for setting, value in values.items():
        if setting in SPECIAL_CONTRIBUTIONS:
            assigned = SPECIAL_CONTRIBUTIONS[setting]
            if isinstance(value, list):
                composed = [item for source_value in assigned.values() for item in source_value]
                if len(composed) != len(set(composed)) or set(composed) != set(value):
                    raise RuntimeError(f"special composition no longer matches {setting}")
            elif list(assigned.values()) != [value]:
                raise RuntimeError(f"special scalar no longer matches {setting}")
            for source, source_value in assigned.items():
                assign_path(by_source.setdefault(source, {}), setting, source_value)
            continue
        sources = bindings[setting]
        if setting in {"structure.features.spec", "structure.features.realization"}:
            if not isinstance(value, list) or len(sources) != len(value):
                raise RuntimeError(f"feature contribution mismatch at {setting}")
            for source, item in zip(sources, value, strict=True):
                assign_path(by_source.setdefault(source, {}), setting, [item])
            continue
        if len(sources) != 1:
            raise RuntimeError(f"unresolved multi-source setting {setting}: {sources}")
        assign_path(by_source.setdefault(sources[0], {}), setting, value)
    return by_source


def render_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9_./:-]+", value):
        return value
    raise RuntimeError(f"unsupported Project Settings scalar: {value!r}")


def render_yaml(node: dict[str, Any] | list[Any], indent: int = 0) -> list[str]:
    prefix = " " * indent
    if isinstance(node, list):
        if not node:
            raise RuntimeError("empty Project Settings lists are not supported")
        return [f"{prefix}- {render_scalar(item)}" for item in node]
    lines: list[str] = []
    for key in sorted(node):
        value = node[key]
        if isinstance(value, (dict, list)):
            lines.append(f"{prefix}{key}:")
            lines.extend(render_yaml(value, indent + 2))
        else:
            lines.append(f"{prefix}{key}: {render_scalar(value)}")
    return lines


def revise_atom(path: Path, tree: dict[str, Any]) -> str:
    text = path.read_text(encoding="utf-8")
    first, separator, remainder = text.partition("\n")
    if first != "---" or not separator:
        raise RuntimeError(f"{path}: expected YAML frontmatter")
    boundary = remainder.find("\n---\n")
    if boundary < 0:
        raise RuntimeError(f"{path}: unterminated YAML frontmatter")
    frontmatter = remainder[:boundary]
    body = remainder[boundary + 5:]
    if re.search(r"(?m)^project_settings:", frontmatter):
        raise RuntimeError(f"{path}: project_settings already exists")
    version_match = re.findall(r"(?m)^version: ([1-9][0-9]*)$", frontmatter)
    updated_match = re.findall(r"(?m)^updated_at: .+$", frontmatter)
    if len(version_match) != 1 or len(updated_match) != 1:
        raise RuntimeError(f"{path}: invalid revision metadata")
    anchor = re.search(r"(?m)^(?:tier|version):", frontmatter)
    if anchor is None:
        raise RuntimeError(f"{path}: cannot place project_settings")
    block = "project_settings:\n" + "\n".join(render_yaml(tree, 2)) + "\n"
    revised_frontmatter = frontmatter[:anchor.start()] + block + frontmatter[anchor.start():]
    revised_frontmatter = re.sub(
        r"(?m)^version: [1-9][0-9]*$",
        f"version: {int(version_match[0]) + 1}",
        revised_frontmatter,
        count=1,
    )
    revised_frontmatter = re.sub(
        r"(?m)^updated_at: .+$",
        f"updated_at: {TIMESTAMP}",
        revised_frontmatter,
        count=1,
    )
    return f"---\n{revised_frontmatter}\n---\n{body}"


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


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    prepared: list[tuple[Path, str]] = []
    for source, tree in sorted(contributions(root).items()):
        path = active_atom(root, source)
        prepared.append((path, revise_atom(path, tree)))
    print(f"atoms={len(prepared)} apply={str(args.apply).lower()}")
    for path, _ in prepared:
        print(path.relative_to(root))
    if args.apply:
        for path, text in prepared:
            atomic_write(path, text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
