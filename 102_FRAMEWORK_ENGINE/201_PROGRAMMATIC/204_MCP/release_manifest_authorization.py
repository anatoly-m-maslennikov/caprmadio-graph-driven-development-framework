"""Trusted-host authorization capability for one Release manifest publication.

This is deliberately not an MCP route, a JSON contract, a callback, or a
credential service.  A trusted host creates an opaque context only after
checking the Project's registered Operator, current source-derived Release
admission, and exact current manifest.  The publisher validates that same
context immediately before writing.
"""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path, PurePosixPath
import re
import tomllib
from collections.abc import Mapping
from types import MappingProxyType
from typing import Any
import weakref

from release_source_admission import (
    AUTHORITY_PIN,
    ReleaseSourceAdmissionError,
    derive_release_graph_admission,
)
from selected_routes import (
    SELECTED_ROUTE_NAMES,
    SelectedRouteError,
    canonical_digest,
    canonical_json,
    load_selected_manifest,
    selected_manifest_ref,
)


_OPERATORS_REGISTRY = PurePosixPath(".caprmedio_caprmedio/operators_registry.toml")
_SHA256 = re.compile(r"[0-9a-f]{64}")
_PLAN_FIELDS = frozenset({
    "manifest_ref", "observed_input_sha256", "current_route_names", "candidate_route_names",
    "candidate_canonical_manifest_sha256", "added_route", "added_admission_route", "candidate_byte_count",
})


class ReleaseManifestAuthorizationError(ValueError):
    """A trusted Release publication context is absent, stale, or forged."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


class PublicationAuthorizationContext:
    """A non-serializable, host-issued capability bound to one exact plan."""

    __slots__ = (
        "_root", "_plan", "_candidate_payload_sha256", "_source_frontier_digest",
        "_operator_name", "_journal_author", "_llm_session", "_authorization_ref",
        "_purpose", "_pending_event_id", "__weakref__",
    )

    def __init__(self, *_: object, **__: object) -> None:
        raise TypeError("PublicationAuthorizationContext is issued only by a trusted host")

    def __setattr__(self, _: str, __: object) -> None:
        raise AttributeError("PublicationAuthorizationContext is immutable")

    def __repr__(self) -> str:
        return "<PublicationAuthorizationContext trusted-host-issued>"

    def __reduce__(self) -> object:
        raise TypeError("PublicationAuthorizationContext is not serializable")

    def __reduce_ex__(self, _: int) -> object:
        raise TypeError("PublicationAuthorizationContext is not serializable")

    def __getstate__(self) -> object:
        raise TypeError("PublicationAuthorizationContext is not serializable")

    @property
    def operator_name(self) -> str:
        return self._operator_name

    @property
    def journal_author(self) -> str:
        return self._journal_author

    @property
    def llm_session(self) -> Mapping[str, str]:
        return MappingProxyType({"app": self._llm_session[0], "uuid": self._llm_session[1]})

    @property
    def authorization_ref(self) -> str:
        return self._authorization_ref

    @property
    def source_frontier_digest(self) -> str:
        return self._source_frontier_digest

    @property
    def authority_digest(self) -> str:
        return str(AUTHORITY_PIN["digest"])


_issued: dict[int, tuple[weakref.ReferenceType[PublicationAuthorizationContext], tuple[object, ...]]] = {}


def _reject(code: str, message: str) -> None:
    raise ReleaseManifestAuthorizationError(code, message)


def _root(value: str | Path) -> Path:
    try:
        requested = Path(value)
        root = requested.resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise ReleaseManifestAuthorizationError("publication-root-invalid", "Project root is unavailable") from error
    if requested.is_symlink() or not root.is_dir() or root.is_symlink():
        _reject("publication-root-invalid", "Project root must be a regular directory")
    return root


def _safe_ref(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or "\n" in value or "\r" in value:
        _reject("publication-context-invalid", f"{label} must be a non-empty single-line reference")
    candidate = PurePosixPath(value)
    if candidate.is_absolute() or not candidate.parts or any(part in {"", ".", ".."} for part in candidate.parts):
        _reject("publication-context-invalid", f"{label} must be a safe repository-relative reference")
    return value


def _sha256(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        _reject("publication-plan-invalid", f"{label} must be a lowercase SHA-256 digest")
    return value


def _read_regular(root: Path, relative: PurePosixPath, *, label: str) -> bytes:
    cursor = root
    try:
        for part in relative.parts:
            cursor /= part
            if cursor.is_symlink():
                _reject("publication-context-invalid", f"{label} has a symlinked ancestor")
        if not cursor.is_file():
            _reject("publication-context-invalid", f"{label} is unavailable")
        return cursor.read_bytes()
    except ReleaseManifestAuthorizationError:
        raise
    except OSError as error:
        raise ReleaseManifestAuthorizationError("publication-context-invalid", f"{label} is unreadable") from error


def _normalize_plan(value: Any, root: Path) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        _reject("publication-plan-invalid", "publication plan must be an object")
    fields = set(value)
    if fields - {"mode", *_PLAN_FIELDS} or not _PLAN_FIELDS <= fields:
        _reject("publication-plan-invalid", "publication plan has unsupported or missing fields")
    if "mode" in value and value["mode"] != "plan":
        _reject("publication-plan-invalid", "publication plan mode must be plan when supplied")
    manifest_ref = value["manifest_ref"]
    if not isinstance(manifest_ref, str) or manifest_ref != selected_manifest_ref(root):
        _reject("publication-plan-invalid", "publication plan has a different manifest carrier")
    current, candidate = value["current_route_names"], value["candidate_route_names"]
    if (not isinstance(current, list) or current != list(SELECTED_ROUTE_NAMES)
            or not isinstance(candidate, list) or candidate != [*SELECTED_ROUTE_NAMES, "release_version"]):
        _reject("publication-plan-invalid", "publication plan route sequence is not the admitted additive successor")
    if value["added_route"] != "release_version" or value["added_admission_route"] != "release_version":
        _reject("publication-plan-invalid", "publication plan does not describe the Release route")
    size = value["candidate_byte_count"]
    if type(size) is not int or size <= 0:
        _reject("publication-plan-invalid", "publication candidate byte count must be positive")
    return {
        "manifest_ref": manifest_ref,
        "observed_input_sha256": _sha256(value["observed_input_sha256"], "observed_input_sha256"),
        "current_route_names": tuple(current),
        "candidate_route_names": tuple(candidate),
        "candidate_canonical_manifest_sha256": _sha256(
            value["candidate_canonical_manifest_sha256"], "candidate_canonical_manifest_sha256"
        ),
        "added_route": "release_version",
        "added_admission_route": "release_version",
        "candidate_byte_count": size,
    }


def _derive_prepublication(root: Path) -> tuple[dict[str, Any], bytes, bytes, Path, dict[str, Any]]:
    try:
        current = load_selected_manifest(root)
    except (OSError, ValueError, SelectedRouteError) as error:
        raise ReleaseManifestAuthorizationError("publication-input-unavailable", "current selected manifest is unavailable") from error
    if [row.get("route") for row in current.get("routes", [])] != list(SELECTED_ROUTE_NAMES):
        _reject("publication-input-stale", "publication requires the current exact fifteen-route manifest")
    if "release_source_admissions" in current:
        _reject("publication-input-stale", "publication requires a manifest without Release admission")
    try:
        route, admission = derive_release_graph_admission(root)
    except (OSError, ValueError, TypeError, ReleaseSourceAdmissionError) as error:
        raise ReleaseManifestAuthorizationError("publication-source-stale", "Release source admission is not current") from error
    candidate = copy.deepcopy(current)
    candidate.pop("manifest_ref", None)
    candidate["routes"].append(copy.deepcopy(route))
    candidate["release_source_admissions"] = [copy.deepcopy(admission)]
    candidate["source_freshness"]["selected_binding_digest"] = canonical_digest(candidate["routes"])
    candidate.pop("canonical_manifest_sha256", None)
    candidate["canonical_manifest_sha256"] = canonical_digest(candidate)
    relative = selected_manifest_ref(root)
    manifest = root / relative
    observed = _read_regular(root, PurePosixPath(relative), label="selected manifest carrier")
    payload = (canonical_json(candidate) + "\n").encode("utf-8")
    plan = {
        "manifest_ref": relative,
        "observed_input_sha256": hashlib.sha256(observed).hexdigest(),
        "current_route_names": [row["route"] for row in current["routes"]],
        "candidate_route_names": [row["route"] for row in candidate["routes"]],
        "candidate_canonical_manifest_sha256": candidate["canonical_manifest_sha256"],
        "added_route": "release_version",
        "added_admission_route": "release_version",
        "candidate_byte_count": len(payload),
    }
    return _normalize_plan(plan, root), observed, payload, manifest, admission


def _source_frontier_digest(admission: Mapping[str, Any]) -> str:
    """Seal D572's live admission and its authority pin without a second table."""
    return canonical_digest({"authority": dict(AUTHORITY_PIN), "admission": dict(admission)})


def _operator_row(root: Path, operator_name: object) -> Mapping[str, Any]:
    if not isinstance(operator_name, str) or not operator_name or "\n" in operator_name or "\r" in operator_name:
        _reject("publication-operator-invalid", "Operator name must be a non-empty single line")
    try:
        parsed = tomllib.loads(_read_regular(root, _OPERATORS_REGISTRY, label="operators registry").decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise ReleaseManifestAuthorizationError("publication-operator-invalid", "operators registry is invalid") from error
    entries = parsed.get("operators") if isinstance(parsed, Mapping) else None
    if not isinstance(entries, list):
        _reject("publication-operator-invalid", "operators registry has no operator records")
    matching = [entry for entry in entries if isinstance(entry, Mapping) and entry.get("name") == operator_name]
    if len(matching) != 1:
        _reject("publication-operator-invalid", "Operator is not uniquely registered for this Project")
    return matching[0]


def _journal_context(operator: Mapping[str, Any], journal_author: object, llm_session: object) -> tuple[str, tuple[str, str]]:
    if not isinstance(journal_author, str):
        _reject("publication-journal-context-invalid", "Journal author must be a Git username")
    try:
        import sys
        tools = Path(__file__).resolve().parents[1] / "201_TOOLS"
        if str(tools) not in sys.path:
            sys.path.insert(0, str(tools))
        import work_journal
        work_journal.validate_partition(journal_author, "2000-01-01", "UTC")
    except (ImportError, RuntimeError, ValueError) as error:
        raise ReleaseManifestAuthorizationError(
            "publication-journal-context-invalid", "Journal author is not valid for Work Journal schema 3"
        ) from error
    if not isinstance(llm_session, Mapping) or set(llm_session) != {"app", "uuid"}:
        _reject("publication-journal-context-invalid", "llm_session must contain only app and uuid")
    app, identifier = llm_session.get("app"), llm_session.get("uuid")
    if not isinstance(app, str) or not app or not isinstance(identifier, str) or not identifier:
        _reject("publication-journal-context-invalid", "llm_session app and uuid must be non-empty strings")
    # The registry presently has no Journal-author mapping.  If one is added,
    # enforce it; otherwise retain the independently validated trusted pair.
    if "journal_author" in operator and operator["journal_author"] != journal_author:
        _reject("publication-journal-context-invalid", "Journal author differs from the registered Operator mapping")
    return journal_author, (app, identifier)


def _snapshot(context: PublicationAuthorizationContext) -> tuple[object, ...]:
    if type(context) is not PublicationAuthorizationContext:
        _reject("publication-context-forged", "publication context has the wrong type")
    issued = _issued.get(id(context))
    if issued is None or issued[0]() is not context:
        _reject("publication-context-forged", "publication context was not issued by this trusted host")
    values = (
        context._root, tuple(sorted(context._plan.items())), context._candidate_payload_sha256,
        context._source_frontier_digest, context._operator_name, context._journal_author,
        context._llm_session, context._authorization_ref, context._purpose, context._pending_event_id,
    )
    if values != issued[1]:
        _reject("publication-context-forged", "publication context was altered after issuance")
    return values


def _issue(
    root: Path, plan: Mapping[str, Any], *, candidate_payload: bytes, source_frontier_digest: str,
    operator_name: str, journal_author: str, llm_session: tuple[str, str], authorization_ref: str,
    purpose: str, pending_event_id: str | None,
) -> PublicationAuthorizationContext:
    context = object.__new__(PublicationAuthorizationContext)
    object.__setattr__(context, "_root", root.as_posix())
    object.__setattr__(context, "_plan", MappingProxyType(dict(plan)))
    object.__setattr__(context, "_candidate_payload_sha256", hashlib.sha256(candidate_payload).hexdigest())
    object.__setattr__(context, "_source_frontier_digest", source_frontier_digest)
    object.__setattr__(context, "_operator_name", operator_name)
    object.__setattr__(context, "_journal_author", journal_author)
    object.__setattr__(context, "_llm_session", llm_session)
    object.__setattr__(context, "_authorization_ref", authorization_ref)
    object.__setattr__(context, "_purpose", purpose)
    object.__setattr__(context, "_pending_event_id", pending_event_id)
    values = (
        context._root, tuple(sorted(context._plan.items())), context._candidate_payload_sha256,
        context._source_frontier_digest, context._operator_name, context._journal_author,
        context._llm_session, context._authorization_ref, context._purpose, context._pending_event_id,
    )
    identifier = id(context)
    _issued[identifier] = (weakref.ref(context, lambda _reference: _issued.pop(identifier, None)), values)
    return context


def authorize_operator_publication(
    project_root: str | Path,
    plan: Mapping[str, Any],
    *,
    operator_name: str,
    journal_author: str,
    llm_session: Mapping[str, str],
    authorization_ref: str,
) -> PublicationAuthorizationContext:
    """Issue one trusted-host-only capability for the exact current plan."""
    root = _root(project_root)
    supplied = _normalize_plan(plan, root)
    expected, observed, payload, _, admission = _derive_prepublication(root)
    if supplied != expected:
        _reject("publication-plan-stale", "publication plan differs from the current source-derived successor")
    if hashlib.sha256(observed).hexdigest() != supplied["observed_input_sha256"]:
        _reject("publication-input-stale", "selected manifest bytes differ from the supplied plan")
    operator = _operator_row(root, operator_name)
    author, session = _journal_context(operator, journal_author, llm_session)
    return _issue(
        root, supplied, candidate_payload=payload, source_frontier_digest=_source_frontier_digest(admission),
        operator_name=operator_name, journal_author=author, llm_session=session,
        authorization_ref=_safe_ref(authorization_ref, "authorization_ref"),
        purpose="publication", pending_event_id=None,
    )


def _pending_recovery_evidence(
    root: Path, pending_event_id: object,
) -> tuple[dict[str, Any], bytes, dict[str, Any], Mapping[str, Any]]:
    """Open the one existing sealed Release intent; never accept caller history."""
    if not isinstance(pending_event_id, str) or not pending_event_id:
        _reject("publication-recovery-invalid", "pending event id must be a non-empty string")
    try:
        import sys
        tools = Path(__file__).resolve().parents[1] / "201_TOOLS"
        if str(tools) not in sys.path:
            sys.path.insert(0, str(tools))
        import work_journal
        from release_manifest_lifecycle import ACTION_ID, _event_id, _read_intent

        pending, event, _, _ = work_journal._read_pending_event(root, pending_event_id)
        intent = _read_intent(pending)
    except Exception as error:
        raise ReleaseManifestAuthorizationError(
            "publication-recovery-invalid", "sealed Release publication evidence is unavailable or invalid"
        ) from error
    plan = _normalize_plan(intent["plan"], root)
    result = event.get("result")
    if (
        event.get("action_id") != ACTION_ID
        or event.get("event") != "completed"
        or not isinstance(result, Mapping)
        or result.get("path") != plan["manifest_ref"]
        or result.get("sha256") is None
        or pending.get("result_ref") != plan["manifest_ref"]
        or pending.get("effect_refs") != [plan["manifest_ref"]]
        or _event_id(root, intent, str(event.get("previous_result_event"))) != pending_event_id
    ):
        _reject("publication-recovery-invalid", "pending evidence is not the exact sealed Release successor")
    sealed_result_sha = _sha256(result.get("sha256"), "pending.result.sha256")
    payload = _read_regular(root, PurePosixPath(plan["manifest_ref"]), label="published selected manifest")
    if hashlib.sha256(payload).hexdigest() != sealed_result_sha:
        _reject("publication-recovery-ambiguous", "published manifest bytes differ from the sealed pending result")
    try:
        loaded = load_selected_manifest(root)
    except (OSError, ValueError, SelectedRouteError) as error:
        raise ReleaseManifestAuthorizationError(
            "publication-recovery-ambiguous", "published manifest cannot be reopened as the admitted successor"
        ) from error
    if (
        [row.get("route") for row in loaded.get("routes", [])] != [*SELECTED_ROUTE_NAMES, "release_version"]
        or loaded.get("canonical_manifest_sha256") != plan["candidate_canonical_manifest_sha256"]
    ):
        _reject("publication-recovery-ambiguous", "published manifest is not the sealed Release successor")
    try:
        _, admission = derive_release_graph_admission(root)
    except (OSError, ValueError, TypeError, ReleaseSourceAdmissionError) as error:
        raise ReleaseManifestAuthorizationError(
            "publication-source-stale", "Release source admission is not current"
        ) from error
    frontier = _source_frontier_digest(admission)
    if (
        intent["source_frontier_digest"] != frontier
        or intent["authority_digest"] != AUTHORITY_PIN["digest"]
    ):
        _reject("publication-source-stale", "sealed pending intent has a stale Release source frontier")
    return plan, payload, dict(event), admission


def _validate_recovery_actor(
    event: Mapping[str, Any], *, journal_author: str, session: tuple[str, str],
) -> None:
    if event.get("author") != journal_author or event.get("llm_session") != {"app": session[0], "uuid": session[1]}:
        _reject("publication-recovery-invalid", "trusted recovery actor does not match sealed pending evidence")


def authorize_operator_publication_recovery(
    project_root: str | Path,
    pending_event_id: str,
    *,
    operator_name: str,
    journal_author: str,
    llm_session: Mapping[str, str],
    authorization_ref: str,
) -> PublicationAuthorizationContext:
    """Issue a finalization-only context from one existing sealed pending intent.

    It accepts no historical Plan or candidate bytes from a caller.  The
    physical selected-manifest carrier must already equal the pending exact
    successor, so this context cannot authorize an initial publication or any
    replacement.
    """
    root = _root(project_root)
    plan, payload, event, admission = _pending_recovery_evidence(root, pending_event_id)
    operator = _operator_row(root, operator_name)
    author, session = _journal_context(operator, journal_author, llm_session)
    _validate_recovery_actor(event, journal_author=author, session=session)
    return _issue(
        root, plan, candidate_payload=payload, source_frontier_digest=_source_frontier_digest(admission),
        operator_name=operator_name, journal_author=author, llm_session=session,
        authorization_ref=_safe_ref(authorization_ref, "authorization_ref"),
        purpose="recovery", pending_event_id=pending_event_id,
    )


def validate_publication_context(
    context: PublicationAuthorizationContext,
    project_root: str | Path,
    plan: Mapping[str, Any],
    *,
    manifest_state: str = "input",
) -> PublicationAuthorizationContext:
    """Freshly validate an issued context before publish or after candidate write.

    ``input`` is the only pre-write state.  ``candidate`` is an explicit
    recovery/readback state and still requires the sealed candidate bytes and
    the canonical loader's current sixteen-route validation.
    """
    root = _root(project_root)
    snapshot = _snapshot(context)
    supplied = _normalize_plan(plan, root)
    (
        stored_root, stored_plan_items, payload_sha, frontier_sha, operator_name, journal_author,
        session, _, purpose, pending_event_id,
    ) = snapshot
    if root.as_posix() != stored_root:
        _reject("publication-context-stale", "publication context belongs to another Project root")
    if supplied != dict(stored_plan_items):
        _reject("publication-context-stale", "publication plan differs from the issued context")
    operator = _operator_row(root, operator_name)
    _journal_context(operator, journal_author, {"app": session[0], "uuid": session[1]})
    try:
        _, admission = derive_release_graph_admission(root)
    except (OSError, ValueError, TypeError, ReleaseSourceAdmissionError) as error:
        raise ReleaseManifestAuthorizationError("publication-source-stale", "Release source admission is not current") from error
    if _source_frontier_digest(admission) != frontier_sha:
        _reject("publication-source-stale", "Release source frontier differs from the issued context")
    relative = PurePosixPath(supplied["manifest_ref"])
    current_bytes = _read_regular(root, relative, label="selected manifest carrier")
    if manifest_state == "input":
        if purpose != "publication":
            _reject("publication-recovery-finalization-only", "recovery authority cannot authorize a manifest write")
        expected, observed, payload, _, _ = _derive_prepublication(root)
        if expected != supplied or observed != current_bytes:
            _reject("publication-input-stale", "selected manifest input differs from the issued plan")
        if hashlib.sha256(current_bytes).hexdigest() != supplied["observed_input_sha256"]:
            _reject("publication-input-stale", "selected manifest digest differs from the issued plan")
        if hashlib.sha256(payload).hexdigest() != payload_sha:
            _reject("publication-context-stale", "candidate serialization differs from the issued context")
    elif manifest_state == "candidate":
        if hashlib.sha256(current_bytes).hexdigest() != payload_sha:
            _reject("publication-candidate-stale", "published manifest bytes differ from the sealed candidate")
        try:
            loaded = load_selected_manifest(root)
        except (OSError, ValueError, SelectedRouteError) as error:
            raise ReleaseManifestAuthorizationError("publication-candidate-stale", "published manifest is not current") from error
        if ([row.get("route") for row in loaded.get("routes", [])] != [*SELECTED_ROUTE_NAMES, "release_version"]
                or loaded.get("canonical_manifest_sha256") != supplied["candidate_canonical_manifest_sha256"]):
            _reject("publication-candidate-stale", "published manifest is not the issued Release successor")
        if purpose == "recovery":
            evidence_plan, evidence_payload, evidence_event, _ = _pending_recovery_evidence(root, pending_event_id)
            if evidence_plan != supplied or evidence_payload != current_bytes:
                _reject("publication-recovery-ambiguous", "sealed recovery evidence differs from the issued context")
            _validate_recovery_actor(evidence_event, journal_author=journal_author, session=session)
        elif purpose != "publication":
            _reject("publication-context-forged", "publication context has an unsupported authority purpose")
    else:
        _reject("publication-context-invalid", "manifest_state must be input or candidate")
    return context


def validate_candidate_payload(
    context: PublicationAuthorizationContext,
    project_root: str | Path,
    plan: Mapping[str, Any],
    payload: bytes,
) -> None:
    """Confirm a normal publication payload without exposing a sealed digest."""
    if type(payload) is not bytes or not payload:
        _reject("publication-payload-invalid", "candidate payload must be non-empty bytes")
    validate_publication_context(context, project_root, plan, manifest_state="input")
    snapshot = _snapshot(context)
    if snapshot[8] != "publication":
        _reject("publication-recovery-finalization-only", "recovery authority cannot validate a pre-write payload")
    if hashlib.sha256(payload).hexdigest() != snapshot[2]:
        _reject("publication-payload-stale", "candidate payload differs from the sealed publication context")


__all__ = [
    "PublicationAuthorizationContext",
    "ReleaseManifestAuthorizationError",
    "authorize_operator_publication",
    "authorize_operator_publication_recovery",
    "validate_candidate_payload",
    "validate_publication_context",
]
