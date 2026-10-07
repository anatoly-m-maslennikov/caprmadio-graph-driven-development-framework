"""Worker lifecycle contract for the private Release-host health listener."""

from __future__ import annotations

import os
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import MagicMock, patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

import backend  # noqa: E402
import orchestrator  # noqa: E402


class _Engine:
    def __init__(self, root: Path, events: list[tuple], saved: list[tuple]) -> None:
        self.root = root
        self._events = events
        self._saved = saved

    def save(self, path: Path, value: dict) -> None:
        self._events.append(("save", Path(path).name))
        self._saved.append((Path(path), value.copy()))


class ReleaseHostHealthLifecycleTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = APP.parents[3] / ".caprmedio_tmp/tests/release-host-health-lifecycle"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.ready = self.root / "release-host" / "worker.ready"

    def _run_worker(self, *, release_host: bool, listener=None):
        events: list[tuple] = []
        saved: list[tuple] = []
        engine = _Engine(self.root, events, saved)
        dbos = MagicMock()
        dbos.side_effect = lambda **_config: events.append(("dbos", "configure"))
        dbos.launch.side_effect = lambda: events.append(("dbos", "launch"))
        dbos.register_queue.side_effect = lambda *_args, **_kwargs: events.append(("dbos", "queue"))
        dbos.destroy.side_effect = lambda: events.append(("dbos", "destroy"))
        dbos_module = types.ModuleType("dbos")
        dbos_module.DBOS = dbos
        self._last_worker_run = events, saved, dbos
        stop = MagicMock()
        stop.wait.side_effect = lambda: events.append(("stop", "wait"))
        scheduler = {"application": "release-app" if release_host else "ordinary-app",
                     "queue": "release-host" if release_host else "base-revise",
                     "app_version": "release-v1" if release_host else "ordinary-v1"}
        with patch.dict(sys.modules, {"dbos": dbos_module}), \
                patch.object(backend, "database", return_value=(self.root / "db.sqlite", "sqlite:///unused")), \
                patch.object(backend, "Coordinator", return_value=engine), \
                patch.object(backend, "_scheduler_identity", return_value=scheduler), \
                patch.object(backend, "release_host_runtime", return_value=release_host), \
                patch.object(backend, "implementation_mock_runtime", return_value=False), \
                patch.object(backend, "docker_runtime", return_value=False), \
                patch.object(backend, "runtime_fingerprint", return_value="f" * 64), \
                patch.object(backend, "register_execution"), \
                patch.object(backend, "SelectedNativeProviders"), \
                patch.object(backend.threading, "Event", return_value=stop), \
                patch.object(backend.signal, "getsignal", return_value=object()), \
                patch.object(backend.signal, "signal"), \
                patch.object(os, "getpid", return_value=4321):
            if listener is None:
                backend.worker(self.root, ready_file=self.ready,
                               release_start_token="a" * 64 if release_host else None)
            else:
                health_module = types.ModuleType("release_host_health")
                health_module.HealthShutdownIncomplete = type(
                    "HealthShutdownIncomplete", (RuntimeError,), {},
                )
                health_module.start_listener = lambda root, identity: listener(
                    root, identity, events, health_module,
                )
                with patch.dict(sys.modules, {"release_host_health": health_module}):
                    backend.worker(self.root, ready_file=self.ready,
                                   release_start_token="a" * 64 if release_host else None)
        return events, saved, dbos

    def test_release_listener_starts_before_identical_ready_carriers_and_closes_before_destroy(self) -> None:
        handle = MagicMock()
        def listener(root, identity, events, _health_module):
            events.append(("listener", "start"))
            self.assertEqual(self.root, root)
            self.assertEqual("a" * 64, identity["start_token"])
            handle.close.side_effect = lambda: events.append(("listener", "close"))
            return handle

        worker_events, saved, dbos = self._run_worker(release_host=True, listener=listener)
        self.assertLess(worker_events.index(("dbos", "queue")), worker_events.index(("listener", "start")))
        self.assertEqual(["worker.json", "worker.ready"], [path.name for path, _ in saved])
        self.assertEqual(saved[0][1], saved[1][1])
        self.assertEqual({"pid", "start_token", "application_version", "runtime_fingerprint", "state"},
                         set(saved[0][1]))
        self.assertEqual("ready", saved[0][1]["state"])
        self.assertLess(worker_events.index(("listener", "close")), worker_events.index(("dbos", "destroy")))
        dbos.destroy.assert_called_once_with()

    def test_unproven_listener_close_preserves_ready_identity_and_skips_dbos_destroy(self) -> None:
        def listener(_root, _identity, _events, health_module):
            handle = MagicMock()
            handle.close.side_effect = health_module.HealthShutdownIncomplete("join is unproven")
            return handle

        with self.assertRaisesRegex(RuntimeError, "join is unproven"):
            self._run_worker(release_host=True, listener=listener)
        _events, saved, dbos = self._last_worker_run
        self.assertEqual(["worker.json", "worker.ready"], [path.name for path, _ in saved])
        self.assertEqual(saved[0][1], saved[1][1])
        self.assertEqual("ready", saved[0][1]["state"])
        dbos.destroy.assert_not_called()

    def test_listener_start_failure_destroys_dbos_without_publishing_ready_carriers(self) -> None:
        failure = RuntimeError("listener startup failed")
        events: list[tuple] = []
        saved: list[tuple] = []
        engine = _Engine(self.root, events, saved)
        dbos = MagicMock()
        dbos_module = types.ModuleType("dbos")
        dbos_module.DBOS = dbos
        with patch.dict(sys.modules, {"dbos": dbos_module}), \
                patch.object(backend, "database", return_value=(self.root / "db.sqlite", "sqlite:///unused")), \
                patch.object(backend, "Coordinator", return_value=engine), \
                patch.object(backend, "_scheduler_identity", return_value={"application": "release-app", "queue": "release-host", "app_version": "release-v1"}), \
                patch.object(backend, "release_host_runtime", return_value=True), \
                patch.object(backend, "implementation_mock_runtime", return_value=False), \
                patch.object(backend, "runtime_fingerprint", return_value="f" * 64), \
                patch.object(backend, "register_execution"), \
                patch.object(backend, "SelectedNativeProviders"), \
                patch.object(backend.threading, "Event", return_value=MagicMock()), \
                patch.object(backend.signal, "getsignal", return_value=object()), \
                patch.object(backend.signal, "signal"), \
                patch.object(os, "getpid", return_value=4321), \
                patch.dict(sys.modules, {"release_host_health": types.SimpleNamespace(start_listener=MagicMock(side_effect=failure))}):
            with self.assertRaisesRegex(RuntimeError, "listener startup failed"):
                backend.worker(self.root, ready_file=self.ready, release_start_token="a" * 64)
        self.assertEqual([], saved)
        dbos.destroy.assert_called_once_with()

    def test_ordinary_worker_does_not_start_release_listener_or_publish_release_identity(self) -> None:
        worker_events, saved, _dbos = self._run_worker(release_host=False)
        self.assertEqual(["worker.ready"], [path.name for path, _ in saved])
        self.assertNotIn("start_token", saved[0][1])
        self.assertEqual("ready", saved[0][1]["state"])
        self.assertIn(("dbos", "destroy"), worker_events)

    def test_unproven_listener_shutdown_preserves_ready_and_refuses_stopped_state(self) -> None:
        from release_host_health import HealthShutdownIncomplete

        events: list[tuple] = []
        saved: list[tuple] = []
        engine = _Engine(self.root, events, saved)
        directory = self.root / "release-host"
        directory.mkdir()
        ready = directory / "worker.ready"

        def blocked_worker(_root, *, ready_file, **_kwargs):
            Path(ready_file).write_text("still-published", encoding="utf-8")
            raise HealthShutdownIncomplete("listener join is unproven")

        with patch.object(orchestrator, "_worker_paths", return_value=(engine, directory, directory / "worker.log")), \
                patch.object(orchestrator, "publish_transport"), \
                patch.object(orchestrator, "worker", side_effect=blocked_worker), \
                patch.object(orchestrator, "runtime_fingerprint", return_value="f" * 64), \
                patch.object(orchestrator.secrets, "token_hex", return_value="a" * 64), \
                patch.object(orchestrator.os, "getpid", return_value=4321), \
                patch.object(orchestrator.fcntl, "flock"):
            with self.assertRaisesRegex(HealthShutdownIncomplete, "join is unproven"):
                orchestrator._foreground_worker(self.root, release_host=True)
        self.assertTrue(ready.is_file())
        self.assertEqual("still-published", ready.read_text(encoding="utf-8"))
        self.assertEqual(["starting"], [value["state"] for _, value in saved])


if __name__ == "__main__":
    unittest.main()
