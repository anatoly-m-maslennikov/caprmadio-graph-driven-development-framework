"""D560 native Release Version boundary checks in disposable local projects."""

from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_version import ReleaseVersionError, release_version  # noqa: E402
from release_handoff_fixture import ReleaseFixture, reseal  # noqa: E402


RESULT_FIELDS = {
    "operation",
    "outcome",
    "candidate_snapshot_manifest_sha256",
    "prior_release",
    "candidate_release",
    "runtime_selection",
    "skill_selection",
    "attempted_effects",
    "gate_evidence_refs",
    "image_refs",
    "rollback_state",
    "run_receipt_refs",
}


class ReleaseVersionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.fixture = ReleaseFixture(Path(self.temporary.name))

    def request(self, operation: str = "prepare", **changes: object) -> dict[str, object]:
        manifest = copy.deepcopy(self.fixture.manifest)
        value: dict[str, object] = {
            "operation": operation,
            "project_root": str(self.fixture.root),
            "candidateSnapshotManifest": manifest,
            "expected_executing_release": manifest["executing_release"],
            "expected_project_structure_digest": manifest["project_structure_digest"],
            "expected_framework_settings_digest": manifest["framework_settings_digest"],
            "expected_source_frontier_digest": manifest["source_frontier_digest"],
            "run_receipt_refs": ["workflow-run:selected-release", "action-run:release-prepare"],
        }
        value.update(changes)
        return value

    def test_prepare_rebuilds_complete_candidate_and_preserves_every_project_byte(self) -> None:
        before = self.fixture.snapshot()

        result = release_version(self.request())

        encoded = result.model_dump(mode="json")
        self.assertEqual(set(encoded), RESULT_FIELDS)
        self.assertEqual(encoded["operation"], "prepare")
        self.assertEqual(encoded["outcome"], "prepared")
        self.assertEqual(encoded["candidate_snapshot_manifest_sha256"], self.fixture.manifest["sha256"])
        self.assertEqual(encoded["prior_release"], "N")
        self.assertEqual(encoded["candidate_release"], "N+1")
        self.assertEqual(encoded["runtime_selection"], "unchanged")
        self.assertEqual(encoded["skill_selection"], "unchanged")
        self.assertEqual(encoded["attempted_effects"], [])
        self.assertEqual(encoded["gate_evidence_refs"], [])
        self.assertEqual(encoded["image_refs"], [])
        self.assertEqual(encoded["rollback_state"], "not_attempted")
        self.assertEqual(encoded["run_receipt_refs"], self.request()["run_receipt_refs"])
        self.assertEqual(self.fixture.snapshot(), before)

    def test_unknown_or_substituted_request_authority_is_refused(self) -> None:
        for field in ("source_root", "output_path", "source_patch", "journal_payload", "run_event", "image_prune", "phase"):
            with self.subTest(forbidden=field):
                with self.assertRaises(ReleaseVersionError) as raised:
                    release_version(self.request(**{field: "forged"}))
                self.assertEqual(raised.exception.code, "release-request-invalid")

        forged = copy.deepcopy(self.fixture.manifest)
        forged["source_inventory_rows"][0]["source_sha256"] = "0" * 64
        forged = reseal(forged)
        with self.assertRaises(ReleaseVersionError) as local:
            release_version(self.request(candidateSnapshotManifest=forged))
        self.assertEqual(local.exception.code, "release-currentness-stale")

        with self.assertRaises(ReleaseVersionError) as frontier:
            release_version(self.request(expected_source_frontier_digest="0" * 64))
        self.assertEqual(frontier.exception.code, "release-request-invalid")

    def test_stale_local_selection_source_structure_and_settings_refuse_before_effect(self) -> None:
        mutations = {
            "selection": (".caprmedio_runtime/framework/current.toml", b"release = 'other'\n"),
            "source": (".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/core-λ.md", b"changed source\n"),
            "structure": (".caprmedio_caprmedio/project_structure.toml", b"changed structure\n"),
            "settings": (".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml", b"changed settings\n"),
        }
        for name, (relative, payload) in mutations.items():
            with self.subTest(binding=name):
                temporary = tempfile.TemporaryDirectory()
                try:
                    fixture = ReleaseFixture(Path(temporary.name))
                    request = {
                        "operation": "prepare",
                        "project_root": str(fixture.root),
                        "candidateSnapshotManifest": copy.deepcopy(fixture.manifest),
                        "expected_executing_release": fixture.manifest["executing_release"],
                        "expected_project_structure_digest": fixture.manifest["project_structure_digest"],
                        "expected_framework_settings_digest": fixture.manifest["framework_settings_digest"],
                        "expected_source_frontier_digest": fixture.manifest["source_frontier_digest"],
                        "run_receipt_refs": ["workflow-run:selected-release"],
                    }
                    target = fixture.root / relative
                    before = fixture.snapshot()
                    target.write_bytes(payload)
                    with self.assertRaises(ReleaseVersionError) as raised:
                        release_version(request)
                    self.assertEqual(raised.exception.code, "release-currentness-stale")
                    self.assertEqual(target.read_bytes(), payload)
                    self.assertEqual(
                        {path: row for path, row in fixture.snapshot().items() if path != relative},
                        {path: row for path, row in before.items() if path != relative},
                    )
                finally:
                    temporary.cleanup()

    def test_apply_and_recording_recovery_are_blocked_without_effect_or_replay(self) -> None:
        before = self.fixture.snapshot()

        apply_result = release_version(self.request("apply"))
        recovery_result = release_version(
            self.request("recover_recording", failed_recording_ref="action-run:release-recording-failed")
        )

        for result, operation in ((apply_result, "apply"), (recovery_result, "recover_recording")):
            with self.subTest(operation=operation):
                self.assertEqual(result.operation, operation)
                self.assertEqual(result.outcome, "blocked")
                self.assertEqual(result.attempted_effects, [])
                self.assertEqual(result.gate_evidence_refs, [])
                self.assertEqual(result.image_refs, [])
                self.assertEqual(result.runtime_selection, "unchanged")
                self.assertEqual(result.skill_selection, "unchanged")
        self.assertEqual(self.fixture.snapshot(), before)

        with self.assertRaises(ReleaseVersionError) as missing_recovery:
            release_version(self.request("recover_recording"))
        self.assertEqual(missing_recovery.exception.code, "release-request-invalid")
        with self.assertRaises(ReleaseVersionError) as stray_recovery:
            release_version(self.request(failed_recording_ref="action-run:unexpected"))
        self.assertEqual(stray_recovery.exception.code, "release-request-invalid")


if __name__ == "__main__":
    unittest.main()
