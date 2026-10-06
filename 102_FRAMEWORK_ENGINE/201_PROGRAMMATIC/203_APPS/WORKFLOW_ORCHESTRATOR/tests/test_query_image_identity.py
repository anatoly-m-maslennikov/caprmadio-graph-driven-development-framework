"""Pure admission tests for the opt-in query Docker image identity."""
from __future__ import annotations

import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


TESTS = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS))

import test_selected_query_mcp_e2e as query  # noqa: E402


IMAGE = "sha256:" + "b" * 64


class QueryImageIdentityTests(unittest.TestCase):
    """No Docker process, container, temporary carrier, or opt-in Run here."""

    def test_required_query_image_accepts_one_lowercase_immutable_identity(self) -> None:
        self.assertEqual(IMAGE, query._required_query_image({"CAPRMEDIO_DOCKER_QUERY_IMAGE": IMAGE}))

    def test_missing_or_empty_query_image_is_rejected(self) -> None:
        for environment in ({}, {"CAPRMEDIO_DOCKER_QUERY_IMAGE": ""}):
            with self.subTest(environment=environment):
                with self.assertRaisesRegex(AssertionError, "CAPRMEDIO_DOCKER_QUERY_IMAGE"):
                    query._required_query_image(environment)

    def test_mutable_or_malformed_query_image_is_rejected(self) -> None:
        for value in ("caprmedio-runtime:local", "sha256:" + "B" * 64, "sha256:" + "b" * 63, 1):
            with self.subTest(value=value):
                with self.assertRaisesRegex(AssertionError, "immutable sha256"):
                    query._required_query_image({"CAPRMEDIO_DOCKER_QUERY_IMAGE": value})

    def test_selected_identity_propagates_to_runtime_environment(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runtime = query.strict.Runtime(Path(directory), mock=True, image=IMAGE)
            with patch.dict(os.environ, {"CAPRMEDIO_IMAGE": "sha256:" + "c" * 64}, clear=False):
                self.assertEqual(IMAGE, runtime.environment()["CAPRMEDIO_IMAGE"])


if __name__ == "__main__":
    unittest.main()
