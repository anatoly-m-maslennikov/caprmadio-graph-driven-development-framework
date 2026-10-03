---
atom_id: CAPRMEDIO-META-REQU-127
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Governance Origin
  depends_on:
    continuant:
      - semantics
project_graph_state:
  artifacts:
    routing:
      enabled_governance_origins:
        - internal
        - external
version: 13
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-127-CORE_META_MODEL-CORE-REQUIREMENT--define-two-governance-origins.md
---
# Define two Governance origins

Governance origin classifies **where** a governed Artifact's primary meaning is owned. It has **`=2`** values:

- `internal` **means** the current project establishes **and** owns the meaning;
- `external` **means** an identified source outside the current project establishes **or** imposes the meaning, while the project records **and** binds itself to that source.

Governance origin is independent of Artifact form, Content role, structural scope, provenance, **and** graph relations. A graph relation is a typed frontmatter edge **and** does **not** create another Governance origin.

The current project boundary is ambient. SEMANTICS owns these two meanings; GOVERNANCE registers the concrete Types **and** carrier rules admitted at their coordinates.
