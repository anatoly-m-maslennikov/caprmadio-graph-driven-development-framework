"""Red contract tests for the one-shot N15 unknown-effect resolver.

The public boundary is deliberately filesystem-rooted so production uses the
same sealed carriers as the existing Release recovery entry point.  These
tests use only temporary roots: no live N15 Run, Journal, DBOS, Docker, or
Release effect is opened by this suite.
"""
from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from unittest import mock
from contextlib import nullcontext
import json
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import release_unknown_effect_resolution as resolver  # noqa: E402
from contracts import ResolveReleaseUnknownEffect  # noqa: E402


RUN_ID = "release-epic-resume-20261006-N15"
IDENTITY = "5228bc2214ef3868794ae48f12c435c266587fd856fcefdd4598612b3ba80ec4"
AUTHORIZATION_REF = ".caprmedio_caprmedio/01_concern/CA-C-517-QUESTION--resolve-the-unknown-n15-unit-outcome.md"
AUTHORIZATION_SHA256 = "1d3d7c3c1d10827362952d684193fe844e634d18dfa5098a32f54af4863974d4"
CHECKPOINT_SHA256 = "71d93f97c0f07b84e94d49d5bd18a4ab83d86e3e52d00e39368ce881153a4344"


def _request(**changes: str) -> dict[str, str]:
    request = {
        "operation": "resolve_release_unknown_effect",
        "run_id": RUN_ID,
        "request_identity": IDENTITY,
        "authorization_ref": AUTHORIZATION_REF,
        "authorization_sha256": AUTHORIZATION_SHA256,
        "expected_checkpoint_sha256": CHECKPOINT_SHA256,
    }
    request.update(changes)
    return request


class ReleaseUnknownEffectResolutionTests(unittest.TestCase):
    """The resolver may terminalize history once, but never perform an effect."""

    def _temporary_root(self) -> tempfile.TemporaryDirectory[str]:
        return tempfile.TemporaryDirectory(prefix="n15-unknown-effect-", dir="/private/tmp", ignore_cleanup_errors=True)

    def test_six_key_variant_is_closed_before_any_carrier_or_effect_access(self) -> None:
        """Missing, extra, or ordinary-recovery-shaped requests are blocked."""
        malformed = [
            {key: value for key, value in _request().items() if key != "authorization_sha256"},
            {**_request(), "old_effect": "replay"},
            {"operation": "recover_selected_release", "run_id": RUN_ID, "request_identity": IDENTITY},
        ]
        with self._temporary_root() as temporary:
            root = Path(temporary)
            with mock.patch("subprocess.run") as run, \
                 mock.patch.object(resolver.work_journal, "_event_lock", side_effect=lambda *_args: nullcontext()):
                for request in malformed:
                    with self.subTest(request=request):
                        result = resolver.resolve_release_unknown_effect(root, request)
                        self.assertEqual(
                            {"operation", "run_id", "disposition", "blocked_reason"}, set(result), result,
                        )
                        self.assertEqual("blocked", result["disposition"])
                run.assert_not_called()

    def test_six_key_contract_never_retypes_ordinary_recovery(self) -> None:
        accepted = ResolveReleaseUnknownEffect.model_validate(_request())
        self.assertEqual("resolve_release_unknown_effect", accepted.operation)
        self.assertEqual(RUN_ID, accepted.run_id)
        with self.assertRaises(ValueError):
            ResolveReleaseUnknownEffect.model_validate({**_request(), "effect": "retry"})
        with self.assertRaises(ValueError):
            ResolveReleaseUnknownEffect.model_validate({
                "operation": "recover_selected_release", "run_id": RUN_ID,
                "request_identity": IDENTITY,
            })

    def test_checkpoint_or_authorization_change_blocks_before_replay_or_history_mutation(self) -> None:
        """Caller-supplied seals cannot turn the resolver into ordinary recovery."""
        changed = (
            _request(expected_checkpoint_sha256="0" * 64),
            _request(authorization_sha256="0" * 64),
            _request(request_identity="0" * 64),
        )
        with self._temporary_root() as temporary:
            root = Path(temporary)
            with mock.patch("subprocess.run") as run, \
                 mock.patch.object(resolver.work_journal, "_event_lock", side_effect=lambda *_args: nullcontext()):
                for request in changed:
                    with self.subTest(request=request):
                        result = resolver.resolve_release_unknown_effect(root, request)
                        self.assertEqual("blocked", result["disposition"])
                        self.assertEqual({"operation", "run_id", "disposition", "blocked_reason"}, set(result))
                run.assert_not_called()

    def test_absent_frozen_run_is_not_replaced_with_new_history(self) -> None:
        """Missing evidence is a refusal, not a replacement Run or history."""
        with self._temporary_root() as temporary:
            root = Path(temporary)
            with mock.patch.object(resolver.work_journal, "_event_lock", side_effect=lambda *_args: nullcontext()):
                result = resolver.resolve_release_unknown_effect(root, _request())
            self.assertEqual("blocked", result["disposition"])
            self.assertEqual({"operation", "run_id", "disposition", "blocked_reason"}, set(result))
            self.assertFalse(list(root.rglob("*.ndjson")))

    def _state(self, root: Path, session: mock.Mock) -> object:
        return SimpleNamespace(
            root=root,
            folder=root / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID,
            execution={},
            session=session,
            terminal_checkpoint={"stopped": True, "unknown_reason": "unknown_effect"},
            terminal_checkpoint_ref=f".caprmedio_install/workflow_orchestrator/runs/{RUN_ID}/release_unknown_effect_terminal_checkpoint.json",
            resolution_ref=f".caprmedio_install/workflow_orchestrator/runs/{RUN_ID}/release_unknown_effect_resolution.json",
        )

    def test_valid_resolution_records_only_three_interrupted_facts_and_no_unit_outcome(self) -> None:
        with self._temporary_root() as temporary:
            root = Path(temporary)
            session = mock.Mock()
            session.interrupted = {}
            session.terminal = {}
            session.finish_run.side_effect = [
                {"disposition": "interrupted", "event_id": "action-event"},
                {"disposition": "interrupted", "event_id": "step-event"},
                {"disposition": "interrupted", "event_id": "workflow-event"},
            ]
            state = self._state(root, session)
            writes: list[tuple[Path, object]] = []
            with mock.patch.object(resolver, "_load_admitted_state", return_value=state), \
                 mock.patch.object(resolver, "_read_existing_resolution", return_value=None), \
                 mock.patch.object(resolver, "_authorization"), \
                 mock.patch.object(resolver, "_current_resolver_authority", return_value=[{"atom_id": atom} for atom in ("CA-R-1895", "CA-M-351", "CA-E-594", "CA-D-589")]), \
                 mock.patch.object(resolver, "_cancel_scheduler"), \
                 mock.patch.object(resolver, "_ensure_terminal_checkpoint"), \
                 mock.patch.object(resolver, "_interruption_prefix", return_value=[]), \
                 mock.patch.object(resolver.work_journal, "_event_lock", side_effect=lambda *_args: nullcontext()), \
                 mock.patch.object(resolver.SelectedExecution, "_write", side_effect=lambda path, value: writes.append((path, value))):
                result = resolver.resolve_release_unknown_effect(root, _request())
            self.assertEqual("resolved", result["disposition"])
            self.assertEqual(["action-event", "step-event", "workflow-event"], result["event_refs"])
            self.assertEqual("unknown_effect", result["unknown_reason"])
            self.assertNotIn("outcome", result)
            self.assertEqual(3, session.finish_run.call_count)
            for call in session.finish_run.call_args_list:
                self.assertEqual("interrupted_pending", call.kwargs["outcome"])
                self.assertEqual([], call.kwargs["effect_refs"])
            self.assertEqual(1, len(writes))
            record = writes[0][1]
            self.assertEqual(12, len(record))
            self.assertEqual("release_unknown_effect_resolution_v1", record["schema"])
            self.assertEqual("unknown_effect", record["resolution_kind"])
            self.assertEqual(["action-event", "step-event", "workflow-event"], record["event_refs"])

    def test_existing_resolution_is_returned_before_current_authority_and_without_replay(self) -> None:
        for operation in (resolver.preflight, resolver.resolve_release_unknown_effect):
            with self.subTest(operation=operation.__name__), self._temporary_root() as temporary:
                root = Path(temporary)
                session = mock.Mock()
                state = self._state(root, session)
                existing = {"event_refs": ["action-event", "step-event", "workflow-event"]}
                with mock.patch.object(resolver, "_load_admitted_state", return_value=state), \
                     mock.patch.object(resolver, "_read_existing_resolution", return_value=existing), \
                     mock.patch.object(resolver, "_authorization") as authorization, \
                     mock.patch.object(resolver, "_current_resolver_authority") as authority, \
                     mock.patch.object(resolver, "_cancel_scheduler") as cancel, \
                     mock.patch.object(resolver.work_journal, "_event_lock", side_effect=lambda *_args: nullcontext()), \
                     mock.patch.object(resolver.SelectedExecution, "_write") as write:
                    result = operation(root, _request())
                self.assertEqual("already_resolved", result["disposition"])
                self.assertEqual(existing["event_refs"], result["event_refs"])
                authorization.assert_not_called()
                authority.assert_not_called()
                cancel.assert_not_called()
                write.assert_not_called()
                session.finish_run.assert_not_called()

    def test_competing_terminal_receipt_blocks_without_replacing_history(self) -> None:
        with self._temporary_root() as temporary:
            root = Path(temporary)
            with mock.patch.object(resolver, "_load_admitted_state", side_effect=resolver._Blocked("competing terminal receipt")), \
                 mock.patch.object(resolver, "_authorization") as authorization, \
                 mock.patch.object(resolver, "_cancel_scheduler") as cancel, \
                 mock.patch.object(resolver.work_journal, "_event_lock", side_effect=lambda *_args: nullcontext()), \
                 mock.patch.object(resolver.SelectedExecution, "_write") as write:
                result = resolver.resolve_release_unknown_effect(root, _request())
            self.assertEqual("blocked", result["disposition"])
            self.assertIn("competing terminal receipt", result["blocked_reason"])
            authorization.assert_not_called()
            cancel.assert_not_called()
            write.assert_not_called()

    def test_existing_resolution_without_terminal_checkpoint_is_not_recreated(self) -> None:
        """A supposedly settled record cannot manufacture its missing companion."""
        pins = [
            {"atom_id": atom, "version": 1, "source_path": f"sources/{atom}.md", "digest": "a" * 64}
            for atom in ("CA-R-1895", "CA-M-351", "CA-E-594", "CA-D-589")
        ]
        refs = ["action-event", "step-event", "workflow-event"]
        with self._temporary_root() as temporary:
            root = Path(temporary)
            session = mock.Mock()
            state = self._state(root, session)
            record_path = root / state.resolution_ref
            record_path.parent.mkdir(parents=True)
            record_path.write_text(json.dumps(resolver._record_value(authority=pins, event_refs=refs)))
            for operation in (resolver.preflight, resolver.resolve_release_unknown_effect):
                with self.subTest(operation=operation.__name__), \
                     mock.patch.object(resolver, "_load_admitted_state", return_value=state), \
                     mock.patch.object(resolver, "_authorization") as authorization, \
                     mock.patch.object(resolver, "_current_resolver_authority") as authority, \
                     mock.patch.object(resolver, "_cancel_scheduler") as cancel, \
                     mock.patch.object(resolver, "_interruption_prefix", return_value=refs), \
                     mock.patch.object(resolver.work_journal, "_event_lock", side_effect=lambda *_args: nullcontext()), \
                     mock.patch.object(resolver.SelectedExecution, "_write") as write:
                    result = operation(root, _request())
                self.assertEqual("blocked", result["disposition"])
                self.assertFalse((root / state.terminal_checkpoint_ref).exists())
                authorization.assert_not_called()
                authority.assert_not_called()
                cancel.assert_not_called()
                write.assert_not_called()

if __name__ == "__main__":
    unittest.main()
