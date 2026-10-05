"""Explicit Project-scoped Docker lifecycle; never creates Workflow requests."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

DIRECTORY = Path(__file__).resolve().parent
SOURCE_ROOT = DIRECTORY.parents[4]
IMAGE = "caprmedio-runtime:local"


def image_reference(environment=None):
    """Use an explicit image identity when one is supplied; retain the dev fallback."""
    value = (os.environ if environment is None else environment).get("CAPRMEDIO_IMAGE")
    return value or IMAGE


class Runtime:
    def __init__(self, root, *, mock=False, auth_file=None):
        self.root = Path(root).resolve(strict=True)
        self.mock, self.auth_file = mock, auth_file
        self.project = "caprmedio-" + hashlib.sha256(str(self.root).encode()).hexdigest()[:12]

    def environment(self):
        environment = dict(
            os.environ,
            CAPRMEDIO_PROJECT_ROOT=str(self.root),
            CAPRMEDIO_IMAGE=image_reference(),
        )
        environment.pop("CAPRMEDIO_CODEX_AUTH_FILE", None)
        if not self.mock and self.auth_file:
            environment["CAPRMEDIO_CODEX_AUTH_FILE"] = str(
                Path(self.auth_file).resolve(strict=True)
            )
        return environment

    def command(self, *arguments, authentication=False):
        command = [
            "docker",
            "compose",
            "--env-file",
            "/dev/null",
            "--project-name",
            self.project,
            "-f",
            str(DIRECTORY / "compose.yaml"),
        ]
        if self.mock:
            command += ["-f", str(DIRECTORY / "mock.compose.yaml")]
        elif authentication:
            command += ["-f", str(DIRECTORY / "auth.compose.yaml")]
        return command + list(arguments)

    def call(self, *arguments, authentication=False, capture=True, timeout=60):
        result = subprocess.run(
            self.command(*arguments, authentication=authentication),
            env=self.environment(),
            text=True,
            capture_output=capture,
            timeout=timeout,
            check=False,
        )
        if result.returncode:
            raise RuntimeError("Docker operation failed; inspect service logs")
        return result.stdout if capture else None

    def build(self):
        command = [
            "docker",
            "build",
            "--file",
            str(DIRECTORY / "Dockerfile"),
            "--tag",
            IMAGE,
            "--build-arg",
            f"RUNTIME_UID={os.getuid()}",
            "--build-arg",
            f"RUNTIME_GID={os.getgid()}",
            str(SOURCE_ROOT),
        ]
        subprocess.run(command, check=True)

    def prepare(self):
        for relative in (".caprmedio_caprmedio", ".git"):
            if (self.root / relative).is_symlink():
                raise ValueError("Runtime mounts must not be symlinks")
        if not (self.root / ".caprmedio_caprmedio").is_dir() or not (self.root / ".git").is_dir():
            raise ValueError("Project authority and a directory Git repository are required")
        for relative in (".caprmedio_install", ".caprmedio_tmp", "tmp"):
            path = self.root / relative
            if path.is_symlink():
                raise ValueError("Runtime mounts must not be symlinks")
            path.mkdir(exist_ok=True)
        if not self.mock and not self.auth_file:
            raise ValueError("Pass --auth-file explicitly; credentials are not guessed")
        directory = self.root / ".caprmedio_install"
        for name in ("workflow_orchestrator", "docker"):
            directory /= name
            if directory.is_symlink():
                raise ValueError("Runtime routing directories must not be symlinks")
            directory.mkdir(exist_ok=True)
        marker = directory / "transport.json"
        if marker.is_symlink() or (marker.exists() and not marker.is_file()):
            raise ValueError("Unsafe runtime routing marker")

    def start(self):
        self.prepare()
        self.call(
            "up",
            "-d",
            "--wait",
            "--wait-timeout",
            "60",
            "--force-recreate",
            "agent",
            "worker",
            authentication=not self.mock,
            timeout=90,
        )
        marker = self.root / ".caprmedio_install/workflow_orchestrator/docker/transport.json"
        descriptor, name = tempfile.mkstemp(prefix="transport-", suffix=".json", dir=marker.parent)
        temporary = Path(name)
        try:
            with os.fdopen(descriptor, "w") as handle:
                json.dump({"transport": "docker", "project_name": self.project}, handle)
                handle.flush()
                os.fsync(handle.fileno())
            temporary.replace(marker)
        finally:
            temporary.unlink(missing_ok=True)
        return {
            "runtime": "docker",
            "project_name": self.project,
            "outcome": "ready",
            "agent_mode": "mock" if self.mock else "codex",
        }

    def stop(self):
        self.call("stop", "worker", "agent", timeout=60)
        return {"runtime": "docker", "outcome": "stopped", "persistent_state": "retained"}

    def status(self):
        raw = self.call("ps", "--all", "--format", "json")
        services = [json.loads(line) for line in raw.splitlines() if line.strip()]
        return {"runtime": "docker", "project_name": self.project, "services": services}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=SOURCE_ROOT)
    parser.add_argument("--auth-file", type=Path)
    parser.add_argument("--mock", action="store_true")
    parser.add_argument(
        "operation", choices=["build", "start", "stop", "restart", "status", "logs", "mcp"]
    )
    args = parser.parse_args()
    runtime = Runtime(args.project_root, mock=args.mock, auth_file=args.auth_file)
    if args.operation == "build":
        runtime.build()
    elif args.operation in ("start", "restart"):
        if args.operation == "restart":
            runtime.stop()
        print(json.dumps(runtime.start()))
    elif args.operation == "stop":
        print(json.dumps(runtime.stop()))
    elif args.operation == "status":
        print(json.dumps(runtime.status()))
    elif args.operation == "logs":
        runtime.call("logs", "--tail", "100", capture=False)
    else:
        os.execvpe(
            "docker",
            runtime.command("run", "--rm", "--no-deps", "-T", "mcp"),
            runtime.environment(),
        )


if __name__ == "__main__":
    main()
