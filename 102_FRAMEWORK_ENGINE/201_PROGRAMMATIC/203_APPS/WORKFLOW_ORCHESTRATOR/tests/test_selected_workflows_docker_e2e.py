"""Selected W01--W15 Docker/MCP golden evidence harness.

This is intentionally an opt-in Docker suite.  With ``CAPRMEDIO_DOCKER_E2E=1``
it fails on an absent route manifest, MCP registration, shared-run integration,
or functional evidence; it never turns any of those states into a skip/pass.
The existing Base Revise Docker tests remain a separate regression suite.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import unittest
from typing import Any, Mapping


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
sys.path.insert(0, str(APP / "docker"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
RELEASE_ROOT = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION"
sys.path.insert(0, str(RELEASE_ROOT))

from runtime import Runtime  # noqa: E402
from release_e2e_context import load_release_e2e_context  # noqa: E402
from selected_workflows_docker_fixture import (  # noqa: E402
    GoldenCase,
    GoldenCorpusError,
    GoldenProject,
    FixtureLease,
    JOURNAL_CASES,
    ROUTE_CASES,
    STATUS_DOMAINS,
)

try:
    E2E_CONTEXT = load_release_e2e_context(os.environ)
except Exception:
    E2E_CONTEXT = None


def _structured_tool_result(response: Any) -> dict[str, Any]:
    """Unwrap the installed MCP 2.3 result without inferring JSON from text."""
    if response.is_error:
        raise AssertionError(f"MCP Tool returned an error: {response}")
    if response.result_type != "complete":
        raise AssertionError(f"MCP Tool returned an incomplete result: {response}")
    value = response.structured_content
    if not isinstance(value, dict):
        raise AssertionError(f"MCP Tool did not return a structured object: {response}")
    return value


async def _stdio_tool_call(parameters: Any, tool: str, request: dict[str, Any]) -> dict[str, Any]:
    """One uncached MCP 2.3 stdio connection and handshake for one Tool call."""
    from mcp import Client

    async with Client(parameters, cache=None, read_timeout_seconds=20) as client:
        response = await client.call_tool(tool, {"request": request})
    return _structured_tool_result(response)


@unittest.skipUnless(
    os.environ.get("CAPRMEDIO_DOCKER_E2E") == "1" and E2E_CONTEXT is not None,
    "requires CAPRMEDIO_DOCKER_E2E=1 and sealed Release E2E context",
)
class SelectedWorkflowsDockerEndToEnd(unittest.IsolatedAsyncioTestCase):
    """One runtime and one disposable Git Project per source-bound route."""

    async def _call(self, runtime: Runtime, root: Path, tool: str, request: dict) -> dict:
        """Use a new stdio MCP client per call to prove reconnect persistence."""
        try:
            from mcp import StdioServerParameters
        except ImportError as error:  # exact command must use the declared MCP group
            self.fail(f"Docker/MCP harness dependency is unavailable: {error}")
        parameters = StdioServerParameters(
            command=sys.executable,
            args=[str(APP / "docker/runtime.py"), "--project-root", str(root), "--image",
                  E2E_CONTEXT.candidate_image_digest, "--mock", "mcp"],
        )
        self.assertEqual(runtime.root, root.resolve(strict=True), "MCP runtime must bind the same fixture")
        return await _stdio_tool_call(parameters, tool, request)

    async def _start(self, runtime: Runtime) -> None:
        try:
            started = await asyncio.to_thread(runtime.start)
        except RuntimeError as error:
            self.fail(f"mock Docker runtime did not start: {error}")
        self.assertEqual("ready", started.get("outcome"), started)
        self.assertEqual("mock", started.get("agent_mode"), started)

    async def _stop(self, runtime: Runtime) -> None:
        await asyncio.to_thread(runtime.call, "down", "--volumes", timeout=60)

    def _new_fixture(self, case: GoldenCase) -> tuple[FixtureLease, Path, GoldenProject]:
        parent = E2E_CONTEXT.scratch_root / "selected-workflows-docker-e2e"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        fixture = GoldenProject(ROOT, root, case, execution_project_root="/project")
        return FixtureLease(root), root, fixture

    @staticmethod
    def _runtime(root: Path) -> Runtime:
        return Runtime(root, mock=True, image=E2E_CONTEXT.candidate_image_digest)

    async def _preview(self, runtime: Runtime, root: Path, fixture: GoldenProject,
                       request_id: str) -> dict:
        # Input preparation belongs to the disposable fixture, not the MCP
        # preview. Seal the complete request before observing that boundary.
        request = fixture.request(request_id=request_id)
        before = fixture.snapshot()
        journal = root / ".caprmedio_caprmedio/_journal"
        self.assertTrue(journal.is_dir(), "preview requires the valid canonical Journal")
        records_before = self._recording_snapshot(root)
        initial_events = self._events(root)
        if fixture.case.case_id == "W03":
            self.assertEqual(["golden-w03-predecessor"], [event.get("event_id") for event in initial_events])
            self.assertTrue(all(event.get("schema_version") != 5 for event in initial_events), initial_events)
        else:
            self.assertEqual([], initial_events, "preview fixture must contain no fabricated Run events")
        result = await self._call(runtime, root, fixture.case.route, request)
        self.assertEqual("preview", result.get("disposition"), result)
        self.assertIn("proposal_receipt", result, result)
        self.assertIn("proposal_receipt_digest", result, result)
        self.assertEqual(before, fixture.snapshot(), "a preview must not mutate admitted authority")
        self.assertEqual(records_before, self._recording_snapshot(root), "preview must not write Journal or Run records")
        self.assertEqual(initial_events, self._events(root), "preview must preserve initial Journal evidence")
        return result

    @staticmethod
    def _recording_snapshot(root: Path) -> dict[str, str]:
        """Observe canonical Journal and selected/shared recorder files only."""
        roots = [root / ".caprmedio_caprmedio/_journal", root / ".caprmedio_runtime",
                 root / ".caprmedio_install/workflow_orchestrator/runs"]
        snapshot = {}
        for directory in roots:
            for path in directory.rglob("*"):
                if path.is_symlink():
                    raise AssertionError("preview recording boundary contains a symbolic link")
                if not path.is_file():
                    continue
                if path.name == ".env" or path.name.startswith(".env.") or path.name.endswith(".env"):
                    raise AssertionError("unexpected environment file in disposable recording boundary")
                snapshot[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        return snapshot

    async def _terminal_status(self, runtime: Runtime, root: Path, run_id: str) -> dict:
        """Reconnect after enqueue; an acknowledgement is not terminal evidence."""
        deadline = time.monotonic() + 75
        pending = {"queued", "admitted", "started", "running", "pending"}
        observed: dict = {}
        while time.monotonic() < deadline:
            observed = await self._call(
                runtime, root, "workflow_orchestrator", {"operation": "status", "run_id": run_id}
            )
            if observed.get("outcome") not in pending:
                return observed
            await asyncio.sleep(0.25)
        self.fail(f"selected Workflow did not reach a truthful terminal state: {observed}")

    async def _execute_status_case(
        self, runtime: Runtime, root: Path, fixture: GoldenProject, path: Path,
        status: str, request_id: str,
    ) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
        """Exercise W04 through preview, selected enqueue, and reconnect status."""
        preview = await self._call(
            runtime, root, fixture.case.route,
            fixture.request_for_status(path, status, request_id=request_id),
        )
        self.assertEqual("preview", preview.get("disposition"), preview)
        execute = fixture.request_for_status(
            path, status, request_id=request_id, mode="execute",
            receipt=preview["proposal_receipt"], receipt_digest=preview["proposal_receipt_digest"],
        )
        admitted = await self._call(
            runtime, root, "workflow_orchestrator",
            {"operation": "enqueue_selected", "run_id": request_id, "execution": execute},
        )
        self.assertIn(admitted.get("outcome"), {"queued", "admitted", "started", "running", "pending", "completed"}, admitted)
        terminal = await self._terminal_status(runtime, root, request_id)
        self.assertEqual("terminal", terminal.get("disposition"), terminal)
        self.assertEqual("completed", terminal.get("outcome"), terminal)
        selected = terminal.get("selected_result")
        self.assertIsInstance(selected, dict, terminal)
        graph = self._graph_result(root, request_id)
        rows = self._assert_graph_path_and_native_results(root, fixture, request_id, graph)
        self._assert_shared_run_journal(root, request_id, self._route_binding(fixture), selected, graph)
        native = self._action_progress(root, request_id, rows[-1]["action_run_id"]).get("native_result")
        self.assertIsInstance(native, dict, native)
        return native, graph, selected

    @staticmethod
    def _read_json(path: Path, *, label: str) -> dict[str, Any]:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise AssertionError(f"{label} is absent or not JSON: {path}") from error
        if not isinstance(value, dict):
            raise AssertionError(f"{label} must be a JSON object: {path}")
        return value

    @staticmethod
    def _safe_existing_ref(root: Path, reference: object, *, label: str) -> Path:
        if not isinstance(reference, str) or not reference:
            raise AssertionError(f"{label} must be a non-empty repository-relative reference: {reference!r}")
        relative = Path(reference)
        if relative.is_absolute() or ".." in relative.parts:
            raise AssertionError(f"{label} escapes the disposable Project: {reference!r}")
        path = root / relative
        if not path.is_file():
            raise AssertionError(f"{label} does not name an existing file: {reference!r}")
        return path

    @staticmethod
    def _route_binding(fixture: GoldenProject) -> dict[str, Any]:
        if fixture.manifest is None:
            raise AssertionError("the golden fixture has no frozen manifest")
        route = next((row for row in fixture.manifest["routes"] if row.get("route") == fixture.case.route), None)
        if not isinstance(route, dict):
            raise AssertionError(f"the frozen manifest has no binding for {fixture.case.route}")
        return route

    def _graph_result(self, root: Path, run_id: str) -> dict[str, Any]:
        return self._read_json(
            root / ".caprmedio_install/workflow_orchestrator/runs" / run_id / "graph_result.json",
            label="selected graph result",
        )

    def _action_progress(self, root: Path, run_id: str, action_run_id: object) -> dict[str, Any]:
        if not isinstance(action_run_id, str):
            raise AssertionError(f"selected action run identity is invalid: {action_run_id!r}")
        return self._read_json(
            root / ".caprmedio_install/workflow_orchestrator/runs" / run_id / f"{action_run_id}.json",
            label="native Action progress",
        )

    def _assert_shared_run_journal(
        self,
        root: Path,
        request_id: str,
        route: Mapping[str, Any],
        selected: Mapping[str, Any],
        graph: Mapping[str, Any],
    ) -> None:
        """Bind J01--J08 to actual per-Run records, never marker presence."""
        rows = graph.get("step_results")
        self.assertIsInstance(rows, list, graph)
        self.assertTrue(rows, graph)
        expected_run_ids = [request_id]
        expected_definitions: dict[str, Mapping[str, Any]] = {request_id: route["workflow"]}
        expected_parent: dict[str, str | None] = {request_id: None}
        route_steps = {item["step"]["atom_id"]: item for item in route["ordered_steps"]}
        for row in rows:
            self.assertIsInstance(row, dict, row)
            step_id = row.get("step_definition_id")
            action_id = row.get("action_definition_id")
            self.assertIn(step_id, route_steps, row)
            binding = route_steps[step_id]
            self.assertEqual(binding["action"]["atom_id"], action_id, row)
            step_run_id = row.get("step_run_id")
            action_run_id = row.get("action_run_id")
            self.assertIsInstance(step_run_id, str, row)
            self.assertIsInstance(action_run_id, str, row)
            expected_run_ids.extend((step_run_id, action_run_id))
            expected_definitions[step_run_id] = binding["step"]
            expected_definitions[action_run_id] = binding["action"]
            expected_parent[step_run_id] = request_id
            expected_parent[action_run_id] = step_run_id
            if route.get("route") == "replace_atom" and action_id == "CA-O-128":
                replacements = [
                    item for item in route.get("native_action_calls", [])
                    if isinstance(item, Mapping) and item.get("atom_id") == "CA-O-051"
                ]
                self.assertEqual(1, len(replacements), route)
                child_run_id = f"{action_run_id}:nested:CA-O-051"
                expected_run_ids.append(child_run_id)
                expected_definitions[child_run_id] = replacements[0]
                expected_parent[child_run_id] = action_run_id
            if route.get("route") == "create_atom" and action_id == "CA-O-128":
                creations = [
                    item for item in route.get("native_action_calls", [])
                    if isinstance(item, Mapping) and item.get("atom_id") == "CA-O-032"
                ]
                self.assertEqual(1, len(creations), route)
                child_run_id = f"{action_run_id}:nested:CA-O-032"
                expected_run_ids.append(child_run_id)
                expected_definitions[child_run_id] = creations[0]
                expected_parent[child_run_id] = action_run_id

        # J01: the retained selected result must be a clean terminal receipt,
        # not the outer DBOS acknowledgement returned by enqueue_selected.
        self.assertEqual("terminal", selected.get("disposition"), selected)
        terminals = selected.get("terminal_runs")
        self.assertIsInstance(terminals, list, selected)
        workflow_terminals = [row for row in terminals if row.get("run_id") == request_id]
        self.assertEqual(1, len(workflow_terminals), terminals)
        self.assertEqual("completed", workflow_terminals[0].get("outcome"), workflow_terminals[0])
        self.assertEqual(expected_run_ids, selected.get("run_ids"), selected)
        self.assertEqual(len(expected_run_ids), len(terminals), terminals)
        terminal_by_run_id = {row.get("run_id"): row for row in terminals}
        self.assertEqual(set(expected_run_ids), set(terminal_by_run_id), terminals)

        # J02/J03: every actual Workflow/Step/Action has exactly one start and
        # one successful terminal fact.  Interrupted/failed facts cannot be a
        # happy-path substitute.
        events = [
            event for event in self._events(root)
            if event.get("schema_version") == 5 and event.get("kind") == "workflow_execution"
            and event.get("llm_session", {}).get("uuid") == request_id
        ]
        self.assertEqual(2 * len(expected_run_ids), len(events), events)
        self.assertEqual(len({event.get("event_id") for event in events}), len(events), events)
        self.assertTrue(all(event.get("schema_version") == 5 for event in events), events)
        self.assertTrue(all(event.get("event") not in {"failed", "interrupted", "abandoned"} for event in events), events)
        for run_id in expected_run_ids:
            facts = [event for event in events if event.get("run", {}).get("run_id") == run_id]
            self.assertEqual(["started", "completed"], [event.get("event") for event in facts], facts)
            self.assertIsNone(facts[0].get("outcome"), facts[0])
            self.assertEqual("completed", facts[1].get("outcome"), facts[1])

            # J04/J05: source-bound definition and parent identities on both
            # facts must match the frozen manifest, not merely a similarly named Run.
            for event in facts:
                definition = event["run"].get("definition")
                pinned = expected_definitions[run_id]
                self.assertEqual(
                    {"atom_id": pinned["atom_id"], "version": pinned["version"],
                     "path": pinned["source_path"], "digest": pinned["digest"]},
                    definition,
                    event,
                )
                parent = expected_parent[run_id]
                if parent is None:
                    self.assertNotIn("parent_run_id", event["run"], event)
                else:
                    self.assertEqual(parent, event["run"].get("parent_run_id"), event)

        if route.get("route") == "replace_atom":
            replacement_events = [
                event for event in self._events(root)
                if event.get("schema_version") == 3
                and event.get("event_id") == f"selected-replacement:{request_id}:step:1:action:1:nested:CA-O-051"
            ]
            self.assertEqual(1, len(replacement_events), replacement_events)
            replacement = replacement_events[0]
            self.assertEqual("golden-w03-predecessor", replacement.get("previous_result_event"), replacement)
            self.assertEqual("CA-R-100", replacement.get("predecessor_atom_id"), replacement)
            self.assertEqual(["CA-R-103"], replacement.get("successor_atom_ids"), replacement)
            self._safe_existing_ref(root, replacement.get("result", {}).get("path"), label="replacement archive")

        # J06/J07/J08: status's terminal records and Journal evidence agree on
        # clean outcome and actual retained result/effect references.
        for run_id in expected_run_ids:
            terminal = terminal_by_run_id[run_id]
            self.assertEqual("terminal", terminal.get("disposition"), terminal)
            self.assertEqual("completed", terminal.get("outcome"), terminal)
            self._safe_existing_ref(root, terminal.get("result_ref"), label="terminal result")
            effects = terminal.get("effect_refs")
            self.assertIsInstance(effects, list, terminal)
            for effect in effects:
                self._safe_existing_ref(root, effect, label="terminal effect")

    def _assert_graph_path_and_native_results(
        self,
        root: Path,
        fixture: GoldenProject,
        request_id: str,
        graph: Mapping[str, Any],
    ) -> list[dict[str, Any]]:
        route = self._route_binding(fixture)
        self.assertEqual("completed", graph.get("outcome"), graph)
        self.assertEqual(request_id, graph.get("workflow_run_id"), graph)
        self.assertEqual(route["workflow"]["atom_id"], graph.get("workflow_definition_id"), graph)
        rows = graph.get("step_results")
        self.assertIsInstance(rows, list, graph)
        self.assertTrue(rows, graph)
        steps = {item["step"]["atom_id"]: item for item in route["ordered_steps"]}
        self.assertEqual(route["entry_step"], rows[0].get("step_definition_id"), rows)
        for index, row in enumerate(rows):
            self.assertIsInstance(row, dict, row)
            step_id = row.get("step_definition_id")
            self.assertIn(step_id, steps, row)
            bound = steps[step_id]
            self.assertEqual(bound["action"]["atom_id"], row.get("action_definition_id"), row)
            ordinal = next(
                ordinal for ordinal, item in enumerate(route["ordered_steps"], start=1)
                if item["step"]["atom_id"] == step_id
            )
            expected_step = f"{request_id}:step:{ordinal}"
            actual_step = row.get("step_run_id")
            self.assertTrue(
                actual_step == expected_step or (
                    isinstance(actual_step, str) and actual_step.startswith(expected_step + ":visit:")
                ),
                row,
            )
            self.assertEqual(f"{actual_step}:action:1", row.get("action_run_id"), row)
            self.assertIsInstance(row.get("result"), str, row)
            self.assertIsInstance(row.get("effect_refs"), list, row)
            for effect in row["effect_refs"]:
                self._safe_existing_ref(root, effect, label="native Action effect")
            if index:
                previous = rows[index - 1]
                admissible = {
                    transition["to"] for transition in route["on_result"]
                    if transition["from"] == previous["step_definition_id"]
                    and transition["condition"] == previous["result"]
                }
                self.assertIn(step_id, admissible, {"previous": previous, "current": row, "route": route})

            progress = self._action_progress(root, request_id, row["action_run_id"])
            self.assertEqual(row["action_run_id"], progress.get("action_run_id"), progress)
            self.assertEqual(row["result"], progress.get("result"), progress)
            if fixture.case.case_id not in {"W11", "W12"}:
                self.assertIsInstance(progress.get("native_result"), dict, progress)
        return rows

    def _assert_route_specific_effects(
        self,
        root: Path,
        fixture: GoldenProject,
        execute: Mapping[str, Any],
        before: Mapping[str, str],
        rows: list[dict[str, Any]],
    ) -> None:
        case_id = fixture.case.case_id
        effects = sorted({effect for row in rows for effect in row["effect_refs"]})
        if case_id in {"W01", "W02", "W03", "W04", "W05", "W06", "W07", "W08"}:
            self.assertTrue(effects, rows)
            self.assertNotEqual(before, fixture.snapshot(), "a native authority success must alter admitted state")
            if case_id in {"W01", "W02", "W03", "W04"}:
                native = self._action_progress(root, execute["request_id"], rows[-1]["action_run_id"]).get("native_result")
                self.assertIsInstance(native, dict, native)
                self.assertEqual("applied", native.get("outcome"), native)
                self.assertTrue(native.get("effects"), native)
        elif case_id == "W09":
            retained = execute["parameters"]["base_packet"]["retained_state"]
            self.assertEqual("mock-not-live-llm", retained.get("transport"), retained)
            native = self._action_progress(root, execute["request_id"], rows[2]["action_run_id"]).get("native_result")
            self.assertIsInstance(native, dict, native)
            self.assertIn(
                "mock-not-live-llm",
                json.dumps(native, sort_keys=True),
                "W09 evidence must say mock-not-live-llm; it is not live Agent proof",
            )
        elif case_id == "W10":
            self.assertTrue(effects, rows)
        elif case_id in {"W11", "W12"}:
            self.assertTrue(effects, rows)
            for effect in effects:
                payload = self._safe_existing_ref(root, effect, label="projection effect").read_bytes()
                self.assertTrue(payload, effect)
                projection = json.loads(payload)
                self.assertIs(True, projection.get("non_authoritative"), projection)
                self.assertTrue(projection.get("source_frontier_evidence"), projection)
        elif case_id == "W13":
            self.assertTrue(effects, rows)
            native = self._action_progress(root, execute["request_id"], rows[-1]["action_run_id"]).get("native_result")
            self.assertIsInstance(native, dict, native)
            self.assertTrue(native.get("source_frontier_digest"), native)
            for effect in effects:
                self.assertTrue(self._safe_existing_ref(root, effect, label="compiled projection").read_bytes(), effect)
        elif case_id in {"W14", "W15"}:
            self.assertEqual([], effects, rows)
            self.assertEqual(before, fixture.snapshot(), "native queries are read-only")
            progress = self._action_progress(root, execute["request_id"], rows[0]["action_run_id"])
            native = progress["native_result"]
            self.assertIsInstance(native, dict, progress)
            self.assertIsInstance(native.get("snapshot"), dict, native)
            self.assertIsInstance(native.get("results"), list, native)
            if case_id == "W14":
                self.assertTrue(native["snapshot"].get("digest"), native)
                self.assertTrue(native.get("coverage", {}).get("complete"), native)
                self.assertTrue(all(set(row) == {"artifact_id"} for row in native["results"]), native)
            else:
                self.assertIn(native.get("status"), {"complete", "incomplete"}, native)
                own_event_ids = {
                    event.get("event_id") for event in self._events(root)
                    if event.get("llm_session", {}).get("uuid") == execute["request_id"]
                }
                self.assertTrue(set(native["snapshot"].get("event_ids", [])).isdisjoint(own_event_ids), native)
                self.assertTrue(all(isinstance(event_id, str) for event_id in native["results"]), native)
        else:
            self.fail(f"no strict route-specific evidence assertion for {case_id}")

    @staticmethod
    def _events(root: Path) -> list[dict]:
        journal = root / ".caprmedio_caprmedio/_journal"
        values: list[dict] = []
        for path in sorted(journal.glob("*.ndjson")):
            values.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line)
        return values

    async def test_golden_corpus_covers_exact_w01_w15_and_j01_j08(self) -> None:
        self.assertEqual(15, len(ROUTE_CASES))
        self.assertEqual(tuple(f"W{number:02d}" for number in range(1, 16)), tuple(case for case, _ in ROUTE_CASES))
        self.assertEqual(tuple(f"J{number:02d}" for number in range(1, 9)), JOURNAL_CASES)
        for case_id, route in ROUTE_CASES:
            temporary, _root, fixture = self._new_fixture(GoldenCase(case_id, route))
            try:
                manifest = fixture.prepare()
                self.assertEqual(route, next(item["route"] for item in manifest["routes"] if item["route"] == route))
            except GoldenCorpusError as error:
                self.fail(str(error))
            finally:
                temporary.cleanup()

    async def test_fresh_image_runtime_does_not_mount_host_implementation(self) -> None:
        """The selected proof must execute `/workspace` code, not a host Engine mount."""
        temporary, root, fixture = self._new_fixture(GoldenCase("W01", "create_atom"))
        try:
            fixture.prepare()
            runtime = self._runtime(root)
            config = json.loads(
                await asyncio.to_thread(
                    runtime.call, "--profile", "stdio", "config", "--format", "json"
                )
            )
            for name in ("worker", "mcp"):
                mounts = config["services"][name]["volumes"]
                targets = {mount["target"] for mount in mounts}
                self.assertNotIn("/project/102_FRAMEWORK_ENGINE", targets, config["services"][name])
                self.assertIn("/project", targets, config["services"][name])
                git = next(mount for mount in mounts if mount["target"] == "/project/.git")
                self.assertTrue(git.get("read_only", False), config["services"][name])
        except GoldenCorpusError as error:
            self.fail(str(error))
        finally:
            temporary.cleanup()

    async def test_all_fifteen_previews_are_read_only_and_survive_mcp_reconnect(self) -> None:
        for case_id, route in ROUTE_CASES:
            with self.subTest(case=case_id):
                temporary, root, fixture = self._new_fixture(GoldenCase(case_id, route))
                runtime = self._runtime(root)
                launched = False
                try:
                    fixture.prepare()
                    launched = True  # Runtime.start can create the Agent before readiness fails.
                    await self._start(runtime)
                    await self._preview(runtime, root, fixture, f"golden-{case_id.lower()}-preview")
                except GoldenCorpusError as error:
                    self.fail(str(error))
                finally:
                    if launched:
                        await self._stop(runtime)
                    temporary.cleanup()

    async def test_all_fifteen_execute_with_native_effects_and_clean_shared_run_lineage(self) -> None:
        """A happy route is valid only after one reconnected clean terminal proof."""
        for case_id, route_name in ROUTE_CASES:
            with self.subTest(case=case_id):
                case = GoldenCase(case_id, route_name)
                temporary, root, fixture = self._new_fixture(case)
                runtime = self._runtime(root)
                launched = False
                try:
                    fixture.prepare()
                    launched = True
                    await self._start(runtime)
                    request_id = f"golden-{case_id.lower()}-happy"
                    preview = await self._preview(runtime, root, fixture, request_id)
                    before = fixture.snapshot()
                    execute = fixture.request(
                        request_id=request_id,
                        mode="execute",
                        receipt=preview["proposal_receipt"],
                        receipt_digest=preview["proposal_receipt_digest"],
                    )
                    admitted = await self._call(
                        runtime,
                        root,
                        "workflow_orchestrator",
                        {"operation": "enqueue_selected", "run_id": request_id, "execution": execute},
                    )
                    self.assertIn(
                        admitted.get("outcome"),
                        {"queued", "admitted", "started", "running", "pending", "completed"},
                        admitted,
                    )
                    terminal = await self._terminal_status(runtime, root, request_id)
                    # backend.status flattens outcome/disposition for convenience,
                    # but all selected execution evidence remains nested here.
                    self.assertEqual("terminal", terminal.get("disposition"), terminal)
                    self.assertEqual("completed", terminal.get("outcome"), terminal)
                    selected = terminal.get("selected_result")
                    self.assertIsInstance(selected, dict, terminal)
                    graph = self._graph_result(root, request_id)
                    rows = self._assert_graph_path_and_native_results(root, fixture, request_id, graph)
                    self._assert_shared_run_journal(root, request_id, self._route_binding(fixture), selected, graph)
                    self._assert_route_specific_effects(root, fixture, execute, before, rows)
                except GoldenCorpusError as error:
                    self.fail(str(error))
                finally:
                    if launched:
                        await self._stop(runtime)
                    temporary.cleanup()

    async def test_w04_all_current_roles_and_admitted_statuses(self) -> None:
        """CA-P-1616: exercise every source-admitted W04 status through Docker/MCP."""
        for role, _letter, _folder, source_id, statuses in STATUS_DOMAINS:
            with self.subTest(role=role):
                temporary, root, fixture = self._new_fixture(GoldenCase("W04", "change_atom_status"))
                runtime = self._runtime(root)
                launched = False
                try:
                    fixture.prepare()
                    launched = True
                    await self._start(runtime)
                    final_observed: Path | None = None
                    final_status: str | None = None
                    for offset, changed in enumerate(statuses):
                        current = next(value for value in statuses
                                       if value != changed and value.casefold() != "draft")
                        path = fixture.status_atom(role, current, number=8000 + offset)
                        native, _graph, _selected = await self._execute_status_case(
                            runtime, root, fixture, path, changed,
                            f"p1616-{role.lower()}-{changed.casefold()}-change",
                        )
                        self.assertEqual("applied", native.get("outcome"), native)
                        model = native["status_model"]
                        self.assertEqual(list(statuses), model["statuses"], native)
                        model_pin = model["model_sources"][0]
                        self.assertEqual(source_id, model_pin["atom_id"], native)
                        self.assertEqual(
                            hashlib.sha256((root / model_pin["path"]).read_bytes()).hexdigest(),
                            model_pin["sha256"], native,
                        )
                        observed = root / native["observed"]["path"]
                        self.assertTrue(observed.is_file(), native)
                        self.assertEqual(changed, native["observed"]["status"], native)
                        if role == "Requirement" and changed == "Draft":
                            self.assertIsNone(native["observed"]["atom_id"], native)
                            self.assertNotIn("atom_id:", observed.read_text(encoding="utf-8"), native)
                            self.assertIn("history", native, native)
                        final_observed, final_status = observed, changed

                    assert final_observed is not None and final_status is not None
                    noop, _graph, _selected = await self._execute_status_case(
                        runtime, root, fixture, final_observed, final_status, f"p1616-{role.lower()}-noop",
                    )
                    self.assertEqual("no-op", noop.get("outcome"), noop)
                    self.assertTrue(all(effect.get("state") == "unchanged" for effect in noop.get("effects", [])), noop)

                    before = fixture.snapshot()
                    with self.assertRaisesRegex(AssertionError, "status-unadmitted"):
                        await self._call(
                            runtime, root, fixture.case.route,
                            fixture.request_for_status(
                                final_observed, "NotAdmitted", request_id=f"p1616-{role.lower()}-rejected",
                            ),
                        )
                    self.assertEqual(before, fixture.snapshot(), "rejected W04 request changed authority")
                except GoldenCorpusError as error:
                    self.fail(str(error))
                finally:
                    if launched:
                        await self._stop(runtime)
                    temporary.cleanup()

    async def test_stale_source_rejects_without_workflow_or_journal_effect(self) -> None:
        case = GoldenCase("W13", "build_applicable_methodology")
        temporary, root, fixture = self._new_fixture(case)
        runtime = self._runtime(root)
        launched = False
        try:
            fixture.prepare()
            fixture.corrupt_one_bound_source()
            before = fixture.snapshot()
            launched = True
            await self._start(runtime)
            result = await self._call(
                runtime, root, case.route, fixture.request(request_id="golden-w13-stale")
            )
            self.assertEqual("rejected", result.get("disposition"), result)
            self.assertEqual(before, fixture.snapshot())
            self.assertFalse(list((root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")))
        except GoldenCorpusError as error:
            self.fail(str(error))
        finally:
            if launched:
                await self._stop(runtime)
            temporary.cleanup()


class SelectedWorkflowJournalHarnessTest(unittest.TestCase):
    """Non-Docker regression for the W01 child-Run evidence contract."""

    _events = staticmethod(SelectedWorkflowsDockerEndToEnd._events)
    _safe_existing_ref = staticmethod(SelectedWorkflowsDockerEndToEnd._safe_existing_ref)

    def test_create_atom_requires_the_source_bound_o032_child_run(self) -> None:
        request_id = "w01-harness"
        step_run_id = f"{request_id}:step:1"
        action_run_id = f"{step_run_id}:action:1"
        child_run_id = f"{action_run_id}:nested:CA-O-032"
        pins = {
            "workflow": {"atom_id": "CA-O-127", "version": 1, "source_path": "definitions/workflow.md", "digest": "a" * 64},
            "step": {"atom_id": "CA-O-129", "version": 1, "source_path": "definitions/step.md", "digest": "b" * 64},
            "action": {"atom_id": "CA-O-128", "version": 1, "source_path": "definitions/action.md", "digest": "c" * 64},
            "creation": {"atom_id": "CA-O-032", "version": 1, "source_path": "definitions/creation.md", "digest": "d" * 64},
        }
        route = {
            "route": "create_atom", "workflow": pins["workflow"],
            "ordered_steps": [{"step": pins["step"], "action": pins["action"]}],
            "native_action_calls": [pins["creation"]],
        }
        graph = {"step_results": [{"step_run_id": step_run_id, "action_run_id": action_run_id,
                                   "step_definition_id": "CA-O-129", "action_definition_id": "CA-O-128"}]}
        run_pins = {
            request_id: pins["workflow"], step_run_id: pins["step"], action_run_id: pins["action"],
            child_run_id: {"atom_id": "CA-O-032", "version": 1, "source_path": "definitions/creation.md", "digest": "d" * 64},
        }
        parents = {request_id: None, step_run_id: request_id, action_run_id: step_run_id, child_run_id: action_run_id}
        with tempfile.TemporaryDirectory(dir=Path.cwd() / ".caprmedio_tmp", ignore_cleanup_errors=True) as directory:
            root = Path(directory)
            journal = root / ".caprmedio_caprmedio/_journal"
            journal.mkdir(parents=True)
            events = []
            terminals = []
            for run_id, pin in run_pins.items():
                for event_name, outcome in (("started", None), ("completed", "completed")):
                    run = {"run_id": run_id, "definition": {"atom_id": pin["atom_id"], "version": pin["version"],
                                                               "path": pin["source_path"], "digest": pin["digest"]}}
                    if parents[run_id] is not None:
                        run["parent_run_id"] = parents[run_id]
                    events.append({"schema_version": 5, "kind": "workflow_execution", "event_id": f"{run_id}-{event_name}",
                                   "event": event_name, "outcome": outcome, "llm_session": {"uuid": request_id}, "run": run})
                result_ref = f"evidence/{run_id}.json"
                result = root / result_ref
                result.parent.mkdir(parents=True, exist_ok=True)
                result.write_text("{}", encoding="utf-8")
                terminals.append({"run_id": run_id, "disposition": "terminal", "outcome": "completed",
                                  "result_ref": result_ref, "effect_refs": []})
            (journal / "runs.ndjson").write_text("\n".join(json.dumps(event) for event in events) + "\n", encoding="utf-8")
            selected = {"disposition": "terminal", "run_ids": list(run_pins), "terminal_runs": terminals}

            SelectedWorkflowsDockerEndToEnd._assert_shared_run_journal(self, root, request_id, route, selected, graph)


if __name__ == "__main__":
    unittest.main()
