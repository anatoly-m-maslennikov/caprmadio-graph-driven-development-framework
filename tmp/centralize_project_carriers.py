"""Record CA-P-1556's byte-verified partial Projection-relocation evidence.

This helper is deliberately read-only except when invoked with ``--write`` to
create the one approved migration map.  It never moves, renames, rewrites, or
deletes a carrier.
"""
from __future__ import annotations

import argparse
import errno
import hashlib
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / ".caprmedio_caprmedio"
PROJECTION_ROOT = CONTROL / "_projection"
MAP_TARGET = PROJECTION_ROOT / "migration/CA-P-1549-project-projection-carrier-map.json"
MOVE_COMMIT = "615b4925019f0efbbb3562f1d91dd1f5f71fd85d"
APPLICABLE_ROOT = CONTROL / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
APPLICABLE_SOURCE_ROOT = APPLICABLE_ROOT / "000_APPLICABLE_MTHD_sources"
APPLICABLE_TARGET_ROOT = PROJECTION_ROOT / "APPLICABLE_METHODOLOGY"
ROLE_NAMES = ("04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations", "09_ops")
LEGACY_MANIFEST = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_workflow_bindings.json"
LEGACY_MANIFEST_TARGET = PROJECTION_ROOT / "legacy/selected_workflow_bindings.original_thirteen.json"
CANONICAL_MANIFEST = PROJECTION_ROOT / "selected_workflow_bindings.json"
SOURCE_LINE = re.compile(rb"(?m)^  source_carrier_path: ([^\r\n]+)$")


def repository_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*arguments: str) -> bytes:
    result = subprocess.run(
        ["git", *arguments], cwd=ROOT, capture_output=True, check=False
    )
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git {' '.join(arguments)} failed: {detail}")
    return result.stdout


def read_current(path: Path, *, label: str) -> bytes:
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"{label} must be a non-symlink regular file: {repository_path(path)}")
    return path.read_bytes()


def read_blob(revision: str, repository_relative_path: str) -> bytes:
    return git("show", f"{revision}:{repository_relative_path}")


def predecessor() -> str:
    return git("rev-parse", f"{MOVE_COMMIT}^").decode("ascii").strip()


def completed_moves() -> list[tuple[str, str]]:
    tokens = git("diff-tree", "--no-commit-id", "--name-status", "-r", "-M100%", "-z", MOVE_COMMIT).split(b"\0")
    moves: list[tuple[str, str]] = []
    index = 0
    while index < len(tokens) - 1:
        status = tokens[index].decode("utf-8")
        if status.startswith(("R", "C")):
            if index + 2 >= len(tokens):
                raise RuntimeError("truncated Git rename record")
            old_path = tokens[index + 1].decode("utf-8")
            new_path = tokens[index + 2].decode("utf-8")
            index += 3
            if status == "R100" and old_path.startswith(".caprmedio_caprmedio/") and new_path.startswith(".caprmedio_caprmedio/_projection/"):
                moves.append((old_path, new_path))
        else:
            index += 2
    if len(moves) != 102:
        raise RuntimeError(f"expected 102 completed R100 Projection moves in {MOVE_COMMIT}, found {len(moves)}")
    return moves


def projection_records(parent: str) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for old_path, new_path in completed_moves():
        current_path = ROOT / new_path
        old_current_path = ROOT / old_path
        if old_current_path.exists() or old_current_path.is_symlink():
            raise RuntimeError(f"completed move source unexpectedly exists: {old_path}")
        predecessor_bytes = read_blob(parent, old_path)
        commit_bytes = read_blob(MOVE_COMMIT, new_path)
        current_bytes = read_current(current_path, label="completed Projection destination")
        predecessor_sha = digest(predecessor_bytes)
        commit_sha = digest(commit_bytes)
        current_sha = digest(current_bytes)
        if predecessor_sha != commit_sha or commit_sha != current_sha:
            raise RuntimeError(f"Projection bytes changed or were not preserved: {new_path}")
        records.append({
            "old_path": old_path,
            "new_path": new_path,
            "bytes": len(current_bytes),
            "sha256_predecessor": predecessor_sha,
            "sha256_completed_commit": commit_sha,
            "sha256_current": current_sha,
            "bytes_preserved": True,
        })
    return records


def source_reference(data: bytes, *, label: str) -> str:
    matches = SOURCE_LINE.findall(data)
    if len(matches) != 1:
        raise RuntimeError(f"expected one source_carrier_path in {label}, found {len(matches)}")
    try:
        value = matches[0].decode("utf-8")
    except UnicodeDecodeError as error:
        raise RuntimeError(f"source_carrier_path is not UTF-8 in {label}") from error
    if value.startswith(("/", "~")) or "\\" in value:
        raise RuntimeError(f"source_carrier_path is unsafe in {label}")
    return value


def applicable_evidence(parent: str) -> dict[str, object]:
    source_root = APPLICABLE_SOURCE_ROOT.resolve()
    role_records: list[dict[str, object]] = []
    source_records: list[dict[str, object]] = []
    for role in ROLE_NAMES:
        old_directory = APPLICABLE_ROOT / role
        planned_directory = APPLICABLE_TARGET_ROOT / role
        if old_directory.is_symlink() or not old_directory.is_dir():
            raise RuntimeError(f"Applicable Methodology source role is unavailable: {repository_path(old_directory)}")
        if planned_directory.exists() or planned_directory.is_symlink():
            raise RuntimeError(f"Applicable Methodology planned target changed after denial: {repository_path(planned_directory)}")
        paths = sorted(old_directory.rglob("*.md"))
        role_records.append({
            "old_path": repository_path(old_directory),
            "planned_new_path": repository_path(planned_directory),
            "current_state": "untouched_at_old_path",
            "carrier_count": len(paths),
        })
        for path in paths:
            relative_path = repository_path(path)
            current_reference = source_reference(read_current(path, label="Applicable Methodology carrier"), label=relative_path)
            predecessor_reference = source_reference(read_blob(parent, relative_path), label=f"{parent}:{relative_path}")
            resolved_source = (path.parent / current_reference).resolve()
            try:
                resolved_source.relative_to(source_root)
            except ValueError as error:
                raise RuntimeError(f"source_carrier_path leaves authoritative source root: {relative_path}") from error
            source_bytes = read_current(resolved_source, label="authoritative source")
            if current_reference != predecessor_reference:
                raise RuntimeError(f"source_carrier_path changed after denied operation: {relative_path}")
            source_records.append({
                "carrier_path": relative_path,
                "source_carrier_path": current_reference,
                "authoritative_source_path": repository_path(resolved_source),
                "authoritative_source_sha256_current": digest(source_bytes),
                "matches_git_predecessor": True,
            })
    if len(source_records) != 963:
        raise RuntimeError(f"expected 963 untouched Applicable Methodology source links, found {len(source_records)}")
    return {
        "state": "incomplete_denied_untouched",
        "denied_operation": {
            "operation": "rename",
            "source": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/04_requirement",
            "destination": ".caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY/04_requirement",
            "errno": errno.EPERM,
            "errno_name": "EPERM",
            "error": "Operation not permitted",
        },
        "role_directories": role_records,
        "source_links": source_records,
        "summary": {
            "role_directory_count": len(role_records),
            "untouched_source_link_count": len(source_records),
            "source_links_matching_git_predecessor": len(source_records),
            "carrier_rebases_attempted": 0,
            "carrier_moves_retried": 0,
        },
    }


def legacy_manifest_evidence() -> dict[str, object]:
    legacy_bytes = read_current(LEGACY_MANIFEST, label="legacy selected-workflow manifest")
    canonical_bytes = read_current(CANONICAL_MANIFEST, label="canonical selected-workflow manifest")
    if LEGACY_MANIFEST_TARGET.exists() or LEGACY_MANIFEST_TARGET.is_symlink():
        raise RuntimeError("legacy selected-workflow manifest target unexpectedly exists")
    return {
        "state": "untouched_pending",
        "current_path": repository_path(LEGACY_MANIFEST),
        "planned_new_path": repository_path(LEGACY_MANIFEST_TARGET),
        "planned_new_path_exists": False,
        "sha256_current": digest(legacy_bytes),
        "canonical_manifest_path": repository_path(CANONICAL_MANIFEST),
        "canonical_manifest_sha256_current": digest(canonical_bytes),
        "differs_from_canonical_manifest": legacy_bytes != canonical_bytes,
        "move_attempted": False,
    }


def build_evidence() -> dict[str, object]:
    parent = predecessor()
    moves = projection_records(parent)
    return {
        "schema_version": 1,
        "task": "CA-P-1556",
        "scope": "durable read-only accounting of a partial CA-P-1549 migration",
        "completed_move_commit": MOVE_COMMIT,
        "git_predecessor_commit": parent,
        "completed_projection_moves": moves,
        "completed_projection_summary": {
            "state": "byte_verified_completed_partial",
            "move_count": len(moves),
            "total_bytes": sum(int(record["bytes"]) for record in moves),
            "all_bytes_match_predecessor_commit_and_current": True,
        },
        "applicable_methodology": applicable_evidence(parent),
        "legacy_selected_workflow_bindings": legacy_manifest_evidence(),
        "journal": {"state": "untouched", "helper_did_not_read_or_write_journal": True},
        "aggregate_completion_claim": False,
    }


def write_map(evidence: dict[str, object]) -> None:
    if MAP_TARGET.exists() or MAP_TARGET.is_symlink():
        raise RuntimeError(f"migration map already exists: {repository_path(MAP_TARGET)}")
    directory = MAP_TARGET.parent
    if directory.exists():
        if directory.is_symlink() or not directory.is_dir():
            raise RuntimeError(f"migration map parent is not a real directory: {repository_path(directory)}")
    else:
        directory.mkdir(parents=True)
    MAP_TARGET.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the approved partial-evidence map")
    args = parser.parse_args()
    evidence = build_evidence()
    if args.write:
        write_map(evidence)
    summary = {
        "map_written": args.write,
        "projection_move_count": evidence["completed_projection_summary"]["move_count"],
        "projection_total_bytes": evidence["completed_projection_summary"]["total_bytes"],
        "untouched_applicable_source_links": evidence["applicable_methodology"]["summary"]["untouched_source_link_count"],
        "legacy_manifest_move_attempted": evidence["legacy_selected_workflow_bindings"]["move_attempted"],
        "aggregate_completion_claim": evidence["aggregate_completion_claim"],
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
