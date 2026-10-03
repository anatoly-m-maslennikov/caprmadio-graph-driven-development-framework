---
subject_scopes:
  - provenance
version: 23
updated_at: 2026-08-25 01:49:10 +0400
relations:
  delivery_for:
    - CA-M-087
    - CA-M-182
    - CA-R-802
    - CA-R-803
    - CA-R-804
    - CA-R-805
    - CA-R-812
    - CA-R-1121
    - CA-R-1124
    - CA-R-1064
    - CA-R-1065
---
# Deliver project-local commit automation

Deliver four peer Tool units, COMMIT_TRIGGER, COMMIT_CONTEXT, APPEND_CHANGE_RECORDS, and COMMIT_CHANGE_SET, plus one independently supervised repository-local COMMIT_AUTOMATION service. Canonical source and shared libraries live under 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS; INSTALL_TOOLS publishes a content-addressed self-contained release under .caprmedio_install; mutable operational state stays below .caprmedio_runtime.

The Codex transport is one asynchronous PostToolUse command Hook. It normalizes one host event, atomically renames one immutable envelope into .caprmedio_runtime/state/commit_automation/inbox/, and exits. It contains no broad scan, graph traversal, before-event snapshot, context gathering, Journal append, Git mutation, retry, or pipeline-worker spawn. The background service consumes the durable inbox, performs low-frequency repository reconciliation, asks one pure manager for the admissible graph or next command, persists every transition, and lets a mechanical Scheduler dispatch COMMIT_CONTEXT -> APPEND_CHANGE_RECORDS -> COMMIT_CHANGE_SET.

The service preserves accepted work across Hook completion, manager termination, pause, stop, start, reload, crash, and release replacement. It enforces one active Git-mutating pipeline per repository; later events mark the repository pending. Workers are atomic and non-deciding. COMMIT_CHANGE_SET owns only the sealed Git boundary and never imports or orchestrates its peers. Real-change commits and Journal-only commits remain separate gate items.

The release provides install, status, enable, disable, pause, resume, stop, start, reload, uninstall, recovery, and reconciliation controls. Status reports adapters, process and selected release, queue and action phases, gate and lease state, budget and circuit state, pending or blocked work, dead letters, last completed real-change and Journal batch, and deterministic recovery instructions. Budget exhaustion and integrity-sensitive failures pause autonomous execution for Operator recovery. Hooks and adapters are transport only; Git Hooks remain narrow synchronous Evaluations or observers.
