"""Opt-in query-specific proof against the exact selected Workflow image.

Run on the host with the declared MCP/orchestrator dependency groups and
CAPRMEDIO_DOCKER_QUERY_E2E=1. No worker-exec or alternate-driver fallback is
permitted. Skipped image cases are unfinished evidence, never a pass.
"""
from __future__ import annotations

import asyncio
from copy import deepcopy
import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from typing import Any

TESTS = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS))

import test_selected_workflows_docker_e2e as strict  # noqa: E402
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject  # noqa: E402

_IMMUTABLE_IMAGE = re.compile(r"sha256:[0-9a-f]{64}")
_MISSING = object()


def _required_query_image(environment: dict[str, str] | os._Environ[str]) -> str:
    """Return the opt-in query acceptance image, never a mutable fallback.

    Query acceptance is deliberately separate from normal development image
    selection.  An operator opts in only by supplying this exact immutable
    identity alongside ``CAPRMEDIO_DOCKER_QUERY_E2E=1``.
    """
    value = environment.get("CAPRMEDIO_DOCKER_QUERY_IMAGE")
    if not isinstance(value, str) or not _IMMUTABLE_IMAGE.fullmatch(value):
        raise AssertionError(
            "CAPRMEDIO_DOCKER_QUERY_IMAGE must name one immutable sha256 image ID "
            "for query acceptance"
        )
    return value


def _projection_fingerprint(root: Path) -> dict[str, str]:
    """Include the canonical Projection root, directories and every file byte.

    An absent root differs from an empty root. Journal/Run recording lives
    outside this boundary and remains governed by the existing recorder checks.
    """
    projection = root / ".caprmedio_caprmedio/_projection"
    if projection.parent.is_symlink():
        raise AssertionError("query Projection control root may not be a symbolic link")
    if projection.is_symlink():
        raise AssertionError("query Projection boundary may not be a symbolic link")
    if not projection.exists():
        return {}
    if not projection.is_dir():
        raise AssertionError("query Projection boundary must be a directory")
    fingerprint = {".": "directory"}
    for path in sorted(projection.rglob("*")):
        if path.is_symlink():
            raise AssertionError("query Projection boundary contains a symbolic link")
        relative = path.relative_to(projection).as_posix()
        if any(part == ".env" or part.startswith(".env.") or part.endswith(".env")
               for part in path.relative_to(projection).parts):
            raise AssertionError("unexpected environment file in query Projection boundary")
        if path.is_dir():
            fingerprint[relative] = "directory"
        elif path.is_file():
            fingerprint[relative] = "file:" + hashlib.sha256(path.read_bytes()).hexdigest()
        else:
            raise AssertionError("query Projection boundary contains a non-regular member")
    return fingerprint


def _assert_projection_unchanged(root: Path, before: dict[str, str]) -> None:
    if before != _projection_fingerprint(root):
        raise AssertionError("query must not create, delete or change canonical Project _projection")


class QueryProject(GoldenProject):
    """Choose native query inputs before preview; never rewrite a receipt."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.query_request: dict[str, Any] = {"limit": 100}

    def native_query_parameters(self, route: str) -> dict[str, Any]:
        if route != self.case.route or route not in {
            "find_and_fetch_artifacts", "find_and_fetch_journal_events"
        }:
            raise AssertionError("query fixture must retain its one selected route")
        return {"query_request": deepcopy(self.query_request)}


class QueryFixtureCarrierTests(unittest.TestCase):
    """Source-only carrier verification; no image or Run is invoked here."""

    def test_query_parameters_are_independent_copies_and_route_bound(self) -> None:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as directory:
            fixture = QueryProject(strict.ROOT, Path(directory),
                                   GoldenCase("W15", "find_and_fetch_journal_events"),
                                   execution_project_root="/project")
            chosen = {"mode": "fields", "select": ["event:/event"], "limit": 2,
                      "snapshot": {"snapshot_handle": "opaque"}, "cursor": "opaque-cursor"}
            fixture.query_request = deepcopy(chosen)
            first = fixture.native_query_parameters(fixture.case.route)
            first["query_request"]["snapshot"]["snapshot_handle"] = "changed-copy"
            self.assertEqual(chosen, fixture.native_query_parameters(fixture.case.route)["query_request"])
            self.assertEqual("/project", fixture.execution_project_root)
            with self.assertRaises(AssertionError):
                fixture.native_query_parameters("find_and_fetch_artifacts")

    def test_projection_guard_detects_creation_deletion_and_content_change(self) -> None:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as directory:
            root = Path(directory)
            projection = root / ".caprmedio_caprmedio/_projection"
            absent = _projection_fingerprint(root)
            projection.mkdir(parents=True)
            with self.assertRaisesRegex(AssertionError, "canonical Project _projection"):
                _assert_projection_unchanged(root, absent)
            empty = _projection_fingerprint(root)
            empty_child = projection / "empty"
            empty_child.mkdir()
            with self.assertRaisesRegex(AssertionError, "canonical Project _projection"):
                _assert_projection_unchanged(root, empty)
            member = projection / "selected_workflow_bindings.json"
            member.write_text('{"revision":1}', encoding="utf-8")
            first = _projection_fingerprint(root)
            _assert_projection_unchanged(root, first)
            member.write_text('{"revision":2}', encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "canonical Project _projection"):
                _assert_projection_unchanged(root, first)
            changed = _projection_fingerprint(root)
            member.unlink()
            with self.assertRaisesRegex(AssertionError, "canonical Project _projection"):
                _assert_projection_unchanged(root, changed)
            directories = _projection_fingerprint(root)
            empty_child.rmdir()
            with self.assertRaisesRegex(AssertionError, "canonical Project _projection"):
                _assert_projection_unchanged(root, directories)
            empty_root = _projection_fingerprint(root)
            projection.rmdir()
            with self.assertRaisesRegex(AssertionError, "canonical Project _projection"):
                _assert_projection_unchanged(root, empty_root)


class QueryProjectionBoundarySourceTests(unittest.IsolatedAsyncioTestCase):
    """Mock the transport only; exercise the real preview Projection guard."""

    async def test_preview_rejects_silent_projection_write_even_when_other_snapshots_match(self) -> None:
        from types import SimpleNamespace

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as directory:
            root = Path(directory)
            (root / ".caprmedio_caprmedio/_journal").mkdir(parents=True)
            projection = root / ".caprmedio_caprmedio/_projection"
            projection.mkdir()
            harness_case = SelectedQueryMcpEndToEnd("test_w14_fields_headings_closed_filter_and_retained_pagination")
            harness_case.fixture = SimpleNamespace(
                root=root, case=GoldenCase("W14", "find_and_fetch_artifacts"),
                request=lambda **_: {"parameters": {"query_request": {}}}, snapshot=lambda: {})
            harness_case.runtime = object()

            async def silent_projection_write(*_: Any) -> dict[str, Any]:
                (projection / "unrequested.json").write_text('{"published":true}', encoding="utf-8")
                return {"disposition": "preview", "proposal_receipt": {}, "proposal_receipt_digest": "sealed"}

            harness_case.harness = SimpleNamespace(
                _recording_snapshot=lambda _: {}, _call=silent_projection_write)
            with self.assertRaisesRegex(AssertionError, "canonical Project _projection"):
                await harness_case._preview("projection-write-source-check")


@unittest.skipUnless(
    os.environ.get("CAPRMEDIO_DOCKER_QUERY_E2E") == "1",
    "requires host declared dependencies and CAPRMEDIO_DOCKER_QUERY_E2E=1; unrun image evidence",
)
class SelectedQueryMcpEndToEnd(unittest.IsolatedAsyncioTestCase):
    """Happy queries and deliberate refusals have separate test methods."""

    async def asyncSetUp(self) -> None:
        self.harness = strict.SelectedWorkflowsDockerEndToEnd(
            "test_fresh_image_runtime_does_not_mount_host_implementation")
        self.runtime: strict.Runtime | None = None
        self.lease: FixtureLease | None = None
        self.launched = False
        self.query_image = _required_query_image(os.environ)
        observed = await asyncio.to_thread(
            subprocess.run, ["docker", "image", "inspect", "caprmedio-runtime:local", "--format", "{{.Id}}"],
            capture_output=True, text=True, timeout=20, check=False,
        )
        self.assertEqual(0, observed.returncode, "the admitted image must already exist")
        self.assertEqual(self.query_image, observed.stdout.strip(),
                         "query proof must bind the requested exact fresh image")
        self._previous_runtime_image = os.environ.get("CAPRMEDIO_IMAGE", _MISSING)
        os.environ["CAPRMEDIO_IMAGE"] = self.query_image

    async def asyncTearDown(self) -> None:
        try:
            if self.launched and self.runtime is not None:
                await self.harness._stop(self.runtime)
            if self.lease is not None:
                self.lease.cleanup()
        finally:
            if self._previous_runtime_image is _MISSING:
                os.environ.pop("CAPRMEDIO_IMAGE", None)
            else:
                os.environ["CAPRMEDIO_IMAGE"] = self._previous_runtime_image

    async def _start_fixture(self, case_id: str, route: str) -> QueryProject:
        parent = strict.ROOT / ".caprmedio_tmp/tests/selected-query-mcp-e2e"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        self.lease = FixtureLease(root)
        self.fixture = QueryProject(strict.ROOT, root, GoldenCase(case_id, route),
                                    execution_project_root="/project")
        self.fixture.prepare()
        self.runtime = strict.Runtime(root, mock=True)
        self.assertEqual(self.query_image, self.runtime.environment()["CAPRMEDIO_IMAGE"],
                         "query Runtime must receive the requested immutable image identity")
        self.launched = True
        await self.harness._start(self.runtime)
        return self.fixture

    async def _preview(self, request_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
        """Unlike an initial preview, a later query may observe actual prior facts."""
        fixture, runtime = self.fixture, self.runtime
        assert runtime is not None
        request = fixture.request(request_id=request_id)
        before = fixture.snapshot()
        projections = _projection_fingerprint(fixture.root)
        records = self.harness._recording_snapshot(fixture.root)
        self.assertTrue((fixture.root / ".caprmedio_caprmedio/_journal").is_dir())
        preview = await self.harness._call(runtime, fixture.root, fixture.case.route, request)
        self.assertEqual("preview", preview.get("disposition"), preview)
        self.assertIn("proposal_receipt", preview)
        self.assertIn("proposal_receipt_digest", preview)
        self.assertEqual(before, fixture.snapshot(), "query preview must not mutate sources")
        self.assertEqual(records, self.harness._recording_snapshot(fixture.root),
                         "query preview must not create or change any Journal/Run record")
        _assert_projection_unchanged(fixture.root, projections)
        return request, preview

    def _sealed_execution(self, request_id: str, request: dict[str, Any],
                          preview: dict[str, Any]) -> dict[str, Any]:
        execution = self.fixture.request(request_id=request_id, mode="execute",
                                         receipt=preview["proposal_receipt"],
                                         receipt_digest=preview["proposal_receipt_digest"])
        for field in ("parameters", "parameters_digest", "target_frontier", "target_frontier_digest",
                      "effects", "effects_digest", "definition_manifest", "source_freshness"):
            self.assertEqual(request[field], execution[field], f"sealed query input changed: {field}")
        return execution

    async def _execute(self, query: dict[str, Any], request_id: str, *, happy: bool = True) -> dict[str, Any]:
        fixture, runtime = self.fixture, self.runtime
        assert runtime is not None
        fixture.query_request = deepcopy(query)
        projections = _projection_fingerprint(fixture.root)
        request, preview = await self._preview(request_id)
        execute = self._sealed_execution(request_id, request, preview)
        before = fixture.snapshot()
        admitted = await self.harness._call(runtime, fixture.root, "workflow_orchestrator", {
            "operation": "enqueue_selected", "run_id": request_id, "execution": execute})
        self.assertIn(admitted.get("outcome"),
                      {"queued", "admitted", "started", "running", "pending", "completed", "failed"}, admitted)
        terminal = await self.harness._terminal_status(runtime, fixture.root, request_id)
        self.assertEqual("terminal", terminal.get("disposition"), terminal)
        graph = self.harness._graph_result(fixture.root, request_id)
        selected = terminal.get("selected_result")
        self.assertIsInstance(selected, dict, terminal)
        if happy:
            self.assertEqual("completed", terminal.get("outcome"), terminal)
            rows = self.harness._assert_graph_path_and_native_results(fixture.root, fixture, request_id, graph)
            self.harness._assert_shared_run_journal(
                fixture.root, request_id, self.harness._route_binding(fixture), selected, graph)
        else:
            self.assertIn(terminal.get("outcome"), {"failed", "interrupted_pending"}, terminal)
            rows = graph["step_results"]
            facts = [event for event in self.harness._events(fixture.root)
                     if event.get("llm_session", {}).get("uuid") == request_id]
            self.assertTrue(facts, "an invoked native refusal must retain actual Run evidence")
            self.assertTrue(any(event.get("event") in {"failed", "interrupted"} for event in facts), facts)
        self.assertEqual(before, fixture.snapshot(), "native queries must have no source effects")
        _assert_projection_unchanged(fixture.root, projections)
        self.assertEqual([], [effect for row in rows for effect in row["effect_refs"]])
        native = self.harness._action_progress(fixture.root, request_id, rows[0]["action_run_id"])["native_result"]
        self.assertIsInstance(native, dict, native)
        if fixture.case.case_id == "W15" and isinstance(native.get("snapshot"), dict):
            own = {event["event_id"] for event in self.harness._events(fixture.root)
                   if event.get("llm_session", {}).get("uuid") == request_id}
            self.assertTrue(own.isdisjoint(native["snapshot"].get("event_ids", [])), native)
        return native

    async def test_w14_fields_headings_closed_filter_and_retained_pagination(self) -> None:
        await self._start_fixture("W14", "find_and_fetch_artifacts")
        query = {"filter": '"fm:/atom_id" IN ("CA-R-100", "CA-R-101") AND '
                            '("fm:/atom_id" != "CA-R-100" OR NOT ("fm:/atom_id" = "CA-R-101"))',
                 "select": ["fm:/version", "fm:/status", "section:/1:Summary/2:Scope"], "limit": 1}
        first = await self._execute(query, "query-w14-first")
        self.assertEqual([{"artifact_id": "CA-R-100", "fm:/version": 1, "fm:/status": "Active",
                           "section:/1:Summary/2:Scope": "\nFixture scope.\n\n"}], first["results"])
        self.assertTrue(first["has_more"])
        self.assertTrue(first["coverage"]["complete"])
        self.assertEqual(2, first["coverage"]["matched_count"])
        self.assertEqual({"complete": True, "incomplete": False, "findings": []}, first["diagnostics"])
        second = await self._execute({**query, "snapshot": first["snapshot"], "cursor": first["next_cursor"]},
                                     "query-w14-continuation")
        self.assertEqual([{"artifact_id": "CA-R-101", "fm:/version": 1, "fm:/status": "Active",
                           "section:/1:Summary/2:Scope": "\nFixture scope.\n\n"}], second["results"])
        self.assertEqual(first["snapshot"], second["snapshot"])
        self.assertFalse(second["has_more"])
        self.assertIsNone(second["next_cursor"])

    async def test_w15_actual_facts_fields_filter_and_worker_retained_snapshot(self) -> None:
        fixture = await self._start_fixture("W15", "find_and_fetch_journal_events")
        self.assertEqual([], self.harness._events(fixture.root), "seed facts must come from the actual first Run")
        seed = await self._execute({"limit": 100}, "query-w15-seed")
        self.assertEqual([], seed["results"])
        self.assertEqual([], seed["snapshot"]["event_ids"])
        seed_facts = self.harness._events(fixture.root)
        self.assertEqual(6, len(seed_facts))
        expected = [{"event_id": event["event_id"], "event:/event": "completed",
                     "event:/run/definition/atom_id": event["run"]["definition"]["atom_id"],
                     "event:/outcome": "completed"}
                    for event in sorted(seed_facts, key=lambda row: row["event_id"].encode())
                    if event["event"] == "completed"]
        query = {"filter": '"event:/llm_session/uuid" IN ("query-w15-seed") AND '
                            '"event:/event" != "started" AND '
                            '("event:/run/definition/atom_id" = "CA-O-161" OR '
                            'NOT ("event:/run/definition/atom_id" = "CA-O-161"))',
                 "mode": "fields", "select": ["event:/event", "event:/run/definition/atom_id", "event:/outcome"],
                 "limit": 2}
        first = await self._execute(query, "query-w15-first")
        self.assertEqual(expected[:2], first["results"])
        self.assertEqual("incomplete", first["status"])
        self.assertEqual({"scanned": 6, "matched": 3, "returned": 2, "complete": False}, first["coverage"])
        self.assertEqual({event["event_id"] for event in seed_facts}, set(first["snapshot"]["event_ids"]))
        self.assertTrue(first["snapshot"]["snapshot_handle"])
        second = await self._execute({**query, "snapshot": first["snapshot"], "cursor": first["next_cursor"]},
                                     "query-w15-continuation")
        self.assertEqual(expected[2:], second["results"])
        self.assertEqual("complete", second["status"])
        self.assertEqual(first["snapshot"], second["snapshot"])
        self.assertEqual({"scanned": 6, "matched": 3, "returned": 1, "complete": True}, second["coverage"])
        self.assertEqual([], second["findings"])
        self.assertIsNone(second["next_cursor"])
        self.assertTrue(all(row["configured"] > 0 and row["source"] in {"default", "instance", "request", "snapshot"}
                            for row in second["limits"].values()))

    async def test_w14_expected_secret_and_mutation_refusals(self) -> None:
        await self._start_fixture("W14", "find_and_fetch_artifacts")
        secret = await self._execute({"select": ["fm:/token"], "limit": 1}, "query-w14-secret", happy=False)
        self.assertEqual("invalid", secret["status"])
        self.assertEqual([], secret["results"])
        self.assertIn("secret-shaped selector", secret["findings"][0]["code"])
        self.fixture.query_request = {"mutation": {"write": "forbidden"}}
        projections = _projection_fingerprint(self.fixture.root)
        request, preview = await self._preview("query-w14-mutation")
        execute = self._sealed_execution("query-w14-mutation", request, preview)
        before = self.harness._recording_snapshot(self.fixture.root)
        assert self.runtime is not None
        with self.assertRaisesRegex(AssertionError, "MCP Tool returned an error"):
            await self.harness._call(self.runtime, self.fixture.root, "workflow_orchestrator", {
                "operation": "enqueue_selected", "run_id": "query-w14-mutation", "execution": execute})
        self.assertEqual(before, self.harness._recording_snapshot(self.fixture.root),
                         "unsupported mutation must be refused before any Run record")
        _assert_projection_unchanged(self.fixture.root, projections)
        query = {"filter": '"fm:/atom_id" IN ("CA-R-100", "CA-R-101")', "limit": 1}
        retained = await self._execute(query, "query-w14-retained-prerequisite")
        altered = deepcopy(retained["snapshot"])
        altered["digest"] = "0" * 64
        tampered = await self._execute({**query, "snapshot": altered, "cursor": retained["next_cursor"]},
                                       "query-w14-altered-snapshot", happy=False)
        self.assertEqual("invalid", tampered["status"])
        self.assertEqual([], tampered["results"])
        self.assertIn("tampered retained snapshot", tampered["findings"][0]["code"])

    async def test_w15_expected_protected_selector_and_limit_diagnostics(self) -> None:
        await self._start_fixture("W15", "find_and_fetch_journal_events")
        protected = await self._execute({"mode": "fields", "select": ["event:/details/api_key"], "limit": 1},
                                        "query-w15-protected", happy=False)
        self.assertEqual("invalid", protected["status"])
        self.assertEqual([], protected["results"])
        self.assertEqual("protected-selector", protected["findings"][0]["code"])
        limited = await self._execute({"limit": 2, "limits": {"max_page_size": 1}},
                                      "query-w15-limit", happy=False)
        self.assertEqual("invalid", limited["status"])
        self.assertEqual("page-limit-exceeded", limited["findings"][0]["code"])
        self.assertEqual(1, limited["limits"]["max_page_size"]["configured"])
        self.assertEqual("request", limited["limits"]["max_page_size"]["source"])
        self.assertTrue(limited["limits"]["max_page_size"]["exhausted"])
        self.assertEqual([], limited["results"])
        retained = await self._execute({"limit": 1}, "query-w15-retained-prerequisite")
        self.assertTrue(retained["next_cursor"])
        altered = deepcopy(retained["snapshot"])
        altered["prefix_digest"] = "0" * 64
        tampered = await self._execute({"limit": 1, "snapshot": altered, "cursor": retained["next_cursor"]},
                                       "query-w15-altered-snapshot", happy=False)
        self.assertEqual("invalid", tampered["status"])
        self.assertEqual("changed-snapshot", tampered["findings"][0]["code"])
        self.assertEqual([], tampered["results"])


if __name__ == "__main__":
    unittest.main()
