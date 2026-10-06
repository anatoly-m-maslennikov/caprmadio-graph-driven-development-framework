"""Closed-context parser tests using retained, canonical golden inputs only."""
from __future__ import annotations

import argparse
import inspect
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = RELEASE_ROOT.parents[3]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))
from release_e2e_context import (  # noqa: E402
    CANDIDATE_IMAGE_ENVIRONMENT_VARIABLE,
    CONTEXT_ENVIRONMENT_VARIABLE,
    ReleaseE2EContext,
    ReleaseE2EContextError,
    context_sha256,
    load_release_e2e_context,
)
from run_release_e2e import _bound_harness  # noqa: E402


IMAGE = "sha256:" + "a" * 64
MANIFEST = "b" * 64
GRAMMAR = "c" * 64
PHASE_MAP = "d" * 64
START_DIRECTORY = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests"
HARNESS_SOURCES = (
    f"{START_DIRECTORY}/test_docker_e2e.py",
    f"{START_DIRECTORY}/test_selected_workflows_docker_e2e.py",
    f"{START_DIRECTORY}/test_selected_query_mcp_e2e.py",
)


def canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


class ReleaseE2EContextContractTests(unittest.TestCase):
    """Each negative case changes one member of an otherwise sealed input."""

    def setUp(self) -> None:
        retained = REPOSITORY / ".caprmedio_tmp/tests/release-e2e-context"
        retained.mkdir(parents=True, exist_ok=True)
        # Retain inputs for failure diagnostics; cleanup is never part of this gate.
        self.root = Path(tempfile.mkdtemp(prefix="closed-context-", dir=retained)).resolve()
        self.source_root = self.root / "sealed-source"
        self.scratch_root = self.source_root / "scratch"
        self.report_root = self.scratch_root / "reports"
        self.report_root.mkdir(parents=True)
        for source in HARNESS_SOURCES:
            path = self.source_root / source
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# retained E2E harness fixture\n", encoding="utf-8")
        self._context_number = 0

    def golden(self) -> dict[str, object]:
        harnesses = []
        for source in HARNESS_SOURCES:
            pattern = Path(source).name
            optins = {"CAPRMEDIO_DOCKER_E2E": "1"}
            if pattern == "test_selected_query_mcp_e2e.py":
                optins = {
                    "CAPRMEDIO_DOCKER_QUERY_E2E": "1",
                    "CAPRMEDIO_DOCKER_QUERY_IMAGE": IMAGE,
                    "CAPRMEDIO_IMAGE": IMAGE,
                }
            harnesses.append({
                "source_path": source,
                "start_directory": START_DIRECTORY,
                "pattern": pattern,
                "junit_path": str(self.report_root / f"{pattern}.xml"),
                "context_optins": optins,
            })
        return {
            "schema_version": 1,
            "source_root": str(self.source_root),
            "scratch_root": str(self.scratch_root),
            "report_root": str(self.report_root),
            "candidate_snapshot_manifest_sha256": MANIFEST,
            "candidate_image_digest": IMAGE,
            "grammar_sha256": GRAMMAR,
            "phase_map_sha256": PHASE_MAP,
            "fixed_harnesses": harnesses,
            "phase_bindings": ["image-inspect", *(Path(source).name for source in HARNESS_SOURCES)],
        }

    def write_context(self, payload: object, *, canonical: bool = True) -> Path:
        self._context_number += 1
        path = self.scratch_root / f"context-{self._context_number}.json"
        data = canonical_json(payload) if canonical else json.dumps(payload, indent=2, sort_keys=True).encode()
        path.write_bytes(data)
        return path

    def environment(self, path: Path, *, image: str = IMAGE) -> dict[str, str]:
        return {CONTEXT_ENVIRONMENT_VARIABLE: str(path), CANDIDATE_IMAGE_ENVIRONMENT_VARIABLE: image}

    def load(self, payload: object, *, canonical: bool = True, image: str = IMAGE) -> ReleaseE2EContext:
        return load_release_e2e_context(self.environment(self.write_context(payload, canonical=canonical), image=image))

    def assert_refused(self, payload: object, message: str, *, canonical: bool = True, image: str = IMAGE) -> None:
        with self.assertRaisesRegex(ReleaseE2EContextError, message):
            self.load(payload, canonical=canonical, image=image)

    def test_loader_is_sole_environment_boundary_and_context_is_frozen(self) -> None:
        self.assertEqual(("environment",), tuple(inspect.signature(load_release_e2e_context).parameters))
        self.assertTrue(ReleaseE2EContext.__dataclass_params__.frozen)
        with self.assertRaises(ReleaseE2EContextError):
            load_release_e2e_context({})
        self.assertNotIn(CONTEXT_ENVIRONMENT_VARIABLE, os.environ)

    def test_good_canonical_context_preserves_all_fixed_bindings_and_optins(self) -> None:
        context = self.load(self.golden())
        self.assertEqual(str(self.source_root), context.source_root)
        self.assertEqual(("image-inspect", *(Path(source).name for source in HARNESS_SOURCES)), context.phase_bindings)
        self.assertEqual(HARNESS_SOURCES, tuple(harness.source_path for harness in context.harnesses))
        self.assertEqual((("CAPRMEDIO_DOCKER_E2E", "1"),), context.harnesses[0].context_optins)
        self.assertEqual((("CAPRMEDIO_DOCKER_E2E", "1"),), context.harnesses[1].context_optins)
        self.assertEqual(
            (("CAPRMEDIO_DOCKER_QUERY_E2E", "1"), ("CAPRMEDIO_DOCKER_QUERY_IMAGE", IMAGE), ("CAPRMEDIO_IMAGE", IMAGE)),
            context.harnesses[2].context_optins,
        )
        self.assertEqual(64, len(context_sha256(context)))

    def test_refuses_environment_image_that_differs_from_sealed_image(self) -> None:
        self.assert_refused(self.golden(), "environment differs", image="sha256:" + "e" * 64)

    def test_refuses_malformed_manifest_grammar_and_phase_hashes(self) -> None:
        for field in ("candidate_snapshot_manifest_sha256", "grammar_sha256", "phase_map_sha256"):
            with self.subTest(field=field):
                payload = self.golden()
                payload[field] = "A" * 64
                self.assert_refused(payload, "lowercase SHA-256")

    def test_refuses_phase_binding_reorder_and_duplicate(self) -> None:
        payload = self.golden()
        payload["phase_bindings"] = ["image-inspect", "test_selected_query_mcp_e2e.py", "test_selected_workflows_docker_e2e.py", "test_docker_e2e.py"]
        self.assert_refused(payload, "phase bindings")
        payload = self.golden()
        payload["phase_bindings"][-1] = "test_selected_workflows_docker_e2e.py"
        self.assert_refused(payload, "phase bindings")

    def test_refuses_wrong_harness_source_and_source_traversal(self) -> None:
        payload = self.golden()
        payload["fixed_harnesses"][0]["source_path"] = HARNESS_SOURCES[1]
        self.assert_refused(payload, "fixed E2E sources")
        payload = self.golden()
        payload["fixed_harnesses"][0]["source_path"] = "../test_docker_e2e.py"
        self.assert_refused(payload, "normalized relative path")

    def test_refuses_noncanonical_duplicate_and_unknown_context_json(self) -> None:
        self.assert_refused(self.golden(), "canonical JSON", canonical=False)
        path = self.scratch_root / "duplicate.json"
        path.write_bytes(b'{"schema_version":1,"schema_version":1}')
        with self.assertRaisesRegex(ReleaseE2EContextError, "canonical JSON"):
            load_release_e2e_context(self.environment(path))
        payload = self.golden()
        payload["unexpected"] = "x"
        self.assert_refused(payload, "unsupported schema")

    def test_refuses_junit_path_traversal_and_report_root_escape(self) -> None:
        payload = self.golden()
        payload["fixed_harnesses"][0]["junit_path"] = str(self.report_root / "../outside.xml")
        self.assert_refused(payload, "outside the sealed report root")
        outside = self.root / "outside-report"
        outside.mkdir()
        payload = self.golden()
        payload["report_root"] = str(outside)
        self.assert_refused(payload, "report_root is outside")

    def test_refuses_source_context_and_root_symlinks(self) -> None:
        context_target = self.write_context(self.golden())
        context_link = self.scratch_root / "context-link.json"
        context_link.symlink_to(context_target)
        with self.assertRaisesRegex(ReleaseE2EContextError, "regular absolute file"):
            load_release_e2e_context(self.environment(context_link))
        source_link = self.root / "source-link"
        source_link.symlink_to(self.source_root, target_is_directory=True)
        payload = self.golden()
        payload["source_root"] = str(source_link)
        self.assert_refused(payload, "non-symlink directory")

    def test_refuses_scratch_outside_source_and_report_outside_scratch(self) -> None:
        outside = self.root / "outside"
        outside.mkdir()
        payload = self.golden()
        payload["scratch_root"] = str(outside)
        self.assert_refused(payload, "scratch_root is outside")
        payload = self.golden()
        payload["report_root"] = str(outside)
        self.assert_refused(payload, "report_root is outside")
        payload = self.golden()
        payload["report_root"] = str(self.scratch_root)
        self.assert_refused(payload, "report_root must be a strict child")
        external_context = outside / "context.json"
        external_context.write_bytes(canonical_json(self.golden()))
        with self.assertRaisesRegex(ReleaseE2EContextError, "outside the executor-owned scratch root"):
            load_release_e2e_context(self.environment(external_context))

    def test_driver_rejects_wrong_cwd_and_absent_sealed_source_without_a_loader_mock(self) -> None:
        context = self.load(self.golden())
        harness = context.harnesses[0]
        args = argparse.Namespace(start_directory=START_DIRECTORY, pattern=harness.pattern, junit=harness.junit_path)
        previous = Path.cwd()
        try:
            os.chdir(self.scratch_root)
            with self.assertRaisesRegex(ReleaseE2EContextError, "working directory differs"):
                _bound_harness(context, args)
            os.chdir(self.source_root)
            (self.source_root / harness.source_path).unlink()
            with self.assertRaisesRegex(ReleaseE2EContextError, "source is absent or unsafe"):
                _bound_harness(context, args)
        finally:
            os.chdir(previous)

    def test_rejects_source_as_scratch_root(self) -> None:
        """D582 requires dedicated writable scratch outside source reads."""
        payload = self.golden()
        payload["scratch_root"] = str(self.source_root)
        self.assert_refused(payload, "scratch_root must be a strict child")

    def test_rejects_unclosed_or_unbound_optins(self) -> None:
        """D582 fixes all harness opt-ins and binds query values to the image."""
        payload = self.golden()
        payload["fixed_harnesses"][0]["context_optins"] = {"CAPRMEDIO_DOCKER_E2E": "0", "UNDECLARED": "1"}
        self.assert_refused(payload, "opt-ins")
