#!/usr/bin/env python3
"""Collapse the retired SPEC Feature tree into six concrete CAPRMEDIO Layers.

Parameters:
    root: repository root; defaults to the current directory.
    --apply: persist the migration; omission is a dry run.
    --session-id: required provenance for an applied migration.

The migration creates this actual top-level structure under `.caprmedio`:

    100_LAYER_1_META
    200_LAYER_2_GOV
    300_LAYER_3_METHODOLOGY
    400_LAYER_4_FRAMEWORK_ENGINE
    500_LAYER_5_DOCUMENTATION
    600_LAYER_6_RELEASES

The old SPEC and METHODOLOGY scopes are merged into METHODOLOGY. TOOLS,
SKILLS, EXTENSIONS, ADAPTERS, and EVALUATION are merged into
FRAMEWORK_ENGINE. Active carrier identities and references are migrated to the
new owning Layer. Retired Feature-scope authority is archived. Append-only
Journals and archived carrier content are not rewritten.

Before mutation, a complete `.caprmedio` backup is created beneath
`.caprmedio_runtime/migrations/migrate_to_six_framework_layers/`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
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
from project_runtime import atomic_tempfile  # noqa: E402
from work_journal import append_record, event_record  # noqa: E402


CONTROL_ROOT = Path(".caprmedio")
RUNTIME_ROOT = Path(
    ".caprmedio_runtime/migrations/migrate_to_six_framework_layers"
)
THIS_SCRIPT = Path("002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/migrate_to_six_framework_layers.py")
SESSION_TIMESTAMP_FORMAT = "%Y%m%dT%H%M%S%z"
ATOM_TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
TEXT_SUFFIXES = {
    ".cfg",
    ".ini",
    ".json",
    ".md",
    ".py",
    ".sh",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
EXCLUDED_TREE_PARTS = {".git", ".caprmedio_runtime", "010_journals"}
GENERATED_PATHS = {
    Path(".caprmedio/caprmedio_project_settings.toml"),
    Path(".caprmedio/08_implementation/CAPRMEDIO-MAPS-001--project-settings-source-map.yaml"),
}


@dataclass(frozen=True)
class ScopeMerge:
    source: Path
    destination: Path
    old_identity_prefix: str | None
    new_identity_prefix: str | None


MERGES = (
    ScopeMerge(
        Path(".caprmedio/300_LAYER_3_SPEC"),
        Path(".caprmedio/300_LAYER_3_METHODOLOGY"),
        "CAPRMEDIO-SPEC-",
        "CAPRMEDIO-METHODOLOGY-",
    ),
    ScopeMerge(
        Path(".caprmedio/301_FEATURE_METHODOLOGY"),
        Path(".caprmedio/300_LAYER_3_METHODOLOGY"),
        "CAPRMEDIO-SPEC-METHODOLOGY-",
        "CAPRMEDIO-METHODOLOGY-",
    ),
    ScopeMerge(
        Path(".caprmedio/302_FEATURE_TOOLS"),
        Path(".caprmedio/400_LAYER_4_FRAMEWORK_ENGINE"),
        "CAPRMEDIO-SPEC-TOOLS-",
        "CAPRMEDIO-FRAMEWORK-ENGINE-",
    ),
    ScopeMerge(
        Path(".caprmedio/303_FEATURE_SKILLS"),
        Path(".caprmedio/400_LAYER_4_FRAMEWORK_ENGINE"),
        "CAPRMEDIO-SPEC-SKILLS-",
        "CAPRMEDIO-FRAMEWORK-ENGINE-",
    ),
    ScopeMerge(
        Path(".caprmedio/304_FEATURE_EXTENSIONS"),
        Path(".caprmedio/400_LAYER_4_FRAMEWORK_ENGINE"),
        "CAPRMEDIO-SPEC-EXTENSIONS-",
        "CAPRMEDIO-FRAMEWORK-ENGINE-",
    ),
    ScopeMerge(
        Path(".caprmedio/305_FEATURE_ADAPTERS"),
        Path(".caprmedio/400_LAYER_4_FRAMEWORK_ENGINE"),
        "CAPRMEDIO-SPEC-ADAPTERS-",
        "CAPRMEDIO-FRAMEWORK-ENGINE-",
    ),
    ScopeMerge(
        Path(".caprmedio/306_FEATURE_EVALUATION"),
        Path(".caprmedio/400_LAYER_4_FRAMEWORK_ENGINE"),
        "CAPRMEDIO-SPEC-EVALUATION-",
        "CAPRMEDIO-FRAMEWORK-ENGINE-",
    ),
    ScopeMerge(
        Path(".caprmedio/307_FEATURE_DOCUMENTATION"),
        Path(".caprmedio/500_LAYER_5_DOCUMENTATION"),
        "CAPRMEDIO-SPEC-DOCUMENTATION-",
        "CAPRMEDIO-DOCUMENTATION-",
    ),
    ScopeMerge(
        Path(".caprmedio/308_FEATURE_RELEASES"),
        Path(".caprmedio/600_LAYER_6_RELEASES"),
        "CAPRMEDIO-SPEC-RELEASES-",
        "CAPRMEDIO-RELEASES-",
    ),
)

DESTINATION_LAYERS = tuple(dict.fromkeys(merge.destination for merge in MERGES))

OBSOLETE_SPEC_SCOPE_ATOMS = {
    "CAPRMEDIO-SPEC-REQU-497--govern-complete-spec-feature-topology.md",
    "CAPRMEDIO-SPEC-REQU-498--define-methodology-feature-scope.md",
    "CAPRMEDIO-SPEC-REQU-499--define-tools-feature-scope.md",
    "CAPRMEDIO-SPEC-REQU-500--define-skills-feature-scope.md",
    "CAPRMEDIO-SPEC-REQU-502--define-adapters-feature-scope.md",
    "CAPRMEDIO-SPEC-REQU-503--define-evaluation-feature-scope.md",
    "CAPRMEDIO-SPEC-REQU-504--define-documentation-feature-scope.md",
    "CAPRMEDIO-SPEC-REQU-678--define-releases-feature-scope.md",
    "CAPRMEDIO-SPEC-REQU-691--define-extensions-feature-scope.md",
}

OBSOLETE_FEATURE_REFERENCES = {
    name.removesuffix(".md") for name in OBSOLETE_SPEC_SCOPE_ATOMS
}

STALE_REFERENCE_REPLACEMENTS = {
    "CAPRMEDIO-SPEC-TOOLS-REQU-526--generate-biz-artifact-and-implementation-metrics":
        "CAPRMEDIO-SPEC-TOOLS-REQU-526--generate-current-active-atom-snapshot",
}

LAYER_PARENT_BY_DESTINATION = {
    Path(".caprmedio/300_LAYER_3_METHODOLOGY"):
        "CAPRMEDIO-REQU-701--define-methodology-layer-scope",
    Path(".caprmedio/400_LAYER_4_FRAMEWORK_ENGINE"):
        "CAPRMEDIO-REQU-702--define-framework-engine-layer-scope",
    Path(".caprmedio/500_LAYER_5_DOCUMENTATION"):
        "CAPRMEDIO-REQU-703--define-documentation-layer-scope",
    Path(".caprmedio/600_LAYER_6_RELEASES"):
        "CAPRMEDIO-REQU-704--define-releases-layer-scope",
}

OBSOLETE_CONTRACT_SOURCE = Path(
    ".caprmedio/04_requirement/"
    "CAPRMEDIO-CNTR-011--map-spec-features-to-realization-features.md"
)
OBSOLETE_CONTRACT_DESTINATION = Path(
    ".caprmedio/04_requirement/archive/"
    "CAPRMEDIO-CNTR-011--map-spec-features-to-realization-features.md"
)


@dataclass(frozen=True)
class FileMove:
    source: Path
    destination: Path
    destination_layer: Path
    archived: bool
    identity_changed: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--session-id")
    return parser.parse_args()


def is_archived(path: Path) -> bool:
    return "archive" in path.parts


def renamed_name(name: str, merge: ScopeMerge, archived: bool) -> str:
    if archived or merge.old_identity_prefix is None:
        return name
    if not name.startswith(merge.old_identity_prefix):
        return name
    assert merge.new_identity_prefix is not None
    return merge.new_identity_prefix + name[len(merge.old_identity_prefix):]


def discover_moves(root: Path) -> tuple[list[FileMove], list[Path]]:
    moves: list[FileMove] = []
    junk = sorted((root / CONTROL_ROOT).rglob(".DS_Store"))
    destinations: dict[Path, Path] = {}
    for merge in MERGES:
        source_root = root / merge.source
        if not source_root.exists():
            continue
        for source in sorted(path for path in source_root.rglob("*") if path.is_file()):
            if source.name == ".DS_Store":
                continue
            relative = source.relative_to(source_root)
            archived = is_archived(relative)
            if (
                merge.source == Path(".caprmedio/300_LAYER_3_SPEC")
                and source.name in OBSOLETE_SPEC_SCOPE_ATOMS
            ):
                relative = Path("04_requirement/archive") / source.name
                archived = True
            name = renamed_name(relative.name, merge, archived)
            destination = root / merge.destination / relative.parent / name
            if destination in destinations:
                raise RuntimeError(
                    "destination collision: "
                    f"{destinations[destination].relative_to(root)}, "
                    f"{source.relative_to(root)} -> {destination.relative_to(root)}"
                )
            if destination.exists() and destination != source:
                raise RuntimeError(
                    f"destination already exists: {destination.relative_to(root)}"
                )
            destinations[destination] = source
            moves.append(
                FileMove(
                    source=source,
                    destination=destination,
                    destination_layer=merge.destination,
                    archived=archived,
                    identity_changed=source.name != name,
                )
            )
    return moves, junk


def identity_replacements(moves: list[FileMove]) -> dict[str, str]:
    replacements: dict[str, str] = {}
    for move in moves:
        if not move.identity_changed or move.source.suffix != ".md":
            continue
        old = move.source.stem
        new = move.destination.stem
        if old in replacements and replacements[old] != new:
            raise RuntimeError(f"ambiguous identity migration: {old}")
        replacements[old] = new
    if len(set(replacements.values())) != len(replacements):
        raise RuntimeError("multiple identities collapse to one destination identity")
    return replacements


def replace_tokens(text: str, replacements: dict[str, str]) -> str:
    revised = text
    for old, new in sorted(replacements.items(), key=lambda item: -len(item[0])):
        revised = revised.replace(old, new)
    return revised


def replace_paths(text: str) -> str:
    revised = text
    for merge in MERGES:
        revised = revised.replace(
            merge.source.as_posix(), merge.destination.as_posix()
        )
        revised = revised.replace(
            merge.source.name, merge.destination.name
        )
    return revised


def replace_obsolete_feature_parents(text: str, parent: str) -> str:
    revised = replace_tokens(text, STALE_REFERENCE_REPLACEMENTS)
    for reference in sorted(OBSOLETE_FEATURE_REFERENCES):
        revised = revised.replace(reference, parent)
    return deduplicate_relation_items(revised)


def deduplicate_relation_items(text: str) -> str:
    lines = text.splitlines()
    in_frontmatter = bool(lines and lines[0] in {"---", "+++"})
    delimiter = lines[0] if in_frontmatter else None
    in_relations = False
    seen: set[str] = set()
    output: list[str] = []
    for index, line in enumerate(lines):
        if index > 0 and delimiter is not None and line == delimiter:
            in_frontmatter = False
            in_relations = False
        if in_frontmatter and line == "relations:":
            in_relations = True
            seen = set()
        elif in_relations and re.match(r"^  [A-Za-z_][A-Za-z0-9_]*:$", line):
            seen = set()
        elif in_relations and line and not line.startswith("  "):
            in_relations = False
        if in_relations and line.startswith("    - "):
            if line in seen:
                continue
            seen.add(line)
        output.append(line)
    suffix = "\n" if text.endswith("\n") else ""
    return "\n".join(output) + suffix


def replace_spec_body_label(text: str, destination_layer: Path) -> str:
    if destination_layer != Path(".caprmedio/300_LAYER_3_METHODOLOGY"):
        return text
    if not text.startswith(("---\n", "+++\n")):
        return text
    delimiter = text[:3]
    marker = f"\n{delimiter}\n"
    boundary = text.find(marker, 4)
    if boundary < 0:
        return text
    head = text[: boundary + len(marker)]
    body = text[boundary + len(marker) :]
    body = re.sub(r"\bSPEC\b", "METHODOLOGY", body)
    return head + body


def bump_atom_revision(text: str, timestamp: str) -> str:
    if not text.startswith(("---\n", "+++\n")):
        return text
    delimiter = text[:3]
    marker = f"\n{delimiter}\n"
    boundary = text.find(marker, 4)
    if boundary < 0:
        return text
    frontmatter = text[4:boundary]
    if delimiter == "---":
        version_pattern = re.compile(r"(?m)^version:\s*(\d+)\s*$")
        updated_pattern = re.compile(r"(?m)^updated_at:\s*[^\n]+$")
        updated_line = f"updated_at: {timestamp}"
    else:
        version_pattern = re.compile(r"(?m)^version\s*=\s*(\d+)\s*$")
        updated_pattern = re.compile(r'(?m)^updated_at\s*=\s*"[^\n]+"\s*$')
        updated_line = f'updated_at = "{timestamp}"'
    versions = version_pattern.findall(frontmatter)
    updated = updated_pattern.findall(frontmatter)
    if not versions and not updated:
        return text
    if len(versions) != 1 or len(updated) != 1:
        raise RuntimeError("cannot bump malformed Atom revision metadata")
    version = int(versions[0]) + 1
    frontmatter = version_pattern.sub(
        (f"version: {version}" if delimiter == "---" else f"version = {version}"),
        frontmatter,
        count=1,
    )
    frontmatter = updated_pattern.sub(updated_line, frontmatter, count=1)
    return f"{delimiter}\n{frontmatter}\n{delimiter}\n{text[boundary + len(marker):]}"


def read_text(path: Path) -> str | None:
    if path.suffix.lower() not in TEXT_SUFFIXES or path.is_symlink():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def external_text_candidates(root: Path, moves: list[FileMove]) -> list[Path]:
    moved_sources = {move.source for move in moves}
    candidates: list[Path] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path in moved_sources or path.is_symlink():
            continue
        relative = path.relative_to(root)
        if relative == THIS_SCRIPT or relative in GENERATED_PATHS:
            continue
        if relative.parts[:3] == ("FRAMEWORK_ENGINE", "TOOLS", "migrations"):
            continue
        if any(part in EXCLUDED_TREE_PARTS for part in relative.parts):
            continue
        if is_archived(relative) or read_text(path) is None:
            continue
        candidates.append(path)
    return candidates


def build_payloads(
    root: Path,
    moves: list[FileMove],
    replacements: dict[str, str],
    timestamp: str,
) -> tuple[dict[Path, str], dict[Path, str]]:
    moved_payloads: dict[Path, str] = {}
    for move in moves:
        original = read_text(move.source)
        if original is None or move.archived:
            continue
        parent = LAYER_PARENT_BY_DESTINATION[move.destination_layer]
        revised = replace_obsolete_feature_parents(original, parent)
        revised = replace_tokens(revised, replacements)
        revised = replace_paths(revised)
        revised = replace_spec_body_label(revised, move.destination_layer)
        if revised != original or move.source != move.destination:
            revised = bump_atom_revision(revised, timestamp)
        moved_payloads[move.destination] = revised

    external_payloads: dict[Path, str] = {}
    for path in external_text_candidates(root, moves):
        original = path.read_text(encoding="utf-8")
        revised = replace_tokens(original, replacements)
        revised = replace_paths(revised)
        if revised == original:
            continue
        revised = bump_atom_revision(revised, timestamp)
        external_payloads[path] = revised
    return moved_payloads, external_payloads


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


def tree_digest(path: Path) -> str:
    digest = hashlib.sha256()
    for file in sorted(item for item in path.rglob("*") if item.is_file()):
        digest.update(file.relative_to(path).as_posix().encode())
        digest.update(b"\0")
        digest.update(file.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def create_backup(root: Path, timestamp: dt.datetime) -> Path:
    label = timestamp.strftime(SESSION_TIMESTAMP_FORMAT)
    backup_root = root / RUNTIME_ROOT / label
    if backup_root.exists():
        raise RuntimeError(f"backup already exists: {backup_root.relative_to(root)}")
    backup_root.mkdir(parents=True)
    source = root / CONTROL_ROOT
    destination = backup_root / "caprmedio"
    shutil.copytree(source, destination, symlinks=True)
    manifest = {
        "created_at": timestamp.isoformat(),
        "source": CONTROL_ROOT.as_posix(),
        "backup": destination.relative_to(root).as_posix(),
        "sha256": tree_digest(destination),
    }
    (backup_root / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return backup_root


def remove_empty_sources(root: Path) -> None:
    for merge in MERGES:
        source = root / merge.source
        if not source.exists():
            continue
        for directory in sorted(
            (path for path in source.rglob("*") if path.is_dir()),
            key=lambda path: len(path.parts),
            reverse=True,
        ):
            directory.rmdir()
        source.rmdir()


def apply_migration(
    root: Path,
    moves: list[FileMove],
    junk: list[Path],
    moved_payloads: dict[Path, str],
    external_payloads: dict[Path, str],
) -> None:
    for destination in DESTINATION_LAYERS:
        (root / destination).mkdir(parents=True, exist_ok=True)
    for move in moves:
        move.destination.parent.mkdir(parents=True, exist_ok=True)
        move.source.rename(move.destination)
        if move.destination in moved_payloads:
            atomic_write(move.destination, moved_payloads[move.destination])
    for path in junk:
        path.unlink()
    remove_empty_sources(root)
    for path, revised in external_payloads.items():
        atomic_write(path, revised)
    source = root / OBSOLETE_CONTRACT_SOURCE
    destination = root / OBSOLETE_CONTRACT_DESTINATION
    if source.exists():
        if destination.exists():
            raise RuntimeError(
                f"obsolete Contract destination exists: {destination.relative_to(root)}"
            )
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.rename(destination)


def main() -> int:
    args = parse_args()
    root = repository_root(Path(args.root))
    if args.apply and not args.session_id:
        raise RuntimeError("--session-id is required with --apply")

    moves, junk = discover_moves(root)
    replacements = identity_replacements(moves)
    now = dt.datetime.now().astimezone()
    timestamp = now.strftime(ATOM_TIMESTAMP_FORMAT)
    moved_payloads, external_payloads = build_payloads(
        root, moves, replacements, timestamp
    )
    contract_move = (
        (root / OBSOLETE_CONTRACT_SOURCE).exists()
        and not (root / OBSOLETE_CONTRACT_DESTINATION).exists()
    )
    changed = bool(moves or junk or external_payloads or contract_move)

    print(f"changed={str(changed).lower()}")
    print(f"file_moves={len(moves)}")
    print(f"identity_changes={len(replacements)}")
    print(f"moved_text_changes={len(moved_payloads)}")
    print(f"external_text_changes={len(external_payloads)}")
    print(f"finder_metadata_removed={len(junk)}")
    print(f"obsolete_contract_archived={str(contract_move).lower()}")
    for merge in MERGES:
        if (root / merge.source).exists():
            print(f"merge {merge.source} -> {merge.destination}")

    if not args.apply or not changed:
        return 0

    backup = create_backup(root, now)
    apply_migration(root, moves, junk, moved_payloads, external_payloads)
    record = event_record(
        root=root,
        event="completed",
        action_id="migrate-to-six-framework-layers-20260818",
        kind="structural_migration",
        scope="project",
        operation="migrate_to_six_framework_layers",
        session_id=args.session_id,
        subjects=[merge.source.as_posix() for merge in MERGES],
        outputs=[destination.as_posix() for destination in DESTINATION_LAYERS],
        preceding_event=None,
        details={
            "backup": backup.relative_to(root).as_posix(),
            "file_moves": str(len(moves)),
            "identity_changes": str(len(replacements)),
            "text_changes": str(len(moved_payloads) + len(external_payloads)),
        },
    )
    journal = append_record(root, record)
    print(f"backup={backup.relative_to(root)}")
    print(f"journal={journal.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
