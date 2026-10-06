"""An explicit scheduler namespace; native state is never silently imported."""

import os


def _runtime_namespace():
    """Return the one explicit scheduler namespace selected for this process."""
    value = os.environ.get("CAPRMEDIO_RUNTIME_NAMESPACE", "")
    if value not in ("", "docker", "release-host"):
        raise ValueError("Unsupported runtime namespace")
    return value


def docker_runtime():
    return _runtime_namespace() == "docker"


def release_host_runtime():
    """Only the expressly started Release host executor selects this namespace."""
    return _runtime_namespace() == "release-host"


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
    if release_host_runtime():
        return base + "/release-host"
    return base + "/docker" if docker_runtime() else base
