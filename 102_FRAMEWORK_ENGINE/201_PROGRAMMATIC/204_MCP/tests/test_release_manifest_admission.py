"""Preparatory canonical loader proof, not Release registration or execution."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
APP_TESTS = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
for location in (MCP, MCP / "tests", APP_TESTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import test_release_source_admission as source_goldens  # noqa: E402
from selected_routes import (  # noqa: E402
    SELECTED_ROUTE_NAMES, SelectedRouteAdapter, SelectedRouteError, canonical_digest,
    load_selected_manifest, selected_manifest_contract,
)
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402


class _NeverSupport:
    def __init__(self) -> None:
        self.calls = 0

    def run_selected_operation(self, request: dict) -> dict:
        self.calls += 1
        raise AssertionError("refused input reached shared support")


class ReleaseManifestAdmissionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        source_goldens.ReleaseSourceAdmissionTest.setUpClass()

    def setUp(self) -> None:
        # Reuse actual D572 plus all39 copied pins; add the actual unchanged15
        # manifest through its strict existing source-copy fixture helper.
        self.fixture = source_goldens.ReleaseSourceAdmissionTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        project = GoldenProject(REPOSITORY, self.root, GoldenCase("W04", "change_atom_status"))
        self.base = project._copy_reviewed_manifest()
        self.path = project.manifest_path
        self.record = copy.deepcopy(self.fixture.record)
        self.release = copy.deepcopy(self.fixture.route)

    def successor(self) -> dict:
        return {**copy.deepcopy(self.base), "routes": [*copy.deepcopy(self.base["routes"]), copy.deepcopy(self.release)],
                "release_source_admissions": [copy.deepcopy(self.record)]}

    def save(self, manifest: dict, *, rehash: bool = True) -> None:
        if rehash:
            manifest["source_freshness"]["selected_binding_digest"] = canonical_digest(manifest["routes"])
            unsigned = {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
            manifest["canonical_manifest_sha256"] = canonical_digest(unsigned)
        self.path.write_text(json.dumps(manifest, separators=(",", ":")), encoding="utf-8")

    def refusal(self, manifest: dict) -> None:
        self.save(manifest)
        before = self.fixture.snapshot()
        support = _NeverSupport()
        with self.assertRaises(SelectedRouteError):
            SelectedRouteAdapter(self.root, service=support)
        self.assertEqual(0, support.calls)
        self.assertEqual(before, self.fixture.snapshot())

    def test_actual_fifteen_route_compatibility_is_byte_preserving_and_not_advertised_as_sixteen(self) -> None:
        before = self.fixture.snapshot()
        loaded = load_selected_manifest(self.root)
        self.assertEqual(list(SELECTED_ROUTE_NAMES), [row["route"] for row in loaded["routes"]])
        self.assertEqual(15, len(SELECTED_ROUTE_NAMES))
        self.assertEqual(list(SELECTED_ROUTE_NAMES), selected_manifest_contract(self.root)["route_names"])
        self.assertNotIn("release_source_admissions", loaded)
        self.assertEqual(self.base["source_freshness"], loaded["source_freshness"])
        self.assertEqual(self.base["query_source_admissions"], loaded["query_source_admissions"])
        self.assertEqual((REPOSITORY / self.path.relative_to(self.root)).read_bytes(), self.path.read_bytes())
        self.assertEqual(before, self.fixture.snapshot())

    def test_actual_source_bound_successor_sixteen_loads_without_changing_first_fifteen_or_registration(self) -> None:
        manifest = self.successor()
        self.save(manifest)
        before = self.fixture.snapshot()
        loaded = load_selected_manifest(self.root)
        self.assertEqual([*SELECTED_ROUTE_NAMES, "release_version"], [row["route"] for row in loaded["routes"]])
        self.assertEqual(self.base["routes"], loaded["routes"][:-1])
        self.assertEqual([self.record], loaded["release_source_admissions"])
        self.assertEqual(self.base["query_source_admissions"], loaded["query_source_admissions"])
        self.assertEqual(15, len(SELECTED_ROUTE_NAMES), "a preparatory loader must not advertise/register Release")
        self.assertEqual(before, self.fixture.snapshot())

    def test_missing_extra_unknown_or_out_of_order_release_evidence_refuses_before_support(self) -> None:
        manifest = self.successor()
        manifest.pop("release_source_admissions")
        self.refusal(manifest)
        for value in ([], None, [self.record, self.record], [{**self.record, "caller_approval": True}]):
            self.refusal({**self.successor(), "release_source_admissions": value})
        self.refusal({**copy.deepcopy(self.base), "release_source_admissions": []})
        for field in ("ordered_steps", "ordered_actions", "rmed_frontier"):
            manifest = self.successor()
            manifest["release_source_admissions"][0][field].reverse()
            self.refusal(manifest)
        manifest = self.successor()
        manifest["release_source_admissions"][0]["rmed_frontier"].pop()
        self.refusal(manifest)
        for field in ("mutation_capable", "native_action_calls"):
            manifest = self.successor()
            manifest["release_source_admissions"][0].pop(field)
            self.refusal(manifest)
        for field, values in (("mutation_capable", (None, 0, False)),
                              ("native_action_calls", (None, 0, False, ["CA-O-165"]))):
            for value in values:
                manifest = self.successor()
                manifest["release_source_admissions"][0][field] = value
                self.refusal(manifest)

    def test_registry_order_unknown_route_and_existing_query_guards_remain_closed(self) -> None:
        manifest = self.successor()
        manifest["routes"][0], manifest["routes"][1] = manifest["routes"][1], manifest["routes"][0]
        self.refusal(manifest)
        manifest = self.successor()
        manifest["routes"][-1]["route"] = "release_unlisted"
        self.refusal(manifest)
        manifest = self.successor()
        manifest["routes"].append(copy.deepcopy(self.release))
        self.refusal(manifest)
        manifest = self.successor()
        manifest["query_source_admissions"].pop()
        self.refusal(manifest)
        manifest = self.successor()
        manifest["source_freshness"]["selected_source_registry_version"] = 3
        self.refusal(manifest)

    def test_rehashed_structurally_valid_release_graph_alterations_refuse_before_support(self) -> None:
        mutations = (
            ("entry_step", lambda route: route.__setitem__("entry_step", "CA-O-171")),
            ("transition", lambda route: route["on_result"][0].__setitem__("to", "CA-O-172")),
            ("native-call", lambda route: route.__setitem__(
                "native_action_calls", [copy.deepcopy(route["ordered_actions"][0])])),
            ("capability", lambda route: route.__setitem__("mutation_capable", False)),
        )
        for name, mutate in mutations:
            with self.subTest(name=name):
                manifest = self.successor()
                mutate(manifest["routes"][-1])
                self.refusal(manifest)

    def test_self_digest_binding_digest_and_stale_actual_rmed_are_rejected(self) -> None:
        manifest = self.successor()
        self.save(manifest)
        manifest["canonical_manifest_sha256"] = "f" * 64
        self.save(manifest, rehash=False)
        with self.assertRaisesRegex(SelectedRouteError, "canonical digest differs"):
            load_selected_manifest(self.root)
        manifest = self.successor()
        self.save(manifest)
        manifest["source_freshness"]["selected_binding_digest"] = "f" * 64
        unsigned = {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
        manifest["canonical_manifest_sha256"] = canonical_digest(unsigned)
        self.save(manifest, rehash=False)
        with self.assertRaisesRegex(SelectedRouteError, "binding digest differs"):
            load_selected_manifest(self.root)
        pin = self.record["rmed_frontier"][-1]
        source = self.root / pin["source_path"]
        source.write_bytes(source.read_bytes() + b"\nDeliberately stale D574.\n")
        self.refusal(self.successor())

    def test_raw_duplicate_members_reject_before_json_collapse_at_every_depth(self) -> None:
        self.save(self.successor())
        text = self.path.read_text()
        mutations = (text.replace('"schema_version":1', '"schema_version":1,"schema_version":1', 1),
                     text.replace('"route":"release_version"', '"route":"release_version","route":"release_version"', 1),
                     text.replace('"atom_id":"CA-O-164"', '"atom_id":"CA-O-164","atom_id":"CA-O-164"', 1))
        for raw in mutations:
            self.assertNotEqual(text, raw)
            self.path.write_text(raw)
            before = self.fixture.snapshot()
            with self.assertRaisesRegex(SelectedRouteError, "duplicate JSON"):
                load_selected_manifest(self.root)
            self.assertEqual(before, self.fixture.snapshot())

    def test_release_evidence_cannot_enter_d527_request_or_its_two_field_manifest(self) -> None:
        support = _NeverSupport()
        adapter = SelectedRouteAdapter(self.root, service=support)
        parameters, refs, effects = {}, ["fixture/target"], []
        request = {"operation_route": "create_scope_unit", "mode": "preview", "request_id": "release-field-refusal",
                   "parameters": parameters, "parameters_digest": canonical_digest(parameters),
                   "target_frontier": refs, "target_frontier_digest": canonical_digest(refs),
                   "effects": effects, "effects_digest": canonical_digest(effects),
                   "definition_manifest": {"manifest_ref": self.path.relative_to(self.root).as_posix(),
                                           "manifest_digest": self.base["canonical_manifest_sha256"]},
                   "source_freshness": copy.deepcopy(self.base["source_freshness"]),
                   "initiative": {"initiative_id": "fixture", "instruction_summary": "refusal fixture"}}
        for location in ("outer", "definition_manifest"):
            forged = copy.deepcopy(request)
            target = forged if location == "outer" else forged["definition_manifest"]
            target["release_source_admissions"] = [self.record]
            result = adapter.invoke("create_scope_unit", forged)
            self.assertEqual("rejected", result["disposition"], result)
            self.assertEqual(0, support.calls)


if __name__ == "__main__":
    unittest.main()
