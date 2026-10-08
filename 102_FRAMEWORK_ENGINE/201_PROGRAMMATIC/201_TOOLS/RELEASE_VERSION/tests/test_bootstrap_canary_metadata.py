"""Execute the fixed canary's inventory statements against real fixture files."""

from __future__ import annotations

import ast
import hashlib
import json
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

import bootstrap_image  # noqa: E402
from release_contract import canonical_json  # noqa: E402
from release_handoff import PackageRow  # noqa: E402
from release_packaging import _render_manifest  # noqa: E402


LEGACY_PROGRAM_SHA256 = "40ac5ae85db43860e0882e46d327bb63b816c50978a4ff5b14e4f90d1268ff99"
LEGACY_INVENTORY = b"if p.is_file()} == expected\n"
METADATA_INVENTORY = b"if p.is_file() and p.name != '.DS_Store'} == expected\n"


class BootstrapCanaryMetadataTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="bootstrap-canary-inventory-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.package = self.root / "PACKAGE"
        self.package.mkdir()
        rows = []
        for resource, source, destination, payload, mode in (
            ("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/entry.py", "FRAMEWORK_ENGINE/entry.py", b"sealed engine\n", 0o755),
            ("METHODOLOGY", "sources/rule.md", "METHODOLOGY/sources/rule.md", b"sealed rule\n", 0o644),
        ):
            path = self.package / destination
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
            path.chmod(mode)
            rows.append(PackageRow(resource=resource, source_path=source, destination_path=destination,
                                   sha256=hashlib.sha256(payload).hexdigest(), mode=mode))
        self.rows = tuple(rows)
        source_context = "d" * 64
        manifest = _render_manifest(source_context, self.rows).encode("utf-8")
        (self.package / "manifest.toml").write_bytes(manifest)
        self.spec = self.root / "bootstrap-canary.json"
        self.spec.write_bytes(canonical_json({
            "manifest_sha256": hashlib.sha256(manifest).hexdigest(),
            "source_context_sha256": source_context,
            "package_rows": [{"resource": row.resource, "source_path": row.source_path,
                              "destination": row.destination_path, "sha256": row.sha256, "mode": row.mode}
                             for row in self.rows],
        }))

    def execute_inventory(self, program: bytes | None = None) -> None:
        # Run the actual fixed program up to its MCP probe, not a second
        # implementation of its inventory/hash/mode checks. Only the two
        # absolute image paths are mapped to the disposable fixture.
        parsed = ast.parse(program if program is not None else bootstrap_image._metadata_canary())
        statements = []
        for statement in parsed.body:
            if isinstance(statement, ast.AsyncFunctionDef):
                break
            if not isinstance(statement, (ast.Import, ast.ImportFrom)):
                statements.append(statement)

        def image_path(value):
            paths = {"/opt/caprmedio-framework": self.package,
                     "/opt/caprmedio-bootstrap-canary.json": self.spec}
            return paths[value]

        exec(compile(ast.Module(body=statements, type_ignores=[]), "fixed-canary-inventory", "exec"),
             {"Path": image_path, "hashlib": hashlib, "json": json, "tomllib": tomllib})

    def test_legacy_bytes_and_only_metadata_inventory_change(self) -> None:
        legacy = bootstrap_image._canary()
        self.assertEqual(LEGACY_PROGRAM_SHA256, hashlib.sha256(legacy).hexdigest())
        self.assertEqual(1, legacy.count(LEGACY_INVENTORY))
        self.assertEqual(legacy.replace(LEGACY_INVENTORY, METADATA_INVENTORY, 1),
                         bootstrap_image._metadata_canary())

    def test_exact_package_passes_both_inventory_programs(self) -> None:
        self.execute_inventory()
        self.execute_inventory(bootstrap_image._canary())

    def test_generation_refuses_unadmitted_current_probe_bytes(self) -> None:
        changed = bootstrap_image._canary() + b"print('unadmitted current probe')\n"
        with patch.object(bootstrap_image, "_canary", return_value=changed):
            with self.assertRaises(bootstrap_image.BootstrapImageError):
                bootstrap_image._metadata_canary()

    def test_ds_store_at_any_package_depth_is_ignored_without_mutation(self) -> None:
        metadata = [self.package / ".DS_Store", self.package / "METHODOLOGY/.DS_Store",
                    self.package / "METHODOLOGY/sources/.DS_Store"]
        for path in metadata:
            path.write_bytes(b"Finder metadata is not package content\n")
        self.execute_inventory()
        self.assertEqual([b"Finder metadata is not package content\n"] * len(metadata),
                         [path.read_bytes() for path in metadata])
        with self.assertRaises(AssertionError):
            self.execute_inventory(bootstrap_image._canary())

    def test_other_extra_files_are_not_ignored(self) -> None:
        for name in ("unowned.txt", ".ds_store", ".DS_Store.bak", "fixture.pyc"):
            with self.subTest(name=name):
                extra = self.package / name
                extra.write_bytes(b"unadmitted file\n")
                try:
                    with self.assertRaises(AssertionError):
                        self.execute_inventory()
                finally:
                    extra.unlink()

    def test_missing_real_package_file_is_rejected(self) -> None:
        path = self.package / self.rows[0].destination_path
        path.unlink()
        with self.assertRaises(AssertionError):
            self.execute_inventory()

    def test_tampered_real_package_bytes_or_mode_are_rejected(self) -> None:
        path = self.package / self.rows[0].destination_path
        original = path.read_bytes()
        path.write_bytes(original + b"tampered\n")
        with self.assertRaises(AssertionError):
            self.execute_inventory()
        path.write_bytes(original)
        path.chmod(0o644)
        with self.assertRaises(AssertionError):
            self.execute_inventory()

    def test_manifest_or_source_context_mismatch_is_rejected(self) -> None:
        manifest = self.package / "manifest.toml"
        original = manifest.read_bytes()
        manifest.write_bytes(original + b"\n")
        with self.assertRaises(AssertionError):
            self.execute_inventory()
        manifest.write_bytes(original)
        spec = json.loads(self.spec.read_bytes())
        spec["source_context_sha256"] = "e" * 64
        self.spec.write_bytes(canonical_json(spec))
        with self.assertRaises(AssertionError):
            self.execute_inventory()


if __name__ == "__main__":
    unittest.main()
