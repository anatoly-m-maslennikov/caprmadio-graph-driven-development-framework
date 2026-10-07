"""Private Release-host shutdown contract; no signal, worker, or DBOS runtime."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

import release_host_shutdown as shutdown  # noqa: E402


class ReleaseHostShutdownTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = APP.parents[3] / ".caprmedio_tmp/tests/release-host-shutdown"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.identity = {
            "pid": 12345,
            "start_token": "a" * 64,
            "application_version": "release-host-v1",
            "runtime_fingerprint": "b" * 64,
            "state": "ready",
        }
        directory = self.root / ".caprmedio_install/workflow_orchestrator/release-host"
        directory.mkdir(parents=True)
        for name in ("worker.json", "worker.ready"):
            (directory / name).write_text(json.dumps(self.identity), encoding="utf-8")

    def listener(self, *, has_work, request_stop):
        health_handle = shutdown.health.start_listener(self.root, self.identity)
        self.addCleanup(health_handle.close)
        handle = shutdown.start_listener(
            self.root, self.identity, has_work=has_work, request_stop=request_stop,
        )
        self.addCleanup(handle.close)
        return handle

    def test_busy_worker_returns_closed_three_field_result_without_stop_callback(self) -> None:
        called: list[object] = []
        self.listener(has_work=lambda: True, request_stop=lambda: called.append(True))

        result = shutdown.stop_worker(self.root, timeout=1)

        self.assertEqual({"operation", "nonce", "disposition"}, set(result))
        self.assertEqual("stop-release-worker", result["operation"])
        self.assertEqual("busy", result["disposition"])
        self.assertEqual([], called)

    def test_exact_live_identity_is_authenticated_without_current_disk_fingerprint_admission(self) -> None:
        self.listener(has_work=lambda: True, request_stop=lambda: self.fail("busy must not stop"))

        # Management shutdown authenticates the live pair and private probe;
        # it must not consult the current-code availability gate.
        with patch("release_host_bridge.availability", side_effect=AssertionError("current-code gate")):
            result = shutdown.stop_worker(self.root, timeout=1)
        self.assertEqual("busy", result["disposition"])

    def test_stale_or_mismatched_ready_identity_returns_pending_before_listener_callback(self) -> None:
        called: list[object] = []
        self.listener(has_work=lambda: False, request_stop=lambda: called.append(True))
        ready = self.root / ".caprmedio_install/workflow_orchestrator/release-host/worker.ready"
        ready.write_text(json.dumps(self.identity | {"start_token": "c" * 64}), encoding="utf-8")

        result = shutdown.stop_worker(self.root, timeout=1)
        self.assertEqual({"operation", "nonce", "disposition"}, set(result))
        self.assertEqual("pending", result["disposition"])
        self.assertEqual([], called)

    def test_missing_old_protocol_is_bounded_pending_without_signal_fallback(self) -> None:
        result = shutdown.stop_worker(self.root, timeout=0.2)

        self.assertEqual({"operation", "nonce", "disposition"}, set(result))
        self.assertEqual("stop-release-worker", result["operation"])
        self.assertEqual("pending", result["disposition"])

    def test_accepted_but_unproven_stop_returns_pending_without_a_final_receipt(self) -> None:
        accepted: list[object] = []
        self.listener(has_work=lambda: False, request_stop=lambda: accepted.append(True))

        result = shutdown.stop_worker(self.root, timeout=0.2)

        self.assertEqual([True], accepted)
        self.assertEqual({"operation", "nonce", "disposition"}, set(result))
        self.assertEqual("pending", result["disposition"])
        replies = self.root / ".caprmedio_install/workflow_orchestrator/release-host/shutdown/replies"
        for path in replies.glob("*.json"):
            value = json.loads(path.read_text(encoding="utf-8"))
            self.assertNotEqual("stopped", value.get("disposition"))
            self.assertNotIn("lock_released", value)

    def test_idle_stop_replaces_acceptance_only_after_stopped_metadata_and_lock_proof(self) -> None:
        host = self.root / ".caprmedio_install/workflow_orchestrator/release-host"
        (host / "worker.lock").touch()
        order: list[str] = []

        def request_stop() -> None:
            marker = host / "shutdown/stopping.json"
            self.assertTrue(marker.is_file())
            self.assertEqual("stopping", json.loads(marker.read_text())["state"])
            order.append("request-stop")
            (host / "worker.json").write_text(
                json.dumps(self.identity | {"state": "stopped"}), encoding="utf-8",
            )

        self.listener(has_work=lambda: False, request_stop=request_stop)
        result = shutdown.stop_worker(self.root, timeout=1)

        self.assertEqual(["request-stop"], order)
        self.assertEqual({"operation", "nonce", "pid", "start_token", "application_version",
                          "runtime_fingerprint", "state", "disposition", "lock_released"}, set(result))
        self.assertEqual("stopped", result["state"])
        self.assertEqual("stopped", result["disposition"])
        self.assertTrue(result["lock_released"])
        reply = host / "shutdown/replies" / f"{result['nonce']}.json"
        self.assertEqual(result, json.loads(reply.read_text(encoding="utf-8")))
        self.assertFalse((host / "shutdown/stopping.json").exists())

    def test_malformed_expired_replayed_and_symlinked_shutdown_carriers_refuse_without_stop(self) -> None:
        host = self.root / ".caprmedio_install/workflow_orchestrator/release-host"
        channel = host / "shutdown"
        requests = channel / "requests"
        replies = channel / "replies"
        requests.mkdir(parents=True)
        replies.mkdir()
        nonce = "c" * 64
        request = {"operation": "stop-release-worker", "nonce": nonce,
                   "deadline_monotonic": 10.0, **self.identity}
        with self.assertRaises(shutdown.ShutdownError):
            shutdown._request({"nonce": nonce}, self.identity, 1.0)
        with self.assertRaises(shutdown.ShutdownError):
            shutdown._request(request, self.identity, 10.0)
        replay = requests / f"{nonce}.json"
        replay.write_text(json.dumps(request), encoding="utf-8")
        with self.assertRaises(shutdown.ShutdownError):
            shutdown._create(replay, request, channel)
        replay.unlink()
        unsafe = requests / ("d" * 64 + ".json")
        unsafe.symlink_to(self.root / "outside")
        with self.assertRaises(shutdown.ShutdownError):
            shutdown._messages(requests)

    def test_incomplete_listener_join_keeps_stopping_marker_without_stopped_receipt(self) -> None:
        host = self.root / ".caprmedio_install/workflow_orchestrator/release-host"
        channel = host / "shutdown"
        (channel / "requests").mkdir(parents=True)
        (channel / "replies").mkdir()
        marker = {"nonce": "e" * 64, **self.identity, "state": "stopping"}
        (channel / "stopping.json").write_text(json.dumps(marker), encoding="utf-8")
        handle = shutdown.start_listener(self.root, self.identity, has_work=lambda: False,
                                         request_stop=lambda: None)
        self.addCleanup(lambda: handle.thread.join(1))
        handle.thread = MagicMock()
        handle.thread.is_alive.return_value = True

        with self.assertRaises(shutdown.ShutdownIncomplete):
            handle.close()
        self.assertEqual(marker, json.loads((channel / "stopping.json").read_text(encoding="utf-8")))
        self.assertFalse(any(json.loads(path.read_text()).get("disposition") == "stopped"
                             for path in (channel / "replies").glob("*.json")))

    def test_admission_fence_blocks_dispatch_until_shutdown_is_released(self) -> None:
        host = self.root / ".caprmedio_install/workflow_orchestrator/release-host"
        with shutdown.admission_fence(self.root) as require_open:
            require_open()
            channel = host / "shutdown"
            marker = {"nonce": "f" * 64, **self.identity, "state": "stopping"}
            (channel / "stopping.json").write_text(json.dumps(marker), encoding="utf-8")
            with self.assertRaises(shutdown.ShutdownError):
                shutdown.require_dispatch_open(self.root)
        (host / "shutdown/stopping.json").unlink()
        shutdown.require_dispatch_open(self.root)


if __name__ == "__main__":
    unittest.main()
