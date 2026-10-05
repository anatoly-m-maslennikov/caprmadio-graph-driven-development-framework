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
import os
from pathlib import Path, PurePosixPath
import stat
import sys
import time
from typing import Any


TOOLS_ROOT = Path(__file__).resolve().parents[2]
STRUCTURE_ROOT = TOOLS_ROOT / "WORKFLOW_OPERATIONS" / "PROJECT_STRUCTURE"
for _path in (TOOLS_ROOT, STRUCTURE_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import lifecycle_intents  # noqa: E402
import project_structure  # noqa: E402
from atom_operations import split_frontmatter, frontmatter_scalar, ToolError as AtomToolError  # noqa: E402
from work_journal import canonical_json_bytes  # noqa: E402
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
_MAX_EVIDENCE_BYTES = 1024 * 1024
_MAX_EVIDENCE_REFERENCES = 128
_MAX_TOTAL_EVIDENCE_BYTES = 8 * 1024 * 1024

NATIVE_REVERT_EVIDENCE_SOURCE_REMAINDERS: tuple[str, ...] = ()


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


class _EvidenceReader:
    """Read only bounded, non-secret Project members, with no symlink traversal."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.control = lifecycle_intents.control_root(root).relative_to(root)
        self.total = 0
        self.cache: dict[str, bytes] = {}
        self.journal_snapshot: Mapping[str, Any] | None = None
        self.deadline = time.monotonic() + 10

    def read(self, reference: object) -> bytes:
        if time.monotonic() > self.deadline:
            raise NativeRevertProviderError("evidence observation timeout")
        if isinstance(reference, str) and reference.startswith("event:"):
            return self._event(reference)
        if not isinstance(reference, str) or not reference or any(c in reference for c in (":", "\\", "\x00")):
            raise NativeRevertProviderError("unsupported evidence reference")
        relative = PurePosixPath(reference)
        if not relative.parts or relative.is_absolute() or ".." in relative.parts or relative.as_posix() != reference:
            raise NativeRevertProviderError("unsafe evidence reference")
        if relative.parts[:len(self.control.parts)] != self.control.parts:
            raise NativeRevertProviderError("evidence reference is outside the configured authority/evidence root")
        if any(part == ".git" or part == ".env" or part.startswith(".env.") or part.endswith(".env")
               or any(term in part.lower().replace("-", "_")
                      for term in ("secret", "password", "credential", "private_key", "api_key", "id_rsa", "id_ed25519"))
               for part in relative.parts):
            raise NativeRevertProviderError("protected evidence reference")
        if reference in self.cache:
            return self.cache[reference]
        if len(self.cache) >= _MAX_EVIDENCE_REFERENCES:
            raise NativeRevertProviderError("evidence reference limit exceeded")
        descriptors: list[int] = []
        try:
            parent = os.open(self.root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            descriptors.append(parent)
            for part in relative.parts[:-1]:
                parent = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent)
                descriptors.append(parent)
            descriptor = os.open(relative.parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
            descriptors.append(descriptor)
            observed = os.fstat(descriptor)
            if not stat.S_ISREG(observed.st_mode) or observed.st_size > _MAX_EVIDENCE_BYTES:
                raise NativeRevertProviderError("evidence member is non-regular or exceeds its byte limit")
            with os.fdopen(os.dup(descriptor), "rb") as stream:
                content = stream.read(_MAX_EVIDENCE_BYTES + 1)
            self.total += len(content)
            if len(content) > _MAX_EVIDENCE_BYTES or self.total > _MAX_TOTAL_EVIDENCE_BYTES:
                raise NativeRevertProviderError("evidence byte limit exceeded")
        except OSError as error:
            raise NativeRevertProviderError("evidence member is missing, unsafe, or unreadable") from error
        finally:
            for descriptor in reversed(descriptors):
                os.close(descriptor)
        self.cache[reference] = content
        return content

    def _event(self, reference: str) -> bytes:
        """Resolve Event identities through the one canonical read-only reader."""
        if reference in self.cache:
            return self.cache[reference]
        event_id = reference[len("event:"):]
        if not event_id or len(event_id) > 256 or len(self.cache) >= _MAX_EVIDENCE_REFERENCES:
            raise NativeRevertProviderError("unsupported or excessive Event reference")
        query_root = TOOLS_ROOT / "FIND_AND_FETCH_JOURNAL_EVENTS"
        if str(query_root) not in sys.path:
            sys.path.insert(0, str(query_root))
        from find_and_fetch_journal_events import JournalQueryError, capture_snapshot, query

        try:
            if self.journal_snapshot is None:
                self.journal_snapshot = capture_snapshot(self.root, limits={
                    "max_snapshot_members": _MAX_EVIDENCE_REFERENCES,
                    "max_file_bytes": _MAX_EVIDENCE_BYTES,
                    "max_total_read_bytes": max(1, _MAX_TOTAL_EVIDENCE_BYTES - self.total),
                    "timeout_seconds": 10,
                })
                self.total += self.journal_snapshot["prefix_bytes"]
            result = query(self.journal_snapshot, {
                "mode": "full_events", "filter": '"event:/event_id" = ' + json.dumps(event_id), "limit": 2,
                "limits": {"max_total_read_bytes": max(1, _MAX_TOTAL_EVIDENCE_BYTES - self.total)},
            })
        except JournalQueryError as error:
            raise NativeRevertProviderError("canonical Event evidence is unavailable: " + error.code) from error
        rows = result.get("results")
        self.total += result.get("limits", {}).get("max_total_read_bytes", {}).get("consumed", 0)
        if result.get("status") != "complete" or not isinstance(rows, list) or len(rows) != 1:
            raise NativeRevertProviderError("canonical Event evidence is missing or unresolved")
        content = canonical_json_bytes(rows[0]["event"])
        self.total += len(content)
        if len(content) > _MAX_EVIDENCE_BYTES or self.total > _MAX_TOTAL_EVIDENCE_BYTES:
            raise NativeRevertProviderError("Event evidence byte limit exceeded")
        self.cache[reference] = content
        return content


def _unique_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate evidence JSON member")
        result[key] = value
    return result


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
        """Validate the frozen packet and re-observe its representable evidence."""
        try:
            if _canonical(request) != _canonical(self.approved_request):
                return ["approved_reversal_request"]
        except NativeRevertProviderError:
            return ["approved_reversal_request"]
        return self._current_evidence_mismatches()

    def revalidate(self, request: Mapping[str, Any]) -> list[str]:
        """Recheck source-bound approval/permission/evidence before each effect.

        Current target hashes are independently re-observed by
        ``RevertChangesService`` immediately before dispatch.  This method
        purposefully has no recovery or inference branch.
        """
        return self.validate_request(request)

    def _current_evidence_mismatches(self) -> list[str]:
        errors: list[str] = []
        request = self.approved_request
        try:
            reader = _EvidenceReader(self.root)
        except (OSError, ValueError, AtomToolError) as error:
            return [f"evidence_root:{error}"]
        pins: dict[str, str] = {}

        def pin(value: object, name: str, extra: frozenset[str] = frozenset()) -> bytes | None:
            if not isinstance(value, Mapping) or set(value) != {"evidence_ref", "evidence_hash", *extra}:
                errors.append(f"{name}:evidence_pin")
                return None
            reference, expected = value.get("evidence_ref"), value.get("evidence_hash")
            if not isinstance(reference, str) or not isinstance(expected, str) or len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
                errors.append(f"{name}:evidence_pin")
                return None
            if reference in pins and pins[reference] != expected:
                errors.append(f"{name}:conflicting_pin")
                return None
            pins[reference] = expected
            try:
                content = reader.read(reference)
            except NativeRevertProviderError as error:
                errors.append(f"{name}:evidence:{error}")
                return None
            if hashlib.sha256(content).hexdigest() != expected:
                errors.append(f"{name}:evidence_hash")
            return content

        def collection(name: str, expected_refs: object) -> list[Mapping[str, Any]]:
            values = request.get(name)
            if not isinstance(values, list) or not values or len(values) > _MAX_EVIDENCE_REFERENCES:
                errors.append(f"{name}:evidence_pins")
                return []
            for index, value in enumerate(values):
                pin(value, f"{name}:{index}")
            references = [value.get("evidence_ref") if isinstance(value, Mapping) else None for value in values]
            if references != expected_refs:
                errors.append(f"{name}:reference_alignment")
            return values

        collection("selected_change", request.get("selected_change_refs"))
        collection("history_record", request.get("history_reference_evidence"))
        collection("before_record", [effect.get("before_evidence") for effect in self._effect_by_id.values()])
        collection("after_record", [effect.get("after_evidence") for effect in self._effect_by_id.values()])
        references = request.get("affected_reference_hashes")
        affected = request.get("affected_reference")
        if not isinstance(references, Mapping) or not references or not isinstance(affected, list) or not affected or len(affected) > _MAX_EVIDENCE_REFERENCES:
            errors.append("affected_reference:evidence_pins")
        else:
            for index, value in enumerate(affected):
                pin(value, f"affected_reference:{index}")
            observed = {value.get("evidence_ref"): value.get("evidence_hash") for value in affected if isinstance(value, Mapping) and isinstance(value.get("evidence_ref"), str)}
            if len(observed) != len(affected) or observed != references:
                errors.append("affected_reference:hash_alignment")

        governing = request.get("governing_definition")
        content = pin(governing, "governing_definition", frozenset({"atom_id", "revision"}))
        if isinstance(governing, Mapping):
            if governing.get("evidence_hash") != request.get("governing_definition_hash"):
                errors.append("governing_definition:hash_alignment")
            if content is not None:
                try:
                    frontmatter, _ = split_frontmatter(content.decode("utf-8"))
                    reference = governing.get("evidence_ref", "")
                    current_atom = lifecycle_intents.atom_from_path(self.root, self.root / reference)
                    selected_atom = lifecycle_intents.resolve_selector(self.root, governing.get("atom_id"))
                    if (governing.get("atom_id") != "CA-O-131" or frontmatter_scalar(frontmatter, "atom_id") != governing.get("atom_id")
                            or type(governing.get("revision")) is not int or governing["revision"] < 1
                            or frontmatter_scalar(frontmatter, "version") != str(governing["revision"])
                            or frontmatter_scalar(frontmatter, "status") != "Active"
                            or current_atom.lifecycle != "active" or selected_atom.path != current_atom.path
                            or any(part in {"_projection", "archive", "drafts", "done", "canceled"} for part in PurePosixPath(reference).parts)):
                        errors.append("governing_definition:identity_revision_currentness")
                except (UnicodeDecodeError, AtomToolError, TypeError, OSError):
                    errors.append("governing_definition:identity_revision_currentness")

        for name in ("operator_decision", "executor_permission"):
            value = request.get(name)
            if not isinstance(value, Mapping):
                errors.append(f"{name}:evidence_pin")
                continue
            expected_fields = {key: item for key, item in value.items() if key not in {"evidence_ref", "evidence_hash"}}
            content = pin(value, name, frozenset(expected_fields))
            if content is None:
                continue
            try:
                observed = json.loads(content, object_pairs_hook=_unique_json_object)
                if not isinstance(observed, Mapping) or any(observed.get(key) != item for key, item in expected_fields.items()):
                    errors.append(f"{name}:record_binding")
                if name == "operator_decision" and (not isinstance(observed, Mapping) or observed.get("status") != "approved"
                        or observed.get("approved_effect_ids") != list(self._effect_by_id)
                        or _canonical(observed.get("ordered_effects")) != _canonical(request["ordered_effects"])):
                    errors.append("operator_decision:approval_revoked_or_effect_order")
                if name == "executor_permission":
                    capability = observed.get("capability") if isinstance(observed, Mapping) else None
                    supported = {effect["capability_binding"]["capability_id"] for effect in self._effect_by_id.values()}
                    if (not isinstance(observed, Mapping) or observed.get("granted") is not True
                            or not isinstance(capability, str) or (capability != "governed-reversal" and supported != {capability})):
                        errors.append("executor_permission:revoked_or_unsupported")
            except (UnicodeDecodeError, ValueError):
                errors.append(f"{name}:record_json")

        for effect_id, effect in self._effect_by_id.items():
            permission = effect["capability_binding"]["permission_evidence"]
            try:
                content = reader.read(permission["evidence_ref"])
                if hashlib.sha256(content).hexdigest() != permission["evidence_hash"]:
                    errors.append(f"capability_permission_hash:{effect_id}")
                observed = json.loads(content, object_pairs_hook=_unique_json_object)
                if not isinstance(observed, Mapping) or observed.get("capability_id") != permission["capability_id"]:
                    errors.append(f"capability_permission_identity:{effect_id}")
                if not isinstance(observed, Mapping) or observed.get("granted") is not True:
                    errors.append(f"capability_permission_revoked:{effect_id}")
            except (NativeRevertProviderError, UnicodeDecodeError, ValueError) as error:
                errors.append(f"capability_permission_evidence:{effect_id}:{error}")
        for effect_id, effect in self._effect_by_id.items():
            for reference in effect["capability_binding"]["evidence_refs"]:
                if reference not in pins:
                    errors.append(f"effect_evidence:{effect_id}:unbound_reference")
        return errors

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
        current_errors = self.revalidate(self.approved_request)
        if current_errors:
            raise NativeRevertProviderError("current evidence is not admitted: " + ", ".join(current_errors))
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
    "NATIVE_REVERT_EVIDENCE_SOURCE_REMAINDERS",
    "NativeRevertProvider",
    "NativeRevertProviderError",
    "make_native_revert_service",
]
