"""Opt-in real containers with a mocked Agent; no credentials or paid calls.

Build the image first, then set CAPRMEDIO_DOCKER_E2E=1. A missing image fails;
the test never silently downloads an image or starts a real Project's worker.
"""

import asyncio
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import unittest

from mcp import Client, StdioServerParameters

APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
sys.path.insert(0, str(APP))
sys.path.insert(0, str(APP / "docker"))
RELEASE_ROOT = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION"
sys.path.insert(0, str(RELEASE_ROOT))
from runtime import Runtime  # noqa: E402
from release_e2e_context import load_release_e2e_context  # noqa: E402

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
        self.started = False

    async def asyncTearDown(self):
        if self.started:
            # Only this randomly named fixture's containers/volume are removed.
            # Real runtime stop deliberately preserves its authentication volume.
            await asyncio.to_thread(self.runtime.call, "down", "--volumes", timeout=60)
        self.temporary.cleanup()

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


if __name__ == "__main__":
    unittest.main()
