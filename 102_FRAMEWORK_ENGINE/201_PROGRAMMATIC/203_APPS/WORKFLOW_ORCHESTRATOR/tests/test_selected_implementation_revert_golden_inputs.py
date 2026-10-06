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
                return {"result": "implemented", "outputs": {"candidate": packet["candidate"],
                                                                     "phase": packet["phase"],
                                                                     "changed_paths": ["fixture/implementation.py"]},
                        "evidence": [{"transport": "mock-not-live-llm"}]}
            result = implementation_actions.implement_selected_queue("CA-O-093", packet, mock_transport,
                                                                      selected_project_root=fixture.root)
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
            proposed = {"frontmatter": frontmatter, "content": content + "\nReverted detail.\n"}
            parameters = {"target": target, "proposed": proposed, "change_class": "semantic_revision",
                          "semantic_assessment_report": fixture._semantic_assessment_report(target, proposed)}
            # Forecast establishes the exact native post-effect descriptor; no inverse is invented.
            forecast = fixture.root / "forecast"; forecast.mkdir(); (forecast / ".git").mkdir();
            import shutil; shutil.copytree(fixture.root / ".caprmedio_caprmedio", forecast / ".caprmedio_caprmedio")
            forecast_target = lifecycle_intents.carrier_descriptor(forecast, "CA-R-100")
            with mock.patch.object(lifecycle_intents, "datetime", FrozenDatetime):
                predicted = lifecycle_intents.update_atom_action(forecast, {**parameters, "target": forecast_target}, execute=True, authorized=True)
            self.assertEqual("applied", predicted["outcome"], predicted)

            evidence_root = fixture.root / ".caprmedio_caprmedio/evidence"
            evidence_root.mkdir(parents=True, exist_ok=True)

            def record(name: str, value: object) -> dict[str, str]:
                path = evidence_root / name
                path.write_bytes(json.dumps(value, sort_keys=True, separators=(",", ":")).encode())
                return {"evidence_ref": path.relative_to(fixture.root).as_posix(),
                        "evidence_hash": hashlib.sha256(path.read_bytes()).hexdigest()}

            selected = record("selected-change.json", {"accepted": True, "selected_effect_ids": ["lifecycle-update"]})
            history = record("preserved.json", {"history": "retained", "references": "preserved"})
            before = record("lifecycle-before.json", {"state": "active version 1"})
            after = record("lifecycle-after.json", {"state": "active version 2"})
            permission = record("lifecycle-permission.json", {"capability_id": "lifecycle.update_atom", "granted": True})
            effect = {"effect_id": "lifecycle-update", "target_id": "atom:CA-R-100", "expected_before": "active version 1", "expected_after": "active version 2", "expected_current_hash": digest(target), "expected_result_hash": digest(predicted["observed"]), "before_evidence": before["evidence_ref"], "after_evidence": after["evidence_ref"],
                "capability_binding": {"capability_id": "lifecycle.update_atom", "parameters": parameters, "target": target, "permission_evidence": {"capability_id": "lifecycle.update_atom", "granted": True, **permission}, "evidence_refs": [before["evidence_ref"], after["evidence_ref"], history["evidence_ref"]]}}
            request = {"selected_change_refs": [selected["evidence_ref"]], "targets": ["atom:CA-R-100"], "affected_reference_hashes": {history["evidence_ref"]: history["evidence_hash"]}, "governing_definition_hash": "", "operator_decision": {"decision_id": "approved", "approved_effect_ids": ["lifecycle-update"], "status": "approved"}, "cancellation_boundary": {"after_effect_ids": ["lifecycle-update"]}, "executor_permission": {"capability": "governed-reversal", "granted": True}, "durable_evidence_location": "journal://fixture", "ordered_effects": [effect], "expected_result": {"state": "reverted"}, "history_reference_evidence": [history["evidence_ref"]], "current_hashes": {"atom:CA-R-100": digest(target)}, "selected_change": [selected], "history_record": [history], "affected_reference": [history], "before_record": [before], "after_record": [after]}
            definition = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-131-CORE_META_MODEL-ACTION--apply-an-approved-reversal.md"
            definition_target = fixture.root / definition
            definition_target.parent.mkdir(parents=True, exist_ok=True)
            definition_target.write_bytes((ROOT / definition).read_bytes())
            definition_pin = hashlib.sha256(definition_target.read_bytes()).hexdigest()
            request["governing_definition"] = {"atom_id": "CA-O-131", "revision": 2, "evidence_ref": definition, "evidence_hash": definition_pin}
            request["governing_definition_hash"] = definition_pin
            operator = request["operator_decision"]
            request["operator_decision"] = {**operator, **record("operator_decision.json", {**operator, "ordered_effects": request["ordered_effects"]})}
            executor = request["executor_permission"]
            request["executor_permission"] = {**executor, **record("executor_permission.json", executor)}
            service = make_native_revert_service({"project_root": str(fixture.root), "approved_reversal_request": request})
            stale = json.loads(json.dumps(request)); stale["current_hashes"]["atom:CA-R-100"] = "0" * 64
            self.assertEqual("blocked", service.handle({"operation": "admit", "reversal_request": stale})["outcome"])
            unsupported = json.loads(json.dumps(request)); unsupported["ordered_effects"][0]["capability_binding"]["capability_id"] = "file.write"
            with self.assertRaises(NativeRevertProviderError):
                make_native_revert_service({"project_root": str(fixture.root), "approved_reversal_request": unsupported})
            admitted = service.handle({"operation": "admit", "reversal_request": request})
            self.assertEqual("admitted", admitted["outcome"], admitted)
            with mock.patch.object(lifecycle_intents, "datetime", FrozenDatetime):
                result = service.execute_with_session(admitted["approved_reversal_manifest"], Session(), "w10-action")
            self.assertEqual("reverted", result["outcome"]); self.assertIn("Reverted detail.", target_path.read_text(encoding="utf-8"))
            self.assertTrue(any((fixture.root / ".caprmedio_caprmedio").rglob("CA-R-100--target@1.md")))
        finally: lease.cleanup()


if __name__ == "__main__": unittest.main()
