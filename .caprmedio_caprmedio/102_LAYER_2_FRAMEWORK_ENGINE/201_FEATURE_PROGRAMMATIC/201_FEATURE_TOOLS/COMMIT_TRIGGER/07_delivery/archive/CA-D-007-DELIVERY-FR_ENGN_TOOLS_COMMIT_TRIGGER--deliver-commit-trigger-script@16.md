---
subject_scopes:
  - feature-boundary
version: 16
updated_at: 2026-08-25 01:49:10 +0400
relations:
  delivery_for:
    - CA-R-803
    - CA-R-1124
    - CA-R-1064
---
# Deliver the commit-trigger script

Realize COMMIT_TRIGGER through 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER/commit_trigger.py and its content-identical carrier in the selected installed release. INSTALL_TOOLS, not COMMIT_TRIGGER, owns Tool and Hook installation.

The user-level Codex carrier is one generic asynchronous PostToolUse command Hook with full-value matcher .* and async: true. It resolves the Git root from Hook cwd, requires the exact repository-local caprmedio.codex-hooks = v1 activation, exits without effect when activation or the installed launcher is absent, and otherwise delegates to the stable install-owned commit-trigger launcher. The command identity contains no repository-specific absolute path or release digest.

The launcher validates and normalizes the host payload into one immutable schema-versioned event and atomically renames it into .caprmedio_runtime/state/commit_automation/inbox/<event_id>.json. The event records source, repository, session, turn, Tool-use, Hook event, stable event identity, observation time, and candidate changed targets available from the payload. Repeated event identity is idempotent. Concurrent and out-of-order callbacks write independent events. Intake returns after durable acceptance and performs no repository scan, graph traversal, before-event snapshot, context gathering, Journal append, Git mutation, retry, lifecycle control, or direct worker spawn.

Automatic-commit PreToolUse, SessionStart, and Stop callbacks are not installed. Missed delivery and external edits are reconciled by the independently supervised repository service. Runtime event provenance is compacted to Journal-resolvable identities and receipts after canonical Journal acceptance.
