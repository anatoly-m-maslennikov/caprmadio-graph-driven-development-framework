"""Pure validation tests for the retired-image shared receipt handoff."""
from __future__ import annotations

from pathlib import Path
import sys
from types import SimpleNamespace
import unittest


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

from selected_execution import SelectedExecutionError
from selected_native_providers import SelectedNativeProviders


SHA = "a" * 64
PRIOR = "sha256:" + "b" * 64
RECEIPT = "c" * 64
REF = "_journal/release/retire/receipt.json"


def result(*, packet=None, **overrides):
    packet = packet if packet is not None else {
        "on_recorded_result": "release retired",
        "candidate_snapshot_manifest_sha256": SHA,
        "prior_image_digest": PRIOR,
        "retirement_receipt_ref": REF,
        "retirement_receipt_sha256": RECEIPT,
    }
    values = {
        "outcome": "pending", "effect_outcome": "retired", "phase": "retire",
        "workflow_run_id": "wf-1", "step_run_id": "step-1", "action_run_id": "action-1",
        "step_atom_id": "CA-O-179", "action_atom_id": "CA-O-169",
        "candidate_snapshot_manifest_sha256": SHA,
        "shared_action_recording": packet,
        "output": SimpleNamespace(prior_image_digest=PRIOR, receipt_sha256=RECEIPT),
    }
    values.update(overrides)
    return SimpleNamespace(**values)


class ReleaseRecordingHandshakeTests(unittest.TestCase):
    def validate(self, value, refs=None):
        return SelectedNativeProviders._shared_retirement_recording(
            value, candidate_sha256=SHA, workflow_run_id="wf-1", step_run_id="step-1",
            action_run_id="action-1", step_atom_id="CA-O-179", action_atom_id="CA-O-169",
            frozen_result="release retired", effect_refs=refs if refs is not None else [REF],
        )

    def test_accepts_only_exact_retired_result_handoff(self):
        self.assertEqual(self.validate(result())["retirement_receipt_sha256"], RECEIPT)

    def test_rejects_non_pending_or_non_retired_private_result(self):
        for overrides in ({"outcome": "completed"}, {"effect_outcome": "retained"}):
            with self.subTest(overrides=overrides), self.assertRaises(SelectedExecutionError):
                self.validate(result(**overrides))

    def test_rejects_foreign_identity_and_candidate(self):
        for overrides in ({"action_run_id": "other"}, {"candidate_snapshot_manifest_sha256": "d" * 64}):
            with self.subTest(overrides=overrides), self.assertRaises(SelectedExecutionError):
                self.validate(result(**overrides))

    def test_rejects_frozen_edge_effect_reference_and_evidence_mismatches(self):
        for value, refs in (
            (result(packet={**result().shared_action_recording, "on_recorded_result": "other"}), [REF]),
            (result(), ["other/receipt.json"]),
            (result(output=SimpleNamespace(prior_image_digest="sha256:" + "d" * 64, receipt_sha256=RECEIPT)), [REF]),
        ):
            with self.subTest(value=value, refs=refs), self.assertRaises(SelectedExecutionError):
                self.validate(value, refs)

    def test_rejects_unknown_recording_fields(self):
        packet = {**result().shared_action_recording, "caller_terminal": "completed"}
        with self.assertRaises(SelectedExecutionError):
            self.validate(result(packet=packet))


if __name__ == "__main__":
    unittest.main()
