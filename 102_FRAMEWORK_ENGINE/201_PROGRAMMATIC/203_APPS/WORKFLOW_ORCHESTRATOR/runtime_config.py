"""An explicit scheduler namespace; native state is never silently imported."""

import os


def docker_runtime():
    value = os.environ.get("CAPRMEDIO_RUNTIME_NAMESPACE", "")
    if value not in ("", "docker"):
        raise ValueError("Unsupported runtime namespace")
    return value == "docker"


def control_directory():
    base = ".caprmedio_install/workflow_orchestrator"
    return base + "/docker" if docker_runtime() else base
