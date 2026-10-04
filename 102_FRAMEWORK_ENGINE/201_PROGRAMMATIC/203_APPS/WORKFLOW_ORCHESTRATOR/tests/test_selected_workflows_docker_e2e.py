"""Selected W01--W13 Docker/MCP golden evidence harness.

This is intentionally an opt-in Docker suite.  With ``CAPRMEDIO_DOCKER_E2E=1``
it fails on an absent route manifest, MCP registration, shared-run integration,
or functional evidence; it never turns any of those states into a skip/pass.
The existing Base Revise Docker tests remain a separate regression suite.
"""
from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import unittest


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
sys.path.insert(0, str(APP / "docker"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from runtime import Runtime  # noqa: E402
from selected_workflows_docker_fixture import (  # noqa: E402
    GoldenCase,
    GoldenCorpusError,
    GoldenProject,
    FixtureLease,
    JOURNAL_CASES,
    ROUTE_CASES,
)


@unittest.skipUnless(
    os.environ.get("CAPRMEDIO_DOCKER_E2E") == "1",
    "requires CAPRMEDIO_DOCKER_E2E=1; skipped Docker evidence is not a pass",
)
class SelectedWorkflowsDockerEndToEnd(unittest.IsolatedAsyncioTestCase):
    """One runtime and one disposable Git Project per source-bound route."""

    async def _call(self, runtime: Runtime, root: Path, tool: str, request: dict) -> dict:
        """Use a new stdio MCP client per call to prove reconnect persistence."""
        try:
            from mcp import Client, StdioServerParameters
        except ImportError as error:  # exact command must use the declared MCP group
            self.fail(f"Docker/MCP harness dependency is unavailable: {error}")
        parameters = StdioServerParameters(
            command=sys.executable,
            args=[str(APP / "docker/runtime.py"), "--project-root", str(root), "--mock", "mcp"],
        )
        async with Client(parameters) as client:
            response = await client.call_tool(tool, {"request": request})
        self.assertFalse(response.is_error, str(response))
        value = response.structured_content
        self.assertIsInstance(value, dict, value)
        return value

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
        parent = ROOT / ".caprmedio_tmp/tests/selected-workflows-docker-e2e"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        fixture = GoldenProject(ROOT, root, case)
        return FixtureLease(root), root, fixture

    async def _preview(self, runtime: Runtime, root: Path, fixture: GoldenProject,
                       request_id: str) -> dict:
        before = fixture.snapshot()
        result = await self._call(runtime, root, fixture.case.route, fixture.request(request_id=request_id))
        self.assertEqual("preview", result.get("disposition"), result)
        self.assertIn("proposal_receipt", result, result)
        self.assertIn("proposal_receipt_digest", result, result)
        self.assertEqual(before, fixture.snapshot(), "a preview must not mutate admitted authority")
        self.assertFalse(list((root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")))
        return result

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

    @staticmethod
    def _events(root: Path) -> list[dict]:
        journal = root / ".caprmedio_caprmedio/_journal"
        values: list[dict] = []
        for path in sorted(journal.glob("*.ndjson")):
            values.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line)
        return values

    async def test_golden_corpus_covers_exact_w01_w13_and_j01_j08(self) -> None:
        self.assertEqual(13, len(ROUTE_CASES))
        self.assertEqual(tuple(f"W{number:02d}" for number in range(1, 14)), tuple(case for case, _ in ROUTE_CASES))
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
            runtime = Runtime(root, mock=True)
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

    async def test_all_thirteen_previews_are_read_only_and_survive_mcp_reconnect(self) -> None:
        for case_id, route in ROUTE_CASES:
            with self.subTest(case=case_id):
                temporary, root, fixture = self._new_fixture(GoldenCase(case_id, route))
                runtime = Runtime(root, mock=True)
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

    async def test_execute_requires_real_effects_journal_receipts_and_reconnected_status(self) -> None:
        """A happy route must prove effects, not a queued or MCP acknowledgement."""
        case = GoldenCase("W01", "create_atom")
        temporary, root, fixture = self._new_fixture(case)
        runtime = Runtime(root, mock=True)
        launched = False
        try:
            fixture.prepare()
            launched = True
            await self._start(runtime)
            request_id = "golden-w01-happy"
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
                {"queued", "admitted", "started", "running", "pending", "completed", "no_op", "partial", "cancelled", "interrupted_pending"},
                admitted,
            )
            terminal = await self._terminal_status(runtime, root, request_id)
            self.assertIn(terminal.get("outcome"), {"completed", "no_op", "partial", "cancelled", "interrupted_pending", "failed", "interrupted"}, terminal)
            run_ids = terminal.get("run_ids", admitted.get("run_ids"))
            self.assertIsInstance(run_ids, list, terminal)
            self.assertTrue(run_ids, terminal)
            events = self._events(root)
            selected = [event for event in events if event.get("run", {}).get("run_id") in set(run_ids)]
            self.assertTrue(selected, "the selected Run must have canonical Journal evidence")
            self.assertEqual(len({event["event_id"] for event in selected}), len(selected))
            self.assertTrue(all(event.get("schema_version") == 5 for event in selected))
            if terminal["outcome"] == "no_op":
                self.assertEqual(before, fixture.snapshot(), "no-op must have no fictional authority effect")
            else:
                effects = terminal.get("effect_refs", admitted.get("effect_refs", []))
                self.assertTrue(effects, terminal)
                for effect in effects:
                    self.assertTrue((root / effect).exists(), f"missing admitted effect: {effect}")
                self.assertNotEqual(before, fixture.snapshot(), "an effect outcome must change admitted state")
        except GoldenCorpusError as error:
            self.fail(str(error))
        finally:
            if launched:
                await self._stop(runtime)
            temporary.cleanup()

    async def test_stale_source_rejects_without_workflow_or_journal_effect(self) -> None:
        case = GoldenCase("W13", "build_applicable_methodology")
        temporary, root, fixture = self._new_fixture(case)
        runtime = Runtime(root, mock=True)
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


if __name__ == "__main__":
    unittest.main()
