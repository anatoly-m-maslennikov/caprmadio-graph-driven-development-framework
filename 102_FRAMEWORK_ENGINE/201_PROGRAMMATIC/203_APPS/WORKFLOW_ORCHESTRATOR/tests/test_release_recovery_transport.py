"""Transport-only tests for the sealed Release recovery entry point."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


APP = Path(__file__).resolve().parents[1]
MCP = APP.parents[1] / "204_MCP"
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, MCP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import backend  # noqa: E402
from contracts import RecoverSelectedRelease  # noqa: E402
from selected_native_providers import SelectedNativeProviders  # noqa: E402
from selected_routes import SELECTED_ROUTE_NAMES, SelectedRouteAdapter  # noqa: E402


RUN_ID = "release-recovery-transport"
IDENTITY = "a" * 64


class _Transport:
    def __init__(self, status="ENQUEUED", result=None):
        self.calls = []
        self.status = status
        self.result = result

    def enqueue(self, configuration, *args):
        self.calls.append((configuration, args))

    def destroy(self):
        pass

    def retrieve_workflow(self, workflow_id):
        configuration, args = next(call for call in self.calls if call[0]["workflow_id"] == workflow_id)
        return type("Handle", (), {
            "get_status": lambda _self: type("Status", (), {
                "status": self.status, "name": configuration["workflow_name"],
                "queue_name": configuration["queue_name"], "input": {"args": args, "kwargs": {}},
            })(),
            "get_result": lambda _self: self.result,
        })()


class _DBOS:
    def __init__(self):
        self.workflows = {}

    def step(self, *, name):
        return lambda function: function

    def workflow(self, *, name):
        def register(function):
            self.workflows[name] = function
            return function
        return register


class _Support:
    def recover_selected_release(self, request):
        return {"workflow_run_id": request["run_id"], "disposition": "queued"}


class ReleaseRecoveryTransportTests(unittest.TestCase):
    def test_contract_is_closed_and_typed(self):
        value = RecoverSelectedRelease.model_validate({
            "operation": "recover_selected_release", "run_id": RUN_ID, "request_identity": IDENTITY,
        })
        self.assertEqual(RUN_ID, value.run_id)
        with self.assertRaises(ValueError):
            RecoverSelectedRelease.model_validate({
                "operation": "recover_selected_release", "run_id": RUN_ID,
                "request_identity": IDENTITY, "execution": {},
            })

    def test_backend_uses_distinct_scheduler_handle_and_original_run(self):
        frozen = {"request": {"run_id": RUN_ID, "execution": {"operation_route": "release_version"}}}
        transport = _Transport()
        with mock.patch.object(backend.SelectedExecution, "load", return_value=frozen), \
             mock.patch.object(backend, "_release_request_identity", return_value=IDENTITY), \
             mock.patch.object(backend, "client", return_value=transport), \
             mock.patch.object(backend, "status", side_effect=lambda *_: {"workflow_run_id": RUN_ID}):
            result = backend.recover_selected_release(".", {
                "operation": "recover_selected_release", "run_id": RUN_ID, "request_identity": IDENTITY,
            })
        self.assertEqual(RUN_ID, result["workflow_run_id"])
        self.assertRegex(result["recovery_transport_handle"], r"^[0-9a-f]{32}$")
        self.assertEqual("ENQUEUED", result["recovery_transport_status"]["scheduler_status"])
        self.assertNotIn("result", result["recovery_transport_status"])
        configuration, args = transport.calls[0]
        self.assertEqual(backend.RECOVERY_WORKFLOW, configuration["workflow_name"])
        self.assertEqual((RUN_ID, IDENTITY), args)

    def test_repeated_explicit_recovery_gets_fresh_scheduler_delivery_handle(self):
        frozen = {"request": {"run_id": RUN_ID, "execution": {"operation_route": "release_version"}}}
        transport = _Transport()
        request = {"operation": "recover_selected_release", "run_id": RUN_ID, "request_identity": IDENTITY}
        with mock.patch.object(backend.SelectedExecution, "load", return_value=frozen), \
             mock.patch.object(backend, "_release_request_identity", return_value=IDENTITY), \
             mock.patch.object(backend, "client", return_value=transport), \
             mock.patch.object(backend, "status", side_effect=lambda *_: {"workflow_run_id": RUN_ID}):
            first = backend.recover_selected_release(".", request)
            second = backend.recover_selected_release(".", request)
        self.assertEqual(RUN_ID, first["workflow_run_id"])
        self.assertEqual(RUN_ID, second["workflow_run_id"])
        self.assertNotEqual(first["recovery_transport_handle"], second["recovery_transport_handle"])
        self.assertNotEqual(transport.calls[0][0]["workflow_id"], transport.calls[1][0]["workflow_id"])
        self.assertEqual((RUN_ID, IDENTITY), transport.calls[0][1])
        self.assertEqual((RUN_ID, IDENTITY), transport.calls[1][1])

    def test_prior_canonical_success_is_not_reported_as_recovery_output(self):
        frozen = {"request": {"run_id": RUN_ID, "execution": {"operation_route": "release_version"}}}
        transport = _Transport()
        prior = {"workflow_run_id": RUN_ID, "scheduler_status": "SUCCESS",
                 "result": {"outcome": "completed", "old": True}, "outcome": "completed",
                 "selected_result": {"event_receipts": [{"event_id": "sealed-event-1"}]}}
        with mock.patch.object(backend.SelectedExecution, "load", return_value=frozen), \
             mock.patch.object(backend, "_release_request_identity", return_value=IDENTITY), \
             mock.patch.object(backend, "client", return_value=transport), \
             mock.patch.object(backend, "status", return_value=prior):
            result = backend.recover_selected_release(".", {
                "operation": "recover_selected_release", "run_id": RUN_ID, "request_identity": IDENTITY,
            })
        self.assertEqual(prior, result["canonical_run"])
        self.assertEqual("ENQUEUED", result["recovery_transport_status"]["scheduler_status"])
        self.assertEqual(["sealed-event-1"], result["canonical_journal_refs"])
        self.assertIsNone(result["blocked_or_pending_reason"])
        self.assertNotIn("result", result["recovery_transport_status"])
        self.assertNotIn("outcome", result)

    def test_terminal_transport_disposition_does_not_claim_canonical_completion(self):
        frozen = {"request": {"run_id": RUN_ID, "execution": {"operation_route": "release_version"}}}
        canonical = {"workflow_run_id": RUN_ID, "outcome": "interrupted"}
        for scheduler_status, disposition in (
            ("SUCCESS", "transport_succeeded"),
            ("ERROR", "transport_failed"),
            ("CANCELLED", "transport_cancelled"),
        ):
            with self.subTest(scheduler_status=scheduler_status):
                transport = _Transport(scheduler_status, {"transport_only": True})
                with mock.patch.object(backend.SelectedExecution, "load", return_value=frozen), \
                     mock.patch.object(backend, "_release_request_identity", return_value=IDENTITY), \
                     mock.patch.object(backend, "client", return_value=transport), \
                     mock.patch.object(backend, "status", return_value=canonical):
                    result = backend.recover_selected_release(".", {
                        "operation": "recover_selected_release", "run_id": RUN_ID,
                        "request_identity": IDENTITY,
                    })
                self.assertEqual(disposition, result["disposition"])
                self.assertEqual(canonical, result["canonical_run"])
                self.assertNotIn("outcome", result)

    def test_observer_reads_only_the_exact_recovery_handle_across_terminal_states(self):
        for state, expected in (("PENDING", None), ("SUCCESS", {"recovered": True}), ("ERROR", None)):
            status = type("Status", (), {
                "status": state, "name": backend.RECOVERY_WORKFLOW, "queue_name": backend.QUEUE,
                "input": {"args": (RUN_ID, IDENTITY), "kwargs": {}},
            })()
            handle = mock.Mock()
            handle.get_status.return_value = status
            handle.get_result.return_value = {"recovered": True}
            transport = mock.Mock()
            transport.retrieve_workflow.return_value = handle
            observed = backend._observe_recovery_transport(transport, "b" * 32, RUN_ID, IDENTITY)
            self.assertEqual(state, observed["scheduler_status"])
            self.assertEqual(expected, observed.get("result"))
            transport.retrieve_workflow.assert_called_once_with("b" * 32)

    def test_canonical_receipts_are_exact_or_empty_with_truthful_pending_reason(self):
        refs, reason = backend._canonical_recovery_observation({
            "reason": "recording pending", "selected_result": {"event_receipts": [{"event_id": "sealed-1"}]},
        })
        self.assertEqual(["sealed-1"], refs)
        self.assertEqual("recording pending", reason)
        refs, reason = backend._canonical_recovery_observation({"selected_result": {"event_receipts": [{"bad": "x"}]}})
        self.assertEqual([], refs)
        self.assertIsNone(reason)
        refs, reason = backend._canonical_recovery_observation({"selected_result": {
            "disposition": "recording_pending", "pending_event_ids": ["pending-sealed-event"],
            "event_receipts": [],
        }})
        self.assertEqual([], refs)
        self.assertEqual("canonical selected Run has pending sealed event recording", reason)

    def test_backend_rejects_non_release_or_changed_seal_before_queue(self):
        frozen = {"request": {"run_id": RUN_ID, "execution": {"operation_route": "create_atom"}}}
        with mock.patch.object(backend.SelectedExecution, "load", return_value=frozen), \
             mock.patch.object(backend, "client") as client:
            with self.assertRaisesRegex(RuntimeError, "only for an existing frozen Release"):
                backend.recover_selected_release(".", {
                    "operation": "recover_selected_release", "run_id": RUN_ID, "request_identity": IDENTITY,
                })
        client.assert_not_called()

    def test_worker_workflow_calls_only_private_recovery_provider(self):
        dbos = _DBOS()
        provider = mock.Mock()
        backend.register_execution(dbos, type("Engine", (), {"root": Path("/")})(), selected_providers=provider)
        result = dbos.workflows[backend.RECOVERY_WORKFLOW](RUN_ID, IDENTITY)
        provider.recover_release.assert_called_once_with(RUN_ID, IDENTITY)
        self.assertEqual(provider.recover_release.return_value, result)

    def test_provider_rechecks_same_shared_identity_before_private_recovery(self):
        with tempfile.TemporaryDirectory() as temporary:
            provider = SelectedNativeProviders(temporary)
            frozen = {"request": {"run_id": RUN_ID, "execution": {"operation_route": "release_version"}}}
            private = mock.Mock()
            private.recover_release.return_value = {"workflow_run_id": RUN_ID, "disposition": "blocked"}
            with mock.patch.object(SelectedNativeProviders, "execution", return_value=private), \
                 mock.patch("selected_native_providers.SelectedExecution.load", return_value=frozen), \
                 mock.patch("workflow_run_support._canonical_digest", return_value=IDENTITY):
                self.assertEqual({"workflow_run_id": RUN_ID, "disposition": "blocked"}, provider.recover_release(RUN_ID, IDENTITY))
            private.recover_release.assert_called_once_with(frozen)

    def test_mcp_blocks_unadmitted_or_extra_recovery_carriers(self):
        manifest = {"routes": [{"route": name} for name in (*SELECTED_ROUTE_NAMES, "release_version")]}
        adapter = SelectedRouteAdapter(".", service=_Support(), strict_manifest=False)
        request = {"operation": "recover_selected_release", "run_id": RUN_ID, "request_identity": IDENTITY}
        with mock.patch("selected_routes.load_selected_manifest", return_value=manifest):
            self.assertEqual("queued", adapter.recover_release(request)["disposition"])
            self.assertEqual("rejected", adapter.recover_release({**request, "payload": {}})["disposition"])
