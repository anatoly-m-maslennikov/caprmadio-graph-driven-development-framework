---
subject_scopes:
  - runtime
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-400--hidden-project-control-root
---

# Requirement — Separate control, runtime, and scratch state

The canonical repository-local boundaries are:

- `.caprmedio/` — committed DSET settings, governance, evergreen artifacts, atomic
  artifacts, Version records, schemas, templates, and generated views;
- `.caprmedio_runtime/` — ignored, bounded, resumable project runtime state,
  including runs, session checkpoints, caches, readiness records, and recovery
  backups; and
- `/tmp/` on POSIX — disposable DSET process scratch and test workspaces that
  must be removed when their owning operation exits. Native Windows uses its
  operating-system temporary root because `/tmp` is not a portable Windows
  location.

Ambient POSIX `TMPDIR`, `TEMP`, or `TMP` values must not redirect DSET scratch
workspaces into the repository. Cleanup errors are failures, not ignored
success. A test or subprocess must leave no `dset-*` scratch directory in the
repository after normal completion or a handled failure.

Short-lived same-directory files or directories used exclusively to preserve
atomic publication may live beside their destination. They are transactional
swap state rather than resumable runtime or scratch workspaces, and must be
replaced or removed before the operation returns.

Persisted control and runtime paths are repository-root-relative. Markdown
links may remain relative to their owning file. Schema 1.0–1.2 layouts and the
schema 1.3 `.caprmedio/runtime/` location remain read-only compatibility inputs;
current initialization and writes use `.caprmedio_runtime/`.

This Requirement atom is immutable. Later correction requires a successor and
an append-only lifecycle event.

## Primary claim

A DSET project separates committed control state under .caprmedio, ignored resumable runtime state under .caprmedio_runtime, and disposable scratch workspaces under the host temporary root.

## Rationale

Control truth, resumable operational state, and disposable process scratch have different authority, retention, and cleanup semantics and therefore require visibly distinct roots.
