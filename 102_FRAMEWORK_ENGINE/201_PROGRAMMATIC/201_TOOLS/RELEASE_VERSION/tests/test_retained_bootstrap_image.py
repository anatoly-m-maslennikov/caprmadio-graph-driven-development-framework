"""Retained producer fixtures; mocked subprocess markers are never live proof."""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
for directory in (RELEASE_ROOT, Path(__file__).resolve().parent):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import test_bootstrap_image as initial_fixture  # noqa: E402
import bootstrap_image  # noqa: E402
from bootstrap_image import (  # noqa: E402
    BootstrapImageError,
    produce_initial_framework_image,
    produce_retained_framework_image,
    read_retained_initial_framework_image,
)
from release_image import DockerSubprocessExecutor  # noqa: E402
from release_contract import canonical_json  # noqa: E402
from release_inventory import _is_ephemeral_directory, _is_ephemeral_file  # noqa: E402


OLD_IMAGE = initial_fixture.IMAGE_ID
NEW_IMAGE = "sha256:" + "b" * 64


class RetainedBootstrapImageTests(unittest.TestCase):
    def setUp(self) -> None:
        fixture = initial_fixture.BootstrapImageTests(
            "test_produces_one_immutable_image_with_exact_two_plan_labels_and_canary"
        )
        fixture.setUp()
        self.root, self.plan = fixture.root, fixture.plan
        self.executor = DockerSubprocessExecutor()
        old_docker = initial_fixture.GoldenDocker()
        # This exercises production receipt parsing with recorded subprocess
        # responses. No Docker socket, daemon, container or image is accessed.
        legacy_argv = bootstrap_image._canary_argv(OLD_IMAGE)[:-2] + ("/opt/caprmedio-bootstrap-canary.py",)
        with (patch.object(DockerSubprocessExecutor, "run", side_effect=old_docker.run),
              patch.object(bootstrap_image, "_canary_argv", return_value=legacy_argv)):
            self.original = produce_initial_framework_image(self.plan, executor=self.executor)
        self.assertEqual("verified", self.original.outcome)
        package = self.root / ".caprmedio_runtime/framework/releases" / self.plan.release
        package.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(self.root / self.original.context_root / "PACKAGE", package, copy_function=shutil.copy2)
        self.assertEqual(self.original, read_retained_initial_framework_image(self.root, self.plan.release, OLD_IMAGE))
        self.docker = initial_fixture.GoldenDocker()
        self.docker.image_id = NEW_IMAGE
        self.docker.inspect_id = NEW_IMAGE
        self.docker.canary = {"image_digest": NEW_IMAGE}

    def produce(self):
        with patch.object(DockerSubprocessExecutor, "run", side_effect=self.docker.run):
            return produce_retained_framework_image(
                self.root, self.plan.release, OLD_IMAGE, executor=self.executor,
            )

    def test_exact_legacy_probe_and_commands_reopen_without_context_changes(self):
        proof = self.root / self.original.proof_root
        before = self.persistent_proof_snapshot(proof)
        records = json.loads((proof / "commands.json").read_bytes())
        self.assertEqual("/opt/caprmedio-bootstrap-canary.py", records[-1]["argv"][-1])
        self.assertEqual(bootstrap_image._canary(), (proof / "context/bootstrap-canary.py").read_bytes())
        self.assertEqual(self.original, read_retained_initial_framework_image(self.root, self.plan.release, OLD_IMAGE))
        self.assertEqual(before, self.persistent_proof_snapshot(proof))

    def test_historical_known_programs_reopen_after_current_probe_helpers_change(self):
        result = self.produce()
        self.assertEqual("verified", result.outcome)
        with (patch.object(bootstrap_image, "_canary", return_value=b"changed current legacy helper\n"),
              patch.object(bootstrap_image, "_metadata_canary", return_value=b"changed current metadata helper\n")):
            self.assertEqual(self.original, read_retained_initial_framework_image(self.root, self.plan.release, OLD_IMAGE))
            self.assertEqual(result, read_retained_initial_framework_image(self.root, self.plan.release, NEW_IMAGE))

    @staticmethod
    def persistent_proof_snapshot(proof):
        snapshot = {".": (None, proof.stat().st_mode & 0o777)}
        for path in proof.rglob("*"):
            relative = path.relative_to(proof)
            if any(_is_ephemeral_directory(part) for part in relative.parts):
                continue
            if path.is_dir():
                snapshot[relative.as_posix()] = (None, path.stat().st_mode & 0o777)
            elif path.is_file() and not _is_ephemeral_file(path.name):
                snapshot[relative.as_posix()] = (path.read_bytes(), path.stat().st_mode & 0o777)
        return snapshot

    def test_different_id_filters_metadata_preserves_modes_and_ignores_live_source_changes(self):
        original_context = self.root / self.original.context_root
        metadata = original_context / "PACKAGE/.DS_Store"
        metadata.write_bytes(b"retained finder metadata")
        bytecode = original_context / "__pycache__/fixture.pyc"
        bytecode.parent.mkdir()
        bytecode.write_bytes(b"retained ephemeral bytecode")
        frozen = {path.relative_to(original_context).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
                  for path in original_context.rglob("*") if path.is_file()}
        (self.root / "pyproject.toml").write_bytes(b"current host dependency drift")
        engine_row = next(row for row in self.plan.rows if row.resource == "FRAMEWORK_ENGINE")
        (self.root / engine_row.source_path).write_bytes(b"current host Engine drift")
        original_proof = self.root / self.original.proof_root
        proof_before = self.persistent_proof_snapshot(original_proof)

        result = self.produce()

        self.assertEqual("verified", result.outcome)
        self.assertEqual(NEW_IMAGE, result.image_digest)
        self.assertEqual(bootstrap_image._canary_argv(NEW_IMAGE), self.docker.calls[-1])
        self.assertEqual(self.original.context_sha256, result.context_sha256)
        copied = self.root / result.context_root
        self.assertEqual(bootstrap_image._canary(), (copied / "bootstrap-canary.py").read_bytes())
        self.assertFalse((copied / "PACKAGE/.DS_Store").exists())
        self.assertFalse((copied / "__pycache__/fixture.pyc").exists())
        self.assertEqual(frozen, {path.relative_to(original_context).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
                                  for path in original_context.rglob("*") if path.is_file()})
        for relative, (payload, mode) in frozen.items():
            if relative.endswith((".DS_Store", ".pyc")):
                continue
            self.assertEqual((payload, mode), ((copied / relative).read_bytes(), (copied / relative).stat().st_mode & 0o777))
        self.assertEqual(result, read_retained_initial_framework_image(self.root, self.plan.release, NEW_IMAGE))
        self.assertEqual(proof_before, self.persistent_proof_snapshot(original_proof))
        self.assertEqual(self.original, read_retained_initial_framework_image(self.root, self.plan.release, OLD_IMAGE))

    def test_same_id_keeps_historical_proof_and_returns_fresh_attempt_receipt(self):
        proof = self.root / self.original.proof_root
        before = {path.relative_to(proof).as_posix(): path.read_bytes() for path in proof.rglob("*") if path.is_file()}
        self.docker.image_id = self.docker.inspect_id = OLD_IMAGE
        self.docker.canary = {"image_digest": OLD_IMAGE}

        result = self.produce()

        self.assertEqual("verified", result.outcome)
        self.assertEqual(OLD_IMAGE, result.image_digest)
        self.assertEqual(self.original.bootstrap_proof_key, result.bootstrap_proof_key)
        self.assertEqual(self.original.proof_root, result.proof_root)
        self.assertEqual(self.original.context_root, result.context_root)
        self.assertNotEqual(self.original.evidence_root, result.evidence_root)
        self.assertEqual(before, {path.relative_to(proof).as_posix(): path.read_bytes() for path in proof.rglob("*") if path.is_file()})
        receipt = self.root / result.evidence_root / "evidence.toml"
        self.assertEqual(hashlib.sha256(receipt.read_bytes()).hexdigest(), result.receipt_sha256)
        records = json.loads((receipt.parent / "commands.json").read_bytes())
        self.assertEqual(["build", "inspect", "canary"], [record["phase"] for record in records])
        self.assertEqual(self.original, read_retained_initial_framework_image(self.root, self.plan.release, OLD_IMAGE))

    def test_test_double_is_never_relabelled_as_actual_production_attempt(self):
        for image in (OLD_IMAGE, NEW_IMAGE):
            with self.subTest(image=image):
                self.docker.image_id = self.docker.inspect_id = image
                self.docker.canary = {"image_digest": image}
                result = produce_retained_framework_image(self.root, self.plan.release, OLD_IMAGE, executor=self.docker)
                self.assertEqual("test-double", result.execution_kind)
                if image == NEW_IMAGE:
                    with self.assertRaises(BootstrapImageError):
                        read_retained_initial_framework_image(self.root, self.plan.release, NEW_IMAGE)

    def test_tampered_original_proof_refuses_before_any_docker_command(self):
        original_context = self.root / self.original.context_root
        (original_context / "pyproject.toml").write_bytes(b"tampered retained dependency")
        with self.assertRaises(BootstrapImageError):
            self.produce()
        self.assertEqual([], self.docker.calls)

    def test_ephemeral_symlink_is_refused_before_any_docker_command(self):
        (self.root / self.original.context_root / ".DS_Store").symlink_to(self.root / "pyproject.toml")
        with self.assertRaises(BootstrapImageError):
            self.produce()
        self.assertEqual([], self.docker.calls)

    def test_build_timeout_retains_one_uncertain_attempt_without_inspect_or_canary(self):
        self.docker.timeout = "build"
        result = self.produce()
        self.assertEqual("effect_uncertain", result.outcome)
        self.assertEqual(1, len(self.docker.calls))
        self.assertIsNone(result.image_digest)
        self.assertFalse(result.bootstrap_proof_key)

    def test_failed_canary_never_publishes_a_canonical_replacement_proof(self):
        self.docker.fail = "canary"
        result = self.produce()
        self.assertEqual("failed", result.outcome)
        self.assertFalse(result.bootstrap_proof_key)
        self.assertEqual(NEW_IMAGE, result.image_digest)

    def test_retained_package_drift_after_build_starts_retains_attempt_without_canonical_proof(self):
        row = next(row for row in self.plan.rows if row.resource == "FRAMEWORK_ENGINE")
        package_file = self.root / ".caprmedio_runtime/framework/releases" / self.plan.release / row.destination_path
        original_run = self.docker.run

        def mutate_after_build(argv, **kwargs):
            response = original_run(argv, **kwargs)
            if tuple(argv[:2]) == ("docker", "build"):
                package_file.write_bytes(package_file.read_bytes() + b"\nretained package drift\n")
            return response

        with patch.object(DockerSubprocessExecutor, "run", side_effect=mutate_after_build):
            result = produce_retained_framework_image(
                self.root, self.plan.release, OLD_IMAGE, executor=self.executor,
            )

        self.assertNotEqual("verified", result.outcome)
        self.assertFalse(result.bootstrap_proof_key)
        new_key = hashlib.sha256(canonical_json([self.plan.release, NEW_IMAGE])).hexdigest()
        self.assertFalse((self.root / ".caprmedio_runtime/framework/bootstrap-image-evidence" / new_key).exists())
        with self.assertRaises(BootstrapImageError):
            read_retained_initial_framework_image(self.root, self.plan.release, NEW_IMAGE)
        attempt = self.root / result.evidence_root
        receipt = (attempt / "evidence.toml").read_bytes()
        self.assertEqual(hashlib.sha256(receipt).hexdigest(), result.receipt_sha256)
        commands = (attempt / "commands.json").read_bytes()
        self.assertEqual(hashlib.sha256(commands).hexdigest(), result.commands_sha256)
        records = json.loads(commands)
        self.assertEqual(["build", "inspect", "canary"], [record["phase"] for record in records])
        for record in records:
            for stream in ("stdout", "stderr"):
                payload = (attempt / record[stream + "_path"]).read_bytes()
                self.assertEqual(hashlib.sha256(payload).hexdigest(), record[stream + "_sha256"])


if __name__ == "__main__":
    unittest.main()
