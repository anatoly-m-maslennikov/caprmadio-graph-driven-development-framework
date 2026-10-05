"""Timing regressions for the Suite Owner's control-context checks.

These are deliberately pure fixture-seam tests.  They do not invoke Docker or
claim an image execution result: the executor records only whether the owner
would have reached its isolated-execution boundary.
"""

from __future__ import annotations

import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
import sys

if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

import release_suite  # noqa: E402
from release_suite_reference_context import ReleaseSuiteReferenceContextError  # noqa: E402


class _RecordingExecutor:
    """Fixture seam: records entry but does not run a process or image."""

    source_context_sha256 = "b" * 64
    image_path = "/fixture/isolated-image/bin"

    def __init__(self, on_run=None) -> None:
        self.calls = 0
        self.on_run = on_run

    def run(self, command, *, workspace, output_root, working_directory, environment, timeout_seconds):
        self.calls += 1
        if self.on_run is not None:
            self.on_run()
        return release_suite.SuiteExecutionResult(0, b"fixture stdout", b"fixture stderr")


class ReleaseSuiteContextTimingTests(unittest.TestCase):
    """A control-carrier change is caught on the correct side of execution."""

    def setUp(self) -> None:
        # Retain these small fixture trees: this host can refuse nested-temp
        # cleanup, and the tests never touch a Project carrier.
        self.root = Path(tempfile.mkdtemp(prefix="release-suite-context-timing-")).resolve()
        selector = self.root / release_suite.CURRENT_SELECTOR_RELATIVE
        selector.parent.mkdir(parents=True)
        selector.write_bytes(b"fixture selector\n")
        self.control = self.root / "controls" / "suite-control.toml"
        self.control.parent.mkdir()
        self.control.write_bytes(b"revision = 1\n")
        self.candidate = SimpleNamespace(
            manifest=SimpleNamespace(
                sha256="a" * 64,
                full_suite_environment=SimpleNamespace(
                    runner=release_suite.SUPPORTED_RUNNER,
                    command=release_suite.SUITE_DRIVER_COMMAND,
                    working_directory=".",
                ),
            ),
            authority=SimpleNamespace(executing_release="selected-n"),
        )
        self.compilation = SimpleNamespace(child_materialization_root="compiled-candidate")
        self.context = SimpleNamespace(
            trusted_binding_values=(
                ("candidate_snapshot_manifest_sha256", "a" * 64),
                ("compiled_candidate_root", "compiled-candidate"),
                ("selected_n_identity", "selected-n"),
                ("selected_n_image_context", "b" * 64),
            ),
            reference_rows=(),
            control_context_digest="c" * 64,
        )
        self.active_n = ("d" * 64, "e" * 64, "f" * 64)

    def _patches(self, executor, materialize, revalidate):
        stack = ExitStack()
        for seam in (
            patch.object(release_suite, "_validate_bound_inputs", return_value=self.root),
            patch.object(release_suite, "_active_n_state", return_value=self.active_n),
            patch.object(release_suite, "_capture_reference_context", return_value=self.context),
            patch.object(release_suite, "_materialize_suite_workspace", side_effect=materialize),
            patch.object(release_suite, "revalidate_context", side_effect=revalidate),
        ):
            stack.enter_context(seam)
        return stack

    def test_control_change_during_materialization_refuses_before_executor(self) -> None:
        events: list[str] = []
        executor = _RecordingExecutor(lambda: events.append("executor"))

        def materialize(*_args):
            events.append("materialize")
            self.control.write_bytes(b"revision = changed-before-executor\n")
            return "1" * 64

        def revalidate(*_args):
            events.append("pre-run-revalidate")
            if self.control.read_bytes() != b"revision = 1\n":
                raise ReleaseSuiteReferenceContextError("fixture control carrier changed")
            return self.context

        with self._patches(executor, materialize, revalidate):
            evidence = release_suite.execute_bound_release_suite(
                self.candidate, self.compilation, executor=executor,
            )

        self.assertEqual(events, ["materialize", "pre-run-revalidate"])
        self.assertEqual(executor.calls, 0)
        self.assertEqual(evidence.outcome, "recording_uncertain")
        self.assertIn("ReleaseSuiteReferenceContextError", evidence.reason)

    def test_control_change_by_executor_is_refused_by_post_run_revalidation(self) -> None:
        events: list[str] = []

        def mutate_after_execution():
            events.append("executor")
            self.control.write_bytes(b"revision = changed-after-executor\n")

        executor = _RecordingExecutor(mutate_after_execution)

        def materialize(*_args):
            events.append("materialize")
            return "2" * 64

        def revalidate(*_args):
            phase = "pre-run-revalidate" if "pre-run-revalidate" not in events else "post-run-revalidate"
            events.append(phase)
            if self.control.read_bytes() != b"revision = 1\n":
                raise ReleaseSuiteReferenceContextError("fixture control carrier changed")
            return self.context

        with self._patches(executor, materialize, revalidate), \
                patch.object(release_suite, "_observe_report", return_value=(1, ("Tools",), "")):
            evidence = release_suite.execute_bound_release_suite(
                self.candidate, self.compilation, executor=executor,
            )

        self.assertEqual(events, ["materialize", "pre-run-revalidate", "executor", "post-run-revalidate"])
        self.assertEqual(executor.calls, 1)
        self.assertEqual(evidence.outcome, "stale")
        self.assertIn("post-suite bindings no longer validate", evidence.reason)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
