"""Canonical Journal recording for the two explicitly admitted direct Actions.

This deliberately does *not* use the selected-workflow registry, a selected
route, or :class:`workflow_run_support.RunTracker`.  CA-O-180 and CA-O-187 are
source-pinned, Operator-authorized direct Actions. Their durable invocation intent is the
canonical ``started`` Journal event; it is written and reopened before any
effect is eligible to run.

The module owns no private Action ledger.  It uses the existing Work Journal's
sealed events, receipt de-duplication, append contexts, and pending-event
recovery.  Therefore an interrupted process cannot silently replay an unknown
installation effect: it may only recover the exact original pending Journal
event, and a previously started direct Action requires a new deliberate
recovery decision outside this session.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import tomllib
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import work_journal


DIRECT_ACTION_APP = "direct-action-session"
INITIALIZATION_ACTION_ID = "FRAMEWORK_INITIALIZATION"
RESTORATION_ACTION_ID = "FRAMEWORK_IMAGE_RESTORATION"
STRUCTURAL_SCOPE = "PROJECT_CONFIGURATION"
ACTION_ATOM_ID = "CA-O-180"
ACTION_ATOM_VERSION = 1
ACTION_ATOM_RELATIVE = Path(
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/"
    "CA-O-180-PROJECT_CONFIGURATION-ACTION--initialize-the-first-framework-runtime-and-project-local-ca-skill.md"
)
# This is an intentional source pin.  A changed O-180 source must be reviewed
# and rebound here rather than silently changing what a direct bootstrap Run
# claims to implement.
ACTION_ATOM_SHA256 = "327f9e9722ed4346251172e36b42e0ad5a322de62ec13ecce21c52f89790a073"
RESTORATION_ATOM_ID = "CA-O-187"
RESTORATION_ATOM_VERSION = 2
RESTORATION_ATOM_RELATIVE = ACTION_ATOM_RELATIVE.parent / "CA-O-187-PROJECT_CONFIGURATION-ACTION--restore-the-selected-missing-bootstrap-image.md"
RESTORATION_ATOM_SHA256 = "6e0320a7026f37c6e0e4199051d47a4c597cdbe22bb5fb1bfb7b0626258852c1"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,159}$")
_OUTCOMES = frozenset({"completed", "no_op", "failed", "cancelled", "partial"})


class DirectActionJournalError(RuntimeError):
    """Stable direct-Action Journal refusal or recording failure."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


@dataclass(frozen=True)
class _ActionDescriptor:
    atom_id: str
    version: int
    path: Path
    digest: str
    instruction: str


def _action_descriptor(action_id: str) -> _ActionDescriptor:
    """Select only the two reviewed direct Actions; callers supply no pins."""
    if action_id == INITIALIZATION_ACTION_ID:
        return _ActionDescriptor(ACTION_ATOM_ID, ACTION_ATOM_VERSION, ACTION_ATOM_RELATIVE,
                                 ACTION_ATOM_SHA256, "first Framework runtime initialization")
    if action_id == RESTORATION_ACTION_ID:
        return _ActionDescriptor(RESTORATION_ATOM_ID, RESTORATION_ATOM_VERSION, RESTORATION_ATOM_RELATIVE,
                                 RESTORATION_ATOM_SHA256, "retained selected Framework image restoration")
    raise DirectActionJournalError("direct-action-unadmitted", "direct Action is not one of the two admitted Actions")


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _safe_ref(value: object, label: str, *, allow_none: bool = False) -> str | None:
    if value is None and allow_none:
        return None
    if not isinstance(value, str) or not value:
        raise DirectActionJournalError("direct-action-invalid-input", f"{label} must be a non-empty repository-relative reference")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise DirectActionJournalError("direct-action-invalid-input", f"{label} must be repository-relative")
    return value


def _digest(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise DirectActionJournalError("direct-action-invalid-input", f"{label} must be a lowercase SHA-256 digest")
    return value


def _regular_root(value: str | Path) -> Path:
    try:
        root = Path(value).resolve(strict=True)
    except OSError as error:
        raise DirectActionJournalError("direct-action-root-invalid", "project root does not exist") from error
    if root.is_symlink() or not root.is_dir():
        raise DirectActionJournalError("direct-action-root-invalid", "project root must be a regular directory")
    return root


def _read_regular_relative(root: Path, relative: Path, *, code: str, label: str) -> bytes:
    """Read an exact Project carrier without crossing a symlinked ancestor."""
    candidate = root
    try:
        for part in relative.parts:
            candidate = candidate / part
            if candidate.is_symlink():
                raise DirectActionJournalError(code, f"{label} has a symlinked ancestor")
        if not candidate.is_file():
            raise DirectActionJournalError(code, f"{label} is unavailable")
        return candidate.read_bytes()
    except DirectActionJournalError:
        raise
    except OSError as error:
        raise DirectActionJournalError(code, f"{label} is unreadable") from error


def _source_binding(root: Path, action_id: str = INITIALIZATION_ACTION_ID) -> dict[str, Any]:
    descriptor = _action_descriptor(action_id)
    name = descriptor.atom_id.removeprefix("CA-")
    payload = _read_regular_relative(
        root,
        descriptor.path,
        code="direct-action-source-stale",
        label=f"the exact {name} source carrier",
    )
    if _sha256(payload) != descriptor.digest:
        raise DirectActionJournalError("direct-action-source-stale", f"the exact {name} source digest is not admitted")
    return {
        "kind": "action",
        "atom_id": descriptor.atom_id,
        "version": descriptor.version,
        "path": descriptor.path.as_posix(),
        "digest": descriptor.digest,
    }


def _authorization(root: Path, value: Mapping[str, Any]) -> dict[str, str]:
    if not isinstance(value, Mapping) or set(value) != {"operator", "authorization_ref"}:
        raise DirectActionJournalError(
            "direct-action-authorization-required",
            "explicit Operator authorization requires operator and authorization_ref",
        )
    operator = value.get("operator")
    if not isinstance(operator, str) or not operator.strip() or "\n" in operator or "\r" in operator:
        raise DirectActionJournalError("direct-action-authorization-required", "Operator identity must be a non-empty single line")
    registry_relative = Path(".caprmedio_caprmedio/operators_registry.toml")
    try:
        entries = tomllib.loads(
            _read_regular_relative(
                root,
                registry_relative,
                code="direct-action-authorization-required",
                label="registered Operator evidence",
            ).decode("utf-8")
        ).get("operators")
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise DirectActionJournalError(
            "direct-action-authorization-required",
            "registered Operator evidence is unavailable",
        ) from error
    if not isinstance(entries, list) or not any(
        isinstance(entry, Mapping) and entry.get("name") == operator for entry in entries
    ):
        raise DirectActionJournalError(
            "direct-action-authorization-required",
            "explicit Operator is not registered for this Project",
        )
    return {"operator": operator, "authorization_ref": str(_safe_ref(value.get("authorization_ref"), "authorization_ref"))}


def _image_digest(value: object) -> str:
    if not isinstance(value, str) or not value.startswith("sha256:") or _SHA256.fullmatch(value.removeprefix("sha256:")) is None:
        raise DirectActionJournalError("direct-action-invalid-input", "intent.image_digest must be an immutable sha256 image ID")
    return value


def _intent(value: Mapping[str, Any], action_id: str = INITIALIZATION_ACTION_ID) -> dict[str, str]:
    if action_id == RESTORATION_ACTION_ID:
        expected = {"action_id", "kind", "manifest_sha256", "source_context_sha256",
                    "selected_selector_sha256", "old_image_digest", "retained_proof_receipt_sha256",
                    "retained_context_sha256"}
        if not isinstance(value, Mapping) or set(value) != expected:
            raise DirectActionJournalError("direct-action-invalid-intent", "restoration intent has unsupported or missing fields")
        if value.get("action_id") != RESTORATION_ACTION_ID or value.get("kind") != "retained_selected_framework_image_restoration":
            raise DirectActionJournalError("direct-action-invalid-intent", "intent does not describe the admitted restoration Action")
        return {
            "action_id": RESTORATION_ACTION_ID,
            "kind": "retained_selected_framework_image_restoration",
            "old_image_digest": _image_digest(value.get("old_image_digest")),
            **{field: _digest(value.get(field), f"intent.{field}") for field in
               ("manifest_sha256", "source_context_sha256", "selected_selector_sha256",
                "retained_proof_receipt_sha256", "retained_context_sha256")},
        }
    _action_descriptor(action_id)
    expected = {"action_id", "kind", "manifest_sha256", "source_context_sha256", "image_digest"}
    if not isinstance(value, Mapping) or set(value) != expected:
        raise DirectActionJournalError("direct-action-invalid-intent", "initialization intent has unsupported or missing fields")
    if value.get("action_id") != INITIALIZATION_ACTION_ID or value.get("kind") != "first_framework_runtime_installation":
        raise DirectActionJournalError("direct-action-invalid-intent", "intent does not describe the admitted first-runtime Action")
    return {
        "action_id": INITIALIZATION_ACTION_ID,
        "kind": "first_framework_runtime_installation",
        "manifest_sha256": _digest(value.get("manifest_sha256"), "intent.manifest_sha256"),
        "source_context_sha256": _digest(value.get("source_context_sha256"), "intent.source_context_sha256"),
        "image_digest": _image_digest(value.get("image_digest")),
    }


def _journal_parts(root: Path) -> list[Path]:
    """Return the configured canonical Journal parts without creating a Journal."""
    try:
        journal_root = root / work_journal.configured_journal_root(root)
    except (OSError, RuntimeError) as error:
        raise DirectActionJournalError("direct-action-journal-unavailable", "canonical Work Journal is unavailable") from error
    if not journal_root.exists():
        return []
    if journal_root.is_symlink() or not journal_root.is_dir():
        raise DirectActionJournalError("direct-action-journal-invalid", "canonical Work Journal root is not a regular directory")
    return sorted(path for path in journal_root.glob("*.ndjson") if path.is_file() and not path.is_symlink())


def _reopen_event(root: Path, event_id: str) -> tuple[dict[str, Any], dict[str, Any]] | None:
    """Read one already-appended sealed event and reconstruct its receipt.

    This is a Journal reader, not a second event store.  The receipt shape is
    identical to the Work Journal writer's receipt and is calculated from the
    exact carrier bytes that were reopened.
    """
    for path in _journal_parts(root):
        try:
            raw = path.read_bytes()
        except OSError as error:
            raise DirectActionJournalError("direct-action-journal-unavailable", f"cannot reopen {path.name}") from error
        if raw and not raw.endswith(b"\n"):
            raise DirectActionJournalError("direct-action-journal-invalid", f"Journal carrier lacks terminal newline: {path.name}")
        lines = raw.splitlines(keepends=True)
        for line_number, line in enumerate(lines, start=1):
            try:
                candidate = json.loads(line)
            except json.JSONDecodeError as error:
                raise DirectActionJournalError("direct-action-journal-invalid", f"invalid JSON in {path.name}:{line_number}") from error
            if not isinstance(candidate, dict) or candidate.get("event_id") != event_id:
                continue
            try:
                event = work_journal.validate_sealed_event(candidate)
            except work_journal.WorkJournalError as error:
                raise DirectActionJournalError("direct-action-journal-invalid", f"invalid sealed Journal event {event_id}") from error
            before = b"".join(lines[: line_number - 1])
            appended = b"".join(lines[:line_number])
            try:
                carrier = path.relative_to(root).as_posix()
            except ValueError as error:
                raise DirectActionJournalError("direct-action-journal-invalid", "Journal carrier escapes project root") from error
            return event, {
                "event_id": event["event_id"],
                "action_id": event["action_id"],
                "event_digest": event["event_digest"],
                "carrier": carrier,
                "line": line_number,
                "previous_carrier_digest": _sha256(before),
                "appended_carrier_digest": _sha256(appended),
            }
    return None


class DirectActionSession:
    """One explicitly authorized closed direct Action backed only by Journal v5.

    ``actual``, ``terminal``, and ``receipts`` are intentionally small
    observable state for the installer.  They are not a durable side ledger;
    the canonical Work Journal remains the only durable Run evidence.
    """

    def __init__(
        self,
        project_root: str | Path,
        *,
        author: str,
        operator_authorization: Mapping[str, Any],
        action_id: str = INITIALIZATION_ACTION_ID,
        timezone: str = "UTC",
        now: Callable[[], dt.datetime] | None = None,
    ) -> None:
        self.descriptor = _action_descriptor(action_id)
        self.action_id = action_id
        self.root = _regular_root(project_root)
        try:
            work_journal.validate_partition(author, "2000-01-01", timezone)
        except work_journal.WorkJournalError as error:
            raise DirectActionJournalError("direct-action-journal-context-invalid", str(error)) from error
        self.author = author
        self.timezone = timezone
        self.authorization = _authorization(self.root, operator_authorization)
        self._now = now or (lambda: dt.datetime.now(dt.UTC))
        self.actual: dict[str, dict[str, Any]] = {}
        self.terminal: dict[str, dict[str, Any]] = {}
        self.receipts: list[dict[str, Any]] = []
        self.pending: dict[str, dict[str, Any]] = {}
        self._observed: dict[str, dict[str, Any]] = {}
        self._invocation_locks: list[tuple[str, Any]] = []
        self._closed = False

    def __enter__(self) -> "DirectActionSession":
        if self._closed:
            raise DirectActionJournalError("direct-action-invocation-closed", "direct Action session is closed")
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        del exc_type, exc, traceback
        self.close()

    def close(self) -> None:
        """Release a locally held invocation lock without inferring an outcome.

        Callers should use this session as a context manager.  Closing never
        replays an effect or writes a synthetic terminal fact: a persisted
        ``started`` event remains recovery-only evidence.
        """
        if not self._closed:
            self._release_invocation_lock()
            self._closed = True

    def begin_action(
        self,
        *,
        action_id: str,
        requested_run_id: str,
        intent: Mapping[str, Any],
    ) -> Mapping[str, Any]:
        """Append and reopen the exact started event before any installer effect.

        A new process that sees a previously started action raises a recovery
        requirement.  It never assumes the absent terminal event means no
        effect happened and never emits a second start event.
        """
        if self._closed:
            raise DirectActionJournalError("direct-action-invocation-closed", "direct Action session is closed")
        if action_id != self.action_id:
            raise DirectActionJournalError("direct-action-unadmitted", f"only {self.action_id} is admitted by this Session")
        if not isinstance(requested_run_id, str) or _RUN_ID.fullmatch(requested_run_id) is None:
            raise DirectActionJournalError("direct-action-invalid-run", "requested_run_id has invalid syntax")
        normalized_intent = _intent(intent, self.action_id)
        binding = _source_binding(self.root, self.action_id)
        identity = self._run_identity(requested_run_id, binding)
        run_id = f"direct-action:{identity}"
        existing = self.actual.get(run_id)
        if existing is not None:
            raise DirectActionJournalError(
                "direct-action-invocation-active",
                "this direct Action invocation is already active in this session",
            )
        self._acquire_invocation_lock(requested_run_id, binding)

        try:
            started_id = f"direct-action:{identity}:started"
            pending_start = self._pending_event(started_id)
            if pending_start is not None:
                self._validate_started(pending_start, requested_run_id, normalized_intent, binding, run_id)
                raise DirectActionJournalError(
                    "direct-action-recording-pending",
                    f"canonical started evidence is pending; recover only original event {started_id}",
                )
            reopened = _reopen_event(self.root, started_id)
            if reopened is not None:
                event, _ = reopened
                self._validate_started(event, requested_run_id, normalized_intent, binding, run_id)
                terminal = self._existing_terminal(identity, requested_run_id, normalized_intent, binding, run_id)
                if terminal is not None:
                    raise DirectActionJournalError("direct-action-already-terminal", "this direct Action already has canonical terminal evidence")
                raise DirectActionJournalError(
                    "direct-action-recovery-required",
                    "canonical started evidence exists without a terminal result; inspect or recover the original recording only",
                )

            event = self._event(
                event_id=started_id,
                run_id=run_id,
                requested_run_id=requested_run_id,
                intent=normalized_intent,
                binding=binding,
                event_name="started",
                outcome=None,
                result_ref=None,
                effect_refs=[],
                report_ref=None,
            )
            receipt = self._append(event, result_ref=None, effect_refs=[])
            reopened = _reopen_event(self.root, started_id)
            if reopened is None:
                raise DirectActionJournalError("direct-action-journal-unavailable", "started Action evidence did not reopen after append")
            saved, saved_receipt = reopened
            self._validate_started(saved, requested_run_id, normalized_intent, binding, run_id)
            if saved_receipt != receipt:
                raise DirectActionJournalError("direct-action-journal-invalid", "reopened started receipt differs from append receipt")
            self.actual[run_id] = {
                "requested_run_id": requested_run_id,
                "intent": normalized_intent,
                "binding": binding,
                "event_id": started_id,
                "event_receipt": dict(receipt),
            }
            self.receipts.append(dict(receipt))
            return {"run_id": run_id, "disposition": "started", "event_id": started_id, "event_receipt": dict(receipt)}
        except BaseException:
            self._release_invocation_lock()
            raise

    def record_effects(self, run_id: str, *, result_ref: str, effect_refs: list[str]) -> None:
        """Keep observed actual effects until the sole terminal writer records them."""
        self._require_open_run(run_id)
        result = str(_safe_ref(result_ref, "result_ref"))
        effects = self._effect_refs(effect_refs)
        observed = {"result_ref": result, "effect_refs": effects}
        prior = self._observed.get(run_id)
        if prior is not None and prior != observed:
            raise DirectActionJournalError("direct-action-effect-mismatch", "one Action Run cannot replace observed actual effects")
        self._observed[run_id] = observed

    def finish_action(
        self,
        run_id: str,
        *,
        outcome: str,
        result_ref: str,
        effect_refs: list[str],
        report_ref: str | None = None,
    ) -> Mapping[str, Any]:
        """Append one terminal fact after effects were observed by the caller."""
        run = self._require_open_run(run_id)
        if outcome not in _OUTCOMES:
            raise DirectActionJournalError("direct-action-invalid-outcome", "outcome is not admitted")
        result = str(_safe_ref(result_ref, "result_ref"))
        effects = self._effect_refs(effect_refs)
        report = _safe_ref(report_ref, "report_ref", allow_none=True)
        observed = self._observed.get(run_id)
        if observed is None:
            raise DirectActionJournalError("direct-action-effects-unobserved", "actual effects must be observed before terminal recording")
        if observed != {"result_ref": result, "effect_refs": effects}:
            raise DirectActionJournalError("direct-action-effect-mismatch", "terminal evidence must retain observed actual effects")
        identity = self._run_identity(run["requested_run_id"], run["binding"])
        event_name = {"completed": "completed", "no_op": "completed", "failed": "failed", "partial": "failed", "cancelled": "abandoned"}[outcome]
        terminal_key = work_journal.canonical_json_digest(
            {
                "intent_sha256": self._intent_identity(run["intent"], run["binding"]),
                "outcome": outcome,
                "result_ref": result,
                "effect_refs": effects,
                "report_ref": report,
            }
        )
        event_id = f"direct-action:{identity}:terminal:{terminal_key}"
        event = self._event(
            event_id=event_id,
            run_id=run_id,
            requested_run_id=run["requested_run_id"],
            intent=run["intent"],
            binding=run["binding"],
            event_name=event_name,
            outcome=outcome,
            result_ref=result,
            effect_refs=effects,
            report_ref=report,
        )
        try:
            reopened = _reopen_event(self.root, event_id)
            if reopened is not None:
                saved, receipt = reopened
                self._validate_terminal(saved, run_id, run["requested_run_id"], run["intent"], run["binding"], event)
                result_value = self._terminal_result(event, receipt)
                self.terminal[run_id] = result_value
                self.receipts.append(dict(receipt))
                return dict(result_value)
            receipt = self._append(event, result_ref=result, effect_refs=effects)
            reopened = _reopen_event(self.root, event_id)
            if reopened is None:
                raise DirectActionJournalError("direct-action-journal-unavailable", "terminal Action evidence did not reopen after append")
            saved, saved_receipt = reopened
            self._validate_terminal(saved, run_id, run["requested_run_id"], run["intent"], run["binding"], event)
            if saved_receipt != receipt:
                raise DirectActionJournalError("direct-action-journal-invalid", "reopened terminal receipt differs from append receipt")
            result_value = self._terminal_result(event, receipt)
            self.terminal[run_id] = result_value
            self.receipts.append(dict(receipt))
            return dict(result_value)
        finally:
            # A completed terminal append, an append failure retained as a
            # pending original event, and an invalid terminal input all end
            # this process-local invocation.  Another process may inspect or
            # recover, but never replay its unknown effect under this lock.
            self._release_invocation_lock()
            self._closed = True

    def recover_pending(self, event_id: str) -> Mapping[str, Any]:
        """Recover only the exact pending direct-Action Journal event bytes.

        This method cannot run an installer effect, create a replacement event,
        or infer an outcome.  It intentionally validates the sealed historic
        definition rather than reading the *current* O-180 source: source
        evolution cannot make the original Journal fact unrecoverable, nor can
        recovery admit a new execution under that historic source binding.
        """
        if not isinstance(event_id, str) or not event_id.startswith("direct-action:"):
            raise DirectActionJournalError("direct-action-pending-invalid", "event_id is not a direct Action event")
        try:
            _, event, _, _ = work_journal._read_pending_event(self.root, event_id)
        except work_journal.WorkJournalError as error:
            raise DirectActionJournalError("direct-action-pending-invalid", str(error)) from error
        binding = event.get("run", {}).get("definition")
        if (
            event.get("schema_version") != 5
            or event.get("kind") != "workflow_execution"
            or event.get("action_id") != self.action_id
            or event.get("event") not in {"started", "completed", "failed", "abandoned"}
            or event.get("author") != self.author
            or event.get("llm_session", {}).get("app") != DIRECT_ACTION_APP
            or event.get("structural_scope") != STRUCTURAL_SCOPE
            or event.get("initiative", {}).get("initiative_ref") != self.authorization["authorization_ref"]
            or event.get("initiative", {}).get("instruction_summary")
            != "Operator " + self.authorization["operator"]
            + " authorized " + self.descriptor.instruction + "; intent SHA-256 "
            + event.get("llm_session", {}).get("uuid", "")
            or event.get("run", {}).get("kind") != "action"
            or not isinstance(event.get("run", {}).get("run_id"), str)
            or not event["run"]["run_id"].startswith("direct-action:")
            or not isinstance(binding, Mapping)
            or set(binding) != {"atom_id", "version", "path", "digest"}
            or binding.get("atom_id") != self.descriptor.atom_id
            or binding.get("path") != self.descriptor.path.as_posix()
            or type(binding.get("version")) is not int
            or binding["version"] < 1
            or not isinstance(binding.get("digest"), str)
            or _SHA256.fullmatch(binding["digest"]) is None
            or event.get("definition_bindings")
            != [{"kind": "action", **dict(binding)}]
        ):
            raise DirectActionJournalError(
                "direct-action-pending-invalid",
                f"pending event does not belong to a sealed {self.descriptor.atom_id} direct Action recording",
            )
        try:
            receipt = work_journal.recover_pending_event(self.root, event_id)
        except work_journal.WorkJournalError as error:
            raise DirectActionJournalError("direct-action-recovery-failed", str(error)) from error
        self.receipts.append(dict(receipt))
        return {"event_id": event_id, "disposition": "recovered", "event_receipt": dict(receipt)}

    def _run_identity(self, requested_run_id: str, binding: Mapping[str, Any]) -> str:
        return work_journal.canonical_json_digest(
            {
                "action_id": self.action_id,
                "requested_run_id": requested_run_id,
                "binding": dict(binding),
                "project_root": str(self.root),
                "structural_scope": STRUCTURAL_SCOPE,
            }
        )

    def _intent_identity(self, intent: Mapping[str, str], binding: Mapping[str, Any]) -> str:
        return work_journal.canonical_json_digest(
            {
                "intent": dict(intent),
                "binding": dict(binding),
                "operator": self.authorization["operator"],
                "authorization_ref": self.authorization["authorization_ref"],
                "author": self.author,
            }
        )

    def _acquire_invocation_lock(self, requested_run_id: str, binding: Mapping[str, Any]) -> None:
        if self._invocation_locks:
            raise DirectActionJournalError("direct-action-invocation-active", "this session already holds a direct Action invocation lock")
        keys = (
            self._boundary_lock_key(),
            "direct-action-invocation:" + self._run_identity(requested_run_id, binding),
        )
        try:
            for key in keys:
                lock = work_journal._event_lock(self.root, key)
                lock.__enter__()
                self._invocation_locks.append((key, lock))
        except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
            self._release_invocation_lock()
            raise DirectActionJournalError(
                "direct-action-lock-unavailable",
                "direct Action boundary or this requested Action Run is already exclusively owned",
            ) from error

    def _release_invocation_lock(self) -> None:
        locks, self._invocation_locks = self._invocation_locks, []
        for _, lock in reversed(locks):
            lock.__exit__(None, None, None)

    def _first_initialization_lock_key(self) -> str:
        """One bootstrap boundary per Project, independent of requested Run ID."""
        return "direct-action-first-initialization:" + work_journal.canonical_json_digest(
            {
                "action_id": INITIALIZATION_ACTION_ID,
                "project_root": str(self.root),
                "structural_scope": STRUCTURAL_SCOPE,
            }
        )

    def _boundary_lock_key(self) -> str:
        if self.action_id == INITIALIZATION_ACTION_ID:
            return self._first_initialization_lock_key()
        return "direct-action-image-restoration:" + work_journal.canonical_json_digest(
            {"action_id": self.action_id, "project_root": str(self.root), "structural_scope": STRUCTURAL_SCOPE}
        )

    def _event(
        self,
        *,
        event_id: str,
        run_id: str,
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        event_name: str,
        outcome: str | None,
        result_ref: str | None,
        effect_refs: Sequence[str],
        report_ref: str | None,
    ) -> dict[str, Any]:
        moment = self._now()
        if moment.tzinfo is None:
            raise DirectActionJournalError("direct-action-journal-context-invalid", "clock must return a timezone-aware timestamp")
        if self.timezone == "UTC":
            moment = moment.astimezone(dt.UTC)
        payload: dict[str, Any] = {
            "schema_version": 5,
            "kind": "workflow_execution",
            "event_id": event_id,
            "action_id": self.action_id,
            "event": event_name,
            "author": self.author,
            "occurred_at": moment.isoformat(timespec="seconds"),
            "llm_session": {"app": DIRECT_ACTION_APP, "uuid": self._intent_identity(intent, binding)},
            "structural_scope": STRUCTURAL_SCOPE,
            "initiative": {
                "initiative_id": self.descriptor.atom_id,
                "instruction_summary": "Operator " + self.authorization["operator"]
                + " authorized " + self.descriptor.instruction + "; intent SHA-256 "
                + self._intent_identity(intent, binding),
                "initiative_ref": self.authorization["authorization_ref"],
            },
            "run": {
                "run_id": run_id,
                "kind": "action",
                "definition": {key: binding[key] for key in ("atom_id", "version", "path", "digest")},
            },
            "definition_bindings": [dict(binding)],
            "input_ref": self.authorization["authorization_ref"],
            "outcome": outcome,
            "result_ref": result_ref,
            "effect_refs": list(effect_refs),
            "report_ref": report_ref,
            "redaction": {"redacted": False, "fields": []},
        }
        return work_journal.with_event_digest(payload)

    def _context(self, event: Mapping[str, Any]) -> dict[str, Any]:
        occurred_at = dt.datetime.fromisoformat(str(event["occurred_at"]))
        try:
            return work_journal.seal_append_context(
                self.root,
                event,
                author=self.author,
                local_date=occurred_at.date().isoformat(),
                timezone=self.timezone,
            )
        except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
            raise DirectActionJournalError("direct-action-journal-unavailable", "cannot seal canonical Journal append context") from error

    def _append(self, event: Mapping[str, Any], *, result_ref: str | None, effect_refs: list[str]) -> dict[str, Any]:
        context = self._context(event)
        try:
            return work_journal.append_sealed_events(
                self.root,
                [event],
                author=context["author"],
                local_date=context["local_date"],
                timezone=context["timezone"],
                append_context=context,
            )[0]
        except OSError as error:
            try:
                work_journal.store_pending_event(
                    self.root,
                    event,
                    context,
                    result_ref=result_ref,
                    effect_refs=effect_refs,
                    diagnostic="direct Action Journal append failure",
                )
            except (OSError, RuntimeError, work_journal.WorkJournalError) as pending_error:
                raise DirectActionJournalError(
                    "direct-action-recording-unrecoverable",
                    "Journal append failed and original event recovery evidence could not be stored",
                ) from pending_error
            self.pending[str(event["event_id"])] = {
                "event": dict(event),
                "context": context,
                "run_id": event["run"]["run_id"],
            }
            raise DirectActionJournalError(
                "direct-action-recording-pending",
                f"canonical Journal append failed; recover only original event {event['event_id']}",
            ) from error
        except work_journal.WorkJournalError as error:
            # A deterministic identity collision is safe only when reopening
            # proves the recorded event is the exact expected one.  The caller
            # does that immediately after this helper returns or raises.
            raise DirectActionJournalError("direct-action-journal-rejected", str(error)) from error

    def _existing_terminal(
        self,
        identity: str,
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        run_id: str,
    ) -> tuple[dict[str, Any], dict[str, Any]] | None:
        prefix = f"direct-action:{identity}:terminal:"
        found: tuple[dict[str, Any], dict[str, Any]] | None = None
        for path in _journal_parts(self.root):
            try:
                raw = path.read_bytes()
            except OSError as error:
                raise DirectActionJournalError("direct-action-journal-unavailable", f"cannot reopen {path.name}") from error
            for line in raw.splitlines():
                try:
                    event_id = json.loads(line).get("event_id")
                except (AttributeError, json.JSONDecodeError) as error:
                    raise DirectActionJournalError("direct-action-journal-invalid", f"invalid Journal record in {path.name}") from error
                if isinstance(event_id, str) and event_id.startswith(prefix):
                    candidate = _reopen_event(self.root, event_id)
                    if candidate is None:
                        raise DirectActionJournalError("direct-action-journal-invalid", "terminal event disappeared during reopen")
                    event, receipt = candidate
                    self._validate_terminal_shape(event, run_id, requested_run_id, intent, binding)
                    if found is not None:
                        raise DirectActionJournalError("direct-action-journal-invalid", "one direct Action has conflicting terminal evidence")
                    found = (event, receipt)
        return found

    def _pending_event(self, event_id: str) -> dict[str, Any] | None:
        """Return the exact sealed pending event, if one exists, without retrying it."""
        try:
            _, event, _, _ = work_journal._read_pending_event(self.root, event_id)
        except work_journal.WorkJournalError as error:
            if error.code == "pending-not-found":
                return None
            raise DirectActionJournalError("direct-action-pending-invalid", str(error)) from error
        return event

    def _validate_started(
        self,
        event: Mapping[str, Any],
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        run_id: str,
    ) -> None:
        if event.get("event") != "started" or event.get("outcome") is not None:
            raise DirectActionJournalError("direct-action-journal-invalid", "reopened event is not a started direct Action")
        self._validate_terminal_shape(event, run_id, requested_run_id, intent, binding, allow_nonterminal=True)

    def _validate_terminal(
        self,
        event: Mapping[str, Any],
        run_id: str,
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        expected: Mapping[str, Any],
    ) -> None:
        self._validate_terminal_shape(event, run_id, requested_run_id, intent, binding)
        if dict(event) != dict(expected):
            raise DirectActionJournalError("direct-action-journal-invalid", "reopened terminal evidence does not match this Action result")

    def _validate_terminal_shape(
        self,
        event: Mapping[str, Any],
        run_id: str,
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        *,
        allow_nonterminal: bool = False,
    ) -> None:
        expected_intent_identity = self._intent_identity(intent, binding)
        actual_session = event.get("llm_session")
        if (
            isinstance(actual_session, Mapping)
            and actual_session.get("app") == DIRECT_ACTION_APP
            and event.get("run", {}).get("run_id") == run_id
            and actual_session.get("uuid") != expected_intent_identity
        ):
            raise DirectActionJournalError(
                "direct-action-intent-conflict",
                "requested_run_id already binds a different immutable direct Action intent",
            )
        if (
            event.get("schema_version") != 5
            or event.get("kind") != "workflow_execution"
            or event.get("action_id") != self.action_id
            or event.get("author") != self.author
            or event.get("llm_session") != {"app": DIRECT_ACTION_APP, "uuid": expected_intent_identity}
            or event.get("structural_scope") != STRUCTURAL_SCOPE
            or event.get("initiative") != {
                "initiative_id": self.descriptor.atom_id,
                "instruction_summary": "Operator " + self.authorization["operator"]
                + " authorized " + self.descriptor.instruction + "; intent SHA-256 "
                + expected_intent_identity,
                "initiative_ref": self.authorization["authorization_ref"],
            }
            or event.get("run") != {
                "run_id": run_id,
                "kind": "action",
                "definition": {key: binding[key] for key in ("atom_id", "version", "path", "digest")},
            }
            or event.get("definition_bindings") != [dict(binding)]
            or event.get("input_ref") != self.authorization["authorization_ref"]
        ):
            raise DirectActionJournalError("direct-action-journal-invalid", "reopened Journal event does not bind this direct Action")
        if not allow_nonterminal and event.get("event") not in {"completed", "failed", "abandoned"}:
            raise DirectActionJournalError("direct-action-journal-invalid", "reopened Journal event is not terminal direct Action evidence")

    @staticmethod
    def _effect_refs(value: object) -> list[str]:
        if not isinstance(value, list) or len(set(value)) != len(value):
            raise DirectActionJournalError("direct-action-invalid-effects", "effect_refs must be a duplicate-free list")
        return [str(_safe_ref(item, "effect_ref")) for item in value]

    def _require_open_run(self, run_id: str) -> dict[str, Any]:
        if self._closed or not self._invocation_locks:
            raise DirectActionJournalError("direct-action-invocation-closed", "direct Action invocation no longer holds its exclusive lock")
        if not isinstance(run_id, str) or run_id not in self.actual:
            raise DirectActionJournalError("direct-action-unknown-run", "Action Run is not started by this session")
        if run_id in self.terminal or any(item.get("run_id") == run_id for item in self.pending.values()):
            raise DirectActionJournalError("direct-action-terminal", "Action Run already has terminal or pending Journal evidence")
        return self.actual[run_id]

    @staticmethod
    def _terminal_result(event: Mapping[str, Any], receipt: Mapping[str, Any]) -> dict[str, Any]:
        return {
            "event_id": event["event_id"],
            "run_id": event["run"]["run_id"],
            "disposition": "terminal",
            "outcome": event["outcome"],
            "result_ref": event["result_ref"],
            "effect_refs": list(event["effect_refs"]),
            "report_ref": event["report_ref"],
            "event_receipt": dict(receipt),
        }


__all__ = [
    "ACTION_ATOM_ID",
    "ACTION_ATOM_RELATIVE",
    "ACTION_ATOM_SHA256",
    "ACTION_ATOM_VERSION",
    "DIRECT_ACTION_APP",
    "DirectActionJournalError",
    "DirectActionSession",
    "INITIALIZATION_ACTION_ID",
    "RESTORATION_ACTION_ID",
    "RESTORATION_ATOM_ID",
    "RESTORATION_ATOM_RELATIVE",
    "RESTORATION_ATOM_SHA256",
    "RESTORATION_ATOM_VERSION",
]
