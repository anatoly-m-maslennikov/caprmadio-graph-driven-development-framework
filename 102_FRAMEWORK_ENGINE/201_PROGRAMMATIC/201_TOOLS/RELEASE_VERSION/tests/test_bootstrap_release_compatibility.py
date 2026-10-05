"""The first-install N is accepted only by the exact promotion prior reader."""

from __future__ import annotations

import json
import hashlib
import os
import shutil
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from framework_initialization import (  # noqa: E402
    PACKAGE_IMAGE_LABEL,
    SOURCE_CONTEXT_IMAGE_LABEL,
    initialize_framework_runtime,
    plan_initial_framework_installation,
)
from release_image import DockerCommandResult  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_promotion import _prove_prior_skill  # noqa: E402
from release_suite import _active_n_state, _bootstrap_source_context_is_valid  # noqa: E402
from release_suite_execution import _inspect_bound_n_image, _selector_binding  # noqa: E402


IMAGE_ID = "sha256:" + "a" * 64


class _Journal:
    def begin_action(self, **_kwargs):
        return {"run_id": "bootstrap-run", "disposition": "started"}

    def record_effects(self, *_args, **_kwargs):
        return None

    def finish_action(self, run_id, *, outcome, result_ref, effect_refs, report_ref=None):
        return {"run_id": run_id, "outcome": outcome, "disposition": "terminal"}


class _ImageFixture:
    def __init__(self, manifest_sha256: str, source_context_sha256: str) -> None:
        self.labels = {
            PACKAGE_IMAGE_LABEL: manifest_sha256,
            SOURCE_CONTEXT_IMAGE_LABEL: source_context_sha256,
        }

    def run(self, _argv, *, cwd, timeout_seconds):
        del cwd, timeout_seconds
        return DockerCommandResult(0, json.dumps([{"Id": IMAGE_ID, "Config": {
            "Labels": self.labels, "Env": ["PATH=/usr/bin:/bin"],
        }}]).encode(), b"")


class BootstrapReleaseCompatibilityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="bootstrap-n-")).resolve()
        for relative, payload in {
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py": b"tool\n",
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py": b"app\n",
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py": b"server\n",
            "102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md": b"prompt\n",
            "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md": b"# ca\n",
            "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml": b"name: ca\n",
            (".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
             "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/source.md"): b"source\n",
            (".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
             "04_requirement/compiled.md"): b"compiled\n",
        }.items():
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)

    def _initialize(self):
        plan = plan_initial_framework_installation(self.root)
        image = _ImageFixture(plan.manifest_sha256, plan.source_context_sha256)
        real_replace = os.replace

        def retained_fixture_replace(source, target):
            if Path(source).is_dir():
                shutil.copytree(source, target, dirs_exist_ok=True)
                return None
            return real_replace(source, target)

        with patch("framework_initialization.os.replace", side_effect=retained_fixture_replace):
            result = initialize_framework_runtime(
                self.root,
                journal=_Journal(),
                requested_run_id="bootstrap-action",
                image_digest=IMAGE_ID,
                image_executor=image,
            )
        self.assertEqual(result["state"], "installed")
        return plan, result

    def _selector_bytes(self, values: dict) -> bytes:
        return "".join(f'{key} = {json.dumps(value)}\n' for key, value in values.items()).encode("utf-8")

    def _assert_rejected_source_context(self, plan, selector: bytes, replacement: str) -> None:
        original = self.root / ".caprmedio_runtime/framework/releases" / plan.release / "manifest.toml"
        changed = original.read_text(encoding="utf-8").replace(
            f'candidate_snapshot_manifest_sha256 = "{plan.source_context_sha256}"',
            f"candidate_snapshot_manifest_sha256 = {replacement}",
        ).encode("utf-8")
        release = hashlib.sha256(changed).hexdigest()
        retained = original.parent.parent / release
        shutil.copytree(original.parent, retained)
        (retained / "manifest.toml").write_bytes(changed)
        values = tomllib.loads(selector.decode("utf-8"))
        root = f".caprmedio_runtime/framework/releases/{release}"
        values.update({
            "manifest_sha256": release,
            "release": release,
            "selected_release_root": root,
            "framework_engine_root": root + "/FRAMEWORK_ENGINE",
            "methodology_root": root + "/METHODOLOGY",
        })
        candidate = SimpleNamespace(authority=SimpleNamespace(executing_release=release))
        with self.assertRaises(ReleaseContractError) as raised:
            _prove_prior_skill(self.root, candidate, self._selector_bytes(values), self.root / ".agents/skills/ca")
        self.assertEqual(raised.exception.code, "release-promotion-skill-ownership-unknown")

    def test_actual_bootstrap_n_is_proven_for_the_next_promotion(self) -> None:
        plan, installed = self._initialize()
        selector = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        candidate = SimpleNamespace(authority=SimpleNamespace(executing_release=plan.release))

        records = _prove_prior_skill(self.root, candidate, selector, self.root / ".agents/skills/ca")

        self.assertNotEqual(plan.source_context_sha256, plan.release)
        self.assertEqual(installed["release"], plan.release)
        self.assertTrue(any(row["path"] == "SKILL.md" for row in records))

        forged = tomllib.loads(selector.decode("utf-8"))
        forged["manifest_sha256"] = "0" * 64
        forged_bytes = self._selector_bytes(forged)
        with self.assertRaises(ReleaseContractError) as raised:
            _prove_prior_skill(self.root, candidate, forged_bytes, self.root / ".agents/skills/ca")
        self.assertEqual(raised.exception.code, "release-promotion-skill-ownership-unknown")

        for mutation in (
            {"framework_engine_root": ".caprmedio_runtime/framework/releases/wrong/FRAMEWORK_ENGINE"},
            {"methodology_root": ".caprmedio_runtime/framework/releases/wrong/METHODOLOGY"},
            {"image_digest": "not-an-immutable-image-digest"},
            {"schema_version": True},
            {"unexpected": "extra"},
        ):
            forged = tomllib.loads(selector.decode("utf-8"))
            forged.update(mutation)
            with self.assertRaises(ReleaseContractError) as raised:
                _prove_prior_skill(self.root, candidate, self._selector_bytes(forged), self.root / ".agents/skills/ca")
            self.assertEqual(raised.exception.code, "release-promotion-skill-ownership-unknown")

        for replacement in ("0", "false", '"' + "A" * 64 + '"'):
            self._assert_rejected_source_context(plan, selector, replacement)
        self.assertFalse(_bootstrap_source_context_is_valid(None))

    def test_actual_bootstrap_n_binds_its_exact_framework_image_labels(self) -> None:
        plan, _installed = self._initialize()
        candidate = SimpleNamespace(authority=SimpleNamespace(executing_release=plan.release))
        image = _ImageFixture(plan.manifest_sha256, plan.source_context_sha256)

        _active_n_state(self.root, candidate)
        selected = _selector_binding(self.root, candidate)
        verified = _inspect_bound_n_image(image, self.root, selected)

        self.assertTrue(verified.bootstrap)
        self.assertEqual(verified.executing_release, plan.release)
        self.assertEqual(verified.source_context_sha256, plan.source_context_sha256)
        self.assertEqual(verified.image_path, "/usr/bin:/bin")


if __name__ == "__main__":
    unittest.main()
