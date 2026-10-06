"""Pure command-shape tests for the installed-N suite sandbox adapter."""

from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_image import DockerCommandResult
from release_contract import canonical_json
from release_suite import (
    CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE,
    COMPILED_ROOT_ENVIRONMENT_VARIABLE,
    PROJECT_ROOT_ENVIRONMENT_VARIABLE,
    REPORT_ENVIRONMENT_VARIABLE,
    SOURCE_BINDINGS_ENVIRONMENT_VARIABLE,
    SOURCE_BINDINGS_RELATIVE,
    SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE,
)
from release_suite_execution import (
    InstalledNSuiteDockerExecutor,
    SelectedNImageBinding,
)


IMAGE = "sha256:" + "a" * 64
SHA = "b" * 64
CONTEXT = "c" * 64
CONTAINER = "d" * 64


class GovernedSuiteBindingsTests(unittest.TestCase):
    def test_actual_module_rules_carrier_is_exact_canonical_json(self) -> None:
        # Read the governed carrier itself, not the canonical fixture below.
        # A single trailing newline is valid JSON but is not an admitted
        # sealed module-rules byte sequence.
        payload = (RELEASE_ROOT / "release_suite_bindings.json").read_bytes()
        self.assertEqual(payload, canonical_json(json.loads(payload)))


class FakeDocker:
    def __init__(self, *, inspect_payload=None, run_result=None):
        self.calls = []
        self.inspect_payload = inspect_payload or [{"Id": IMAGE, "Config": {"Labels": {
            "org.caprmedio.candidate": "N", "org.caprmedio.context": CONTEXT,
        }, "Env": ["PATH=/opt/caprmedio/bin:/usr/bin"]}}]
        self.run_result = run_result or DockerCommandResult(0, b"suite stdout", b"suite stderr")
        self.write_timeout_cid = True
        self.container_payload = [{"Id": CONTAINER, "Config": {"Labels": {
            "org.caprmedio.release-suite": SHA, "org.caprmedio.release-suite-attempt": "attempt-test",
        }}}]

    def run(self, argv, *, cwd, timeout_seconds):
        self.calls.append((tuple(argv), cwd, timeout_seconds))
        if argv[:3] == ("docker", "image", "inspect"):
            import json
            return DockerCommandResult(0, json.dumps(self.inspect_payload).encode(), b"")
        if argv[:2] == ("docker", "run"):
            if (self.run_result.timed_out or self.run_result.exit_code is None) and self.write_timeout_cid:
                Path(argv[argv.index("--cidfile") + 1]).write_text(CONTAINER, encoding="ascii")
            return self.run_result
        if argv[:3] == ("docker", "container", "inspect"):
            import json
            return DockerCommandResult(0, json.dumps(self.container_payload).encode(), b"")
        if argv[:3] == ("docker", "container", "rm"):
            return DockerCommandResult(0, b"removed\n", b"")
        raise AssertionError(argv)


class InstalledNSuiteDockerExecutorTests(unittest.TestCase):
    def setUp(self) -> None:
        # The Release suite intentionally retains attempt carriers.  Keep this
        # pure command fixture as a retained disposable carrier too: on this
        # macOS profile temp cleanup can be denied after nested mount-shaped
        # directories are created, and cleanup is not test evidence.
        self.root = Path(tempfile.mkdtemp())
        self.attempt = self.root / ".caprmedio_runtime/release_suite" / SHA / "attempt-test"
        self.workspace, self.output = self.attempt / "workspace", self.attempt / "output"
        self.workspace.mkdir(parents=True)
        self.output.mkdir()
        (self.workspace / "tests").mkdir()
        rules_relative = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_suite_bindings.json"
        test_relative = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_fixture.py"
        rules = canonical_json({"module_probes": [], "schema_version": 1})
        test_source = b"import unittest\n"
        for relative, payload in ((rules_relative, rules), (test_relative, test_source)):
            path = self.workspace / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
        rule_sha256 = hashlib.sha256(rules).hexdigest()
        test_sha256 = hashlib.sha256(test_source).hexdigest()
        bindings = canonical_json({
            "schema_version": 1,
            "candidate_snapshot_manifest_sha256": SHA,
            "mapping_rules": {"source_path": rules_relative, "sha256": rule_sha256},
            "package_rows": [
                {"resource": "FRAMEWORK_ENGINE", "source_path": rules_relative,
                 "destination_path": "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_suite_bindings.json",
                 "sha256": rule_sha256, "mode": 0o644},
                {"resource": "FRAMEWORK_ENGINE", "source_path": test_relative,
                 "destination_path": "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_fixture.py",
                 "sha256": test_sha256, "mode": 0o644},
            ],
        })
        bindings_path = self.workspace / SOURCE_BINDINGS_RELATIVE
        bindings_path.parent.mkdir(parents=True, exist_ok=True)
        bindings_path.write_bytes(bindings)
        self.bindings_sha256 = hashlib.sha256(bindings).hexdigest()
        selected_root = self.root / ".caprmedio_runtime/framework/releases/N"
        selected_root.mkdir(parents=True)
        (selected_root / "manifest.toml").write_text("schema_version = 1\n", encoding="utf-8")
        selector = self.root / ".caprmedio_runtime/framework/current.toml"
        selector.parent.mkdir(parents=True, exist_ok=True)
        selector_bytes = (
            'schema_version = 1\n'
            'candidate_snapshot_manifest_sha256 = "N"\n'
            'release = "N"\n'
            'candidate_release = "candidate"\n'
            'selected_release_root = ".caprmedio_runtime/framework/releases/N"\n'
            'framework_engine_root = ".caprmedio_runtime/framework/releases/N/FRAMEWORK_ENGINE"\n'
            'methodology_root = ".caprmedio_runtime/framework/releases/N/METHODOLOGY"\n'
            f'candidate_image_digest = "{IMAGE}"\n'
            f'candidate_image_context_sha256 = "{CONTEXT}"\n'
        ).encode("utf-8")
        selector.write_bytes(selector_bytes)
        self.docker = FakeDocker()
        self.executor = InstalledNSuiteDockerExecutor(
            root=self.root,
            docker=self.docker,
            candidate_snapshot_manifest_sha256=SHA,
            executing_release="N",
            image_digest=IMAGE,
            source_context_sha256=CONTEXT,
            selected_n_image=SelectedNImageBinding(
                IMAGE, "N", CONTEXT, False, hashlib.sha256(selector_bytes).hexdigest(),
                "candidate", "/opt/caprmedio/bin:/usr/bin"
            ),
            image_path="/opt/caprmedio/bin:/usr/bin",
            sealed_command=("python", "-m", "pytest"),
            sealed_working_directory="tests",
            compiled_root="compiled/candidate",
        )

    def environment(self) -> dict[str, str]:
        return {
            "PATH": "/opt/caprmedio/bin:/usr/bin",
            PROJECT_ROOT_ENVIRONMENT_VARIABLE: "/workspace",
            REPORT_ENVIRONMENT_VARIABLE: "/output/coverage.xml",
            COMPILED_ROOT_ENVIRONMENT_VARIABLE: "compiled/candidate",
            CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE: SHA,
            SOURCE_BINDINGS_ENVIRONMENT_VARIABLE: "/workspace/" + SOURCE_BINDINGS_RELATIVE,
            SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE: self.bindings_sha256,
        }

    def test_exact_command_uses_only_workspace_output_and_fixed_sandbox_controls(self) -> None:
        result = self.executor.run(
            ("python", "-m", "pytest"), workspace=self.workspace, output_root=self.output,
            working_directory="tests", environment=self.environment(), timeout_seconds=120,
        )

        self.assertEqual(result.exit_code, 0)
        # One reinspection verifies the exact selected immutable image and
        # image-derived PATH immediately before the isolated run.
        self.assertEqual(len(self.docker.calls), 2)
        argv = self.docker.calls[-1][0]
        self.assertEqual(argv[:8], ("docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL", "--security-opt=no-new-privileges", "--pids-limit=128"))
        self.assertIn(f"type=bind,src={self.workspace},dst=/workspace,readonly", argv)
        self.assertIn(f"type=bind,src={self.output},dst=/output", argv)
        self.assertFalse(any(item.startswith(f"type=bind,src={self.root},dst=") for item in argv))
        self.assertIn("/tmp:rw,nosuid,nodev,exec,size=1g,mode=1777", argv)
        self.assertIn("/workspace/.caprmedio_tmp:rw,nosuid,nodev,exec,size=1g,mode=1777", argv)
        scratch = self.workspace / ".caprmedio_tmp"
        self.assertTrue(scratch.is_dir())
        self.assertEqual(list(scratch.iterdir()), [])
        self.assertNotIn("/var/run/docker.sock", argv)
        self.assertIn("PATH=/opt/caprmedio/bin:/usr/bin", argv)
        self.assertIn(f"{SOURCE_BINDINGS_ENVIRONMENT_VARIABLE}=/workspace/{SOURCE_BINDINGS_RELATIVE}", argv)
        self.assertIn(f"{SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE}={self.bindings_sha256}", argv)
        self.assertIn("--cidfile", argv)
        self.assertIn("org.caprmedio.release-suite=" + SHA, argv)
        self.assertEqual(argv[argv.index("--entrypoint") + 1], "python")
        self.assertEqual(argv[-3:], (IMAGE, "-m", "pytest"))
        self.assertEqual(self.docker.calls[-1][1], self.root)

    def test_nonempty_image_entrypoint_is_overridden_by_the_sealed_command(self) -> None:
        self.docker.inspect_payload[0]["Config"]["Entrypoint"] = ["/image-start"]

        result = self.executor.run(
            ("python", "-m", "pytest"), workspace=self.workspace, output_root=self.output,
            working_directory="tests", environment=self.environment(), timeout_seconds=120,
        )

        self.assertEqual(result.exit_code, 0)
        argv = self.docker.calls[-1][0]
        self.assertEqual(argv[argv.index("--entrypoint") + 1], "python")
        self.assertEqual(argv[-3:], (IMAGE, "-m", "pytest"))
        self.assertNotIn("/image-start", argv)

    def test_mount_escape_and_environment_override_refuse_before_docker_run(self) -> None:
        from release_contract import ReleaseContractError
        outside = self.root.parent
        with self.assertRaises(ReleaseContractError) as escaped:
            self.executor.run(("python", "-m", "pytest"), workspace=outside, output_root=self.output,
                              working_directory="tests", environment=self.environment(), timeout_seconds=120)
        self.assertEqual(escaped.exception.code, "release-suite-executor-mount-unsafe")
        changed = self.environment() | {PROJECT_ROOT_ENVIRONMENT_VARIABLE: str(self.root)}
        with self.assertRaises(ReleaseContractError) as environment:
            self.executor.run(("python", "-m", "pytest"), workspace=self.workspace, output_root=self.output,
                              working_directory="tests", environment=changed, timeout_seconds=120)
        self.assertEqual(environment.exception.code, "release-suite-executor-environment-untrusted")
        self.assertEqual(self.docker.calls, [])

    def test_symlinked_or_nonleaf_mounts_and_host_path_reject_before_docker_run(self) -> None:
        from release_contract import ReleaseContractError
        outside = self.root / "outside"
        outside.mkdir()
        linked_attempt = self.attempt.parent / "attempt-symlink"
        linked_workspace = linked_attempt / "workspace"
        linked_output = linked_attempt / "output"
        linked_attempt.mkdir()
        linked_workspace.symlink_to(outside, target_is_directory=True)
        linked_output.mkdir()
        with self.assertRaises(ReleaseContractError) as linked:
            self.executor.run(("python", "-m", "pytest"), workspace=linked_workspace, output_root=linked_output,
                              working_directory="tests", environment=self.environment(), timeout_seconds=120)
        self.assertEqual(linked.exception.code, "release-suite-executor-mount-unsafe")
        self.assertEqual(self.docker.calls, [])

    def test_nonempty_or_symlinked_scratch_refuses_before_docker_run(self) -> None:
        from release_contract import ReleaseContractError

        scratch = self.workspace / ".caprmedio_tmp"
        scratch.mkdir()
        (scratch / "unexpected").write_text("not scratch", encoding="utf-8")
        with self.assertRaises(ReleaseContractError) as nonempty:
            self.executor.run(("python", "-m", "pytest"), workspace=self.workspace, output_root=self.output,
                              working_directory="tests", environment=self.environment(), timeout_seconds=120)
        self.assertEqual(nonempty.exception.code, "release-suite-executor-scratch-unsafe")
        self.assertEqual([call[0][:2] for call in self.docker.calls], [("docker", "image")])

        self.docker.calls.clear()

        (scratch / "unexpected").unlink()
        scratch.rmdir()
        target = self.root / "outside-scratch"
        target.mkdir()
        scratch.symlink_to(target, target_is_directory=True)
        with self.assertRaises(ReleaseContractError) as linked:
            self.executor.run(("python", "-m", "pytest"), workspace=self.workspace, output_root=self.output,
                              working_directory="tests", environment=self.environment(), timeout_seconds=120)
        self.assertEqual(linked.exception.code, "release-suite-executor-scratch-unsafe")
        self.assertEqual([call[0][:2] for call in self.docker.calls], [("docker", "image")])

    def test_timeout_never_becomes_a_successful_process_result(self) -> None:
        self.docker.run_result = DockerCommandResult(None, b"", b"timeout", timed_out=True)
        result = self.executor.run(("python", "-m", "pytest"), workspace=self.workspace, output_root=self.output,
                                   working_directory="tests", environment=self.environment(), timeout_seconds=120)
        self.assertTrue(result.timed_out)
        self.assertIsNone(result.exit_code)
        self.assertFalse(result.left_descendants)
        self.assertEqual(self.docker.calls[-2][0][:3], ("docker", "container", "inspect"))
        self.assertEqual(self.docker.calls[-1][0][:3], ("docker", "container", "rm"))

    def test_timeout_without_a_proven_container_leaves_descendant_state_unknown(self) -> None:
        self.docker.run_result = DockerCommandResult(None, b"", b"timeout", timed_out=True)
        self.docker.write_timeout_cid = False

        result = self.executor.run(("python", "-m", "pytest"), workspace=self.workspace, output_root=self.output,
                                   working_directory="tests", environment=self.environment(), timeout_seconds=120)

        self.assertTrue(result.timed_out)
        self.assertIsNone(result.exit_code)
        self.assertTrue(result.left_descendants)
        self.assertEqual(self.docker.calls[-1][0][:2], ("docker", "run"))

    def test_missing_exit_status_is_not_treated_as_a_clean_suite_completion(self) -> None:
        self.docker.run_result = DockerCommandResult(None, b"", b"no status")
        self.docker.write_timeout_cid = False

        result = self.executor.run(("python", "-m", "pytest"), workspace=self.workspace, output_root=self.output,
                                   working_directory="tests", environment=self.environment(), timeout_seconds=120)

        self.assertFalse(result.timed_out)
        self.assertIsNone(result.exit_code)
        self.assertTrue(result.left_descendants)

    def test_host_path_and_wrong_image_path_refuse_before_docker_run(self) -> None:
        from release_contract import ReleaseContractError
        wrong = self.environment() | {"PATH": os.defpath}
        with self.assertRaises(ReleaseContractError) as path:
            self.executor.run(("python", "-m", "pytest"), workspace=self.workspace, output_root=self.output,
                              working_directory="tests", environment=wrong, timeout_seconds=120)
        self.assertEqual(path.exception.code, "release-suite-executor-environment-untrusted")
        with self.assertRaises(ReleaseContractError) as output:
            self.executor.run(("python", "-m", "pytest"), workspace=self.workspace,
                              output_root=self.attempt / "other", working_directory="tests",
                              environment=self.environment(), timeout_seconds=120)
        self.assertEqual(output.exception.code, "release-suite-executor-mount-unsafe")
        self.assertEqual(self.docker.calls, [])

    def test_image_environment_with_a_second_value_refuses_before_container_run(self) -> None:
        from release_contract import ReleaseContractError

        self.docker.inspect_payload[0]["Config"]["Env"].append("UNDECLARED_SECRET=value")
        with self.assertRaises(ReleaseContractError) as image:
            self.executor.run(("python", "-m", "pytest"), workspace=self.workspace, output_root=self.output,
                              working_directory="tests", environment=self.environment(), timeout_seconds=120)
        self.assertEqual(image.exception.code, "release-suite-executor-n-unproven")
        self.assertEqual(len(self.docker.calls), 1)
        self.assertEqual(self.docker.calls[0][0][:3], ("docker", "image", "inspect"))


if __name__ == "__main__":
    unittest.main()
