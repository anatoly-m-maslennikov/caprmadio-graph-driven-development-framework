"""TDD contract for CA-D-588's closed selected-source pin successor."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
if str(MCP) not in sys.path:
    sys.path.insert(0, str(MCP))

from selected_source_refresh import (  # noqa: E402
    RegisteredSourceRefreshError,
    derive_registered_source_refresh,
    derive_registered_source_successor,
    registered_source_refresh,
)
from release_manifest_authorization import (  # noqa: E402
    authorize_operator_publication_recovery,
    authorize_operator_refresh,
)
from release_manifest_lifecycle import ReleaseManifestLifecycle  # noqa: E402
from release_manifest_publisher import (  # noqa: E402
    plan_release_manifest_refresh,
    recover_release_manifest_publish,
    refresh_release_manifest,
)
from selected_routes import load_selected_manifest, selected_manifest_ref  # noqa: E402

REPOSITORY = MCP.parents[2]
GOLDEN_INPUT = MCP / "tests/selected_source_refresh_golden/input_manifest.v7.json"
GOLDEN_CONTROLS = MCP / "tests/selected_source_refresh_golden/historical_controls.json"


class RegisteredSelectedSourceRefreshTest(unittest.TestCase):
    """The derivation is pure; source and lifecycle checks belong at its boundaries."""

    @staticmethod
    def _pin(*, version: int, digest: str) -> dict[str, object]:
        return {
            "atom_id": "CA-O-128",
            "version": version,
            "source_path": (
                ".caprmedio_caprmedio/000_CAPRMEDIO_framework/"
                "00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/"
                "001_CORE_META_MODEL/09_operations/"
                "CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md"
            ),
            "digest": digest,
        }

    def _manifest(self, registration: dict[str, object]) -> dict[str, object]:
        prior = registration["prior_pin"]
        assert isinstance(prior, dict)
        routes: list[dict[str, object]] = []
        for route_name in registration["routes"]:
            routes.append({
                "route": route_name,
                "workflow": {"atom_id": "CA-O-1", "version": 1, "source_path": "workflow.md", "digest": "a" * 64},
                "ordered_steps": [{"step": {"atom_id": "CA-O-2", "version": 1, "source_path": "step.md", "digest": "b" * 64},
                                   "action": copy.deepcopy(prior)}],
                "ordered_actions": [copy.deepcopy(prior)],
                "native_action_calls": [],
                "entry_step": "CA-O-2",
                "on_result": [{"from": "CA-O-2", "condition": "ok", "to": "complete"}],
                "mutation_capable": True,
            })
        routes.extend({"route": name, "unchanged": True} for name in ("other-a", "other-b"))
        return {
            "schema_version": 1,
            "source_freshness": {"selected_binding_digest": "0" * 64},
            "query_source_admissions": [{"route": "query", "unchanged": True}],
            "routes": routes,
            "canonical_manifest_sha256": "1" * 64,
            "release_source_admissions": [{"unchanged": True}],
        }

    def test_closed_registration_is_the_exact_d588_revision(self) -> None:
        registration = registered_source_refresh()
        self.assertEqual(1, registration["schema_version"])
        self.assertEqual("prepared-successors-o128-v4-20261006", registration["registration_id"])
        self.assertEqual("5ca6c9907a4dffbe84319b7d4e391c6242e1969cfea5902845e50f0bd8ae3012", registration["input_manifest_sha256"])
        self.assertEqual("c0edfd130a32386258397da81796d9efab6c1154b17666419edc988d76efc9ba", registration["input_canonical_manifest_sha256"])
        self.assertEqual(["create_atom", "update_atom", "replace_atom", "change_atom_status"], registration["routes"])
        self.assertEqual(8, registration["pin_occurrences"])
        self.assertEqual(3, registration["prior_pin"]["version"])
        self.assertEqual(4, registration["current_pin"]["version"])
        self.assertEqual(8, registration["requirement_pin"]["version"])

    def test_successor_replaces_exactly_eight_registered_action_pins_and_rederives_only_digests(self) -> None:
        registration = registered_source_refresh()
        manifest = self._manifest(registration)
        before = copy.deepcopy(manifest)

        candidate = derive_registered_source_successor(manifest, registration)

        self.assertEqual(before["query_source_admissions"], candidate["query_source_admissions"])
        self.assertEqual(before["release_source_admissions"], candidate["release_source_admissions"])
        self.assertEqual(before["routes"][4:], candidate["routes"][4:])
        self.assertNotEqual(before["source_freshness"]["selected_binding_digest"], candidate["source_freshness"]["selected_binding_digest"])
        self.assertNotEqual(before["canonical_manifest_sha256"], candidate["canonical_manifest_sha256"])
        for route in candidate["routes"][:4]:
            self.assertEqual(registration["current_pin"], route["ordered_steps"][0]["action"])
            self.assertEqual(registration["current_pin"], route["ordered_actions"][0])

    def test_topology_or_pin_occurrence_changes_refuse_without_mutating_input(self) -> None:
        registration = registered_source_refresh()
        manifest = self._manifest(registration)
        manifest["routes"][0]["ordered_actions"] = []
        broken_before = copy.deepcopy(manifest)

        with self.assertRaises(RegisteredSourceRefreshError):
            derive_registered_source_successor(manifest, registration)

        self.assertEqual(broken_before, manifest)


class RegisteredSourceRefreshE2ETest(unittest.TestCase):
    """A disposable closure of the real D588 16-route historical carrier."""

    @staticmethod
    def _pin_paths(value: object) -> set[str]:
        found: set[str] = set()
        if isinstance(value, dict):
            source = value.get("source_path")
            if isinstance(source, str):
                found.add(source)
            for item in value.values():
                found.update(RegisteredSourceRefreshE2ETest._pin_paths(item))
        elif isinstance(value, list):
            for item in value:
                found.update(RegisteredSourceRefreshE2ETest._pin_paths(item))
        return found

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        source_manifest = GOLDEN_INPUT
        self.manifest_bytes = source_manifest.read_bytes()
        self.manifest = json.loads(self.manifest_bytes)
        self.assertEqual("5ca6c9907a4dffbe84319b7d4e391c6242e1969cfea5902845e50f0bd8ae3012", hashlib.sha256(self.manifest_bytes).hexdigest())
        self.assertEqual(16, len(self.manifest["routes"]))
        manifest_target = self.root / selected_manifest_ref(REPOSITORY)
        manifest_target.parent.mkdir(parents=True, exist_ok=True)
        manifest_target.write_bytes(self.manifest_bytes)
        controls = json.loads(GOLDEN_CONTROLS.read_text(encoding="utf-8"))["carriers"]
        for relative, contents in controls.items():
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(contents, encoding="utf-8")
        historical_authority = {
            "atom_id": "CA-D-572", "version": 13,
            "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-572-TOOLS-DELIVERY--serialize-additive-release-route-source-admission.md",
            "digest": "72712694ba4d40069ac03e6d2513b04b15bd1d2970e26108e2ae152c5da54d69",
        }
        import release_manifest_authorization as authorization_module
        import release_source_admission as admission_module
        authority_patch = patch.object(admission_module, "AUTHORITY_PIN", historical_authority)
        authorization_patch = patch.object(authorization_module, "AUTHORITY_PIN", historical_authority)
        authority_patch.start()
        authorization_patch.start()
        self.addCleanup(authority_patch.stop)
        self.addCleanup(authorization_patch.stop)
        paths = self._pin_paths(self.manifest)
        paths.update({
            self.manifest["source_freshness"]["selected_source_registry_ref"],
            ".caprmedio_caprmedio/caprmedio_project_settings.toml",
            ".caprmedio_caprmedio/operators_registry.toml",
            ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/07_delivery/CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh.md",
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes@3.md",
            ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/REPLACE_ATOM/04_requirement/CA-R-1041-TOOLS--coordinate-atom-replacement-intent.md",
        })
        # Release-admission validation uses this authority carrier in addition
        # to the pins retained by the admitted sixteen-route document.
        from release_source_admission import AUTHORITY_REF
        paths.add(AUTHORITY_REF)
        authority_text = controls[AUTHORITY_REF]
        private_block = re.search(r"(?ms)^## Private implementation carriers\n+```json\n(.*?)\n```$", authority_text)
        self.assertIsNotNone(private_block)
        paths.update(row["source_path"] for row in json.loads(private_block.group(1)))
        for relative in paths:
            self._copy(relative)

    def _copy(self, relative: str) -> None:
        source = REPOSITORY / relative
        destination = self.root / relative
        if destination.exists():
            return
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    def _authorize(self, plan: dict[str, object]) -> object:
        return authorize_operator_refresh(
            self.root, plan, operator_name="Anatoly Maslennikov", journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "d588-real-reader"},
            authorization_ref="authorization/d588-real-reader.md",
        )

    def test_real_closed_reader_derives_and_publishes_the_exact_successor(self) -> None:
        current, candidate, payload, carrier = derive_registered_source_refresh(self.root)
        self.assertEqual(self.manifest_bytes, carrier.read_bytes())
        self.assertEqual(16, len(current["routes"]))
        self.assertEqual(16, len(candidate["routes"]))
        self.assertEqual("c0edfd130a32386258397da81796d9efab6c1154b17666419edc988d76efc9ba", current["canonical_manifest_sha256"])
        self.assertEqual("9671de66fd510f1c5d77a66e4376a9388e3448d5842ef54638d272da6f08bc9e", candidate["canonical_manifest_sha256"])
        self.assertEqual(102964, len(payload))
        plan = plan_release_manifest_refresh(self.root)
        with patch("release_manifest_lifecycle.subprocess.run", return_value=types.SimpleNamespace(returncode=0, stdout="f" * 40 + "\n")):
            result = refresh_release_manifest(self.root, execute=True, authorization=self._authorize(plan))
        self.assertEqual("published", result["disposition"], result)
        self.assertEqual(payload, carrier.read_bytes())
        self.assertEqual(candidate["canonical_manifest_sha256"], load_selected_manifest(self.root)["canonical_manifest_sha256"])

    def test_real_reader_refuses_tampered_input_and_registered_carriers_before_effects(self) -> None:
        carrier = self.root / selected_manifest_ref(self.root)
        checks = [
            (carrier, b"\nraw-input-drift"),
            (self.root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes@3.md", b"\narchive-drift"),
            (self.root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md", b"\ncurrent-action-drift"),
            (self.root / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/REPLACE_ATOM/04_requirement/CA-R-1041-TOOLS--coordinate-atom-replacement-intent.md", b"\nrequirement-drift"),
        ]
        for path, drift in checks:
            original = path.read_bytes()
            path.write_bytes(original + drift)
            with self.assertRaises(RegisteredSourceRefreshError):
                derive_registered_source_refresh(self.root)
            self.assertEqual(original + drift, path.read_bytes())
            path.write_bytes(original)

        registration = self.root / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/07_delivery/CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh.md"
        original = registration.read_bytes()
        registration.write_bytes(original.replace(b'"schema_version": 1,', b'"schema_version": 1,\n  "schema_version": 1,', 1))
        with self.assertRaises(RegisteredSourceRefreshError):
            derive_registered_source_refresh(self.root)

    def test_real_reader_postseal_drift_and_recording_recovery_never_replay(self) -> None:
        carrier = self.root / selected_manifest_ref(self.root)
        before = carrier.read_bytes()
        plan = plan_release_manifest_refresh(self.root)
        original_prepare = ReleaseManifestLifecycle.prepare_release_manifest_publication
        action = self.root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md"

        def seal_then_drift(lifecycle: object, sealed: dict, payload: bytes, **kwargs: object) -> str:
            event_id = original_prepare(lifecycle, sealed, payload, **kwargs)
            action.write_bytes(action.read_bytes() + b"\npost-seal-source-drift")
            return event_id

        with patch("release_manifest_lifecycle.subprocess.run", return_value=types.SimpleNamespace(returncode=0, stdout="e" * 40 + "\n")), patch.object(ReleaseManifestLifecycle, "prepare_release_manifest_publication", new=seal_then_drift):
            result = refresh_release_manifest(self.root, execute=True, authorization=self._authorize(plan))
        self.assertEqual("pending_publication", result["disposition"], result)
        self.assertEqual(before, carrier.read_bytes())

        # A recording failure occurs only after the exact effect; recovery must
        # finalize that event, never invoke another replacement.
        self.setUp()
        carrier = self.root / selected_manifest_ref(self.root)
        plan = plan_release_manifest_refresh(self.root)
        with patch("release_manifest_lifecycle.subprocess.run", return_value=types.SimpleNamespace(returncode=0, stdout="d" * 40 + "\n")), patch.object(ReleaseManifestLifecycle, "record_release_manifest_publication", side_effect=RuntimeError("recording failed")):
            result = refresh_release_manifest(self.root, execute=True, authorization=self._authorize(plan))
        self.assertEqual("recording_required", result["disposition"], result)
        event_id = result["pending_event_id"]
        published = carrier.read_bytes()
        recovery = authorize_operator_publication_recovery(
            self.root, event_id, operator_name="Anatoly Maslennikov", journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "d588-real-reader"}, authorization_ref="authorization/d588-recovery.md",
        )
        with patch("release_manifest_publisher._atomic_write", side_effect=AssertionError("recovery replayed write")):
            recovered = recover_release_manifest_publish(self.root, pending_event_id=event_id, authorization=recovery)
        self.assertEqual("recovered", recovered["disposition"])
        self.assertEqual(published, carrier.read_bytes())


if __name__ == "__main__":
    unittest.main()
