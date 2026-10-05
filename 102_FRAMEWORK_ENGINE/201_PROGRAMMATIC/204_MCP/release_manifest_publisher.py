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


def plan_release_manifest_publish(project_root: str | Path) -> dict[str, Any]:
    """Return a non-writing plan for the one additive Release projection."""
    root = _root(project_root)
    plan, _, _ = _plan(root)
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
    "recover_release_manifest_publish",
]
