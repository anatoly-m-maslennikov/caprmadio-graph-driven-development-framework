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
      - CAPRMEDIO-GOV-REQU-454--running-logs-use-ndjson
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-REQU-453--artifact-carrier-format-policy
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-217--three-revision-modes-without-evergreen
---

# Requirement — Separate governed, journal, and runtime state

Every DSET project uses three distinct root directories:

| Root | Owned content | Revision behavior |
|---|---|---|
| `.caprmedio/` | Governed artifacts, installed methodology, settings, tools, skill instructions, schemas, templates, and maintained views | Atomic or maintained according to registered artifact type |
| `.caprmedio_journal/` | Canonical durable running logs, event streams, audit trails, and other ordered record sequences | Append-only |
| `.caprmedio_runtime/` | Caches, scratch files, temporary materializations, process state, and other reconstructible working data | Disposable |

Every persisted DSET running log uses NDJSON under `.caprmedio_journal/` as its
canonical carrier. Each appended line is one complete UTF-8 JSON record
followed by a newline. Accepted records are never edited, reordered, or
deleted. Rotation and retention may create or seal carriers without rewriting
accepted records.

Nothing under `.caprmedio_runtime/` may be the only copy of governed truth, durable
history, or canonical evidence. The directory may be removed between runs
without changing project meaning or losing accepted journal records.

TOON may represent a selected journal frontier as a generated maintained view.
A disposable rendering may live under `.caprmedio_runtime/`; a promoted governed
view lives under `.caprmedio/`. In both cases, the NDJSON sequence remains canonical
for the recorded observations.

Git-tracking, retention, rotation, and optional external replication of
`.caprmedio_journal/` are separate project policies. They do not change its
append-only semantics or make it disposable runtime state.

## Primary claim

DSET separates governed project state, canonical append-only history, and
disposable runtime state into `.caprmedio/`, `.caprmedio_journal/`, and
`.caprmedio_runtime/`.

## Rationale

The boundary prevents canonical observations from being deleted with runtime
scratch data while keeping high-churn append-only history separate from
human-governed artifacts and executable methodology.
