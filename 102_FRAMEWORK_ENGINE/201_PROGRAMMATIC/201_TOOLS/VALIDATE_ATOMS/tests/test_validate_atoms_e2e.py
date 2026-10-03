"""Source-authored golden reports exercised through the real public command.

No validator modules are imported here. /__fixture__/ in static JSON is only
an absolute-path placeholder relocated before subprocess invocation.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any
import unittest

from golden_fixtures import (
    copy_fixtures,
    fingerprint,
    fixture_path,
    isolated_directory,
    no_duplicate_keys,
    read_json,
)
from golden_support import assert_report_contract

HERE = Path(__file__).resolve().parent
COMMAND = HERE.parent / "validate_atoms.py"
PLACEHOLDER = "/__fixture__"


MANIFEST = read_json(HERE / "cases.json")


class GoldenCorpus(unittest.TestCase):
    maxDiff = 12000

    def test_public_executable_exists(self) -> None:
        self.assertTrue(COMMAND.is_file(), f"Missing delivered executable: {COMMAND}")

    def test_manifest_and_expected_reports(self) -> None:
        self.assertEqual(set(MANIFEST), {"schema_version", "cases"})
        self.assertEqual(MANIFEST["schema_version"], 1)
        self.assertTrue(MANIFEST["cases"])
        ids: set[str] = set()
        for case in MANIFEST["cases"]:
            with self.subTest(case=case["case_id"]):
                self.assertEqual(
                    set(case),
                    {
                        "case_id",
                        "request",
                        "fixture_paths",
                        "authority",
                        "check_codes",
                        "expected_report",
                        "expected_exit_code",
                    },
                )
                self.assertNotIn(case["case_id"], ids)
                ids.add(case["case_id"])
                self.assertTrue(case["authority"])
                self.assertTrue(case["fixture_paths"])
                self.assertTrue(case["check_codes"])
                fixture_path(case["request"]).read_bytes()
                for path in case["fixture_paths"]:
                    self.assertTrue(fixture_path(path).exists(), path)
                expected = read_json(fixture_path(case["expected_report"]))
                assert_report_contract(self, expected)
                self.assertEqual(
                    case["expected_exit_code"],
                    {"valid": 0, "invalid": 1, "incomplete": 2, "error": 3}[expected["result"]],
                )

    def test_authority_copies_are_exact(self) -> None:
        for item in read_json(HERE / "source_bindings.json"):
            with self.subTest(authority=item["atom_id"]):
                actual = hashlib.sha256(fixture_path(item["fixture_path"]).read_bytes()).hexdigest()
                self.assertEqual(
                    actual, item["sha256"], "fixture bytes diverged from reviewed source binding"
                )

    def run_case(self, case: dict[str, Any]) -> None:
        with isolated_directory() as directory:
            root = Path(directory) / "fixture"
            root.mkdir()
            copy_fixtures(case["fixture_paths"], root)
            request = (
                fixture_path(case["request"])
                .read_text(encoding="utf-8")
                .replace(PLACEHOLDER, str(root))
            )
            expected = json.loads(
                fixture_path(case["expected_report"])
                .read_text(encoding="utf-8")
                .replace(PLACEHOLDER, str(root)),
                object_pairs_hook=no_duplicate_keys,
            )
            request_file = Path(directory) / "request.json"
            request_file.write_text(request, encoding="utf-8")
            before = fingerprint(Path(directory))
            reports = []
            for input_arg in (str(request_file), "-"):
                completed = subprocess.run(
                    [sys.executable, str(COMMAND), "--input", input_arg],
                    input=request if input_arg == "-" else None,
                    text=True,
                    capture_output=True,
                    cwd=directory,
                    env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
                    timeout=45,
                )
                self.assertEqual(
                    fingerprint(Path(directory)), before, "validator mutated fixture tree"
                )
                self.assertEqual(completed.returncode, case["expected_exit_code"], completed.stderr)
                try:
                    report = json.loads(completed.stdout, object_pairs_hook=no_duplicate_keys)
                except (ValueError, TypeError) as error:
                    self.fail(
                        f"stdout must contain exactly one JSON report: {error}; {completed.stdout!r}"
                    )
                assert_report_contract(self, report)
                self.assertEqual(report, expected)
                reports.append(report)
            self.assertEqual(reports[0], reports[1], "file and stdin calls differ")


def attach_case(case: dict[str, Any]) -> None:
    def test(self: GoldenCorpus) -> None:
        self.run_case(case)

    test.__name__ = "test_e2e_" + case["case_id"]
    setattr(GoldenCorpus, test.__name__, test)


for _case in MANIFEST["cases"]:
    attach_case(_case)


if __name__ == "__main__":
    unittest.main()
