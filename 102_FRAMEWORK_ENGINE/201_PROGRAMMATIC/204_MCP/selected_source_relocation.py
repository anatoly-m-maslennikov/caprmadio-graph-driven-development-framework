"""Closed CA-D-592 derivation for one acceptance-carrier relocation."""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any, Mapping

from selected_routes import SelectedRouteError, canonical_digest, validate_selected_manifest_document


_REF = PurePosixPath(".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/07_delivery/CA-D-592-MCP-DELIVERY--register-exact-acceptance-carrier-relocations.md")
_SHA = "10ce7ffdae76ee2e8d2fe167396529dd01e8091d4a1513a877d5fee9ec89deb8"
_HEADING = "### Accepted carrier relocations"
_DIGEST = re.compile(r"^[0-9a-f]{64}$")
_EXPECTED = {
    "schema_version": 1, "registration_id": "acceptance-carrier-relocations-p1117-20261008",
    "authorization_ref": ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations.md",
    "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
    "input_manifest_sha256": "1381b8c41d59e7f3636ac69e37e365e41b8429469e748e9824e982a7ccdd71a9",
    "input_canonical_manifest_sha256": "2235d03cdb904942c9b26118a867769696fbe3dfc650eebb6c2e8d49b19bbc4e",
}
_ROWS = (
    ("CA-P-1618", 1, ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/29-CA-P-1618-TASK--accept-current-artifact-query-source-frontier.md", ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/29-CA-P-1618-TASK--accept-current-artifact-query-source-frontier.md", "bdf10c928c10c102dc489c8e3e526ffe73e8a33d492f4dabc8b5d0129c453b1f"),
    ("CA-P-1535", 2, ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/15-CA-P-1535-TASK--accept-final-journal-query-source.md", ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/15-CA-P-1535-TASK--accept-final-journal-query-source.md", "6246b46d2961d795e29eeb224f01b14979434d4ad24cf3f4913c490268cf52dc"),
    ("CA-P-1622", 4, ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/10-CA-P-1620-TASK--deliver-release-version-workflow/done/02-CA-P-1622-TASK--review-release-version-source-and-admission.md", ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/10-CA-P-1620-TASK--deliver-release-version-workflow/done/02-CA-P-1622-TASK--review-release-version-source-and-admission.md", "7cd6a839a190add10108bdd5e58700aeae7a89316aa721b2b5340bda865a2739"),
)

class SelectedSourceRelocationError(ValueError): pass

def _safe(root: Path, ref: str) -> Path:
    rel = PurePosixPath(ref)
    if rel.is_absolute() or not rel.parts or any(p in {"", ".", ".."} for p in rel.parts): raise SelectedSourceRelocationError("unsafe registered carrier")
    path = root
    for part in rel.parts:
        path /= part
        if path.is_symlink(): raise SelectedSourceRelocationError("registered carrier has symlinked ancestor")
    if not path.is_file(): raise SelectedSourceRelocationError("registered carrier is unavailable")
    return path

def _object(pairs):
    value = {}
    for key, item in pairs:
        if key in value: raise SelectedSourceRelocationError("duplicate JSON member")
        value[key] = item
    return value

def registered_source_relocation(root: str | Path) -> dict[str, Any]:
    root = Path(root).resolve(strict=True)
    raw = _safe(root, str(_REF)).read_bytes()
    if hashlib.sha256(raw).hexdigest() != _SHA: raise SelectedSourceRelocationError("CA-D-592 bytes are stale")
    match = re.search(rf"(?ms)^{re.escape(_HEADING)}\s*\n\s*```json\s*\n(.*?)\n```\s*$", raw.decode("utf-8"))
    if match is None: raise SelectedSourceRelocationError("CA-D-592 registration is absent")
    value = json.loads(match.group(1), object_pairs_hook=_object)
    if not isinstance(value, Mapping) or set(value) != {*_EXPECTED, "relocations"} or any(value[k] != v for k, v in _EXPECTED.items()): raise SelectedSourceRelocationError("CA-D-592 registration is not closed")
    rows = value["relocations"]
    if type(value["schema_version"]) is not int or not isinstance(rows, list) or len(rows) != 3: raise SelectedSourceRelocationError("CA-D-592 relocation cardinality is invalid")
    expected = [{"atom_id": a, "version": v, "prior_source_path": p, "current_source_path": c, "digest": d} for a,v,p,c,d in _ROWS]
    if rows != expected: raise SelectedSourceRelocationError("CA-D-592 relocation rows differ")
    return copy.deepcopy(dict(value))

def derive_registered_source_relocation(root: str | Path):
    root = Path(root).resolve(strict=True); registration = registered_source_relocation(root)
    raw = _safe(root, registration["input_manifest_ref"]).read_bytes()
    if hashlib.sha256(raw).hexdigest() != registration["input_manifest_sha256"]: raise SelectedSourceRelocationError("registered input bytes differ")
    manifest = json.loads(raw, object_pairs_hook=_object)
    if manifest.get("canonical_manifest_sha256") != registration["input_canonical_manifest_sha256"]: raise SelectedSourceRelocationError("registered input canonical digest differs")
    rows = registration["relocations"]
    for row in rows:
        source = _safe(root, row["current_source_path"]); body = source.read_bytes()
        if hashlib.sha256(body).hexdigest() != row["digest"]: raise SelectedSourceRelocationError("registered current carrier digest is stale")
        text = body.decode("utf-8")
        if not re.search(rf'(?m)^atom_id:\s*["\']?{re.escape(row["atom_id"])}', text) or not re.search(rf'(?m)^version:\s*["\']?{row["version"]}(?:\s|$)', text): raise SelectedSourceRelocationError("registered current carrier metadata differs")
    candidate = copy.deepcopy(manifest); count = {row["prior_source_path"]: 0 for row in rows}; mapping = {row["prior_source_path"]: row["current_source_path"] for row in rows}
    def replace(value):
        if isinstance(value, dict): return {k: replace(v) for k,v in value.items()}
        if isinstance(value, list): return [replace(v) for v in value]
        if isinstance(value, str) and value in mapping: count[value] += 1; return mapping[value]
        return value
    candidate = replace(candidate)
    if any(value != 1 for value in count.values()): raise SelectedSourceRelocationError("registered prior path occurrence differs")
    candidate.pop("canonical_manifest_sha256"); candidate["canonical_manifest_sha256"] = canonical_digest(candidate)
    try: validate_selected_manifest_document(root, candidate)
    except (OSError, TypeError, ValueError, SelectedRouteError) as error: raise SelectedSourceRelocationError("relocation candidate is not admitted") from error
    payload = (json.dumps(candidate, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    return dict(manifest), candidate, payload, root / registration["input_manifest_ref"]
