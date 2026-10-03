#!/usr/bin/env python3
"""Migrate the framework identity, content role, and specification acronym.

This standalone migration is read-only by default. It changes the framework
identity ``CAPRMADIO`` to ``CAPRMEDIO``, the content role ``Assurance`` to
``Evaluation``, token-bounded ``ASSU`` to ``EVAL``, and token-bounded ``RMAD``
to ``RMED`` while preserving case.
Append-only journals, runtime state, caches and virtual environments, symlinks,
binary file contents, and this script are outside the mutable content surface.
Verification reports excluded historical/runtime occurrences separately from
mutable leftovers.
"""
from __future__ import annotations

import argparse
import os
import re
import stat
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


SCRIPT_RELATIVE_PATH = Path("002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/migrate_framework_identity.py")
SCRIPT_PATH = Path(__file__).resolve()
TOOLS_ROOT = SCRIPT_PATH.parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402

LEFT_TOKEN_BOUNDARY = r"(?:(?<![A-Za-z0-9])|(?<=\\[nrt]))"
FRAMEWORK_PATTERN = re.compile(
    rf"{LEFT_TOKEN_BOUNDARY}CAPRMADIO(?![A-Za-z0-9])",
    re.IGNORECASE,
)
ROLE_PATTERN = re.compile(
    rf"{LEFT_TOKEN_BOUNDARY}ASSURANCE(?![A-Za-z0-9])",
    re.IGNORECASE,
)
SHORT_ROLE_PATTERN = re.compile(
    rf"{LEFT_TOKEN_BOUNDARY}ASSU(?![A-Za-z0-9])",
    re.IGNORECASE,
)
SPEC_ACRONYM_PATTERN = re.compile(
    rf"{LEFT_TOKEN_BOUNDARY}RMAD(?![A-Za-z0-9])",
    re.IGNORECASE,
)
OLD_PATTERNS = (
    FRAMEWORK_PATTERN,
    ROLE_PATTERN,
    SHORT_ROLE_PATTERN,
    SPEC_ACRONYM_PATTERN,
)

BINARY_SUFFIXES = {
    ".7z", ".a", ".bin", ".bmp", ".class", ".db", ".dll", ".dylib", ".eot",
    ".exe", ".gif", ".gz", ".ico", ".jpeg", ".jpg", ".lockb", ".mp3", ".mp4",
    ".o", ".pdf", ".png", ".pyc", ".so", ".sqlite", ".tar", ".ttf", ".wav",
    ".webp", ".woff", ".woff2", ".xz", ".zip",
}

CACHE_OR_VENV_PARTS = {
    ".cache", ".conda", ".coverage", ".env", ".gradle", ".hypothesis",
    ".mypy_cache", ".next", ".nox", ".pytest_cache", ".ruff_cache", ".sass-cache",
    ".tox", ".turbo", ".uv-cache", ".venv", "__pycache__", "build", "cache",
    "coverage", "dist", "env", "node_modules", "out", "site-packages", "target",
    "venv",
}


@dataclass(frozen=True)
class PathMove:
    source: Path
    destination: Path


@dataclass(frozen=True)
class TextChange:
    source: Path
    original: bytes
    revised: bytes
    mode: int


@dataclass(frozen=True)
class SymlinkChange:
    source: Path
    original_target: str
    revised_target: str


@dataclass(frozen=True)
class Plan:
    moves: tuple[PathMove, ...]
    text_changes: tuple[TextChange, ...]
    symlink_changes: tuple[SymlinkChange, ...]


@dataclass(frozen=True)
class Verification:
    mutable_leftovers: int
    excluded_occurrences: int
    excluded_by_reason: tuple[tuple[str, int], ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="repository root (default: current directory)")
    parser.add_argument("--apply", action="store_true", help="write the migration; default is dry-run")
    parser.add_argument("--session-id", help="required provenance identifier with --apply")
    parser.add_argument(
        "--verify", "--verification", action="store_true",
        help="verify mutable leftovers without writing",
    )
    parser.add_argument("--show", type=int, default=20, help="maximum preview entries (default: 20)")
    return parser.parse_args()


def resolve_root(argument: str) -> Path:
    root = Path(argument).expanduser().resolve()
    if not root.is_dir():
        raise RuntimeError(f"repository root is not a directory: {root}")
    return root


def exclusion_reason(path: Path, root: Path) -> str | None:
    """Return the first applicable exclusion reason for *path*."""

    if path.resolve() == SCRIPT_PATH:
        return "migration-script"
    try:
        relative = path.relative_to(root)
    except ValueError:
        return "outside-root"
    if relative == SCRIPT_RELATIVE_PATH:
        return "migration-script"
    parts = relative.parts
    lowered = {part.casefold() for part in parts}
    if ".git" in lowered:
        return "git"
    if "010_journals" in lowered:
        return "journals"
    if ".caprmadio_runtime" in lowered or ".caprmedio_runtime" in lowered:
        return "runtime"
    if any(part.casefold() in CACHE_OR_VENV_PARTS for part in parts):
        return "cache-or-venv"
    return None


def iter_entries(root: Path, *, include_historical: bool = False) -> list[Path]:
    """Enumerate regular entries and directories on the supported surface."""

    entries: list[Path] = []
    for current, directories, files in os.walk(root, topdown=True, followlinks=False):
        current_path = Path(current)
        retained_directories: list[str] = []
        for name in directories:
            candidate = current_path / name
            reason = exclusion_reason(candidate, root)
            if candidate.is_symlink():
                if reason is None:
                    entries.append(candidate)
                continue
            if reason is None:
                retained_directories.append(name)
            elif include_historical and reason in {"journals", "runtime"}:
                retained_directories.append(name)
        directories[:] = retained_directories
        for name in retained_directories:
            entries.append(current_path / name)
        for name in files:
            candidate = current_path / name
            entries.append(candidate)
    return sorted(entries, key=lambda item: item.relative_to(root).as_posix())


def preserve_case(source: str, target: str) -> str:
    if source.isupper():
        return target.upper()
    if source.islower():
        return target.lower()
    if source[:1].isupper() and source[1:].islower():
        return target[:1].upper() + target[1:].lower()

    result: list[str] = []
    for index, character in enumerate(target):
        source_character = source[index] if index < len(source) else source[-1]
        if source_character.isupper():
            result.append(character.upper())
        elif source_character.islower():
            result.append(character.lower())
        else:
            result.append(character)
    return "".join(result)


def replace_case(pattern: re.Pattern[str], target: str, text: str) -> str:
    return pattern.sub(lambda match: preserve_case(match.group(0), target), text)


def rewrite_text(text: str) -> str:
    rewritten = replace_case(FRAMEWORK_PATTERN, "CAPRMEDIO", text)
    rewritten = replace_case(ROLE_PATTERN, "Evaluation", rewritten)
    rewritten = replace_case(SHORT_ROLE_PATTERN, "EVAL", rewritten)
    return replace_case(SPEC_ACRONYM_PATTERN, "RMED", rewritten)


def transformed_name(name: str) -> str:
    return rewrite_text(name)


def is_probably_text(path: Path, payload: bytes) -> bool:
    if path.suffix.casefold() in BINARY_SUFFIXES or b"\x00" in payload:
        return False
    try:
        payload.decode("utf-8")
    except UnicodeDecodeError:
        return False
    controls = sum(byte < 9 or 13 < byte < 32 for byte in payload)
    return not payload or controls * 20 <= len(payload)


def read_text(path: Path) -> tuple[bytes, str] | None:
    payload = path.read_bytes()
    if not is_probably_text(path, payload):
        return None
    return payload, payload.decode("utf-8")


def mutable_entries(root: Path) -> list[Path]:
    return [path for path in iter_entries(root) if exclusion_reason(path, root) is None]


def path_key(path: Path, root: Path) -> str:
    # Case-folding catches collisions on case-insensitive filesystems before
    # os.replace can encounter them halfway in.
    return path.relative_to(root).as_posix().casefold()


def plan_path_moves(root: Path, entries: list[Path]) -> tuple[PathMove, ...]:
    moves: list[PathMove] = []
    for source in entries:
        new_name = transformed_name(source.name)
        if new_name != source.name:
            moves.append(PathMove(source, source.with_name(new_name)))

    destinations: dict[str, Path] = {}
    existing_entries = {path_key(path, root): path for path in entries}
    collisions: list[str] = []
    for move in moves:
        destination_key = path_key(move.destination, root)
        previous = destinations.get(destination_key)
        if previous is not None:
            collisions.append(
                f"{move.destination.relative_to(root)} from "
                f"{previous.relative_to(root)} and {move.source.relative_to(root)}"
            )
        destinations[destination_key] = move.source
        # Any existing destination is a collision, including another source
        # being renamed. The key check catches case-only aliases on a
        # case-sensitive checkout before an operator moves it to macOS.
        existing = existing_entries.get(destination_key)
        if existing is not None or os.path.lexists(move.destination):
            existing_label = (
                existing.relative_to(root).as_posix() if existing is not None
                else move.destination.relative_to(root).as_posix()
            )
            collisions.append(
                f"{move.destination.relative_to(root)} already exists "
                f"as {existing_label} "
                f"(source {move.source.relative_to(root)})"
            )

    if collisions:
        sample = "; ".join(collisions[:5])
        suffix = "" if len(collisions) <= 5 else f"; ... {len(collisions) - 5} more"
        raise RuntimeError(f"destination collision(s): {sample}{suffix}")

    # Deepest-first lets nested directory moves complete before parent moves.
    return tuple(
        sorted(
            moves,
            key=lambda move: (
                -len(move.source.relative_to(root).parts),
                move.source.relative_to(root).as_posix(),
            ),
        )
    )


def destination_for(path: Path, root: Path) -> Path:
    relative = path.relative_to(root)
    return root.joinpath(*(transformed_name(part) for part in relative.parts))


def plan_text_changes(root: Path, entries: list[Path]) -> tuple[TextChange, ...]:
    changes: list[TextChange] = []
    for path in entries:
        if not path.is_file() or path.is_symlink():
            continue
        result = read_text(path)
        if result is None:
            continue
        original, text = result
        revised = rewrite_text(text).encode("utf-8")
        if revised != original:
            changes.append(
                TextChange(
                    source=path,
                    original=original,
                    revised=revised,
                    mode=stat.S_IMODE(path.stat().st_mode),
                )
            )
    return tuple(changes)


def plan_symlink_changes(entries: list[Path]) -> tuple[SymlinkChange, ...]:
    changes: list[SymlinkChange] = []
    for path in entries:
        if not path.is_symlink():
            continue
        original_target = os.readlink(path)
        revised_target = rewrite_text(original_target)
        if revised_target != original_target:
            changes.append(
                SymlinkChange(
                    source=path,
                    original_target=original_target,
                    revised_target=revised_target,
                )
            )
    return tuple(changes)


def build_plan(root: Path) -> Plan:
    entries = mutable_entries(root)
    return Plan(
        moves=plan_path_moves(root, entries),
        text_changes=plan_text_changes(root, entries),
        symlink_changes=plan_symlink_changes(entries),
    )


def atomic_write(path: Path, payload: bytes, mode: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(
        path, "migrations", prefix=".identity-migration-", suffix=".tmp"
    )
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


def apply_plan(root: Path, plan: Plan) -> None:
    completed_moves: list[PathMove] = []
    written: list[tuple[TextChange, Path]] = []
    rewritten_symlinks: list[tuple[SymlinkChange, Path]] = []
    try:
        for move in plan.moves:
            if os.path.lexists(move.destination):
                raise RuntimeError(
                    f"destination appeared during apply: {move.destination.relative_to(root)}"
                )
            os.replace(move.source, move.destination)
            completed_moves.append(move)

        for change in plan.text_changes:
            destination = destination_for(change.source, root)
            atomic_write(destination, change.revised, change.mode)
            written.append((change, destination))

        for change in plan.symlink_changes:
            destination = destination_for(change.source, root)
            destination.unlink()
            destination.symlink_to(change.revised_target)
            rewritten_symlinks.append((change, destination))
    except BaseException:
        # Restore changed content first while the moved topology is still
        # present, then undo moves in reverse (parent moves are undone first).
        for change, destination in reversed(written):
            try:
                atomic_write(destination, change.original, change.mode)
            except OSError:
                pass
        for change, destination in reversed(rewritten_symlinks):
            try:
                destination.unlink()
                destination.symlink_to(change.original_target)
            except OSError:
                pass
        for move in reversed(completed_moves):
            try:
                os.replace(move.destination, move.source)
            except OSError:
                pass
        raise


def matching_count(text: str) -> int:
    return sum(len(pattern.findall(text)) for pattern in OLD_PATTERNS)


def verify_tree(root: Path) -> Verification:
    mutable_leftovers = 0
    excluded_occurrences = 0
    by_reason: Counter[str] = Counter()
    for path in iter_entries(root, include_historical=True):
        reason = exclusion_reason(path, root)
        if reason == "migration-script":
            continue
        path_matches = matching_count(path.name)
        if reason is None:
            mutable_leftovers += path_matches
        elif reason in {"journals", "runtime"}:
            excluded_occurrences += path_matches
            by_reason[reason] += path_matches

        if path.is_symlink() and reason in {None, "journals", "runtime"}:
            target_matches = matching_count(os.readlink(path))
            if reason is None:
                mutable_leftovers += target_matches
            else:
                excluded_occurrences += target_matches
                by_reason[reason] += target_matches
        elif path.is_file() and reason in {None, "journals", "runtime"}:
            result = read_text(path)
            if result is None:
                continue
            content_matches = matching_count(result[1])
            if reason is None:
                mutable_leftovers += content_matches
            else:
                excluded_occurrences += content_matches
                by_reason[reason] += content_matches
    return Verification(
        mutable_leftovers=mutable_leftovers,
        excluded_occurrences=excluded_occurrences,
        excluded_by_reason=tuple(sorted(by_reason.items())),
    )


def print_plan(root: Path, plan: Plan, show: int, mode: str) -> None:
    total_changes = len(plan.moves) + len(plan.text_changes) + len(plan.symlink_changes)
    print(
        f"mode={mode} changes={total_changes} path_moves={len(plan.moves)} "
        f"text_changes={len(plan.text_changes)} "
        f"symlink_changes={len(plan.symlink_changes)}"
    )
    limit = max(show, 0)
    for move in plan.moves[:limit]:
        print(f"path {move.source.relative_to(root)} -> {move.destination.relative_to(root)}")
    if len(plan.moves) > limit:
        print(f"path_preview_remaining={len(plan.moves) - limit}")
    for change in plan.text_changes[:limit]:
        print(f"text {change.source.relative_to(root)}")
    if len(plan.text_changes) > limit:
        print(f"text_preview_remaining={len(plan.text_changes) - limit}")
    for change in plan.symlink_changes[:limit]:
        print(
            f"symlink {change.source.relative_to(root)}: "
            f"{change.original_target} -> {change.revised_target}"
        )
    if len(plan.symlink_changes) > limit:
        print(f"symlink_preview_remaining={len(plan.symlink_changes) - limit}")


def print_verification(verification: Verification, *, result: str) -> None:
    details = ",".join(f"{name}:{count}" for name, count in verification.excluded_by_reason)
    print(
        f"verification={result} mutable_leftovers={verification.mutable_leftovers} "
        f"excluded_occurrences={verification.excluded_occurrences} "
        f"excluded_by_reason={details or 'none'}"
    )


def main() -> int:
    args = parse_args()
    if args.apply and not args.session_id:
        raise RuntimeError("--session-id is required with --apply")
    root = resolve_root(args.root)

    if args.verify and not args.apply:
        verification = verify_tree(root)
        print_verification(
            verification,
            result="pass" if verification.mutable_leftovers == 0 else "fail",
        )
        return 0 if verification.mutable_leftovers == 0 else 1

    plan = build_plan(root)
    print_plan(root, plan, args.show, "apply" if args.apply else "dry-run")
    if not args.apply:
        verification = verify_tree(root)
        print_verification(
            verification,
            result="pass" if verification.mutable_leftovers == 0 else "planned",
        )
        return 0

    apply_plan(root, plan)
    verification = verify_tree(root)
    print_verification(
        verification,
        result="pass" if verification.mutable_leftovers == 0 else "fail",
    )
    return 0 if verification.mutable_leftovers == 0 else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(f"error={error}", file=sys.stderr)
        raise SystemExit(2)
