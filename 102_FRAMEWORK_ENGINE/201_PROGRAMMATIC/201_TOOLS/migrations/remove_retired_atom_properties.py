#!/usr/bin/env python3
"""Plan/apply exact removal of three retired Atom frontmatter properties."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import stat
import sys
from typing import Any, Iterator

import yaml
from yaml.events import AliasEvent, MappingEndEvent, MappingStartEvent
from yaml.events import SequenceEndEvent, SequenceStartEvent
from yaml.nodes import MappingNode, Node, ScalarNode, SequenceNode


RETIRED_PROPERTIES = frozenset({"cce_form", "cce_version", "llm_session_ids"})
PLAN_KIND = "remove_retired_atom_properties"
EXCLUDED_PARTS = frozenset({"history", "archive", "archives", "archived", "draft", "drafts",
                            "status", "statuses", "done", "resolved", "canceled", "cancelled"})
SAFE_TAGS = frozenset("tag:yaml.org,2002:" + name for name in (
    "null", "bool", "int", "float", "binary", "timestamp", "omap", "pairs", "set",
    "str", "seq", "map",
))


class MigrationError(ValueError):
    """Unsafe, stale, or unsupported input; no guessed transformation."""


def _digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _yaml_resources(frontmatter: str) -> None:
    depth = 0
    for count, event in enumerate(yaml.parse(frontmatter, Loader=yaml.SafeLoader), 1):
        if isinstance(event, AliasEvent) or getattr(event, "anchor", None):
            raise MigrationError("YAML anchors and aliases are unsupported.")
        if isinstance(event, (MappingStartEvent, SequenceStartEvent)):
            depth += 1
        if isinstance(event, (MappingEndEvent, SequenceEndEvent)):
            depth -= 1
        if depth > 64 or count > 100_000:
            raise MigrationError("YAML exceeds the parser safety ceiling.")


def _validate_node(node: Node) -> None:
    if node.tag not in SAFE_TAGS:
        raise MigrationError("Unsupported YAML tag or merge key.")
    if isinstance(node, MappingNode):
        keys: set[str] = set()
        for key, value in node.value:
            if not isinstance(key, ScalarNode) or key.tag != "tag:yaml.org,2002:str":
                raise MigrationError("YAML mapping keys must be strings.")
            if key.value in keys:
                raise MigrationError("Duplicate YAML mapping key.")
            keys.add(key.value)
            _validate_node(value)
    elif isinstance(node, SequenceNode):
        for child in node.value:
            _validate_node(child)


def _mapping(frontmatter: str) -> MappingNode | None:
    _yaml_resources(frontmatter)
    node = yaml.compose(frontmatter, Loader=yaml.SafeLoader)
    if node is None:
        return None
    if not isinstance(node, MappingNode) or node.flow_style:
        raise MigrationError("Frontmatter must be a block-style YAML mapping.")
    _validate_node(node)
    for key, _ in node.value:
        if key.start_mark.column != 0 or key.start_mark.line != key.end_mark.line:
            raise MigrationError("Indented, explicit, or multiline top-level keys are unsupported.")
    return node


def _syntax_end(node: Node) -> int:
    """Block collection end marks can point past unrelated trailing comments."""
    if isinstance(node, ScalarNode) or getattr(node, "flow_style", False):
        return node.end_mark.index
    if isinstance(node, MappingNode):
        return max((_syntax_end(n) for pair in node.value for n in pair), default=node.end_mark.index)
    return max((_syntax_end(n) for n in node.value), default=node.end_mark.index)


def _line_end(text: str, index: int) -> int:
    if index > 0 and text[index - 1] == "\n":
        return index
    newline = text.find("\n", index)
    return len(text) if newline < 0 else newline + 1


def _frontmatter(raw: bytes) -> tuple[str, str, str]:
    text = raw.decode("utf-8")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0] not in ("---\n", "---\r\n"):
        raise MigrationError("Carrier must start with a YAML frontmatter delimiter.")
    for index, line in enumerate(lines[1:], 1):
        if line in ("---\n", "---\r\n", "---"):
            return lines[0], "".join(lines[1:index]), "".join(lines[index:])
    raise MigrationError("Carrier has no supported closing frontmatter delimiter.")


def _node_signature(node: Node | None) -> Any:
    if node is None:
        return None
    if isinstance(node, MappingNode):
        return (node.tag, tuple((_node_signature(k), _node_signature(v)) for k, v in node.value))
    if isinstance(node, SequenceNode):
        return (node.tag, tuple(_node_signature(child) for child in node.value))
    return (node.tag, node.value)


def remove_retired_properties(raw: bytes) -> tuple[bytes, list[str]]:
    """Remove only the three top-level keys, retaining all other carrier bytes.

    PyYAML marks address Unicode code points, so surgery is on decoded UTF-8;
    encoding back preserves original bytes, including CRLF and Markdown bodies.
    Invalid/ambiguous YAML raises MigrationError (a ValueError subclass).
    """
    try:
        opening, frontmatter, closing_and_body = _frontmatter(raw)
        mapping = _mapping(frontmatter)
        if mapping is None:
            return raw, []
        spans: list[tuple[int, int]] = []
        removed: list[str] = []
        kept = []
        for key, value in mapping.value:
            if key.value in RETIRED_PROPERTIES:
                spans.append((key.start_mark.index, _line_end(frontmatter, _syntax_end(value))))
                removed.append(key.value)
            else:
                kept.append((key, value))
        if not removed:
            return raw, []
        changed = frontmatter
        for start, end in reversed(spans):
            changed = changed[:start] + changed[end:]
        expected = MappingNode(mapping.tag, kept)
        after_node = _mapping(changed)
        if kept and _node_signature(expected) != _node_signature(after_node):
            raise MigrationError("Removal would change a retained YAML value.")
        if not kept and after_node is not None:
            raise MigrationError("Removal did not leave empty frontmatter.")
        return (opening + changed + closing_and_body).encode("utf-8"), removed
    except MigrationError:
        raise
    except (UnicodeError, yaml.YAMLError, RecursionError) as error:
        raise MigrationError("Malformed or unsupported UTF-8/YAML frontmatter.") from error


def _revision(raw: bytes) -> tuple[bytes, int]:
    opening, frontmatter, closing_and_body = _frontmatter(raw)
    mapping = _mapping(frontmatter)
    if mapping is not None:
        for key, value in mapping.value:
            if key.value != "version":
                continue
            start, end = value.start_mark.index, value.end_mark.index
            if value.tag != "tag:yaml.org,2002:int" or re.fullmatch(r"[1-9][0-9]*", frontmatter[start:end]) is None:
                raise MigrationError("Version must be an unquoted positive decimal integer.")
            version = int(frontmatter[start:end])
            changed = frontmatter[:start] + str(version + 1) + frontmatter[end:]
            return (opening + changed + closing_and_body).encode("utf-8"), version
    raise MigrationError("A carried Version is required for revision-safe migration.")


def _archive_path(path: Path, version: int) -> Path:
    return path.parent / "archive" / f"{path.stem}@{version}{path.suffix}"


def _archive_exists(path: Path, before: bytes) -> bool:
    try:
        existing = _read(path)
    except FileNotFoundError:
        return False
    if existing != before:
        raise MigrationError("Existing revision archive differs from the exact prior carrier.")
    return True


def _absolute(value: Any) -> Path:
    if not isinstance(value, str) or not value or "\x00" in value:
        raise MigrationError("Expected a nonempty filesystem path.")
    path = Path(value)
    if not path.is_absolute() or ".." in path.parts:
        raise MigrationError("Paths must be absolute and cannot contain parent traversal.")
    return path


def _check_parts(path: Path) -> None:
    for part in path.parts:
        if part == ".env" or part.startswith(".env."):
            raise MigrationError("Protected .env path is excluded.")


def _carrier_path(value: Any, root: Path) -> Path:
    path = _absolute(value)
    _check_parts(path)
    if not path.is_relative_to(root) or path == root or path.suffix.lower() != ".md":
        raise MigrationError("Carrier must be a Markdown file beneath source-root.")
    directories = (root.name, *path.relative_to(root).parts[:-1])
    if any(part.casefold().lstrip("._") in EXCLUDED_PARTS for part in directories):
        raise MigrationError("History, archive, draft, and status directories are excluded.")
    return path


def _directory(path: Path) -> int:
    current = os.open(path.anchor, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for part in path.parts[1:]:
            following = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=current)
            os.close(current)
            current = following
        return current
    except BaseException:
        os.close(current)
        raise


@contextmanager
def _descriptor(path: Path, flags: int = os.O_RDONLY) -> Iterator[int]:
    """Open every directory and the final file without following symlinks."""
    current = _directory(path.parent)
    try:
        descriptor = os.open(path.name, flags | os.O_NOFOLLOW, dir_fd=current)
        try:
            info = os.fstat(descriptor)
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                raise MigrationError("Carrier must be a regular file with exactly one hard link.")
            yield descriptor
        finally:
            os.close(descriptor)
    finally:
        os.close(current)


def _read_descriptor(descriptor: int) -> bytes:
    os.lseek(descriptor, 0, os.SEEK_SET)
    chunks = []
    while chunk := os.read(descriptor, 1024 * 1024):
        chunks.append(chunk)
    return b"".join(chunks)


def _read(path: Path) -> bytes:
    with _descriptor(path) as descriptor:
        return _read_descriptor(descriptor)


def _json_read(path: Path) -> tuple[bytes, dict[str, Any]]:
    _check_parts(path)
    raw = _read(path)
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise MigrationError("Expected a JSON object.")
    return raw, value


def _report_inputs(report: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, set[str]]]:
    carriers = {}
    for carrier in report["carriers"]:
        path = carrier["path"]
        if path in carriers:
            raise MigrationError("Duplicate report carrier path.")
        carriers[path] = carrier
    selected = report.get("selection", {}).get("selected", list(carriers))
    if len(set(selected)) != len(selected) or set(selected) != set(carriers):
        raise MigrationError("Report selection and assessed carriers must match exactly.")
    targets: dict[str, set[str]] = {}
    for finding in report["findings"]:
        if finding.get("code") == "PROPERTY_RETIRED" and finding.get("property") in RETIRED_PROPERTIES:
            path = finding.get("path")
            if path not in carriers:
                raise MigrationError("Retired-property finding has no selected carrier binding.")
            targets.setdefault(path, set()).add(finding["property"])
    return carriers, targets


def _report_carrier(carrier: dict[str, Any], root: Path) -> tuple[Path, bytes]:
    path = _carrier_path(carrier["path"], root)
    if carrier.get("representation", "source") != "source":
        raise MigrationError("Only source carriers can be migrated.")
    raw = _read(path)
    if _digest(raw) != carrier.get("sha256"):
        raise MigrationError("Carrier changed since validation; produce a fresh report.")
    return path, raw


def build_plan(report: dict[str, Any], root: Path, report_raw: bytes) -> dict[str, Any]:
    carriers, targets = _report_inputs(report)
    baseline, changes, blockers = [], [], []
    for name, carrier in sorted(carriers.items()):
        try:
            path, raw = _report_carrier(carrier, root)
            baseline.append({"path": str(path), "sha256": _digest(raw)})
            if name not in targets:
                continue
            after, removed = remove_retired_properties(raw)
            if set(removed) != targets[name]:
                raise MigrationError("Reported retired properties do not match the carrier exactly.")
            if removed:
                after, version = _revision(after)
                archive = _archive_path(path, version)
                _archive_exists(archive, raw)
                changes.append({"path": str(path), "before_sha256": _digest(raw),
                                "after_sha256": _digest(after), "before": raw.decode("utf-8"),
                                "after": after.decode("utf-8"), "removed": removed,
                                "version": version, "after_version": version + 1,
                                "archive": str(archive), "archive_sha256": _digest(raw)})
        except (MigrationError, OSError) as error:
            blockers.append({"path": name, "reason": str(error)})
    return {"schema_version": 1, "kind": PLAN_KIND, "mode": "dry-run", "source_root": str(root),
            "report_sha256": _digest(report_raw), "baseline": baseline, "changes": changes,
            "blockers": blockers, "counts": {"selected": len(carriers), "changes": len(changes),
            "removed_properties": sum(len(change["removed"]) for change in changes),
            "blockers": len(blockers)}}


def _validate_change(change: dict[str, Any], root: Path) -> tuple[str, bytes]:
    path = _carrier_path(change["path"], root)
    before, after = change["before"].encode("utf-8"), change["after"].encode("utf-8")
    if _digest(before) != change["before_sha256"] or _digest(after) != change["after_sha256"]:
        raise MigrationError("Plan content does not match its recorded digests.")
    transformed, removed = remove_retired_properties(before)
    transformed, version = _revision(transformed)
    if not removed or transformed != after or removed != change["removed"]:
        raise MigrationError("Plan change is not the exact retired-property transformation.")
    if (change["version"] != version or change["after_version"] != version + 1
            or change["archive"] != str(_archive_path(path, version))
            or change["archive_sha256"] != _digest(before)):
        raise MigrationError("Plan does not preserve the exact required prior revision archive.")
    return str(path), after


def _plan_changes(plan: dict[str, Any], root: Path) -> dict[str, dict[str, Any]]:
    if plan.get("schema_version") != 1 or plan.get("kind") != PLAN_KIND or plan.get("blockers"):
        raise MigrationError("Unsupported or blocked migration plan.")
    changes = {}
    for change in plan["changes"]:
        name, _ = _validate_change(change, root)
        if name in changes:
            raise MigrationError("Duplicate plan change path.")
        changes[name] = change
    return changes


def _preflight(plan: dict[str, Any], root: Path, changes: dict[str, dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    completed = []
    for binding in plan["baseline"]:
        name = str(_carrier_path(binding["path"], root))
        if name in seen:
            raise MigrationError("Duplicate baseline path.")
        seen.add(name)
        current = _digest(_read(Path(name)))
        change = changes.get(name)
        if change and binding["sha256"] != change["before_sha256"]:
            raise MigrationError("Baseline and change digests disagree.")
        if change and current == change["after_sha256"]:
            completed.append(name)
        elif current != binding["sha256"]:
            raise MigrationError("Baseline changed or is missing; no carriers were written.")
    if not set(changes).issubset(seen):
        raise MigrationError("Plan change has no baseline binding.")
    for change in changes.values():
        _archive_exists(Path(change["archive"]), change["before"].encode("utf-8"))
    return completed


def _ensure_archive(change: dict[str, Any]) -> None:
    path = Path(change["archive"])
    before = change["before"].encode("utf-8")
    if _archive_exists(path, before):
        return
    # Create the fixed sibling through a no-follow descriptor as well.
    parent = _directory(path.parent.parent)
    try:
        try:
            os.mkdir(path.parent.name, dir_fd=parent)
        except FileExistsError:
            pass
    finally:
        os.close(parent)
    try:
        with _descriptor_output(path) as descriptor:
            _write_descriptor(descriptor, before)
            os.fsync(descriptor)
    except FileExistsError:
        if not _archive_exists(path, before):
            raise MigrationError("Revision archive appeared but cannot be verified.")
    if not _archive_exists(path, before):
        raise MigrationError("Revision archive failed read-back verification.")


def _write_descriptor(descriptor: int, raw: bytes) -> None:
    remaining = memoryview(raw)
    while remaining:
        written = os.write(descriptor, remaining)
        if written == 0:
            raise OSError("Write made no progress.")
        remaining = remaining[written:]


def _replace_carrier(parent: int, path: Path, source: int, change: dict[str, Any]) -> None:
    original = os.fstat(source)
    if not stat.S_ISREG(original.st_mode) or original.st_nlink != 1:
        raise MigrationError("Carrier must remain a singly linked regular file.")
    temporary = ".retired-properties-" + secrets.token_hex(12) + ".tmp"
    staged = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                     stat.S_IMODE(original.st_mode), dir_fd=parent)
    exists = True
    try:
        try:
            os.fchmod(staged, stat.S_IMODE(original.st_mode))
            _write_descriptor(staged, change["after"].encode("utf-8"))
            os.fsync(staged)
        finally:
            os.close(staged)
        current = os.stat(path.name, dir_fd=parent, follow_symlinks=False)
        if ((current.st_dev, current.st_ino) != (original.st_dev, original.st_ino)
                or current.st_nlink != 1 or not stat.S_ISREG(current.st_mode)
                or _digest(_read_descriptor(source)) != change["before_sha256"]):
            raise MigrationError("Carrier changed immediately before replacement; apply stopped.")
        os.replace(temporary, path.name, src_dir_fd=parent, dst_dir_fd=parent)
        exists = False
        os.fsync(parent)
    finally:
        if exists:
            os.unlink(temporary, dir_fd=parent)


def _apply_change(change: dict[str, Any]) -> bool:
    path = Path(change["path"])
    parent = _directory(path.parent)
    try:
        source = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent)
        try:
            current = _digest(_read_descriptor(source))
            if current == change["after_sha256"]:
                return False
            if current != change["before_sha256"]:
                raise MigrationError("Carrier changed immediately before write; apply stopped.")
            _replace_carrier(parent, path, source, change)
        finally:
            os.close(source)
        if _digest(_read(path)) != change["after_sha256"]:
            raise MigrationError("Carrier read-back digest mismatch.")
        return True
    finally:
        os.close(parent)


def apply_plan(plan: dict[str, Any], root: Path) -> dict[str, Any]:
    changes = _plan_changes(plan, root)
    completed = _preflight(plan, root, changes)
    applied = []
    for name, change in changes.items():
        _ensure_archive(change)
        if _apply_change(change):
            applied.append(name)
        elif name not in completed:
            completed.append(name)
    return {"schema_version": 1, "kind": PLAN_KIND, "mode": "apply", "source_root": str(root),
            "applied": applied, "already_applied": sorted(completed),
            "counts": {"applied": len(applied), "already_applied": len(completed)}}


def _output(path: str | None, result: dict[str, Any]) -> None:
    encoded = (json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    if path is None:
        sys.stdout.buffer.write(encoded)
        return
    output = _absolute(str(Path(path).absolute()))
    _check_parts(output)
    # Never overwrite a carrier, existing plan, report, symlink, or other file.
    with _descriptor_output(output) as descriptor:
        remaining = memoryview(encoded)
        while remaining:
            written = os.write(descriptor, remaining)
            if written == 0:
                raise OSError("Output write made no progress.")
            remaining = remaining[written:]


def _preflight_output(value: str | None) -> None:
    if value is None:
        return
    path = _absolute(str(Path(value).absolute()))
    _check_parts(path)
    parent = _directory(path.parent)
    try:
        try:
            os.stat(path.name, dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError:
            return
        raise MigrationError("Output file already exists; no carriers were written.")
    finally:
        os.close(parent)


@contextmanager
def _descriptor_output(path: Path) -> Iterator[int]:
    current = _directory(path.parent)
    try:
        descriptor = os.open(path.name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                             0o600, dir_fd=current)
        try:
            yield descriptor
        finally:
            os.close(descriptor)
    finally:
        os.close(current)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", help="Existing VALIDATE_ATOMS JSON report")
    parser.add_argument("--source-root", help="Exact allowed source directory")
    parser.add_argument("--output", help="New plan/receipt JSON file (never overwrites)")
    parser.add_argument("--apply", metavar="PLAN", help="Apply this existing reviewed plan")
    args = parser.parse_args(argv)
    try:
        _preflight_output(args.output)
        if args.apply:
            if args.report:
                raise MigrationError("--apply cannot be combined with --report.")
            _, plan = _json_read(_absolute(str(Path(args.apply).absolute())))
            root = _absolute(plan["source_root"])
            if args.source_root and _absolute(str(Path(args.source_root).absolute())) != root:
                raise MigrationError("--source-root differs from the reviewed plan.")
            result = apply_plan(plan, root)
        else:
            if not args.report or not args.source_root or not args.output:
                raise MigrationError("Dry-run requires --report, --source-root, and --output.")
            report_raw, report = _json_read(_absolute(str(Path(args.report).absolute())))
            root = _absolute(str(Path(args.source_root).absolute()))
            result = build_plan(report, root, report_raw)
        _output(args.output, result)
        return 2 if result.get("blockers") else 0
    except (MigrationError, OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(json.dumps({"error": str(error), "kind": PLAN_KIND}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
