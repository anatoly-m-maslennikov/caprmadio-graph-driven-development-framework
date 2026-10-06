"""Mocked, private bootstrap-image producer proof; never invokes Docker."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for directory in (RELEASE_ROOT, TEST_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from bootstrap_image_golden.fixture import materialize  # noqa: E402
import bootstrap_image  # noqa: E402
from framework_initialization import (  # noqa: E402
    PACKAGE_IMAGE_LABEL,
    SOURCE_CONTEXT_IMAGE_LABEL,
    plan_initial_framework_installation,
)
import framework_initialization as initialization  # noqa: E402
from framework_compiler_currentness import CanonicalCompilerCurrentness  # noqa: E402
from release_image import DockerCommandResult  # noqa: E402
from release_contract import canonical_json  # noqa: E402

# Test-first private producer API.  This module is intentionally absent until
# the publisher-owned implementation is supplied.
from bootstrap_image import (  # noqa: E402
    BootstrapImageError,
    produce_initial_framework_image,
    revalidate_initial_framework_image,
)


IMAGE_ID = "sha256:" + "a" * 64


class GoldenDocker:
    """A command-recording Docker double; no socket, daemon, or image exists."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, ...]] = []
        self.fail: str | None = None
        self.timeout: str | None = None
        self.inspect_id = IMAGE_ID
        self.image_id = IMAGE_ID
        self.labels: dict[str, str] = {}
        self.canary: dict[str, object] = {}
        self.spec: dict[str, object] = {}

    def run(self, argv, *, cwd: Path, timeout_seconds: int) -> DockerCommandResult:
        call = tuple(argv)
        self.calls.append(call)
        operation = "build" if "build" in call else "inspect" if call[:3] == ("docker", "image", "inspect") else "canary"
        if operation == "build":
            for index, item in enumerate(call):
                if item == "--label":
                    key, value = call[index + 1].split("=", 1)
                    self.labels[key] = value
            iidfile = Path(call[call.index("--iidfile") + 1])
            iidfile.write_text(self.image_id + "\n", encoding="utf-8")
            self.spec = json.loads((Path(call[-1]) / "bootstrap-canary.json").read_bytes())
            stdout = b"build output\n"
        elif operation == "inspect":
            stdout = json.dumps([{"Id": self.inspect_id, "Config": {"Labels": self.labels}}]).encode()
        else:
            payload = {
                "schema": "caprmedio.bootstrap_image_canary.v1",
                "image_digest": IMAGE_ID,
                "manifest_sha256": self.spec["manifest_sha256"],
                "source_context_sha256": self.spec["source_context_sha256"],
                "verified_files": len(self.spec["package_rows"]),
                "mcp_tools": ["get_mcp_reload_status", "query_artifact"],
                **self.canary,
            }
            stdout = json.dumps(payload, sort_keys=True).encode()
        return DockerCommandResult(
            17 if self.fail == operation else 0,
            stdout,
            b"golden stderr\n",
            self.timeout == operation,
        )


class BootstrapImageTests(unittest.TestCase):
    def setUp(self) -> None:
        retained = RELEASE_ROOT / ".caprmedio_tmp/tests/bootstrap-image"
        retained.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="bootstrap-image-", dir=retained))
        materialize(self.root)
        currentness = CanonicalCompilerCurrentness(
            compiled_root=".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY",
            source_root=".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources",
            compiler_entrypoint="102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
            compiler_entrypoint_sha256="c" * 64,
            source_frontier_digest="d" * 64,
            output_tree_digest="e" * 64,
            output_plan_sha256="f" * 64,
            source_snapshot=(("fixture", "a" * 64),),
        )
        self.currentness = currentness
        with patch.object(initialization, "verify_canonical_compiler_currentness", return_value=currentness):
            self.plan = plan_initial_framework_installation(self.root)
        self.docker = GoldenDocker()

    def produce(self, plan=None, docker=None):
        real_replace = os.replace

        def retained_fixture_replace(source, target):
            source_path, target_path = Path(source), Path(target)
            if source_path.is_dir():
                shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                return None
            return real_replace(source, target)

        # The managed host denies the production directory rename.  Model only
        # that primitive for the disposable retained fixture; byte sealing and
        # canonical proof validation remain production behavior.
        with patch.object(bootstrap_image.os, "replace", side_effect=retained_fixture_replace):
            return produce_initial_framework_image(plan or self.plan, executor=docker or self.docker)

    def test_produces_one_immutable_image_with_exact_two_plan_labels_and_canary(self) -> None:
        evidence = self.produce()
        self.assertEqual(evidence.image_digest, IMAGE_ID)
        self.assertEqual(evidence.outcome, "verified")
        self.assertEqual(evidence.manifest_sha256, self.plan.manifest_sha256)
        self.assertEqual(evidence.source_context_sha256, self.plan.source_context_sha256)
        self.assertEqual(
            self.docker.labels,
            {
                PACKAGE_IMAGE_LABEL: self.plan.manifest_sha256,
                SOURCE_CONTEXT_IMAGE_LABEL: self.plan.source_context_sha256,
            },
        )
        self.assertEqual([call[1] for call in self.docker.calls], ["build", "image", "run"])
        self.assertNotIn("--tag", self.docker.calls[0])
        self.assertNotIn("push", tuple(item for call in self.docker.calls for item in call))
        self.assertNotIn("rm", tuple(item for call in self.docker.calls for item in call))
        context = self.root / evidence.evidence_root / "context"
        self.assertEqual((context / "PACKAGE/manifest.toml").read_bytes(), self.plan.manifest_bytes)
        self.assertTrue((context / "pyproject.toml").is_file())
        self.assertTrue((context / "uv.lock").is_file())
        self.assertTrue((context / "bootstrap-canary.py").is_file())
        self.assertTrue((context / "bootstrap-canary.json").is_file())
        self.assertTrue((context / "102_FRAMEWORK_ENGINE").is_dir())
        pinned_dockerfile = self.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile"
        copied_dockerfile = context / pinned_dockerfile.relative_to(self.root)
        self.assertEqual(pinned_dockerfile.read_bytes(), copied_dockerfile.read_bytes())
        self.assertIn(b"COPY 102_FRAMEWORK_ENGINE ./102_FRAMEWORK_ENGINE", copied_dockerfile.read_bytes())
        self.assertIn(
            b"COPY --chown=${RUNTIME_UID}:${RUNTIME_GID} PACKAGE /opt/caprmedio-framework",
            (context / "Dockerfile").read_bytes(),
        )
        self.assertFalse((self.root / ".caprmedio_runtime/framework/current.toml").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/framework/releases").exists())
        self.assertFalse((self.root / ".agents/skills/ca").exists())

    def test_canonical_proof_preserves_sealed_executable_engine_row_mode(self) -> None:
        engine_path = self.root / next(
            row.source_path for row in self.plan.rows if row.resource == "FRAMEWORK_ENGINE"
        )
        original_mode = engine_path.stat().st_mode & 0o777
        engine_path.chmod(0o755)
        try:
            with patch.object(initialization, "verify_canonical_compiler_currentness", return_value=self.currentness):
                plan = plan_initial_framework_installation(self.root)
            docker = GoldenDocker()
            evidence = self.produce(plan, docker)
            self.assertEqual("verified", evidence.outcome)
            copied = self.root / evidence.evidence_root / "context" / engine_path.relative_to(self.root)
            self.assertEqual(0o755, copied.stat().st_mode & 0o777)
            self.assertEqual("verified", revalidate_initial_framework_image(plan, IMAGE_ID, executor=docker).outcome)
        finally:
            engine_path.chmod(original_mode)

    def test_d575_proof_key_paths_command_records_and_exact_immutable_bindings(self) -> None:
        evidence = self.produce()
        proof_key = hashlib.sha256(canonical_json([
            self.plan.manifest_sha256,
            IMAGE_ID,
        ])).hexdigest()
        relative = f".caprmedio_runtime/framework/bootstrap-image-evidence/{proof_key}"
        proof = self.root / relative
        self.assertEqual(relative, evidence.evidence_root)
        self.assertTrue((proof / "evidence.toml").is_file())
        self.assertTrue((proof / "context").is_dir())
        parsed = tomllib.loads((proof / "evidence.toml").read_text(encoding="utf-8"))
        self.assertEqual(proof_key, parsed["bootstrap_proof_key"])
        self.assertEqual(relative, parsed["proof_root"])
        self.assertEqual(relative + "/context", parsed["context_root"])

        records = json.loads((proof / "commands.json").read_bytes())
        self.assertEqual(["build", "inspect", "canary"], [record["phase"] for record in records])
        for record in records:
            phase = record["phase"]
            self.assertIsInstance(record["started_at_ns"], int)
            self.assertIsInstance(record["finished_at_ns"], int)
            self.assertLessEqual(record["started_at_ns"], record["finished_at_ns"])
            self.assertEqual(f"commands/{phase}/stdout", record["stdout_path"])
            self.assertEqual(f"commands/{phase}/stderr", record["stderr_path"])
            self.assertTrue((proof / record["stdout_path"]).is_file())
            self.assertTrue((proof / record["stderr_path"]).is_file())

        build, inspect, canary = [record["argv"] for record in records]
        self.assertIn(IMAGE_ID, inspect)
        self.assertIn(IMAGE_ID, canary)
        self.assertEqual({
            f"{PACKAGE_IMAGE_LABEL}={self.plan.manifest_sha256}",
            f"{SOURCE_CONTEXT_IMAGE_LABEL}={self.plan.source_context_sha256}",
        }, {build[index + 1] for index, item in enumerate(build) if item == "--label"})

    def test_canary_image_id_mismatch_and_missing_engine_copy_input_are_nonpassing(self) -> None:
        docker = GoldenDocker()
        docker.canary = {"image_digest": "sha256:" + "b" * 64}
        self.assertNotEqual("verified", produce_initial_framework_image(self.plan, executor=docker).outcome)

        dockerfile = self.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile"
        original = dockerfile.read_bytes()
        dockerfile.write_bytes(original.replace(b"COPY 102_FRAMEWORK_ENGINE ./102_FRAMEWORK_ENGINE\n", b""))
        try:
            self.assertNotEqual("verified", self.produce().outcome)
        finally:
            dockerfile.write_bytes(original)

    def test_refuses_wrong_immutable_id_or_label_only_image(self) -> None:
        for field, value in (
            ("image_id", "caprmedio-bootstrap:latest"),
            ("inspect_id", "sha256:" + "b" * 64),
            ("labels", {}),
        ):
            with self.subTest(field=field):
                setattr(self.docker, field, value)
                self.assertNotEqual("verified", self.produce().outcome)

    def test_failed_or_timed_out_effect_never_becomes_evidence(self) -> None:
        for operation in ("build", "inspect", "canary"):
            for kind in ("fail", "timeout"):
                with self.subTest(operation=operation, kind=kind):
                    docker = GoldenDocker()
                    setattr(docker, kind, operation)
                    evidence = produce_initial_framework_image(self.plan, executor=docker)
                    self.assertNotEqual(evidence.outcome, "verified")

    def test_readonly_revalidation_reopens_retained_proof_without_build_or_canary_replay(self) -> None:
        evidence = self.produce()
        before = list(self.docker.calls)
        reopened = revalidate_initial_framework_image(self.plan, evidence.image_digest, executor=self.docker)
        self.assertEqual(reopened.image_digest, evidence.image_digest)
        self.assertEqual(before + [("docker", "image", "inspect", IMAGE_ID)], self.docker.calls)

    def test_canary_output_must_bind_package_source_context_and_complete_mcp_proof(self) -> None:
        for forged in (
            {"manifest_sha256": "b" * 64},
            {"source_context_sha256": "c" * 64},
            {"verified_files": 1},
            {"mcp_tools": []},
            {"schema": "unbound"},
        ):
            with self.subTest(forged=forged):
                docker = GoldenDocker()
                docker.canary = forged
                self.assertNotEqual("verified", produce_initial_framework_image(self.plan, executor=docker).outcome)

    def test_revalidation_refuses_changed_source_context_modes_or_retained_proof_bytes(self) -> None:
        evidence = self.produce()
        cases = {
            "source": self.root / self.plan.rows[0].source_path,
            "context": self.root / evidence.evidence_root / "context/PACKAGE/manifest.toml",
            "command_output": self.root / evidence.evidence_root / "commands/build/stdout",
        }
        for label, path in cases.items():
            with self.subTest(label=label):
                original = path.read_bytes()
                path.write_bytes(original + b"changed")
                try:
                    with self.assertRaises(BootstrapImageError):
                        revalidate_initial_framework_image(self.plan, IMAGE_ID, executor=self.docker)
                finally:
                    path.write_bytes(original)

        source = self.root / self.plan.rows[0].source_path
        mode = source.stat().st_mode & 0o777
        source.chmod(0o600)
        try:
            with self.assertRaises(BootstrapImageError):
                revalidate_initial_framework_image(self.plan, IMAGE_ID, executor=self.docker)
        finally:
            source.chmod(mode)

    def test_revalidation_refuses_missing_source_or_context_carrier_before_inspection(self) -> None:
        evidence = self.produce()
        cases = {
            "source": self.root / self.plan.rows[0].source_path,
            "context": self.root / evidence.evidence_root / "context/PACKAGE/manifest.toml",
        }
        for label, path in cases.items():
            with self.subTest(label=label):
                original = path.read_bytes()
                path.unlink()
                before = list(self.docker.calls)
                try:
                    with self.assertRaises(BootstrapImageError):
                        revalidate_initial_framework_image(self.plan, IMAGE_ID, executor=self.docker)
                    self.assertEqual(before, self.docker.calls)
                finally:
                    path.write_bytes(original)

    def test_revalidation_refuses_missing_retained_output_and_changed_image_labels_without_effect_replay(self) -> None:
        evidence = self.produce()
        output = self.root / evidence.evidence_root / "commands/inspect/stderr"
        original = output.read_bytes()
        output.unlink()
        before = list(self.docker.calls)
        with self.assertRaises(BootstrapImageError):
            revalidate_initial_framework_image(self.plan, IMAGE_ID, executor=self.docker)
        self.assertEqual(before, self.docker.calls)

        # A fresh inspection is the only permitted revalidation effect, and
        # labels no longer prove the image after the retained bytes are fixed.
        output.write_bytes(original)
        evidence = self.produce()
        self.docker.labels.clear()
        before = list(self.docker.calls)
        with self.assertRaises(BootstrapImageError):
            revalidate_initial_framework_image(self.plan, IMAGE_ID, executor=self.docker)
        self.assertEqual(before + [("docker", "image", "inspect", IMAGE_ID)], self.docker.calls)

    def test_revalidation_keeps_test_double_origin_despite_fresh_subprocess_inspect(self) -> None:
        evidence = self.produce()
        self.assertEqual("test-double", evidence.execution_kind)
        actual = bootstrap_image.DockerSubprocessExecutor()
        fresh = DockerCommandResult(
            0,
            json.dumps([{"Id": IMAGE_ID, "Config": {"Labels": self.docker.labels}}]).encode(),
            b"fresh inspect stderr\n",
        )
        # Patch the subprocess boundary itself: this exercises the actual-executor
        # type branch without contacting a Docker daemon.
        with patch.object(actual, "run", return_value=fresh) as run:
            reopened = revalidate_initial_framework_image(self.plan, IMAGE_ID, executor=actual)
        self.assertEqual("test-double", reopened.execution_kind)
        run.assert_called_once_with(("docker", "image", "inspect", IMAGE_ID), cwd=self.root, timeout_seconds=60)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
