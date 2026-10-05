"""Focused executable contracts for the bounded Implementation Agent transport."""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import textwrap
import unittest


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

from implementation_agent import ImplementationAgent  # noqa: E402


class ImplementationAgentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.workspace = self.root / "disposable-workspace"
        self.workspace.mkdir()
        self.script = self.root / "fake_codex.py"

    def packet(self, *, write: bool = False, timeout: int = 5) -> dict[str, object]:
        permissions: dict[str, object] = {"allowed": True}
        if write:
            permissions["implementation_workspace"] = {
                "kind": "disposable_workspace",
                "path": str(self.workspace),
                "allow_write": True,
            }
        return {
            "workspace": str(self.workspace),
            "permissions": permissions,
            "agent_timeout_seconds": timeout,
        }

    def write_fake(self, body: str) -> None:
        self.script.write_text(
            "from __future__ import annotations\n"
            "import json\n"
            "from pathlib import Path\n"
            "import subprocess\n"
            "import sys\n"
            "args = sys.argv[1:]\n"
            "output = Path(args[args.index('--output-last-message') + 1])\n"
            "workspace = Path(args[args.index('--cd') + 1])\n"
            "prompt = sys.stdin.read()\n"
            + textwrap.dedent(body),
            encoding="utf-8",
        )

    def agent(self) -> ImplementationAgent:
        return ImplementationAgent([sys.executable, str(self.script)])

    def test_read_only_callback_uses_safe_cli_flags_and_returns_current_shape(self) -> None:
        self.write_fake(
            """
            assert 'Current Action prompt:\\nprepare tests\\n' in prompt
            assert '"workspace":"' in prompt
            assert args[args.index('--sandbox') + 1] == 'read-only'
            assert '--model' not in args and '--profile' not in args
            assert 'danger-full-access' not in args and '--full-auto' not in args
            output.write_text(json.dumps({
                'result': 'prepared',
                'outputs': {'golden_e2e': ['case'], 'commands': [['python', '-m', 'unittest']], 'expected_outcomes': ['fails first']},
                'evidence': ['prepared by fake CLI'],
                'blockers': [],
            }))
            """
        )

        result = self.agent()("prepare tests", self.packet())

        self.assertEqual(result["result"], "prepared")
        self.assertEqual(result["blockers"], [])
        self.assertEqual(result["evidence"][-1]["sandbox"], "read-only")
        self.assertFalse(list(self.workspace.iterdir()))

    def test_golden_executable_performs_disposable_code_and_test_work_with_observed_hash(self) -> None:
        self.write_fake(
            """
            implementation = workspace / 'implementation.py'
            implementation.write_text('def ready():\\n    return True\\n')
            test = workspace / 'golden_test.py'
            test.write_text('from implementation import ready\\nassert ready()\\n')
            check = subprocess.run([sys.executable, '-B', str(test)], cwd=workspace, capture_output=True, text=True)
            assert check.returncode == 0, check.stderr
            output.write_text(json.dumps({
                'result': 'implemented',
                'outputs': {'candidate': 'golden-v1', 'changed_paths': ['implementation.py', 'golden_test.py']},
                'evidence': [{'command': [sys.executable, str(test)], 'returncode': check.returncode}],
                'blockers': [],
            }))
            """
        )

        result = self.agent()("implement the golden case", self.packet(write=True))

        self.assertEqual(result["result"], "implemented")
        observed = result["outputs"]["changed_paths"]
        self.assertEqual([entry["path"] for entry in observed], ["golden_test.py", "implementation.py"])
        self.assertEqual(
            observed[1]["after_sha256"],
            hashlib.sha256((self.workspace / "implementation.py").read_bytes()).hexdigest(),
        )
        self.assertEqual(result["evidence"][-1]["sandbox"], "workspace-write")

    def test_rejects_missing_invalid_and_out_of_boundary_output_without_success(self) -> None:
        self.write_fake("pass\n")
        missing = self.agent()("missing output", self.packet())
        self.assertEqual(missing["result"], "blocked")
        self.assertIn("missing", missing["blockers"][0])

        self.write_fake("output.write_text('[1, 2, 3]')\n")
        invalid = self.agent()("invalid output", self.packet())
        self.assertEqual(invalid["result"], "blocked")

        outside = self.root / "outside.py"
        self.addCleanup(outside.unlink, missing_ok=True)
        self.write_fake(
            """
            outside = workspace.parent / 'outside.py'
            outside.write_text('outside the admitted boundary')
            output.write_text(json.dumps({
                'result': 'implemented',
                'outputs': {'candidate': 'unsafe', 'changed_paths': ['../outside.py']},
                'evidence': ['untrusted declaration'],
                'blockers': [],
            }))
            """
        )
        out_of_bounds = self.agent()("out of bounds", self.packet(write=True))
        self.assertEqual(out_of_bounds["result"], "blocked")
        self.assertIn("out-of-bound", out_of_bounds["blockers"][0])
        self.assertTrue(outside.exists())

    def test_timeout_and_unadmitted_write_never_fabricate_success(self) -> None:
        self.write_fake(
            """
            (workspace / 'unexpected.py').write_text('x = 1')
            output.write_text(json.dumps({
                'result': 'implemented',
                'outputs': {'candidate': 'bad', 'changed_paths': ['unexpected.py']},
                'evidence': ['claimed'],
                'blockers': [],
            }))
            """
        )
        unadmitted = self.agent()("read-only implementation", self.packet())
        self.assertEqual(unadmitted["result"], "blocked")
        self.assertIn("without an admitted", unadmitted["blockers"][0])

        self.workspace.joinpath("unexpected.py").unlink()
        self.write_fake("(workspace / 'timed_out.py').write_text('x = 1')\nimport time\ntime.sleep(2)\n")
        timed_out = self.agent()("bounded dispatch", self.packet(timeout=1))
        self.assertEqual(timed_out["result"], "blocked")
        self.assertEqual(timed_out["evidence"][0]["status"], "timeout")
        self.assertEqual(timed_out["evidence"][0]["observed_changes"][0]["path"], "timed_out.py")


if __name__ == "__main__":
    unittest.main()
