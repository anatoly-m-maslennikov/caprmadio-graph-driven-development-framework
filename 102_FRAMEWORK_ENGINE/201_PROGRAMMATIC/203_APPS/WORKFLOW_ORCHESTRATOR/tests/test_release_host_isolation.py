"""Disposable-project integration regression for the isolated Release host.

This is deliberately a transport test: it uses the production marker and
binding carriers, but does not start DBOS, Docker, an Agent, or a Release.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


APP = Path(__file__).resolve().parents[1]
for location in (APP, APP / "docker"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import backend  # noqa: E402
import orchestrator  # noqa: E402
import release_host_bridge  # noqa: E402


RUN_ID = "release-host-isolation-run"
IDENTITY = "a" * 64


class ReleaseHostIsolationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.root.joinpath(".caprmedio_caprmedio").mkdir()

    def host_environment(self):
        return mock.patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "release-host"})

    def _write_ready_host(self) -> None:
        release_host_bridge.publish_transport(self.root)
        database = self.root / release_host_bridge.DATABASE
        database.parent.mkdir(parents=True, exist_ok=True)
        database.write_bytes(b"host-scheduler")
        ready = self.root / release_host_bridge.READY
        ready.write_text(json.dumps({
            "application_version": backend.RELEASE_HOST_APP_VERSION,
            "pid": 12345,
            "runtime_fingerprint": "fixture-fingerprint",
            "state": "ready",
        }), encoding="utf-8")

    def test_release_host_store_is_separate_and_does_not_mutate_native_or_docker_store(self):
        native = self.root / ".caprmedio_install/workflow_orchestrator/dbos.sqlite"
        docker = self.root / ".caprmedio_install/workflow_orchestrator/docker/dbos.sqlite"
        for path, value in ((native, b"native-enqueued-base-revise"),
                            (docker, b"docker-existing-queue")):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(value)

        with mock.patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": ""}):
            native_path, _ = backend.database(self.root)
        with mock.patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "docker"}):
            docker_path, _ = backend.database(self.root)
        with self.host_environment():
            host_path, _ = backend.database(self.root)

        self.assertEqual(native, native_path)
        self.assertEqual(docker, docker_path)
        self.assertEqual(self.root / release_host_bridge.DATABASE, host_path)
        self.assertNotIn(host_path, (native_path, docker_path))
        self.assertEqual(b"native-enqueued-base-revise", native.read_bytes())
        self.assertEqual(b"docker-existing-queue", docker.read_bytes())

    def test_release_route_selects_host_before_existing_docker_marker_and_non_release_stays_docker(self):
        marker = self.root / ".caprmedio_install/workflow_orchestrator/docker/transport.json"
        marker.parent.mkdir(parents=True, exist_ok=True)
        original_marker = {"transport": "docker", "project_name": "caprmedio-fixture"}
        marker.write_text(json.dumps(original_marker), encoding="utf-8")
        release = {"operation": "enqueue_selected", "run_id": RUN_ID,
                   "execution": {"operation_route": "release_version"}}
        ordinary = {"operation": "enqueue_selected", "run_id": "ordinary-selected",
                    "execution": {"operation_route": "create_atom"}}
        with mock.patch.object(orchestrator, "invoke_release_host", return_value={"host": True}) as host, \
                mock.patch("docker_bridge.invoke", return_value={"docker": True}) as docker:
            self.assertEqual({"host": True}, orchestrator.run(self.root, release))
            self.assertEqual({"docker": True}, orchestrator.run(self.root, ordinary))

        host.assert_called_once()
        docker.assert_called_once()
        self.assertEqual(original_marker, json.loads(marker.read_text(encoding="utf-8")))

    def test_unready_or_foreign_host_run_fails_closed_without_subprocess_or_queue_fallback(self):
        self._write_ready_host()
        release_host_bridge.retain_binding(self.root, run_id=RUN_ID, frozen_request_digest=IDENTITY)
        ready = self.root / release_host_bridge.READY
        ready.write_text("{}", encoding="utf-8")
        with mock.patch("release_host_bridge.subprocess.run", side_effect=AssertionError("no executor")) as execute:
            with self.assertRaisesRegex(release_host_bridge.ReleaseHostUnavailable, "readiness is invalid"):
                release_host_bridge.invoke(self.root, {"operation": "status", "run_id": RUN_ID})
            with self.assertRaisesRegex(release_host_bridge.ReleaseHostUnavailable, "binding is unavailable"):
                release_host_bridge.invoke(self.root, {"operation": "status", "run_id": "foreign-run"})
        execute.assert_not_called()

    def test_historical_frozen_source_status_requires_exact_host_provenance_without_revalidation(self):
        frozen = {
            "request": {"run_id": RUN_ID, "execution": {"operation_route": "release_version"}},
            "graph": {"route": "release_version"},
        }
        release_host_bridge.retain_binding(
            self.root,
            run_id=RUN_ID,
            frozen_request_digest=release_host_bridge.request_digest(frozen["request"]),
        )
        selected = mock.Mock()
        selected.load.return_value = frozen
        selected._revalidate.side_effect = AssertionError("historical observation must not revalidate source")
        selected.run_directory.return_value = self.root / "no-selected-run-carrier"
        status = mock.Mock(status="PENDING")
        handle = mock.Mock()
        handle.get_status.return_value = status
        transport = mock.Mock()
        transport.retrieve_workflow.return_value = handle
        with self.host_environment(), \
                mock.patch.object(backend, "SelectedExecution", return_value=selected), \
                mock.patch.object(backend, "_release_request_identity", return_value=IDENTITY), \
                mock.patch("release_host_bridge.availability", return_value={"ready": True}), \
                mock.patch.object(backend, "client", return_value=transport) as client:
            observed = backend.status(self.root, {"operation": "status", "run_id": RUN_ID})
            self.assertEqual("PENDING", observed["scheduler_status"])
            selected._revalidate.assert_not_called()
            transport.retrieve_workflow.assert_called_once_with(RUN_ID)

            # A saved Run may be observed after a legitimate source refresh,
            # but its retained binding must still match the exact frozen request.
            frozen["request"]["execution"]["tampered"] = True
            with self.assertRaisesRegex(release_host_bridge.ReleaseHostUnavailable, "does not match"):
                backend.status(self.root, {"operation": "status", "run_id": RUN_ID})

            foreign = {
                "request": {"run_id": "foreign-run", "execution": {"operation_route": "release_version"}},
                "graph": {"route": "release_version"},
            }
            selected.load.return_value = foreign
            with self.assertRaisesRegex(release_host_bridge.ReleaseHostUnavailable, "binding is unavailable"):
                backend.status(self.root, {"operation": "status", "run_id": "foreign-run"})

        client.assert_called_once_with(self.root)
        transport.destroy.assert_called_once()

    def test_explicit_host_start_publishes_only_transport_not_a_run(self):
        interpreter = self.root / release_host_bridge.FIXED_INTERPRETER
        interpreter.parent.mkdir(parents=True, exist_ok=True)
        interpreter.write_text("#!/bin/sh\n", encoding="utf-8")
        child = mock.Mock(pid=54321)
        with mock.patch("orchestrator.subprocess.Popen", return_value=child) as started:
            result = orchestrator._start_worker(self.root, release_host=True)

        self.assertEqual(54321, result["release_worker_pid"])
        self.assertEqual("starting", result["outcome"])
        started.assert_called_once()
        self.assertEqual({"namespace": "release-host", "transport": "release-host"},
                         release_host_bridge.transport(self.root))
        self.assertFalse((self.root / release_host_bridge.BINDINGS).exists())
        self.assertFalse((self.root / ".caprmedio_tmp").exists())


if __name__ == "__main__":
    unittest.main()
