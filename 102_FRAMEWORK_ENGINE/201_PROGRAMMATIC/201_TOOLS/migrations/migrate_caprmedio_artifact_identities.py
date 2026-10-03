#!/usr/bin/env python3
"""Migrate governed CAPRMEDIO identities to the canonical grammar.

Parameters:
    root: repository root; defaults to the current directory.
    --apply: persist the migration; omission is a fail-closed dry run.
    --session-id: required provenance for an applied migration.
    --show: number of old-to-new mappings printed.

The tool inventories numbered Markdown carriers outside the framework symlink
view and append-only Journals, derives Type and structural scope, assigns one
project-wide sequence per Type prefix, rewrites mutable references, and appends
the complete identity map to the Work Journal. Existing Journal bytes are never
rewritten. Applied changes use one script-owned recovery directory.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import sys
import tomllib
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve()
TOOLS_ROOT = SCRIPT_PATH.parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402
REPOSITORY_ROOT = next(parent for parent in SCRIPT_PATH.parents if (parent / ".git").exists())
sys.pycache_prefix = str(REPOSITORY_ROOT / ".caprmedio_tmp/cache/python")

from artifact_metadata import repository_root  # noqa: E402
from work_journal import append_record, event_record  # noqa: E402


CONTROL_ROOT = Path(".caprmedio")
SETTINGS_PATH = CONTROL_ROOT / "caprmedio_settings.toml"
RUNTIME_DIRECTORY = Path(".caprmedio_runtime/migrate_caprmedio_artifact_identities")
EXCLUDED_CONTROL_DIRECTORIES = {"000_caprmedio_framework", "010_journals"}
EXCLUDED_ROOT_DIRECTORIES = {".git", ".f4f", ".caprmedio_runtime"}
TEXT_SUFFIXES = {
    ".cfg", ".ini", ".json", ".jsonl", ".md", ".py", ".sh",
    ".toml", ".txt", ".yaml", ".yml",
}
CONTENT_ROLE_DIRECTORIES = {
    "01_concern": "concern",
    "02_analysis": "analysis",
    "03_plan": "plan",
    "04_requirement": "requirement",
    "05_method": "method",
    "06_evaluation": "evaluation",
    "07_delivery": "delivery",
    "08_implementation": "implementation",
    "09_ops": "ops",
}
IDENTITY_DERIVED_PROPERTIES = {"artifact_id", "artifact_type", "scope_path"}
IDENTITY_NUMBER = re.compile(r"(?:^|-)(\d{3})(?=-|$)")
SUMMARY = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
YAML_PROPERTY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s|$)")
TOML_PROPERTY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*=")
TOKEN_CHARACTER = r"A-Za-z0-9_-"


ARTIFACT_TYPE_TO_TYPE = {
    "analysis": "analysis",
    "analysis_report": "analysis",
    "evaluation": "evaluation",
    "constraint": "constraint",
    "contract": "contract",
    "concern": "concern",
    "conflict": "conflict",
    "development_backlog": "development_backlog",
    "evaluation_case": "evaluation",
    "evaluation_plan": "evaluation",
    "evidence_record": "ops",
    "external_analysis_report": "external_analysis_report",
    "external_evidence_record": "external_evidence_record",
    "external_method": "external_method",
    "implementation_decision": "method",
    "integration_decision": "method_binding",
    "method": "method",
    "method_binding": "method_binding",
    "plan": "plan",
    "problem": "concern",
    "question": "concern",
    "requirement": "requirement",
    "review_protocol": "review_protocol",
    "specification": "catalog",
    "test_case": "evaluation",
    "test_plan": "evaluation",
    "verification_record": "verification_record",
}


FAMILY_MARKERS = (
    ("EXTERNAL-ANALYSIS-REPORT", "external_analysis_report"),
    ("EXTERNAL-EVIDENCE-RECORD", "external_evidence_record"),
    ("EVALUATION-CASE", "evaluation"),
    ("EVIDENCE-RECORD", "ops"),
    ("ANALYSIS-REPORT", "analysis"),
    ("VERIFICATION-RECORD", "verification_record"),
    ("TEST-CASE", "evaluation"),
    ("QA-CASE", "evaluation"),
    ("SPECIFICATION", "catalog"),
    ("REQUIREMENT", "requirement"),
    ("CONSTRAINT", "constraint"),
    ("CONTRACT", "contract"),
    ("OPPORTUNITY", "concern"),
    ("QUESTION", "concern"),
    ("PROBLEM", "concern"),
    ("DEFECT", "concern"),
    ("CONFLICT", "conflict"),
    ("ANALYSIS", "analysis"),
    ("DECISION", "method"),
    ("METHOD", "method"),
    ("VERSION", "version"),
    ("PLAN", "plan"),
    ("GOAL", "goal"),
    ("RISK", "concern"),
    ("GAP", "concern"),
    ("IDEC", "method_binding"),
    ("IMPL", "method"),
    ("ANRP", "analysis"),
    ("BKLG", "development_backlog"),
    ("CATL", "catalog"),
)


@dataclass(frozen=True)
class Frontmatter:
    delimiter: str | None
    content: str
    body: str
    artifact_type: str | None
    artifact_subtype: str | None


@dataclass(frozen=True)
class Carrier:
    source: Path
    relative_source: Path
    destination: Path
    relative_destination: Path
    old_stem: str
    old_short_id: str
    new_stem: str
    new_short_id: str
    type_name: str
    type_prefix: str
    subtype: str | None
    scope_path: tuple[str, ...]
    original_text: str
    revised_text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--session-id")
    parser.add_argument("--show", type=int, default=20)
    return parser.parse_args()


def load_settings(root: Path) -> dict[str, Any]:
    return tomllib.loads((root / SETTINGS_PATH).read_text(encoding="utf-8"))


def parse_registered_prefixes(root: Path) -> tuple[dict[str, str], dict[str, str]]:
    matches = sorted(
        path for path in (root / CONTROL_ROOT).rglob("*register-caprmedio-type-prefixes.md")
        if "archive" not in path.parts and "drafts" not in path.parts and not path.is_symlink()
    )
    if len(matches) != 1:
        raise RuntimeError(f"expected one active Type-prefix authority, found {len(matches)}")
    text = matches[0].read_text(encoding="utf-8")
    by_type: dict[str, str] = {}
    for type_name, prefix in re.findall(r"^\| `([^`]+)` \| `([A-Z]{4})` \|$", text, re.MULTILINE):
        if type_name in by_type:
            raise RuntimeError(f"duplicate registered Type: {type_name}")
        by_type[type_name] = prefix
    required = set(ARTIFACT_TYPE_TO_TYPE.values()) - {"version", "goal"}
    required.update({"requirement:goal", "catalog", "ops", "verification_record"})
    missing = sorted(required - set(by_type))
    if missing:
        raise RuntimeError(f"Type-prefix authority is incomplete: {', '.join(missing)}")
    prefix_to_type: dict[str, str] = {}
    for type_name, prefix in by_type.items():
        if prefix in prefix_to_type:
            raise RuntimeError(f"duplicate registered prefix: {prefix}")
        prefix_to_type[prefix] = type_name
    return by_type, prefix_to_type


def yaml_scalar(content: str, name: str, path: Path) -> str | None:
    matches = re.findall(rf"(?m)^{re.escape(name)}:\s*([^\n#]+)$", content)
    if len(matches) > 1:
        raise RuntimeError(f"{path}: duplicate {name}")
    return matches[0].strip().strip('"').strip("'") if matches else None


def split_frontmatter(text: str, path: Path) -> Frontmatter:
    delimiter = text[:3] if text.startswith(("---\n", "+++\n")) else None
    if delimiter is None:
        return Frontmatter(None, "", text, None, None)
    marker = f"\n{delimiter}\n"
    remainder = text[4:]
    boundary = remainder.find(marker)
    if boundary < 0:
        raise RuntimeError(f"{path}: unterminated frontmatter")
    content = remainder[:boundary]
    body = remainder[boundary + len(marker):]
    if delimiter == "+++":
        try:
            data = tomllib.loads(content)
        except tomllib.TOMLDecodeError as error:
            raise RuntimeError(f"{path}: invalid TOML frontmatter: {error}") from error
        artifact_type = data.get("artifact_type")
        artifact_subtype = data.get("artifact_subtype")
    else:
        artifact_type = yaml_scalar(content, "artifact_type", path)
        artifact_subtype = yaml_scalar(content, "artifact_subtype", path)
    for name, value in (("artifact_type", artifact_type), ("artifact_subtype", artifact_subtype)):
        if value is not None and not isinstance(value, str):
            raise RuntimeError(f"{path}: {name} must be a scalar string")
    return Frontmatter(delimiter, content, body, artifact_type, artifact_subtype)


def remove_yaml_properties(content: str, names: set[str]) -> list[str]:
    source = content.splitlines()
    result: list[str] = []
    index = 0
    while index < len(source):
        match = YAML_PROPERTY.match(source[index])
        if match and match.group(1) in names:
            index += 1
            while index < len(source):
                line = source[index]
                if line and not line[0].isspace():
                    break
                index += 1
            continue
        result.append(source[index])
        index += 1
    return result


def remove_toml_properties(content: str, names: set[str]) -> list[str]:
    return [
        line for line in content.splitlines()
        if not ((match := TOML_PROPERTY.match(line)) and match.group(1) in names)
    ]


def revise_frontmatter(frontmatter: Frontmatter, subtype: str | None, path: Path) -> str:
    if frontmatter.delimiter is None:
        if subtype is None:
            return frontmatter.body
        return f"---\nartifact_subtype: {subtype}\n---\n{frontmatter.body}"
    names = set(IDENTITY_DERIVED_PROPERTIES) | {"artifact_subtype"}
    if frontmatter.delimiter == "---":
        lines = remove_yaml_properties(frontmatter.content, names)
        if subtype is not None:
            lines.insert(0, f"artifact_subtype: {subtype}")
    else:
        lines = remove_toml_properties(frontmatter.content, names)
        if subtype is not None:
            lines.insert(0, f'artifact_subtype = "{subtype}"')
    while lines and not lines[-1]:
        lines.pop()
    revised = f"{frontmatter.delimiter}\n{'\n'.join(lines)}\n{frontmatter.delimiter}\n{frontmatter.body}"
    split_frontmatter(revised, path)
    return revised


def structural_registry(settings: dict[str, Any]) -> dict[str, tuple[str, ...]]:
    structure = settings.get("structure")
    if not isinstance(structure, dict):
        raise RuntimeError("settings require [structure]")
    layers = structure.get("layers")
    features = structure.get("features", {})
    if not isinstance(layers, list) or not all(isinstance(item, str) for item in layers):
        raise RuntimeError("structure.layers must be an array of names")
    if not isinstance(features, dict):
        raise RuntimeError("structure.features must be a table")
    registry: dict[str, tuple[str, ...]] = {}
    layer_positions: dict[str, int] = {}
    for position, layer in enumerate(layers, start=1):
        registry[f"{position}00_LAYER_{position}_{layer.upper()}"] = (layer.upper(),)
        layer_positions[layer] = position
    for owner, names in features.items():
        if owner not in layer_positions:
            raise RuntimeError(f"features registered for unknown Layer: {owner}")
        if not isinstance(names, list) or not all(isinstance(item, str) for item in names):
            raise RuntimeError(f"structure.features.{owner} must be an array of names")
        for feature_position, feature in enumerate(names, start=1):
            if feature_position > 9:
                raise RuntimeError("flat Feature layout supports at most nine Features per Layer")
            owner_position = layer_positions[owner]
            registry[f"{owner_position}0{feature_position}_FEATURE_{feature.upper()}"] = (
                owner.upper(), feature.upper()
            )
    return registry


def scope_for(relative: Path, registry: dict[str, tuple[str, ...]]) -> tuple[str, ...]:
    first = relative.parts[0]
    if first in registry:
        return registry[first]
    if re.match(r"^\d{3}_(?:LAYER|FEATURE)_", first):
        raise RuntimeError(f"unregistered structural directory: {first}")
    return ()


def content_role_for(relative: Path) -> str | None:
    roles = [CONTENT_ROLE_DIRECTORIES[part] for part in relative.parts if part in CONTENT_ROLE_DIRECTORIES]
    if len(roles) > 1:
        raise RuntimeError(f"multiple Content-role directories: {relative}")
    return roles[0] if roles else None


def identity_parts(stem: str, project_prefix: str) -> tuple[str, str]:
    if not stem.startswith(f"{project_prefix}-"):
        raise RuntimeError(f"identity does not start with {project_prefix}: {stem}")
    match = IDENTITY_NUMBER.search(stem)
    if match is None:
        raise RuntimeError(f"identity has no three-digit sequence: {stem}")
    old_short = stem[:match.end()]
    summary = stem.split("--", 1)[1] if "--" in stem else stem[match.end():].lstrip("-")
    if not summary or SUMMARY.fullmatch(summary) is None:
        raise RuntimeError(f"invalid or missing identity summary: {stem}")
    return old_short, summary


def family_before_number(stem: str) -> str:
    match = IDENTITY_NUMBER.search(stem)
    if match is None:
        raise RuntimeError(f"identity has no sequence: {stem}")
    return stem[:match.start()].rstrip("-")


def infer_subtype(
    stem: str,
    artifact_type: str | None,
    artifact_subtype: str | None,
) -> str | None:
    if artifact_subtype:
        return artifact_subtype
    family = family_before_number(stem)
    tokens = family.split("-")
    if "GOAL" in tokens:
        return "goal"
    for marker, subtype in (
        ("QUESTION", "question"), ("PROBLEM", "problem"), ("RISK", "risk"),
        ("OPPORTUNITY", "opportunity"), ("DEFECT", "defect"), ("GAP", "gap"),
    ):
        if marker in tokens:
            return subtype
    if "rationale--" in stem:
        return "rationale"
    if "ANALYSIS-REPORT" in family:
        return "analysis_report"
    if artifact_type in {"evaluation_case", "evaluation_plan", "test_case", "test_plan"}:
        return "qa_case"
    if artifact_type == "implementation_decision":
        return "implementation_decision"
    if "-CATL-" in f"-{stem}-" and "--" in stem:
        left = stem.split("--", 1)[0]
        match = IDENTITY_NUMBER.search(left)
        if match and left[match.end():].startswith("-"):
            return left[match.end() + 1:]
    return None


def type_for_version(subtype: str | None, path: Path) -> str:
    if subtype in {"roadmap", "release_plan"}:
        return "plan"
    if subtype == "readiness_record":
        return "verification_record"
    if subtype == "version_scope":
        return "delivery"
    raise RuntimeError(f"{path}: cannot route legacy Version subtype {subtype!r}")


def infer_type(
    *, stem: str, path: Path, role: str | None, artifact_type: str | None,
    artifact_subtype: str | None, prefix_to_type: dict[str, str],
) -> str:
    family = family_before_number(stem)
    family_tokens = family.split("-")
    explicit = [prefix_to_type[token] for token in family_tokens if token in prefix_to_type]
    if len(set(explicit)) > 1:
        raise RuntimeError(f"{path}: multiple registered Type prefixes in identity")
    if explicit:
        return explicit[0]
    if artifact_type == "version" or "VERSION" in family_tokens:
        return type_for_version(artifact_subtype, path)
    if artifact_type == "conflict" or artifact_subtype == "conflict" or "CONFLICT" in family_tokens:
        return "conflict"
    if artifact_type == "requirement" and artifact_subtype == "goal":
        return "requirement:goal"
    if artifact_type in ARTIFACT_TYPE_TO_TYPE:
        return ARTIFACT_TYPE_TO_TYPE[artifact_type]
    for marker, type_name in FAMILY_MARKERS:
        if marker in family:
            return "requirement:goal" if type_name == "goal" else type_name
    fallback = {
        "concern": "concern", "analysis": "analysis", "plan": "plan",
        "requirement": "requirement", "method": "method", "evaluation": "evaluation",
        "delivery": "delivery", "ops": "ops",
    }
    if role in fallback:
        return fallback[role]
    raise RuntimeError(f"{path}: cannot infer a registered Type")


def discover_carrier_sources(root: Path, project_prefix: str) -> list[Path]:
    sources: list[Path] = []
    for path in sorted((root / CONTROL_ROOT).rglob("*.md")):
        relative = path.relative_to(root / CONTROL_ROOT)
        if relative.parts[0] in EXCLUDED_CONTROL_DIRECTORIES or path.is_symlink():
            continue
        if path.stem.startswith(f"{project_prefix}-") and IDENTITY_NUMBER.search(path.stem):
            sources.append(path)
    if not sources:
        raise RuntimeError("no governed identity carriers found")
    return sources


def make_carriers(root: Path, settings: dict[str, Any]) -> list[Carrier]:
    project = settings.get("project", {})
    identity = settings.get("artifacts", {}).get("identity", {})
    project_prefix = identity.get("project_prefix") if identity.get("project_prefix_enabled") else ""
    if not project_prefix or project_prefix != project.get("key"):
        raise RuntimeError("enabled project identity prefix must equal project.key")
    if identity.get("subtype_in_names") is not False:
        raise RuntimeError("migration requires artifacts.identity.subtype_in_names = false")
    by_type, prefix_to_type = parse_registered_prefixes(root)
    registry = structural_registry(settings)
    preliminary: list[dict[str, Any]] = []
    old_stems: set[str] = set()
    for source in discover_carrier_sources(root, project_prefix):
        relative = source.relative_to(root / CONTROL_ROOT)
        text = source.read_text(encoding="utf-8")
        frontmatter = split_frontmatter(text, source)
        old_short, summary = identity_parts(source.stem, project_prefix)
        if source.stem in old_stems:
            raise RuntimeError(f"duplicate full identity stem: {source.stem}")
        old_stems.add(source.stem)
        scope = scope_for(relative, registry)
        type_name = infer_type(
            stem=source.stem,
            path=source,
            role=content_role_for(relative),
            artifact_type=frontmatter.artifact_type,
            artifact_subtype=frontmatter.artifact_subtype,
            prefix_to_type=prefix_to_type,
        )
        subtype = infer_subtype(source.stem, frontmatter.artifact_type, frontmatter.artifact_subtype)
        if type_name == "requirement:goal":
            subtype = "goal"
        preliminary.append({
            "source": source, "relative": relative, "text": text,
            "frontmatter": frontmatter, "old_short": old_short, "summary": summary,
            "scope": scope, "type_name": type_name, "prefix": by_type[type_name],
            "subtype": subtype,
        })
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in preliminary:
        grouped[item["prefix"]].append(item)
    carriers: list[Carrier] = []
    for prefix in sorted(grouped):
        items = sorted(grouped[prefix], key=lambda item: item["relative"].as_posix())
        if len(items) > 999:
            raise RuntimeError(f"{prefix} sequence exceeds the three-digit grammar")
        preserved_numbers: dict[int, dict[str, Any]] = {}
        assigned_numbers: dict[Path, int] = {}
        pending: list[dict[str, Any]] = []
        for item in items:
            canonical_base = "-".join([project_prefix, *item["scope"], prefix])
            match = re.fullmatch(
                rf"{re.escape(canonical_base)}-(\d{{3}})--{re.escape(item['summary'])}",
                item["source"].stem,
            )
            if match is None:
                pending.append(item)
                continue
            number = int(match.group(1))
            if number in preserved_numbers:
                other = preserved_numbers[number]["source"]
                raise RuntimeError(
                    f"duplicate canonical {prefix} sequence {number:03d}: {other} and {item['source']}"
                )
            preserved_numbers[number] = item
            assigned_numbers[item["source"]] = number
        available = (number for number in range(1, 1000) if number not in preserved_numbers)
        for item in pending:
            assigned_numbers[item["source"]] = next(available)
        for item in items:
            number = assigned_numbers[item["source"]]
            new_short = "-".join([project_prefix, *item["scope"], prefix, f"{number:03d}"])
            new_stem = f"{new_short}--{item['summary']}"
            destination = item["source"].with_name(f"{new_stem}.md")
            carriers.append(Carrier(
                source=item["source"],
                relative_source=item["relative"],
                destination=destination,
                relative_destination=destination.relative_to(root / CONTROL_ROOT),
                old_stem=item["source"].stem,
                old_short_id=item["old_short"],
                new_stem=new_stem,
                new_short_id=new_short,
                type_name=item["type_name"],
                type_prefix=prefix,
                subtype=item["subtype"],
                scope_path=item["scope"],
                original_text=item["text"],
                revised_text=revise_frontmatter(item["frontmatter"], item["subtype"], item["source"]),
            ))
    validate_destinations(carriers)
    return carriers


def validate_destinations(carriers: list[Carrier]) -> None:
    sources = {carrier.source for carrier in carriers}
    destinations: dict[Path, Path] = {}
    for carrier in carriers:
        if carrier.destination in destinations:
            raise RuntimeError(
                f"destination collision: {destinations[carrier.destination]} and {carrier.source}"
            )
        destinations[carrier.destination] = carrier.source
        if carrier.destination.exists() and carrier.destination not in sources:
            raise RuntimeError(f"destination exists outside migration set: {carrier.destination}")


def token_pattern(token: str) -> re.Pattern[str]:
    return re.compile(rf"(?<![{TOKEN_CHARACTER}]){re.escape(token)}(?![{TOKEN_CHARACTER}])")


def combined_token_pattern(tokens: set[str] | dict[str, str]) -> re.Pattern[str] | None:
    if not tokens:
        return None
    alternatives = "|".join(re.escape(token) for token in sorted(tokens, key=lambda value: (-len(value), value)))
    return re.compile(rf"(?<![{TOKEN_CHARACTER}])(?:{alternatives})(?![{TOKEN_CHARACTER}])")


def reference_map(carriers: list[Carrier]) -> tuple[dict[str, str], set[str]]:
    mapping = {
        carrier.old_stem: carrier.new_stem
        for carrier in carriers if carrier.old_stem != carrier.new_stem
    }
    shorts: dict[str, set[str]] = defaultdict(set)
    for carrier in carriers:
        shorts[carrier.old_short_id].add(carrier.new_stem)
    ambiguous = {old for old, targets in shorts.items() if len(targets) > 1}
    for old, targets in shorts.items():
        if len(targets) == 1:
            target = next(iter(targets))
            if old != target:
                mapping[old] = target
    return mapping, ambiguous


def rewrite_tokens(text: str, mapping: dict[str, str], pattern: re.Pattern[str] | None) -> str:
    if pattern is None:
        return text
    return pattern.sub(lambda match: mapping[match.group(0)], text)


def mutable_text_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for directory, directory_names, file_names in os.walk(root, followlinks=False):
        directory_path = Path(directory)
        relative_directory = directory_path.relative_to(root)
        retained: list[str] = []
        for name in directory_names:
            child_relative = relative_directory / name
            child = root / child_relative
            if child.is_symlink() or name in EXCLUDED_ROOT_DIRECTORIES:
                continue
            if relative_directory == Path(".") and name.startswith(".") and name not in {
                ".caprmedio",
                ".github",
            }:
                continue
            if name in {"__pycache__", "node_modules"}:
                continue
            if child_relative in {
                CONTROL_ROOT / "000_caprmedio_framework",
                CONTROL_ROOT / "010_journals",
            }:
                continue
            retained.append(name)
        directory_names[:] = retained
        for name in file_names:
            path = directory_path / name
            if not path.is_symlink() and path.suffix.lower() in TEXT_SUFFIXES:
                files.append(path)
    return sorted(files)


def build_rewrites(
    root: Path, carriers: list[Carrier]
) -> tuple[dict[Path, bytes], dict[str, str], set[str]]:
    mapping, ambiguous = reference_map(carriers)
    mapping_pattern = combined_token_pattern(mapping)
    ambiguous_pattern = combined_token_pattern(ambiguous)
    carrier_by_source = {carrier.source: carrier for carrier in carriers}
    writes: dict[Path, bytes] = {}
    text_after: dict[Path, str] = {}
    for path in mutable_text_files(root):
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as error:
            raise RuntimeError(f"non-UTF-8 file in mutable text surface: {path}") from error
        base = carrier_by_source[path].revised_text if path in carrier_by_source else original
        revised = rewrite_tokens(base, mapping, mapping_pattern)
        destination = carrier_by_source[path].destination if path in carrier_by_source else path
        text_after[destination] = revised
        if destination != path or revised != original:
            writes[destination] = revised.encode("utf-8")
    if ambiguous_pattern:
        occurrences = [
            (path, match.group(0))
            for path, text in text_after.items()
            if (match := ambiguous_pattern.search(text))
        ]
        if occurrences:
            sample = ", ".join(
                f"{path.relative_to(root)}:{token}"
                for path, token in occurrences[:5]
            )
            raise RuntimeError(
                f"ambiguous historical short identities remain in: {sample}"
            )
    if mapping_pattern:
        occurrences = [
            (path, match.group(0))
            for path, text in text_after.items()
            if (match := mapping_pattern.search(text))
        ]
        if occurrences:
            sample = ", ".join(f"{path.relative_to(root)}:{token}" for path, token in occurrences[:5])
            raise RuntimeError(f"stale migrated identities remain in: {sample}")
    return writes, mapping, ambiguous


def mapping_payload(carriers: list[Carrier]) -> list[dict[str, str]]:
    return [
        {
            "from": carrier.old_stem,
            "to": carrier.new_stem,
            "source": (CONTROL_ROOT / carrier.relative_source).as_posix(),
            "destination": (CONTROL_ROOT / carrier.relative_destination).as_posix(),
        }
        for carrier in sorted(carriers, key=lambda item: item.relative_source.as_posix())
        if carrier.old_stem != carrier.new_stem
        or carrier.relative_source != carrier.relative_destination
    ]


def mapping_digest(payload: list[dict[str, str]]) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def atomic_write_bytes(path: Path, payload: bytes, mode: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "migrations")
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary_name, mode)
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def backup_files(root: Path, paths: set[Path], runtime: Path) -> dict[Path, int]:
    modes: dict[Path, int] = {}
    for path in sorted(paths):
        if not path.is_file() or path.is_symlink():
            raise RuntimeError(f"cannot back up regular file: {path}")
        destination = runtime / "backup" / path.relative_to(root)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)
        modes[path] = stat.S_IMODE(path.stat().st_mode)
    return modes


def restore_backup(root: Path, backed_up: set[Path], runtime: Path, created: set[Path]) -> None:
    for path in sorted(created, reverse=True):
        if path.exists() and path not in backed_up:
            path.unlink()
    for original in sorted(backed_up):
        backup = runtime / "backup" / original.relative_to(root)
        original.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(backup, original)


def apply_migration(
    *, root: Path, carriers: list[Carrier], writes: dict[Path, bytes],
    payload: list[dict[str, str]], digest: str, session_id: str,
) -> Path:
    governing_subjects = [
        carrier.new_stem
        for carrier in carriers
        if carrier.new_stem.endswith("--expandable-scope-path-identities")
        and not {"archive", "drafts", "solved", "done"}.intersection(
            carrier.relative_source.parts
        )
    ]
    if len(set(governing_subjects)) != 1:
        raise RuntimeError("cannot resolve the singular identity-migration authority")
    runtime = root / RUNTIME_DIRECTORY
    if runtime.exists() and any(runtime.iterdir()):
        raise RuntimeError(f"runtime recovery directory is not empty: {runtime}")
    runtime.mkdir(parents=True, exist_ok=True)
    carrier_destinations = {carrier.destination for carrier in carriers}
    sources = {carrier.source for carrier in carriers}
    noncarrier_changes = {path for path in writes if path not in carrier_destinations}
    backed_up = sources | noncarrier_changes
    modes = backup_files(root, backed_up, runtime)
    (runtime / "identity-map.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    created: set[Path] = set()
    try:
        stage_root = runtime / "staged"
        stage_root.mkdir(parents=True, exist_ok=True)
        for index, carrier in enumerate(carriers, start=1):
            if carrier.source != carrier.destination:
                os.replace(carrier.source, stage_root / f"{index:04d}.md")
        for carrier in carriers:
            if carrier.destination not in writes:
                if carrier.source != carrier.destination:
                    raise RuntimeError(f"renamed carrier has no prepared payload: {carrier.source}")
                continue
            atomic_write_bytes(carrier.destination, writes[carrier.destination], modes[carrier.source])
            if carrier.destination not in backed_up:
                created.add(carrier.destination)
        for destination, data in writes.items():
            if destination not in carrier_destinations:
                atomic_write_bytes(destination, data, modes[destination])
        record = event_record(
            root=root,
            event="completed",
            action_id="migrate-caprmedio-artifact-identities",
            kind="identity_migration",
            scope="project",
            operation="migrate_artifact_identities",
            session_id=session_id,
            subjects=list(set(governing_subjects)),
            outputs=[f"identity-map-sha256:{digest}", f"migrated-identities:{len(payload)}"],
            preceding_event=None,
            details={"identity_map": payload, "mapping_sha256": digest},  # type: ignore[arg-type]
        )
        journal_path = append_record(root, record)
    except BaseException:
        restore_backup(root, backed_up, runtime, created)
        raise
    shutil.rmtree(runtime)
    runtime.parent.mkdir(parents=True, exist_ok=True)
    return journal_path


def report(
    carriers: list[Carrier], writes: dict[Path, bytes], payload: list[dict[str, str]],
    digest: str, ambiguous: set[str], show: int,
) -> None:
    carrier_destinations = {carrier.destination for carrier in carriers}
    output = {
        "carriers": len(carriers),
        "identity_changes": len(payload),
        "content_writes": len(writes),
        "noncarrier_reference_writes": len(set(writes) - carrier_destinations),
        "ambiguous_historical_short_ids_resolved_by_full_stem": sorted(ambiguous),
        "mapping_sha256": digest,
        "scopes": dict(sorted(Counter("-".join(c.scope_path) or "PROJECT" for c in carriers).items())),
        "type_prefixes": dict(sorted(Counter(c.type_prefix for c in carriers).items())),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))
    for item in payload[:max(show, 0)]:
        print(f"{item['from']} -> {item['to']}")
    if len(payload) > max(show, 0):
        print(f"... {len(payload) - max(show, 0)} more mappings")


def main() -> int:
    args = parse_args()
    root = repository_root(Path(args.root))
    if args.apply and not args.session_id:
        raise RuntimeError("--session-id is required with --apply")
    carriers = make_carriers(root, load_settings(root))
    writes, _references, ambiguous = build_rewrites(root, carriers)
    payload = mapping_payload(carriers)
    digest = mapping_digest(payload)
    report(carriers, writes, payload, digest, ambiguous, args.show)
    if args.apply:
        journal = apply_migration(
            root=root, carriers=carriers, writes=writes, payload=payload,
            digest=digest, session_id=args.session_id,
        )
        print(f"journal={journal.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
