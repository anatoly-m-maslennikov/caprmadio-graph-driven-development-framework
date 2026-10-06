"""Checkpoint coverage for the sealed Release-suite control-context digest.

The codec is structural: it preserves the typed private frontier without
opening durable carriers.  The next Release phase reopens the trusted suite
receipt before it can stage a package or invoke Docker.
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_actions import (  # noqa: E402
    PHASES,
    ReleaseActionRun,
    ReleasePhaseResult,
    SelectedReleaseActionContext,
    _fingerprint,
)
from release_checkpoint import (  # noqa: E402
    dump_release_checkpoint,
    load_release_checkpoint,
    release_action_checkpoint_sha256,
    restore_release_action_checkpoint,
)
from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import SealedSourceCopy  # noqa: E402
from release_suite import SuiteGateEvidence  # noqa: E402
from test_release_checkpoint import (  # noqa: E402
    PROJECT_ROOT,
    _candidate,
    _compilation,
    _digest,
    _preflight,
    _request,
)


class ReleaseSuiteContextCheckpointTests(unittest.TestCase):
    """The checkpoint codec must not weaken the D580 context binding."""

    def setUp(self) -> None:
        self.candidate = _candidate()
        self.request = _request(self.candidate)
        self.context_digest = "a" * 64

    def _run_with_suite(self) -> ReleaseActionRun:
        run = ReleaseActionRun(
            PROJECT_ROOT,
            "checkpoint-suite-context",
            _fingerprint(self.request),
            self.request,
        )
        compilation = _compilation(self.candidate)
        source_copy = SealedSourceCopy(
            self.candidate,
            compilation.source_copy_root,
            compilation.actual_derived_source_copy_sha256,
        )
        suite = SuiteGateEvidence(
            candidate_snapshot_manifest_sha256=self.candidate.manifest.sha256,
            outcome="passed",
            reason="complete bound suite execution",
            runner="local-subprocess",
            command=("python", "run_release_suite.py"),
            working_directory=".",
            exit_code=0,
            executed_tests=3,
            coverage=("Methodology", "Tools", "Apps", "MCP", "Agentic", "Skill"),
            evidence_root=".caprmedio_runtime/release_suite/checkpoint-context",
            stdout_sha256=_digest("b"),
            stderr_sha256=_digest("c"),
            report_sha256=_digest("d"),
            executing_selector_sha256=_digest("e"),
            executing_release_package_sha256=_digest("f"),
            executing_skill_sha256=_digest("0"),
            receipt_sha256=_digest("1"),
            elapsed_seconds=0.01,
            control_context_digest=self.context_digest,
        )
        outputs = (self.candidate, self.candidate, source_copy, compilation, suite)
        run.candidate = self.candidate
        run.preflight = _preflight(self.candidate)
        run.source_copy = source_copy
        run.compilation = compilation
        run.suite = suite
        for index, output in enumerate(outputs):
            context = SelectedReleaseActionContext(
                PROJECT_ROOT,
                run.workflow_run_id,
                f"step-{index}",
                f"action-{index}",
                run.workflow_run_id,
                f"step-{index}",
                *PHASES[index][:2],
                run.frozen_parameters_sha256,
            )
            run.contexts[index] = context
            run.results[index] = ReleasePhaseResult(
                run.workflow_run_id,
                context.step_run_id,
                context.action_run_id,
                *PHASES[index],
                "completed",
                "observed",
                self.candidate.manifest.sha256,
                (),
                (),
                ("journal-event-1",),
                output=output,
            )
        run.next_phase = len(outputs)
        return run

    def test_round_trip_and_recovery_preserve_control_context_digest(self) -> None:
        run = self._run_with_suite()
        payload = dump_release_checkpoint(run)

        restored = restore_release_action_checkpoint(
            json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
        )
        recovered, recordings = load_release_checkpoint(
            payload,
            expected_request=self.request,
            expected_workflow_run_id=run.workflow_run_id,
        )

        self.assertEqual(restored.suite.control_context_digest, self.context_digest)
        self.assertEqual(recovered.suite.control_context_digest, self.context_digest)
        self.assertEqual(recordings, {})

    def test_missing_control_context_digest_is_rejected(self) -> None:
        payload = dump_release_checkpoint(self._run_with_suite())

        missing = json.loads(json.dumps(payload))
        missing["state"]["suite"]["value"].pop("control_context_digest")
        missing["sha256"] = release_action_checkpoint_sha256(missing)
        with self.assertRaises(ReleaseContractError):
            restore_release_action_checkpoint(json.dumps(missing, sort_keys=True, separators=(",", ":")).encode("utf-8"))

    def test_resealed_context_is_structurally_decodable(self) -> None:
        """Receipt reopening, rather than the codec, rejects this context."""

        payload = dump_release_checkpoint(self._run_with_suite())
        tampered = json.loads(json.dumps(payload))
        tampered["state"]["suite"]["value"]["control_context_digest"] = "0" * 64
        # The phase result retains the same Suite observation independently.
        # Altering only state would be caught by ordinary state/result equality,
        # not by validation of the digest itself.
        suite_result = next(record for record in tampered["results"] if record["index"] == 4)
        suite_result["result"]["output"]["value"]["control_context_digest"] = "0" * 64
        tampered["sha256"] = release_action_checkpoint_sha256(tampered)
        restored = restore_release_action_checkpoint(
            json.dumps(tampered, sort_keys=True, separators=(",", ":")).encode("utf-8")
        )
        self.assertEqual(restored.suite.control_context_digest, "0" * 64)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
