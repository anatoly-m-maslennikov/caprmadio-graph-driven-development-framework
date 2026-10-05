"""Existing host MCP queue calls can explicitly select the Docker worker."""

import json
import os
from pathlib import Path
import re
import subprocess

from docker.image_reference import IMAGE, image_reference

MARKER = ".caprmedio_install/workflow_orchestrator/docker/transport.json"


def _environment(root, environment=None):
    """Retain an explicit runtime image instead of silently reverting to a tag."""
    source = os.environ if environment is None else environment
    return dict(
        source,
        CAPRMEDIO_PROJECT_ROOT=str(root),
        CAPRMEDIO_ENGINE_SOURCE_ROOT=str(Path(__file__).resolve().parents[4]),
        CAPRMEDIO_IMAGE=image_reference(source),
    )


def invoke(root, request):
    from engine import Coordinator

    root = Path(root).resolve(strict=True)
    marker = Coordinator(root, None).store.path(MARKER)
    value = json.loads(marker.read_text())
    if set(value) != {"transport", "project_name"} or value["transport"] != "docker":
        raise ValueError("Invalid Docker transport selection")
    project = value["project_name"]
    if not isinstance(project, str) or not re.fullmatch(r"caprmedio-[a-z0-9-]{1,64}", project):
        raise ValueError("Invalid Docker Compose Project name")
    compose = Path(__file__).with_name("docker") / "compose.yaml"
    command = [
        "docker",
        "compose",
        "--env-file",
        "/dev/null",
        "--project-name",
        project,
        "-f",
        str(compose),
        "exec",
        "-T",
        "worker",
        "python",
        "/workspace/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/"
        "WORKFLOW_ORCHESTRATOR/orchestrator.py",
        "--project-root",
        "/project",
        request["operation"],
    ]
    environment = _environment(root)
    try:
        result = subprocess.run(
            command,
            input=json.dumps(request),
            capture_output=True,
            text=True,
            env=environment,
            timeout=60,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise RuntimeError("Docker runtime is unavailable; no native queue fallback") from error
    if result.returncode:
        raise RuntimeError(
            "Docker queue call failed; inspect runtime logs; no native queue fallback"
        )
    try:
        return json.loads(result.stdout)
    except (ValueError, TypeError) as error:
        raise RuntimeError("Docker queue returned invalid structured output") from error
