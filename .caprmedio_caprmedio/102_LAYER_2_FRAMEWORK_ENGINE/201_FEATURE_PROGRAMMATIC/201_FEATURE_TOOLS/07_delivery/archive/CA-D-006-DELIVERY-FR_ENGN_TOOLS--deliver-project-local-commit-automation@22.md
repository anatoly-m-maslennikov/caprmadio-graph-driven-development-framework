---
subject_scopes:
  - provenance
version: 22
updated_at: 2026-08-23 16:45:00 +0400
relations:
  delivery_for:
    - CA-M-087
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

Deliver four peer Tool units: `COMMIT_TRIGGER`, `COMMIT_CONTEXT`, `APPEND_CHANGE_RECORDS`, and `COMMIT_CHANGE_SET`. Their canonical source carriers and shared libraries live under `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS`; `INSTALL_TOOLS` publishes content-addressed self-contained releases under `.caprmedio_install`, while mutable operational state stays under `.caprmedio_runtime`.

Registered adapters and authorized MCP Atom mutations submit a sealed Initiative action to `COMMIT_TRIGGER`, which durably acknowledges one idempotent outbox item and returns. Scheduled context workers are read-only and may run concurrently. Journal workers prepare and append canonical action records independently, using one writer or batcher per shared Journal carrier. `COMMIT_CHANGE_SET` alone owns the repository-scoped fenced Git lease: it creates real-change commits containing only their frozen action targets and the Initiative-based message, or later Journal-only batch commits containing only selected Journal carriers. It never mixes those classes and never treats Journal append as a Git-gate operation.

The release provides explicit install, status, enable, disable, uninstall, recovery, and reconciliation controls. Status is read-only and reports enabled adapters, outbox and gate state, pending or blocked work, last completed real-change and Journal batch, and deterministic recovery instructions. Hooks and adapters are transport only: they do not decide Atom semantics, append a Journal record, or bypass the gate. Installation preserves conflicting `core.hooksPath` state by failing closed without backup copies or mutation.
