"""Opt-in publisher for the source-admitted sixteen-route binding projection.

This module is deliberately not an MCP route and does not execute a Release.  A
caller gets a read-only plan unless it explicitly requests ``execute``.
"""
from __future__ import annotations

import copy
import hashlib
import os
from pathlib import Path
import tempfile
from typing import Any, Mapping

from selected_routes import (
    SELECTED_ROUTE_NAMES,
    SelectedRouteError,
    canonical_digest,
    canonical_json,
    load_selected_manifest,
    selected_manifest_ref,
)


class ReleaseManifestPublishError(ValueError):
    """The bounded additive projection cannot be planned or published."""


def _root(value: str | Path) -> Path:
    try:
        result = Path(value).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise ReleaseManifestPublishError("project root is unavailable") from error
    if not result.is_dir():
        raise ReleaseManifestPublishError("project root is unavailable")
    return result


def _derive(project_root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """Use the Release graph owner's closed source-derived API only."""
    from release_source_admission import derive_release_graph_admission
    try:
        value = derive_release_graph_admission(project_root)
    except (OSError, ValueError, TypeError) as error:
        raise ReleaseManifestPublishError(f"Release graph admission is not current: {error}") from error
    if (not isinstance(value, tuple) or len(value) != 2
            or not isinstance(value[0], Mapping) or not isinstance(value[1], Mapping)):
        raise ReleaseManifestPublishError("accepted Release graph admission returned an invalid contract")
    route, admission = (copy.deepcopy(dict(item)) for item in value)
    if route.get("route") != "release_version" or admission.get("route") != "release_version":
        raise ReleaseManifestPublishError("accepted Release graph admission is not release_version")
    return route, admission


def _candidate(project_root: Path) -> tuple[dict[str, Any], dict[str, Any], bytes, Path]:
    """Validate current15, then construct—not publish—its exact successor."""
    try:
        current = load_selected_manifest(project_root)
    except (OSError, ValueError, SelectedRouteError) as error:
        raise ReleaseManifestPublishError(f"current selected manifest is unavailable: {error}") from error
    if tuple(row["route"] for row in current["routes"]) != SELECTED_ROUTE_NAMES:
        raise ReleaseManifestPublishError("publication requires the current exact fifteen-route manifest")
    if "release_source_admissions" in current:
        raise ReleaseManifestPublishError("publication requires a manifest without Release admission")
    route, admission = _derive(project_root)
    candidate = copy.deepcopy(current)
    candidate.pop("manifest_ref", None)
    candidate["routes"].append(route)
    candidate["release_source_admissions"] = [admission]
    candidate["source_freshness"]["selected_binding_digest"] = canonical_digest(candidate["routes"])
    candidate.pop("canonical_manifest_sha256", None)
    candidate["canonical_manifest_sha256"] = canonical_digest(candidate)
    path = project_root / selected_manifest_ref(project_root)
    payload = (canonical_json(candidate) + "\n").encode("utf-8")
    return current, candidate, payload, path


def _plan(project_root: Path) -> tuple[dict[str, Any], bytes, Path]:
    current, candidate, payload, path = _candidate(project_root)
    try:
        observed = path.read_bytes()
    except OSError as error:
        raise ReleaseManifestPublishError("current selected manifest bytes are unavailable") from error
    return {
        "manifest_ref": path.relative_to(project_root).as_posix(),
        "observed_input_sha256": hashlib.sha256(observed).hexdigest(),
        "current_route_names": [row["route"] for row in current["routes"]],
        "candidate_route_names": [row["route"] for row in candidate["routes"]],
        "candidate_canonical_manifest_sha256": candidate["canonical_manifest_sha256"],
        "added_route": "release_version",
        "added_admission_route": candidate["release_source_admissions"][0]["route"],
        "candidate_byte_count": len(payload),
    }, observed, path


def _refresh_admission_structure_matches(old: Any, current: Any) -> bool:
    """Compare one stale admission while allowing only pin revision changes."""
    if isinstance(old, Mapping) and isinstance(current, Mapping):
        if set(old) != set(current):
            return False
        is_pin = set(old) == {"atom_id", "version", "source_path", "digest"}
        for key in old:
            if is_pin and key in {"version", "digest"}:
                continue
            if not _refresh_admission_structure_matches(old[key], current[key]):
                return False
        return True
    if isinstance(old, list) and isinstance(current, list):
        return len(old) == len(current) and all(
            _refresh_admission_structure_matches(left, right) for left, right in zip(old, current, strict=True)
        )
    return type(old) is type(current) and old == current


def _refresh_candidate(
    project_root: Path, *, require_drift: bool = True,
) -> tuple[dict[str, Any], dict[str, Any], bytes, Path, dict[str, Any]]:
    """Construct the one guarded sixteen-route refresh candidate.

    D588 is deliberately not a second refresh protocol: its one closed raw
    historical input is admitted only when the normal stale-Release-admission
    reader refuses it.  Both successors then use the identical opaque context,
    intent, write, readback, recording and recovery boundaries below.
    """
    try:
        from selected_routes import load_release_manifest_refresh_base
        current = load_release_manifest_refresh_base(project_root)
    except (ImportError, OSError, TypeError, ValueError, RuntimeError) as normal_error:
        try:
            from selected_source_refresh import derive_registered_source_refresh
            current, candidate, payload, path = derive_registered_source_refresh(project_root)
        except (ImportError, OSError, TypeError, ValueError, RuntimeError):
            try:
                from selected_source_relocation import derive_registered_source_relocation
                current, candidate, payload, path = derive_registered_source_relocation(project_root)
            except (ImportError, OSError, TypeError, ValueError, RuntimeError) as relocation_error:
                raise ReleaseManifestPublishError(
                    f"refresh input manifest is unavailable: {normal_error}"
                ) from relocation_error
        admissions = candidate.get("release_source_admissions") if isinstance(candidate, Mapping) else None
        if not isinstance(admissions, list) or len(admissions) != 1 or not isinstance(admissions[0], Mapping):
            raise ReleaseManifestPublishError("registered refresh candidate has no current Release admission")
        return current, candidate, payload, path, copy.deepcopy(dict(admissions[0]))
    if not isinstance(current, Mapping):
        raise ReleaseManifestPublishError("refresh input manifest returned an invalid contract")
    current = copy.deepcopy(dict(current))
    expected_names = [*SELECTED_ROUTE_NAMES, "release_version"]
    routes = current.get("routes")
    if (not isinstance(routes, list)
            or [row.get("route") for row in routes if isinstance(row, Mapping)] != expected_names
            or len(routes) != len(expected_names)):
        raise ReleaseManifestPublishError("refresh requires the exact admitted sixteen-route manifest")
    admissions = current.get("release_source_admissions")
    if not isinstance(admissions, list) or len(admissions) != 1 or not isinstance(admissions[0], Mapping):
        raise ReleaseManifestPublishError("refresh requires exactly one existing Release admission")
    release_route = routes[-1]
    old_admission = admissions[0]
    route, admission = _derive(project_root)
    if release_route != route:
        raise ReleaseManifestPublishError("refresh cannot replace the current Release route")
    if not _refresh_admission_structure_matches(old_admission, admission):
        raise ReleaseManifestPublishError("refresh Release admission identities or structure differ from current D572")
    if require_drift and old_admission == admission:
        raise ReleaseManifestPublishError("refresh requires stale Release admission input")
    candidate = copy.deepcopy(current)
    candidate.pop("manifest_ref", None)
    candidate["release_source_admissions"] = [copy.deepcopy(admission)]
    candidate["source_freshness"]["selected_binding_digest"] = canonical_digest(candidate["routes"])
    candidate.pop("canonical_manifest_sha256", None)
    candidate["canonical_manifest_sha256"] = canonical_digest(candidate)
    path = project_root / selected_manifest_ref(project_root)
    payload = (canonical_json(candidate) + "\n").encode("utf-8")
    return current, candidate, payload, path, admission


def _refresh_parts(
    project_root: Path, *, require_drift: bool = True,
) -> tuple[dict[str, Any], bytes, dict[str, Any], bytes, Path, dict[str, Any], dict[str, Any]]:
    current, candidate, payload, path, admission = _refresh_candidate(project_root, require_drift=require_drift)
    try:
        observed = path.read_bytes()
    except OSError as error:
        raise ReleaseManifestPublishError("current selected manifest bytes are unavailable") from error
    plan = {
        "publication_operation": "refresh",
        "manifest_ref": path.relative_to(project_root).as_posix(),
        "observed_input_sha256": hashlib.sha256(observed).hexdigest(),
        "current_route_names": [row["route"] for row in current["routes"]],
        "candidate_route_names": [row["route"] for row in candidate["routes"]],
        "candidate_canonical_manifest_sha256": candidate["canonical_manifest_sha256"],
        "added_route": "release_version",
        "added_admission_route": "release_version",
        "candidate_byte_count": len(payload),
    }
    return plan, observed, current, payload, path, admission, candidate


def plan_release_manifest_publish(project_root: str | Path) -> dict[str, Any]:
    """Return a non-writing plan for the one additive Release projection."""
    root = _root(project_root)
    plan, _, _ = _plan(root)
    return {"mode": "plan", **plan}


def plan_release_manifest_refresh(project_root: str | Path) -> dict[str, Any]:
    """Return a non-writing plan for one stale Release-admission refresh."""
    root = _root(project_root)
    plan, _, _, _, _, _, _ = _refresh_parts(root)
    return {"mode": "plan", **plan}


def _atomic_write(path: Path, payload: bytes) -> None:
    if path.is_symlink() or not path.parent.is_dir():
        raise ReleaseManifestPublishError("selected manifest carrier is unavailable")
    try:
        descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except OSError as error:
        raise ReleaseManifestPublishError("could not atomically publish selected manifest") from error
    finally:
        if "temporary" in locals():
            try:
                Path(temporary).unlink(missing_ok=True)
            except OSError:
                pass


def publish_release_manifest(
    project_root: str | Path, *, execute: bool = False, authorization: Any = None,
) -> dict[str, Any]:
    """Plan by default; publish only with ``execute=True`` and verify exact bytes."""
    if type(execute) is not bool:
        raise ReleaseManifestPublishError("execute must be a boolean")
    root = _root(project_root)
    plan, observed, path = _plan(root)
    _, candidate, payload, _ = _candidate(root)
    if not execute:
        return {"mode": "plan", **plan}
    try:
        from release_manifest_authorization import PublicationAuthorizationContext, validate_publication_context
        from release_manifest_lifecycle import ReleaseManifestLifecycle
    except ImportError as error:
        raise ReleaseManifestPublishError("trusted Release manifest lifecycle is unavailable") from error
    if not isinstance(authorization, PublicationAuthorizationContext):
        raise ReleaseManifestPublishError("execute requires a trusted host-created publication context")
    try:
        sealed_plan = {"mode": "plan", **plan}
        context = validate_publication_context(authorization, root, sealed_plan)
        lifecycle = ReleaseManifestLifecycle(root, context)
        if lifecycle.authorize_release_manifest_publication(plan, context) is not True:
            raise ReleaseManifestPublishError("trusted publication context was refused")
    except (TypeError, ValueError) as error:
        raise ReleaseManifestPublishError(f"trusted publication context is invalid: {error}") from error
    if path.read_bytes() != observed:
        raise ReleaseManifestPublishError("selected manifest input changed after authorization")
    # Re-derive all source-pinned input after authorization, before the one write.
    current_after, candidate_after, payload_after, _ = _candidate(root)
    if (current_after["routes"] != candidate["routes"][:-1]
            or candidate_after != candidate or payload_after != payload):
        raise ReleaseManifestPublishError("source-derived successor changed after authorization")
    try:
        with lifecycle.release_manifest_publication_lock(plan):
            pending_event_id = lifecycle.prepare_release_manifest_publication(plan, payload)
            if not isinstance(pending_event_id, str) or not pending_event_id:
                raise ReleaseManifestPublishError("trusted lifecycle did not seal a publication intent")
            # Sealing intent is an observable boundary.  Do not overwrite a manifest
            # or source frontier changed by another authorized context meanwhile.
            validate_publication_context(context, root, sealed_plan, manifest_state="input")
            if path.read_bytes() != observed:
                raise ReleaseManifestPublishError("selected manifest input changed after intent sealing")
            current_final, candidate_final, payload_final, _ = _candidate(root)
            if (current_final["routes"] != candidate["routes"][:-1]
                    or candidate_final != candidate or payload_final != payload):
                raise ReleaseManifestPublishError("source-derived successor changed after intent sealing")
            _atomic_write(path, payload)
    except (OSError, RuntimeError, ValueError, TypeError) as error:
        pending_event_id = locals().get("pending_event_id")
        result = {"mode": "execute", "published": False,
                  "disposition": "pending_publication" if isinstance(pending_event_id, str) and pending_event_id else "blocked",
                  "publication_requirement": str(error), **plan}
        if isinstance(pending_event_id, str) and pending_event_id:
            result["pending_event_id"] = pending_event_id
        return result
    try:
        published = path.read_bytes()
        if published != payload:
            raise ReleaseManifestPublishError("published manifest bytes differ from the sealed candidate")
        loaded = load_selected_manifest(root)
    except (OSError, ValueError, SelectedRouteError) as error:
        return {"mode": "execute", "published": True, "disposition": "readback_required",
                "pending_event_id": pending_event_id, "readback_requirement": str(error), **plan}
    names = [row["route"] for row in loaded["routes"]]
    if names != [*SELECTED_ROUTE_NAMES, "release_version"]:
        return {"mode": "execute", "published": True, "disposition": "readback_required",
                "pending_event_id": pending_event_id,
                "readback_requirement": "published manifest does not discover the additive Release route", **plan}
    try:
        validate_publication_context(context, root, sealed_plan, manifest_state="candidate")
    except (TypeError, ValueError) as error:
        return {"mode": "execute", "published": True, "disposition": "readback_required",
                "pending_event_id": pending_event_id, "readback_requirement": str(error), **plan}
    evidence = {"mode": "execute", "published": True, "published_route_names": names, **plan}
    try:
        receipt = lifecycle.record_release_manifest_publication(dict(evidence))
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        return {**evidence, "disposition": "recording_required", "pending_event_id": pending_event_id,
                "recording_requirement": str(error)}
    if (not isinstance(receipt, Mapping) or set(receipt) != {"recording_ref", "candidate_canonical_manifest_sha256"}
            or not isinstance(receipt["recording_ref"], str) or not receipt["recording_ref"]
            or receipt["candidate_canonical_manifest_sha256"] != plan["candidate_canonical_manifest_sha256"]):
        return {**evidence, "disposition": "recording_required", "pending_event_id": pending_event_id,
                "recording_requirement": "trusted internal lifecycle recording is incomplete"}
    return {**evidence, "disposition": "published", "recording_ref": receipt["recording_ref"]}


def refresh_release_manifest(
    project_root: str | Path, *, execute: bool = False, authorization: Any = None,
) -> dict[str, Any]:
    """Plan by default; refresh only the stale Release admission when authorized."""
    if type(execute) is not bool:
        raise ReleaseManifestPublishError("execute must be a boolean")
    root = _root(project_root)
    plan, observed, current, payload, path, _, candidate = _refresh_parts(root)
    if not execute:
        return {"mode": "plan", **plan}
    try:
        from release_manifest_authorization import PublicationAuthorizationContext, validate_refresh_context
        from release_manifest_lifecycle import ReleaseManifestLifecycle
    except ImportError as error:
        raise ReleaseManifestPublishError("trusted Release manifest lifecycle is unavailable") from error
    if not isinstance(authorization, PublicationAuthorizationContext):
        raise ReleaseManifestPublishError("execute requires a trusted host-created refresh context")
    try:
        sealed_plan = {"mode": "plan", **plan}
        context = validate_refresh_context(authorization, root, sealed_plan)
        lifecycle = ReleaseManifestLifecycle(root, context)
        if lifecycle.authorize_release_manifest_publication(plan, context) is not True:
            raise ReleaseManifestPublishError("trusted refresh context was refused")
    except (TypeError, ValueError) as error:
        raise ReleaseManifestPublishError(f"trusted refresh context is invalid: {error}") from error
    if path.read_bytes() != observed:
        raise ReleaseManifestPublishError("selected manifest input changed after refresh authorization")
    current_after_plan, candidate_after_plan, payload_after_plan, _, _ = _refresh_candidate(root)
    if (current_after_plan != current
            or candidate_after_plan != candidate or payload_after_plan != payload):
        raise ReleaseManifestPublishError("source-derived refresh successor changed after authorization")
    try:
        with lifecycle.release_manifest_publication_lock(plan):
            pending_event_id = lifecycle.prepare_release_manifest_publication(plan, payload)
            if not isinstance(pending_event_id, str) or not pending_event_id:
                raise ReleaseManifestPublishError("trusted lifecycle did not seal a refresh intent")
            validate_refresh_context(context, root, sealed_plan, manifest_state="input")
            if path.read_bytes() != observed:
                raise ReleaseManifestPublishError("selected manifest input changed after refresh intent sealing")
            current_final, candidate_final, payload_final, _, _ = _refresh_candidate(root)
            if (current_final != current_after_plan
                    or candidate_final != candidate
                    or payload_final != payload):
                raise ReleaseManifestPublishError("source-derived refresh successor changed after intent sealing")
            _atomic_write(path, payload)
    except (OSError, RuntimeError, ValueError, TypeError) as error:
        pending_event_id = locals().get("pending_event_id")
        result = {"mode": "execute", "published": False,
                  "disposition": "pending_publication" if isinstance(pending_event_id, str) and pending_event_id else "blocked",
                  "publication_requirement": str(error), **plan}
        if isinstance(pending_event_id, str) and pending_event_id:
            result["pending_event_id"] = pending_event_id
        return result
    try:
        published = path.read_bytes()
        if published != payload:
            raise ReleaseManifestPublishError("refreshed manifest bytes differ from the sealed candidate")
        loaded = load_selected_manifest(root)
    except (OSError, ValueError, SelectedRouteError) as error:
        return {"mode": "execute", "published": True, "disposition": "readback_required",
                "pending_event_id": pending_event_id, "readback_requirement": str(error), **plan}
    names = [row["route"] for row in loaded["routes"]]
    if names != [*SELECTED_ROUTE_NAMES, "release_version"]:
        return {"mode": "execute", "published": True, "disposition": "readback_required",
                "pending_event_id": pending_event_id,
                "readback_requirement": "refreshed manifest does not retain the exact sixteen-route projection", **plan}
    try:
        validate_refresh_context(context, root, sealed_plan, manifest_state="candidate")
    except (TypeError, ValueError) as error:
        return {"mode": "execute", "published": True, "disposition": "readback_required",
                "pending_event_id": pending_event_id, "readback_requirement": str(error), **plan}
    evidence = {"mode": "execute", "published": True, "published_route_names": names, **plan}
    try:
        receipt = lifecycle.record_release_manifest_publication(dict(evidence))
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        return {**evidence, "disposition": "recording_required", "pending_event_id": pending_event_id,
                "recording_requirement": str(error)}
    if (not isinstance(receipt, Mapping) or set(receipt) != {"recording_ref", "candidate_canonical_manifest_sha256"}
            or not isinstance(receipt["recording_ref"], str) or not receipt["recording_ref"]
            or receipt["candidate_canonical_manifest_sha256"] != plan["candidate_canonical_manifest_sha256"]):
        return {**evidence, "disposition": "recording_required", "pending_event_id": pending_event_id,
                "recording_requirement": "trusted internal lifecycle recording is incomplete"}
    return {**evidence, "disposition": "published", "recording_ref": receipt["recording_ref"]}


def recover_release_manifest_publish(
    project_root: str | Path, *, pending_event_id: str, authorization: Any,
) -> dict[str, Any]:
    """Finalize one host-authorized, already-published sealed intent; never write bytes."""
    root = _root(project_root)
    if not isinstance(pending_event_id, str) or not pending_event_id:
        raise ReleaseManifestPublishError("recovery requires one sealed pending event identity")
    try:
        from release_manifest_authorization import PublicationAuthorizationContext
        from release_manifest_lifecycle import ReleaseManifestLifecycle
    except ImportError as error:
        raise ReleaseManifestPublishError("trusted Release manifest lifecycle is unavailable") from error
    if not isinstance(authorization, PublicationAuthorizationContext):
        raise ReleaseManifestPublishError("recovery requires a trusted host-created publication context")
    try:
        recovered = ReleaseManifestLifecycle(root, authorization).recover_release_manifest_publication(pending_event_id)
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        return {"mode": "recover", "disposition": "recording_required", "pending_event_id": pending_event_id,
                "recording_requirement": str(error)}
    return {"mode": "recover", "pending_event_id": pending_event_id, **dict(recovered)}


__all__ = [
    "ReleaseManifestPublishError", "plan_release_manifest_publish", "publish_release_manifest",
    "plan_release_manifest_refresh", "refresh_release_manifest",
    "recover_release_manifest_publish",
]
