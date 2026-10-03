"""Independent CA-D-493@3 assertions; deliberately imports no validator code."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any
import unittest

JsonObject = dict[str, Any]


def _keys(test: unittest.TestCase, value: JsonObject, names: str) -> None:
    test.assertIsInstance(value, dict)
    test.assertEqual(set(value), set(names.split()))


def _integer(test: unittest.TestCase, value: Any, minimum: int = 0) -> None:
    test.assertIs(type(value), int)
    test.assertGreaterEqual(value, minimum)


def _binding(test: unittest.TestCase, value: JsonObject, atom: bool = False) -> None:
    test.assertIsInstance(value, dict)
    if atom:
        _keys(test, value, "atom_id version sha256 path")
        test.assertIsInstance(value["atom_id"], str)
        test.assertTrue(value["atom_id"])
        _integer(test, value["version"], 1)
    else:
        test.assertLessEqual(set(value), {"path", "sha256"})
        test.assertIn("path", value)
    test.assertTrue(Path(value["path"]).is_absolute())
    if "sha256" in value:
        test.assertRegex(value["sha256"], r"^[0-9a-f]{64}$")


def _diagnostic(test: unittest.TestCase, value: JsonObject) -> None:
    _keys(test, value, "code severity path span property authority reason evidence")
    for name in ("code", "reason"):
        test.assertIsInstance(value[name], str)
        test.assertTrue(value[name])
    test.assertIn(value["severity"], ("error", "warning", "info"))
    if value["path"] is not None:
        test.assertTrue(Path(value["path"]).is_absolute())
    for name in ("property", "evidence"):
        test.assertTrue(value[name] is None or isinstance(value[name], str))
    for item in value["authority"]:
        _binding(test, item, atom=True)
    if value["span"] is not None:
        span = value["span"]
        _keys(test, span, "start_line start_column end_line end_column")
        for part in span.values():
            _integer(test, part, 1)
        test.assertLessEqual(
            (span["start_line"], span["start_column"]), (span["end_line"], span["end_column"])
        )


def _bindings(test: unittest.TestCase, value: JsonObject) -> None:
    _keys(test, value, "methodology action rules context workflow step")
    for name in ("methodology", "rules"):
        for item in value[name]:
            _binding(test, item, atom=True)
    for item in value["context"]:
        _binding(test, item)
    for name in ("action", "workflow", "step"):
        if value[name] is not None:
            _binding(test, value[name], atom=True)


def _selection(test: unittest.TestCase, value: JsonObject) -> None:
    _keys(test, value, "requested source_roots selected excluded unresolved")
    for name in ("source_roots", "selected"):
        test.assertEqual(value[name], sorted(set(value[name])))
        for path in value[name]:
            test.assertTrue(Path(path).is_absolute())
    for name in ("excluded", "unresolved"):
        for item in value[name]:
            _keys(test, item, "path atom_id reason")


def _coverage(test: unittest.TestCase, value: JsonObject) -> None:
    _keys(test, value, "targets rules outcomes gaps")
    _keys(test, value["targets"], "selected assessed excluded unresolved")
    _keys(test, value["rules"], "required supported unsupported")
    _keys(test, value["outcomes"], "passed failed not_applicable not_checked")
    for name in ("targets", "rules", "outcomes"):
        for count in value[name].values():
            _integer(test, count)
    test.assertEqual(
        value["rules"]["required"], value["rules"]["supported"] + value["rules"]["unsupported"]
    )


def _diagnostic_groups(test: unittest.TestCase, report: JsonObject) -> None:
    groups = (report["findings"], report["coverage"]["gaps"], report["execution"]["diagnostics"])
    for group in groups:
        for item in group:
            _diagnostic(test, item)
        test.assertEqual(len(group), len({json.dumps(item, sort_keys=True) for item in group}))


def _carrier_outcomes(test: unittest.TestCase, report: JsonObject) -> None:
    counts = {name: 0 for name in report["coverage"]["outcomes"]}
    for carrier in report["carriers"]:
        _keys(test, carrier, "path atom_id version sha256 representation source_path outcomes")
        test.assertIn(carrier["representation"], ("source", "projected", "unresolved"))
        for outcome in carrier["outcomes"]:
            _keys(test, outcome, "code outcome authority reason finding_indexes")
            counts[outcome["outcome"]] += 1
            for item in outcome["authority"]:
                _binding(test, item, atom=True)
            for index in outcome["finding_indexes"]:
                _integer(test, index)
                test.assertLess(index, len(report["findings"]))
            if outcome["outcome"] == "failed":
                test.assertTrue(
                    any(
                        report["findings"][i]["severity"] == "error"
                        for i in outcome["finding_indexes"]
                    )
                )
    test.assertEqual(report["coverage"]["outcomes"], counts)


def _target_counts(test: unittest.TestCase, report: JsonObject) -> None:
    targets = report["coverage"]["targets"]
    for name in ("selected", "excluded", "unresolved"):
        test.assertEqual(targets[name], len(report["selection"][name]))
    test.assertEqual(targets["assessed"], sum(bool(c["outcomes"]) for c in report["carriers"]))


def _execution(test: unittest.TestCase, report: JsonObject) -> None:
    _keys(test, report["currentness"], "state affected_inputs")
    test.assertIn(report["currentness"]["state"], ("unchanged", "changed", "unverified"))
    for item in report["currentness"]["affected_inputs"]:
        _binding(test, item)
    _keys(test, report["execution"], "limits limit_sources stopped_by diagnostics run_context")
    test.assertEqual(set(report["execution"]["limits"]), set(report["execution"]["limit_sources"]))


def _valid_result(test: unittest.TestCase, report: JsonObject) -> None:
    if report["result"] != "valid":
        return
    coverage = report["coverage"]
    test.assertGreater(coverage["targets"]["selected"], 0)
    test.assertEqual(coverage["outcomes"]["failed"], 0)
    test.assertEqual(coverage["outcomes"]["not_checked"], 0)
    test.assertEqual(coverage["rules"]["unsupported"], 0)
    test.assertFalse(coverage["gaps"])
    test.assertFalse(report["selection"]["unresolved"])
    test.assertEqual(report["currentness"]["state"], "unchanged")


def assert_report_contract(test: unittest.TestCase, report: JsonObject) -> None:
    """Check the full independent golden contract without runtime model reuse."""
    _keys(
        test,
        report,
        "schema_version result bindings selection coverage carriers findings currentness execution",
    )
    test.assertIs(type(report["schema_version"]), int)
    test.assertEqual(report["schema_version"], 1)
    test.assertIn(report["result"], ("valid", "invalid", "incomplete", "error"))
    _bindings(test, report["bindings"])
    _selection(test, report["selection"])
    _coverage(test, report["coverage"])
    _diagnostic_groups(test, report)
    _carrier_outcomes(test, report)
    _target_counts(test, report)
    _execution(test, report)
    _valid_result(test, report)
