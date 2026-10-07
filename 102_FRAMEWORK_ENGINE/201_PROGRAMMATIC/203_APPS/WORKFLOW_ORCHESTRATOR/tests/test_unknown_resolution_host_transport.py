"""Red-first transport boundary for the one host-isolated unknown-effect resolution."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

import release_host_bridge as bridge  # noqa: E402
import release_unknown_effect_resolution as resolver  # noqa: E402


class UnknownResolutionHostTransportTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = APP.parents[3] / ".caprmedio_tmp/tests/unknown-resolution-host-transport"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        interpreter = self.root / bridge.FIXED_INTERPRETER
        interpreter.parent.mkdir(parents=True)
        interpreter.write_text("fixture interpreter", encoding="utf-8")

    def request(self) -> dict[str, str]:
        return {
            "operation": resolver._OPERATION,
            "run_id": resolver._RUN_ID,
            "request_identity": resolver._REQUEST_IDENTITY,
            "authorization_ref": resolver._AUTHORIZATION_REF,
            "authorization_sha256": resolver._AUTHORIZATION_SHA256,
            "expected_checkpoint_sha256": resolver._CHECKPOINT_SHA256,
        }

    def test_exact_six_key_unknown_resolution_uses_fixed_host_cli_without_ready_worker(self) -> None:
        request = self.request()
        expected = {"operation": resolver._OPERATION, "disposition": "terminalized"}
        with patch("release_host_bridge.binding") as bound, \
             patch("release_host_bridge.availability") as ready, \
             patch("release_host_bridge.subprocess.run", return_value=SimpleNamespace(
                 returncode=0, stdout=json.dumps(expected),
             )) as launched:
            result = bridge.invoke(self.root, request)

        self.assertEqual(expected, result)
        bound.assert_not_called()
        ready.assert_not_called()
        command = launched.call_args.args[0]
        self.assertEqual([str(self.root / bridge.FIXED_INTERPRETER), str(APP / "orchestrator.py"),
                          "--project-root", str(self.root), resolver._OPERATION], command)
        self.assertNotIn("shell", launched.call_args.kwargs)
        self.assertFalse(launched.call_args.kwargs["check"])
        self.assertEqual(request, json.loads(launched.call_args.kwargs["input"]))

    def test_malformed_unknown_request_refuses_without_ready_check_or_subprocess(self) -> None:
        malformed = self.request() | {"caller_command": "arbitrary"}
        with patch("release_host_bridge.binding") as bound, \
             patch("release_host_bridge.availability") as ready, \
             patch("release_host_bridge.subprocess.run") as launched:
            with self.assertRaises((ValueError, bridge.ReleaseHostUnavailable)):
                bridge.invoke(self.root, malformed)
        bound.assert_not_called()
        ready.assert_not_called()
        launched.assert_not_called()

    def test_ordinary_recovery_retains_ready_worker_guard(self) -> None:
        request = {"operation": "recover_selected_release", "run_id": "ordinary-recovery"}
        bridge.retain_binding(self.root, run_id="ordinary-recovery", frozen_request_digest="a" * 64)
        with patch("release_host_bridge.availability", side_effect=bridge.ReleaseHostUnavailable("not ready")) as ready, \
             patch("release_host_bridge.subprocess.run") as launched:
            with self.assertRaisesRegex(bridge.ReleaseHostUnavailable, "not ready"):
                bridge.invoke(self.root, request)
        ready.assert_called_once()
        launched.assert_not_called()


if __name__ == "__main__":
    unittest.main()
