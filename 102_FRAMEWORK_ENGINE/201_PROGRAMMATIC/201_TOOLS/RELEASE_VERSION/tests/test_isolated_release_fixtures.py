"""Host-Python dry tests for the isolated Release fixture runner.

These tests retain their fixture root under the host temporary directory on
purpose.  Docker is always mocked: they prove command construction and source
sealing without contacting a socket, building an image, or creating a real
container.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TEST_ROOT = Path(__file__).resolve().parent
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))

from run_isolated_release_fixtures import (  # noqa: E402
    DEPENDENCY_MODULES,
    FixtureIsolationError,
    SealedFixtureSnapshot,
    _arguments,
    _matches_requirement,
    prepare_snapshot,
    run_isolated_fixtures,
    verify_image_compatibility,
)


IMAGE = "sha256:" + "a" * 64


class IsolatedReleaseFixtureTests(unittest.TestCase):
    """All created files remain in one declared host-test fixture root."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture_root = Path(tempfile.mkdtemp(prefix="caprmedio-isolated-release-fixture-tests-"))
        print(f"retained_host_test_fixture_root: {cls.fixture_root}")

    def _project(self, name: str) -> Path:
        project = self.fixture_root / name
        engine = project / "102_FRAMEWORK_ENGINE" / "201_PROGRAMMATIC" / "201_TOOLS"
        engine.mkdir(parents=True, exist_ok=True)
        (engine / "fixture.py").write_text("fixture = True\n", encoding="utf-8")
        (project / "pyproject.toml").write_text(
            """[dependency-groups]
rmed-workflow-mcp = ["mcp==2.3.0", "PyYAML==6.0.3", "jsonschema>=4.23,<5"]
workflow-orchestrator = ["dbos==2.31.1", "pydantic==2.13.5", "PyYAML==6.0.3"]
validate-atoms = ["pydantic==2.13.5", "PyYAML==6.0.3"]
""",
            encoding="utf-8",
        )
        (project / "uv.lock").write_text("version = 1\n", encoding="utf-8")
        return project

    def _snapshot(self) -> SealedFixtureSnapshot:
        project = self._project("source")
        parent = self.fixture_root / "snapshots"
        parent.mkdir(exist_ok=True)
        with patch("run_isolated_release_fixtures.control_closure_paths", return_value=()), patch(
            "run_isolated_release_fixtures.subprocess.run"
        ) as docker:
            snapshot = prepare_snapshot(project, parent)
        docker.assert_not_called()
        return snapshot

    def test_prepare_snapshot_seals_current_regular_files_without_contacting_docker(self) -> None:
        snapshot = self._snapshot()
        records = {record.path: record for record in snapshot.records}
        self.assertIn("pyproject.toml", records)
        self.assertIn("uv.lock", records)
        self.assertIn("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/fixture.py", records)
        self.assertTrue((Path(snapshot.path) / ".caprmedio_isolated_release_fixture_snapshot.json").is_file())
        self.assertEqual(snapshot.dependency_requirements["jsonschema"], ">=4.23,<5")

    def test_prepare_snapshot_copies_exact_control_closure_rows_and_deduplicates_engine_overlap(self) -> None:
        """Closure derivation is mocked; byte/mode sealing remains real."""
        project = self._project("closure")
        control = project / ".caprmedio_caprmedio/controls/release.toml"
        control.parent.mkdir(parents=True)
        control.write_bytes(b"control = 'fixture'\n")
        control.chmod(0o700)
        parent = self.fixture_root / "closure-snapshots"
        parent.mkdir()
        closure = (
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/fixture.py",
            ".caprmedio_caprmedio/controls/release.toml",
        )
        with patch(
            "run_isolated_release_fixtures.control_closure_paths",
            return_value=closure,
            create=True,
        ), patch("run_isolated_release_fixtures.subprocess.run") as docker:
            snapshot = prepare_snapshot(project, parent)
        docker.assert_not_called()
        records = [record for record in snapshot.records if record.path == closure[0]]
        self.assertEqual(1, len(records))
        control_record = next(record for record in snapshot.records if record.path == closure[1])
        self.assertEqual(0o700, control_record.mode)
        self.assertEqual(__import__("hashlib").sha256(control.read_bytes()).hexdigest(), control_record.sha256)
        copied = Path(snapshot.path) / closure[1]
        self.assertEqual(control.read_bytes(), copied.read_bytes())
        self.assertEqual(0o700, copied.stat().st_mode & 0o777)

    def test_missing_unsafe_or_secret_closure_path_refuses_before_docker_or_secret_read(self) -> None:
        project = self._project("closure-refusal")
        parent = self.fixture_root / "closure-refusal-snapshots"
        parent.mkdir()
        secret = project / ".caprmedio_caprmedio/.env"
        original_read = Path.read_bytes
        read_paths: list[Path] = []

        def guarded_read(path: Path) -> bytes:
            read_paths.append(path)
            if path == secret:
                raise AssertionError("secret closure bytes were read")
            return original_read(path)

        for closure in (
            (".caprmedio_caprmedio/missing.toml",),
            ("../escape.toml",),
            (".caprmedio_caprmedio/.env",),
        ):
            with self.subTest(closure=closure), patch(
                "run_isolated_release_fixtures.control_closure_paths",
                return_value=closure,
                create=True,
            ), patch.object(Path, "read_bytes", autospec=True, side_effect=guarded_read), patch(
                "run_isolated_release_fixtures.subprocess.run"
            ) as docker:
                with self.assertRaises(FixtureIsolationError):
                    prepare_snapshot(project, parent)
            docker.assert_not_called()
        self.assertNotIn(secret, read_paths)

    def test_secret_shaped_engine_file_is_refused_before_its_bytes_are_read(self) -> None:
        project = self._project("secret")
        secret = project.resolve() / "102_FRAMEWORK_ENGINE" / ".env"
        parent = self.fixture_root / "secret-snapshots"
        parent.mkdir()
        original_read = Path.read_bytes
        read_paths: list[Path] = []

        def guarded_read(path: Path) -> bytes:
            read_paths.append(path)
            if path == secret:
                raise AssertionError("secret carrier bytes were read")
            return original_read(path)

        with patch(
            "run_isolated_release_fixtures.persistent_regular_files",
            return_value=[secret],
        ), patch("run_isolated_release_fixtures.control_closure_paths", return_value=()), patch.object(
            Path, "read_bytes", autospec=True, side_effect=guarded_read
        ):
            with self.assertRaises(FixtureIsolationError) as raised:
                prepare_snapshot(project, parent)
        self.assertIn("release-inventory-secret-refused", str(raised.exception))
        self.assertNotIn(secret, read_paths)

    def test_cli_requires_a_full_immutable_local_image_identifier(self) -> None:
        with self.assertRaises(SystemExit):
            _arguments(["--image", "caprmedio-runtime:latest"])
        options = _arguments(["--image", IMAGE])
        self.assertEqual(options.image, IMAGE)
        self.assertFalse(options.run)

    def test_dependency_ranges_accept_current_jsonschema_range_and_reject_outside_versions(self) -> None:
        self.assertTrue(_matches_requirement("4.25.1", ">=4.23,<5"))
        self.assertFalse(_matches_requirement("4.22.9", ">=4.23,<5"))
        self.assertFalse(_matches_requirement("5.0.0", ">=4.23,<5"))
        self.assertTrue(_matches_requirement("2.13.5", "==2.13.5"))
        self.assertTrue(_matches_requirement("4.23.0", "==4.23"))
        with self.assertRaises(FixtureIsolationError):
            _matches_requirement("4.25.1", ">=4.23,,<5")

    def test_image_preflight_is_no_network_no_socket_and_checks_source_inputs_and_import_versions(self) -> None:
        snapshot = self._snapshot()
        records = {record.path: record.sha256 for record in snapshot.records}
        payload = json.dumps(
            {
                "inputs": {"pyproject.toml": records["pyproject.toml"], "uv.lock": records["uv.lock"]},
                "versions": {
                    "pydantic": "2.13.5",
                    "PyYAML": "6.0.3",
                    "mcp": "2.3.0",
                    "jsonschema": "4.25.1",
                    "dbos": "2.31.1",
                },
            }
        )
        with patch(
            "run_isolated_release_fixtures.subprocess.run",
            return_value=subprocess.CompletedProcess(("docker",), 0, payload, ""),
        ) as docker:
            observed = verify_image_compatibility(IMAGE, snapshot)
        self.assertEqual(observed["versions"]["jsonschema"], "4.25.1")
        command = docker.call_args.args[0]
        self.assertEqual(command[:4], ("docker", "run", "--rm", "--network"))
        self.assertIn("none", command)
        self.assertIn("--read-only", command)
        self.assertNotIn("--mount", command)
        self.assertNotIn("--privileged", command)
        self.assertIn(IMAGE, command)

    def test_image_preflight_rejects_tags_before_contacting_docker(self) -> None:
        snapshot = self._snapshot()
        with patch("run_isolated_release_fixtures.subprocess.run") as docker:
            with self.assertRaises(FixtureIsolationError):
                verify_image_compatibility("caprmedio-runtime:latest", snapshot)
        docker.assert_not_called()

    def test_fixture_run_uses_only_a_readonly_source_bind_and_container_tmpfs(self) -> None:
        snapshot = self._snapshot()
        records = {record.path: record.sha256 for record in snapshot.records}
        preflight = json.dumps(
            {
                "inputs": {"pyproject.toml": records["pyproject.toml"], "uv.lock": records["uv.lock"]},
                "versions": {
                    "pydantic": "2.13.5",
                    "PyYAML": "6.0.3",
                    "mcp": "2.3.0",
                    "jsonschema": "4.25.1",
                    "dbos": "2.31.1",
                },
            }
        )
        docker_results = [
            subprocess.CompletedProcess(("docker",), 0, preflight, ""),
            subprocess.CompletedProcess(("docker",), 0),
        ]
        with patch("run_isolated_release_fixtures.subprocess.run", side_effect=docker_results) as docker:
            result = run_isolated_fixtures(IMAGE, snapshot, ["test_release_suite.ReleaseSuiteTests.test_golden"])
        self.assertEqual(result, 0)
        command = docker.call_args_list[1].args[0]
        self.assertIn("--network", command)
        self.assertIn("none", command)
        self.assertIn("--read-only", command)
        self.assertIn("--tmpfs", command)
        self.assertIn("--mount", command)
        self.assertEqual(1, command.count("--mount"))
        mount = command[command.index("--mount") + 1]
        self.assertEqual(mount, f"type=bind,source={snapshot.path},target=/workspace,readonly")
        self.assertNotIn("docker.sock", " ".join(command))
        self.assertNotIn("--privileged", command)
        self.assertIn("/opt/venv/bin/python", command)
        self.assertIn("--rm", command)
        self.assertIn("HOME=/home/caprmedio", command)
        self.assertIn("PYTHONNOUSERSITE=1", command)
        self.assertIn("PYTHONDONTWRITEBYTECODE=1", command)
        self.assertEqual("/tmp", command[command.index("--workdir") + 1])
        runner = command[command.index(IMAGE) + 1]
        self.assertEqual(
            "/workspace/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/retained_fixture_runner.py",
            runner,
        )
        self.assertTrue((TEST_ROOT.parents[4] / Path(runner).relative_to("/workspace")).is_file())

    def test_dependency_module_contract_has_no_undeclared_runtime_probe(self) -> None:
        self.assertEqual(set(DEPENDENCY_MODULES), {"pydantic", "PyYAML", "mcp", "jsonschema", "dbos"})


if __name__ == "__main__":
    unittest.main()
