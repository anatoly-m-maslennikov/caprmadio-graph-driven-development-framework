"""An explicit scheduler namespace; native state is never silently imported."""

import os


def docker_runtime():
    value = os.environ.get("CAPRMEDIO_RUNTIME_NAMESPACE", "")
    if value not in ("", "docker"):
        raise ValueError("Unsupported runtime namespace")
    return value == "docker"


def implementation_mock_runtime():
    """Only the explicit Docker mock startup selects the fixed mock callback."""
    mode = os.environ.get("CAPRMEDIO_AGENT_MODE", "")
    if mode not in ("", "codex", "mock"):
        raise ValueError("Unsupported Agent runtime mode")
    if mode == "mock" and not docker_runtime():
        raise ValueError("Implementation mock requires explicit Docker startup")
    return mode == "mock"


def control_directory():
    base = ".caprmedio_install/workflow_orchestrator"
    return base + "/docker" if docker_runtime() else base
