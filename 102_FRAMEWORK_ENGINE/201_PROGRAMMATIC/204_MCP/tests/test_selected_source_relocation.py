"""Closed, disposable-fixture proof for the D592 three-carrier relocation."""
from __future__ import annotations

import hashlib
import base64
import gzip
import json
from pathlib import Path
import shutil
import sys
import tempfile
import types
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
GOLDEN_INPUT = MCP / "tests/selected_source_relocation_golden/input_manifest.1381b8.json.gz.b64"
for location in (MCP, MCP / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import selected_source_relocation as relocation  # noqa: E402
from release_manifest_authorization import authorize_operator_refresh  # noqa: E402
from release_manifest_lifecycle import ReleaseManifestLifecycle  # noqa: E402
from release_manifest_publisher import (  # noqa: E402
    ReleaseManifestPublishError, plan_release_manifest_refresh, recover_release_manifest_publish,
    refresh_release_manifest,
)
from release_source_admission import AUTHORITY_REF, derive_release_private_carriers  # noqa: E402
from selected_routes import load_selected_manifest, selected_manifest_ref  # noqa: E402
import work_journal  # noqa: E402


def _source_paths(value: object) -> set[str]:
    if isinstance(value, dict):
        return ({value["source_path"]} if isinstance(value.get("source_path"), str) else set()) | set().union(
            *(_source_paths(item) for item in value.values())
        )
    if isinstance(value, list):
        return set().union(*(_source_paths(item) for item in value)) if value else set()
    return set()


class SelectedSourceRelocationTest(unittest.TestCase):
    """No fixture carries a symlink, secret, or prebuilt replacement manifest."""

    def setUp(self) -> None:
        parent = REPOSITORY / ".caprmedio_tmp/tests/selected-source-relocation"
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=parent, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.manifest_ref = str(selected_manifest_ref(REPOSITORY))
        raw = gzip.decompress(base64.b64decode(GOLDEN_INPUT.read_bytes()))
        self.assertEqual(
            "1381b8c41d59e7f3636ac69e37e365e41b8429469e748e9824e982a7ccdd71a9",
            hashlib.sha256(raw).hexdigest(),
        )
        self.before = raw
        document = json.loads(raw)
        paths = _source_paths(document)
        # The input is intentionally stale at exactly the three registered
        # predecessor locations.  The replacement carriers are copied below.
        paths.difference_update(row[2] for row in relocation._ROWS)
        paths.update(row[3] for row in relocation._ROWS)
        freshness = document["source_freshness"]
        paths.add(freshness["selected_source_registry_ref"])
        paths.update({self.manifest_ref, str(relocation._REF), AUTHORITY_REF,
                      ".caprmedio_caprmedio/operators_registry.toml",
                      ".caprmedio_caprmedio/caprmedio_project_settings.toml"})
        paths.update(row["source_path"] for row in derive_release_private_carriers(REPOSITORY))
        for relative in paths:
            source = REPOSITORY / relative
            self.assertTrue(source.is_file() and not source.is_symlink(), relative)
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        self.path = self.root / self.manifest_ref
        self.path.write_bytes(raw)

    def _registration(self) -> Path:
        return self.root / relocation._REF

    def _trust_fixture_registration(self, raw: bytes):
        self._registration().write_bytes(raw)
        return patch.object(relocation, "_SHA", hashlib.sha256(raw).hexdigest())

    def _plan(self) -> dict:
        return plan_release_manifest_refresh(self.root)

    def _authorization(self):
        return authorize_operator_refresh(
            self.root, self._plan(), operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "selected-source-relocation"},
            authorization_ref=relocation._EXPECTED["authorization_ref"],
        )

    def _git(self):
        return patch("release_manifest_lifecycle.subprocess.run",
                     return_value=types.SimpleNamespace(returncode=0, stdout="a" * 40 + "\n"))

    def _pending(self) -> list[str]:
        pending = self.root / ".caprmedio_runtime/state/work_journal/pending"
        return sorted(item.stem for item in pending.glob("release-manifest:*.json")) if pending.exists() else []

    def test_plan_replaces_exactly_three_registered_paths(self) -> None:
        old, candidate, payload, path = relocation.derive_registered_source_relocation(self.root)
        self.assertEqual(self.path, path)
        self.assertEqual(self.before, self.path.read_bytes())
        self.assertEqual(old["routes"], candidate["routes"])
        self.assertEqual(old["source_freshness"], candidate["source_freshness"])
        self.assertNotEqual(old["canonical_manifest_sha256"], candidate["canonical_manifest_sha256"])
        for _, _, prior, current, _ in relocation._ROWS:
            self.assertIn(prior, self.before.decode())
            self.assertIn(current, payload.decode())
            self.assertNotIn(prior, payload.decode())

    def test_malformed_duplicate_stale_and_extra_registration_refuse(self) -> None:
        original = self._registration().read_text(encoding="utf-8")
        variants = (
            original.replace('"schema_version": 1,', '"schema_version": 1,"schema_version": 1,', 1),
            original.replace('"schema_version": 1,', '"schema_version": 2,', 1),
            original.replace('"registration_id":', '"extra":true,"registration_id":', 1),
            original.replace('"relocations": [', '"relocations": [false,', 1),
        )
        for changed in variants:
            with self.subTest(changed=changed[:32]), self._trust_fixture_registration(changed.encode()):
                with self.assertRaises(relocation.SelectedSourceRelocationError):
                    relocation.registered_source_relocation(self.root)

    def test_tampered_registered_current_carrier_and_input_refuse(self) -> None:
        current = self.root / relocation._ROWS[0][3]
        current.write_bytes(current.read_bytes() + b"\nstale\n")
        with self.assertRaises(relocation.SelectedSourceRelocationError):
            relocation.derive_registered_source_relocation(self.root)
        current.write_bytes((REPOSITORY / relocation._ROWS[0][3]).read_bytes())
        self.path.write_bytes(self.before + b"\n")
        with self.assertRaises(relocation.SelectedSourceRelocationError):
            relocation.derive_registered_source_relocation(self.root)

    def test_untrusted_or_forged_authorization_never_writes(self) -> None:
        with self.assertRaises(ReleaseManifestPublishError):
            refresh_release_manifest(self.root, execute=True, authorization={"authorized": True})
        plan = self._plan()
        forged = dict(plan)
        forged["candidate_byte_count"] += 1
        with self.assertRaises(Exception):
            authorize_operator_refresh(
                self.root, forged, operator_name="Anatoly Maslennikov", journal_author="anatoly-m-maslennikov",
                llm_session={"app": "test", "uuid": "forged"}, authorization_ref=relocation._EXPECTED["authorization_ref"],
            )
        self.assertEqual(self.before, self.path.read_bytes())

    def test_publish_appends_shared_journal_receipt_and_readback(self) -> None:
        with self._git():
            result = refresh_release_manifest(self.root, execute=True, authorization=self._authorization())
        self.assertEqual("published", result["disposition"])
        self.assertTrue(result["recording_ref"].startswith("journal:release-manifest:"))
        loaded = load_selected_manifest(self.root)
        self.assertEqual(16, len(loaded["routes"]))
        self.assertEqual([], self._pending())

    def test_second_execute_refuses_without_replay(self) -> None:
        with self._git():
            refresh_release_manifest(self.root, execute=True, authorization=self._authorization())
        published = self.path.read_bytes()
        with self.assertRaises(ReleaseManifestPublishError):
            self._plan()
        self.assertEqual(published, self.path.read_bytes())

    def test_recording_only_recovery_never_replays_write(self) -> None:
        original = work_journal.append_sealed_events
        calls = 0
        def fail_final(*args, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise work_journal.WorkJournalError("injected", "final append failure")
            return original(*args, **kwargs)
        with self._git(), patch("release_manifest_lifecycle.work_journal.append_sealed_events", side_effect=fail_final):
            result = refresh_release_manifest(self.root, execute=True, authorization=self._authorization())
        self.assertEqual("recording_required", result["disposition"])
        pending = self._pending()
        self.assertEqual(1, len(pending))
        before_recovery = self.path.read_bytes()
        # Recovery uses the sealed event only; it has no manifest-write input.
        from release_manifest_authorization import authorize_operator_publication_recovery
        context = authorize_operator_publication_recovery(
            self.root, pending[0], operator_name="Anatoly Maslennikov", journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "selected-source-relocation"},
            authorization_ref=relocation._EXPECTED["authorization_ref"],
        )
        recovered = recover_release_manifest_publish(self.root, pending_event_id=pending[0], authorization=context)
        self.assertEqual("recovered", recovered["disposition"])
        self.assertEqual(before_recovery, self.path.read_bytes())

    def test_prewrite_failure_keeps_pending_and_repeat_does_not_write(self) -> None:
        with self._git(), patch("release_manifest_publisher._atomic_write", side_effect=ReleaseManifestPublishError("injected")):
            result = refresh_release_manifest(self.root, execute=True, authorization=self._authorization())
        self.assertEqual("pending_publication", result["disposition"])
        self.assertEqual(self.before, self.path.read_bytes())
        pending = self._pending()
        self.assertEqual(1, len(pending))
        writes = 0
        from release_manifest_publisher import _atomic_write as original_write
        def counted_write(path, payload):
            nonlocal writes
            writes += 1
            return original_write(path, payload)
        with self._git(), patch("release_manifest_publisher._atomic_write", side_effect=counted_write):
            retry = refresh_release_manifest(self.root, execute=True, authorization=self._authorization())
        self.assertEqual("published", retry["disposition"])
        self.assertEqual(1, writes)
        self.assertEqual([], self._pending())
