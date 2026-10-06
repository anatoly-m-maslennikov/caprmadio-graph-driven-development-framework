"""Release-host transport boundary tests; no worker, queue, or Docker daemon runs."""

import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

import release_host_bridge as bridge  # noqa: E402


class ReleaseHostBridgeTests(unittest.TestCase):
    def setUp(self):
        temporary = APP.parents[3] / ".caprmedio_tmp/tests/release-host-bridge"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        interpreter = self.root / bridge.FIXED_INTERPRETER
        interpreter.parent.mkdir(parents=True)
        interpreter.write_text("fixture interpreter")
        bridge.publish_transport(self.root)
        ready = self.root / bridge.READY
        ready.parent.mkdir(parents=True, exist_ok=True)
        ready.write_text(json.dumps({
            "state": "ready", "pid": 1, "application_version": "release-host-v1",
            "runtime_fingerprint": "f" * 64,
        }))
        (self.root / bridge.DIRECTORY / "worker.json").write_text(
            json.dumps({"pid": 1, "state": "starting"})
        )
        (self.root / bridge.DATABASE).touch()
        self.worker_alive = patch("release_host_bridge._worker_is_alive", return_value=True)
        self.runtime_fingerprint = patch("release_host_bridge._runtime_fingerprint", return_value="f" * 64)
        self.application_version = patch("release_host_bridge._application_version", return_value="release-host-v1")
        self.worker_alive.start()
        self.runtime_fingerprint.start()
        self.application_version.start()
        self.addCleanup(self.worker_alive.stop)
        self.addCleanup(self.runtime_fingerprint.stop)
        self.addCleanup(self.application_version.stop)

    def test_exact_binding_is_idempotent_and_rejects_a_changed_request(self):
        first = bridge.retain_binding(self.root, run_id="release-1", frozen_request_digest="a" * 64)
        self.assertEqual("release-host", first["transport"])
        self.assertEqual(first, bridge.retain_binding(
            self.root, run_id="release-1", frozen_request_digest="a" * 64,
        ))
        with self.assertRaisesRegex(bridge.ReleaseHostUnavailable, "conflicts"):
            bridge.retain_binding(self.root, run_id="release-1", frozen_request_digest="b" * 64)

    def test_missing_binding_never_adopts_a_foreign_status_run(self):
        with patch("release_host_bridge.subprocess.run") as launched:
            with self.assertRaisesRegex(bridge.ReleaseHostUnavailable, "binding"):
                bridge.invoke(self.root, {"operation": "status", "run_id": "native-run"})
        launched.assert_not_called()

    def test_unavailable_marker_ready_or_database_fails_before_subprocess(self):
        bridge.retain_binding(self.root, run_id="release-1", frozen_request_digest="a" * 64)
        cases = (
            self.root / bridge.MARKER,
            self.root / bridge.READY,
            self.root / bridge.DATABASE,
        )
        for path in cases:
            with self.subTest(path=path.name), patch("release_host_bridge.subprocess.run") as launched:
                saved = path.read_bytes()
                path.unlink()
                try:
                    with self.assertRaises(bridge.ReleaseHostUnavailable):
                        bridge.invoke(self.root, {"operation": "status", "run_id": "release-1"})
                finally:
                    path.write_bytes(saved)
                launched.assert_not_called()

    def test_dead_worker_mismatched_state_or_stale_fingerprint_blocks_before_child_admission(self):
        self.worker_alive.stop()
        self.runtime_fingerprint.stop()
        self.application_version.stop()
        bridge.retain_binding(self.root, run_id="release-1", frozen_request_digest="a" * 64)
        request = {"operation": "status", "run_id": "release-1"}
        with patch("release_host_bridge.subprocess.run") as launched, \
             patch("release_host_bridge._application_version", return_value="release-host-v1"), \
             patch("release_host_bridge._runtime_fingerprint", return_value="f" * 64), \
             patch("release_host_bridge._worker_is_alive", return_value=False):
            with self.assertRaisesRegex(bridge.ReleaseHostUnavailable, "readiness is invalid"):
                bridge.invoke(self.root, request)
        launched.assert_not_called()
        worker_state = self.root / bridge.DIRECTORY / "worker.json"
        worker_state.write_text(json.dumps({"pid": 2, "state": "starting"}))
        with patch("release_host_bridge.subprocess.run") as launched, \
             patch("release_host_bridge._worker_is_alive", return_value=True), \
             patch("release_host_bridge._application_version", return_value="release-host-v1"), \
             patch("release_host_bridge._runtime_fingerprint", return_value="f" * 64):
            with self.assertRaisesRegex(bridge.ReleaseHostUnavailable, "readiness is invalid"):
                bridge.invoke(self.root, request)
        launched.assert_not_called()
        worker_state.write_text(json.dumps({"pid": 1, "state": "starting"}))
        with patch("release_host_bridge.subprocess.run") as launched, \
             patch("release_host_bridge._worker_is_alive", return_value=True), \
             patch("release_host_bridge._application_version", return_value="release-host-v1"), \
             patch("release_host_bridge._runtime_fingerprint", return_value="a" * 64):
            with self.assertRaisesRegex(bridge.ReleaseHostUnavailable, "fingerprint is stale"):
                bridge.invoke(self.root, request)
        launched.assert_not_called()

    def test_subprocess_has_the_fixed_interpreter_and_private_namespace(self):
        bridge.retain_binding(self.root, run_id="release-1", frozen_request_digest="a" * 64)
        original = os.environ.get("CAPRMEDIO_RUNTIME_NAMESPACE")
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "docker",
                                    "CAPRMEDIO_AGENT_MODE": "mock"}), \
             patch("release_host_bridge.subprocess.run", return_value=SimpleNamespace(
                 returncode=0, stdout='{"outcome":"queued"}',
             )) as launched:
            result = bridge.invoke(self.root, {"operation": "status", "run_id": "release-1"})
            self.assertEqual("docker", os.environ["CAPRMEDIO_RUNTIME_NAMESPACE"])
            self.assertEqual("mock", os.environ["CAPRMEDIO_AGENT_MODE"])
        self.assertEqual({"outcome": "queued"}, result)
        command = launched.call_args.args[0]
        self.assertEqual(str(self.root / bridge.FIXED_INTERPRETER), command[0])
        self.assertEqual(str(APP / "orchestrator.py"), command[1])
        environment = launched.call_args.kwargs["env"]
        self.assertEqual("release-host", environment["CAPRMEDIO_RUNTIME_NAMESPACE"])
        self.assertNotIn("CAPRMEDIO_AGENT_MODE", environment)
        self.assertEqual(original, os.environ.get("CAPRMEDIO_RUNTIME_NAMESPACE") if original is not None else None)

    def test_explicit_launcher_uses_distinct_host_worker_and_log(self):
        import orchestrator

        child = SimpleNamespace(pid=12345)
        with patch("orchestrator.subprocess.Popen", return_value=child) as spawned:
            result = orchestrator._start_worker(self.root, release_host=True)
        self.assertEqual(12345, result["release_worker_pid"])
        self.assertEqual(".caprmedio_install/workflow_orchestrator/release-host/worker.log",
                         result["log_path"])
        command = spawned.call_args.args[0]
        self.assertEqual(str(self.root / bridge.FIXED_INTERPRETER), command[0])
        self.assertEqual("release-worker", command[-1])
        environment = spawned.call_args.kwargs["env"]
        self.assertEqual("release-host", environment["CAPRMEDIO_RUNTIME_NAMESPACE"])

    def test_release_host_child_does_not_reenter_an_existing_docker_marker(self):
        import orchestrator

        marker = self.root / ".caprmedio_install/workflow_orchestrator/docker/transport.json"
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text(json.dumps({"transport": "docker", "project_name": "caprmedio-fixture"}))
        release = {"operation": "enqueue_selected", "run_id": "release-child",
                   "execution": {"operation_route": "release_version"}}
        status = {"operation": "status", "run_id": "release-child"}
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "release-host"}), \
             patch("docker_bridge.invoke") as docker, \
             patch.object(orchestrator, "enqueue_selected", return_value={"backend": "enqueue"}) as enqueue, \
             patch.object(orchestrator, "status", return_value={"backend": "status"}) as observe:
            self.assertEqual({"backend": "enqueue"}, orchestrator.run(self.root, release))
            self.assertEqual({"backend": "status"}, orchestrator.run(self.root, status))
        enqueue.assert_called_once()
        observe.assert_called_once()
        docker.assert_not_called()


if __name__ == "__main__":
    unittest.main()
