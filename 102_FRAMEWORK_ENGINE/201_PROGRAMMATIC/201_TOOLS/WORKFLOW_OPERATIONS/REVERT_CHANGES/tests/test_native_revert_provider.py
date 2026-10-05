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
from work_journal import canonical_json_bytes  # noqa: E402
from native_revert_provider import (  # noqa: E402
    NATIVE_REVERT_EVIDENCE_SOURCE_REMAINDERS,
    NativeRevertProvider,
    NativeRevertProviderError,
    make_native_revert_service,
)


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


def canonical_digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def bind_actual_evidence(root: Path, request: dict[str, object]) -> dict[str, object]:
    """Create current records only in a disposable Project, using D536@2 pins."""
    request = json.loads(json.dumps(request))
    evidence = root / ".caprmedio_caprmedio/evidence"
    evidence.mkdir(parents=True, exist_ok=True)

    def record(name: str, value: object) -> dict[str, str]:
        path = evidence / name
        path.write_bytes(canonical_json_bytes(value))
        return {"evidence_ref": path.relative_to(root).as_posix(), "evidence_hash": hashlib.sha256(path.read_bytes()).hexdigest()}

    selected = record("selected-change.json", {"accepted": True, "selected_effect_ids": [effect["effect_id"] for effect in request["ordered_effects"]]})
    history = record("preserved.json", {"history": "retained", "references": "preserved"})
    request.update(selected_change=[selected], selected_change_refs=[selected["evidence_ref"]],
                   history_record=[history], history_reference_evidence=[history["evidence_ref"]],
                   affected_reference=[history], affected_reference_hashes={history["evidence_ref"]: history["evidence_hash"]},
                   before_record=[], after_record=[])
    for effect in request["ordered_effects"]:
        before = record(effect["effect_id"] + "-before.json", {"state": effect["expected_before"]})
        after = record(effect["effect_id"] + "-after.json", {"state": effect["expected_after"]})
        request["before_record"].append(before)
        request["after_record"].append(after)
        effect.update(before_evidence=before["evidence_ref"], after_evidence=after["evidence_ref"])
        binding = effect["capability_binding"]
        permission = record(effect["effect_id"] + "-permission.json", {
            "capability_id": binding["capability_id"], "granted": True})
        binding["permission_evidence"].update(permission)
        binding["evidence_refs"] = [before["evidence_ref"], after["evidence_ref"], history["evidence_ref"]]
    for name in ("operator_decision", "executor_permission"):
        value = {key: item for key, item in request[name].items() if key not in {"evidence_ref", "evidence_hash"}}
        observed = {**value, "ordered_effects": request["ordered_effects"]} if name == "operator_decision" else value
        request[name] = {**value, **record(name + ".json", observed)}
    relative = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-131-CORE_META_MODEL-ACTION--apply-an-approved-reversal.md"
    source = PACKAGE.parents[4] / relative
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(source.read_bytes())
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    request.update(governing_definition={"atom_id": "CA-O-131", "revision": 2, "evidence_ref": relative, "evidence_hash": digest},
                   governing_definition_hash=digest)
    return request


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

    def test_synthetic_lifecycle_evidence_is_blocked_without_native_effect(self) -> None:
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
                self.assertEqual("blocked", admitted["outcome"])
                session = SharedActionSession()
                result = admitted

        self.assertEqual(0, result["effect_account"]["applied_effect_count"])
        self.assertEqual([], session.starts)
        self.assertEqual([], session.finishes)
        self.assertNotIn("Semantic reversal detail.", target_path.read_text(encoding="utf-8"))
        self.assertFalse(any((self.root / ".caprmedio_caprmedio").rglob("CA-R-100--target@1.md")))
        self.assertTrue(set(NATIVE_REVERT_EVIDENCE_SOURCE_REMAINDERS) <= set(result["missing_or_mismatched_bindings"]))

    def test_synthetic_structural_evidence_is_blocked_without_native_effect(self) -> None:
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
        result = admitted

        self.assertEqual("blocked", result["outcome"])
        self.assertEqual(after_text, structure_path.read_text(encoding="utf-8"))
        self.assertEqual([], session.starts)
        self.assertEqual([], session.finishes)

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

    def _actual_permission_request(self) -> tuple[dict[str, object], Path]:
        """Supply real representable evidence without fabricating the source gaps."""
        path = self._atom(self.root)
        target = lifecycle_intents.carrier_descriptor(self.root, "CA-R-100")
        permission_path = self.root / ".caprmedio_caprmedio/evidence/permission.json"
        permission_path.parent.mkdir(parents=True, exist_ok=True)
        permission_path.write_text(json.dumps({"capability_id": "lifecycle.update_atom", "granted": True}), encoding="utf-8")
        preserved = self.root / ".caprmedio_caprmedio/evidence/preserved.md"
        preserved.write_text("Actual preserved evidence.\n", encoding="utf-8")
        effect = {"effect_id": "actual-permission", "target_id": "atom:CA-R-100",
                  "expected_before": "version 1", "expected_after": "version 2",
                  "expected_current_hash": canonical_digest(target), "expected_result_hash": "d" * 64,
                  "before_evidence": "evidence/preserved.md", "after_evidence": "evidence/preserved.md",
                  "capability_binding": self._binding("lifecycle.update_atom", {
                      "target": target, "proposed": self._proposal(path), "change_class": "semantic_revision"},
                      target, before="evidence/preserved.md", after="evidence/preserved.md")}
        effect["capability_binding"]["permission_evidence"].update(
            evidence_ref="evidence/permission.json", evidence_hash=hashlib.sha256(permission_path.read_bytes()).hexdigest())
        effect["capability_binding"]["evidence_refs"] = ["evidence/preserved.md"]
        request = self._request(effect, effect["expected_current_hash"])
        request["affected_reference_hashes"] = {"evidence/preserved.md": hashlib.sha256(preserved.read_bytes()).hexdigest()}
        request["selected_change_refs"] = ["evidence/preserved.md"]
        request["history_reference_evidence"] = ["evidence/preserved.md"]
        request = bind_actual_evidence(self.root, request)
        permission_path = self.root / request["ordered_effects"][0]["capability_binding"]["permission_evidence"]["evidence_ref"]
        return request, permission_path

    def test_current_actual_evidence_pins_permit_admission(self) -> None:
        request, _permission_path = self._actual_permission_request()
        provider = NativeRevertProvider({"project_root": str(self.root), "approved_reversal_request": request})
        self.assertEqual(list(NATIVE_REVERT_EVIDENCE_SOURCE_REMAINDERS), provider.revalidate(request))
        service = make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": request})
        self.assertEqual("admitted", service.admit(request)["outcome"])

    def test_actual_permission_revocation_and_hash_change_block_before_start_or_effect(self) -> None:
        request, permission_path = self._actual_permission_request()
        service = make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": request})
        provider = NativeRevertProvider({"project_root": str(self.root), "approved_reversal_request": request})
        admitted = service.admit(request)
        self.assertEqual("admitted", admitted["outcome"])
        manifest = admitted["approved_reversal_manifest"]
        for granted in (False, True):
            with self.subTest(granted=granted):
                permission_path.write_text(json.dumps({"capability_id": "lifecycle.update_atom", "granted": granted,
                                                      "changed": True}), encoding="utf-8")
                session = SharedActionSession()
                with mock.patch.object(lifecycle_intents, "update_atom_action", side_effect=AssertionError("effect must not start")) as effect:
                    result = service.execute_with_session(manifest, session, "action-131")
                    with self.assertRaisesRegex(NativeRevertProviderError, "current evidence is not admitted"):
                        provider.apply_effect(request["ordered_effects"][0])
                self.assertEqual("blocked", result["outcome"])
                self.assertIn("capability_permission_hash:actual-permission", result["missing_or_mismatched_bindings"])
                if not granted:
                    self.assertIn("capability_permission_revoked:actual-permission", result["missing_or_mismatched_bindings"])
                self.assertEqual([], session.starts)
                self.assertEqual([], session.finishes)
                effect.assert_not_called()

    def test_actual_reference_change_and_unsafe_permission_are_rejected(self) -> None:
        request, _permission = self._actual_permission_request()
        provider = NativeRevertProvider({"project_root": str(self.root), "approved_reversal_request": request})
        preserved = self.root / request["history_record"][0]["evidence_ref"]
        preserved.write_text("Changed reference.\n", encoding="utf-8")
        self.assertIn("affected_reference:0:evidence_hash", provider.revalidate(request))
        for reference in ("../outside.json", ".", ".env", "https://example.test/permission", ".caprmedio_caprmedio/evidence/link.json"):
            with self.subTest(reference=reference):
                if reference.endswith("link.json"):
                    (self.root / reference).symlink_to(_permission)
                changed = json.loads(json.dumps(request))
                changed["ordered_effects"][0]["capability_binding"]["permission_evidence"]["evidence_ref"] = reference
                bound = NativeRevertProvider({"project_root": str(self.root), "approved_reversal_request": changed})
                self.assertTrue(any(item.startswith("capability_permission_evidence:actual-permission:")
                                    for item in bound.revalidate(changed)))

        unsupported = json.loads(json.dumps(request))
        unsupported["ordered_effects"][0]["capability_binding"]["capability_id"] = "file.write"
        unsupported["ordered_effects"][0]["capability_binding"]["permission_evidence"]["capability_id"] = "file.write"
        with self.assertRaisesRegex(NativeRevertProviderError, "RMED remainder: no admitted native capability"):
            make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": unsupported})
        self.assertEqual(1, lifecycle_intents.carrier_descriptor(self.root, "CA-R-100")["version"])

    def test_selected_event_is_reobserved_through_canonical_journal_reader(self) -> None:
        request, _permission_path = self._actual_permission_request()
        control = self.root / ".caprmedio_caprmedio"
        defaults = control / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
        defaults.mkdir(parents=True, exist_ok=True)
        (defaults / "caprmedio_framework_default_settings.toml").write_text(
            "[query]\nmax_request_bytes = 4096\nmax_grammar_depth = 16\nmax_filter_tokens = 128\n"
            "max_in_members = 16\nmax_selected_fields = 8\nmax_page_size = 2\nmax_snapshot_members = 8\n"
            "max_file_bytes = 4096\nmax_total_read_bytes = 16384\ntimeout_seconds = 10\nmax_findings = 8\n",
            encoding="utf-8")
        journal = control / "_journal"
        journal.mkdir()
        event = {"event_id": "accepted-1", "event_type": "Completed", "result": "accepted change é"}
        member = journal / "accepted.ndjson"
        member.write_text(json.dumps(event) + "\n", encoding="utf-8")
        request["selected_change_refs"] = ["event:accepted-1"]
        request["selected_change"] = [{"evidence_ref": "event:accepted-1", "evidence_hash": hashlib.sha256(canonical_json_bytes(event)).hexdigest()}]
        provider = NativeRevertProvider({"project_root": str(self.root), "approved_reversal_request": request})
        self.assertEqual(list(NATIVE_REVERT_EVIDENCE_SOURCE_REMAINDERS), provider.revalidate(request))
        event["result"] = "changed accepted evidence"
        member.write_text(json.dumps(event) + "\n", encoding="utf-8")
        self.assertIn("selected_change:0:evidence_hash", provider.revalidate(request))

    def test_large_and_duplicate_permission_evidence_is_rejected(self) -> None:
        request, permission_path = self._actual_permission_request()
        provider = NativeRevertProvider({"project_root": str(self.root), "approved_reversal_request": request})
        permission_path.write_bytes(b"x" * (1024 * 1024 + 1))
        self.assertTrue(any("exceeds its byte limit" in item for item in provider.revalidate(request)))
        permission_path.write_text('{"capability_id":"lifecycle.update_atom","granted":false,"granted":true}', encoding="utf-8")
        self.assertTrue(any("duplicate evidence JSON member" in item for item in provider.revalidate(request)))

    def _structural_request(self, count: int = 1) -> tuple[dict[str, object], list[Path], str]:
        before = "schema_version = 1\n"
        after = before + "\n# admitted partial cutover\n"
        effects, paths = [], []
        for number in range(count):
            path = self.root / f".caprmedio_caprmedio/structure-{number}.toml"
            path.write_text(after, encoding="utf-8")
            paths.append(path)
            boundary = {"authorized_boundary": f"exact-cutover-{number}", "references": [], "toml": {
                "path": path.relative_to(self.root).as_posix(), "before_text": before,
                "before_sha256": hashlib.sha256(before.encode()).hexdigest(), "after_sha256": hashlib.sha256(after.encode()).hexdigest()}}
            effect = {"effect_id": f"structure-{number}", "target_id": f"structure:{number}",
                      "expected_before": "recorded partial cutover", "expected_after": "recorded pre-cutover",
                      "expected_current_hash": canonical_digest({"members": [{"path": path.relative_to(self.root).as_posix(), "sha256": hashlib.sha256(after.encode()).hexdigest()}]}),
                      "expected_result_hash": canonical_digest({"members": [{"path": path.relative_to(self.root).as_posix(), "sha256": hashlib.sha256(before.encode()).hexdigest()}]}),
                      "before_evidence": "before:structure", "after_evidence": "after:structure",
                      "capability_binding": self._binding("structure.rollback_scope_unit_change", {"recovery_boundary": boundary},
                                                          {"recovery_boundary": boundary}, before="before:structure", after="after:structure")}
            effects.append(effect)
        request = self._request(effects[0], effects[0]["expected_current_hash"])
        request.update(ordered_effects=effects, targets=[effect["target_id"] for effect in effects],
                       current_hashes={effect["target_id"]: effect["expected_current_hash"] for effect in effects})
        request["operator_decision"]["approved_effect_ids"] = [effect["effect_id"] for effect in effects]
        request["cancellation_boundary"]["after_effect_ids"] = [effect["effect_id"] for effect in effects]
        return bind_actual_evidence(self.root, request), paths, before

    def test_current_actual_pins_execute_exact_structural_reversal(self) -> None:
        request, paths, before = self._structural_request()
        service = make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": request})
        admitted = service.admit(request)
        self.assertEqual("admitted", admitted["outcome"])
        session = SharedActionSession()
        result = service.execute_with_session(admitted["approved_reversal_manifest"], session, "action-131")
        self.assertEqual("reverted", result["outcome"])
        self.assertEqual(before, paths[0].read_text())
        self.assertEqual(1, result["effect_account"]["applied_effect_count"])
        self.assertEqual(["action-131"], session.starts)
        self.assertEqual([("actual-action-131", "completed")], session.finishes)

    def test_actual_decision_executor_and_governing_changes_block_before_start(self) -> None:
        request, _paths, _before = self._structural_request()
        for name, field, value in (("operator_decision", "status", "revoked"),
                                   ("executor_permission", "granted", False),
                                   ("governing_definition", "version", "3")):
            with self.subTest(name=name):
                path = self.root / request[name]["evidence_ref"]
                before_bytes = path.read_bytes()
                service = make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": request})
                admitted = service.admit(request)
                self.assertEqual("admitted", admitted["outcome"])
                if name == "governing_definition":
                    path.write_bytes(before_bytes.replace(b"version: 2", b"version: 3"))
                else:
                    data = json.loads(before_bytes)
                    data[field] = value
                    path.write_bytes(canonical_json_bytes(data))
                session = SharedActionSession()
                result = service.execute_with_session(admitted["approved_reversal_manifest"], session, "action-131")
                self.assertEqual("blocked", result["outcome"])
                self.assertIn(f"{name}:evidence_hash", result["missing_or_mismatched_bindings"])
                self.assertEqual([], session.starts)
                path.write_bytes(before_bytes)

    def test_permission_revoked_after_one_effect_blocks_unperformed_remainder(self) -> None:
        import project_structure
        request, paths, before = self._structural_request(2)
        service = make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": request})
        admitted = service.admit(request)
        self.assertEqual("admitted", admitted["outcome"])
        original = project_structure.rollback_scope_unit_change

        def revoke_after_first(root, boundary):
            result = original(root, boundary)
            permission = self.root / request["ordered_effects"][1]["capability_binding"]["permission_evidence"]["evidence_ref"]
            record = json.loads(permission.read_bytes())
            record["granted"] = False
            permission.write_bytes(canonical_json_bytes(record))
            return result

        with mock.patch.object(project_structure, "rollback_scope_unit_change", side_effect=revoke_after_first) as effect:
            result = service.execute_with_session(admitted["approved_reversal_manifest"], SharedActionSession(), "action-131")
        self.assertEqual("blocked", result["outcome"])
        self.assertEqual(1, effect.call_count)
        self.assertEqual(before, paths[0].read_text())
        self.assertIn("admitted partial cutover", paths[1].read_text())
        self.assertEqual(["completed", "unattempted"], [effect["status"] for effect in result["effect_account"]["effects"]])

    def test_multiple_selected_pins_align_exactly_and_mismatch_is_denied(self) -> None:
        request, _permission = self._actual_permission_request()
        second = dict(request["history_record"][0])
        request["selected_change"].append(second)
        request["selected_change_refs"].append(second["evidence_ref"])
        provider = NativeRevertProvider({"project_root": str(self.root), "approved_reversal_request": request})
        self.assertEqual([], provider.revalidate(request))
        request["selected_change_refs"].reverse()
        changed = NativeRevertProvider({"project_root": str(self.root), "approved_reversal_request": request})
        self.assertIn("selected_change:reference_alignment", changed.revalidate(request))

    def test_identical_effect_ids_do_not_authorize_changed_parameters(self) -> None:
        request, _paths, _before = self._structural_request()
        changed = json.loads(json.dumps(request))
        binding = changed["ordered_effects"][0]["capability_binding"]
        binding["parameters"]["recovery_boundary"]["authorized_boundary"] = "different-approved-boundary"
        binding["target"]["recovery_boundary"]["authorized_boundary"] = "different-approved-boundary"
        service = make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": changed})
        result = service.admit(changed)
        self.assertEqual("blocked", result["outcome"])
        self.assertIn("operator_decision:approval_revoked_or_effect_order", result["missing_or_mismatched_bindings"])


if __name__ == "__main__":
    unittest.main()
