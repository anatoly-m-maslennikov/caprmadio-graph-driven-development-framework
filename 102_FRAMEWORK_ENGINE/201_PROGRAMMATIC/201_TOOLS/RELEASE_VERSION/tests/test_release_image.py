"""Fake Docker command goldens; these are never actual image/Release proof."""

from __future__ import annotations

import json
import sys
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for directory in (RELEASE_ROOT, TEST_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from release_contract import ReleaseContractError
from release_image import (
    DockerCommandResult, build_candidate_image, verify_candidate_image, retire_prior_image,
    verify_bound_image_evidence,
)
from release_suite import execute_bound_release_suite
import test_release_suite as suite_test

IMAGE_ID = "sha256:" + "a" * 64


class FakeDocker:
    """Explicit command/output fixture, no daemon, socket, image or container."""

    def __init__(self):
        self.calls = []
        self.labels = {}
        self.spec = {}
        self.fail = None
        self.forge = None
        self.after = None
        self.timeout = None

    def run(self, argv, *, cwd, timeout_seconds):
        self.calls.append(tuple(argv))
        operation = argv[1]
        if operation == "build":
            context = Path(argv[-1])
            self.spec = json.loads((context / "canary.json").read_bytes())
            for index, item in enumerate(argv):
                if item == "--label":
                    key, value = argv[index + 1].split("=", 1)
                    self.labels[key] = value
            Path(argv[argv.index("--iidfile") + 1]).write_text(IMAGE_ID + "\n")
            stdout = b"#1 DONE\nwriting image sha256:aaaaaaaa\n"
        elif operation == "image":
            stdout = json.dumps([{"Id": IMAGE_ID, "Config": {"Labels": self.labels}}]).encode()
        elif operation == "run":
            output = {
                "schema": "caprmedio.release_version.image_canary.v1",
                "candidate_snapshot_manifest_sha256": self.spec["candidate_snapshot_manifest_sha256"],
                "package_manifest_sha256": self.spec["package_manifest_sha256"],
                "verified_files": len(self.spec["package_rows"]),
                "mcp_tools": ["get_mcp_reload_status", "query_artifact"],
            }
            if self.forge:
                output.update(self.forge)
            stdout = json.dumps(output).encode()
        else:
            raise AssertionError(tuple(argv))
        if self.after:
            self.after(operation)
        return DockerCommandResult(17 if self.fail == operation else 0, stdout, b"fixture stderr\n", self.timeout == operation)


class ReleaseImageTests(unittest.TestCase):
    def setUp(self):
        self.fixture = suite_test.ReleaseSuiteTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.fixture.fixture.write("pyproject.toml", b"[project]\nname = 'fixture'\nversion = '0.0.0'\n")
        self.fixture.fixture.write("uv.lock", b"version = 1\n")
        self.fixture.fixture.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile",
                                   b"FROM scratch\nCOPY pyproject.toml uv.lock ./\nCOPY 102_FRAMEWORK_ENGINE ./102_FRAMEWORK_ENGINE\n")
        self.candidate, self.compilation = self.fixture.bound()
        self.suite = execute_bound_release_suite(self.candidate, self.compilation)
        self.assertTrue(self.suite.passed)
        self.docker = FakeDocker()

    def build(self):
        return build_candidate_image(self.candidate, self.compilation, self.suite, executor=self.docker)

    def test_golden_exact_private_context_complete_package_immutable_build_and_canary(self):
        selector = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        build = self.build()
        self.assertEqual(build.outcome, "built")
        self.assertEqual(build.candidate_image_digest, IMAGE_ID)
        context = self.root / build.context_root
        self.assertEqual((context / "PACKAGE/manifest.toml").read_bytes(),
                         (self.root / self.fixture.package["release_root"] / "manifest.toml").read_bytes())
        self.assertTrue((context / "PACKAGE/METHODOLOGY/compiled").is_dir())
        self.assertTrue((context / "PACKAGE/SKILLS/ca/agents/openai.yaml").is_file())
        self.assertTrue((context / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md").is_file())
        self.assertIn(b"COPY PACKAGE /opt/caprmedio-framework", (context / "Dockerfile").read_bytes())
        self.assertNotIn("--tag", self.docker.calls[0])
        verified = verify_candidate_image(self.candidate, self.compilation, self.suite, build, executor=self.docker)
        self.assertEqual(verified.outcome, "verified")
        self.assertEqual(verified.candidate_image_digest, IMAGE_ID)
        self.assertEqual(verified.execution_kind, "test-double")
        with self.assertRaises(ReleaseContractError):
            verify_bound_image_evidence(self.candidate, self.compilation, self.suite, build, verified)
        run = next(call for call in self.docker.calls if call[1] == "run")
        self.assertIn(IMAGE_ID, run)
        self.assertIn("--network=none", run)
        self.assertNotIn("-v", run)
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector)

    def test_failed_build_retains_context_and_no_verified_identity(self):
        self.docker.fail = "build"
        result = self.build()
        self.assertEqual(result.outcome, "failed")
        self.assertIsNone(result.candidate_image_digest)
        self.assertTrue((self.root / result.context_root).is_dir())
        self.assertEqual(len(self.docker.calls), 1)

    def test_build_inspect_identity_mismatch_is_incomplete(self):
        self.docker.after = lambda operation: self.docker.labels.clear() if operation == "build" else None
        self.assertEqual(self.build().outcome, "incomplete")

    def test_forged_suite_receipt_refused_before_docker(self):
        with self.assertRaises(ReleaseContractError):
            build_candidate_image(self.candidate, self.compilation, replace(self.suite, receipt_sha256="b" * 64), executor=self.docker)
        self.assertEqual(self.docker.calls, [])

    def test_stale_input_refused_before_docker(self):
        self.fixture.fixture.core.write_bytes(b"changed authority")
        with self.assertRaises((ReleaseContractError, ValueError)):
            self.build()
        self.assertEqual(self.docker.calls, [])

    def test_partial_package_refused_before_docker(self):
        path = self.root / self.fixture.package["release_root"] / "SKILLS/ca/SKILL.md"
        path.unlink()
        with self.assertRaises(Exception):
            self.build()
        self.assertEqual(self.docker.calls, [])

    def test_forged_build_identity_refused_before_canary(self):
        build = self.build()
        before = len(self.docker.calls)
        with self.assertRaises(ReleaseContractError):
            verify_candidate_image(self.candidate, self.compilation, self.suite,
                                   replace(build, candidate_image_digest="sha256:" + "b" * 64), executor=self.docker)
        self.assertEqual(len(self.docker.calls), before)

    def test_modified_private_context_refused(self):
        build = self.build()
        (self.root / build.context_root / "PACKAGE/SKILLS/ca/SKILL.md").write_text("tampered")
        with self.assertRaises(ReleaseContractError):
            verify_candidate_image(self.candidate, self.compilation, self.suite, build, executor=self.docker)

    def test_failed_canary_never_passes(self):
        build = self.build()
        self.docker.fail = "run"
        result = verify_candidate_image(self.candidate, self.compilation, self.suite, build, executor=self.docker)
        self.assertEqual(result.outcome, "failed")

    def test_partial_or_mismatched_canary_output_never_passes(self):
        build = self.build()
        for forged in ({"verified_files": 1}, {"mcp_tools": []},
                       {"candidate_snapshot_manifest_sha256": "b" * 64}):
            with self.subTest(forged=forged):
                self.docker.forge = forged
                result = verify_candidate_image(self.candidate, self.compilation, self.suite, build, executor=self.docker)
                self.assertEqual(result.outcome, "incomplete")

    def test_changed_n_during_build_returns_stale(self):
        self.docker.after = lambda operation: (self.root / ".caprmedio_runtime/framework/current.toml").write_text('release = "other"\n') if operation == "build" else None
        self.assertEqual(self.build().outcome, "stale")

    def test_timeout_retains_uncertain_build_without_replay(self):
        self.docker.timeout = "build"
        result = self.build()
        self.assertEqual(result.outcome, "effect_uncertain")
        self.assertEqual(len(self.docker.calls), 1)
        self.assertTrue((self.root / result.context_root).is_dir())

    def test_changed_public_skill_during_build_returns_stale(self):
        def change(operation):
            if operation == "build":
                self.fixture.fixture.write(".agents/skills/ca/SKILL.md", b"changed public Skill")
        self.docker.after = change
        self.assertEqual(self.build().outcome, "stale")

    def test_recording_failure_retains_effect_identity_without_success_or_replay(self):
        import release_image
        real_write = release_image._write
        def fail_receipt(path, payload, mode=0o644):
            if path.name == "receipt.json":
                raise OSError("deliberate recording failure")
            return real_write(path, payload, mode)
        with patch.object(release_image, "_write", side_effect=fail_receipt):
            result = self.build()
        self.assertEqual(result.outcome, "recording_uncertain")
        self.assertEqual(result.candidate_image_digest, IMAGE_ID)
        self.assertIsNone(result.receipt_sha256)
        self.assertEqual(sum(call[1] == "build" for call in self.docker.calls), 1)
        self.assertTrue((self.root / result.context_root).is_dir())

    def test_retirement_without_observed_promotion_cannot_run_docker(self):
        with self.assertRaises(ReleaseContractError) as caught:
            retire_prior_image(self.candidate, prior_image_digest=IMAGE_ID, executor=self.docker)
        self.assertEqual(caught.exception.code, "release-image-promotion-producer-missing")
        self.assertEqual(self.docker.calls, [])


if __name__ == "__main__":
    unittest.main()
