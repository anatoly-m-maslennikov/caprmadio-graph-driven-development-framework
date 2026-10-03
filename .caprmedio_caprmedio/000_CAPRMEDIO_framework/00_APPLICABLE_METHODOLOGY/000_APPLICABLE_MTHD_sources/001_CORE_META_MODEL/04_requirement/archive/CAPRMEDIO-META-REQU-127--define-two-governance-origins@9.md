---
cce_version: cce_1
cce_form: definition
subjects:
  declared:
    continuant:
      - semantics
project_graph_state:
  artifacts:
    routing:
      enabled_governance_origins:
        - internal
        - external
tier: core
version: 9
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
---
# Define two Governance origins

Governance origin classifies where a governed Artifact's primary meaning is owned. It has exactly two values:

- `internal` means the current project establishes and owns the meaning;
- `external` means an identified source outside the current project establishes or imposes the meaning, while the project records and binds itself to that source.

Governance origin is independent of Artifact form, Content role, structural scope, provenance, and graph relations. A graph relation is a typed frontmatter edge and does not create another Governance origin.

The current project boundary is ambient. SEMANTICS owns these two meanings; GOVERNANCE registers the concrete Types and carrier rules admitted at their coordinates.
