"""Narrow stale-Release-admission refresh-base contract tests."""
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
REPOSITORY = MCP.parents[2]
if str(MCP) not in sys.path:
    sys.path.insert(0, str(MCP))

import release_source_admission as admission_module  # noqa: E402
from release_manifest_authorization import authorize_operator_publication  # noqa: E402
from release_manifest_publisher import (  # noqa: E402
    plan_release_manifest_publish,
    publish_release_manifest,
)
from release_source_admission import (  # noqa: E402
    AUTHORITY_REF,
    derive_release_graph_admission,
    derive_release_private_carriers,
    derive_release_source_admission,
)
from selected_routes import (  # noqa: E402
    SELECTED_ROUTE_NAMES,
    SelectedRouteError,
    canonical_digest,
    canonical_json,
    load_release_manifest_refresh_base,
    load_selected_manifest,
    selected_manifest_ref,
)


def _pin_paths(value: object) -> list[str]:
    if isinstance(value, dict):
        paths = [value["source_path"]] if isinstance(value.get("source_path"), str) else []
        for child in value.values():
            paths.extend(_pin_paths(child))
        return paths
    if isinstance(value, list):
        paths: list[str] = []
        for child in value:
            paths.extend(_pin_paths(child))
        return paths
    return []


class ReleaseManifestRefreshBaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source_manifest = json.loads(
            (REPOSITORY / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json").read_text(
                encoding="utf-8"
            )
        )
        cls.current_admission = derive_release_source_admission(REPOSITORY)
        cls.private_carriers = derive_release_private_carriers(REPOSITORY)

    def setUp(self) -> None:
        scratch = REPOSITORY / ".caprmedio_tmp/epic-resume-fixtures/release-manifest-refresh-base"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=scratch)
        self._restore_pin = lambda: None
        self.root = Path(self.temporary.name)
        self._copy_manifest_closure()
        self.manifest_path = self.root / selected_manifest_ref(self.root)
        initial = copy.deepcopy(self.source_manifest)
        initial["routes"] = [
            route for route in initial["routes"] if route["route"] != "release_version"
        ]
        initial.pop("release_source_admissions", None)
        self._save(initial)
        initial_plan = plan_release_manifest_publish(self.root)
        initial_context = authorize_operator_publication(
            self.root,
            initial_plan,
            operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "refresh-base-initial"},
            authorization_ref="authorization/refresh-base-initial.md",
        )
        with patch(
            "release_manifest_lifecycle.subprocess.run",
            return_value=types.SimpleNamespace(returncode=0, stdout="0" * 40 + "\n"),
        ):
            result = publish_release_manifest(self.root, execute=True, authorization=initial_context)
        self.assertEqual("published", result["disposition"])
        self.initial_manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        self._advance_accepted_pin()

    def tearDown(self) -> None:
        self._restore_pin()
        self.temporary.cleanup()

    def _copy(self, relative: str) -> None:
        source = REPOSITORY / relative
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)

    def _copy_manifest_closure(self) -> None:
        manifest = copy.deepcopy(self.source_manifest)
        self._copy(".caprmedio_caprmedio/caprmedio_project_settings.toml")
        self._copy(".caprmedio_caprmedio/operators_registry.toml")
        self._copy(manifest["source_freshness"]["selected_source_registry_ref"])
        for relative in _pin_paths(manifest["routes"]):
            self._copy(relative)
        for relative in _pin_paths(manifest["query_source_admissions"]):
            self._copy(relative)
        admission = self.current_admission
        for relative in _pin_paths(admission):
            self._copy(relative)
        self._copy(AUTHORITY_REF)
        for row in self.private_carriers:
            self._copy(row["source_path"])
        manifest_path = self.root / selected_manifest_ref(self.root)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(canonical_json(manifest) + "\n", encoding="utf-8")

    def _save(self, manifest: dict[str, object]) -> None:
        manifest["source_freshness"]["selected_binding_digest"] = canonical_digest(manifest["routes"])
        unsigned = {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
        manifest["canonical_manifest_sha256"] = canonical_digest(unsigned)
        self.manifest_path.write_text(canonical_json(manifest) + "\n", encoding="utf-8")

    def _advance_accepted_pin(self) -> None:
        """Make the published sixteen-route fixture stale through one accepted pin."""
        admission = self.initial_manifest["release_source_admissions"][0]
        private_paths = {row["source_path"] for row in self.private_carriers}
        pin = next(
            item for item in admission["rmed_frontier"]
            if item["source_path"] not in private_paths and item is not admission["rmed_frontier"][6]
        )
        source = self.root / pin["source_path"]
        authority = self.root / AUTHORITY_REF
        source_before, authority_before = source.read_bytes(), authority.read_bytes()
        source_after = re.sub(
            rf"(?m)^version:\s*{pin['version']}\s*$",
            f"version: {pin['version'] + 1}",
            source_before.decode("utf-8"),
            count=1,
        ).encode("utf-8")
        self.assertNotEqual(source_before, source_after)
        digest_after = hashlib.sha256(source_after).hexdigest()
        old_row = f"| {pin['atom_id']} | {pin['version']} | `{pin['source_path']}` | `{pin['digest']}` |"
        new_row = f"| {pin['atom_id']} | {pin['version'] + 1} | `{pin['source_path']}` | `{digest_after}` |"
        authority_after = authority_before.decode("utf-8").replace(old_row, new_row, 1).encode("utf-8")
        self.assertNotEqual(authority_before, authority_after)
        source.write_bytes(source_after)
        authority.write_bytes(authority_after)
        authority_patch = patch.object(
            admission_module,
            "AUTHORITY_PIN",
            {**admission_module.AUTHORITY_PIN, "digest": hashlib.sha256(authority_after).hexdigest()},
        )
        authority_patch.start()

        def restore() -> None:
            authority_patch.stop()
            source.write_bytes(source_before)
            authority.write_bytes(authority_before)

        self._restore_pin = restore

    def test_accepts_only_stale_admission_and_retains_old_record(self) -> None:
        before = self.manifest_path.read_bytes()
        result = load_release_manifest_refresh_base(self.root)
        self.assertEqual([*SELECTED_ROUTE_NAMES, "release_version"],
                         [route["route"] for route in result["routes"]])
        self.assertEqual(self.initial_manifest["release_source_admissions"], result["release_source_admissions"])
        self.assertEqual(before, self.manifest_path.read_bytes())
        self.assertEqual(result["manifest_ref"], selected_manifest_ref(self.root))

    def test_old_rmed_carrier_is_not_reopened_by_refresh_base(self) -> None:
        relative = self.initial_manifest["release_source_admissions"][0]["rmed_frontier"][6]["source_path"]
        path = self.root / relative
        original = path.read_bytes()
        path.unlink()
        try:
            result = load_release_manifest_refresh_base(self.root)
            self.assertEqual(self.initial_manifest["release_source_admissions"], result["release_source_admissions"])
        finally:
            path.write_bytes(original)

    def test_manifest_leaf_and_ancestor_symlinks_refuse_before_read(self) -> None:
        target = self.root / "manifest-copy.json"
        target.write_bytes(self.manifest_path.read_bytes())
        self.manifest_path.unlink()
        self.manifest_path.symlink_to(target)
        with self.assertRaises(SelectedRouteError):
            load_release_manifest_refresh_base(self.root)

        self.manifest_path.unlink()
        target.unlink()
        self._copy_manifest_closure()
        self.manifest_path = self.root / selected_manifest_ref(self.root)
        projection = self.manifest_path.parent
        target_dir = self.root / "projection-copy"
        target_dir.mkdir()
        shutil.copyfile(self.manifest_path, target_dir / self.manifest_path.name)
        self.manifest_path.unlink()
        projection.rmdir()
        projection.symlink_to(target_dir, target_is_directory=True)
        with self.assertRaises(SelectedRouteError):
            load_release_manifest_refresh_base(self.root)

    def test_no_admission_drift_refuses_refresh(self) -> None:
        manifest = copy.deepcopy(self.initial_manifest)
        _, current = derive_release_graph_admission(self.root)
        manifest["release_source_admissions"] = [current]
        self._save(manifest)
        with self.assertRaisesRegex(SelectedRouteError, "no admission drift"):
            load_release_manifest_refresh_base(self.root)

    def test_release_route_must_match_current_source_derived_route(self) -> None:
        manifest = copy.deepcopy(self.initial_manifest)
        manifest["routes"][-1]["mutation_capable"] = False
        self._save(manifest)
        with self.assertRaisesRegex(SelectedRouteError, "Release route differs"):
            load_release_manifest_refresh_base(self.root)

    def test_pin_identity_and_non_pin_occurrence_drift_refuse(self) -> None:
        manifest = copy.deepcopy(self.initial_manifest)
        manifest["release_source_admissions"][0]["rmed_frontier"][6]["atom_id"] = "CA-R-9999"
        self._save(manifest)
        with self.assertRaises(SelectedRouteError):
            load_release_manifest_refresh_base(self.root)

        manifest = copy.deepcopy(self.initial_manifest)
        steps = manifest["release_source_admissions"][0]["ordered_steps"]
        steps[0], steps[1] = steps[1], steps[0]
        self._save(manifest)
        with self.assertRaises(SelectedRouteError):
            load_release_manifest_refresh_base(self.root)

    def test_version_digest_drift_is_allowed_at_each_legal_pin_site(self) -> None:
        locations = (
            ("acceptance_frontier", ("acceptance_frontier",)),
            ("workflow", ("workflow",)),
            ("ordered_step_step", ("ordered_steps", 0, "step")),
            ("ordered_step_action", ("ordered_steps", 0, "action")),
            ("ordered_action", ("ordered_actions", 0)),
            ("rmed_frontier", ("rmed_frontier", 0)),
        )
        for _, location in locations:
            manifest = copy.deepcopy(self.initial_manifest)
            pin: object = manifest["release_source_admissions"][0]
            for part in location:
                pin = pin[part]  # type: ignore[index]
            pin["version"] = 99  # type: ignore[index]
            pin["digest"] = "0" * 64  # type: ignore[index]
            self._save(manifest)
            load_release_manifest_refresh_base(self.root)

    def test_unknown_admission_fields_and_invalid_pin_shapes_refuse(self) -> None:
        manifest = copy.deepcopy(self.initial_manifest)
        manifest["release_source_admissions"][0]["caller_approval"] = True
        self._save(manifest)
        with self.assertRaises(SelectedRouteError):
            load_release_manifest_refresh_base(self.root)

        manifest = copy.deepcopy(self.initial_manifest)
        manifest["schema_version"] = True
        self._save(manifest)
        with self.assertRaises(SelectedRouteError):
            load_release_manifest_refresh_base(self.root)

        manifest = copy.deepcopy(self.initial_manifest)
        manifest["source_freshness"]["selected_binding_ref"] = "other-manifest.json#/routes"
        self._save(manifest)
        with self.assertRaises(SelectedRouteError):
            load_release_manifest_refresh_base(self.root)

        manifest = copy.deepcopy(self.initial_manifest)
        pin = manifest["release_source_admissions"][0]["rmed_frontier"][6]
        pin["version"] = True
        self._save(manifest)
        with self.assertRaises(SelectedRouteError):
            load_release_manifest_refresh_base(self.root)

    def test_strict_loader_still_rejects_the_stale_admission(self) -> None:
        with self.assertRaises(SelectedRouteError):
            load_selected_manifest(self.root)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
