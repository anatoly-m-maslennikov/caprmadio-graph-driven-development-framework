"""Public, importable COMMIT_TRIGGER Tool interface."""

from .commit_trigger import (
    AdapterSpec,
    FileState,
    PipelineCorrelation,
    ToolError,
    detect_watch_observations,
    emit_triggers,
    emit_from_registered_adapter,
    resolve_codex_session,
    scan_governed_files,
    watch_triggers,
)

__all__ = [
    "AdapterSpec",
    "FileState",
    "PipelineCorrelation",
    "ToolError",
    "detect_watch_observations",
    "emit_triggers",
    "emit_from_registered_adapter",
    "resolve_codex_session",
    "scan_governed_files",
    "watch_triggers",
]
