"""Disposable-project proofs for the CA-O-131 native effect provider."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


PACKAGE = Path(__file__).resolve().parents[1]
TOOLS = PACKAGE.parents[1]
STRUCTURE = TOOLS / "WORKFLOW_OPERATIONS" / "PROJECT_STRUCTURE"
for path in (PACKAGE, TOOLS, STRUCTURE):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import lifecycle_intents  # noqa: E402
from native_revert_provider import (  # noqa: E402
    NativeRevertProvider,
    NativeRevertProviderError,
    make_native_revert_service,
)


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


def canonical_digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


class FrozenDatetime(datetime):
    @classmethod
    def now(cls, tz: timezone | None = None) -> "FrozenDatetime":
        result = cls(2026, 10, 5, 12, 0, 0, tzinfo=timezone.utc)
        return result if tz is None else result.astimezone(tz)


class SharedActionSession:
    """Minimal J01--J08-shaped session stand-in; it owns one Action run only."""

    def __init__(self) -> None:
        self.starts: list[str] = []
        self.finishes: list[tuple[str, str]] = []
        self.pending: list[str] = []

    def start_run(self, requested_run_id: str) -> dict[str, str]:
        self.starts.append(requested_run_id)
        return {"run_id": f"actual-{requested_run_id}"}

    def finish_run(self, run_id: str, *, outcome: str, result_ref: str, effect_refs: list[str]) -> dict[str, object]:
        self.finishes.append((run_id, outcome))
        return {"run_id": run_id, "outcome": outcome, "result_ref": result_ref,
                "effect_refs": effect_refs, "disposition": "terminal"}


class NativeRevertProviderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = \".caprmedio_caprmedio\"\n\n[authority_modes]\ndefault = \"strict\"\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _atom(self, root: Path) -> Path:
        path = root / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/04_requirement/CA-R-100--target.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\natom_id: CA-R-100\ncontent_role: Requirement\nstatus: Active\nversion: 1\n"
            "updated_at: 2026-10-01 00:00:00 +0000\nrelations: {}\n---\n"
            "# Summary\n\nStable summary\n\n## Scope\n\nFixture scope.\n",
            encoding="utf-8",
        )
        return path

    @staticmethod
    def _proposal(path: Path) -> dict[str, str]:
        text = path.read_text(encoding="utf-8")
        frontmatter, content = text[4:].split("\n---\n", 1)
        return {"frontmatter": frontmatter, "content": content + "\nSemantic reversal detail.\n"}

    @staticmethod
    def _request(effect: dict[str, object], current_hash: str) -> dict[str, object]:
        return {
            "selected_change_refs": ["event:accepted-1", "revision:7"],
            "targets": [effect["target_id"]],
            "affected_reference_hashes": {"reference:preserved": "a" * 64},
            "governing_definition_hash": "b" * 64,
            "operator_decision": {"decision_id": "approved-1", "approved_effect_ids": [effect["effect_id"]], "status": "approved"},
            "cancellation_boundary": {"after_effect_ids": [effect["effect_id"]]},
            "executor_permission": {"capability": "governed-reversal", "granted": True},
            "durable_evidence_location": "journal://disposable-test",
            "ordered_effects": [effect],
            "expected_result": {"state": "reverted"},
            "history_reference_evidence": ["history:preserved", "references:preserved"],
            "current_hashes": {effect["target_id"]: current_hash},
        }

    @staticmethod
    def _binding(capability_id: str, parameters: dict[str, object], target: dict[str, object], *, before: str, after: str) -> dict[str, object]:
        return {
            "capability_id": capability_id,
            "parameters": parameters,
            "target": target,
            "permission_evidence": {
                "capability_id": capability_id,
                "granted": True,
                "evidence_ref": f"permission:{capability_id}",
                "evidence_hash": "c" * 64,
            },
            "evidence_refs": [before, after, "history:preserved", "references:preserved"],
        }

    def test_factory_executes_exact_lifecycle_effect_through_one_shared_action_run(self) -> None:
        target_path = self._atom(self.root)
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT) as forecast_raw:
            forecast = Path(forecast_raw)
            (forecast / ".git").mkdir()
            (forecast / ".caprmedio_caprmedio").mkdir()
            (forecast / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
                (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").read_text(encoding="utf-8"), encoding="utf-8"
            )
            forecast_path = self._atom(forecast)
            with mock.patch.object(lifecycle_intents, "datetime", FrozenDatetime):
                forecast_target = lifecycle_intents.carrier_descriptor(forecast, "CA-R-100")
                forecast_result = lifecycle_intents.update_atom_action(
                    forecast,
                    {"target": forecast_target, "proposed": self._proposal(forecast_path), "change_class": "semantic_revision"},
                    execute=True,
                    authorized=True,
                )
                expected_result_hash = canonical_digest(forecast_result["observed"])
                target = lifecycle_intents.carrier_descriptor(self.root, "CA-R-100")
                before, after = "before:lifecycle-update", "after:lifecycle-update"
                parameters = {"target": target, "proposed": self._proposal(target_path), "change_class": "semantic_revision"}
                effect: dict[str, object] = {
                    "effect_id": "lifecycle-update", "target_id": "atom:CA-R-100",
                    "expected_before": "active version 1", "expected_after": "active version 2",
                    "expected_current_hash": canonical_digest(target), "expected_result_hash": expected_result_hash,
                    "before_evidence": before, "after_evidence": after,
                    "capability_binding": self._binding("lifecycle.update_atom", parameters, target, before=before, after=after),
                }
                request = self._request(effect, str(effect["expected_current_hash"]))
                service = make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": request})
                admitted = service.handle({"operation": "admit", "reversal_request": request})
                self.assertEqual("admitted", admitted["outcome"])
                session = SharedActionSession()
                result = service.execute_with_session(admitted["approved_reversal_manifest"], session, "action-131")

        self.assertEqual("reverted", result["outcome"])
        self.assertEqual(1, result["effect_account"]["applied_effect_count"])
        self.assertEqual("completed", result["effect_account"]["effects"][0]["status"])
        self.assertEqual(["action-131"], session.starts)
        self.assertEqual([("actual-action-131", "completed")], session.finishes)
        self.assertIn("Semantic reversal detail.", target_path.read_text(encoding="utf-8"))
        self.assertTrue(any((self.root / ".caprmedio_caprmedio").rglob("CA-R-100--target@1.md")))

    def test_factory_executes_only_exact_structural_recovery_boundary(self) -> None:
        structure_path = self.root / ".caprmedio_caprmedio/project_structure.toml"
        before_text = "schema_version = 1\n"
        after_text = "schema_version = 1\n\n# exact partial cutover state\n"
        structure_path.write_text(after_text, encoding="utf-8")
        boundary = {
            "authorized_boundary": "fixture-partial-cutover",
            "toml": {
                "path": ".caprmedio_caprmedio/project_structure.toml",
                "before_sha256": hashlib.sha256(before_text.encode()).hexdigest(),
                "after_sha256": hashlib.sha256(after_text.encode()).hexdigest(),
                "before_text": before_text,
            },
            "references": [],
        }
        before, after = "before:structure-boundary", "after:structure-boundary"
        target = {"recovery_boundary": boundary}
        effect: dict[str, object] = {
            "effect_id": "structure-rollback", "target_id": "structure:fixture-partial-cutover",
            "expected_before": "exact partial cutover", "expected_after": "recorded pre-cutover source",
            "expected_current_hash": "", "expected_result_hash": "",
            "before_evidence": before, "after_evidence": after,
            "capability_binding": self._binding(
                "structure.rollback_scope_unit_change", {"recovery_boundary": boundary}, target, before=before, after=after
            ),
        }
        provider = NativeRevertProvider({"project_root": str(self.root), "approved_reversal_request": self._request(effect, "placeholder")})
        effect["expected_current_hash"] = provider.observe(str(effect["target_id"]))
        effect["expected_result_hash"] = canonical_digest({"members": [{
            "path": ".caprmedio_caprmedio/project_structure.toml",
            "sha256": hashlib.sha256(before_text.encode()).hexdigest(),
        }]})
        request = self._request(effect, str(effect["expected_current_hash"]))
        service = make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": request})
        admitted = service.handle({"operation": "admit", "reversal_request": request})
        session = SharedActionSession()
        result = service.execute_with_session(admitted["approved_reversal_manifest"], session, "action-131")

        self.assertEqual("reverted", result["outcome"])
        self.assertEqual(before_text, structure_path.read_text(encoding="utf-8"))
        self.assertEqual(["action-131"], session.starts)
        self.assertEqual(1, len(session.finishes))

    def test_changed_or_unsupported_effect_is_denied_before_run_or_mutation(self) -> None:
        target_path = self._atom(self.root)
        target = lifecycle_intents.carrier_descriptor(self.root, "CA-R-100")
        before, after = "before:denial", "after:denial"
        parameters = {"target": target, "proposed": self._proposal(target_path), "change_class": "semantic_revision"}
        effect: dict[str, object] = {
            "effect_id": "lifecycle-update", "target_id": "atom:CA-R-100",
            "expected_before": "active version 1", "expected_after": "active version 2",
            "expected_current_hash": canonical_digest(target), "expected_result_hash": "d" * 64,
            "before_evidence": before, "after_evidence": after,
            "capability_binding": self._binding("lifecycle.update_atom", parameters, target, before=before, after=after),
        }
        request = self._request(effect, str(effect["expected_current_hash"]))
        service = make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": request})
        changed = json.loads(json.dumps(request))
        changed["ordered_effects"][0]["capability_binding"]["permission_evidence"]["granted"] = False
        denied = service.handle({"operation": "admit", "reversal_request": changed})
        self.assertEqual("blocked", denied["outcome"])
        self.assertIn("approved_reversal_request", denied["missing_or_mismatched_bindings"])
        self.assertIn("capability_permission:lifecycle-update", denied["missing_or_mismatched_bindings"])
        self.assertEqual(1, lifecycle_intents.carrier_descriptor(self.root, "CA-R-100")["version"])

        unsupported = json.loads(json.dumps(request))
        unsupported["ordered_effects"][0]["capability_binding"]["capability_id"] = "file.write"
        unsupported["ordered_effects"][0]["capability_binding"]["permission_evidence"]["capability_id"] = "file.write"
        with self.assertRaisesRegex(NativeRevertProviderError, "RMED remainder: no admitted native capability"):
            make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": unsupported})
        self.assertEqual(1, lifecycle_intents.carrier_descriptor(self.root, "CA-R-100")["version"])


if __name__ == "__main__":
    unittest.main()
