"""Foreground services with immutable code and explicit runtime-only credentials."""

import json
import os
from pathlib import Path
import shutil
import sys
from urllib.request import urlopen

APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path("/project")
sys.path.insert(0, str(APP))


def seed_authentication():
    if os.environ.get("CAPRMEDIO_AGENT_MODE") == "mock":
        return
    destination = Path.home() / ".codex/auth.json"
    if destination.is_file():
        return
    seed = Path("/run/secrets/codex_auth")
    if not seed.is_file():
        raise RuntimeError("Missing explicitly admitted Codex credential seed")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(".initial")
    shutil.copyfile(seed, temporary)
    temporary.chmod(0o600)
    temporary.replace(destination)


def worker_health():
    from engine import runtime_fingerprint

    directory = PROJECT_ROOT / ".caprmedio_install/workflow_orchestrator/docker"
    ready = json.loads((directory / "worker.ready").read_text())
    state = json.loads((directory / "worker.json").read_text())
    if ready["pid"] != state["pid"] or state["state"] != "starting":
        raise RuntimeError("Worker is not current")
    os.kill(ready["pid"], 0)
    if ready["runtime_fingerprint"] != runtime_fingerprint(PROJECT_ROOT):
        raise RuntimeError("Worker readiness does not bind this image")


def main():
    mode = sys.argv[1]
    if mode == "agent":
        seed_authentication()
        import uvicorn
        from agent_service import app

        uvicorn.run(app, host="0.0.0.0", port=8091, log_level="warning")
    elif mode == "agent-health":
        with urlopen("http://127.0.0.1:8091/health", timeout=3) as response:
            if not json.load(response)["ready"]:
                raise RuntimeError("Agent is not ready")
    elif mode == "health":
        worker_health()
    else:
        paths = {"worker": APP / "orchestrator.py", "mcp": APP.parents[1] / "204_MCP/server.py",
                 "mcp-http": APP.parents[1] / "204_MCP/server.py"}
        if mode not in paths:
            raise ValueError("Unknown runtime service")
        command = [sys.executable, str(paths[mode]), "--project-root", str(PROJECT_ROOT)]
        if mode == "mcp-http":
            command += ["--transport", "streamable-http"]
        if mode == "worker":
            command.append("worker")
        os.execv(sys.executable, command)


if __name__ == "__main__":
    main()
