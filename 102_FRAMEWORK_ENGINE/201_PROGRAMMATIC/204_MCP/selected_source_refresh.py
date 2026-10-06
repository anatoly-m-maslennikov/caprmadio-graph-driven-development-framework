"""Private CA-D-588 derivation for the one registered selected-source refresh."""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any, Mapping

from selected_routes import SelectedRouteError, canonical_digest, validate_selected_manifest_document


_REGISTRATION_REF = PurePosixPath(
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "204_FEATURE_MCP/07_delivery/"
    "CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh.md"
)
_REGISTRATION_HEADING = "### Accepted source revision"
_DIGEST = re.compile(r"^[0-9a-f]{64}$")
_PIN_FIELDS = frozenset({"atom_id", "version", "source_path", "digest"})
_EXPECTED = {
    "schema_version": 1,
    "registration_id": "prepared-successors-o128-v4-20261006",
    "authorization_ref": ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations.md",
    "repair_task_id": "CA-P-1799",
    "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
    "input_manifest_sha256": "5ca6c9907a4dffbe84319b7d4e391c6242e1969cfea5902845e50f0bd8ae3012",
    "input_canonical_manifest_sha256": "c0edfd130a32386258397da81796d9efab6c1154b17666419edc988d76efc9ba",
    "routes": ["create_atom", "update_atom", "replace_atom", "change_atom_status"],
    "pin_occurrences": 8,
    "prior_pin": {"atom_id": "CA-O-128", "version": 3, "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md", "digest": "b5d052e97bae6ada98849380199e5c67cbf090900beb33ca202f7872d56301e8"},
    "prior_archive_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes@3.md",
    "current_pin": {"atom_id": "CA-O-128", "version": 4, "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md", "digest": "ea36b940a171676977507d366daca9400825e8685018d9c201c15fc5b97eea1c"},
    "requirement_pin": {"atom_id": "CA-R-1041", "version": 8, "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/REPLACE_ATOM/04_requirement/CA-R-1041-TOOLS--coordinate-atom-replacement-intent.md", "digest": "45a87fc9dbb416111b66b22875c844abcce0cd362f0a421190406897413bd9bc"},
}


class RegisteredSourceRefreshError(ValueError):
    """The closed registration or its exact successor is unavailable."""


def _project_root(root: str | Path | None) -> Path:
    try:
        value = Path(root) if root is not None else Path(__file__).resolve().parents[3]
        value = value.resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise RegisteredSourceRefreshError("Project root is unavailable") from error
    if value.is_symlink() or not value.is_dir():
        raise RegisteredSourceRefreshError("Project root is unavailable")
    return value


def _safe_regular(root: Path, reference: str | PurePosixPath, *, label: str) -> Path:
    relative = PurePosixPath(reference)
    if relative.is_absolute() or not relative.parts or any(part in {"", ".", ".."} for part in relative.parts):
        raise RegisteredSourceRefreshError(f"{label} is not a safe Project-relative carrier")
    cursor = root
    try:
        for part in relative.parts:
            cursor /= part
            if cursor.is_symlink():
                raise RegisteredSourceRefreshError(f"{label} has a symlinked ancestor")
        if not cursor.is_file():
            raise RegisteredSourceRefreshError(f"{label} is unavailable")
    except OSError as error:
        raise RegisteredSourceRefreshError(f"{label} is unavailable") from error
    return cursor


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise RegisteredSourceRefreshError("registration JSON contains a duplicate key")
        value[key] = item
    return value


def _validate_registration(value: Any) -> dict[str, Any]:
    if not isinstance(value, Mapping) or dict(value) != _EXPECTED:
        raise RegisteredSourceRefreshError("registration is not the one closed CA-D-588 authority revision")
    # Keep these checks explicit so future edits cannot accidentally make bool an integer.
    if type(value["schema_version"]) is not int or type(value["pin_occurrences"]) is not int:
        raise RegisteredSourceRefreshError("registration schema version and occurrence count must be strict integers")
    for field in ("prior_pin", "current_pin", "requirement_pin"):
        pin = value[field]
        if (not isinstance(pin, Mapping) or set(pin) != _PIN_FIELDS or type(pin["version"]) is not int
                or not isinstance(pin["source_path"], str) or _DIGEST.fullmatch(pin["digest"]) is None):
            raise RegisteredSourceRefreshError("registration pin shape is invalid")
    return copy.deepcopy(dict(value))


def registered_source_refresh(root: str | Path | None = None) -> dict[str, Any]:
    """Read and close the sole D588 JSON registration; callers cannot supply one."""
    project_root = _project_root(root)
    source = _safe_regular(project_root, _REGISTRATION_REF, label="source-refresh registration")
    try:
        text = source.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise RegisteredSourceRefreshError("source-refresh registration is unreadable") from error
    match = re.search(rf"(?ms)^{re.escape(_REGISTRATION_HEADING)}\s*\n\s*```json\s*\n(.*?)\n```\s*$", text)
    if match is None:
        raise RegisteredSourceRefreshError("source-refresh registration has no closed JSON object")
    try:
        value = json.loads(match.group(1), object_pairs_hook=_unique_object)
    except (json.JSONDecodeError, RegisteredSourceRefreshError) as error:
        raise RegisteredSourceRefreshError("source-refresh registration JSON is invalid") from error
    return _validate_registration(value)


def _validate_current_pin(root: Path, pin: Mapping[str, Any], *, label: str) -> None:
    path = _safe_regular(root, str(pin["source_path"]), label=label)
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise RegisteredSourceRefreshError(f"{label} is unreadable") from error
    if hashlib.sha256(raw).hexdigest() != pin["digest"]:
        raise RegisteredSourceRefreshError(f"{label} digest is stale")
    atom = re.search(r"(?m)^atom_id:\s*[\"']?([^\n\"']+)", text)
    version = re.search(r"(?m)^version:\s*[\"']?([^\n\"']+)", text)
    if atom is None or version is None or atom.group(1).strip() != pin["atom_id"] or version.group(1).strip() != str(pin["version"]):
        raise RegisteredSourceRefreshError(f"{label} metadata differs from its registered pin")


def _replace_pins(value: Any, *, prior: Mapping[str, Any], current: Mapping[str, Any], allowed_route: bool, count: list[int]) -> Any:
    if isinstance(value, Mapping):
        if dict(value) == dict(prior):
            if not allowed_route:
                raise RegisteredSourceRefreshError("prior pin occurs outside the registered routes")
            count[0] += 1
            return copy.deepcopy(dict(current))
        return {key: _replace_pins(item, prior=prior, current=current, allowed_route=allowed_route, count=count)
                for key, item in value.items()}
    if isinstance(value, list):
        return [_replace_pins(item, prior=prior, current=current, allowed_route=allowed_route, count=count) for item in value]
    return copy.deepcopy(value)


def derive_registered_source_successor(manifest: Mapping[str, Any], registration: Mapping[str, Any]) -> dict[str, Any]:
    """Purely derive the registered eight-pin successor without an effect."""
    registered = _validate_registration(registration)
    if not isinstance(manifest, Mapping) or not isinstance(manifest.get("routes"), list):
        raise RegisteredSourceRefreshError("refresh input has no route collection")
    candidate = copy.deepcopy(dict(manifest))
    route_names = registered["routes"]
    routes = candidate["routes"]
    if [row.get("route") if isinstance(row, Mapping) else None for row in routes].count(None):
        raise RegisteredSourceRefreshError("refresh input route collection is malformed")
    if len({row["route"] for row in routes}) != len(routes):
        raise RegisteredSourceRefreshError("refresh input route registry is duplicate")
    if any(name not in {row["route"] for row in routes} for name in route_names):
        raise RegisteredSourceRefreshError("registered refresh route is unavailable")
    count = [0]
    candidate["routes"] = [
        _replace_pins(row, prior=registered["prior_pin"], current=registered["current_pin"],
                      allowed_route=row["route"] in route_names, count=count)
        for row in routes
    ]
    if count[0] != registered["pin_occurrences"]:
        raise RegisteredSourceRefreshError("registered prior pin occurrence count differs")
    freshness = candidate.get("source_freshness")
    if not isinstance(freshness, Mapping) or "selected_binding_digest" not in freshness:
        raise RegisteredSourceRefreshError("refresh input source freshness is malformed")
    candidate["source_freshness"] = dict(freshness)
    candidate["source_freshness"]["selected_binding_digest"] = canonical_digest(candidate["routes"])
    candidate.pop("canonical_manifest_sha256", None)
    candidate["canonical_manifest_sha256"] = canonical_digest(candidate)
    return candidate


def derive_registered_source_refresh(root: str | Path) -> tuple[dict[str, Any], dict[str, Any], bytes, Path]:
    """Open the exact historical input, validate active carriers, and derive its successor."""
    project_root = _project_root(root)
    registration = registered_source_refresh(project_root)
    input_path = _safe_regular(project_root, registration["input_manifest_ref"], label="registered input manifest")
    raw = input_path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != registration["input_manifest_sha256"]:
        raise RegisteredSourceRefreshError("registered input manifest bytes differ")
    try:
        manifest = json.loads(raw, object_pairs_hook=_unique_object)
    except (json.JSONDecodeError, RegisteredSourceRefreshError) as error:
        raise RegisteredSourceRefreshError("registered input manifest is invalid") from error
    if not isinstance(manifest, Mapping) or manifest.get("canonical_manifest_sha256") != registration["input_canonical_manifest_sha256"]:
        raise RegisteredSourceRefreshError("registered input manifest canonical digest differs")
    archive = _safe_regular(project_root, registration["prior_archive_path"], label="registered prior archive")
    if hashlib.sha256(archive.read_bytes()).hexdigest() != registration["prior_pin"]["digest"]:
        raise RegisteredSourceRefreshError("registered prior archive bytes differ")
    _validate_current_pin(project_root, registration["current_pin"], label="registered current Action source")
    _validate_current_pin(project_root, registration["requirement_pin"], label="registered current Requirement source")
    candidate = derive_registered_source_successor(manifest, registration)
    try:
        validate_selected_manifest_document(project_root, candidate)
    except (OSError, TypeError, ValueError, SelectedRouteError) as error:
        raise RegisteredSourceRefreshError("registered successor does not satisfy the complete selected-manifest contract") from error
    payload = (json.dumps(candidate, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    return dict(manifest), candidate, payload, input_path


__all__ = [
    "RegisteredSourceRefreshError", "registered_source_refresh", "derive_registered_source_successor",
    "derive_registered_source_refresh",
]
