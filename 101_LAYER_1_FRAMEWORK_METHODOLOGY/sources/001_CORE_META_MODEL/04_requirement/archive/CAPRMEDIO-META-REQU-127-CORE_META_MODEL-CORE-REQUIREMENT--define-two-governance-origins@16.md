---
atom_id: CAPRMEDIO-META-REQU-127
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Governance Origin"
  depends_on:
    - "semantics"
project_graph_state:
  artifacts:
    routing:
      enabled_governance_origins:
        - internal
        - external
version: 16
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CA-M-001
---
# Define two Governance origins

Governance origin classifies **where** a governed Artifact's primary meaning is owned. It has **`=2`** values:

- `internal` **means** the current project establishes **and** owns the meaning;
- `external` **means** an identified source outside the current project establishes **or** imposes the meaning, while the project records **and** binds itself to that source.

Governance origin is independent of Artifact form, Content role, structural scope, provenance, **and** graph relations. A typed graph relation does **not** create another Governance Origin; its Carrier encoding is governed by CA-D-268.

The current project boundary is ambient. Requirement authority defines these two values **and** the admitted Types; Delivery authority governs their Carrier encoding.
