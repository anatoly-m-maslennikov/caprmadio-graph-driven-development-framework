"""Trusted, Journal-backed lifecycle for one Release manifest publication.

This module owns neither a Workflow Run nor a private lifecycle ledger.  It
adapts the publisher to the existing generic Work Journal and to the opaque,
host-created publication authorization context.
"""
from __future__ import annotations

from contextlib import contextmanager
import re
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from typing import Any, Mapping

MCP = Path(__file__).resolve().parent
TOOLS = MCP.parent / "201_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import work_journal  # noqa: E402
from release_manifest_authorization import (  # noqa: E402
    PublicationAuthorizationContext,
    ReleaseManifestAuthorizationError,
    validate_candidate_payload,
    validate_publication_context,
)
from selected_routes import SELECTED_ROUTE_NAMES, SelectedRouteError, load_selected_manifest  # noqa: E402


ACTION_ID = "MCP_RELEASE_MANIFEST_PUBLICATION"
STRUCTURAL_SCOPE = "MCP"
_INTENT_PREFIX = "release-manifest-publication:"
_GIT_COMMIT = re.compile(r"[0-9a-f]{40,64}")


class ReleaseManifestLifecycleError(RuntimeError):
    """The trusted Release manifest lifecycle could not continue truthfully."""


def _root(value: str | Path) -> Path:
    try:
        root = Path(value).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise ReleaseManifestLifecycleError("project root is unavailable") from error
    if root.is_symlink() or not root.is_dir():
        raise ReleaseManifestLifecycleError("project root is unavailable")
    return root


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _safe_ref(value: object, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise ReleaseManifestLifecycleError(f"{label} must be a non-empty repository-relative reference")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ReleaseManifestLifecycleError(f"{label} must be repository-relative")
    return value


def _digest(value: object, label: str) -> str:
    if not isinstance(value, str) or work_journal.SHA256_RE.fullmatch(value) is None:
        raise ReleaseManifestLifecycleError(f"{label} must be a lowercase SHA-256 digest")
    return value


def _normalized_plan(plan: Mapping[str, Any]) -> dict[str, Any]:
    required = {
        "manifest_ref", "observed_input_sha256", "current_route_names", "candidate_route_names",
        "candidate_canonical_manifest_sha256", "added_route", "added_admission_route", "candidate_byte_count",
    }
    if (
        not isinstance(plan, Mapping)
        or not required <= set(plan)
        or set(plan) - required - {"mode"}
        or ("mode" in plan and plan["mode"] != "plan")
    ):
        raise ReleaseManifestLifecycleError("publication plan has missing or unsupported fields")
    result = {key: plan[key] for key in required}
    result["manifest_ref"] = _safe_ref(result["manifest_ref"], "plan.manifest_ref")
    result["observed_input_sha256"] = _digest(result["observed_input_sha256"], "plan.observed_input_sha256")
    result["candidate_canonical_manifest_sha256"] = _digest(
        result["candidate_canonical_manifest_sha256"], "plan.candidate_canonical_manifest_sha256"
    )
    if result["current_route_names"] != list(SELECTED_ROUTE_NAMES) or result["candidate_route_names"] != [*SELECTED_ROUTE_NAMES, "release_version"]:
        raise ReleaseManifestLifecycleError("publication plan does not describe the admitted fifteen-to-sixteen route successor")
    if result["added_route"] != "release_version" or result["added_admission_route"] != "release_version":
        raise ReleaseManifestLifecycleError("publication plan does not describe the admitted Release addition")
    if type(result["candidate_byte_count"]) is not int or result["candidate_byte_count"] < 1:
        raise ReleaseManifestLifecycleError("publication plan has invalid candidate byte count")
    return result


def _intent_base(plan: Mapping[str, Any], context: PublicationAuthorizationContext) -> dict[str, Any]:
    normalized = _normalized_plan(plan)
    return {
        "plan": normalized,
        "source_frontier_digest": _digest(context.source_frontier_digest, "context.source_frontier_digest"),
        "authority_digest": _digest(context.authority_digest, "context.authority_digest"),
    }


def _canonical_intent(plan: Mapping[str, Any], context: PublicationAuthorizationContext, payload: bytes) -> dict[str, Any]:
    if not isinstance(payload, bytes):
        raise ReleaseManifestLifecycleError("candidate publication payload must be bytes")
    return {**_intent_base(plan, context), "candidate_payload_sha256": _sha256(payload)}


def _pending_diagnostic(intent: Mapping[str, Any]) -> str:
    return _INTENT_PREFIX + work_journal.canonical_json_bytes(dict(intent)).decode("utf-8")


def _read_intent(value: Mapping[str, Any]) -> dict[str, Any]:
    diagnostic = value.get("diagnostic")
    if not isinstance(diagnostic, str) or not diagnostic.startswith(_INTENT_PREFIX):
        raise ReleaseManifestLifecycleError("pending publication intent is not owned by this lifecycle")
    try:
        decoded = json.loads(diagnostic.removeprefix(_INTENT_PREFIX))
    except json.JSONDecodeError as error:
        raise ReleaseManifestLifecycleError("pending publication intent is invalid") from error
    if not isinstance(decoded, dict) or set(decoded) != {
        "plan", "source_frontier_digest", "authority_digest", "candidate_payload_sha256",
    }:
        raise ReleaseManifestLifecycleError("pending publication intent has unsupported fields")
    return {
        "plan": _normalized_plan(decoded["plan"]),
        "source_frontier_digest": _digest(decoded["source_frontier_digest"], "pending.source_frontier_digest"),
        "authority_digest": _digest(decoded["authority_digest"], "pending.authority_digest"),
        "candidate_payload_sha256": _digest(
            decoded["candidate_payload_sha256"], "pending.candidate_payload_sha256"
        ),
    }


def _event_id(root: Path, intent: Mapping[str, Any], previous_event: str) -> str:
    return "release-manifest:" + work_journal.canonical_json_digest(
        {"action_id": ACTION_ID, "root": str(root), "intent": dict(intent), "previous_result_event": previous_event}
    )


def _now() -> dt.datetime:
    return dt.datetime.now().astimezone()


class ReleaseManifestLifecycle:
    """One trusted lifecycle adapter injected into the manifest publisher."""

    def __init__(self, project_root: str | Path, context: PublicationAuthorizationContext) -> None:
        self.root = _root(project_root)
        self.context = context
        self._held_carrier_lock: str | None = None

    def authorize_release_manifest_publication(self, plan: Mapping[str, Any], authorization: object) -> bool:
        """Refresh opaque host authority; caller data cannot self-grant access."""
        if authorization is not self.context:
            return False
        try:
            validate_publication_context(self.context, self.root, dict(plan))
        except (ReleaseManifestAuthorizationError, OSError, TypeError, ValueError):
            return False
        return True

    @contextmanager
    def release_manifest_publication_lock(self, plan: Mapping[str, Any]):
        """Hold the one generic Journal carrier lock for a publisher attempt.

        The scope is lifecycle-owned: callers cannot assert that a lock is
        held.  It may span prepare, final freshness checks, and the publisher's
        atomic replacement without creating a second lock or state carrier.
        """
        manifest_ref = _normalized_plan(plan)["manifest_ref"]
        lock_id = "release-manifest-carrier:" + manifest_ref
        if self._held_carrier_lock is not None:
            raise ReleaseManifestLifecycleError("a Release manifest publication lock is already held")
        entered = False
        try:
            with work_journal._event_lock(self.root, lock_id):
                entered = True
                self._held_carrier_lock = lock_id
                try:
                    yield
                finally:
                    self._held_carrier_lock = None
        except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
            # Do not recast a publisher failure from inside the protected
            # scope as a lock-acquisition failure.  The caller needs that
            # original failure to report an honest pre-effect result.
            if entered:
                raise
            raise ReleaseManifestLifecycleError("cannot acquire Release manifest publication lock") from error

    def prepare_release_manifest_publication(self, plan: Mapping[str, Any], payload: bytes) -> str:
        """Persist the exact successor event before the publisher replaces bytes.

        A publisher can use :meth:`release_manifest_publication_lock` to span
        prepare through its atomic write.  Callers without that lifecycle-owned
        scope retain the self-locking default.
        """
        self._validate_payload(plan, payload)
        intent = _canonical_intent(plan, self.context, payload)
        sealed_plan = intent["plan"]
        path = self.root / sealed_plan["manifest_ref"]
        lock_id = "release-manifest-carrier:" + sealed_plan["manifest_ref"]
        if self._held_carrier_lock == lock_id:
            return self._prepare_release_manifest_publication_locked(plan, payload, intent, path)
        if self._held_carrier_lock is not None:
            raise ReleaseManifestLifecycleError("a different Release manifest publication lock is held")
        try:
            # Reuse the Journal's existing cross-process event lock.  A
            # carrier-wide lock prevents two trusted contexts from producing
            # unequal timestamped pending bytes for one manifest binding.
            with work_journal._event_lock(self.root, lock_id):
                return self._prepare_release_manifest_publication_locked(plan, payload, intent, path)
        except ReleaseManifestLifecycleError:
            # A verified lifecycle refusal (for example, malformed history
            # for this exact carrier) is not a Journal persistence failure.
            raise
        except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
            raise ReleaseManifestLifecycleError("cannot persist sealed publication intent") from error

    def _prepare_release_manifest_publication_locked(
        self,
        plan: Mapping[str, Any],
        payload: bytes,
        intent: Mapping[str, Any],
        path: Path,
    ) -> str:
        """Prepare one intent while the caller owns the carrier serialization lock."""
        sealed_plan = intent["plan"]
        # Validation must be fresh after waiting for another publisher.
        self._validate_candidate_payload(plan, payload)
        if _sha256(path.read_bytes()) != sealed_plan["observed_input_sha256"]:
            raise ReleaseManifestLifecycleError("selected manifest input changed before publication intent")
        existing = self._pending_for_binding(intent)
        if existing is not None:
            return existing
        previous_event, prior_version = self._prior_history(path)
        if previous_event is None:
            previous_event, prior_version = self._record_recovered_prior(path)
        event = self._successor_event(intent, payload, previous_event, prior_version + 1)
        context = self._append_context(event)
        try:
            work_journal.store_pending_event(
                self.root,
                event,
                context,
                result_ref=sealed_plan["manifest_ref"],
                effect_refs=[sealed_plan["manifest_ref"]],
                diagnostic=_pending_diagnostic(intent),
                retry_linkage=work_journal.canonical_json_digest(intent),
            )
        except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
            raise ReleaseManifestLifecycleError("cannot persist sealed publication intent") from error
        return str(event["event_id"])

    def record_release_manifest_publication(self, result: Mapping[str, Any]) -> dict[str, str]:
        """Finalize only the pre-effect event after exact published-byte proof."""
        plan = self._plan_from_result(result)
        event_id, intent = self._event_id_for_plan(plan)
        receipt = self._recover_if_exact(event_id, plan, intent)
        return {
            "recording_ref": "journal:" + str(receipt["event_id"]),
            "candidate_canonical_manifest_sha256": intent["plan"]["candidate_canonical_manifest_sha256"],
        }

    def _plan_from_result(self, result: Mapping[str, Any]) -> dict[str, Any]:
        if not isinstance(result, Mapping) or result.get("mode") != "execute" or result.get("published") is not True:
            raise ReleaseManifestLifecycleError("publication result is not a verified execute result")
        plan = {key: result[key] for key in (
            "manifest_ref", "observed_input_sha256", "current_route_names", "candidate_route_names",
            "candidate_canonical_manifest_sha256", "added_route", "added_admission_route", "candidate_byte_count",
        ) if key in result}
        return _normalized_plan(plan)

    def recover_release_manifest_publication(self, event_id: str) -> dict[str, Any]:
        """Recover only exact pending evidence; never replay a manifest replacement."""
        try:
            pending, event, _, _ = work_journal._read_pending_event(self.root, event_id)
        except work_journal.WorkJournalError as error:
            raise ReleaseManifestLifecycleError("pending publication intent is unavailable") from error
        intent = _read_intent(pending)
        plan = dict(intent["plan"])
        expected_id = _event_id(self.root, intent, str(event["previous_result_event"]))
        if event_id != expected_id:
            raise ReleaseManifestLifecycleError("pending publication event identity is not canonical")
        receipt = self._recover_if_exact(event_id, plan, intent)
        return {"event_id": event_id, "disposition": "recovered", "event_receipt": dict(receipt)}

    def _validate_context(self, plan: Mapping[str, Any], *, manifest_state: str = "input") -> None:
        try:
            validated = validate_publication_context(
                self.context, self.root, dict(_normalized_plan(plan)), manifest_state=manifest_state,
            )
        except (ReleaseManifestAuthorizationError, OSError, TypeError, ValueError) as error:
            if manifest_state == "candidate":
                raise ReleaseManifestLifecycleError(
                    "published selected manifest is ambiguous; mutation will not be replayed"
                ) from error
            raise ReleaseManifestLifecycleError("trusted publication authority is unavailable or stale") from error
        if validated is not self.context:
            raise ReleaseManifestLifecycleError("trusted publication authority changed unexpectedly")

    def _validate_payload(self, plan: Mapping[str, Any], payload: bytes) -> None:
        if not isinstance(payload, bytes) or not payload:
            raise ReleaseManifestLifecycleError("candidate publication payload must be non-empty bytes")
        if len(payload) != _normalized_plan(plan)["candidate_byte_count"]:
            raise ReleaseManifestLifecycleError("candidate publication payload has a different byte count from the plan")
        try:
            document = json.loads(payload)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ReleaseManifestLifecycleError("candidate publication payload is not JSON") from error
        if not isinstance(document, dict) or document.get("canonical_manifest_sha256") != plan.get("candidate_canonical_manifest_sha256"):
            raise ReleaseManifestLifecycleError("candidate publication payload is not bound to the exact plan")

    def _validate_candidate_payload(self, plan: Mapping[str, Any], payload: bytes) -> None:
        try:
            validate_candidate_payload(self.context, self.root, dict(_normalized_plan(plan)), payload)
        except (ReleaseManifestAuthorizationError, OSError, TypeError, ValueError) as error:
            raise ReleaseManifestLifecycleError("candidate publication payload is not bound to trusted authority") from error

    def _prior_history(self, path: Path) -> tuple[str | None, int]:
        try:
            journal_root = self.root / work_journal.configured_journal_root(self.root)
        except (OSError, RuntimeError) as error:
            raise ReleaseManifestLifecycleError("canonical Work Journal is unavailable") from error
        reference = path.relative_to(self.root).as_posix()
        found: tuple[str, int, str] | None = None
        for carrier in sorted(journal_root.glob("*.ndjson")) if journal_root.exists() else []:
            if carrier.is_symlink() or not carrier.is_file():
                continue
            try:
                records = carrier.read_text(encoding="utf-8").splitlines()
            except OSError as error:
                raise ReleaseManifestLifecycleError("cannot read canonical Work Journal history") from error
            for line in records:
                try:
                    raw = json.loads(line)
                except json.JSONDecodeError as error:
                    raise ReleaseManifestLifecycleError("canonical Work Journal history is invalid") from error
                # The Journal contains more than generic governed-project
                # state: legacy and Workflow execution events carry their
                # own schemas.  Only a schema-3 generic record that claims
                # this exact carrier can establish its carrier history.  An
                # unrelated record is not evidence about this target and is
                # intentionally not parsed by the generic-state validator.
                raw_result = raw.get("result") if isinstance(raw, dict) else None
                if not isinstance(raw_result, dict) or raw_result.get("path") != reference:
                    continue
                if (
                    raw.get("schema_version") != 3
                    or raw.get("kind") not in {"governed_project_state", "governed_project_change"}
                ):
                    # A record that asserts this exact carrier is potential
                    # lineage evidence.  It must not disappear merely by
                    # naming an unsupported schema or kind.
                    raise ReleaseManifestLifecycleError(
                        "canonical Work Journal history has unsupported target carrier evidence"
                    )
                try:
                    record = work_journal.validate_sealed_event(raw)
                except work_journal.WorkJournalError as error:
                    raise ReleaseManifestLifecycleError("canonical Work Journal history is invalid") from error
                result = record["result"]
                if result.get("state") != "present":
                    continue
                version = result.get("version")
                if type(version) is not int or version < 1:
                    raise ReleaseManifestLifecycleError("canonical Work Journal history has invalid carrier version")
                candidate = (str(record["event_id"]), version, str(result.get("sha256")))
                if found is None or candidate[1] > found[1]:
                    found = candidate
                elif candidate[1] == found[1] and candidate != found:
                    raise ReleaseManifestLifecycleError("canonical Work Journal history has conflicting carrier revisions")
        if found is None:
            return None, 0
        if _sha256(path.read_bytes()) != found[2]:
            raise ReleaseManifestLifecycleError("canonical Work Journal history does not match selected manifest bytes")
        return found[0], found[1]

    def _record_recovered_prior(self, path: Path) -> tuple[str, int]:
        payload = path.read_bytes()
        result = {
            "state": "present",
            "filename": path.name,
            "version": 1,
            "path": path.relative_to(self.root).as_posix(),
            "sha256": _sha256(payload),
        }
        evidence = {
            "carrier": {"identity": "selected_workflow_bindings", "kind": "file", "filename": path.name,
                        "version": 1, "sha256": result["sha256"]},
            **self._working_tree_or_git_evidence(path, payload),
        }
        core = {
            "schema_version": 3,
            "action_id": ACTION_ID,
            "event": "recovered",
            "kind": "governed_project_state",
            "subject_kind": "file",
            "author": self.context.journal_author,
            "occurred_at": self._occurred_at(),
            "llm_session": dict(self.context.llm_session),
            "structural_scope": STRUCTURAL_SCOPE,
            "result": result,
            "recovery_evidence": evidence,
        }
        event = {"event_id": "release-manifest-state:" + work_journal.canonical_json_digest(evidence), **core}
        event = work_journal.with_event_digest(event)
        context = self._append_context(event)
        try:
            work_journal.append_sealed_events(
                self.root, [event], author=context["author"], local_date=context["local_date"],
                timezone=context["timezone"], append_context=context,
            )
        except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
            raise ReleaseManifestLifecycleError("cannot record recovered prior selected manifest state") from error
        return str(event["event_id"]), 1

    def _successor_event(self, intent: Mapping[str, Any], payload: bytes, previous_event: str, version: int) -> dict[str, Any]:
        core = {
            "schema_version": 3,
            "action_id": ACTION_ID,
            "event": "completed",
            "kind": "governed_project_change",
            "subject_kind": "file",
            "author": self.context.journal_author,
            "occurred_at": self._occurred_at(),
            "llm_session": dict(self.context.llm_session),
            "structural_scope": STRUCTURAL_SCOPE,
            "action_type": "UPDATE",
            "sources": [],
            "result": {
                "state": "present", "filename": Path(intent["plan"]["manifest_ref"]).name, "version": version,
                "path": intent["plan"]["manifest_ref"], "sha256": _sha256(payload),
            },
            "previous_result_event": previous_event,
        }
        event = {"event_id": _event_id(self.root, intent, previous_event), **core}
        return work_journal.with_event_digest(event)

    def _pending_for_binding(self, intent: Mapping[str, Any]) -> str | None:
        """Return one exact pre-effect retry, or reject another live binding."""
        pending_root = self.root / work_journal.configured_runtime_root(self.root) / "state" / "work_journal" / "pending"
        matches: list[str] = []
        competing: list[str] = []
        for candidate in sorted(pending_root.glob("release-manifest:*.json")) if pending_root.exists() else []:
            try:
                pending, event, _, _ = work_journal._read_pending_event(self.root, candidate.stem)
                pending_intent = _read_intent(pending)
                if pending_intent == dict(intent):
                    expected_id = _event_id(self.root, pending_intent, str(event["previous_result_event"]))
                    if candidate.stem != expected_id or event["result"].get("sha256") != pending_intent["candidate_payload_sha256"]:
                        raise ReleaseManifestLifecycleError("pending publication intent has inconsistent sealed binding")
                    matches.append(candidate.stem)
                elif pending_intent["plan"]["manifest_ref"] == intent["plan"]["manifest_ref"]:
                    competing.append(candidate.stem)
            except work_journal.WorkJournalError:
                raise ReleaseManifestLifecycleError("pending publication intent is invalid") from None
        if competing:
            raise ReleaseManifestLifecycleError("a different sealed publication intent is already pending")
        if len(matches) != 1:
            if len(matches) > 1:
                raise ReleaseManifestLifecycleError("multiple identical pending publication intents are unavailable")
            return None
        return matches[0]

    def _event_id_for_plan(self, plan: Mapping[str, Any]) -> tuple[str, dict[str, Any]]:
        """Find the sole immutable pending binding for a publisher result."""
        base = _intent_base(plan, self.context)
        pending_root = self.root / work_journal.configured_runtime_root(self.root) / "state" / "work_journal" / "pending"
        matches: list[tuple[str, dict[str, Any]]] = []
        for candidate in sorted(pending_root.glob("release-manifest:*.json")) if pending_root.exists() else []:
            try:
                pending, event, _, _ = work_journal._read_pending_event(self.root, candidate.stem)
                intent = _read_intent(pending)
            except work_journal.WorkJournalError:
                raise ReleaseManifestLifecycleError("pending publication intent is invalid") from None
            if {key: intent[key] for key in base} != base:
                continue
            expected_id = _event_id(self.root, intent, str(event["previous_result_event"]))
            if candidate.stem != expected_id or event["result"].get("sha256") != intent["candidate_payload_sha256"]:
                raise ReleaseManifestLifecycleError("pending publication intent has inconsistent sealed binding")
            matches.append((candidate.stem, intent))
        if len(matches) != 1:
            raise ReleaseManifestLifecycleError("exact pending publication intent is unavailable")
        return matches[0]

    def _recover_if_exact(self, event_id: str, plan: Mapping[str, Any], intent: Mapping[str, Any]) -> dict[str, Any]:
        try:
            _, pending_event, _, _ = work_journal._read_pending_event(self.root, event_id)
        except work_journal.WorkJournalError as error:
            raise ReleaseManifestLifecycleError("sealed publication intent is unavailable") from error
        path = self.root / intent["plan"]["manifest_ref"]
        try:
            payload = path.read_bytes()
        except OSError as error:
            raise ReleaseManifestLifecycleError("published selected manifest is unavailable") from error
        try:
            document = json.loads(payload)
        except (UnicodeDecodeError, json.JSONDecodeError, OSError, ValueError) as error:
            raise ReleaseManifestLifecycleError("published selected manifest cannot be reopened") from error
        if (
            not isinstance(document, dict)
            or _sha256(payload) != pending_event.get("result", {}).get("sha256")
            or document.get("canonical_manifest_sha256") != intent["plan"]["candidate_canonical_manifest_sha256"]
        ):
            raise ReleaseManifestLifecycleError("published selected manifest is ambiguous; mutation will not be replayed")
        self._validate_context(plan, manifest_state="candidate")
        try:
            loaded = load_selected_manifest(self.root)
        except (OSError, ValueError, SelectedRouteError) as error:
            raise ReleaseManifestLifecycleError("published selected manifest cannot be reopened") from error
        if [row.get("route") for row in loaded.get("routes", [])] != [*SELECTED_ROUTE_NAMES, "release_version"]:
            raise ReleaseManifestLifecycleError("published selected manifest is ambiguous; mutation will not be replayed")
        try:
            return work_journal.recover_pending_event(self.root, event_id)
        except work_journal.WorkJournalError as error:
            raise ReleaseManifestLifecycleError("cannot finalize sealed publication evidence") from error

    def _occurred_at(self) -> str:
        moment = _now()
        if moment.tzinfo is None or moment.utcoffset() is None:
            raise ReleaseManifestLifecycleError("Journal clock must be timezone-aware")
        return moment.isoformat(timespec="seconds")

    def _append_context(self, event: Mapping[str, Any]) -> dict[str, Any]:
        occurred = dt.datetime.fromisoformat(str(event["occurred_at"]))
        timezone = occurred.tzname() or occurred.strftime("%z")
        try:
            return work_journal.seal_append_context(
                self.root, event, author=self.context.journal_author,
                local_date=occurred.date().isoformat(), timezone=timezone,
            )
        except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
            raise ReleaseManifestLifecycleError("cannot seal canonical Journal append context") from error

    def _working_tree_or_git_evidence(self, path: Path, payload: bytes) -> dict[str, Any]:
        """Never attribute dirty observed bytes to the current Git commit."""
        relative = path.relative_to(self.root).as_posix()
        # Schema 3 requires a non-empty ``git`` evidence mapping for a
        # recovered state.  Its metadata is deliberately explicit when Git
        # cannot prove these exact observed bytes: no commit is claimed.
        working = {
            "git": {
                "provenance": "working_tree_only",
                "path": relative,
                "sha256": _sha256(payload),
            }
        }
        try:
            head = subprocess.run(
                ["git", "-C", str(self.root), "rev-parse", "HEAD"], text=True,
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False,
            )
            commit = head.stdout.strip()
            if head.returncode != 0 or _GIT_COMMIT.fullmatch(commit) is None:
                return working
            show = subprocess.run(
                ["git", "-C", str(self.root), "show", f"HEAD:{relative}"], text=False,
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False,
            )
        except OSError:
            return working
        committed = show.stdout.encode("utf-8") if isinstance(show.stdout, str) else show.stdout
        if show.returncode == 0 and isinstance(committed, bytes) and committed == payload:
            return {"git": {"commit": commit, "path": relative, "sha256": _sha256(payload)}}
        return working


__all__ = ["ReleaseManifestLifecycle", "ReleaseManifestLifecycleError"]
