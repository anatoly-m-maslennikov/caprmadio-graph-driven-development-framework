"""Strict JSON input contract for the CA-R-1048 identity-migration Doer."""

from __future__ import annotations

import json
import re
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from .models import MigrationError, Request


ATOM_ID = re.compile(r"^CA-([CAPRMEDO])-([0-9]{3,})$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
TOKEN = re.compile(r"^[A-Z][A-Z0-9_]*$")
SUMMARY = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
FIELD = re.compile(r"^[a-z][a-z0-9_]*$")
CLASSIFICATIONS = frozenset({"identityless_legacy", "legacy_identity", "duplicate_id_repair"})
DERIVED_FIELDS = frozenset({"atom_id", "tier"})
KEYS = frozenset({
    "source_path", "destination_path", "expected_source_sha256", "expected_source_version",
    "approved_old_identity", "new_atom_id", "classification", "filename_tokens",
    "frontmatter_removals", "frontmatter_updates", "relation_rewrite_map", "relation_removal_map",
})


def load_request(path: str) -> Request:
    """Load one JSON object without accepting an implicit default plan."""
    try:
        raw = Path(path).read_text(encoding="utf-8") if path != "-" else sys.stdin.read()
        payload = json.loads(raw)
    except (OSError, json.JSONDecodeError) as error:
        raise MigrationError("input-invalid", "--input must contain one valid JSON object") from error
    if not isinstance(payload, Mapping):
        raise MigrationError("input-invalid", "--input must contain one JSON object")
    if set(payload) != KEYS:
        raise MigrationError("input-keys-invalid", "input must contain exactly the documented identity-migration keys")
    return _request(payload)


def _string(payload: Mapping[str, Any], field: str, pattern: re.Pattern[str] | None = None) -> str:
    value = payload.get(field)
    if not isinstance(value, str) or not value or (pattern and not pattern.fullmatch(value)):
        raise MigrationError("input-invalid", f"{field} is invalid")
    return value


def _paths(payload: Mapping[str, Any]) -> tuple[str, str]:
    """Accept only repository-relative control-plane carrier paths."""
    values = tuple(_string(payload, field) for field in ("source_path", "destination_path"))
    for value in values:
        path = Path(value)
        if path.is_absolute() or ".." in path.parts or not value.startswith(".caprmedio/"):
            raise MigrationError("path-invalid", "source_path and destination_path must be safe .caprmedio-relative paths")
    return values


def _filename_tokens(value: Any, atom_id: str) -> tuple[str, tuple[str, ...], str]:
    if not isinstance(value, Mapping) or set(value) != {"source_filename", "destination_prefix", "summary"}:
        raise MigrationError("filename-tokens-invalid", "filename_tokens must declare source_filename, destination_prefix, and summary")
    source = _string(value, "source_filename")
    prefix = value.get("destination_prefix")
    if not isinstance(prefix, list) or len(prefix) < 4 or any(not isinstance(item, str) for item in prefix):
        raise MigrationError("filename-tokens-invalid", "destination_prefix must contain at least four filename tokens")
    summary = _string(value, "summary", SUMMARY)
    expected = atom_id.split("-")
    if prefix[:3] != expected or any(not TOKEN.fullmatch(item) for item in prefix[3:]):
        raise MigrationError("filename-tokens-invalid", "destination_prefix must begin with the exact new_atom_id tokens")
    return source, tuple(prefix), summary


def _fields(value: Any, *, removals: bool) -> tuple[str, ...] | dict[str, Any]:
    if removals:
        if not isinstance(value, list) or any(not isinstance(item, str) or not FIELD.fullmatch(item) for item in value):
            raise MigrationError("frontmatter-invalid", "frontmatter_removals must be an array of simple field names")
        if len(value) != len(set(value)):
            raise MigrationError("frontmatter-invalid", "frontmatter_removals must not repeat a field")
        return tuple(value)
    if not isinstance(value, Mapping) or any(not isinstance(key, str) or not FIELD.fullmatch(key) for key in value):
        raise MigrationError("frontmatter-invalid", "frontmatter_updates must be an object with simple field names")
    return dict(value)


def _relation_maps(payload: Mapping[str, Any]) -> tuple[dict[str, dict[str, str]], dict[str, tuple[str, ...]]]:
    rewrites, removals = payload["relation_rewrite_map"], payload["relation_removal_map"]
    if not isinstance(rewrites, Mapping) or not isinstance(removals, Mapping):
        raise MigrationError("relation-map-invalid", "relation maps must be objects")
    result_rewrites: dict[str, dict[str, str]] = {}
    for relation, targets in rewrites.items():
        if not isinstance(relation, str) or not FIELD.fullmatch(relation) or not isinstance(targets, Mapping):
            raise MigrationError("relation-map-invalid", "relation rewrite map is invalid")
        if any(not isinstance(old, str) or not isinstance(new, str) for old, new in targets.items()):
            raise MigrationError("relation-map-invalid", "relation rewrite targets must be strings")
        parsed = dict(targets)
        if not parsed or any(not old or not ATOM_ID.fullmatch(new) for old, new in parsed.items()):
            raise MigrationError("relation-map-invalid", "every rewritten relation target must be one exact canonical Atom ID")
        result_rewrites[relation] = parsed
    result_removals: dict[str, tuple[str, ...]] = {}
    for relation, targets in removals.items():
        if not isinstance(relation, str) or not FIELD.fullmatch(relation) or not isinstance(targets, list):
            raise MigrationError("relation-map-invalid", "relation removal map is invalid")
        if not targets or any(not isinstance(target, str) or not target for target in targets) or len(targets) != len(set(targets)):
            raise MigrationError("relation-map-invalid", "every removed relation target must be unique and non-empty")
        result_removals[relation] = tuple(targets)
    overlap = {(relation, target) for relation, targets in result_rewrites.items() for target in targets}
    if overlap & {(relation, target) for relation, targets in result_removals.items() for target in targets}:
        raise MigrationError("relation-map-invalid", "one relation target cannot be both rewritten and removed")
    return result_rewrites, result_removals


def _request(payload: Mapping[str, Any]) -> Request:
    source_path, destination_path = _paths(payload)
    atom_id = _string(payload, "new_atom_id", ATOM_ID)
    classification = _string(payload, "classification")
    if classification not in CLASSIFICATIONS:
        raise MigrationError("classification-invalid", "classification must be identityless_legacy, legacy_identity, or duplicate_id_repair")
    old = payload.get("approved_old_identity")
    if classification == "identityless_legacy":
        if old is not None:
            raise MigrationError("old-identity-invalid", "identityless_legacy requires approved_old_identity: null")
    elif not isinstance(old, str) or not old:
        raise MigrationError("old-identity-invalid", "a non-identityless migration requires approved_old_identity")
    source_filename, prefix, summary = _filename_tokens(payload["filename_tokens"], atom_id)
    updates = _fields(payload["frontmatter_updates"], removals=False)
    removals = _fields(payload["frontmatter_removals"], removals=True)
    assert isinstance(updates, dict) and isinstance(removals, tuple)
    if DERIVED_FIELDS & set(updates):
        raise MigrationError("frontmatter-derived-update-invalid", "atom_id and tier are derived from the destination filename and must not be updated")
    if set(updates) & set(removals):
        raise MigrationError("frontmatter-change-conflict", "one frontmatter field cannot be both updated and removed")
    rewrites, relation_removals = _relation_maps(payload)
    return Request(
        source_path, destination_path, _string(payload, "expected_source_sha256", SHA256),
        _integer(payload, "expected_source_version"), old, atom_id, classification, source_filename,
        prefix, summary, removals, updates, rewrites, relation_removals,
    )


def _integer(payload: Mapping[str, Any], field: str) -> int:
    value = payload.get(field)
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise MigrationError("input-invalid", f"{field} must be a positive integer")
    return value
