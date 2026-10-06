#!/usr/bin/env python3
"""Run one sealed candidate E2E harness and emit its only JUnit transport.

This private executable accepts exactly the three argv members defined by the
E2E grammar.  The sealed environment supplies the candidate image and binds
those argv members to a single context phase; it is not a generic unittest
wrapper and cannot select another project, image, output, or runner.
"""

from __future__ import annotations

import argparse
import os
import sys
import time
import traceback
import unittest
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from release_e2e_context import ReleaseE2EContextError, ReleaseE2EHarness, load_release_e2e_context


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-directory", required=True)
    parser.add_argument("--pattern", required=True)
    parser.add_argument("--junit", required=True)
    return parser


@dataclass
class _Case:
    classname: str
    name: str
    elapsed: float
    kind: Literal["success", "failure", "error", "skipped", "expected_failure", "unexpected_success"]
    detail: str = ""


class _JUnitTestResult(unittest.TestResult):
    """A real ``unittest.TestResult`` that serializes every observed testcase."""

    def __init__(self) -> None:
        super().__init__()
        self._started: dict[int, tuple[str, str, float]] = {}
        self.cases: list[_Case] = []

    @staticmethod
    def _identity(test: unittest.case.TestCase) -> tuple[str, str]:
        identifier = test.id()
        module, dot, name = identifier.rpartition(".")
        return (module if dot else identifier, name if dot else identifier)

    def startTest(self, test: unittest.case.TestCase) -> None:  # noqa: N802 - unittest API
        super().startTest(test)
        classname, name = self._identity(test)
        self._started[id(test)] = (classname, name, time.monotonic())

    def _record(self, test: unittest.case.TestCase, kind: _Case.__annotations__["kind"], detail: str = "") -> None:
        started = self._started.pop(id(test), None)
        if started is None:
            classname, name, started_at = (*self._identity(test), time.monotonic())
        else:
            classname, name, started_at = started
        self.cases.append(_Case(classname, name, max(0.0, time.monotonic() - started_at), kind, detail))

    def addSuccess(self, test: unittest.case.TestCase) -> None:  # noqa: N802 - unittest API
        super().addSuccess(test)
        self._record(test, "success")

    def addFailure(self, test: unittest.case.TestCase, err: tuple[type[BaseException], BaseException, object]) -> None:  # noqa: N802
        super().addFailure(test, err)
        self._record(test, "failure", self._exc_info_to_string(err, test))

    def addError(self, test: unittest.case.TestCase, err: tuple[type[BaseException], BaseException, object]) -> None:  # noqa: N802
        super().addError(test, err)
        self._record(test, "error", self._exc_info_to_string(err, test))

    def addSkip(self, test: unittest.case.TestCase, reason: str) -> None:  # noqa: N802
        super().addSkip(test, reason)
        self._record(test, "skipped", reason)

    def addExpectedFailure(self, test: unittest.case.TestCase, err: tuple[type[BaseException], BaseException, object]) -> None:  # noqa: N802
        super().addExpectedFailure(test, err)
        self._record(test, "expected_failure", self._exc_info_to_string(err, test))

    def addUnexpectedSuccess(self, test: unittest.case.TestCase) -> None:  # noqa: N802
        super().addUnexpectedSuccess(test)
        self._record(test, "unexpected_success")


def _bound_harness(context, args: argparse.Namespace) -> ReleaseE2EHarness:
    source_root = Path(context.source_root)
    if Path.cwd().resolve() != source_root.resolve():
        raise ReleaseE2EContextError("driver working directory differs from the sealed source root")
    requested_start = (source_root / args.start_directory).resolve(strict=False)
    requested_junit = Path(args.junit).resolve(strict=False)
    for harness in context.fixed_harnesses:
        expected_start = (source_root / harness.start_directory).resolve(strict=False)
        expected_junit = Path(harness.junit_path).resolve(strict=False)
        if (args.pattern == harness.pattern and requested_start == expected_start and requested_junit == expected_junit):
            source = source_root / harness.source_path
            if source.is_symlink() or not source.is_file():
                raise ReleaseE2EContextError("sealed E2E harness source is absent or unsafe")
            return harness
    raise ReleaseE2EContextError("driver argv is not one fixed sealed E2E phase")


def _render_junit(result: _JUnitTestResult) -> bytes:
    failures = sum(case.kind in {"failure", "expected_failure", "unexpected_success"} for case in result.cases)
    errors = sum(case.kind == "error" for case in result.cases)
    skipped = sum(case.kind == "skipped" for case in result.cases)
    suite = ET.Element("testsuite", {
        "name": "caprmedio.release_e2e",
        "tests": str(len(result.cases)),
        "failures": str(failures),
        "errors": str(errors),
        "skipped": str(skipped),
    })
    for case in result.cases:
        node = ET.SubElement(suite, "testcase", {
            "classname": case.classname,
            "name": case.name,
            "time": f"{case.elapsed:.6f}",
        })
        if case.kind in {"failure", "expected_failure", "unexpected_success"}:
            child = ET.SubElement(node, "failure", {"type": case.kind})
            child.text = case.detail
        elif case.kind == "error":
            child = ET.SubElement(node, "error", {"type": "error"})
            child.text = case.detail
        elif case.kind == "skipped":
            child = ET.SubElement(node, "skipped")
            child.text = case.detail
    return b"<?xml version='1.0' encoding='utf-8'?>\n" + ET.tostring(suite, encoding="utf-8")


def _write_junit(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink() or path.exists():
        raise ReleaseE2EContextError("sealed JUnit output already exists or is unsafe")
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def _reject_duplicate_case_identities(result: _JUnitTestResult) -> bool:
    """Turn duplicate observed testcase identities into a terminal driver error.

    Preserve the observed rows, but mark the repeated occurrence as a driver
    error so the only JUnit transport is terminally non-passing.
    """

    seen: set[tuple[str, str]] = set()
    duplicates: list[tuple[str, str]] = []
    for case in result.cases:
        identity = (case.classname, case.name)
        if identity in seen:
            duplicates.append(identity)
            case.kind = "error"
            case.detail = f"duplicate observed testcase identity: {case.classname}.{case.name}"
        seen.add(identity)
    if not duplicates:
        return False
    return True


def main(argv) -> int:
    args = _parser().parse_args(argv)
    try:
        context = load_release_e2e_context()
        harness = _bound_harness(context, args)
    except ReleaseE2EContextError as error:
        print(f"release E2E context error: {error}", file=sys.stderr)
        return 2
    previous = {key: os.environ.get(key) for key, _value in harness.context_optins}
    try:
        for key, value in harness.context_optins:
            os.environ[key] = value
        suite = unittest.defaultTestLoader.discover(args.start_directory, pattern=args.pattern)
        result = _JUnitTestResult()
        suite.run(result)
    except BaseException:  # retain a JUnit error if unittest discovery itself fails
        result = _JUnitTestResult()
        pseudo = unittest.FunctionTestCase(lambda: None)
        result.startTest(pseudo)
        result.addError(pseudo, sys.exc_info())
    finally:
        for key, old_value in previous.items():
            if old_value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = old_value
    try:
        duplicate_case_identities = _reject_duplicate_case_identities(result)
        _write_junit(Path(args.junit), _render_junit(result))
    except (OSError, ReleaseE2EContextError) as error:
        print(f"release E2E JUnit error: {error}", file=sys.stderr)
        return 2
    successful = (
        result.testsRun > 0
        and not result.failures
        and not result.errors
        and not result.skipped
        and not result.expectedFailures
        and not result.unexpectedSuccesses
        and not duplicate_case_identities
    )
    return 0 if successful else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
