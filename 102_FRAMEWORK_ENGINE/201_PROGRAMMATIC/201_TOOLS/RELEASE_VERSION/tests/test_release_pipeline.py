"""Actual disposable compiler-to-retained-package frontier propagation tests."""

from __future__ import annotations

import sys
import unittest
from dataclasses import replace
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_compilation import render_release_candidate  # noqa: E402
from release_packaging import ReleasePackagingError, stage_framework_package  # noqa: E402
import test_release_compilation as compilation_test  # noqa: E402


class ReleasePipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = compilation_test.ReleaseCompilationTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def compiled(self):
        preflight, candidate = self.fixture.build()
        self.fixture.copy_source()
        handoff = render_release_candidate(candidate, preflight)
        return candidate, handoff

    def test_distinct_canonical_and_compiler_frontiers_stage_complete_idempotent_non_active_package(self) -> None:
        candidate, handoff = self.compiled()
        selector = self.fixture.root / ".caprmedio_runtime/framework/current.toml"
        selector_before = selector.read_bytes()
        self.assertNotEqual(handoff.compiler_frontier_digest, handoff.authority.canonical_source_snapshot_digest)
        self.assertEqual(handoff.compiler_frontier_digest, handoff.authority.source_frontier_digest)
        first = stage_framework_package(self.fixture.root, handoff)
        self.assertTrue(first["staged"])
        self.assertTrue(first["verified"])
        self.assertEqual(selector.read_bytes(), selector_before)
        self.assertFalse((self.fixture.root / ".agents/skills/ca").exists())
        second = stage_framework_package(self.fixture.root, handoff)
        self.assertFalse(second["staged"])
        self.assertTrue(second["verified"])
        self.assertEqual(first["release_root"], second["release_root"])
        self.assertEqual(candidate.authority.executing_release, "N")
        self.assertEqual(selector.read_bytes(), selector_before)

    def test_forged_compiler_frontier_and_stale_canonical_input_refuse_without_selector_change(self) -> None:
        _candidate, handoff = self.compiled()
        selector = self.fixture.root / ".caprmedio_runtime/framework/current.toml"
        selector_before = selector.read_bytes()
        forged_authority = handoff.authority.model_copy(update={"source_frontier_digest": "0" * 64})
        forged = handoff.model_copy(update={"authority": forged_authority})
        with self.assertRaises(ReleasePackagingError) as frontier:
            stage_framework_package(self.fixture.root, forged)
        self.assertEqual(frontier.exception.code, "release-currentness-stale")
        self.assertEqual(selector.read_bytes(), selector_before)
        self.fixture.core.write_bytes(self.fixture.core.read_bytes() + b"stale\n")
        with self.assertRaises(ReleasePackagingError) as stale:
            stage_framework_package(self.fixture.root, handoff)
        self.assertEqual(stale.exception.code, "release-currentness-stale")
        self.assertEqual(selector.read_bytes(), selector_before)


if __name__ == "__main__":
    unittest.main()
