"""D572-derived admission goldens; no registration or release execution claim."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
AUTHORITY_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "201_FEATURE_TOOLS/07_delivery/CA-D-572-TOOLS-DELIVERY--serialize-additive-release-route-source-admission.md"
)
AUTHORITY_SHA = "fb3e91bb5bee075c6394ac9a490b8599cd5cc8a9a86e7893f52e483556847b22"
sys.path.insert(0, str(MCP))

from release_source_admission import (  # noqa: E402
    ReleaseSourceAdmissionError, derive_release_source_admission, validate_release_source_admissions,
)


def reference_record(text: str) -> dict[str, object]:
    """Independent golden extraction from actual accepted Markdown, not 37 constants."""
    acceptance = re.search(r"CA-P-1622@1 at `([^`]+)`, SHA-256 `([0-9a-f]{64})`", text)
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
    return {"route": "release_version",
            "acceptance_frontier": {"atom_id": "CA-P-1622", "version": 1,
                                    "source_path": acceptance[1], "digest": acceptance[2]},
            "workflow": row_pin(tables[0][2]), "ordered_steps": steps,
            "ordered_actions": [copy.deepcopy(row["action"]) for row in steps],
            "rmed_frontier": [row_pin(row) for row in tables[2][2:]]}


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
            raise AssertionError("current D572@3 is not the accepted source pin")
        cls.expected = reference_record(actual.decode("utf-8"))

    def setUp(self) -> None:
        temporary = REPOSITORY / ".caprmedio_tmp/tests/release-source-admission"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for relative in {AUTHORITY_REF, *[pin["source_path"] for pin in all_pins(self.expected)]}:
            source = REPOSITORY / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        self.record = copy.deepcopy(self.expected)
        self.route = {"route": "release_version", **{key: copy.deepcopy(self.record[key])
                       for key in ("workflow", "ordered_steps", "ordered_actions")},
                      "native_action_calls": [], "entry_step": "CA-O-170",
                      "on_result": [], "mutation_capable": True}
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

    def test_actual_authority_derives_exact_repeated_occurrences_and_full_rmed(self) -> None:
        before = self.snapshot()
        record = derive_release_source_admission(self.root)
        self.assertEqual(self.expected, record)
        self.assertEqual(37, len({pin["source_path"] for pin in all_pins(record)}))
        self.assertEqual(10, len(record["ordered_steps"]))
        self.assertEqual(["CA-O-165", "CA-O-165", "CA-O-166", "CA-O-166", "CA-O-168",
                          "CA-O-167", "CA-O-168", "CA-O-168", "CA-O-169", "CA-O-169"],
                         [pin["atom_id"] for pin in record["ordered_actions"]])
        self.assertEqual(20, len(record["rmed_frontier"]))
        self.assertEqual(2, next(pin["version"] for pin in record["rmed_frontier"] if pin["atom_id"] == "CA-D-571"))
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

    def test_actual_fifteen_route_manifest_needs_no_release_authority(self) -> None:
        actual = json.loads((REPOSITORY / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json").read_text())
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
        for field in ("workflow", "ordered_steps", "ordered_actions", "rmed_frontier", "acceptance_frontier"):
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


if __name__ == "__main__":
    unittest.main()
