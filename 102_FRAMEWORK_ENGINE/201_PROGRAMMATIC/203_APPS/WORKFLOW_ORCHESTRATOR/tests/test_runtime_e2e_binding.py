"""Public Runtime boundary checks for sealed Release E2E image binding."""

from __future__ import annotations

import os
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP / "docker"))

from runtime import Runtime, main  # noqa: E402


IMAGE = "sha256:" + "a" * 64


class RuntimeE2EBindingTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = APP.parents[3] / ".caprmedio_tmp/tests/runtime-e2e-binding"
        parent.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(dir=parent))

    def test_explicit_sealed_image_wins_over_ambient_local_tag(self) -> None:
        with patch.dict(
            os.environ, {"CAPRMEDIO_IMAGE": "caprmedio-runtime:local"}, clear=False,
        ):
            runtime = Runtime(self.root, mock=True, image=IMAGE)
            self.assertEqual(IMAGE, runtime.environment()["CAPRMEDIO_IMAGE"])

    def test_default_runtime_image_resolution_is_unchanged(self) -> None:
        ambient = "sha256:" + "b" * 64
        with patch.dict(
            os.environ, {"CAPRMEDIO_IMAGE": ambient}, clear=False,
        ):
            runtime = Runtime(self.root, mock=True)
            self.assertEqual(ambient, runtime.environment()["CAPRMEDIO_IMAGE"])

    def test_exact_image_reaches_compose_without_mutating_process_environment(self) -> None:
        with patch.dict(
            os.environ, {"CAPRMEDIO_IMAGE": "caprmedio-runtime:local"}, clear=False,
        ):
            runtime = Runtime(self.root, mock=True, image=IMAGE)
            before = os.environ["CAPRMEDIO_IMAGE"]
            observed = SimpleNamespace(returncode=0, stdout="")
            with patch("runtime.subprocess.run", return_value=observed) as run:
                runtime.call("config", "--format", "json")
            self.assertEqual("caprmedio-runtime:local", os.environ["CAPRMEDIO_IMAGE"])
            self.assertEqual(before, os.environ["CAPRMEDIO_IMAGE"])
            self.assertIn("docker", run.call_args.args[0])
            self.assertEqual(IMAGE, run.call_args.kwargs["env"]["CAPRMEDIO_IMAGE"])
            self.assertEqual(str(self.root.resolve()), run.call_args.kwargs["env"]["CAPRMEDIO_PROJECT_ROOT"])

    def test_rejects_an_empty_explicit_image(self) -> None:
        with self.assertRaisesRegex(ValueError, "Runtime image"):
            Runtime(self.root, mock=True, image="")

    def test_private_cli_image_handoff_constructs_the_exact_runtime(self) -> None:
        with patch("runtime.Runtime") as runtime:
            runtime.return_value.status.return_value = {"outcome": "ready"}
            with patch.object(sys, "argv", ["runtime.py", "--project-root", str(self.root),
                                              "--image", IMAGE, "--mock", "status"]):
                main()
        self.assertEqual(IMAGE, runtime.call_args.kwargs["image"])


if __name__ == "__main__":
    unittest.main()
