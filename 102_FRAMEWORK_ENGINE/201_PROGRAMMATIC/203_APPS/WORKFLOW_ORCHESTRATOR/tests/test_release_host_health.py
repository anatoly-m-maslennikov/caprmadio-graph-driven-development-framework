"""Private release-host health nonce exchange; no worker, DBOS, or network."""
from __future__ import annotations

import json
import math
from pathlib import Path
import stat
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

import release_host_health as health  # noqa: E402
from release_host_health import HealthError, probe_worker, start_listener  # noqa: E402


class ReleaseHostHealthTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = APP.parents[3] / ".caprmedio_tmp/tests/release-host-health"
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

    def listener(self):
        handle = start_listener(self.root, self.identity)
        self.addCleanup(handle.close)
        return handle

    def health_paths(self) -> tuple[Path, Path]:
        health_root = self.root / ".caprmedio_install/workflow_orchestrator/release-host/health"
        requests, replies = health_root / "requests", health_root / "replies"
        requests.mkdir(parents=True, exist_ok=True)
        replies.mkdir(parents=True, exist_ok=True)
        return requests, replies

    def test_fresh_exact_identity_probes_without_legacy_signal_admission(self) -> None:
        self.listener()

        # The helper is the authoritative path.  A legacy signal observation is
        # intentionally not part of this API and may be sandbox-denied.
        self.assertIsNone(probe_worker(self.root, self.identity))

    def test_wrong_identity_and_malformed_identity_fail_closed(self) -> None:
        self.listener()
        for value in (
            self.identity | {"pid": 54321},
            self.identity | {"start_token": "c" * 64},
            self.identity | {"runtime_fingerprint": "d" * 64},
            {key: value for key, value in self.identity.items() if key != "start_token"},
            self.identity | {"state": "starting"},
        ):
            with self.subTest(value=value), self.assertRaises(HealthError):
                probe_worker(self.root, value)

    def test_listener_rejects_invalid_identity_before_private_carrier_creation(self) -> None:
        for value in (
            self.identity | {"start_token": "A" * 64},
            self.identity | {"runtime_fingerprint": "bad"},
            self.identity | {"pid": 0},
            self.identity | {"unexpected": "field"},
        ):
            with self.subTest(value=value), self.assertRaises(HealthError):
                start_listener(self.root, value)
        self.assertFalse((self.root / ".caprmedio_install").exists())

    def test_stale_oversized_and_symlinked_private_carriers_refuse_before_probe_publication(self) -> None:
        requests, replies = self.health_paths()
        nonce = "e" * 64
        stale = {"nonce": nonce, "deadline_monotonic": 0.0, **self.identity}
        (replies / f"{nonce}.json").write_text(json.dumps(stale), encoding="utf-8")
        with self.assertRaises(HealthError):
            probe_worker(self.root, self.identity)
        (replies / f"{nonce}.json").unlink()
        oversized = replies / ("f" * 64 + ".json")
        oversized.write_bytes(b"x" * 4097)
        with self.assertRaises(HealthError):
            probe_worker(self.root, self.identity)
        oversized.unlink()
        unsafe = requests / ("0" * 64 + ".json")
        unsafe.symlink_to(self.root / "outside")
        with self.assertRaises(HealthError):
            probe_worker(self.root, self.identity)

    def test_regular_ds_store_is_ignored_but_other_wrong_named_carriers_fail_closed(self) -> None:
        requests, _ = self.health_paths()
        (requests / ".DS_Store").write_bytes(b"finder metadata")

        self.assertEqual({}, health._message_files(requests))

        (requests / "not-a-nonce.json").write_text("{}", encoding="utf-8")
        with self.assertRaisesRegex(HealthError, "carrier is unsafe"):
            health._message_files(requests)

    def test_listener_close_stops_and_joins_before_carrier_removal(self) -> None:
        handle = self.listener()
        handle.close()
        handle.close()
        with self.assertRaises(HealthError):
            probe_worker(self.root, self.identity)

    def test_probe_rejects_sixty_four_pending_requests_without_listener_cleanup_race(self) -> None:
        requests, _ = self.health_paths()
        now = 100.0
        payload = {"nonce": "0" * 64, "deadline_monotonic": now + 1.0, **self.identity}
        for index in range(64):
            nonce = f"{index:064x}"
            (requests / f"{nonce}.json").write_text(json.dumps({**payload, "nonce": nonce}), encoding="utf-8")
        with patch.object(health.time, "monotonic", return_value=now):
            with self.assertRaisesRegex(HealthError, "backlog is full"):
                probe_worker(self.root, self.identity)

    def test_probe_publishes_exact_seven_field_finite_two_second_exchange(self) -> None:
        requests, replies = self.health_paths()
        nonce = "c" * 64
        captured: list[dict] = []
        request_path = requests / f"{nonce}.json"
        reply_path = replies / f"{nonce}.json"
        lock = MagicMock()
        lock.__enter__.return_value = lock
        lock.__exit__.return_value = False

        def publish(_path, value, _staging):
            captured.append(dict(value))

        scans = iter((({}, {}), ({nonce: request_path}, {nonce: reply_path})))
        with patch.object(health, "_CapacityLock", return_value=lock), \
                patch.object(health, "_scan", side_effect=lambda *_args: next(scans)), \
                patch.object(health, "_atomic_create", side_effect=publish), \
                patch.object(health, "_unlink_exact"), \
                patch.object(health, "_read_message", side_effect=lambda _path: captured[0]), \
                patch.object(health.secrets, "token_hex", return_value=nonce), \
                patch.object(health.time, "monotonic", side_effect=(100.0, 100.1, 100.2)):
            self.assertIsNone(probe_worker(self.root, self.identity))
        self.assertEqual(1, len(captured))
        exchange = captured[0]
        self.assertEqual({"nonce", "deadline_monotonic", "pid", "start_token",
                          "application_version", "runtime_fingerprint", "state"}, set(exchange))
        self.assertEqual(nonce, exchange["nonce"])
        self.assertTrue(math.isfinite(exchange["deadline_monotonic"]))
        self.assertGreater(exchange["deadline_monotonic"], 100.0)
        self.assertLessEqual(exchange["deadline_monotonic"], 102.0)

    def test_probe_rejects_a_wrong_nonce_reply_with_a_mocked_read_seam(self) -> None:
        requests, replies = self.health_paths()
        nonce, wrong_nonce = "c" * 64, "d" * 64
        request_path = requests / f"{nonce}.json"
        reply_path = replies / f"{nonce}.json"
        captured: list[dict] = []
        lock = MagicMock()
        lock.__enter__.return_value = lock
        lock.__exit__.return_value = False

        def publish(_path, value, _staging):
            captured.append(dict(value))

        scans = iter((({}, {}), ({nonce: request_path}, {nonce: reply_path})))

        def read(_path):
            return {**captured[0], "nonce": wrong_nonce}

        with patch.object(health, "_CapacityLock", return_value=lock), \
                patch.object(health, "_scan", side_effect=lambda *_args: next(scans)), \
                patch.object(health, "_atomic_create", side_effect=publish), \
                patch.object(health, "_unlink_exact"), \
                patch.object(health, "_read_message", side_effect=read), \
                patch.object(health.secrets, "token_hex", return_value=nonce), \
                patch.object(health.time, "monotonic", side_effect=(100.0, 100.1, 100.2)):
            with self.assertRaisesRegex(HealthError, "reply does not match"):
                probe_worker(self.root, self.identity)

    def test_replaced_fifo_is_rejected_with_nonblocking_open_before_any_read(self) -> None:
        carrier = self.root / ("e" * 64 + ".json")
        descriptor = 91
        fifo = SimpleNamespace(st_mode=stat.S_IFIFO, st_size=0)
        with patch.object(health.os, "open", return_value=descriptor) as opened, \
                patch.object(health.os, "fstat", return_value=fifo), \
                patch.object(health.os, "read") as read, \
                patch.object(health.os, "close") as close:
            with self.assertRaisesRegex(HealthError, "unsafe"):
                health._read_message(carrier)
        flags = opened.call_args.args[1]
        self.assertTrue(flags & health.os.O_NONBLOCK)
        read.assert_not_called()
        close.assert_called_once_with(descriptor)


if __name__ == "__main__":
    unittest.main()
