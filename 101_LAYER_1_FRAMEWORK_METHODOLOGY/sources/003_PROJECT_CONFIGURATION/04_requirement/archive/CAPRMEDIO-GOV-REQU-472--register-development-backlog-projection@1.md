---
subject_scopes:
  - artifact-catalog
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-434--release-plan-is-maintained-definition
  child_of:
    - CAPRMEDIO-META-REQU-278--generate-development-backlog-from-its-journal
---
# Register the Development Backlog Projection

GOV registers `development_backlog` as the internal planning Projection Type
with the Delivery Content role.

Each project has at most one active Development Backlog. Its carrier contains
one-line non-authoritative candidates grouped under unscheduled, current target
version, and future target version sections. It may link promoted Atoms but
cannot establish, restate, override, or satisfy their claims.

The Development Backlog is directly updated under the governed release-
planning procedure. It declares no source frontier because its candidates are
planning inputs rather than a representation compiled from current authority.
Git records every persisted revision.

## Rationale

A dedicated Projection Type preserves a cheap movable planning surface without
turning backlog lines into Atoms or overloading source-derived Catalog, Map, or
Hub Projections.
