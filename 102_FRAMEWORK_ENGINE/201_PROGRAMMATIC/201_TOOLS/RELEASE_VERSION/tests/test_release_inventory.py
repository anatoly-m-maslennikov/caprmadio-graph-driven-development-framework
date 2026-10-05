"""Persistent-resource inventory checks using the disposable release fixture."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_compilation import render_release_candidate  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE, tree_sha256  # noqa: E402
from release_inventory import ReleaseInventoryError, refuse_secret_path  # noqa: E402
from release_packaging import stage_framework_package  # noqa: E402
import test_release_compilation as compilation_test  # noqa: E402


class ReleaseInventoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = compilation_test.ReleaseCompilationTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def _render_and_stage(self):
        preflight, candidate = self.fixture.build()
        self.fixture.copy_source()
        handoff = render_release_candidate(candidate, preflight)
        result = stage_framework_package(self.fixture.root, handoff)
        return candidate, handoff, result

    def test_ephemeral_state_does_not_change_seal_or_retained_delivery(self) -> None:
        _baseline_preflight, baseline = self.fixture.build()
        self.fixture.write("102_FRAMEWORK_ENGINE/.caprmedio_tmp/receipt-state.json", b"receipt\n")
        self.fixture.write("102_FRAMEWORK_ENGINE/__pycache__/worker.cpython-313.pyc", b"bytecode\n")
        self.fixture.write("102_FRAMEWORK_ENGINE/.pytest_cache/v/cache/nodeids", b"cache\n")
        self.fixture.write("102_FRAMEWORK_ENGINE/.venv/bin/python", b"virtualenv\n")
        self.fixture.write("102_FRAMEWORK_ENGINE/.DS_Store", b"metadata\n")

        _cached_preflight, cached = self.fixture.build()
        self.assertEqual(cached.manifest, baseline.manifest)
        self.assertEqual(cached.authority, baseline.authority)

        self.fixture.copy_source()
        self.assertEqual(
            tree_sha256(self.fixture.root, CANONICAL_SOURCE_RELATIVE),
            tree_sha256(self.fixture.root, "101_LAYER_1_FRAMEWORK_METHODOLOGY/sources"),
        )
        handoff = render_release_candidate(cached, _cached_preflight)
        materialized = self.fixture.root / handoff.child_materialization_root
        (materialized / ".caprmedio_tmp").mkdir()
        (materialized / ".caprmedio_tmp/receipt-state.json").write_bytes(b"receipt\n")
        (materialized / "__pycache__").mkdir()
        (materialized / "__pycache__/compiled.pyc").write_bytes(b"bytecode\n")
        result = stage_framework_package(self.fixture.root, handoff)
        released = self.fixture.root / result["release_root"]
        self.assertTrue(result["staged"])
        self.assertFalse(any(".caprmedio_tmp" in row.source_path for row in handoff.package_rows))
        self.assertFalse(any("__pycache__" in row.source_path for row in handoff.package_rows))
        self.assertFalse(any(".pytest_cache" in row.source_path for row in handoff.package_rows))
        self.assertFalse(any(".venv" in row.source_path for row in handoff.package_rows))
        self.assertFalse(any(path.name == ".DS_Store" for path in released.rglob("*")))

    def test_unknown_persistent_resource_is_sealed_and_delivered(self) -> None:
        resource = self.fixture.write(
            "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/references/persistent-resource.bin",
            b"persisted resource\n",
            0o600,
        )

        candidate, handoff, result = self._render_and_stage()

        relative = resource.relative_to(self.fixture.root).as_posix()
        self.assertIn(relative, {row.source_path for row in candidate.manifest.source_inventory_rows})
        self.assertIn(relative, {row.source_path for row in handoff.package_rows})
        delivered = self.fixture.root / result["release_root"] / "SKILLS/ca/references/persistent-resource.bin"
        self.assertEqual(delivered.read_bytes(), b"persisted resource\n")
        self.assertEqual(delivered.stat().st_mode & 0o777, 0o600)

    def test_secret_shaped_names_refuse_before_any_byte_read(self) -> None:
        sentinel_names = (".env", ".env.release-sentinel", "release-sentinel.env")
        with patch.object(Path, "read_bytes", side_effect=AssertionError("secret bytes must not be read")) as read_bytes:
            for sentinel in sentinel_names:
                with self.subTest(sentinel=sentinel):
                    with self.assertRaises(ReleaseInventoryError) as direct:
                        refuse_secret_path(sentinel)
                    self.assertEqual(direct.exception.code, "release-inventory-secret-refused")
                    with self.assertRaises(ReleaseContractError) as tree:
                        tree_sha256(self.fixture.root, sentinel)
                    self.assertEqual(tree.exception.code, "release-inventory-secret-refused")
        read_bytes.assert_not_called()

    def test_pinned_docker_copy_inputs_are_required_and_revalidated(self) -> None:
        dockerfile = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile"
        (self.fixture.root / "pyproject.toml").unlink()
        (self.fixture.root / "uv.lock").unlink()
        self.fixture.write(dockerfile, b"FROM scratch\nCOPY pyproject.toml uv.lock ./\n")
        with self.assertRaises(ReleaseContractError) as missing:
            self.fixture.build()
        self.assertEqual(missing.exception.code, "release-image-input-missing")

        self.fixture.write("pyproject.toml", b"[project]\nname = 'fixture'\n")
        lock = self.fixture.write("uv.lock", b"version = 1\n")
        preflight, candidate = self.fixture.build()
        image_rows = {
            row.source_path: row.destination_path
            for row in candidate.manifest.source_inventory_rows
            if row.resource == "IMAGE_INPUT"
        }
        self.assertEqual(image_rows["pyproject.toml"], "IMAGE_INPUT/pyproject.toml")
        self.assertEqual(image_rows["uv.lock"], "IMAGE_INPUT/uv.lock")

        self.fixture.copy_source()
        lock.write_bytes(b"version = 2\n")
        with self.assertRaises(ReleaseContractError) as stale:
            render_release_candidate(candidate, preflight)
        self.assertEqual(stale.exception.code, "release-currentness-stale")


if __name__ == "__main__":
    unittest.main()
