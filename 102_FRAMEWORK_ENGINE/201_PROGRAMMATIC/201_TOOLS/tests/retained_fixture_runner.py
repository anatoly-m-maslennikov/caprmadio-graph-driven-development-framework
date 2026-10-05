#!/usr/bin/env python3
"""Run explicitly selected ``unittest`` fixtures while retaining temp paths.

This is a test-only diagnostic runner.  It deliberately changes only
``TemporaryDirectory.cleanup``: cleanup detaches the finalizer so a fixture
directory remains available for inspection.  It neither catches test errors
nor changes their result; a failing selected test still returns exit status 1.

Example:
    python retained_fixture_runner.py tests.test_example.ExampleTests.test_case

The runner is intentionally not a Release gate and must not be used as
evidence that a fixture suite is clean.
"""

from __future__ import annotations

import argparse
import io
import shutil
import sys
import tempfile
import unittest
from collections.abc import Iterator, Sequence
from contextlib import contextmanager
from unittest.mock import patch


class RetainedTemporaryDirectory(tempfile.TemporaryDirectory[str]):
    """A deliberately retained test directory with no cleanup attempt."""

    def cleanup(self) -> None:
        """Detach the standard finalizer without invoking ``rmtree``."""

        self._finalizer.detach()


def format_retained_paths(paths: Sequence[str]) -> str:
    """Render retained paths even when the selected tests made none."""

    if not paths:
        return "retained_fixture_paths: (none)"
    return "retained_fixture_paths:\n" + "\n".join(f"- {path}" for path in paths)


@contextmanager
def retained_temporary_directories(paths: list[str]) -> Iterator[None]:
    """Route module-level ``tempfile.TemporaryDirectory`` calls to retention."""

    original = tempfile.TemporaryDirectory

    def create(*args: object, **kwargs: object) -> RetainedTemporaryDirectory:
        directory = RetainedTemporaryDirectory(*args, **kwargs)
        paths.append(directory.name)
        return directory

    tempfile.TemporaryDirectory = create  # type: ignore[assignment]
    try:
        yield
    finally:
        tempfile.TemporaryDirectory = original  # type: ignore[assignment]


def run_selected_tests(names: Sequence[str], *, stream: io.TextIOBase) -> unittest.TestResult:
    """Run selected test names unchanged and declare any retained directories."""

    paths: list[str] = []
    with retained_temporary_directories(paths):
        # Load within the retained boundary so tests that import
        # ``TemporaryDirectory`` directly receive the test-only carrier too.
        suite = unittest.defaultTestLoader.loadTestsFromNames(list(names))
        result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    stream.write(format_retained_paths(paths) + "\n")
    stream.flush()
    return result


class _DeliberatelyFailingCase(unittest.TestCase):
    def runTest(self) -> None:
        with tempfile.TemporaryDirectory():
            self.fail("intentional functional failure")


class RetainedFixtureRunnerDryTests(unittest.TestCase):
    """No-filesystem tests for the runner's retention and failure semantics."""

    def test_retention_detaches_cleanup_without_creating_or_removing_a_directory(self) -> None:
        with patch("tempfile.mkdtemp", return_value="/retained/mock-fixture") as created:
            with patch.object(shutil, "rmtree") as removed:
                directory = RetainedTemporaryDirectory()
                directory.cleanup()
        created.assert_called_once()
        removed.assert_not_called()
        self.assertEqual(directory.name, "/retained/mock-fixture")
        self.assertEqual(format_retained_paths([directory.name]), "retained_fixture_paths:\n- /retained/mock-fixture")

    def test_functional_failure_stays_a_failure_and_reports_retention_declaration(self) -> None:
        output = io.StringIO()
        with patch("tempfile.mkdtemp", return_value="/retained/mock-fixture"):
            with patch.object(shutil, "rmtree") as removed:
                result = run_selected_tests([f"{__name__}._DeliberatelyFailingCase"], stream=output)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(len(result.failures), 1)
        removed.assert_not_called()
        self.assertIn("retained_fixture_paths:\n- /retained/mock-fixture", output.getvalue())


def _arguments(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run selected unittest fixtures and retain their TemporaryDirectory paths.")
    parser.add_argument("tests", nargs="*", help="dotted unittest names")
    parser.add_argument("--self-test", action="store_true", help="run only the runner's no-filesystem dry tests")
    options = parser.parse_args(argv)
    if not options.self_test and not options.tests:
        parser.error("at least one dotted unittest name is required")
    return options


def main(argv: Sequence[str] | None = None) -> int:
    options = _arguments(argv)
    names = (
        [f"{__name__}.RetainedFixtureRunnerDryTests"]
        if options.self_test
        else options.tests
    )
    result = run_selected_tests(names, stream=sys.stdout)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
