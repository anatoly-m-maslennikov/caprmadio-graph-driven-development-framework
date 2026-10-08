"""Native W11/W12 graph corpus proof in disposable Project authority."""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
GRAPH_ROOT = APP.parents[1] / "201_TOOLS" / "GENERATE_ENTITY_GRAPH"
if str(GRAPH_ROOT) not in sys.path:
    sys.path.insert(0, str(GRAPH_ROOT))
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

import generate_entity_graph  # noqa: E402
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject  # noqa: E402


class SelectedGraphGoldenInputsTest(unittest.TestCase):
    """W11/W12 invoke their actual Action adapters, not fixture markers."""

    def _fixture(self, case_id: str, route: str) -> tuple[FixtureLease, GoldenProject]:
        parent = ROOT / ".caprmedio_tmp" / "tests" / "selected-graph-golden-inputs"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        fixture = GoldenProject(ROOT, root, GoldenCase(case_id, route))
        fixture.prepare()
        return FixtureLease(root), fixture

    @staticmethod
    def _source_bytes(fixture: GoldenProject) -> dict[str, str]:
        return {
            path.relative_to(fixture.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(fixture.graph_source_dir.glob("*.md"))
        }

    @staticmethod
    def _native_graph_request(fixture: GoldenProject) -> dict[str, object]:
        """Direct Tool proof needs the same non-caller recording capability.

        Selected-route execution receives this object from its real shared
        Action-start recorder; this narrow native-adapter test constructs only
        the structural capability needed to exercise Tool behavior.
        """

        request = fixture.native_parameters()
        request["run_recording_context"] = generate_entity_graph.actual_run_recording_context(
            "golden-workflow", "golden-step", "golden-action",
            {
                "event_id": "golden-action-start",
                "action_id": "golden-action",
                "event_digest": "0" * 64,
                "carrier": ".caprmedio_caprmedio/_journal/golden.ndjson",
                "line": 1,
                "previous_carrier_digest": "0" * 64,
                "appended_carrier_digest": "1" * 64,
            },
        )
        return request

    def test_w11_w12_publish_traceable_deterministic_native_projections(self) -> None:
        for case_id, route, adapter, graph_key, output in (
            ("W11", "build_entities_graph", generate_entity_graph.construct_entities_graph_projection,
             "entities_graph", "entities_graph.json"),
            ("W12", "build_terms_graph", generate_entity_graph.construct_terms_graph_projection,
             "terms_graph", "terms_graph.json"),
        ):
            with self.subTest(case=case_id):
                lease, fixture = self._fixture(case_id, route)
                try:
                    before_sources = self._source_bytes(fixture)
                    request = self._native_graph_request(fixture)
                    first = adapter(fixture.root, request)
                    projection = fixture.root / ".caprmedio_caprmedio/_projection" / output
                    self.assertEqual("built", first["outcome"], first)
                    self.assertTrue(projection.is_file())
                    self.assertIn(graph_key, first)
                    self.assertTrue(first["non_authoritative"])
                    self.assertEqual(before_sources, self._source_bytes(fixture), "graph publication must not change sources")
                    self.assertEqual(
                        [".caprmedio_caprmedio/graph_sources/CA-R-201.md",
                         ".caprmedio_caprmedio/graph_sources/CA-R-202.md",
                         ".caprmedio_caprmedio/graph_sources/CA-R-203.md"],
                        [row["carrier_path"] for row in first["lineage"]],
                    )
                    first_bytes = projection.read_bytes()
                    second = adapter(fixture.root, self._native_graph_request(fixture))
                    self.assertEqual("no_op", second["outcome"], second)
                    self.assertEqual(first_bytes, projection.read_bytes())
                finally:
                    lease.cleanup()

    def test_w11_w12_reject_malformed_or_stale_source_inputs_without_effects(self) -> None:
        for case_id, route, adapter in (
            ("W11", "build_entities_graph", generate_entity_graph.construct_entities_graph_projection),
            ("W12", "build_terms_graph", generate_entity_graph.construct_terms_graph_projection),
        ):
            with self.subTest(case=case_id, condition="malformed"):
                lease, fixture = self._fixture(case_id, route)
                try:
                    malformed = self._native_graph_request(fixture)
                    malformed["selection"] = {"atom_ids": "CA-R-201"}
                    result = adapter(fixture.root, malformed)
                    self.assertEqual("failed", result["outcome"], result)
                    self.assertEqual([], result["output_effects"]["paths"])
                finally:
                    lease.cleanup()
            with self.subTest(case=case_id, condition="stale"):
                lease, fixture = self._fixture(case_id, route)
                try:
                    request = self._native_graph_request(fixture)
                    source = fixture.graph_source_dir / "CA-R-201.md"
                    source.write_text(source.read_text(encoding="utf-8") + "\nChanged after frontier.\n", encoding="utf-8")
                    result = adapter(fixture.root, request)
                    self.assertEqual("stale", result["outcome"], result)
                    self.assertEqual([], result["output_effects"]["paths"])
                finally:
                    lease.cleanup()


if __name__ == "__main__":
    unittest.main()
