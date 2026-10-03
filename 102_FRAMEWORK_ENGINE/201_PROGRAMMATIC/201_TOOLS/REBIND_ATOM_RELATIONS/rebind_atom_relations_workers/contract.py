"""Strict JSON request parsing for the CA-R-1049 relation-rebinding Doer."""

from __future__ import annotations

import json
import re
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from .models import RebindError, Request


ATOM_ID = re.compile(r"^CA-[CAPRMEDO]-[0-9]{3,}$")
FIELD = re.compile(r"^[a-z][a-z0-9_]*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
TIMESTAMP = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")
KEYS = frozenset({
    "source_path",
    "expected_source_sha256",
    "expected_source_version",
    "updated_at",
    "relation_rewrite_map",
    "relation_removal_map",
})


def load_request(path: str) -> Request:
    """Load exactly one sealed relation-only request without implicit defaults."""
    try:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        payload = json.loads(text)
    except (OSError, json.JSONDecodeError) as error:
        raise RebindError("input-invalid", "--input must contain one JSON object") from error
    if not isinstance(payload, Mapping) or set(payload) != KEYS:
        raise RebindError("input-keys-invalid", "input must contain exactly the documented rebind keys")
    return _request(payload)


def _request(payload: Mapping[str, Any]) -> Request:
    """Validate scalar fields and both exact relation change maps."""
    source = _source_path(payload)
    digest = _string(payload, "expected_source_sha256", SHA256)
    version = _positive_integer(payload, "expected_source_version")
    updated_at = _string(payload, "updated_at", TIMESTAMP)
    rewrites = _rewrite_map(payload["relation_rewrite_map"])
    removals = _removal_map(payload["relation_removal_map"])
    _require_nonempty_change(rewrites, removals)
    _reject_overlaps(rewrites, removals)
    return Request(source, digest, version, updated_at, rewrites, removals)


def _source_path(payload: Mapping[str, Any]) -> str:
    """Require one safe, explicit repository-relative active-carrier path."""
    value = _string(payload, "source_path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.suffix != ".md" or not value.startswith(".caprmedio/"):
        raise RebindError("path-invalid", "source_path must be a safe .caprmedio-relative Markdown path")
    return value


def _string(payload: Mapping[str, Any], name: str, pattern: re.Pattern[str] | None = None) -> str:
    """Read one nonempty, optionally pattern-constrained string."""
    value = payload.get(name)
    if not isinstance(value, str) or not value or value != value.strip() or (pattern and not pattern.fullmatch(value)):
        raise RebindError("input-invalid", f"{name} is invalid")
    return value


def _positive_integer(payload: Mapping[str, Any], name: str) -> int:
    """Read one positive integer without accepting booleans."""
    value = payload.get(name)
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise RebindError("input-invalid", f"{name} must be a positive integer")
    return value


def _rewrite_map(value: Any) -> dict[str, dict[str, str]]:
    """Validate exact old-target to canonical-new-ID replacements."""
    if not isinstance(value, Mapping):
        raise RebindError("relation-map-invalid", "relation_rewrite_map must be an object")
    result: dict[str, dict[str, str]] = {}
    for relation, targets in value.items():
        _relation_name(relation)
        if not isinstance(targets, Mapping) or not targets:
            raise RebindError("relation-map-invalid", "each rewrite relation requires a nonempty object")
        parsed = {str(old): str(new) for old, new in targets.items()}
        if any(not isinstance(old, str) or not _target_text(old) or not isinstance(new, str) or not ATOM_ID.fullmatch(new) for old, new in targets.items()):
            raise RebindError("relation-map-invalid", "rewrite targets must be exact old text and canonical new Atom IDs")
        result[relation] = parsed
    return result


def _removal_map(value: Any) -> dict[str, tuple[str, ...]]:
    """Validate exact target removals without accepting repeated source text."""
    if not isinstance(value, Mapping):
        raise RebindError("relation-map-invalid", "relation_removal_map must be an object")
    result: dict[str, tuple[str, ...]] = {}
    for relation, targets in value.items():
        _relation_name(relation)
        if not isinstance(targets, list) or not targets or any(not isinstance(item, str) or not _target_text(item) for item in targets):
            raise RebindError("relation-map-invalid", "each removal relation requires nonempty target text")
        if len(targets) != len(set(targets)):
            raise RebindError("relation-map-invalid", "a removal target must occur once in its request")
        result[relation] = tuple(targets)
    return result


def _relation_name(value: Any) -> None:
    """Reject relation keys outside the controlled YAML-name grammar."""
    if not isinstance(value, str) or not FIELD.fullmatch(value):
        raise RebindError("relation-map-invalid", "relation names must be simple YAML field names")


def _target_text(value: str) -> bool:
    """Accept only one exact, single-line stored relation target."""
    return bool(value and value == value.strip() and "\n" not in value and "\r" not in value)


def _require_nonempty_change(rewrites: Mapping[str, object], removals: Mapping[str, object]) -> None:
    """Reject a revision-only invocation with no declared relation action."""
    if not rewrites and not removals:
        raise RebindError("relation-map-empty", "at least one exact relation rewrite or removal is required")


def _reject_overlaps(rewrites: Mapping[str, Mapping[str, str]], removals: Mapping[str, tuple[str, ...]]) -> None:
    """Forbid requesting two different actions for one stored relation target."""
    rewrite_targets = {(relation, old) for relation, targets in rewrites.items() for old in targets}
    removal_targets = {(relation, old) for relation, targets in removals.items() for old in targets}
    if rewrite_targets & removal_targets:
        raise RebindError("relation-map-invalid", "one relation target cannot be both rewritten and removed")
