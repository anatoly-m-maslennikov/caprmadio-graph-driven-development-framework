"""Native W09 mock-transport and W10 governed-revert golden inputs."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from unittest import mock


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
TOOLS = APP.parents[1] / "201_TOOLS"
IMPLEMENTATION = APP.parents[2] / "202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW"
REVERT = TOOLS / "WORKFLOW_OPERATIONS/REVERT_CHANGES"
for path in (TOOLS, IMPLEMENTATION, REVERT, Path(__file__).resolve().parent):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import implementation_actions  # noqa: E402
import lifecycle_intents  # noqa: E402
from native_revert_provider import NativeRevertProviderError, make_native_revert_service  # noqa: E402
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject  # noqa: E402


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


class Session:
    def start_run(self, requested_run_id: str) -> dict[str, str]: return {"run_id": requested_run_id}
    def finish_run(self, run_id: str, **kwargs: object) -> dict[str, object]: return {"run_id": run_id, **kwargs}


class FrozenDatetime(datetime):
    @classmethod
    def now(cls, tz: timezone | None = None) -> "FrozenDatetime":
        value = cls(2026, 10, 5, 12, 0, 0, tzinfo=timezone.utc)
        return value if tz is None else value.astimezone(tz)


class SelectedImplementationRevertGoldenInputsTest(unittest.TestCase):
    def _fixture(self, case: str, route: str) -> tuple[FixtureLease, GoldenProject]:
        parent = ROOT / ".caprmedio_tmp/tests/selected-implementation-revert-golden-inputs"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        fixture = GoldenProject(ROOT, root, GoldenCase(case, route)); fixture.prepare()
        return FixtureLease(root), fixture

    def test_w09_source_full_packets_drive_executable_mock_transport_not_live_llm(self) -> None:
        lease, fixture = self._fixture("W09", "run_implementation_workflow")
        try:
            parameters = fixture.native_parameters()
            packet = {**parameters["base_packet"], **parameters["step_packets"]["CA-O-093"]}
            implementation = fixture.root / "fixture/implementation.py"
            assertion = fixture.root / "fixture/assertion.py"
            implementation.write_text("def ready(): return False\n", encoding="utf-8")
            assertion.write_text("from implementation import ready\nassert ready()\n", encoding="utf-8")
            command = [sys.executable, str(assertion)]
            self.assertNotEqual(0, subprocess.run(command, cwd=implementation.parent, capture_output=True, text=True).returncode)
            def mock_transport(_prompt: str, _packet: dict) -> dict:
                implementation.write_text("def ready(): return True\n", encoding="utf-8")
                return {"result": "implemented", "outputs": {"candidate": "mock-transport", "changed_paths": ["fixture/implementation.py"]}, "evidence": [{"transport": "mock-not-live-llm"}]}
            result = implementation_actions.implement_selected_queue("CA-O-093", packet, mock_transport)
            self.assertEqual("implemented", result["result"], result)
            self.assertEqual(0, subprocess.run(command, cwd=implementation.parent, capture_output=True, text=True).returncode)
            self.assertEqual("mock-not-live-llm", parameters["base_packet"]["retained_state"]["transport"])
        finally: lease.cleanup()

    def test_w10_native_provider_reverts_only_current_approved_lifecycle_effect(self) -> None:
        lease, fixture = self._fixture("W10", "revert_changes")
        try:
            target_path = fixture.root / ".caprmedio_caprmedio/04_requirement/CA-R-100--target.md"
            target = lifecycle_intents.carrier_descriptor(fixture.root, "CA-R-100")
            text = target_path.read_text(encoding="utf-8"); frontmatter, content = text[4:].split("\n---\n", 1)
            parameters = {"target": target, "proposed": {"frontmatter": frontmatter, "content": content + "\nReverted detail.\n"}, "change_class": "semantic_revision"}
            # Forecast establishes the exact native post-effect descriptor; no inverse is invented.
            forecast = fixture.root / "forecast"; forecast.mkdir(); (forecast / ".git").mkdir();
            import shutil; shutil.copytree(fixture.root / ".caprmedio_caprmedio", forecast / ".caprmedio_caprmedio")
            forecast_target = lifecycle_intents.carrier_descriptor(forecast, "CA-R-100")
            with mock.patch.object(lifecycle_intents, "datetime", FrozenDatetime):
                predicted = lifecycle_intents.update_atom_action(forecast, {**parameters, "target": forecast_target}, execute=True, authorized=True)
            before, after = "before:fixture", "after:fixture"
            effect = {"effect_id": "lifecycle-update", "target_id": "atom:CA-R-100", "expected_before": "active version 1", "expected_after": "active version 2", "expected_current_hash": digest(target), "expected_result_hash": digest(predicted["observed"]), "before_evidence": before, "after_evidence": after,
                "capability_binding": {"capability_id": "lifecycle.update_atom", "parameters": parameters, "target": target, "permission_evidence": {"capability_id": "lifecycle.update_atom", "granted": True, "evidence_ref": "permission:fixture", "evidence_hash": "c" * 64}, "evidence_refs": [before, after, "history:preserved", "references:preserved"]}}
            request = {"selected_change_refs": ["event:accepted"], "targets": ["atom:CA-R-100"], "affected_reference_hashes": {"reference:preserved": "a" * 64}, "governing_definition_hash": "b" * 64, "operator_decision": {"decision_id": "approved", "approved_effect_ids": ["lifecycle-update"], "status": "approved"}, "cancellation_boundary": {"after_effect_ids": ["lifecycle-update"]}, "executor_permission": {"capability": "governed-reversal", "granted": True}, "durable_evidence_location": "journal://fixture", "ordered_effects": [effect], "expected_result": {"state": "reverted"}, "history_reference_evidence": ["history:preserved", "references:preserved"], "current_hashes": {"atom:CA-R-100": digest(target)}}
            service = make_native_revert_service({"project_root": str(fixture.root), "approved_reversal_request": request})
            stale = json.loads(json.dumps(request)); stale["current_hashes"]["atom:CA-R-100"] = "0" * 64
            self.assertEqual("blocked", service.handle({"operation": "admit", "reversal_request": stale})["outcome"])
            unsupported = json.loads(json.dumps(request)); unsupported["ordered_effects"][0]["capability_binding"]["capability_id"] = "file.write"
            with self.assertRaises(NativeRevertProviderError):
                make_native_revert_service({"project_root": str(fixture.root), "approved_reversal_request": unsupported})
            admitted = service.handle({"operation": "admit", "reversal_request": request})
            with mock.patch.object(lifecycle_intents, "datetime", FrozenDatetime):
                result = service.execute_with_session(admitted["approved_reversal_manifest"], Session(), "w10-action")
            self.assertEqual("reverted", result["outcome"]); self.assertIn("Reverted detail.", target_path.read_text(encoding="utf-8"))
            self.assertTrue(any((fixture.root / ".caprmedio_caprmedio").rglob("CA-R-100--target@1.md")))
        finally: lease.cleanup()


if __name__ == "__main__": unittest.main()
