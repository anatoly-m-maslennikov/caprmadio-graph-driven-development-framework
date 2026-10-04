"""Source-bound native effect provider for one selected CA-O-131 reversal.

The provider deliberately has no file-writer, Git, or inverse-operation API.
It accepts one frozen, complete reversal request at queue construction and can
invoke only existing lifecycle and exact Project Structure recovery capabilities.
Run and Journal ownership remains with :mod:`revert_changes` and its shared
selected-run session bridge.
"""
from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from pathlib import Path, PurePosixPath
import sys
from typing import Any


TOOLS_ROOT = Path(__file__).resolve().parents[2]
STRUCTURE_ROOT = TOOLS_ROOT / "WORKFLOW_OPERATIONS" / "PROJECT_STRUCTURE"
for _path in (TOOLS_ROOT, STRUCTURE_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import lifecycle_intents  # noqa: E402
import project_structure  # noqa: E402
from revert_changes import RevertChangesError, RevertChangesService  # noqa: E402


NATIVE_REVERT_PROVIDER_CONTEXT_SCHEMA = {
    "required": {
        "project_root": "existing selected Project root",
        "approved_reversal_request": "one complete CA-R-1833 reversal_request frozen by the selected queue",
    },
    "supported_capability_ids": (
        "lifecycle.update_atom",
        "lifecycle.change_status_atom",
        "structure.rollback_scope_unit_change",
    ),
    "excluded": (
        "generic file writes", "Git reset", "history deletion", "inverse inference", "new Journal serialization",
    ),
}

_CONTEXT_FIELDS = frozenset({"project_root", "approved_reversal_request"})
_BINDING_FIELDS = frozenset({"capability_id", "parameters", "target", "permission_evidence", "evidence_refs"})
_SUPPORTED = frozenset(NATIVE_REVERT_PROVIDER_CONTEXT_SCHEMA["supported_capability_ids"])


class NativeRevertProviderError(ValueError):
    """The selected queue lacks an admitted native reversal capability."""


def _canonical(value: object) -> str:
    try:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    except (TypeError, ValueError) as error:
        raise NativeRevertProviderError("provider context must contain JSON-compatible exact bindings") from error


def _digest(value: object) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _mapping(value: object, name: str) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        raise NativeRevertProviderError(f"{name} must be an object")
    return dict(value)


def _safe_member(root: Path, raw: object) -> Path:
    if not isinstance(raw, str) or not raw or "\\" in raw or "\x00" in raw:
        raise NativeRevertProviderError("RMED remainder: structural recovery path is not an exact repository-relative member")
    candidate = PurePosixPath(raw)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise NativeRevertProviderError("RMED remainder: structural recovery path escapes the selected Project")
    path = root.joinpath(*candidate.parts)
    try:
        path.resolve(strict=False).relative_to(root)
    except ValueError as error:
        raise NativeRevertProviderError("RMED remainder: structural recovery path escapes the selected Project") from error
    return path


class NativeRevertProvider:
    """Bind a frozen selected request to the existing governed native effects.

    A provider has no ambient registration.  Its context is the explicit
    selected-queue handoff and every later request must canonically equal that
    handoff.  This makes a newly supplied effect, permission, or evidence item
    a blocked binding rather than a new mutation authority.
    """

    def __init__(self, context: Mapping[str, Any]) -> None:
        raw = _mapping(context, "native revert provider context")
        if set(raw) != _CONTEXT_FIELDS:
            raise NativeRevertProviderError(
                "native revert provider context must contain only project_root and approved_reversal_request"
            )
        project_root = raw["project_root"]
        if not isinstance(project_root, str) or not project_root:
            raise NativeRevertProviderError("project_root must name one existing selected Project")
        try:
            self.root = Path(project_root).resolve(strict=True)
        except OSError as error:
            raise NativeRevertProviderError("project_root must name one existing selected Project") from error
        if not self.root.is_dir():
            raise NativeRevertProviderError("project_root must name one existing selected Project")
        request = _mapping(raw["approved_reversal_request"], "approved_reversal_request")
        # Round-trip to freeze every nested mapping/list and reject hidden callables.
        self.approved_request: dict[str, Any] = json.loads(_canonical(request))
        effects = self.approved_request.get("ordered_effects")
        if not isinstance(effects, list) or not effects:
            raise NativeRevertProviderError("RMED remainder: approved_reversal_request lacks complete ordered effects")
        self._effect_by_id: dict[str, dict[str, Any]] = {}
        self._effect_by_target: dict[str, dict[str, Any]] = {}
        for raw_effect in effects:
            effect = _mapping(raw_effect, "approved effect")
            effect_id = effect.get("effect_id")
            target_id = effect.get("target_id")
            if not isinstance(effect_id, str) or not effect_id or not isinstance(target_id, str) or not target_id:
                raise NativeRevertProviderError("RMED remainder: approved effect lacks exact effect_id or target_id")
            if effect_id in self._effect_by_id or target_id in self._effect_by_target:
                raise NativeRevertProviderError("RMED remainder: selected native provider requires one exact effect per target")
            self._validate_native_binding(effect)
            self._effect_by_id[effect_id] = effect
            self._effect_by_target[target_id] = effect

    @classmethod
    def from_context(cls, context: Mapping[str, Any]) -> "NativeRevertProvider":
        """Create the explicit provider needed by selected-queue startup."""
        return cls(context)

    def validate_request(self, request: Mapping[str, Any]) -> list[str]:
        """Reject any request that is not the queue's exact approved packet."""
        try:
            return [] if _canonical(request) == _canonical(self.approved_request) else ["approved_reversal_request"]
        except NativeRevertProviderError:
            return ["approved_reversal_request"]

    def revalidate(self, request: Mapping[str, Any]) -> list[str]:
        """Recheck source-bound approval/permission/evidence before each effect.

        Current target hashes are independently re-observed by
        ``RevertChangesService`` immediately before dispatch.  This method
        purposefully has no recovery or inference branch.
        """
        return self.validate_request(request)

    def observe(self, target_id: str) -> str:
        """Return the exact capability-specific current-state hash for one target."""
        effect = self._effect_by_target.get(target_id)
        if effect is None:
            raise NativeRevertProviderError("RMED remainder: target is not bound by the selected effect manifest")
        binding = _mapping(effect["capability_binding"], "capability_binding")
        capability_id = binding["capability_id"]
        if capability_id in {"lifecycle.update_atom", "lifecycle.change_status_atom"}:
            target = _mapping(binding["target"], "lifecycle target")
            atom_id = target.get("atom_id")
            if not isinstance(atom_id, str) or not atom_id:
                raise NativeRevertProviderError("RMED remainder: lifecycle target lacks an exact Atom descriptor")
            return _digest(lifecycle_intents.carrier_descriptor(self.root, atom_id))
        if capability_id == "structure.rollback_scope_unit_change":
            target = _mapping(binding["target"], "structural recovery target")
            if set(target) != {"recovery_boundary"}:
                raise NativeRevertProviderError("RMED remainder: structural target must be one exact recovery boundary")
            return _digest(self._structural_state(target["recovery_boundary"]))
        raise NativeRevertProviderError(f"RMED remainder: no admitted native capability for {capability_id!r}")

    def apply_effect(self, effect: dict[str, Any]) -> Mapping[str, Any]:
        """Invoke only the exact previously bound lifecycle/structure capability."""
        effect_id = effect.get("effect_id")
        registered = self._effect_by_id.get(effect_id) if isinstance(effect_id, str) else None
        if registered is None or _canonical(effect) != _canonical(registered):
            raise NativeRevertProviderError("approved effect no longer exactly matches the selected provider binding")
        binding = _mapping(registered["capability_binding"], "capability_binding")
        capability_id = binding["capability_id"]
        parameters = _mapping(binding["parameters"], "capability parameters")
        target = _mapping(binding["target"], "capability target")
        if capability_id == "lifecycle.update_atom":
            self._require_target_parameter(parameters, target, "target")
            result = lifecycle_intents.update_atom_action(self.root, parameters, execute=True, authorized=True)
        elif capability_id == "lifecycle.change_status_atom":
            self._require_target_parameter(parameters, target, "target")
            result = lifecycle_intents.change_status_atom_action(self.root, parameters, execute=True, authorized=True)
        elif capability_id == "structure.rollback_scope_unit_change":
            if set(target) != {"recovery_boundary"} or parameters != {"recovery_boundary": target["recovery_boundary"]}:
                raise NativeRevertProviderError("structural recovery capability requires the exact bound recovery boundary")
            result = project_structure.rollback_scope_unit_change(self.root, target["recovery_boundary"])
        else:
            raise NativeRevertProviderError(f"RMED remainder: no admitted native capability for {capability_id!r}")
        outcome = result.get("outcome", result.get("state")) if isinstance(result, Mapping) else None
        if outcome not in {"applied", "no-op", "rolled_back"}:
            raise NativeRevertProviderError(f"native capability returned non-completing outcome: {outcome!r}")
        return {
            "capability_id": capability_id,
            "native_result": dict(result),
            "evidence_refs": list(binding["evidence_refs"]),
        }

    def _validate_native_binding(self, effect: Mapping[str, Any]) -> None:
        binding = _mapping(effect.get("capability_binding"), "capability_binding")
        if set(binding) != _BINDING_FIELDS:
            raise NativeRevertProviderError("RMED remainder: capability binding is incomplete")
        capability_id = binding.get("capability_id")
        if capability_id not in _SUPPORTED:
            raise NativeRevertProviderError(f"RMED remainder: no admitted native capability for {capability_id!r}")
        parameters = _mapping(binding.get("parameters"), "capability parameters")
        target = _mapping(binding.get("target"), "capability target")
        permission = _mapping(binding.get("permission_evidence"), "capability permission evidence")
        evidence_refs = binding.get("evidence_refs")
        if permission.get("capability_id") != capability_id or permission.get("granted") is not True:
            raise NativeRevertProviderError("RMED remainder: capability permission is absent, revoked, or mismatched")
        if not isinstance(permission.get("evidence_ref"), str) or not permission["evidence_ref"]:
            raise NativeRevertProviderError("RMED remainder: capability permission evidence reference is missing")
        evidence_hash = permission.get("evidence_hash")
        if not isinstance(evidence_hash, str) or len(evidence_hash) != 64 or any(character not in "0123456789abcdef" for character in evidence_hash):
            raise NativeRevertProviderError("RMED remainder: capability permission evidence hash is invalid")
        if not isinstance(evidence_refs, list) or not evidence_refs or any(not isinstance(item, str) or not item for item in evidence_refs):
            raise NativeRevertProviderError("RMED remainder: capability evidence references are incomplete")
        if capability_id in {"lifecycle.update_atom", "lifecycle.change_status_atom"}:
            self._require_target_parameter(parameters, target, "target")
        elif capability_id == "structure.rollback_scope_unit_change":
            if set(target) != {"recovery_boundary"} or parameters != {"recovery_boundary": target["recovery_boundary"]}:
                raise NativeRevertProviderError("RMED remainder: structural recovery lacks its exact admitted boundary")
            self._structural_state(target["recovery_boundary"])

    @staticmethod
    def _require_target_parameter(parameters: Mapping[str, Any], target: Mapping[str, Any], field: str) -> None:
        if parameters.get(field) != target:
            raise NativeRevertProviderError("RMED remainder: lifecycle capability target differs from the exact approved packet")

    def _structural_state(self, boundary_value: object) -> dict[str, Any]:
        boundary = _mapping(boundary_value, "recovery_boundary")
        references = boundary.get("references", [])
        if not isinstance(references, list):
            raise NativeRevertProviderError("RMED remainder: structural recovery references are not an exact list")
        candidates = [boundary.get("toml"), *references]
        members: list[dict[str, str]] = []
        for record in candidates:
            if record is None:
                continue
            entry = _mapping(record, "recovery boundary member")
            if not isinstance(entry.get("path"), str):
                raise NativeRevertProviderError("RMED remainder: structural recovery member lacks its exact path")
            path = _safe_member(self.root, entry.get("path"))
            if not path.is_file() or path.is_symlink():
                raise NativeRevertProviderError("RMED remainder: structural recovery member is unavailable or unsafe")
            members.append({
                "path": str(entry["path"]),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            })
        if not members:
            raise NativeRevertProviderError("RMED remainder: structural recovery boundary has no exact members")
        return {"members": sorted(members, key=lambda item: item["path"])}


class _SessionOnlyTracker:
    """Prevent direct execution from replacing the selected-run Journal bridge."""

    def start(self, _payload: Mapping[str, Any]) -> Mapping[str, Any]:
        raise RevertChangesError("native revert factory requires execute_with_session and the shared selected Action Run")

    def finish(self, _event: Mapping[str, Any]) -> Mapping[str, Any]:
        raise RevertChangesError("native revert factory requires execute_with_session and the shared selected Action Run")

    def recover(self, _event: Mapping[str, Any]) -> Mapping[str, Any]:
        raise RevertChangesError("native revert factory requires recover_recording_with_session and the shared selected Action Run")


def make_native_revert_service(context: Mapping[str, Any]) -> RevertChangesService:
    """Build the selected-queue CA-O-131 service from its required frozen context.

    The root/backend later supplies this service to ``make_revert_action_handler``.
    The factory intentionally does not register a handler, mutate a Project, or
    create a Workflow/Step/Action Run at startup.
    """
    provider = NativeRevertProvider.from_context(context)
    return RevertChangesService(
        provider.observe,
        provider.apply_effect,
        _SessionOnlyTracker(),
        revalidate=provider.revalidate,
        capability_validator=provider.validate_request,
    )


__all__ = [
    "NATIVE_REVERT_PROVIDER_CONTEXT_SCHEMA",
    "NativeRevertProvider",
    "NativeRevertProviderError",
    "make_native_revert_service",
]
