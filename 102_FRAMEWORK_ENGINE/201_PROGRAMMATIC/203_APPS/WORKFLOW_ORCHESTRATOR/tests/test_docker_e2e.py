"""Opt-in real containers with a mocked Agent; no credentials or paid calls.

Build the image first, then set CAPRMEDIO_DOCKER_E2E=1. A missing image fails;
the test never silently downloads an image or starts a real Project's worker.
"""

import asyncio
import json
import os
from pathlib import Path
import secrets
import socket
import sys
import tempfile
import time
import unittest

from mcp import Client, StdioServerParameters
import httpx2
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client

APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
sys.path.insert(0, str(APP))
sys.path.insert(0, str(APP / "docker"))
RELEASE_ROOT = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION"
sys.path.insert(0, str(RELEASE_ROOT))
from runtime import Runtime  # noqa: E402
from release_e2e_context import load_release_e2e_context  # noqa: E402
from release_recovery_docker_fixture import (  # noqa: E402
    RUN_ID as RELEASE_RECOVERY_RUN_ID,
    ReleaseRecoveryDockerFixture,
)

try:
    E2E_CONTEXT = load_release_e2e_context(os.environ)
except Exception:
    E2E_CONTEXT = None


@unittest.skipUnless(
    os.environ.get("CAPRMEDIO_DOCKER_E2E") == "1" and E2E_CONTEXT is not None,
    "requires sealed Release E2E context and built candidate image",
)
class DockerEndToEnd(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        parent = E2E_CONTEXT.scratch_root / "docker-e2e"
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=parent, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root=".caprmedio_caprmedio"\njournal_root=".caprmedio_caprmedio/_journal"\n'
        )
        (control / "operators_registry.toml").write_text(
            '[[operators]]\nname="mock-operator"\nrole="project owner"\n'
        )
        prompts = (
            ROOT / "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW"
        )
        bindings = json.loads((prompts / "source_bindings.json").read_text())
        workflow = next(row["path"] for row in bindings["sources"] if row["atom_id"] == "CA-O-104")
        target = self.root / workflow
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / workflow).read_bytes())
        self.atom = control / "atom.md"
        self.atom.write_text(
            "---\natom_id: MOCK-R-1\ncontent_role: Requirement\nversion: 1\nstatus: Active\n"
            'updated_at: "2026-10-01T00:00:00Z"\n---\n# Summary\nA stable summary\n\n'
            "## Scope\nMOCK\n\n## Claim\nbad wording\n"
        )
        (control / "rules.md").write_text("mock local rules")
        self.runtime = Runtime(self.root, mock=True, image=E2E_CONTEXT.candidate_image_digest)
        self.started = self.http_started = False

    async def asyncTearDown(self):
        if self.http_started:
            await asyncio.to_thread(self.runtime.mcp_http_stop)
        if self.started:
            # Only this randomly named fixture's containers/volume are removed.
            # Real runtime stop deliberately preserves its authentication volume.
            await asyncio.to_thread(self.runtime.call, "down", "--volumes", timeout=60)
        self.temporary.cleanup()

    def http_environment(self):
        token = secrets.token_urlsafe(32)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            probe.bind(("127.0.0.1", 0))
            port = probe.getsockname()[1]
        return token, port

    async def http_session(self, url, token):
        client = httpx2.AsyncClient(headers={"Authorization": f"Bearer {token}"})
        transport = streamable_http_client(url, http_client=client)
        streams = await transport.__aenter__()
        session = ClientSession(*streams)
        await session.__aenter__()
        await session.initialize()
        return client, transport, session

    async def close_http_session(self, client, transport, session):
        await session.__aexit__(None, None, None)
        await transport.__aexit__(None, None, None)
        await client.aclose()

    async def start(self):
        self.started = True  # clean up partially started fixtures too
        try:
            result = await asyncio.to_thread(self.runtime.start)
        except RuntimeError:
            # Mock-only fixture diagnostics survive its scoped cleanup.
            logs = await asyncio.to_thread(self.runtime.call, "logs", "--no-color", "--tail", "80")
            print(logs, file=sys.stderr)
            raise
        self.assertEqual(result["outcome"], "ready")

    def parameters(self):
        return StdioServerParameters(
            command=sys.executable,
            args=[
                str(APP / "docker/runtime.py"),
                "--project-root",
                str(self.root),
                "--image",
                E2E_CONTEXT.candidate_image_digest,
                "--mock",
                "mcp",
            ],
        )

    async def request(self, operation, run_id):
        request = {"operation": operation, "run_id": run_id}
        if operation == "enqueue":
            request.update(
                selection=[{"atom_id": "MOCK-R-1", "path": ".caprmedio_caprmedio/atom.md"}],
                criteria_paths=[".caprmedio_caprmedio/rules.md"],
                author="mock-operator",
                scope="MOCK",
                allow_fixes=True,
                confidence_threshold=90.0,
            )
        async with Client(self.parameters()) as client:
            result = await client.call_tool("workflow_orchestrator", {"request": request})
            self.assertFalse(result.is_error, str(result))
            return result.structured_content

    async def local_mcp_client_request(self, client, tool, request):
        result = await client.call_tool(tool, {"request": request})
        self.assertFalse(result.is_error, str(result))
        self.assertIsInstance(result.structured_content, dict, result)
        return result.structured_content

    async def local_mcp_request(self, parameters, tool, request):
        """Use the real local MCP implementation for the release-host bridge."""
        async with Client(parameters) as client:
            return await self.local_mcp_client_request(client, tool, request)

    async def wait_for_release_result(self, fixture, predicate):
        deadline = time.monotonic() + 90
        observed = None
        while time.monotonic() < deadline:
            observed = fixture.selected_result()
            if observed is not None and predicate(observed):
                return observed
            await asyncio.sleep(0.25)
        self.fail(f"Release host did not reach the required state: {observed}")

    async def wait_for_recovered_release_event(self, fixture, event_id):
        """Wait for the original sealed terminal only, not later graph work."""
        deadline = time.monotonic() + 90
        observed = []
        while time.monotonic() < deadline:
            observed = [
                row for row in fixture.journal_events()
                if row.get("event_id") == event_id
            ]
            if len(observed) == 1 and event_id not in fixture.pending_event_ids():
                return observed[0]
            await asyncio.sleep(0.25)
        self.fail(
            "Release host did not record the original recovered terminal exactly once: "
            f"events={observed} pending={fixture.pending_event_ids()}"
        )

    async def terminal(self, run_id):
        deadline = time.monotonic() + 75
        result = {}
        while time.monotonic() < deadline:
            result = await self.request("status", run_id)
            if result["outcome"] in ("completed", "interrupted", "failed"):
                return result
            await asyncio.sleep(0.25)
        self.fail(f"Run did not settle: {result}")

    async def agent_calls(self):
        script = "import json; from urllib.request import urlopen; print(json.load(urlopen('http://agent:8091/health'))['calls'])"
        output = await asyncio.to_thread(
            self.runtime.call, "exec", "-T", "worker", "python", "-c", script
        )
        return int(output.strip())

    async def restart_worker(self):
        await asyncio.to_thread(self.runtime.call, "restart", "worker")
        await asyncio.to_thread(
            self.runtime.call,
            "up",
            "-d",
            "--no-deps",
            "--wait",
            "--wait-timeout",
            "60",
            "worker",
            timeout=75,
        )

    async def test_mcp_disconnect_fix_and_restart_preserve_evidence(self):
        await self.start()
        await self.request("enqueue", "docker-fix")  # client fully disconnects here
        completed = await self.terminal("docker-fix")
        self.assertEqual(completed["outcome"], "completed", completed)
        self.assertEqual(completed["recording_blockers"], [])
        self.assertIn("good wording", self.atom.read_text())
        self.assertTrue((self.root / completed["report_path"]).is_file())
        self.assertTrue(list((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")))
        self.assertEqual(await self.agent_calls(), 2)
        await self.restart_worker()
        self.assertEqual((await self.request("status", "docker-fix"))["outcome"], "completed")
        self.assertEqual(await self.agent_calls(), 2)
        self.assertFalse(
            (self.root / ".caprmedio_install/workflow_orchestrator/dbos.sqlite").exists()
        )
        await asyncio.to_thread(self.runtime.stop)
        # Native callers retain Docker routing and cannot silently create a native queue.
        from docker_bridge import invoke

        with self.assertRaises(RuntimeError):
            await asyncio.to_thread(
                invoke, self.root, {"operation": "status", "run_id": "docker-fix"}
            )
        self.assertFalse(
            (self.root / ".caprmedio_install/workflow_orchestrator/dbos.sqlite").exists()
        )

    async def test_uncertain_dispatch_is_not_replayed_after_worker_restart(self):
        self.atom.write_text(self.atom.read_text().replace("bad wording", "SLOW_MOCK"))
        await self.start()
        await self.request("enqueue", "docker-uncertain")
        directory = (
            self.root
            / ".caprmedio_install/workflow_orchestrator/docker/runs/docker-uncertain/0-check"
        )
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            if (directory / "intent.json").is_file() and await self.agent_calls() == 1:
                break
            await asyncio.sleep(0.1)
        else:
            self.fail("Agent dispatch was not observed")
        await asyncio.to_thread(self.runtime.call, "kill", "--signal", "SIGKILL", "worker")
        self.assertFalse((directory / "accepted.json").exists())
        await asyncio.to_thread(
            self.runtime.call,
            "up",
            "-d",
            "--no-deps",
            "--wait",
            "--wait-timeout",
            "60",
            "worker",
            timeout=75,
        )
        result = await self.terminal("docker-uncertain")
        self.assertEqual(result["outcome"], "interrupted", result)
        self.assertEqual(await self.agent_calls(), 1)
        self.assertIn("SLOW_MOCK", self.atom.read_text())

    async def test_authenticated_http_mcp_isolated_from_worker_and_agent(self):
        token, port = self.http_environment()
        previous = {key: os.environ.get(key) for key in
                    ("CAPRMEDIO_MCP_HTTP_SECRET_TOKEN", "CAPRMEDIO_MCP_HTTP_PORT")}
        os.environ["CAPRMEDIO_MCP_HTTP_SECRET_TOKEN"] = token
        os.environ["CAPRMEDIO_MCP_HTTP_PORT"] = str(port)
        self.addCleanup(self.restore_http_environment, previous)
        self.http_started = True
        started = await asyncio.to_thread(self.runtime.mcp_http_start)
        self.assertEqual(f"http://127.0.0.1:{port}/mcp", started["url"])
        status = await asyncio.to_thread(self.runtime.mcp_http_status)
        services = {row.get("Service") for row in status["services"]}
        self.assertEqual({"mcp-http"}, services)
        url = started["url"]
        client, transport, session = await self.http_session(url, token)
        try:
            names = {tool.name for tool in (await session.list_tools()).tools}
            self.assertIn("get_mcp_reload_status", names)
            result = await session.call_tool("get_mcp_reload_status", {"request": {}})
            self.assertFalse(result.is_error, result)
        finally:
            await self.close_http_session(client, transport, session)
        async with httpx2.AsyncClient() as raw:
            health = await raw.get(f"http://127.0.0.1:{port}/health",
                                   headers={"Authorization": f"Bearer {token}"})
            self.assertEqual(200, health.status_code)
            for headers, expected in (
                ({}, 401),
                ({"Authorization": "Bearer wrong"}, 401),
                ({"Authorization": f"Bearer {token}", "Host": "attacker.invalid"}, 421),
                ({"Authorization": f"Bearer {token}", "Origin": "https://attacker.invalid"}, 403),
            ):
                response = await raw.get(f"http://127.0.0.1:{port}/health", headers=headers)
                self.assertEqual(expected, response.status_code)

    async def test_release_host_recovers_one_real_effect_recording_without_replay(self):
        """P1713/P1716: queue/MCP recovery appends only a real pending terminal.

        The existing Docker runtime remains the Base Revise fixture.  Release
        uses its separately selected fixed host interpreter and private DBOS
        namespace because a Docker MCP process cannot directly own that host
        queue.  The fixture injects one local-only writer OSError after source
        delivery has produced an actual effect reference; it never fabricates
        a pending Journal carrier.
        """
        fixture = ReleaseRecoveryDockerFixture.create(E2E_CONTEXT.scratch_root)
        try:
            fixture.start_worker(fault=True)
            preview = await self.local_mcp_request(
                fixture.mcp_parameters(fault=True), "release_version", fixture.preview_request(),
            )
            self.assertEqual("preview", preview.get("disposition"), preview)
            admitted = await self.local_mcp_request(
                fixture.mcp_parameters(fault=True), "release_version", fixture.execute_request(preview),
            )
            self.assertEqual(RELEASE_RECOVERY_RUN_ID, admitted.get("workflow_run_id"), admitted)
            self.assertTrue(
                (fixture.root / ".caprmedio_install/workflow_orchestrator/release-host/transport.json").is_file()
            )
            selected = await self.wait_for_release_result(
                fixture,
                lambda result: result.get("disposition") == "recording_pending",
            )
            pending_ids = selected.get("pending_event_ids", [])
            self.assertEqual(1, len(pending_ids), selected)
            pending_files = fixture.pending_events()
            self.assertEqual(1, len(pending_files), pending_files)
            sealed = json.loads(pending_files[0].read_text(encoding="utf-8"))
            self.assertEqual(pending_ids[0], sealed["event_id"])
            event = json.loads(sealed["event_bytes"])
            self.assertEqual("completed", event["event"])
            self.assertEqual("action", event["run"]["kind"])
            self.assertTrue(event["effect_refs"], event)
            effect = fixture.root / event["effect_refs"][0].split("#", 1)[0]
            self.assertTrue(effect.exists(), event)
            effect_digest = fixture.content_digest(effect)
            before_events = fixture.journal_events()
            self.assertFalse(any(row["event_id"] == event["event_id"] for row in before_events), before_events)

            fixture.stop_worker()
            fixture.start_worker(fault=False)
            # Current source is mandatory for recovery.  A one-byte scoped
            # mutation must be refused while retaining the real pending event;
            # restoring the exact bytes below permits the same frozen run.
            workflow_source = fixture.release_workflow_source()
            original_workflow = workflow_source.read_bytes()
            # Keep one MCP gateway alive across the mutation.  A new gateway
            # correctly refuses stale bindings at startup; this instead tests
            # the independent host-side recovery admission.
            async with Client(fixture.mcp_parameters()) as recovery_client:
                workflow_source.write_bytes(original_workflow + b"\n# fixture stale guard\n")
                stale = await self.local_mcp_client_request(
                    recovery_client, "recover_selected_release", {
                        "operation": "recover_selected_release",
                        "run_id": RELEASE_RECOVERY_RUN_ID,
                        "request_identity": fixture.request_identity(),
                    },
                )
                self.assertEqual("blocked", stale.get("disposition"), stale)
                self.assertIn("stale", " ".join(stale.get("diagnostics", [])).lower(), stale)
                self.assertIn(event["event_id"], fixture.pending_event_ids())
                workflow_source.write_bytes(original_workflow)

                recovered = await self.local_mcp_client_request(
                    recovery_client, "recover_selected_release", {
                        "operation": "recover_selected_release",
                        "run_id": RELEASE_RECOVERY_RUN_ID,
                        "request_identity": fixture.request_identity(),
                    },
                )
                self.assertEqual(RELEASE_RECOVERY_RUN_ID, recovered.get("workflow_run_id"), recovered)
            recovered_event = await self.wait_for_recovered_release_event(fixture, event["event_id"])
            after_events = fixture.journal_events()
            recovered_events = [row for row in after_events if row["event_id"] == event["event_id"]]
            self.assertEqual(1, len(recovered_events), after_events)
            self.assertEqual(event, recovered_event)
            self.assertEqual(event, recovered_events[0])
            self.assertNotIn(event["event_id"], fixture.pending_event_ids())
            self.assertEqual(
                effect_digest, fixture.content_digest(effect),
                "recovery replayed or mutated the delivered source effect",
            )

            binding = fixture.root / ".caprmedio_install/workflow_orchestrator/release-host/bindings" / f"{RELEASE_RECOVERY_RUN_ID}.json"
            binding.write_text(json.dumps({"tampered": True}), encoding="utf-8")
            refused = await self.local_mcp_request(
                fixture.mcp_parameters(), "recover_selected_release", {
                    "operation": "recover_selected_release",
                    "run_id": RELEASE_RECOVERY_RUN_ID,
                    "request_identity": fixture.request_identity(),
                },
            )
            self.assertEqual("blocked", refused.get("disposition"), refused)
            self.assertIn("binding", " ".join(refused.get("diagnostics", [])), refused)
        finally:
            fixture.cleanup()

    @staticmethod
    def restore_http_environment(previous):
        for key, value in previous.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


if __name__ == "__main__":
    unittest.main()
