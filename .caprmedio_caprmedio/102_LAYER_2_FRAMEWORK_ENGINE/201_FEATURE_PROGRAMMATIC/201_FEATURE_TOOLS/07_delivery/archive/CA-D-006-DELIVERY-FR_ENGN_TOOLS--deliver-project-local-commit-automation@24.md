---
atom_id: CA-D-006
cce_version: cce_1
cce_form: delivery
subject_scopes:
  - provenance
version: 24
updated_at: 2026-09-04 03:10:59 +0400
relations:
  delivery_for:
    - CA-M-087
    - CA-M-182
    - CA-M-258
    - CA-R-802
    - CA-R-803
    - CA-R-804
    - CA-R-805
    - CA-R-812
    - CA-R-1121
    - CA-R-1124
    - CA-R-1064
    - CA-R-1065
    - CA-R-1385
---
# Deliver project-local commit automation

Deliver four peer Tool units, COMMIT_TRIGGER, COMMIT_CONTEXT, APPEND_CHANGE_RECORDS, and COMMIT_CHANGE_SET, plus one independently supervised repository-local COMMIT_AUTOMATION service. Canonical source and shared libraries live under 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS; INSTALL_TOOLS publishes a content-addressed self-contained release under .caprmedio_install; mutable operational state stays below .caprmedio_runtime.

The Codex transport is one asynchronous PostToolUse command Hook. It normalizes one host event, atomically renames one immutable envelope into .caprmedio_runtime/state/commit_automation/inbox/, and exits. It contains no broad scan, graph traversal, before-event snapshot, context gathering, Journal append, Git mutation, retry, or pipeline-worker spawn. The background service consumes the durable inbox, performs low-frequency repository reconciliation, asks one pure manager for the admissible graph or next command, persists every transition, and lets a mechanical Scheduler dispatch COMMIT_CONTEXT followed by independent real-change and Journal branches. APPEND_CHANGE_RECORDS appends provenance independently; COMMIT_CHANGE_SET creates real-change commits and later Journal-only batch commits through one fenced gate.

The service preserves accepted work across Hook completion, manager termination, pause, stop, start, reload, crash, and release replacement. It enforces one active commit-creating gate item per repository; later commit items remain pending while context gathering and eligible Journal preparation continue independently. Workers are atomic and non-deciding. COMMIT_CHANGE_SET owns only the sealed commit boundary and never imports or orchestrates its peers. Real-change commits and Journal-only commits remain separate gate items.

The release provides install, status, enable, disable, pause, resume, narrow, stop, start, reload, uninstall, recovery, and reconciliation controls. Status reports the active autonomy envelope and Work binding, adapters, process and selected release, queue and action phases, gate and lease state, budget and circuit state, pending or blocked work, dead letters, last completed real-change and Journal batch, and deterministic recovery instructions. Budget exhaustion, envelope expiry or narrowing, and integrity-sensitive failures pause autonomous execution for Operator recovery. Hooks and adapters are transport only; Git Hooks remain narrow synchronous Evaluations or observers. The release performs no branch, upstream, remote, synchronization, push, tag, or release operation.
