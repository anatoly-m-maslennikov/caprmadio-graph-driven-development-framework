"""Read-only, snapshot-stable Markdown Artifact query core.

This module deliberately has no route, Run, Journal, or Projection side effect.
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import re
import secrets
import time
import tomllib
from dataclasses import dataclass
from datetime import date, datetime, time as datetime_time
from pathlib import Path
from typing import Any, Iterable

import yaml

try:  # package import for adapters
    from .query_filter import MISSING, QueryFilterError, evaluate_filter, parse_filter
except ImportError:  # direct tool-path import for standalone execution
    from query_filter import MISSING, QueryFilterError, evaluate_filter, parse_filter


_QUERY_KEYS = frozenset({
    "max_request_bytes", "max_grammar_depth", "max_filter_tokens",
    "max_in_members", "max_selected_fields", "max_page_size",
    "max_snapshot_members", "max_file_bytes", "max_total_read_bytes",
    "timeout_seconds", "max_findings",
})
_SECRET = re.compile(r"(?:secret|password|token|credential|api[_-]?key)", re.I)
_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
_REPOSITORY_ROOT = Path(__file__).resolve().parents[4]
_DEFAULT_SETTINGS = _REPOSITORY_ROOT / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"
_INSTANCE_SETTINGS = _REPOSITORY_ROOT / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
_SNAPSHOT_SIGNING_KEY = secrets.token_bytes(32)


class ArtifactQueryError(ValueError):
    """A rejected query has no accepted partial result."""


class UniqueSafeLoader(yaml.SafeLoader):
    """SafeLoader with duplicate mapping keys rejected at every nesting level."""


def _construct_mapping(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict[str, Any]:
    pairs = loader.construct_pairs(node, deep=deep)
    result: dict[str, Any] = {}
    for key, value in pairs:
        if not isinstance(key, str) or key in result:
            raise ArtifactQueryError("duplicate or non-string frontmatter key")
        result[key] = value
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)


def _normalize_yaml(value: Any) -> Any:
    """Make YAML temporal scalars explicit strings while retaining JSON types."""
    if isinstance(value, (datetime, date, datetime_time)):
        return value.isoformat()
    if isinstance(value, list):
        return [_normalize_yaml(item) for item in value]
    if isinstance(value, dict):
        normalized: dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str) or key in normalized:
                raise ArtifactQueryError("duplicate or non-string frontmatter key")
            normalized[key] = _normalize_yaml(item)
        return normalized
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    raise ArtifactQueryError("unsupported frontmatter value")


def _load_frontmatter(text: str) -> dict[str, Any]:
    try:
        value = yaml.load(text, Loader=UniqueSafeLoader)
    except (yaml.YAMLError, ArtifactQueryError) as error:
        raise ArtifactQueryError("malformed frontmatter") from error
    if not isinstance(value, dict):
        raise ArtifactQueryError("malformed frontmatter")
    return _normalize_yaml(value)


def _validate_rfc6901(token: str) -> str:
    index = 0
    while index < len(token):
        if token[index] == "~":
            if index + 1 >= len(token) or token[index + 1] not in "01":
                raise ArtifactQueryError("invalid RFC 6901 escape")
            index += 2
        else:
            index += 1
    return token.replace("~1", "/").replace("~0", "~")


def _encode_rfc6901(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def _pointer(value: Any, pointer: str) -> Any:
    if not pointer.startswith("/"):
        raise ArtifactQueryError("invalid frontmatter selector")
    for encoded in pointer[1:].split("/"):
        token = _validate_rfc6901(encoded)
        if isinstance(value, dict):
            if token not in value:
                return MISSING
            value = value[token]
        elif isinstance(value, list):
            if not re.fullmatch(r"0|[1-9][0-9]*", token):
                raise ArtifactQueryError("invalid array index")
            offset = int(token)
            if offset >= len(value):
                return MISSING
            value = value[offset]
        else:
            return MISSING
    return value


def _sections(body: str) -> dict[str, str]:
    """Return canonical section paths and bodies, excluding sibling sections."""
    headings: list[tuple[int, str, int, int]] = []
    in_fence: str | None = None
    offset = 0
    for line in body.splitlines(keepends=True):
        fence = _FENCE.match(line)
        if fence:
            marker = fence.group(1)
            if in_fence is None:
                in_fence = marker[0]
            elif marker[0] == in_fence:
                in_fence = None
            offset += len(line)
            continue
        if in_fence is None:
            match = re.match(r"^(#{1,6})[ \t]+(.+?)[ \t]*$", line.rstrip("\r\n"))
            if match:
                headings.append((len(match.group(1)), match.group(2).strip(), offset, offset + len(line)))
        offset += len(line)

    found: dict[str, str] = {}
    stack: list[tuple[int, str]] = []
    for index, (level, heading, _, after) in enumerate(headings):
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, heading))
        key = "/" + "/".join(f"{part_level}:{_encode_rfc6901(part_heading)}" for part_level, part_heading in stack)
        if key in found:
            raise ArtifactQueryError("duplicate heading path")
        end = len(body)
        for next_level, _, next_start, _ in headings[index + 1:]:
            if next_level <= level:
                end = next_start
                break
        found[key] = body[after:end]
    return found


def _section_key(selector: str) -> str:
    if not selector.startswith("section:/"):
        raise ArtifactQueryError("invalid section selector")
    encoded_segments = selector[len("section:/"):].split("/")
    if not encoded_segments or any(not segment for segment in encoded_segments):
        raise ArtifactQueryError("invalid section selector")
    canonical: list[str] = []
    for segment in encoded_segments:
        match = re.fullmatch(r"([1-6]):(.+)", segment)
        if not match:
            raise ArtifactQueryError("invalid section selector")
        decoded = _validate_rfc6901(match.group(2))
        if _encode_rfc6901(decoded) != match.group(2):
            raise ArtifactQueryError("non-canonical section selector")
        canonical.append(f"{match.group(1)}:{match.group(2)}")
    return "/" + "/".join(canonical)


def _validate_selector(selector: str) -> None:
    if not isinstance(selector, str):
        raise ArtifactQueryError("selector must be a string")
    if _SECRET.search(selector):
        raise ArtifactQueryError("secret-shaped selector is forbidden")
    if selector.startswith("fm:"):
        _pointer({}, selector[3:])
        return
    if selector.startswith("section:"):
        _section_key(selector)
        return
    raise ArtifactQueryError("unknown selector namespace")


def _decode_selector(selector: str, frontmatter: dict[str, Any], sections: dict[str, str]) -> Any:
    _validate_selector(selector)
    if selector.startswith("fm:"):
        return _pointer(frontmatter, selector[3:])
    return sections.get(_section_key(selector), MISSING)


def _has_secret_value(value: Any) -> bool:
    if isinstance(value, dict):
        return any(_SECRET.search(key) or _has_secret_value(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_has_secret_value(item) for item in value)
    return isinstance(value, str) and bool(_SECRET.search(value))


def _contains(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def _resolve_root(root: str | Path) -> Path:
    path = Path(root)
    if path.is_symlink() or not path.is_dir():
        raise ArtifactQueryError("inaccessible root")
    try:
        resolved = path.resolve(strict=True)
    except OSError as error:
        raise ArtifactQueryError("inaccessible root") from error
    if not resolved.is_dir():
        raise ArtifactQueryError("inaccessible root")
    return resolved


def _load_budgets(instance_settings: dict[str, int] | None, request_settings: Any) -> dict[str, int]:
    try:
        with _DEFAULT_SETTINGS.open("rb") as handle:
            defaults = tomllib.load(handle).get("query")
        with _INSTANCE_SETTINGS.open("rb") as handle:
            instance = tomllib.load(handle).get("query", {})
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ArtifactQueryError("unable to resolve query settings") from error
    if not isinstance(defaults, dict) or not isinstance(instance, dict):
        raise ArtifactQueryError("invalid query settings")
    budgets = dict(defaults)
    for overrides in (instance, instance_settings, request_settings):
        if overrides is None:
            continue
        if not isinstance(overrides, dict) or set(overrides) - _QUERY_KEYS:
            raise ArtifactQueryError("invalid query settings")
        budgets.update(overrides)
    if set(budgets) != _QUERY_KEYS or any(type(value) is not int or value <= 0 for value in budgets.values()):
        raise ArtifactQueryError("invalid query budget")
    return budgets


def _canonical_bytes(value: Any) -> bytes:
    try:
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise ArtifactQueryError("request must be UTF-8 JSON") from error


def _digest_members(members: list[dict[str, str]]) -> str:
    return hashlib.sha256(_canonical_bytes(members)).hexdigest()


def _request_binding(request: dict[str, Any], selection: list[str], budgets: dict[str, int]) -> str:
    return hashlib.sha256(_canonical_bytes({
        "filter": request.get("filter"), "select": selection, "settings": budgets,
    })).hexdigest()


def _cursor(snapshot_token: str, binding: str, last: str) -> str:
    payload = _canonical_bytes({"snapshot": snapshot_token, "binding": binding, "last": last})
    signature = hmac.new(_SNAPSHOT_SIGNING_KEY, payload, hashlib.sha256).digest()
    return base64.urlsafe_b64encode(payload + signature).decode("ascii")


def _uncursor(value: Any) -> dict[str, str]:
    if not isinstance(value, str):
        raise ArtifactQueryError("malformed cursor")
    try:
        raw = base64.urlsafe_b64decode(value.encode("ascii"))
        payload, signature = raw[:-32], raw[-32:]
        expected = hmac.new(_SNAPSHOT_SIGNING_KEY, payload, hashlib.sha256).digest()
        if not hmac.compare_digest(signature, expected):
            raise ValueError
        decoded = json.loads(payload)
    except Exception as error:
        raise ArtifactQueryError("malformed cursor") from error
    if set(decoded) != {"snapshot", "binding", "last"} or not all(isinstance(item, str) for item in decoded.values()):
        raise ArtifactQueryError("malformed cursor")
    return decoded


@dataclass(frozen=True)
class _Snapshot:
    token: str
    root: str
    members: tuple[dict[str, str], ...]
    digest: str
    binding: str

    def public(self) -> dict[str, str]:
        return {"reference": f"snapshot:{self.token}", "token": self.token, "digest": self.digest}


_RETAINED_SNAPSHOTS: dict[str, _Snapshot] = {}


def _snapshot_from_request(value: Any, root: Path, binding: str) -> _Snapshot:
    if not isinstance(value, dict) or set(value) != {"reference", "token", "digest"}:
        raise ArtifactQueryError("malformed retained snapshot")
    token = value.get("token")
    if not isinstance(token, str):
        raise ArtifactQueryError("malformed retained snapshot")
    snapshot = _RETAINED_SNAPSHOTS.get(token)
    if snapshot is None or value != snapshot.public():
        raise ArtifactQueryError("foreign or tampered retained snapshot")
    if snapshot.root != str(root) or snapshot.binding != binding:
        raise ArtifactQueryError("retained snapshot request mismatch")
    return snapshot


def _walk_markdown(root: Path) -> Iterable[Path]:
    def onerror(error: OSError) -> None:
        raise ArtifactQueryError("incomplete source") from error

    for directory, names, files in os.walk(root, topdown=True, onerror=onerror, followlinks=False):
        folder = Path(directory)
        if not _contains(root, folder.resolve(strict=True)):
            raise ArtifactQueryError("root escape")
        names.sort()
        files.sort()
        for name in names:
            child = folder / name
            if child.is_symlink() or not _contains(root, child.resolve(strict=True)):
                raise ArtifactQueryError("incomplete source")
        for name in files:
            candidate = folder / name
            if candidate.is_symlink() or not _contains(root, candidate.resolve(strict=True)):
                raise ArtifactQueryError("incomplete source")
            if candidate.suffix.lower() != ".md":
                continue
            if _SECRET.search("/".join(candidate.relative_to(root).parts)):
                raise ArtifactQueryError("forbidden secret carrier")
            yield candidate


def _read_member(root: Path, path: Path, *, budgets: dict[str, int], total_read: int, started: float) -> tuple[dict[str, Any], int]:
    if path.is_symlink() or not _contains(root, path.resolve(strict=True)):
        raise ArtifactQueryError("incomplete source")
    try:
        size = path.stat().st_size
    except OSError as error:
        raise ArtifactQueryError("unreadable Markdown") from error
    if size > budgets["max_file_bytes"] or total_read + size > budgets["max_total_read_bytes"]:
        raise ArtifactQueryError("source budget exceeded")
    if time.monotonic() - started > budgets["timeout_seconds"]:
        raise ArtifactQueryError("source budget exceeded")
    try:
        data = path.read_bytes()
    except OSError as error:
        raise ArtifactQueryError("unreadable Markdown") from error
    total_read += len(data)
    if len(data) > budgets["max_file_bytes"] or total_read > budgets["max_total_read_bytes"]:
        raise ArtifactQueryError("source budget exceeded")
    if time.monotonic() - started > budgets["timeout_seconds"]:
        raise ArtifactQueryError("source budget exceeded")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ArtifactQueryError("unreadable Markdown") from error
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ArtifactQueryError("malformed frontmatter")
    frontmatter, body = text[4:].split("\n---\n", 1)
    fm = _load_frontmatter(frontmatter)
    atom = fm.get("atom_id", MISSING)
    artifact = fm.get("artifact_id", MISSING)
    if atom is not MISSING and artifact is not MISSING:
        raise ArtifactQueryError("conflicting artifact identity")
    identity = atom if atom is not MISSING else artifact
    if not isinstance(identity, str) or not identity:
        raise ArtifactQueryError("missing artifact identity")
    return {
        "path": path, "relative": path.relative_to(root).as_posix(), "id": identity,
        "digest": hashlib.sha256(data).hexdigest(), "fm": fm, "sections": _sections(body),
    }, total_read


def _capture_snapshot(root: Path, budgets: dict[str, int], binding: str) -> tuple[_Snapshot, list[dict[str, Any]]]:
    members: list[dict[str, Any]] = []
    findings: list[str] = []
    enumerated = 0
    total_read = 0
    started = time.monotonic()
    for path in _walk_markdown(root):
        enumerated += 1
        if enumerated > budgets["max_snapshot_members"]:
            raise ArtifactQueryError("snapshot member budget exceeded")
        try:
            member, total_read = _read_member(root, path, budgets=budgets, total_read=total_read, started=started)
            members.append(member)
        except ArtifactQueryError as error:
            if str(error) in {"source budget exceeded", "incomplete source"}:
                raise
            findings.append(str(error))
            if len(findings) > budgets["max_findings"]:
                raise ArtifactQueryError("source findings budget exceeded") from error
    if findings:
        raise ArtifactQueryError("incomplete source: " + "; ".join(findings))
    if len({member["id"] for member in members}) != len(members):
        raise ArtifactQueryError("duplicate artifact identity")
    sealed = [{"path": member["relative"], "id": member["id"], "digest": member["digest"]} for member in members]
    digest = _digest_members(sealed)
    snapshot = _Snapshot(secrets.token_urlsafe(32), str(root), tuple(sealed), digest, binding)
    _RETAINED_SNAPSHOTS[snapshot.token] = snapshot
    return snapshot, members


def _validate_retained_snapshot(snapshot: _Snapshot, root: Path, budgets: dict[str, int]) -> list[dict[str, Any]]:
    """Re-read only sealed member paths; never enumerate the root on continuation."""
    members: list[dict[str, Any]] = []
    total_read = 0
    started = time.monotonic()
    for sealed in snapshot.members:
        relative = Path(sealed["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ArtifactQueryError("tampered retained member")
        path = root / relative
        try:
            member, total_read = _read_member(root, path, budgets=budgets, total_read=total_read, started=started)
        except ArtifactQueryError as error:
            raise ArtifactQueryError("retained snapshot member mismatch") from error
        if member["relative"] != sealed["path"] or member["id"] != sealed["id"] or member["digest"] != sealed["digest"]:
            raise ArtifactQueryError("retained snapshot member mismatch")
        members.append(member)
    if _digest_members([{"path": item["path"], "id": item["id"], "digest": item["digest"]} for item in snapshot.members]) != snapshot.digest:
        raise ArtifactQueryError("tampered retained snapshot")
    return members


def _filter_selectors(tree: Any) -> Iterable[str]:
    kind = tree[0]
    if kind == "not":
        yield from _filter_selectors(tree[1])
    elif kind in {"and", "or"}:
        yield from _filter_selectors(tree[1])
        yield from _filter_selectors(tree[2])
    else:
        yield tree[1]


def query_artifacts(root: str | Path, request: dict[str, Any], *, settings: dict[str, int] | None = None) -> dict[str, Any]:
    """Run one read-only query or continue an explicit retained snapshot.

    A continuation sends the exact ``snapshot`` object and ``next_cursor`` from
    a prior page. It revalidates sealed members without re-enumerating root.
    """
    if not isinstance(request, dict):
        raise ArtifactQueryError("request must be an object")
    if set(request) - {"filter", "select", "limit", "cursor", "snapshot", "settings"}:
        raise ArtifactQueryError("unsupported query request field")
    budgets = _load_budgets(settings, request.get("settings"))
    if len(_canonical_bytes(request)) > budgets["max_request_bytes"]:
        raise ArtifactQueryError("request budget exceeded")
    selection = request.get("select", [])
    if not isinstance(selection, list) or len(selection) > budgets["max_selected_fields"]:
        raise ArtifactQueryError("invalid selected fields")
    for selector in selection:
        _validate_selector(selector)
    limit = request.get("limit", budgets["max_page_size"])
    if type(limit) is not int or not 0 < limit <= budgets["max_page_size"]:
        raise ArtifactQueryError("invalid page limit")
    expression = request.get("filter")
    if expression is not None and not isinstance(expression, str):
        raise QueryFilterError("expression must be a string")
    resolved_root = _resolve_root(root)
    binding = _request_binding(request, selection, budgets)
    retained = request.get("snapshot")
    cursor = request.get("cursor")
    if (retained is None) != (cursor is None):
        raise ArtifactQueryError("continuation requires retained snapshot and cursor")
    if retained is None:
        snapshot, members = _capture_snapshot(resolved_root, budgets, binding)
    else:
        snapshot = _snapshot_from_request(retained, resolved_root, binding)
        members = _validate_retained_snapshot(snapshot, resolved_root, budgets)
    tree = None if expression is None else parse_filter(
        expression, max_depth=budgets["max_grammar_depth"], max_tokens=budgets["max_filter_tokens"],
        max_in_members=budgets["max_in_members"],
    )
    if tree is not None:
        for selector in _filter_selectors(tree):
            _validate_selector(selector)
            # Validate every selector against the sealed domain before boolean
            # short-circuiting, including an otherwise unvisited bad array index.
            for member in members:
                _decode_selector(selector, member["fm"], member["sections"])
    matches = [
        member for member in members
        if tree is None or evaluate_filter(tree, lambda selector, item=member: _decode_selector(selector, item["fm"], item["sections"]))
    ]
    matches.sort(key=lambda member: member["id"].encode("utf-8"))
    if cursor is not None:
        decoded = _uncursor(cursor)
        if decoded["snapshot"] != snapshot.token or decoded["binding"] != binding:
            raise ArtifactQueryError("changed or foreign snapshot cursor")
        matches = [member for member in matches if member["id"].encode("utf-8") > decoded["last"].encode("utf-8")]
    page = matches[:limit]
    rows: list[dict[str, Any]] = []
    for member in page:
        row: dict[str, Any] = {"artifact_id": member["id"]}
        for selector in selection:
            value = _decode_selector(selector, member["fm"], member["sections"])
            if value is not MISSING and _has_secret_value(value):
                raise ArtifactQueryError("secret-shaped selected value")
            row[selector] = "missing" if value is MISSING else value
        rows.append(row)
    has_more = len(matches) > len(page)
    coverage = {
        "examined_count": len(members), "matched_count": len(matches), "returned_count": len(rows),
        "complete": True, "incomplete": False,
    }
    return {
        "snapshot": snapshot.public(), "snapshot_reference": snapshot.public()["reference"],
        **coverage, "coverage": coverage, "has_more": has_more,
        "next_cursor": _cursor(snapshot.token, binding, page[-1]["id"]) if has_more else None,
        "results": rows,
        "diagnostics": {"complete": True, "incomplete": False, "findings": []},
    }
