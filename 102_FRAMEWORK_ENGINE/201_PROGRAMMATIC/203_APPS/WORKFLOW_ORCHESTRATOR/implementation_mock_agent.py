"""Fixed executable Docker mock, not a live model or general-purpose writer.

The current source-bound Action handler admits the packet before this callback.
Only two reserved files may be created, and only in the exact explicitly
admitted disposable workspace. Packet commands and code are never executed.
"""
from __future__ import annotations

from collections.abc import Mapping
import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

from implementation_agent import _workspace, _workspace_write_admitted

TRANSPORT = "mock-not-live-llm"
CANDIDATE = "caprmedio_mock_candidate.py"
TEST = "test_caprmedio_mock_candidate.py"
CANDIDATE_TEXT = "def add(left, right):\n    return left + right\n"
TEST_TEXT = (
    "from pathlib import Path\nimport sys\nimport unittest\n"
    "sys.path.insert(0, str(Path(__file__).parent))\n"
    "from caprmedio_mock_candidate import add\n"
    "class GoldenTest(unittest.TestCase):\n"
    "    def test_add(self):\n        self.assertEqual(5, add(2, 3))\n"
    "if __name__ == '__main__':\n    unittest.main()\n"
)
STEPS = {
    "CA-O-091": ("CA-O-017", "Integrated"),
    "CA-O-092": ("CA-O-018", "Isolated"),
    "CA-O-093": ("CA-O-019", "Isolated"),
    "CA-O-094": ("CA-O-020", "Integrated"),
}


class ImplementationMockAgent:
    def __init__(self, project_root: str | Path):
        self.root = Path(project_root).resolve(strict=True)

    def __call__(self, prompt: str, packet: Mapping[str, Any]) -> dict[str, Any]:
        try:
            if not isinstance(prompt, str) or not isinstance(packet, Mapping):
                raise ValueError("mock requires the current Action prompt and packet")
            header = re.findall(r"^Step: (CA-O-\d+) \| Action: (CA-O-\d+) \| Context: (\w+)$", prompt, re.M)
            if len(header) != 1 or header[0][0] not in STEPS:
                raise ValueError("mock supports only the fixed test-first Action path")
            step, action, context = header[0]
            if STEPS[step] != (action, context) or packet.get("context") != context:
                raise ValueError("mock Action/context binding is mismatched")
            if packet.get("step_marker", step) != step:
                raise ValueError("mock Step binding is mismatched")
            permissions = packet.get("permissions")
            if not isinstance(permissions, Mapping) or permissions.get("allowed") is not True:
                raise ValueError("mock permission is denied")
            workspace = _workspace(packet)
            if workspace == self.root or not workspace.is_relative_to(self.root):
                raise ValueError("mock workspace must be a disposable subdirectory of the selected Project")
            if not _workspace_write_admitted(packet, workspace):
                raise ValueError("mock needs the existing explicit disposable workspace write capability")
            capability = permissions["implementation_workspace"]
            if set(capability) != {"kind", "path", "allow_write"}:
                raise ValueError("mock workspace capability must be exact")
            # ``_workspace`` has already rejected a symlink workspace leaf and
            # returned its canonical directory.  Ancestor aliases such as
            # macOS /var -> /private/var are not a caller-controlled escape.
            # Keep the mock aligned with the selected-route admission guard.
            if Path(packet["workspace"]).is_symlink():
                raise ValueError("mock workspace may not be a symbolic link")
            test = _current(workspace / TEST, TEST_TEXT)
            candidate = _current(workspace / CANDIDATE, CANDIDATE_TEXT)
            outputs: dict[str, Any] = {"workspace": str(workspace), "mock_case": "fixed-add-assertion"}
            evidence: list[dict[str, Any]] = [{"transport": TRANSPORT, "step": step,
                                             "prompt_sha256": _digest(prompt.encode())}]
            if step == "CA-O-091":
                if not test:
                    result = "evaluation_ready"
                elif not candidate:
                    result = "requirement_ready"
                elif any(row.get("step_definition_id") == "CA-O-094" and
                         row.get("result") in {"passed", "checks pass"}
                         for row in packet.get("prior_results", []) if isinstance(row, Mapping)):
                    check = _check(workspace)
                    evidence.append(check)
                    result = "complete" if check["returncode"] == 0 else "blocked"
                else:
                    result = "evaluation_runnable"
            elif step == "CA-O-092":
                if candidate or test:
                    raise ValueError("mock preparation refuses to overwrite or replay existing work")
                _create(workspace / TEST, TEST_TEXT)
                check = _check(workspace)
                evidence.append(check)
                outputs.update(golden_e2e=[TEST], commands=[check["command"]],
                               expected_outcomes=["baseline fails before candidate exists"],
                               changed_paths=[_observed(workspace / TEST)])
                result = "prepared" if check["returncode"] != 0 else "blocked"
            elif step == "CA-O-093":
                if not test or candidate:
                    raise ValueError("mock implementation requires prepared tests and no existing candidate")
                _create(workspace / CANDIDATE, CANDIDATE_TEXT)
                outputs.update(candidate=CANDIDATE, changed_paths=[_observed(workspace / CANDIDATE)])
                evidence.append({"transport": TRANSPORT, "candidate": _observed(workspace / CANDIDATE)})
                result = "implemented"
            else:
                if not test or not candidate:
                    raise ValueError("mock evaluation requires the exact prepared test and candidate")
                check = _check(workspace)
                evidence.append(check)
                outputs.update(commands=[check["command"]], checks=[check],
                               candidate=_observed(workspace / CANDIDATE), test=_observed(workspace / TEST))
                result = "passed" if check["returncode"] == 0 else "failed"
            return {"result": result, "outputs": outputs, "evidence": evidence,
                    "blockers": [] if result != "blocked" else ["mock assertion did not pass"]}
        except (OSError, ValueError, TypeError, subprocess.TimeoutExpired) as error:
            return {"result": "blocked", "outputs": {}, "evidence": [{"transport": TRANSPORT}],
                    "blockers": [str(error)]}


def _digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _current(path: Path, text: str) -> bool:
    if path.is_symlink():
        raise ValueError("mock reserved file may not be a symbolic link")
    if not path.exists():
        return False
    if not path.is_file() or path.stat().st_nlink != 1 or path.stat().st_size > 4096:
        raise ValueError("mock reserved file is not a safe bounded regular file")
    if path.read_bytes() != text.encode():
        raise ValueError("mock refuses changed or unrelated reserved file content")
    return True


def _create(path: Path, text: str) -> None:
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(descriptor, "wb") as handle:
        handle.write(text.encode())
        handle.flush()
        os.fsync(handle.fileno())


def _observed(path: Path) -> dict[str, str]:
    return {"path": path.name, "after_sha256": _digest(path.read_bytes())}


def _check(workspace: Path) -> dict[str, Any]:
    command = [sys.executable, "-I", "-B", str(workspace / TEST)]
    result = subprocess.run(command, cwd=workspace, capture_output=True, timeout=10, check=False)
    return {"transport": TRANSPORT, "command": command, "returncode": result.returncode,
            "stdout_sha256": _digest(result.stdout), "stderr_sha256": _digest(result.stderr)}
