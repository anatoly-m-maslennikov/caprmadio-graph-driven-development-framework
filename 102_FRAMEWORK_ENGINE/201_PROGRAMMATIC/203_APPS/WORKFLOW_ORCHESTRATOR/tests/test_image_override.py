"""Image selection is pure configuration; Docker is not invoked here."""

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
sys.path.insert(0, str(APP / "docker"))

import docker_bridge  # noqa: E402
import runtime  # noqa: E402


IMMUTABLE_IMAGE = "sha256:" + "a" * 64


class ImageOverrideTests(unittest.TestCase):
    def test_runtime_uses_explicit_immutable_image(self):
        self.assertEqual(
            IMMUTABLE_IMAGE, runtime.image_reference({"CAPRMEDIO_IMAGE": IMMUTABLE_IMAGE})
        )
        with tempfile.TemporaryDirectory() as directory:
            instance = runtime.Runtime(Path(directory), mock=True, image=IMMUTABLE_IMAGE)
            with patch.dict(runtime.os.environ, {"CAPRMEDIO_IMAGE": "sha256:" + "b" * 64}):
                self.assertEqual(IMMUTABLE_IMAGE, instance.environment()["CAPRMEDIO_IMAGE"])

    def test_runtime_empty_override_uses_safe_development_fallback(self):
        self.assertEqual(runtime.IMAGE, runtime.image_reference({"CAPRMEDIO_IMAGE": ""}))

    def test_bridge_preserves_explicit_immutable_image(self):
        environment = docker_bridge._environment(
            Path("/project"), {"CAPRMEDIO_IMAGE": IMMUTABLE_IMAGE}
        )
        self.assertEqual(IMMUTABLE_IMAGE, environment["CAPRMEDIO_IMAGE"])
        self.assertEqual("/project", environment["CAPRMEDIO_PROJECT_ROOT"])

    def test_bridge_empty_override_uses_safe_development_fallback(self):
        environment = docker_bridge._environment(Path("/project"), {"CAPRMEDIO_IMAGE": ""})
        self.assertEqual(docker_bridge.IMAGE, environment["CAPRMEDIO_IMAGE"])

    def test_mutable_or_malformed_overrides_are_rejected(self):
        for value in ("alpine:latest", "sha256:" + "A" * 64, "sha256:" + "a" * 63, 1):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "immutable sha256"):
                    runtime.image_reference({"CAPRMEDIO_IMAGE": value})
                with self.assertRaisesRegex(ValueError, "immutable sha256"):
                    docker_bridge._environment(Path("/project"), {"CAPRMEDIO_IMAGE": value})


if __name__ == "__main__":
    unittest.main()
