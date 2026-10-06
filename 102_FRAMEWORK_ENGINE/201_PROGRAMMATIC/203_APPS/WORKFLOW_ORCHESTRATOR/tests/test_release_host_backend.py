"""Deterministic boundary tests for the Release-only host scheduler."""
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

import backend  # noqa: E402
from runtime_config import control_directory, docker_runtime, release_host_runtime  # noqa: E402


RUN_ID = "release-host-run"
IDENTITY = "a" * 64
BINDING_DIGEST = "b" * 64


class _Transport:
    def __init__(self):
        self.calls = []

    def enqueue(self, configuration, *args):
        self.calls.append((configuration, args))

    def destroy(self):
        pass


class _DBOS:
    def __init__(self):
        self.steps = {}
        self.workflows = {}

    def step(self, *, name):
        def register(function):
            self.steps[name] = function
            return function
        return register

    def workflow(self, *, name):
        def register(function):
            self.workflows[name] = function
            return function
        return register


def _release_frozen():
    return {
        "request": {
            "operation": "enqueue_selected",
            "run_id": RUN_ID,
            "execution": {"operation_route": "release_version"},
        },
        "graph": {
            "route": "release_version",
            "workflow": {"atom_id": "CA-O-164"},
        },
    }


class ReleaseHostBackendTests(unittest.TestCase):
    def host_environment(self):
        return mock.patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "release-host"})

    def test_runtime_uses_the_exact_isolated_release_host_directory(self):
        with self.host_environment():
            self.assertTrue(release_host_runtime())
            self.assertFalse(docker_runtime())
            self.assertEqual(
                ".caprmedio_install/workflow_orchestrator/release-host",
                control_directory(),
            )

    def test_host_rejects_base_revise_before_a_coordinator_or_scheduler_write(self):
        request = {
            "operation": "enqueue",
            "run_id": "ordinary-base-revise",
            "selection": [],
            "criteria_paths": ["rules.md"],
            "author": "operator",
            "scope": "TEST",
        }
        with self.host_environment(), mock.patch.object(backend, "Coordinator") as coordinator, \
                mock.patch.object(backend, "client") as client:
            with self.assertRaisesRegex(RuntimeError, "Release host accepts only"):
                backend.enqueue(".", request)
        coordinator.assert_not_called()
        client.assert_not_called()

    def test_host_rejects_non_release_selected_request_before_freeze_or_queue(self):
        selected = mock.Mock()
        with tempfile.TemporaryDirectory() as directory:
            selected.run_directory.return_value = Path(directory) / "missing-selected-run"
            selected._validated_freeze.return_value = {
                "request": {"execution": {"operation_route": "create_atom"}},
                "graph": {"route": "create_atom"},
            }
            request = {"operation": "enqueue_selected", "run_id": RUN_ID, "execution": {"request": "value"}}
            with self.host_environment(), mock.patch.object(backend, "SelectedExecution", return_value=selected), \
                    mock.patch.object(backend, "client") as client:
                with self.assertRaisesRegex(RuntimeError, "exact frozen Release route"):
                    backend.enqueue_selected(".", request)
        selected.freeze.assert_not_called()
        client.assert_not_called()

    def test_host_rejects_an_identical_foreign_shared_selected_carrier_before_any_host_write(self):
        request = {
            "operation": "enqueue_selected",
            "run_id": RUN_ID,
            "execution": {"operation_route": "release_version"},
        }
        frozen = {
            "request": dict(request),
            "graph": {"route": "release_version", "workflow": {"atom_id": "CA-O-164"}},
        }
        # Native and Docker workers use this one canonical selected-Run store.
        # A carrier therefore cannot identify its owner; the absent host
        # binding must reject either foreign origin before any host mutation.
        for origin in ("native", "docker"):
            with self.subTest(origin=origin), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                actual = backend.SelectedExecution(root)
                shared = actual.run_directory(RUN_ID)
                carrier = shared / "selected_request.json"
                carrier.parent.mkdir(parents=True)
                original = json.dumps(frozen, sort_keys=True).encode()
                carrier.write_bytes(original)
                selected = mock.Mock()
                selected.run_directory.return_value = shared
                selected.load.return_value = frozen
                bridge = mock.Mock()
                bridge.request_digest.return_value = BINDING_DIGEST
                bridge.binding.side_effect = RuntimeError(f"{origin} Run has no host binding")
                with self.host_environment(), \
                        mock.patch.object(backend, "SelectedExecution", return_value=selected), \
                        mock.patch.object(backend, "_release_host_bridge", return_value=bridge), \
                        mock.patch.object(backend, "client") as client:
                    with self.assertRaisesRegex(RuntimeError, "has no host binding"):
                        backend.enqueue_selected(root, request)
                selected._validated_freeze.assert_not_called()
                selected.freeze.assert_not_called()
                client.assert_not_called()
                self.assertEqual(original, carrier.read_bytes())
                self.assertFalse((root / ".caprmedio_install/workflow_orchestrator/release-host").exists())

    def test_exact_host_bound_shared_carrier_requires_scheduler_provenance_and_can_reuse_the_run_id(self):
        frozen = _release_frozen()
        request = dict(frozen["request"])
        bridge = mock.Mock()
        bridge.request_digest.return_value = BINDING_DIGEST
        queue_status = type("Status", (), {
            "name": backend.RELEASE_HOST_SELECTED_WORKFLOW,
            "queue_name": backend.RELEASE_HOST_QUEUE,
            "input": {"args": (RUN_ID,), "kwargs": {}},
        })()
        handle = mock.Mock()
        handle.get_status.return_value = queue_status
        transport = mock.Mock()
        transport.retrieve_workflow.return_value = handle
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            actual = backend.SelectedExecution(root)
            shared = actual.run_directory(RUN_ID)
            carrier = shared / "selected_request.json"
            carrier.parent.mkdir(parents=True)
            carrier.write_text(json.dumps(frozen), encoding="utf-8")
            selected = mock.Mock()
            selected.run_directory.return_value = shared
            selected.load.return_value = frozen
            selected._validated_freeze.return_value = frozen
            selected.freeze.return_value = frozen
            with self.host_environment(), \
                    mock.patch.object(backend, "SelectedExecution", return_value=selected), \
                    mock.patch.object(backend, "_release_host_bridge", return_value=bridge), \
                    mock.patch.object(backend, "client", return_value=transport), \
                    mock.patch.object(backend, "status", return_value={"outcome": "queued"}):
                result = backend.enqueue_selected(root, request)
        self.assertEqual("queued", result["disposition"])
        bridge.binding.assert_called_once_with(
            root, run_id=RUN_ID, frozen_request_digest=BINDING_DIGEST,
        )
        transport.retrieve_workflow.assert_called_once_with(RUN_ID)
        transport.enqueue.assert_called_once()

    def test_host_bound_shared_carrier_with_another_scheduler_provenance_rejects_before_freeze(self):
        frozen = _release_frozen()
        bridge = mock.Mock()
        bridge.request_digest.return_value = BINDING_DIGEST
        queue_status = type("Status", (), {
            "name": "selected-workflow-execution", "queue_name": "base-revise",
            "input": {"args": (RUN_ID,), "kwargs": {}},
        })()
        handle = mock.Mock()
        handle.get_status.return_value = queue_status
        transport = mock.Mock()
        transport.retrieve_workflow.return_value = handle
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            actual = backend.SelectedExecution(root)
            shared = actual.run_directory(RUN_ID)
            carrier = shared / "selected_request.json"
            carrier.parent.mkdir(parents=True)
            carrier.write_text(json.dumps(frozen), encoding="utf-8")
            selected = mock.Mock()
            selected.run_directory.return_value = shared
            selected.load.return_value = frozen
            with self.host_environment(), \
                    mock.patch.object(backend, "SelectedExecution", return_value=selected), \
                    mock.patch.object(backend, "_release_host_bridge", return_value=bridge), \
                    mock.patch.object(backend, "client", return_value=transport):
                with self.assertRaisesRegex(RuntimeError, "lacks exact host scheduler provenance"):
                    backend.enqueue_selected(root, frozen["request"])
        selected._validated_freeze.assert_not_called()
        selected.freeze.assert_not_called()

    def test_host_claims_the_digest_then_queues_only_its_own_scheduler_workflow(self):
        frozen = _release_frozen()
        selected = mock.Mock()
        transport = _Transport()
        bridge = mock.Mock()
        bridge.request_digest.return_value = BINDING_DIGEST
        request = {"operation": "enqueue_selected", "run_id": RUN_ID, "execution": {"request": "value"}}
        with tempfile.TemporaryDirectory() as directory:
            selected.run_directory.return_value = Path(directory) / "missing-selected-run"
            selected._validated_freeze.return_value = frozen
            selected.freeze.return_value = frozen
            with self.host_environment(), mock.patch.object(backend, "SelectedExecution", return_value=selected), \
                    mock.patch.object(backend, "_release_host_bridge", return_value=bridge), \
                    mock.patch.object(backend, "_release_request_identity", return_value=IDENTITY), \
                    mock.patch.object(backend, "client", return_value=transport), \
                    mock.patch.object(backend, "status", return_value={"outcome": "queued"}):
                result = backend.enqueue_selected(".", request)
        bridge.availability.assert_called_once_with(".")
        bridge.transport.assert_called_once_with(".")
        bridge.retain_binding.assert_called_once_with(
            ".", run_id=RUN_ID, frozen_request_digest=BINDING_DIGEST,
        )
        self.assertEqual("queued", result["disposition"])
        self.assertEqual(1, len(transport.calls))
        configuration, args = transport.calls[0]
        self.assertEqual(backend.RELEASE_HOST_QUEUE, configuration["queue_name"])
        self.assertEqual(backend.RELEASE_HOST_SELECTED_WORKFLOW, configuration["workflow_name"])
        self.assertEqual(backend.RELEASE_HOST_APP_VERSION, configuration["app_version"])
        self.assertEqual((RUN_ID,), args)

    def test_host_status_rejects_foreign_or_unbound_run_before_client_access(self):
        with self.host_environment(), \
                mock.patch.object(backend, "_release_host_frozen", side_effect=RuntimeError("foreign binding")), \
                mock.patch.object(backend, "client") as client:
            with self.assertRaisesRegex(RuntimeError, "foreign binding"):
                backend.status(".", {"operation": "status", "run_id": RUN_ID})
        client.assert_not_called()

    def test_host_recovery_rechecks_the_retained_binding_before_client_access(self):
        with self.host_environment(), \
                mock.patch.object(backend, "_release_host_frozen", side_effect=RuntimeError("foreign binding")), \
                mock.patch.object(backend, "client") as client:
            with self.assertRaisesRegex(RuntimeError, "foreign binding"):
                backend.recover_selected_release(".", {
                    "operation": "recover_selected_release",
                    "run_id": RUN_ID,
                    "request_identity": IDENTITY,
                })
        client.assert_not_called()

    def test_host_recovery_status_rechecks_the_retained_binding_before_client_access(self):
        with self.host_environment(), \
                mock.patch.object(backend, "_release_host_frozen", side_effect=RuntimeError("foreign binding")), \
                mock.patch.object(backend, "client") as client:
            with self.assertRaisesRegex(RuntimeError, "foreign binding"):
                backend.recover_selected_release_status(".", {
                    "operation": "recover_selected_release_status",
                    "run_id": RUN_ID,
                    "recovery_transport_handle": "c" * 32,
                })
        client.assert_not_called()

    def test_host_worker_registers_only_release_workflows_and_revalidates_at_dispatch(self):
        dbos = _DBOS()
        provider = mock.Mock()
        engine = type("Engine", (), {"root": Path(".")})()
        with self.host_environment(), \
                mock.patch.object(backend, "_release_host_frozen", return_value=(_release_frozen(), IDENTITY)) as frozen:
            backend.register_execution(dbos, engine, selected_providers=provider)
            self.assertEqual(
                {backend.RELEASE_HOST_SELECTED_WORKFLOW, backend.RELEASE_HOST_RECOVERY_WORKFLOW},
                set(dbos.workflows),
            )
            self.assertEqual(
                {"release-host-selected-workflow-dispatch", "release-host-selected-release-recovery"},
                set(dbos.steps),
            )
            self.assertNotIn(backend.WORKFLOW, dbos.workflows)
            self.assertNotIn(backend.SELECTED_WORKFLOW, dbos.workflows)
            dbos.workflows[backend.RELEASE_HOST_SELECTED_WORKFLOW](RUN_ID)
            frozen.assert_called_once_with(Path("."), RUN_ID, require_available=False)
            provider.dispatch.assert_called_once_with(RUN_ID)


if __name__ == "__main__":
    unittest.main()
