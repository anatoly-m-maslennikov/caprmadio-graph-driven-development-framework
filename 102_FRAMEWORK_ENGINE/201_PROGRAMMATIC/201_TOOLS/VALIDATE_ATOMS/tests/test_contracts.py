"""Focused boundary regressions complementing the public-command golden corpus."""

from __future__ import annotations

import copy
from collections.abc import Callable
import json
from pathlib import Path
import sys
import unittest
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from validate_atoms_workers.contracts import (  # noqa: E402
    empty_report,
    parse_request,
    request_error_report,
    validate_report,
)


def request() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "source_roots": ["/source"],
        "allowed_read_roots": ["/allowed"],
        "methodology": {"kind": "sources", "roots": ["/authority"]},
        "selection": {"scope_unit": "TOOLS"},
    }


class RequestBoundaryTests(unittest.TestCase):
    def test_golden_invalid_requests(self) -> None:
        for path in sorted((HERE / "requests").glob("request_*.json")):
            with self.subTest(path=path.name), self.assertRaises(ValueError):
                parse_request(path.read_text(encoding="utf-8"))

    def test_accepted_request_preserves_omission(self) -> None:
        payload = request()
        accepted = parse_request(json.dumps(payload))
        self.assertEqual(accepted.model_dump(mode="json", exclude_unset=True), payload)

    def test_normalizes_and_orders_paths_without_reading(self) -> None:
        payload = request()
        payload["source_roots"] = ["/z/nonexistent/../source", "/a//source/"]
        accepted = parse_request(json.dumps(payload))
        self.assertEqual(accepted.source_roots, ["/a/source", "/z/source"])
        payload["source_roots"] = ["/a//source", "/a/source"]
        with self.assertRaises(ValueError):
            parse_request(json.dumps(payload))

    def test_optional_fields_reject_supplied_null(self) -> None:
        for name in (
            "action_binding",
            "project_structure",
            "reference_roots",
            "exclude_paths",
            "limits",
            "framework_settings",
            "default_settings",
            "run_context",
            "rule_bundle",
        ):
            payload = request()
            payload[name] = None
            with self.subTest(name=name), self.assertRaises(ValueError):
                parse_request(json.dumps(payload))
        for section, name in (
            ("methodology", "frontier"),
            ("selection", "statuses"),
            ("selection", "include_descendants"),
            ("selection", "atoms"),
        ):
            payload = request()
            payload[section][name] = None
            with self.subTest(section=section, name=name), self.assertRaises(ValueError):
                parse_request(json.dumps(payload))

    def test_nested_duplicate_keys_and_nonfinite_numbers(self) -> None:
        for replacement in (
            '{"scope_unit":"TOOLS","scope_unit":"OTHER"}',
            '{"global_tiers":[NaN]}',
            '{"global_tiers":[Infinity]}',
            '{"global_tiers":[-Infinity]}',
            '{"global_tiers":[1e999]}',
        ):
            raw = json.dumps(request()).replace('{"scope_unit": "TOOLS"}', replacement)
            with self.subTest(replacement=replacement), self.assertRaises(ValueError):
                parse_request(raw)

    def test_excessively_nested_json_is_a_request_error(self) -> None:
        with self.assertRaises(ValueError):
            parse_request("[" * 2000 + "1" + "]" * 2000)

    def test_selection_sets_and_dependencies(self) -> None:
        for selector in (
            {"global_tiers": [1, 1]},
            {"local_tiers": ["A", "A"]},
            {"scope_unit": "T", "statuses": ["Draft", "Draft"]},
            {"atoms": [{"atom_id": "A"}, {"atom_id": "A"}]},
            {"atoms": [{"carrier_path": "/a", "version": 1}]},
            {"atoms": [{"atom_id": "A", "version": True}]},
            {"atoms": [{"atom_id": "A", "version": None}]},
            {"local_tiers": [""]},
            {"scope_unit": ""},
            {"global_tiers": [1], "include_descendants": False},
        ):
            payload = request()
            payload["selection"] = selector
            with self.subTest(selector=selector), self.assertRaises(ValueError):
                parse_request(json.dumps(payload))

    def test_binding_and_bundle_types(self) -> None:
        binding = {"atom_id": "CA-R-1", "version": 1, "path": "/r", "sha256": "a" * 64}
        payload = request()
        payload["methodology"]["frontier"] = [binding]
        payload["rule_bundle"] = {"schema_version": 1, "authority": [binding], "checks": []}
        bundle = parse_request(json.dumps(payload)).rule_bundle
        assert bundle is not None
        self.assertEqual(bundle.schema_version, 1)
        for mutation in ({"schema_version": True}, {"authority": [binding, binding]}):
            bad = copy.deepcopy(payload)
            bad["rule_bundle"].update(mutation)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                parse_request(json.dumps(bad))


class ReportBoundaryTests(unittest.TestCase):
    def test_request_error_matches_reviewed_golden(self) -> None:
        golden = json.loads((HERE / "expected/request_duplicate_key.json").read_text())
        self.assertEqual(request_error_report(), golden)
        self.assertEqual(validate_report(golden), golden)

    def test_empty_report_is_fresh_and_valid_shape(self) -> None:
        first, second = empty_report(), empty_report()
        self.assertEqual(validate_report(first), first)
        first["findings"].append({})
        self.assertEqual(second["findings"], [])

    def test_report_rejects_closed_shape_and_bad_counts(self) -> None:
        mutations: list[Callable[[dict[str, Any]], None]] = [
            lambda r: r.update(schema_version=True),
            lambda r: r.update(unknown=1),
            lambda r: r["execution"].update(unknown=1),
            lambda r: r["coverage"]["targets"].update(selected=True),
            lambda r: r["coverage"]["rules"].update(required=1),
            lambda r: r["coverage"]["outcomes"].update(passed=1),
            lambda r: r.update(result="valid"),
            lambda r: r["execution"]["limits"].update(max_candidates=0),
            lambda r: r["execution"]["limit_sources"].update(unknown="request"),
        ]
        for mutate in mutations:
            report = empty_report()
            mutate(report)
            with self.subTest(report=report), self.assertRaises(ValueError):
                validate_report(report)

    def test_report_requires_every_diagnostic_field(self) -> None:
        for name in request_error_report()["execution"]["diagnostics"][0]:
            report = request_error_report()
            del report["execution"]["diagnostics"][0][name]
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate_report(report)


if __name__ == "__main__":
    unittest.main()
