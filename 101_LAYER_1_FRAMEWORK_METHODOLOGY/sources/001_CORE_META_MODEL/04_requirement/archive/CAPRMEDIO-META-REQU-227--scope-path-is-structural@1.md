---
subject_scope: scope-topology
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-193--structural-scope-path
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-189--work-area-scope
      - CAPRMEDIO-META-REQU-211--type-derived-artifact-routes
---

# Requirement — Keep Scope path structural

Scope path is a project-relative, ordered, and extensible structural coordinate.
It may address layers, features, feature groups, declared Work Areas, or their
configured compositions.

The current project is ambient and never repeated in `scope_path`. Project
scope therefore uses an empty path. Scope may govern ownership, applicability,
inheritance, and identity, but it never changes Revision mode, Content role, or
Governance locus.

## Rationale

Separating structural placement from semantic routing allows the same meaning
to apply at different project scales without multiplying semantic types.
