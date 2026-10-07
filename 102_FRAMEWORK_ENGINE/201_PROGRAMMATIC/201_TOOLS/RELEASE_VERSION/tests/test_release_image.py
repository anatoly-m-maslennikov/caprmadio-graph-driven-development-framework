"""Fake Docker command goldens; these are never actual image/Release proof."""

from __future__ import annotations

import json
import hashlib
import sys
import unittest
import threading
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, replace
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
    read_image_execution_artifacts, DockerSubprocessExecutor,
)
from release_contract import canonical_json
from release_handoff import FRAMEWORK_SETTINGS_RELATIVE, PackageRow
from release_packaging import _render_manifest
import test_release_suite as suite_test

IMAGE_ID = "sha256:" + "a" * 64
PRIOR_IMAGE_ID = "sha256:" + "c" * 64
CONTAINER_ID = "d" * 64


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


class FakeRetirementDocker:
    """Read-only Docker-format fixtures; no image or container is touched."""

    def __init__(self, containers=()):
        self.calls = []
        self.containers = list(containers)
        self.fail = None
        self.forge_image = None
        self.after = None
        self.removed = False
        self.timeout = None

    def run(self, argv, *, cwd, timeout_seconds):
        self.calls.append(tuple(argv))
        if argv[:3] == ("docker", "image", "inspect"):
            operation = "absence" if self.removed else "image"
            if self.removed:
                output = b"[]\n"
            else:
                output = json.dumps([{"Id": self.forge_image or argv[3]}]).encode()
        elif argv[:3] == ("docker", "image", "rm"):
            operation = "remove"
            if self.fail != operation:
                self.removed = True
            output = ("Deleted: " + argv[3] + "\n").encode()
        elif argv[:3] == ("docker", "image", "ls"):
            operation = "images"
            output = (IMAGE_ID + "\n" + ("" if self.removed else PRIOR_IMAGE_ID + "\n")).encode()
        elif argv[:3] == ("docker", "container", "ls"):
            operation = "list"
            output = "".join(item["Id"] + "\n" for item in self.containers).encode()
        elif argv[:3] == ("docker", "container", "inspect"):
            operation = "containers"
            output = json.dumps(self.containers).encode()
        else:
            raise AssertionError("unexpected effect: " + str(argv))
        if self.after:
            self.after(operation)
        exit_code = 1 if operation == "absence" else 0
        stderr = ("Error response from daemon: No such image: " + argv[3] + "\n").encode() if operation == "absence" else b"fixture output\n"
        if self.fail == operation:
            exit_code, stderr = 17, b"permission denied\n"
        return DockerCommandResult(exit_code, output, stderr, self.timeout == operation)


class ReleaseImageTests(unittest.TestCase):
    def setUp(self):
        self.setup_candidate()

    def cleanup_candidate(self):
        fixture = getattr(self, "fixture", None)
        if fixture is not None:
            fixture.doCleanups()
            self.fixture = None

    def setup_candidate(self, settings=None):
        self.cleanup_candidate()
        self.fixture = suite_test.ReleaseSuiteTests("run")
        self.fixture.setUp()
        self.addCleanup(self.cleanup_candidate)
        self.root = self.fixture.root
        self.fixture.fixture.write("pyproject.toml", b"[project]\nname = 'fixture'\nversion = '0.0.0'\n")
        self.fixture.fixture.write("uv.lock", b"version = 1\n")
        self.fixture.fixture.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile",
                                   b"FROM scratch\nCOPY pyproject.toml uv.lock ./\nCOPY 102_FRAMEWORK_ENGINE ./102_FRAMEWORK_ENGINE\n")
        if settings is not None:
            self.fixture.fixture.write(FRAMEWORK_SETTINGS_RELATIVE, settings)
        self.candidate, self.compilation = self.fixture.bound()
        # The retained N Skill deliberately differs from the candidate, so
        # selector-first publication tests exercise the separate Skill effect.
        prior = self.root / ".caprmedio_runtime/framework/releases/N"
        prior_skill = b"# Exact retained fixture N Skill\n"
        (prior / "SKILLS/ca/SKILL.md").write_bytes(prior_skill)
        (self.root / ".agents/skills/ca/SKILL.md").write_bytes(prior_skill)
        prior_rows = [PackageRow.model_validate({**row.model_dump(mode="json"),
                      "sha256": hashlib.sha256(prior_skill).hexdigest()})
                      if row.destination_path == "SKILLS/ca/SKILL.md" else row
                      for row in self.compilation.package_rows]
        (prior / "manifest.toml").write_text(_render_manifest("N", prior_rows))
        self.suite = self.fixture.execute_suite(self.candidate, self.compilation)
        self.assertTrue(
            self.suite.passed,
            msg=("sealed fixture suite did not pass: "
                 f"outcome={self.suite.outcome!r}, reason={self.suite.reason!r}, "
                 f"exit_code={self.suite.exit_code!r}, executed_tests={self.suite.executed_tests!r}, "
                 f"evidence_root={self.suite.evidence_root!r}"),
        )
        self.docker = FakeDocker()

    def build(self):
        return build_candidate_image(self.candidate, self.compilation, self.suite, executor=self.docker)

    def recorded_command_fixtures(self):
        """Production-shaped receipts from mocked CLI outputs, never live proof."""
        with patch.object(DockerSubprocessExecutor, "run", side_effect=self.docker.run):
            executor = DockerSubprocessExecutor()
            build = build_candidate_image(self.candidate, self.compilation, self.suite, executor=executor)
            evidence = verify_candidate_image(self.candidate, self.compilation, self.suite, build, executor=executor)
        self.assertEqual(evidence.outcome, "verified")
        return build, evidence

    def reseal_receipt(self, evidence):
        """Deliberately rewrite all outer hashes to test semantic forgery checks."""
        import release_image
        receipt = canonical_json(asdict(replace(evidence, receipt_sha256=None)))
        (self.root / evidence.evidence_root / "receipt.json").write_bytes(receipt)
        return replace(evidence, receipt_sha256=release_image._digest(receipt))

    def rewrite_commands(self, evidence, transform):
        import release_image
        path = self.root / evidence.evidence_root / "commands.json"
        commands = json.loads(path.read_bytes())
        transform(commands)
        payload = canonical_json(commands)
        path.write_bytes(payload)
        return self.reseal_receipt(replace(evidence, commands_sha256=release_image._digest(payload)))

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
        self.assertIn(b"COPY --chown=${RUNTIME_UID}:${RUNTIME_GID} PACKAGE /opt/caprmedio-framework", (context / "Dockerfile").read_bytes())
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

    def retirement_inputs(self, prior_image=PRIOR_IMAGE_ID, settings=None):
        from release_promotion import promote_bound_release
        from test_release_promotion import recorded_gate_fixtures, recorded_host_patches
        if settings is not None:
            self.setup_candidate(settings)
        selector = self.root / ".caprmedio_runtime/framework/current.toml"
        selector.write_text('release = "N"\n' + (f'candidate_image_digest = "{prior_image}"\n' if prior_image else ""))
        self.suite = self.fixture.execute_suite(self.candidate, self.compilation)
        build, verification = self.recorded_command_fixtures()
        args = (self.candidate, self.compilation, self.suite, build, verification)
        with recorded_host_patches():
            self.retirement_gates = recorded_gate_fixtures(*args)
            promotion = promote_bound_release(*args, **self.retirement_gates)
        self.assertEqual(promotion.outcome, "promoted")
        return args + (promotion,)

    def retention_settings(self, condition="until_verified_promotion", images=()):
        return ('[release_version.rollback_retention]\ncondition = ' + json.dumps(condition)
                + '\nrequired_image_digests = ' + json.dumps(list(images)) + '\n').encode()

    def test_retirement_golden_exact_removal_and_absence_only_after_sealed_until_policy(self):
        args = self.retirement_inputs(settings=self.retention_settings())
        docker = FakeRetirementDocker()
        selector = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        prior = (self.root / args[-1].retained_prior_selector_ref).read_bytes()
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "retired")
        self.assertTrue(result.prior_image_absent)
        self.assertEqual(result.required_rollback_refs, ())
        self.assertEqual(result.retention_condition, "until_verified_promotion")
        self.assertEqual([call for call in docker.calls if call[:3] == ("docker", "image", "rm")],
                         [("docker", "image", "rm", PRIOR_IMAGE_ID)])
        self.assertNotIn("--force", [part for call in docker.calls for part in call])
        self.assertNotIn("prune", [part for call in docker.calls for part in call])
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector)
        self.assertEqual((self.root / args[-1].retained_prior_selector_ref).read_bytes(), prior)
        self.assertTrue((self.root / result.removal_intent_ref).is_file())

    def test_retirement_retain_prior_and_explicit_required_image_reference_never_remove(self):
        for settings in (self.retention_settings("retain_prior"), self.retention_settings(images=(PRIOR_IMAGE_ID,))):
            with self.subTest(settings=settings):
                args = self.retirement_inputs(settings=settings)
                docker = FakeRetirementDocker()
                result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
                self.assertEqual(result.outcome, "retained")
                self.assertTrue(result.required_rollback_refs)
                self.assertFalse(docker.removed)

    def test_retirement_malformed_closed_policy_members_remain_pending(self):
        for settings in (self.retention_settings("unknown"), self.retention_settings(images=("mutable:tag",)),
                         self.retention_settings(images=(PRIOR_IMAGE_ID, PRIOR_IMAGE_ID)),
                         self.retention_settings() + b'caller_success = true\n',
                         b'[release_version.rollback_retention]\ncondition = "until_verified_promotion"\n',
                         b'[release_version.rollback_retention]\ncondition = "until_verified_promotion"\nrequired_image_digests = "none"\n'):
            with self.subTest(settings=settings):
                args = self.retirement_inputs(settings=settings)
                docker = FakeRetirementDocker()
                result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
                self.assertEqual(result.outcome, "pending")
                self.assertIsNone(result.required_rollback_refs)
                self.assertFalse(docker.removed)

    def test_retirement_required_other_image_does_not_make_saved_selector_required(self):
        args = self.retirement_inputs(settings=self.retention_settings(images=(IMAGE_ID,)))
        docker = FakeRetirementDocker()
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "retired")
        self.assertIn(args[-1].retained_prior_selector_ref, result.observed_rollback_refs)
        self.assertEqual(result.required_rollback_refs, ())

    def test_retirement_used_container_under_until_policy_never_removes(self):
        args = self.retirement_inputs(settings=self.retention_settings())
        docker = FakeRetirementDocker(({"Id": CONTAINER_ID, "Image": PRIOR_IMAGE_ID, "State": {"Status": "exited"}},))
        self.assertEqual(retire_prior_image(*args, executor=docker, **self.retirement_gates).outcome, "retained")
        self.assertFalse(docker.removed)

    def test_retirement_remove_failure_is_truthful_and_cannot_implicitly_retry(self):
        args = self.retirement_inputs(settings=self.retention_settings())
        docker = FakeRetirementDocker()
        docker.fail = "remove"
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "failed")
        docker.fail = None
        again = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(again.outcome, "pending")
        self.assertEqual(sum(call[:3] == ("docker", "image", "rm") for call in docker.calls), 1)

    def test_retirement_timeout_uncertain_effect_is_not_replayed(self):
        args = self.retirement_inputs(settings=self.retention_settings())
        docker = FakeRetirementDocker()
        docker.timeout = "remove"
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "effect_uncertain")
        docker.removed = False
        docker.timeout = None
        self.assertEqual(retire_prior_image(*args, executor=docker, **self.retirement_gates).outcome, "pending")
        self.assertEqual(sum(call[:3] == ("docker", "image", "rm") for call in docker.calls), 1)

    def test_retirement_absence_permission_failure_is_not_retired(self):
        args = self.retirement_inputs(settings=self.retention_settings())
        docker = FakeRetirementDocker()
        docker.fail = "absence"
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "effect_uncertain")
        self.assertIsNone(result.prior_image_absent)

    def test_retirement_image_still_exists_after_successful_rm_is_uncertain(self):
        args = self.retirement_inputs(settings=self.retention_settings())
        docker = FakeRetirementDocker()
        docker.after = lambda operation: setattr(docker, "removed", False) if operation == "remove" else None
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "effect_uncertain")
        self.assertFalse(result.prior_image_absent)

    def test_retirement_selector_race_before_rm_prevents_removal(self):
        args = self.retirement_inputs(settings=self.retention_settings())
        docker = FakeRetirementDocker()
        docker.after = lambda operation: (self.root / ".caprmedio_runtime/framework/current.toml").write_text('release = "other"\n') if operation == "list" else None
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "stale")
        self.assertFalse(docker.removed)

    def test_retirement_stale_settings_before_or_during_observation_remain_pending(self):
        for during in (False, True):
            with self.subTest(during=during):
                args = self.retirement_inputs(settings=self.retention_settings())
                docker = FakeRetirementDocker()
                def change(operation):
                    if operation == "list":
                        (self.root / FRAMEWORK_SETTINGS_RELATIVE).write_bytes(self.retention_settings("retain_prior"))
                if during:
                    docker.after = change
                else:
                    change("list")
                result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
                self.assertEqual(result.outcome, "pending")
                self.assertIsNone(result.required_rollback_refs)
                self.assertFalse(docker.removed)

    def test_retirement_never_removes_selected_candidate_even_when_prior_identity_matches(self):
        args = self.retirement_inputs(prior_image=IMAGE_ID, settings=self.retention_settings())
        docker = FakeRetirementDocker()
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "pending")
        self.assertEqual(docker.calls, [])

    def test_retirement_recording_failure_after_removal_retains_intent_and_blocks_replay(self):
        import release_image
        args = self.retirement_inputs(settings=self.retention_settings())
        docker = FakeRetirementDocker()
        real_write = release_image._write
        def fail_receipt(path, payload, mode=0o644):
            if path.name == "receipt.json":
                raise OSError("deliberate post-removal receipt failure")
            return real_write(path, payload, mode)
        with patch.object(release_image, "_write", side_effect=fail_receipt):
            result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "recording_uncertain")
        self.assertTrue(result.prior_image_absent)
        self.assertTrue((self.root / result.removal_intent_ref).is_file())
        docker.removed = False
        self.assertEqual(retire_prior_image(*args, executor=docker, **self.retirement_gates).outcome, "pending")
        self.assertEqual(sum(call[:3] == ("docker", "image", "rm") for call in docker.calls), 1)

    def test_retirement_concurrent_admission_has_only_one_exact_removal_effect(self):
        args = self.retirement_inputs(settings=self.retention_settings())
        docker = FakeRetirementDocker()
        rendezvous = threading.Barrier(2)
        docker.after = lambda operation: rendezvous.wait(timeout=10) if operation == "list" else None
        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(retire_prior_image, *args, executor=docker, **self.retirement_gates) for _ in range(2)]
            results = [future.result(timeout=20) for future in futures]
        self.assertEqual(sorted(result.outcome for result in results), ["pending", "retired"])
        self.assertEqual(sum(call[:3] == ("docker", "image", "rm") for call in docker.calls), 1)

    def test_retirement_golden_observes_exact_image_all_containers_and_retained_rollback_selector(self):
        args = self.retirement_inputs()
        docker = FakeRetirementDocker()
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "retained")
        self.assertEqual(result.prior_image_digest, PRIOR_IMAGE_ID)
        self.assertEqual(result.retaining_container_refs, ())
        self.assertIn(args[-1].retained_prior_selector_ref, result.observed_rollback_refs)
        self.assertEqual(result.retention_condition, "retain_prior")
        self.assertEqual(
            result.required_rollback_refs,
            (f"{FRAMEWORK_SETTINGS_RELATIVE}#release_version.rollback_retention.condition",),
        )
        self.assertEqual(docker.calls, [("docker", "image", "inspect", PRIOR_IMAGE_ID),
                                       ("docker", "container", "ls", "--all", "--quiet", "--no-trunc")])
        self.assertEqual(result.execution_kind, "test-double")
        self.assertIsNotNone(result.receipt_sha256)

    def test_retirement_retains_running_and_stopped_exact_image_containers(self):
        args = self.retirement_inputs()
        for state in ("running", "exited"):
            with self.subTest(state=state):
                docker = FakeRetirementDocker(({"Id": CONTAINER_ID, "Image": PRIOR_IMAGE_ID, "State": {"Status": state}},))
                result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
                self.assertEqual(result.outcome, "retained")
                self.assertEqual(result.retaining_container_refs, (CONTAINER_ID,))
                self.assertNotIn("rm", [word for command in docker.calls for word in command])

    def test_retirement_unknown_prior_identity_never_invokes_docker(self):
        args = self.retirement_inputs(None)
        docker = FakeRetirementDocker()
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "pending")
        self.assertIsNone(result.prior_image_digest)
        self.assertIsNone(result.retaining_container_refs)
        self.assertIsNone(result.observed_rollback_refs)
        self.assertEqual(docker.calls, [])

    def test_retirement_forged_or_pending_promotion_refused_before_docker(self):
        args = self.retirement_inputs()
        docker = FakeRetirementDocker()
        for forged in (replace(args[-1], receipt_sha256="b" * 64), replace(args[-1], outcome="pending"),
                       replace(args[-1], prior_image_digest=IMAGE_ID)):
            with self.subTest(forged=forged):
                with self.assertRaises(ReleaseContractError):
                    retire_prior_image(*args[:-1], forged, executor=docker, **self.retirement_gates)
                self.assertEqual(docker.calls, [])

    def test_retirement_missing_forged_or_cross_candidate_gate_refuses_before_any_write(self):
        args = self.retirement_inputs(settings=self.retention_settings())
        cases = (
            ("full_gate", None),
            ("full_gate", replace(self.retirement_gates["full_gate"], reason="caller-forged")),
            ("full_gate", replace(self.retirement_gates["full_gate"], outcome="incomplete")),
            ("full_gate", replace(self.retirement_gates["full_gate"], candidate_snapshot_manifest_sha256="f" * 64)),
            ("e2e", None),
            ("e2e", replace(self.retirement_gates["e2e"], reason="caller-forged")),
            ("e2e", replace(self.retirement_gates["e2e"], candidate_snapshot_manifest_sha256="f" * 64)),
        )
        before = self.fixture.fixture.snapshot()
        for member, evidence in cases:
            with self.subTest(member=member, evidence=evidence):
                docker = FakeRetirementDocker()
                with self.assertRaises(ReleaseContractError):
                    retire_prior_image(*args, executor=docker, **{**self.retirement_gates, member: evidence})
                self.assertEqual(docker.calls, [])
                self.assertEqual(self.fixture.fixture.snapshot(), before)
        with self.assertRaises(TypeError):
            retire_prior_image(*args, executor=FakeRetirementDocker())
        self.assertEqual(self.fixture.fixture.snapshot(), before)

    def test_retirement_changed_full_gate_receipt_refuses_before_any_write(self):
        args = self.retirement_inputs(settings=self.retention_settings())
        receipt = self.root / self.retirement_gates["full_gate"].evidence_root / "receipt.json"
        receipt.write_bytes(receipt.read_bytes() + b" ")
        before = self.fixture.fixture.snapshot()
        docker = FakeRetirementDocker()
        with self.assertRaises(ReleaseContractError):
            retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(docker.calls, [])
        self.assertEqual(self.fixture.fixture.snapshot(), before)

    def test_retirement_missing_or_mismatched_image_is_pending_without_another_target(self):
        args = self.retirement_inputs()
        for failure in ("image", "mismatch"):
            with self.subTest(failure=failure):
                docker = FakeRetirementDocker()
                if failure == "image":
                    docker.fail = "image"
                else:
                    docker.forge_image = IMAGE_ID
                result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
                self.assertEqual(result.outcome, "pending")
                self.assertEqual(docker.calls, [("docker", "image", "inspect", PRIOR_IMAGE_ID)])

    def test_retirement_unknown_container_scan_is_pending_and_never_removes(self):
        args = self.retirement_inputs()
        docker = FakeRetirementDocker()
        docker.fail = "list"
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "pending")
        self.assertIsNone(result.retaining_container_refs)
        self.assertNotIn("rm", [word for command in docker.calls for word in command])

    def test_retirement_inspects_unrelated_containers_without_treating_tags_as_identity(self):
        args = self.retirement_inputs()
        docker = FakeRetirementDocker(({"Id": CONTAINER_ID, "Image": IMAGE_ID,
                                        "Config": {"Image": "prior:mutable-tag"}, "State": {"Status": "exited"}},))
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "retained")
        self.assertEqual(result.retaining_container_refs, ())
        self.assertIn(("docker", "container", "inspect", CONTAINER_ID), docker.calls)

    def test_retirement_partial_container_identity_is_pending(self):
        args = self.retirement_inputs()
        for record in ({"Id": "d" * 12, "Image": PRIOR_IMAGE_ID, "State": {"Status": "exited"}},
                       {"Id": CONTAINER_ID, "Image": "mutable:latest", "State": {"Status": "running"}}):
            with self.subTest(record=record):
                docker = FakeRetirementDocker((record,))
                result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
                self.assertEqual(result.outcome, "pending")
                self.assertNotIn("rm", [word for command in docker.calls for word in command])

    def test_retirement_observes_other_retained_prior_selector_references(self):
        args = self.retirement_inputs()
        extra = ".caprmedio_runtime/release_promotion/other-retained/prior-selector.toml"
        self.fixture.fixture.write(extra, f'image_digest = "{PRIOR_IMAGE_ID}"\n'.encode())
        result = retire_prior_image(*args, executor=FakeRetirementDocker(), **self.retirement_gates)
        self.assertEqual(result.outcome, "retained")
        self.assertEqual(set(result.observed_rollback_refs), {extra, args[-1].retained_prior_selector_ref})
        self.assertEqual(result.required_rollback_refs, (
            FRAMEWORK_SETTINGS_RELATIVE + "#release_version.rollback_retention.condition",
        ))

    def test_retirement_unknown_rollback_scope_is_pending_before_docker(self):
        args = self.retirement_inputs()
        self.fixture.fixture.write(".caprmedio_runtime/release_promotion/unknown/prior-selector.toml", b"unsupported TOML {\n")
        docker = FakeRetirementDocker()
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "pending")
        self.assertEqual(docker.calls, [])

    def test_retirement_missing_approved_retention_condition_never_becomes_removal(self):
        # Seal an absent policy into the fixture itself.  Observed historical
        # selectors are not policy authority and must not be used as a proxy.
        args = self.retirement_inputs(settings=b"")
        docker = FakeRetirementDocker()
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "pending")
        self.assertIn("approved rollback-retention condition", result.reason)
        self.assertNotIn("rm", [word for command in docker.calls for word in command])

    def test_retirement_changed_selection_during_observation_is_stale(self):
        args = self.retirement_inputs()
        docker = FakeRetirementDocker()
        docker.after = lambda operation: (self.root / ".caprmedio_runtime/framework/current.toml").write_text('release = "other"\n') if operation == "list" else None
        result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "stale")
        self.assertNotIn("rm", [word for command in docker.calls for word in command])

    def test_retirement_receipt_failure_retains_without_replaying_effects(self):
        import release_image
        args = self.retirement_inputs()
        docker = FakeRetirementDocker()
        real_write = release_image._write
        def fail_receipt(path, payload, mode=0o644):
            if path.name == "receipt.json":
                raise OSError("deliberate retirement recording failure")
            return real_write(path, payload, mode)
        with patch.object(release_image, "_write", side_effect=fail_receipt):
            result = retire_prior_image(*args, executor=docker, **self.retirement_gates)
        self.assertEqual(result.outcome, "recording_uncertain")
        self.assertIsNone(result.receipt_sha256)
        self.assertEqual(len(docker.calls), 2)

    def test_artifact_reader_before_and_after_selector_change_without_old_n_replay(self):
        build, evidence = self.recorded_command_fixtures()
        expected = self.root / evidence.evidence_root
        self.assertEqual(verify_bound_image_evidence(self.candidate, self.compilation, self.suite, build, evidence), expected)
        before = len(self.docker.calls)
        (self.root / ".caprmedio_runtime/framework/current.toml").write_text('release = "N+1"\n')
        self.assertEqual(read_image_execution_artifacts(self.candidate, self.compilation, self.suite, build, evidence), expected)
        with self.assertRaises(ReleaseContractError):
            verify_bound_image_evidence(self.candidate, self.compilation, self.suite, build, evidence)
        self.assertEqual(len(self.docker.calls), before)

    def test_artifact_reader_rejects_test_double_and_caller_evidence_flags(self):
        build = self.build()
        evidence = verify_candidate_image(self.candidate, self.compilation, self.suite, build, executor=self.docker)
        with self.assertRaises(ReleaseContractError):
            read_image_execution_artifacts(self.candidate, self.compilation, self.suite, build, evidence)
        with self.assertRaises(ReleaseContractError):
            read_image_execution_artifacts(self.candidate, self.compilation, self.suite, build, {"outcome": "verified"})

    def test_artifact_reader_rejects_tampered_suite_output_after_selection(self):
        build, evidence = self.recorded_command_fixtures()
        (self.root / ".caprmedio_runtime/framework/current.toml").write_text('release = "N+1"\n')
        (self.root / self.suite.evidence_root / "stdout.bin").write_bytes(b"tampered")
        with self.assertRaises(ReleaseContractError):
            read_image_execution_artifacts(self.candidate, self.compilation, self.suite, build, evidence)

    def test_artifact_reader_rejects_rehashed_wrong_build_command(self):
        build, evidence = self.recorded_command_fixtures()
        build = self.rewrite_commands(build, lambda commands: commands[0]["argv"].__setitem__(-1, "/unsealed-context"))
        evidence = self.reseal_receipt(replace(evidence, build_receipt_sha256=build.receipt_sha256))
        with self.assertRaises(ReleaseContractError):
            read_image_execution_artifacts(self.candidate, self.compilation, self.suite, build, evidence)

    def test_artifact_reader_rejects_rehashed_mutable_canary_image(self):
        build, evidence = self.recorded_command_fixtures()
        evidence = self.rewrite_commands(evidence, lambda commands: commands[1]["argv"].__setitem__(-2, "mutable:latest"))
        with self.assertRaises(ReleaseContractError):
            read_image_execution_artifacts(self.candidate, self.compilation, self.suite, build, evidence)

    def test_artifact_reader_rejects_rehashed_forged_canary_success(self):
        import release_image
        build, evidence = self.recorded_command_fixtures()
        path = self.root / evidence.evidence_root / "command-1.stdout"
        report = json.loads(path.read_bytes())
        report["verified_files"] = 1
        payload = canonical_json(report)
        path.write_bytes(payload)
        evidence = self.rewrite_commands(evidence, lambda commands: commands[1].__setitem__("stdout_sha256", release_image._digest(payload)))
        with self.assertRaises(ReleaseContractError):
            read_image_execution_artifacts(self.candidate, self.compilation, self.suite, build, evidence)

    def test_artifact_reader_rejects_rehashed_changed_fixed_canary(self):
        import release_image
        build, evidence = self.recorded_command_fixtures()
        context = self.root / build.context_root
        (context / "canary.py").write_text("print('caller-authored success')")
        build = self.reseal_receipt(replace(build, context_sha256=release_image._tree(context)))
        evidence = self.reseal_receipt(replace(evidence, build_receipt_sha256=build.receipt_sha256))
        with self.assertRaises(ReleaseContractError):
            read_image_execution_artifacts(self.candidate, self.compilation, self.suite, build, evidence)

    def test_artifact_reader_rejects_rehashed_unbound_suite_report(self):
        import release_image
        build, evidence = self.recorded_command_fixtures()
        report_path = self.root / self.suite.evidence_root / "coverage.xml"
        original = report_path.read_bytes()
        payload = original.replace(b'caprmedio.source_probe', b'caller.success')
        self.assertNotEqual(payload, original)
        report_path.write_bytes(payload)
        suite = self.reseal_receipt(replace(self.suite, report_sha256=release_image._digest(payload)))
        build = self.reseal_receipt(replace(build, suite_receipt_sha256=suite.receipt_sha256))
        evidence = self.reseal_receipt(replace(evidence, build_receipt_sha256=build.receipt_sha256))
        with self.assertRaises(ReleaseContractError):
            read_image_execution_artifacts(self.candidate, self.compilation, suite, build, evidence)

    def test_artifact_reader_rejects_forged_typed_authority_after_selection(self):
        build, evidence = self.recorded_command_fixtures()
        (self.root / ".caprmedio_runtime/framework/current.toml").write_text('release = "N+1"\n')
        authority = self.candidate.authority.model_copy(update={"executing_release": "other"})
        candidate = replace(self.candidate, authority=authority)
        compilation = self.compilation.model_copy(update={"authority": authority})
        with self.assertRaises(ReleaseContractError):
            read_image_execution_artifacts(candidate, compilation, self.suite, build, evidence)

    def test_artifact_reader_rejects_rehashed_wrong_build_inspection(self):
        import release_image
        build, evidence = self.recorded_command_fixtures()
        path = self.root / build.evidence_root / "command-1.stdout"
        payload = canonical_json([{"Id": "sha256:" + "b" * 64, "Config": {"Labels": self.docker.labels}}])
        path.write_bytes(payload)
        build = self.rewrite_commands(build, lambda commands: commands[1].__setitem__("stdout_sha256", release_image._digest(payload)))
        evidence = self.reseal_receipt(replace(evidence, build_receipt_sha256=build.receipt_sha256))
        with self.assertRaises(ReleaseContractError):
            read_image_execution_artifacts(self.candidate, self.compilation, self.suite, build, evidence)


if __name__ == "__main__":
    unittest.main()
