---
subject_scopes:
  - layout
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-METH-019--classify-artifact-role-separately-from-semantic-type
      - CAPRMEDIO-GOV-REQU-401--control-runtime-and-scratch-boundaries
---

# Requirement — Keep hub navigation stable and folder-level

A hub may directly list:

- stable child areas and their hubs;
- folders that contain atomic artifacts;
- evergreen specifications and plans;
- settings and other long-lived non-atomic files.

A hub never enumerates individual Decision, Question, Problem, QA, or other
atomic carriers. Adding an atom therefore does not require a hub edit. The hub
also never lists or links any file or directory below `.caprmedio_runtime/`; runtime
state is transient and outside durable navigation.

## Primary claim

Hubs represent atomic artifacts only through their containing folders, list evergreen settings and other long-lived non-atomic carriers, and never list or link a .caprmedio_runtime descendant.

## Rationale

Folder-level navigation stays stable as immutable atoms accumulate, while long-lived owners remain directly discoverable and transient runtime state never leaks into the durable navigation surface.
