#!/usr/bin/env python3
"""Apply the bounded FPF-audit repair migration.

The migration is idempotent and fail-closed: it only writes the paths assigned
for the repair, converts only active RMED YAML carriers, and rejects relation
wrappers whose structure is not the registered relation-kind map.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
ROOT = next(parent for parent in SCRIPT_PATH.parents if (parent / ".git").exists())
TOOLS_ROOT = SCRIPT_PATH.parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
SESSION_ENVIRONMENT = "CAPRMEDIO_SESSION_ID"
PRIOR_VERSIONS = {
    # Existing Atoms renamed by this migration.  The values are recovered from
    # the corresponding HEAD carriers; new Atoms intentionally have no entry.
    ".caprmedio/04_requirement/CAPRMEDIO-REQU-003--apply-dry-across-caprmedio.md": 7,
    ".caprmedio/04_requirement/CAPRMEDIO-REQU-035--identify-necessary-information-by-confidence.md": 3,
    ".caprmedio/04_requirement/CAPRMEDIO-REQU-037--require-parent-coverage-without-claiming-topology-completeness.md": 4,
    ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-088--meta-eligibility-rule.md": 1,
    ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-092--authority-evaluation-and-ops-remain-distinct.md": 1,
    ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-113--coordinate-artifacts-without-an-81-type-bijection.md": 1,
    ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections.md": 1,
    ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-155--classify-rmed-atoms-by-applicability-tier.md": 5,
    ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-290--exclude-secrets-from-dset.md": 1,
    ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-338--register-the-project-work-journal.md": 1,
    ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-370--register-closed-gov-subject-scope-vocabulary.md": 1,
}
SKIP = {"archive", "drafts", "done", "solved"}
SCOPE_ROOTS = {
    "project": ROOT / ".caprmedio/04_requirement",
    "meta": ROOT / ".caprmedio/100_LAYER_1_META/04_requirement",
    "gov": ROOT / ".caprmedio/200_LAYER_2_GOV/04_requirement",
}
RMED_ROOTS = (
    ROOT / ".caprmedio/04_requirement",
    ROOT / ".caprmedio/06_evaluation",
    ROOT / ".caprmedio/100_LAYER_1_META/04_requirement",
    ROOT / ".caprmedio/100_LAYER_1_META/05_method",
    ROOT / ".caprmedio/100_LAYER_1_META/06_evaluation",
    ROOT / ".caprmedio/100_LAYER_1_META/07_delivery",
    ROOT / ".caprmedio/200_LAYER_2_GOV/04_requirement",
    ROOT / ".caprmedio/200_LAYER_2_GOV/05_method",
    ROOT / ".caprmedio/200_LAYER_2_GOV/06_evaluation",
    ROOT / ".caprmedio/200_LAYER_2_GOV/07_delivery",
)
TOP = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*:(?:\s|$)")


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = atomic_tempfile(path, "migrations")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text.rstrip() + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def rel(path: str) -> Path:
    return ROOT / path


def operator_timestamp(value: str | None = None) -> str:
    timestamp = value or dt.datetime.now().astimezone().strftime(TIMESTAMP_FORMAT)
    try:
        dt.datetime.strptime(timestamp, TIMESTAMP_FORMAT)
    except ValueError as exc:
        raise RuntimeError(f"invalid operator timestamp: {timestamp!r}") from exc
    return timestamp


def runtime_session(session_id: str | None = None) -> str | None:
    value = session_id or os.environ.get(SESSION_ENVIRONMENT)
    if not value:
        raw = os.environ.get("CODEX_SESSION_ID")
        value = f"codex:{raw}" if raw else ""
    value = value.strip()
    return value or None


def prior_version(path: Path) -> int:
    return PRIOR_VERSIONS.get(path.relative_to(ROOT).as_posix(), 0)


def split_yaml(path: Path, text: str | None = None) -> tuple[list[str], list[str]]:
    source = text if text is not None else path.read_text(encoding="utf-8")
    lines = source.splitlines()
    if not lines or lines[0] != "---":
        raise RuntimeError(f"{path}: expected YAML frontmatter")
    try:
        close = lines.index("---", 1)
    except ValueError as exc:
        raise RuntimeError(f"{path}: unclosed YAML frontmatter") from exc
    return lines[1:close], lines[close + 1 :]


def blocks(front: list[str], path: Path) -> list[tuple[str, list[str]]]:
    result: list[tuple[str, list[str]]] = []
    key: str | None = None
    lines: list[str] = []
    for line in front:
        if TOP.match(line):
            if key is not None:
                result.append((key, lines))
            key = line.split(":", 1)[0]
            lines = [line]
        else:
            if key is None:
                raise RuntimeError(f"{path}: frontmatter before top-level key")
            lines.append(line)
    if key is not None:
        result.append((key, lines))
    names = [name for name, _ in result]
    if len(names) != len(set(names)):
        raise RuntimeError(f"{path}: duplicate frontmatter key")
    return result



def revision_values(path: Path, text: str) -> tuple[int | None, str | None]:
    front, _ = split_yaml(path, text)
    values: dict[str, str] = {}
    for key, block in blocks(front, path):
        if key not in {"version", "updated_at"}:
            continue
        if len(block) != 1:
            raise RuntimeError(f"{path}: {key} must be a scalar")
        values[key] = block[0].split(":", 1)[1].strip()
    version = values.get("version")
    updated_at = values.get("updated_at")
    if version is None and updated_at is None:
        return None, None
    if version is None or updated_at is None:
        raise RuntimeError(f"{path}: version and updated_at must be supplied together")
    if not version.isdigit() or int(version) < 1:
        raise RuntimeError(f"{path}: invalid Atom version {version!r}")
    operator_timestamp(updated_at)
    return int(version), updated_at


def without_revision(path: Path, text: str) -> str:
    front, body = split_yaml(path, text)
    kept: list[str] = []
    for key, block in blocks(front, path):
        if key not in {"version", "updated_at"}:
            kept.extend(block)
    return "\n".join(["---", *kept, "---", *body]).rstrip() + "\n"


def session_block(path: Path, text: str) -> list[str] | None:
    front, _ = split_yaml(path, text)
    for key, block in blocks(front, path):
        if key == "llm_session_ids":
            return block
    return None


def insert_revision(path: Path, text: str, version: int, updated_at: str) -> str:
    front, body = split_yaml(path, text)
    revised: list[str] = []
    inserted = False
    for key, block in blocks(front, path):
        if key == "llm_session_ids" and not inserted:
            revised.extend([f"version: {version}", f"updated_at: {updated_at}"])
            inserted = True
        revised.extend(block)
    if not inserted:
        revised.extend([f"version: {version}", f"updated_at: {updated_at}"])
    return "\n".join(["---", *revised, "---", *body]).rstrip() + "\n"


def parse_relation_block(block: list[str], path: Path) -> dict[str, list[str]]:
    payload = block[1:]
    if not payload:
        return {}
    result: dict[str, list[str]] = {}
    index = 0
    if payload[0].startswith("  - type:"):
        while index < len(payload):
            line = payload[index]
            if not line.startswith("  - type: "):
                raise RuntimeError(f"{path}: unexpected legacy relation line {line!r}")
            kind = line.removeprefix("  - type: ").strip()
            index += 1
            if index >= len(payload) or payload[index] != "    targets:":
                raise RuntimeError(f"{path}: legacy relation {kind} has no targets list")
            index += 1
            targets: list[str] = []
            while index < len(payload) and payload[index].startswith("      - "):
                targets.append(payload[index].removeprefix("      - ").strip())
                index += 1
            if not kind or not targets or kind in result or len(targets) != len(set(targets)):
                raise RuntimeError(f"{path}: invalid legacy relation {kind}")
            result[kind] = targets
        return result
    while index < len(payload):
        line = payload[index]
        match = re.fullmatch(r"  ([a-z][a-z0-9_]*):", line)
        if not match:
            raise RuntimeError(f"{path}: invalid relation-kind map line {line!r}")
        kind = match.group(1)
        index += 1
        targets: list[str] = []
        while index < len(payload) and payload[index].startswith("    - "):
            targets.append(payload[index].removeprefix("    - ").strip())
            index += 1
        if not targets or kind in result or len(targets) != len(set(targets)):
            raise RuntimeError(f"{path}: invalid relation-kind map for {kind}")
        result[kind] = targets
    return result


def render_relations(mapping: dict[str, list[str]]) -> list[str]:
    if not mapping:
        return []
    lines = ["relations:"]
    for kind, targets in mapping.items():
        if not targets or len(targets) != len(set(targets)):
            raise RuntimeError(f"invalid relation output for {kind}")
        lines.append(f"  {kind}:")
        lines.extend(f"    - {target}" for target in targets)
    return lines


def normalized_frontmatter(path: Path) -> tuple[list[tuple[str, list[str]]], list[str]]:
    front, body = split_yaml(path)
    result: list[tuple[str, list[str]]] = []
    found_scope = False
    for key, block in blocks(front, path):
        if key == "subject_scope":
            if len(block) != 1:
                raise RuntimeError(f"{path}: singular subject_scope is not scalar")
            value = block[0].split(":", 1)[1].strip()
            if not value:
                raise RuntimeError(f"{path}: empty singular subject_scope")
            result.append(("subject_scopes", ["subject_scopes:", f"  - {value}"]))
            found_scope = True
        elif key == "subject_scopes":
            if found_scope:
                raise RuntimeError(f"{path}: both subject scope forms")
            found_scope = True
            result.append((key, block))
        elif key == "relations":
            result.append((key, render_relations(parse_relation_block(block, path))))
        else:
            result.append((key, block))
    if not found_scope:
        raise RuntimeError(f"{path}: RMED carrier lacks subject_scopes")
    return result, body


def write_blocks(path: Path, source: list[tuple[str, list[str]]], body: list[str]) -> None:
    front: list[str] = []
    for _, block in source:
        front.extend(block)
    atomic_write(path, "\n".join(["---", *front, "---", *body]))


def normalize_rmed(path: Path) -> None:
    items, body = normalized_frontmatter(path)
    revised: list[tuple[str, list[str]]] = []
    for key, block in items:
        if key == "artifact_subtype":
            if block != ["artifact_subtype: technical_decision"]:
                revised.append((key, block))
            else:
                revised.append((key, ["artifact_subtype: implementation_decision"]))
        else:
            revised.append((key, block))
    write_blocks(path, revised, body)


def relation_map(path: Path) -> tuple[list[tuple[str, list[str]]], list[str], dict[str, list[str]]]:
    items, body = normalized_frontmatter(path)
    mapped = {key: block for key, block in items}
    relations = parse_relation_block(mapped["relations"], path) if "relations" in mapped else {}
    return items, body, relations


def replace_relations(path: Path, mapping: dict[str, list[str]]) -> None:
    items, body = normalized_frontmatter(path)
    result: list[tuple[str, list[str]]] = []
    inserted = False
    for key, block in items:
        if key == "relations":
            if mapping:
                result.append(("relations", render_relations(mapping)))
            inserted = True
        else:
            result.append((key, block))
    if mapping and not inserted:
        result.append(("relations", render_relations(mapping)))
    write_blocks(path, result, body)


def active(path: Path) -> bool:
    return not any(part in SKIP for part in path.parts)


def scope_tier(path: Path) -> tuple[str, int] | None:
    if "100_LAYER_1_META" in path.parts:
        scope = "meta"
    elif "200_LAYER_2_GOV" in path.parts:
        scope = "gov"
    elif path.parent in {ROOT / ".caprmedio/04_requirement", ROOT / ".caprmedio/06_evaluation"}:
        scope = "project"
    else:
        return None
    text = path.read_text(encoding="utf-8")
    tier = re.search(r"^tier: (principle|core|standard)$", text, re.M)
    name = tier.group(1) if tier else "standard"
    rank = {"principle": 0, "core": 1, "standard": 2}[name]
    return scope, rank


def full_active_stems() -> set[str]:
    return {
        path.stem
        for path in (ROOT / ".caprmedio").rglob("*.md")
        if active(path) and not path.is_symlink()
    }


def active_replacements() -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for path in (ROOT / ".caprmedio").rglob("*.md"):
        if not active(path) or path.is_symlink() or not path.read_text(encoding="utf-8").startswith("---\n"):
            continue
        try:
            _, _, relations = relation_map(path)
        except RuntimeError:
            continue
        for old in relations.get("replacement_of", []):
            mapping.setdefault(old, []).append(path.stem)
    return mapping


def repair_child_graph() -> None:
    paths = [
        path
        for directory in RMED_ROOTS
        if directory.exists()
        for path in directory.glob("*.md")
        if active(path) and "-CATL-" not in path.stem
    ]
    by_stem = {path.stem: path for path in paths}
    active_stems = full_active_stems()
    replacements = active_replacements()
    for path in paths:
        _, _, relations = relation_map(path)
        children = relations.get("child_of", [])
        revised: list[str] = []
        changed = False
        for target in children:
            if target not in active_stems:
                candidates = replacements.get(target, [])
                if len(candidates) != 1:
                    raise RuntimeError(f"{path}: child_of target {target} has no unique active successor")
                target = candidates[0]
                changed = True
            source_coord = scope_tier(path)
            target_path = by_stem.get(target)
            target_coord = scope_tier(target_path) if target_path else None
            if source_coord and target_coord and source_coord[0] == target_coord[0] and source_coord[1] == target_coord[1]:
                changed = True
                continue
            revised.append(target)
        if changed:
            if revised:
                relations["child_of"] = revised
            else:
                relations.pop("child_of", None)
            replace_relations(path, relations)
    additions = {
        "CAPRMEDIO-GOV-REQU-334--validate-the-routing-tree": ["CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully"],
        "CAPRMEDIO-GOV-REQU-336--resolve-skill-routing-precedence": ["CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully"],
        "CAPRMEDIO-GOV-REQU-370--register-closed-gov-subject-scope-vocabulary": [
            "CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully",
            "CAPRMEDIO-META-REQU-175--use-canonical-meta-subject-scopes",
        ],
        "CAPRMEDIO-GOV-REQU-339--register-work-journal-events": ["CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance"],
        "CAPRMEDIO-GOV-REQU-340--recover-work-journal-coverage-without-invention": ["CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance"],
        "CAPRMEDIO-GOV-REQU-347--mirror-every-atom-edit-in-git": ["CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance"],
        "CAPRMEDIO-META-REQU-093--analysis-and-ops-fact-boundary": ["CAPRMEDIO-META-REQU-111--nine-content-roles-with-plan"],
        "CAPRMEDIO-META-REQU-094--mechanism-neutral-evaluation-atoms": ["CAPRMEDIO-META-REQU-111--nine-content-roles-with-plan"],
        "CAPRMEDIO-META-REQU-149--keep-conflict-discovery-in-exploration-mode": ["CAPRMEDIO-META-REQU-114--preserve-content-role-boundaries-through-caprmedio-loop"],
        "CAPRMEDIO-META-REQU-639--realize-recurrence-evaluation-through-implementation": ["CAPRMEDIO-META-REQU-091--normative-atoms-are-the-caprmedio-specification"],
        "CAPRMEDIO-META-REQU-640--record-recurrence-check-outcomes-in-ops": ["CAPRMEDIO-META-REQU-091--normative-atoms-are-the-caprmedio-specification"],
        "CAPRMEDIO-GOV-REQU-645--reconcile-materialized-representations": ["CAPRMEDIO-REQU-644--admit-necessary-materialized-representations"],
    }
    for stem, parents in additions.items():
        path = by_stem[stem]
        _, _, relations = relation_map(path)
        current = relations.get("child_of", [])
        relations["child_of"] = [*current, *(parent for parent in parents if parent not in current)]
        replace_relations(path, relations)
    for path in paths:
        scope = scope_tier(path)
        if not scope or scope[0] != "gov" or path.stem == "CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully":
            continue
        _, _, relations = relation_map(path)
        if relations.get("child_of"):
            continue
        relations["child_of"] = ["CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully"]
        replace_relations(path, relations)


def update_project_settings_evaluation() -> None:
    old = "CAPRMEDIO-GOV-REQU-456--separate-route-catalog-and-project-whitelist"
    new = "CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-governed-authority-and-project-settings"
    for number in ("002", "006"):
        path = next((ROOT / ".caprmedio/200_LAYER_2_GOV/06_evaluation").glob(f"CAPRMEDIO-GOV-EVAL-{number}--*.md"))
        _, _, relations = relation_map(path)
        targets = relations.get("check_of", [])
        if old in targets:
            relations["check_of"] = [new if target == old else target for target in targets]
            replace_relations(path, relations)
        text = path.read_text(encoding="utf-8")
        if ".caprmedio/caprmedio_settings.toml" in text:
            atomic_write(path, text.replace(".caprmedio/caprmedio_settings.toml", ".caprmedio/caprmedio_project_settings.toml"))


def repair_stale_strict_relations() -> None:
    replacements = {
        "CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages": {
            "CAPRMEDIO-META-REQU-248--three-artifact-forms": "CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections",
            "CAPRMEDIO-META-REQU-260--one-independently-replaceable-claim-per-atom": "CAPRMEDIO-META-REQU-154--semantic-irreducibility",
        },
        "CAPRMEDIO-GOV-REQU-304--expandable-scope-path-identities": {
            "CAPRMEDIO-GOV-REQU-474--register-current-type-prefixes": "CAPRMEDIO-GOV-REQU-323--register-caprmedio-type-prefixes",
        },
        "CAPRMEDIO-GOV-REQU-313--govern-catalog-map-and-hub-projections": {
            "CAPRMEDIO-GOV-REQU-456--separate-route-catalog-and-project-whitelist": "CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-governed-authority-and-project-settings",
        },
        "CAPRMEDIO-GOV-REQU-311--atomic-revision-change-classes": {
            "CAPRMEDIO-META-REQU-260--one-independently-replaceable-claim-per-atom": "CAPRMEDIO-META-REQU-154--semantic-irreducibility",
        },
        "CAPRMEDIO-GOV-REQU-293--constraints-are-external": {
            "CAPRMEDIO-GOV-REQU-470--register-current-atom-type-surface": "CAPRMEDIO-GOV-REQU-321--register-caprmedio-atom-type-surface",
        },
        "CAPRMEDIO-GOV-REQU-314--production-evaluation-checklists": {
            "CAPRMEDIO-GOV-REQU-470--register-current-atom-type-surface": "CAPRMEDIO-GOV-REQU-321--register-caprmedio-atom-type-surface",
        },
        "CAPRMEDIO-GOV-METH-004--bounded-scripted-migrations": {
            "CAPRMEDIO-GOV-REQU-474--register-current-type-prefixes": "CAPRMEDIO-GOV-REQU-323--register-caprmedio-type-prefixes",
        },
    }
    drops = {
        "CAPRMEDIO-GOV-CNST-001--github-preview-compatibility": {"CAPRMEDIO-META-REQU-259--nonduplicative-current-artifact-properties"},
        "CAPRMEDIO-GOV-REQU-314--production-evaluation-checklists": {"CAPRMEDIO-GOV-REQU-464--meta-and-gov-subject-scope-vocabularies"},
        "CAPRMEDIO-GOV-REQU-308--plain-scalar-frontmatter-values": {"CAPRMEDIO-META-REQU-259--nonduplicative-current-artifact-properties"},
        "CAPRMEDIO-GOV-REQU-341--centralize-plan-carriers-by-default": {
            "CAPRMEDIO-GOV-REQU-477--register-change-plan-subtype",
            "CAPRMEDIO-GOV-REQU-481--use-flat-numbered-layer-feature-layout",
        },
    }
    by_stem = {
        path.stem: path
        for directory in RMED_ROOTS
        if directory.exists()
        for path in directory.glob("*.md")
        if active(path) and "-CATL-" not in path.stem
    }
    for stem, substitution in replacements.items():
        path = by_stem[stem]
        _, _, relations = relation_map(path)
        for kind, targets in list(relations.items()):
            relations[kind] = [substitution.get(target, target) for target in targets]
        replace_relations(path, relations)
    for stem, targets_to_drop in drops.items():
        path = by_stem[stem]
        _, _, relations = relation_map(path)
        for kind in list(relations):
            remaining = [target for target in relations[kind] if target not in targets_to_drop]
            if remaining:
                relations[kind] = remaining
            else:
                del relations[kind]
        replace_relations(path, relations)


def update_renamed_settings_references() -> None:
    old = ".caprmedio/caprmedio_settings.toml"
    new = ".caprmedio/caprmedio_project_settings.toml"
    for directory in (ROOT / ".caprmedio/04_requirement", ROOT / ".caprmedio/06_evaluation", ROOT / ".caprmedio/100_LAYER_1_META", ROOT / ".caprmedio/200_LAYER_2_GOV"):
        for path in directory.rglob("*.md"):
            if not active(path) or path.is_symlink():
                continue
            text = path.read_text(encoding="utf-8")
            revised = text.replace(old, new).replace("`caprmedio_settings.toml`", "`caprmedio_project_settings.toml`")
            if revised != text:
                atomic_write(path, revised)


def settings() -> None:
    path = ROOT / "caprmedio_framework_settings.toml"
    desired = """# CAPRMEDIO framework-engine settings.

[confidence]
# Accepted values are integer percentages from 0 through 100.
necessary_information_threshold_percent = 95
semantic_resolution_threshold_percent = 95
"""
    current = path.read_text(encoding="utf-8") if path.is_file() else ""
    if current != desired:
        atomic_write(path, desired)
    link = ROOT / ".caprmedio/000_caprmedio_framework/caprmedio_framework_settings.toml"
    if link.is_symlink() and os.readlink(link) != "../../caprmedio_framework_settings.toml":
        raise RuntimeError(f"{link}: unexpected existing symlink")
    if not link.exists() and not link.is_symlink():
        os.symlink("../../caprmedio_framework_settings.toml", link)
    old = ROOT / ".caprmedio/caprmedio_settings.toml"
    if old.exists() or old.is_symlink():
        raise RuntimeError("retired caprmedio_settings.toml remains present")


def journal(updated_at: str, session_id: str | None) -> None:
    path = ROOT / ".caprmedio/010_journals/src-work-journal-2026-08-18.ndjson"
    event = {
        "action_id": "4f5b4ef0-4151-47ed-afb2-b38d6037a2f2",
        "details": {"archived_requirements": 2, "created_requirements": 13, "migrated_active_rmed_carriers": True, "settings_carriers": 2},
        "event": "completed",
        "event_id": "17e99a80-9ca5-442f-a027-9d87e773d0ee",
        "governed_subjects": [
            "CAPRMEDIO-REQU-003",
            "CAPRMEDIO-REQU-035",
            "CAPRMEDIO-REQU-642",
            "CAPRMEDIO-EVAL-001",
            "CAPRMEDIO-META-REQU-088",
            "CAPRMEDIO-META-REQU-113",
            "CAPRMEDIO-META-REQU-124",
            "CAPRMEDIO-META-REQU-125",
            "CAPRMEDIO-META-REQU-155",
            "CAPRMEDIO-GOV-REQU-338",
        ],
        "kind": "authority_change",
        "occurred_at": updated_at,
        "operation": "apply_fpf_audit_repairs",
        "produced_outputs": [
            "caprmedio_framework_settings.toml",
            ".caprmedio/caprmedio_project_settings.toml",
            "active_strict_rmed_relation_kind_maps",
        ],
        "schema_version": 1,
        "structural_scope": "project",
    }
    if session_id:
        event["session_id"] = session_id
    line = json.dumps(event, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if '"event_id":"17e99a80-9ca5-442f-a027-9d87e773d0ee"' not in existing:
        atomic_write(path, existing + ("" if not existing or existing.endswith("\n") else "\n") + line + "\n")
    existing = path.read_text(encoding="utf-8")
    correction = {
        "action_id": "4f5b4ef0-4151-47ed-afb2-b38d6037a2f2",
        "details": {"actual_created_requirements": 11, "corrected_event_id": "17e99a80-9ca5-442f-a027-9d87e773d0ee", "incorrect_created_requirements": 13},
        "event": "recovered",
        "event_id": "8f40bde6-3f3e-48e7-8b3e-5f3a0d204e60",
        "governed_subjects": ["CAPRMEDIO-REQU-644", "CAPRMEDIO-REQU-646", "CAPRMEDIO-GOV-REQU-645", "CAPRMEDIO-GOV-REQU-647"],
        "kind": "authority_change",
        "occurred_at": updated_at,
        "operation": "correct_fpf_audit_repair_journal_count",
        "preceding_event": "17e99a80-9ca5-442f-a027-9d87e773d0ee",
        "produced_outputs": [],
        "schema_version": 1,
        "structural_scope": "project",
    }
    if session_id:
        correction["session_id"] = session_id
    correction_line = json.dumps(correction, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    if '"event_id":"8f40bde6-3f3e-48e7-8b3e-5f3a0d204e60"' not in existing:
        atomic_write(path, existing + ("" if existing.endswith("\n") else "\n") + correction_line + "\n")


def requirement(
    path: str,
    subject: str,
    parents: list[str],
    body: str,
    tier: str | None = None,
    replacements: list[str] | None = None,
    *,
    updated_at: str | None = None,
    session_id: str | None = None,
) -> str:
    target = rel(path) if path else None
    timestamp = operator_timestamp(updated_at)
    existing = target.read_text(encoding="utf-8") if target and target.exists() else None
    existing_sessions = session_block(target, existing) if target and existing else None
    sessions = existing_sessions
    if sessions is None:
        runtime = runtime_session(session_id)
        sessions = ["llm_session_ids:", f"  - {runtime}"] if runtime else None

    semantic_front = ["subject_scopes:", f"  - {subject}"]
    if tier:
        semantic_front.append(f"tier: {tier}")
    if sessions:
        semantic_front.extend(sessions)
    semantic_front.extend(["relations:", "  child_of:"])
    semantic_front.extend(f"    - {parent}" for parent in parents)
    if replacements:
        semantic_front.append("  replacement_of:")
        semantic_front.extend(f"    - {replacement}" for replacement in replacements)
    semantic_candidate = "\n".join(["---", *semantic_front, "---", *body.strip().splitlines()]).rstrip() + "\n"

    current_version = current_updated_at = None
    if existing:
        current_version, current_updated_at = revision_values(target, existing)
        same_semantics = without_revision(target, existing) == semantic_candidate
        if same_semantics and current_version is not None and current_updated_at is not None:
            return existing
        else:
            version = (current_version or prior_version(target)) + 1 if (current_version or prior_version(target)) else 1
            revision_time = timestamp
    else:
        previous = prior_version(target) if target else 0
        version = previous + 1 if previous else 1
        revision_time = timestamp

    front = ["---", "subject_scopes:", f"  - {subject}"]
    if tier:
        front.append(f"tier: {tier}")
    front.extend([f"version: {version}", f"updated_at: {revision_time}"])
    if sessions:
        front.extend(sessions)
    front.extend(["relations:", "  child_of:"])
    front.extend(f"    - {parent}" for parent in parents)
    if replacements:
        front.append("  replacement_of:")
        front.extend(f"    - {replacement}" for replacement in replacements)
    front.extend(["---", body.strip()])
    return "\n".join(front) + "\n"


EVALUATION_TEMPLATE = """---
artifact_subtype: qa_case
subject_scopes:
  - authority
relations:
  evaluation_for:
    - CAPRMEDIO-REQU-002--apply-mece-to-canonical-decompositions
    - CAPRMEDIO-REQU-642--govern-canonical-decomposition-conformance
  child_of:
    - CAPRMEDIO-REQU-642--govern-canonical-decomposition-conformance
---
# Canonical decomposition conformance

## Claim checked

Every canonical decomposition satisfies REQU-002 and REQU-642.

## Check

For each declared axis, enumerate the bounded universe and classify every admissible member. Report any missing universe or axis declaration, unclassified member, multiple same-axis assignments, or forced near match without changing the governed decomposition.

## Acceptance

Pass only when no conformance issue is found.

## Failure

Record each issue as a Concern against the narrowest owning scope.
"""


def evaluation_conformance(*, updated_at: str | None, session_id: str | None) -> str:
    path = ROOT / ".caprmedio/06_evaluation/CAPRMEDIO-EVAL-001--canonical-decomposition-conformance.md"
    existing = path.read_text(encoding="utf-8") if path.exists() else None
    sessions = session_block(path, existing) if existing else None
    if sessions is None:
        runtime = runtime_session(session_id)
        sessions = ["llm_session_ids:", f"  - {runtime}"] if runtime else None
    semantic = EVALUATION_TEMPLATE
    if sessions:
        semantic = semantic.replace("\nrelations:\n", "\n" + "\n".join(sessions) + "\nrelations:\n", 1)
    timestamp = operator_timestamp(updated_at)
    if existing:
        current_version, current_updated_at = revision_values(path, existing)
        if current_version is not None and current_updated_at is not None and without_revision(path, existing) == semantic:
            return existing
        previous = current_version or prior_version(path)
        version = previous + 1 if previous else 1
    else:
        version = 1
    return insert_revision(path, semantic, version, timestamp)


def replacements(*, updated_at: str | None = None, session_id: str | None = None) -> dict[str, str]:
    project_principle = "CAPRMEDIO-REQU-003--apply-dry-across-caprmedio"
    gov_core = "CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully"
    return {
        ".caprmedio/04_requirement/CAPRMEDIO-REQU-003--apply-dry-across-caprmedio.md": requirement(
            ".caprmedio/04_requirement/CAPRMEDIO-REQU-003--apply-dry-across-caprmedio.md", "principles", ["CAPRMEDIO-GOAL-001--enable-any-operator-to-build-a-working-system"],
            "# Apply DRY across CAPRMEDIO\n\nCAPRMEDIO must store and maintain each governed meaning under one canonical owner whenever that owner can resolve the meaning completely and unambiguously; every other use must reference, derive, generate, or adapt that owner.",
            "principle",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/04_requirement/CAPRMEDIO-REQU-035--identify-necessary-information-by-confidence.md": requirement(
            ".caprmedio/04_requirement/CAPRMEDIO-REQU-035--identify-necessary-information-by-confidence.md", "authority", ["CAPRMEDIO-REQU-034--scale-through-structure"],
            "# Identify necessary information by confidence\n\nTo determine whether project information is necessary, an LLM must inspect every active Project Principle, every active Atom in the information's full ancestor and descendant lineage, and every other active Atom in the same structural scope. The information is necessary when its omission would leave the LLM below the effective framework-owned confidence threshold configured for the active framework engine. The confidence and threshold are operational heuristics, not comparable probabilities across configurations.",
            "core",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/04_requirement/CAPRMEDIO-REQU-037--require-parent-coverage-without-claiming-topology-completeness.md": requirement(
            ".caprmedio/04_requirement/CAPRMEDIO-REQU-037--require-parent-coverage-without-claiming-topology-completeness.md", "requirement-topology", ["CAPRMEDIO-REQU-029--govern-each-scope-by-authority-mode"],
            "# Require parent coverage without claiming topology completeness\n\nIn strict authority mode, every active tier-classified RMED Atom other than the Project Goal must have at least one permitted active parent: the Project Goal Requirement, an applicable lower-global-tier Atom in the same structural scope, or an Atom permitted by the global tier topology in an ancestor structural scope. This parent-coverage condition is necessary but insufficient for authority-topology completeness and cannot establish Principle-set completeness.",
            replacements=["CAPRMEDIO-REQU-077--require-core-coverage-without-claiming-principle-completeness"],
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/04_requirement/CAPRMEDIO-REQU-644--admit-necessary-materialized-representations.md": requirement(
            ".caprmedio/04_requirement/CAPRMEDIO-REQU-644--admit-necessary-materialized-representations.md", "authority", [project_principle],
            "# Admit necessary materialized representations\n\nCAPRMEDIO may admit a materialized representation only when an explicit Requirement establishes that the representation is necessary for an external contract, portability, performance, availability, audit snapshot, or independently usable publication.",
            "core",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/04_requirement/CAPRMEDIO-REQU-646--govern-project-settings-projection-through-framework-methodology.md": requirement(
            ".caprmedio/04_requirement/CAPRMEDIO-REQU-646--govern-project-settings-projection-through-framework-methodology.md", "authority", ["CAPRMEDIO-REQU-622--establish-project-configuration-through-rmed"],
            "# Govern Project Settings Projection through framework methodology\n\nCAPRMEDIO framework methodology and implementation must define deterministic Project Settings Projection source selection, composition, precedence, and validation without introducing a third settings carrier.",
            replacements=["CAPRMEDIO-REQU-628--place-project-settings-projection-rules-in-the-root-realization"],
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/06_evaluation/CAPRMEDIO-EVAL-001--canonical-decomposition-conformance.md": evaluation_conformance(updated_at=updated_at, session_id=session_id),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-088--meta-eligibility-rule.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-088--meta-eligibility-rule.md", "authority", ["CAPRMEDIO-REQU-002--apply-mece-to-canonical-decompositions"],
            "# META eligibility rule\n\nA rule belongs in META only when it remains true as downstream languages, tools, hosts, providers, and repository layouts change, governs multiple layers or defines a boundary between layers, and can be stated without importing downstream implementation concepts.",
            "core", ["CAPRMEDIO-META-REQU-200--meta-eligibility-rule"],
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-113--coordinate-artifacts-without-an-81-type-bijection.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-113--coordinate-artifacts-without-an-81-type-bijection.md", "artifact-model", ["CAPRMEDIO-REQU-002--apply-mece-to-canonical-decompositions"],
            "# Coordinate artifacts without an 81 Type bijection\n\nEvery governed artifact occupies exactly one semantic coordinate in the three-axis classification space Artifact form × Content role × Governance locus; the space does not require a distinct Type name or admitted Artifact for every coordinate.",
            "core", ["CAPRMEDIO-META-REQU-257--coordinate-artifacts-without-a-72-type-bijection"],
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-124--make-requirement-the-only-universally-mandatory-atom.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-124--make-requirement-the-only-universally-mandatory-atom.md", "semantics", ["CAPRMEDIO-REQU-006--minimal-default-project-model", "CAPRMEDIO-REQU-002--apply-mece-to-canonical-decompositions"],
            "# Make Requirement the only universally mandatory Atom\n\nEvery governed development change that proceeds toward realization has at least one Requirement Atom, and Requirement is the only universally mandatory CAPRMEDIO atomic role.",
            "core",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections.md", "artifact-model", ["CAPRMEDIO-REQU-002--apply-mece-to-canonical-decompositions"],
            "# Three Artifact forms with generated Projections\n\nEvery governed artifact has exactly one Artifact form: Atom, Journal, or Projection.",
            "core", ["CAPRMEDIO-META-REQU-248--three-artifact-forms"],
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-155--classify-rmed-atoms-by-applicability-tier.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-155--classify-rmed-atoms-by-applicability-tier.md", "authority", ["CAPRMEDIO-REQU-002--apply-mece-to-canonical-decompositions", "CAPRMEDIO-REQU-044--organize-authority-as-a-hierarchical-graph", "CAPRMEDIO-REQU-045--separate-hierarchy-dimensions"],
            "# Classify RMED Atoms by applicability tier\n\nWhen a CAPRMEDIO project enables applicability-tier classification, each classified Requirement, Method, Evaluation, and Delivery Atom resolves to exactly one readable tier name in the project-configured ordered tier catalog.",
            "core",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-092--authority-evaluation-and-ops-remain-distinct.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-092--authority-evaluation-and-ops-remain-distinct.md", "authority", ["CAPRMEDIO-REQU-002--apply-mece-to-canonical-decompositions"],
            "# Authority, Evaluation, and Ops remain distinct\n\nCAPRMEDIO distinguishes authoritative Requirements, Methods, Evaluation criteria, and Delivery rules; concrete Implementations of those accepted claims; enacted execution, factual Ops records, and claim-bound evidence; and verification judgments about sufficiency and currentness. Evaluation material, evaluations, evidence, dashboards, and verification judgments may support, challenge, or invalidate reliance on a claim, but cannot establish, edit, replace, or override semantic authority.",
            replacements=["CAPRMEDIO-META-REQU-205--authority-and-evaluation-separation"],
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-169--record-every-projection-rebuild-in-a-journal.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-169--record-every-projection-rebuild-in-a-journal.md", "lifecycle-traceability", ["CAPRMEDIO-REQU-007--full-minimal-traceability"],
            "# Record every Projection rebuild in a Journal\n\nEvery Projection rebuild attempt must produce append-only Journal provenance from its start through exactly one terminal outcome, binding the target Projection, declared source frontier, generator, configuration, and produced revision when successful.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-638--define-concrete-recurrence-protection-as-evaluation.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-638--define-concrete-recurrence-protection-as-evaluation.md", "continuous-improvement", ["CAPRMEDIO-REQU-637--establish-recurrence-protection"],
            "# Define concrete recurrence protection as Evaluation\n\nEach concrete recurrence protection must be represented by an Evaluation Atom that defines one mechanism-neutral bounded check for the corrected failure class.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-648--classify-operator-mandated-constitutional-substrates.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-648--classify-operator-mandated-constitutional-substrates.md", "authority", ["CAPRMEDIO-META-REQU-088--meta-eligibility-rule"],
            "# Classify operator-mandated constitutional substrates\n\nA concrete substrate belongs in META only when the operator makes it mandatory and non-substitutable for CAPRMEDIO governance.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-655--define-atom-artifact-form.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-655--define-atom-artifact-form.md", "artifact-model", ["CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections"],
            "# Define Atom Artifact form\n\nAn Atom is the smallest independently governed unit under its Content role's atomicity model, with one stable identity and one indivisible lifecycle.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-656--define-journal-artifact-form.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-656--define-journal-artifact-form.md", "artifact-model", ["CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections"],
            "# Define Journal Artifact form\n\nA Journal is an ordered sequence of admitted records whose accepted records cannot be edited, reordered, or removed.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-657--define-projection-artifact-form.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-657--define-projection-artifact-form.md", "artifact-model", ["CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections"],
            "# Define Projection Artifact form\n\nA Projection is a non-authoritative generated view reproducibly derived from declared governed sources and never edited as its source of meaning.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-658--define-principle-applicability-tier.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-658--define-principle-applicability-tier.md", "authority", ["CAPRMEDIO-META-REQU-155--classify-rmed-atoms-by-applicability-tier"],
            "# Define Principle applicability tier\n\nThe Principle tier is a project-wide invariant that constrains deeper tiers and may have no direct application by itself.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-659--define-core-applicability-tier.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-659--define-core-applicability-tier.md", "authority", ["CAPRMEDIO-META-REQU-155--classify-rmed-atoms-by-applicability-tier"],
            "# Define Core applicability tier\n\nThe Core tier governs the complete declared Project or structural scope.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-660--define-standard-applicability-tier.md": requirement(
            ".caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-660--define-standard-applicability-tier.md", "authority", ["CAPRMEDIO-META-REQU-155--classify-rmed-atoms-by-applicability-tier"],
            "# Define Standard applicability tier\n\nThe Standard tier governs one proper semantic subsegment of its declared scope.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-338--register-the-project-work-journal.md": requirement(
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-338--register-the-project-work-journal.md", "provenance", ["CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance"],
            "# Register the Project Work Journal\n\nGOV must register `.caprmedio/010_journals/` as the canonical home of one project-wide logical Work Journal composed of collision-resistant append-only NDJSON segments. Accepted records and sealed segments must never be edited, reordered, or deleted; segmentation must preserve deterministic total replay order.",
            replacements=["CAPRMEDIO-GOV-REQU-484--keep-governed-journals-in-role-folders"],
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-356--encode-atom-revision-properties.md": requirement(
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-356--encode-atom-revision-properties.md", "carrier-format", ["CAPRMEDIO-META-REQU-165--atoms-have-version-and-updated-at", gov_core],
            "# Encode Atom revision properties\n\nEvery Atom revision encoding carries `version` as a positive integer and `updated_at` in `YYYY-MM-DD HH:MM:SS` format interpreted in the configured Artifact timestamp timezone. Markdown Atoms encode both properties in YAML frontmatter. A registered native Atom whose executable format excludes governance metadata encodes both properties in its governed external revision binding. Creation writes version one; every committed edit to the Atom carrier contents, including a carrier-only correction, increments `version` by exactly one and updates `updated_at` in the same operation. A path-only lifecycle move changes neither property, while a replacement Atom starts at version one.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-625--encode-framework-settings-as-a-native-toml-atom.md": requirement(
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-625--encode-framework-settings-as-a-native-toml-atom.md", "settings", ["CAPRMEDIO-META-REQU-619--classify-framework-settings-as-an-implementation-atom"],
            "# Encode framework settings as a native TOML Atom\n\n`caprmedio_framework_settings.toml` must contain only executable framework-engine settings and human-readable configuration comments in native TOML. It must not embed YAML frontmatter, Artifact identity, revision metadata, relations, rationale, or provenance.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-645--reconcile-materialized-representations.md": requirement(
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-645--reconcile-materialized-representations.md", "carrier-format", [gov_core, "CAPRMEDIO-REQU-644--admit-necessary-materialized-representations"],
            "# Reconcile materialized representations\n\nEvery admitted materialized representation must identify its canonical source and have a deterministic regeneration or reconciliation rule appropriate to its use.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-647--register-project-settings-projection-mechanics.md": requirement(
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-647--register-project-settings-projection-mechanics.md", "settings", [gov_core, "CAPRMEDIO-META-REQU-627--bind-every-projected-setting-to-exact-source-authority"],
            "# Register Project Settings Projection mechanics\n\nGOV must register `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/generate_project_settings.py` as the deterministic Project Settings generator that emits carrier-native Projection metadata and exact per-setting source-Atom revision bindings, resolves the Framework Settings revision through its Work Journal binding, and rejects missing, stale, ambiguous, or contradictory sources.",
            replacements=["CAPRMEDIO-GOV-REQU-629--encode-project-settings-projection-rules-as-a-toml-atom"],
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-661--register-framework-settings-atom-identity.md": requirement(
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-661--register-framework-settings-atom-identity.md", "settings", ["CAPRMEDIO-META-REQU-619--classify-framework-settings-as-an-implementation-atom"],
            "# Register Framework Settings Atom identity\n\nGOV must register `CAPRMEDIO-FRAMEWORK-SETTINGS` as the stable Artifact identity derived from the governed canonical address `caprmedio_framework_settings.toml`. The framework-installation symlink is a convenience locator and does not establish a second identity.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-662--bind-framework-settings-revisions-in-the-work-journal.md": requirement(
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-662--bind-framework-settings-revisions-in-the-work-journal.md", "settings", ["CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance", "CAPRMEDIO-META-REQU-165--atoms-have-version-and-updated-at"],
            "# Bind Framework Settings revisions in the Work Journal\n\nEvery admitted revision of `CAPRMEDIO-FRAMEWORK-SETTINGS` must have one append-only Work Journal binding containing its monotonic version, `updated_at`, canonical carrier address, and content digest. The latest valid binding whose address and digest match the canonical carrier establishes its current revision; a missing or mismatched binding leaves currentness unknown.",
            updated_at=updated_at, session_id=session_id
        ),
        ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-370--register-closed-gov-subject-scope-vocabulary.md": requirement(
            ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-370--register-closed-gov-subject-scope-vocabulary.md", "subject-scope", [gov_core, "CAPRMEDIO-META-REQU-175--use-canonical-meta-subject-scopes"],
            "# Register the closed GOV Subject-scope vocabulary\n\nGOV Atoms use only the closed GOV Subject-scope vocabulary registered by this Requirement.",
            updated_at=updated_at, session_id=session_id
        ),
    }


def rewrite_gov_290(updated_at: str, session_id: str | None) -> None:
    path = ROOT / ".caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-290--exclude-secrets-from-dset.md"
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        version, _ = revision_values(path, text)
        if version is not None:
            return
        previous = prior_version(path)
        atomic_write(path, insert_revision(path, text, previous + 1 if previous else 1, updated_at))
        return
    if not text.startswith("+++"):
        return
    end = text.find("\n+++", 3)
    if end < 0:
        raise RuntimeError(f"{path}: unclosed TOML frontmatter")
    legacy_front = text[3:end]
    legacy_version = re.search(r"(?m)^version\s*=\s*(\d+)", legacy_front)
    version = int(legacy_version.group(1)) + 1 if legacy_version else prior_version(path) + 1
    sessions = re.search(r"(?m)^llm_session_ids\s*=\s*\[(.*?)\]", legacy_front)
    session_lines = []
    if sessions:
        values = re.findall(r'"([^"]+)"', sessions.group(1))
        if values:
            session_lines = ["llm_session_ids:", *(f"  - {value}" for value in values)]
    body = text[end + 5 :].lstrip("\n")
    front = [
        "---", "subject_scopes:", "  - external-boundary",
        f"version: {version}", f"updated_at: {updated_at}", *session_lines,
        "relations:", "  child_of:",
        "    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully", "---", body,
    ]
    atomic_write(path, "\n".join(front))


def apply(*, updated_at: str | None = None, session_id: str | None = None) -> None:
    timestamp = operator_timestamp(updated_at)
    session = runtime_session(session_id)
    if session is None:
        raise RuntimeError("--session-id or CAPRMEDIO_SESSION_ID is required with --apply")
    archive_requirements = [
        ROOT / ".caprmedio/04_requirement/archive/CAPRMEDIO-REQU-628--place-project-settings-projection-rules-in-the-root-realization.md",
        ROOT / ".caprmedio/200_LAYER_2_GOV/04_requirement/archive/CAPRMEDIO-GOV-REQU-629--encode-project-settings-projection-rules-as-a-toml-atom.md",
    ]
    if not all(path.exists() for path in archive_requirements):
        raise RuntimeError("expected archived two-settings-carrier authorities are missing")
    for name, text in replacements(updated_at=timestamp, session_id=session).items():
        atomic_write(rel(name), text)
    rewrite_gov_290(timestamp, session)
    settings()
    update_project_settings_evaluation()
    update_renamed_settings_references()
    for directory in RMED_ROOTS:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            if active(path) and "-CATL-" not in path.stem:
                normalize_rmed(path)
    repair_child_graph()
    repair_stale_strict_relations()
    subprocess.run(
        [
            sys.executable,
            str(TOOLS_ROOT / "framework_settings_revision.py"),
            "--apply",
            "--session-id",
            session,
            str(ROOT),
        ],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(TOOLS_ROOT / "generate_project_settings.py"),
            "--apply",
            "--session-id",
            session,
            str(ROOT),
        ],
        cwd=ROOT,
        check=True,
    )
    journal(timestamp, session)
    print("applied FPF audit repairs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the bounded repair migration")
    parser.add_argument("--updated-at", help="operator-local revision timestamp (YYYY-MM-DD HH:MM:SS)")
    parser.add_argument("--session-id", help="session identity to record in generated provenance")
    args = parser.parse_args()
    if not args.apply:
        print("dry-run: pass --apply to write the bounded repair migration")
    else:
        apply(updated_at=args.updated_at, session_id=args.session_id)
