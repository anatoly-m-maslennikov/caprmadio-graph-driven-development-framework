"""D572-derived admission goldens; no registration or release execution claim."""
from __future__ import annotations

import copy
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
AUTHORITY_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "201_FEATURE_TOOLS/07_delivery/CA-D-572-TOOLS-DELIVERY--serialize-additive-release-route-source-admission.md"
)
AUTHORITY_SHA = "1f222e05533e9ea1d6cf44c0658e53545140be696c9e898a3aaf9343d0f2495a"
sys.path.insert(0, str(MCP))

import release_source_admission as admission_module  # noqa: E402
from release_source_admission import (  # noqa: E402
    ReleaseSourceAdmissionError, derive_release_graph_admission, derive_release_private_carriers, derive_release_route_graph, derive_release_source_admission,
    validate_release_source_admissions,
)
from selected_routes import canonical_digest  # noqa: E402


def reference_record(text: str) -> dict[str, object]:
    """Independent golden extraction from actual accepted Markdown, not static cardinalities."""
    acceptance = re.search(r"CA-P-1622@([1-9][0-9]*) at `([^`]+)`, SHA-256 `([0-9a-f]{64})`", text)
    assert acceptance is not None
    tables = []
    current = []
    for line in text.splitlines():
        if line.startswith("|"):
            current.append([cell.strip() for cell in line.strip("|").split("|")])
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    assert len(tables) == 3

    def row_pin(row: list[str]) -> dict[str, object]:
        atom_id, version, path, sha = row
        return {"atom_id": atom_id, "version": int(version), "source_path": path.strip("`"), "digest": sha.strip("`")}

    def occurrence(value: str) -> dict[str, object]:
        match = re.fullmatch(r"(CA-O-\d+)@(\d+) `([^`]+)` `([0-9a-f]{64})`", value)
        assert match is not None
        return {"atom_id": match[1], "version": int(match[2]), "source_path": match[3], "digest": match[4]}

    steps = [{"step": occurrence(row[1]), "action": occurrence(row[2])} for row in tables[1][2:]]
    metadata_match = re.search(r"^## Route serialization metadata\n+```json\n(.*?)\n```$", text, re.MULTILINE | re.DOTALL)
    assert metadata_match is not None
    metadata = json.loads(metadata_match[1])
    return {"route": "release_version",
            "acceptance_frontier": {"atom_id": "CA-P-1622", "version": int(acceptance[1]),
                                    "source_path": acceptance[2], "digest": acceptance[3]},
            "workflow": row_pin(tables[0][2]), "ordered_steps": steps,
            "ordered_actions": [copy.deepcopy(row["action"]) for row in steps],
            "rmed_frontier": [row_pin(row) for row in tables[2][2:]], **metadata}


def all_pins(record: dict[str, object]) -> list[dict[str, object]]:
    return [record["acceptance_frontier"], record["workflow"],
            *[pin for row in record["ordered_steps"] for pin in (row["step"], row["action"])],
            *record["ordered_actions"], *record["rmed_frontier"]]


class ReleaseSourceAdmissionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        authority = REPOSITORY / AUTHORITY_REF
        actual = authority.read_bytes()
        if hashlib.sha256(actual).hexdigest() != AUTHORITY_SHA:
            raise AssertionError("current D572@27 is not the accepted source pin")
        cls.expected = reference_record(actual.decode("utf-8"))
        cls.private_carriers = json.loads(re.search(
            r"^## Private implementation carriers\n+```json\n(.*?)\n```$",
            actual.decode("utf-8"), re.MULTILINE | re.DOTALL,
        )[1])

    def setUp(self) -> None:
        temporary = REPOSITORY / ".caprmedio_tmp/tests/release-source-admission"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for relative in {AUTHORITY_REF, *[pin["source_path"] for pin in all_pins(self.expected)],
                         *[row["source_path"] for row in self.private_carriers]}:
            source = REPOSITORY / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        self.record = copy.deepcopy(self.expected)
        self.graph = derive_release_route_graph(self.root)
        self.route = {"route": "release_version", **copy.deepcopy(self.graph)}
        # Fixture input is deliberately not saved as a canonical manifest.
        # Existing loader retains self-digest/registry/other-route validation.
        self.manifest = {"routes": [self.route], "release_source_admissions": [self.record]}

    def snapshot(self) -> dict[str, str | None]:
        return {path.relative_to(self.root).as_posix():
                hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
                for path in self.root.rglob("*")}

    def refused(self, manifest: object) -> None:
        before = self.snapshot()
        with self.assertRaises(ReleaseSourceAdmissionError):
            validate_release_source_admissions(self.root, manifest)
        self.assertEqual(before, self.snapshot(), "rejected admission mutated Project evidence")

    @contextmanager
    def trusted_workflow_source(self, contents: str):
        """Temporarily trust a fixture-only O164/D572 pair for parser negatives."""
        workflow = self.root / self.record["workflow"]["source_path"]
        authority = self.root / AUTHORITY_REF
        original_workflow, original_authority = workflow.read_bytes(), authority.read_bytes()
        try:
            workflow.write_text(contents, encoding="utf-8")
            updated = hashlib.sha256(workflow.read_bytes()).hexdigest()
            updated_authority = original_authority.decode("utf-8").replace(
                self.record["workflow"]["digest"], updated, 1
            ).encode("utf-8")
            authority.write_bytes(updated_authority)
            authority_pin = {**admission_module.AUTHORITY_PIN,
                             "digest": hashlib.sha256(updated_authority).hexdigest()}
            with patch.object(admission_module, "AUTHORITY_PIN", authority_pin):
                yield
        finally:
            workflow.write_bytes(original_workflow)
            authority.write_bytes(original_authority)

    @contextmanager
    def trusted_route_metadata(self, payload: str):
        """Temporarily trust fixture-only typed D572 metadata for provenance tests."""
        authority = self.root / AUTHORITY_REF
        original = authority.read_bytes()
        try:
            updated = original.decode("utf-8").replace(
                '{"mutation_capable": true,"native_action_calls": []}', payload, 1
            ).encode("utf-8")
            self.assertNotEqual(original, updated)
            authority.write_bytes(updated)
            authority_pin = {**admission_module.AUTHORITY_PIN,
                             "digest": hashlib.sha256(updated).hexdigest()}
            with patch.object(admission_module, "AUTHORITY_PIN", authority_pin):
                yield
        finally:
            authority.write_bytes(original)

    def test_actual_authority_derives_exact_repeated_occurrences_and_full_rmed(self) -> None:
        before = self.snapshot()
        record = derive_release_source_admission(self.root)
        self.assertEqual(self.expected, record)
        self.assertEqual(55, len({pin["source_path"] for pin in all_pins(record)}))
        self.assertEqual(12, len(record["ordered_steps"]))
        self.assertEqual(6, record["workflow"]["version"])
        self.assertEqual(4, record["acceptance_frontier"]["version"])
        self.assertEqual(["CA-O-170", "CA-O-171", "CA-O-172", "CA-O-173", "CA-O-185", "CA-O-175",
                          "CA-O-176", "CA-O-186", "CA-O-182", "CA-O-184", "CA-O-178", "CA-O-179"],
                         [row["step"]["atom_id"] for row in record["ordered_steps"]])
        self.assertIs(True, record["mutation_capable"])
        self.assertEqual([], record["native_action_calls"])
        self.assertEqual(["CA-O-165", "CA-O-165", "CA-O-166", "CA-O-166", "CA-O-168",
                          "CA-O-167", "CA-O-168", "CA-O-168", "CA-O-181", "CA-O-183", "CA-O-169", "CA-O-169"],
                         [pin["atom_id"] for pin in record["ordered_actions"]])
        self.assertEqual(34, len(record["rmed_frontier"]))
        self.assertTrue({"CA-R-1886", "CA-M-343", "CA-E-586", "CA-D-579", "CA-D-580",
                         "CA-R-1890", "CA-M-346", "CA-E-589", "CA-D-582"}.issubset(
                             {pin["atom_id"] for pin in record["rmed_frontier"]}))
        self.assertEqual(2, next(pin["version"] for pin in record["rmed_frontier"] if pin["atom_id"] == "CA-D-571"))
        self.assertEqual(2, next(pin["version"] for pin in record["rmed_frontier"] if pin["atom_id"] == "CA-D-573"))
        self.assertEqual(1, next(pin["version"] for pin in record["rmed_frontier"] if pin["atom_id"] == "CA-D-574"))
        self.assertNotIn("CA-D-565", {pin["atom_id"] for pin in record["rmed_frontier"]})
        self.assertNotIn("CA-D-572", {pin["atom_id"] for pin in all_pins(record)})
        self.assertEqual(before, self.snapshot())

    def test_current_complete_record_and_matching_route_validate_without_writes(self) -> None:
        before = self.snapshot()
        original_manifest = copy.deepcopy(self.manifest)
        result = validate_release_source_admissions(self.root, self.manifest)
        self.assertEqual([self.expected], result)
        self.assertEqual(original_manifest, self.manifest)
        self.assertEqual(before, self.snapshot())

    def test_private_carriers_reopen_without_extending_the_public_record(self) -> None:
        before = self.snapshot()
        self.assertEqual(self.private_carriers, derive_release_private_carriers(self.root))
        self.assertEqual(22, len(self.private_carriers))
        self.assertEqual(sorted({row["source_path"] for row in self.private_carriers}),
                         [row["source_path"] for row in self.private_carriers])
        self.assertEqual({"route", "acceptance_frontier", "workflow", "ordered_steps", "ordered_actions",
                          "rmed_frontier", "mutation_capable", "native_action_calls"}, set(self.record))
        for row in self.private_carriers:
            with self.subTest(source_path=row["source_path"]):
                path = self.root / row["source_path"]
                raw = path.read_bytes()
                path.write_bytes(raw + b"\nchanged private carrier\n")
                self.refused(self.manifest)
                path.write_bytes(raw)
        path = self.root / self.private_carriers[0]["source_path"]
        raw = path.read_bytes()
        path.unlink()
        self.refused(self.manifest)
        path.symlink_to(REPOSITORY / self.private_carriers[0]["source_path"])
        self.refused(self.manifest)
        path.unlink()
        path.write_bytes(raw)
        self.assertEqual(before, self.snapshot())

    def test_trusted_fixture_rejects_open_or_cyclic_private_carrier_declarations(self) -> None:
        authority = self.root / AUTHORITY_REF
        original = authority.read_bytes()
        block = re.compile(r"(## Private implementation carriers\n+```json\n)(.*?)(\n```)", re.DOTALL)
        variants = (
            [], self.private_carriers[::-1], [self.private_carriers[0], *self.private_carriers],
            [{**self.private_carriers[0], "caller_approval": True}],
            [{"source_path": "../escape.py", "sha256": "a" * 64}],
            [{"source_path": "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/release_source_admission.py",
              "sha256": "a" * 64}],
        )
        for rows in variants:
            with self.subTest(rows=rows):
                altered = block.sub(lambda match: match[1] + json.dumps(rows) + match[3],
                                    original.decode("utf-8")).encode("utf-8")
                authority.write_bytes(altered)
                pin = {**admission_module.AUTHORITY_PIN, "digest": hashlib.sha256(altered).hexdigest()}
                with patch.object(admission_module, "AUTHORITY_PIN", pin):
                    self.refused(self.manifest)
        authority.write_bytes(original)

    def test_actual_workflow_derives_the_closed_route_graph(self) -> None:
        route, admission = derive_release_graph_admission(self.root)
        self.assertEqual(self.record, admission)
        self.assertEqual("release_version", route["route"])
        self.assertEqual(self.record["workflow"], self.graph["workflow"])
        self.assertEqual(self.record["ordered_steps"], self.graph["ordered_steps"])
        self.assertEqual(self.record["ordered_actions"], self.graph["ordered_actions"])
        self.assertEqual("CA-O-170", self.graph["entry_step"])
        self.assertEqual([], self.graph["native_action_calls"])
        self.assertIs(True, self.graph["mutation_capable"])
        self.assertEqual(12, len(self.graph["on_result"]))
        self.assertEqual([row["step"]["atom_id"] for row in self.record["ordered_steps"]],
                         [edge["from"] for edge in self.graph["on_result"]])
        self.assertEqual("complete", self.graph["on_result"][-1]["to"])

    def test_trusted_fixture_rejects_missing_stop_and_malformed_workflow_tables(self) -> None:
        workflow = (self.root / self.record["workflow"]["source_path"]).read_text(encoding="utf-8")
        variants = (
            workflow.replace(
                "| any missing, stale, unauthorized, failed, partial, recording-blocked, unsafe, or unmatched result | stop with its actual evidence; do not promote, retire, retry, or recurse implicitly |\n",
                "",
                1,
            ),
            workflow.replace("| Step | Action | Bound phase |", "| Step | Bound phase |", 1),
        )
        for contents in variants:
            with self.subTest(contents=contents):
                with self.trusted_workflow_source(contents):
                    with self.assertRaisesRegex(ReleaseSourceAdmissionError, "O164 Workflow graph cannot be parsed"):
                        derive_release_graph_admission(self.root)

    def test_trusted_fixture_derives_flags_from_typed_d572_metadata(self) -> None:
        with self.trusted_route_metadata('{"mutation_capable": false,"native_action_calls": []}'):
            route, _ = derive_release_graph_admission(self.root)
            self.assertIs(False, route["mutation_capable"])
            self.assertEqual([], route["native_action_calls"])
        with self.trusted_route_metadata('{"mutation_capable": true,"native_action_calls": ["CA-O-165"]}'):
            with self.assertRaisesRegex(ReleaseSourceAdmissionError, "closed typed declaration"):
                derive_release_graph_admission(self.root)

    def test_actual_fifteen_route_manifest_needs_no_release_authority(self) -> None:
        actual = json.loads((REPOSITORY / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json").read_text())
        self.assertEqual(16, len(actual["routes"]))
        actual["routes"] = actual["routes"][:-1]
        actual.pop("release_source_admissions")
        actual["source_freshness"]["selected_binding_digest"] = canonical_digest(actual["routes"])
        unsigned = {key: value for key, value in actual.items() if key != "canonical_manifest_sha256"}
        actual["canonical_manifest_sha256"] = canonical_digest(unsigned)
        self.assertEqual(15, len(actual["routes"]))
        self.assertNotIn("release_source_admissions", actual)
        (self.root / AUTHORITY_REF).unlink()
        before = self.snapshot()
        original = copy.deepcopy(actual)
        self.assertEqual([], validate_release_source_admissions(self.root, actual))
        self.assertEqual(original, actual)
        self.assertEqual(before, self.snapshot())

    def test_absent_duplicate_unknown_and_wrong_route_admissions_refuse(self) -> None:
        variants = []
        missing = copy.deepcopy(self.manifest)
        missing.pop("release_source_admissions")
        variants.append(missing)
        for admissions in (None, {}, [], [self.record, self.record], [{**self.record, "caller_approval": True}],
                           [{**self.record, "route": "find_and_fetch_artifacts"}]):
            variants.append({**self.manifest, "release_source_admissions": admissions})
        variants.append({**self.manifest, "routes": [self.route, self.route]})
        variants.append({"routes": [], "release_source_admissions": []})
        variants.append({"routes": [], "release_source_admissions": [self.record]})
        for variant in variants:
            with self.subTest(variant=variant):
                self.refused(variant)

    def test_missing_reordered_duplicate_and_forged_frontiers_refuse(self) -> None:
        for field in ("workflow", "ordered_steps", "ordered_actions", "rmed_frontier", "acceptance_frontier",
                      "mutation_capable", "native_action_calls"):
            record = copy.deepcopy(self.record)
            record.pop(field)
            self.refused({**self.manifest, "release_source_admissions": [record]})
        for field in ("ordered_steps", "ordered_actions", "rmed_frontier"):
            for mutate in (lambda rows: rows[:-1], lambda rows: rows[::-1],
                           lambda rows: [rows[0], *rows[:-1]]):
                record = copy.deepcopy(self.record)
                record[field] = mutate(record[field])
                self.refused({**self.manifest, "release_source_admissions": [record]})
        record = copy.deepcopy(self.record)
        record["acceptance_frontier"]["atom_id"] = "CA-P-1687"
        self.refused({**self.manifest, "release_source_admissions": [record]})
        record = copy.deepcopy(self.record)
        record["rmed_frontier"][-1]["atom_id"] = "CA-D-572"
        self.refused({**self.manifest, "release_source_admissions": [record]})
        for field, values in (("mutation_capable", (None, 0, False)),
                              ("native_action_calls", (None, 0, False, ["CA-O-165"]))):
            for value in values:
                record = copy.deepcopy(self.record)
                record[field] = value
                self.refused({**self.manifest, "release_source_admissions": [record]})

    def test_pin_types_unknown_fields_unsafe_paths_and_forged_live_hash_refuse(self) -> None:
        for field, value in (("version", True), ("version", 0), ("version", "2"),
                             ("digest", "A" * 64), ("digest", "f" * 64),
                             ("source_path", "../escape.md"), ("source_path", "/absolute.md"),
                             ("source_path", "https://example.test/authority.md"),
                             ("source_path", "safe/../definition.md"), ("expected_digest", "f" * 64)):
            record = copy.deepcopy(self.record)
            record["workflow"][field] = value
            self.refused({**self.manifest, "release_source_admissions": [record]})

    def test_every_actual_pin_reobserves_byte_identity_and_positive_version(self) -> None:
        unique = {pin["source_path"]: pin for pin in all_pins(self.record)}
        for relative, pin in unique.items():
            with self.subTest(atom_id=pin["atom_id"]):
                path = self.root / relative
                original = path.read_bytes()
                path.write_bytes(original + b"\nDeliberately stale current source.\n")
                self.refused(self.manifest)
                path.write_bytes(original)
        # A caller cannot refresh the declared hash to bless changed identity.
        pin = self.record["workflow"]
        path = self.root / pin["source_path"]
        raw = path.read_text()
        path.write_text(re.sub(r"(?m)^atom_id:.*$", "atom_id: CA-O-9999", raw, count=1))
        forged = copy.deepcopy(self.manifest)
        forged["release_source_admissions"][0]["workflow"]["digest"] = hashlib.sha256(path.read_bytes()).hexdigest()
        forged["routes"][0]["workflow"] = copy.deepcopy(forged["release_source_admissions"][0]["workflow"])
        self.refused(forged)

    def test_authority_edit_absence_symlink_and_selected_route_disagreement_refuse(self) -> None:
        authority = self.root / AUTHORITY_REF
        original = authority.read_bytes()
        authority.write_bytes(original + b"\nUnaccepted new authority.\n")
        self.refused(self.manifest)
        authority.unlink()
        self.refused(self.manifest)
        authority.symlink_to(REPOSITORY / AUTHORITY_REF)
        self.refused(self.manifest)
        authority.unlink()
        authority.write_bytes(original)
        source = self.root / self.record["workflow"]["source_path"]
        source.unlink()
        source.symlink_to(REPOSITORY / self.record["workflow"]["source_path"])
        self.refused(self.manifest)
        source.unlink()
        shutil.copyfile(REPOSITORY / self.record["workflow"]["source_path"], source)
        route = copy.deepcopy(self.route)
        route["ordered_actions"] = route["ordered_actions"][:-1]
        self.refused({**self.manifest, "routes": [route]})
        route = copy.deepcopy(self.route)
        route["ordered_steps"][0]["step"]["version"] = True
        self.refused({**self.manifest, "routes": [route]})

    def test_structurally_valid_route_graph_alterations_refuse(self) -> None:
        variants = []
        route = copy.deepcopy(self.route)
        route["entry_step"] = "CA-O-171"
        variants.append(route)
        route = copy.deepcopy(self.route)
        route["on_result"][0]["to"] = "CA-O-172"
        variants.append(route)
        route = copy.deepcopy(self.route)
        route["on_result"] = route["on_result"][::-1]
        variants.append(route)
        route = copy.deepcopy(self.route)
        route["native_action_calls"] = [copy.deepcopy(route["ordered_actions"][0])]
        variants.append(route)
        route = copy.deepcopy(self.route)
        route["mutation_capable"] = False
        variants.append(route)
        for route in variants:
            with self.subTest(route=route):
                self.refused({**self.manifest, "routes": [route]})


if __name__ == "__main__":
    unittest.main()
