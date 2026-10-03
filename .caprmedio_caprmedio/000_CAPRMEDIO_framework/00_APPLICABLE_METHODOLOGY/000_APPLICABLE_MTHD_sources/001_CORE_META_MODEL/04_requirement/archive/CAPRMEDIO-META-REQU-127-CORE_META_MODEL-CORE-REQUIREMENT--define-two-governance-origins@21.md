---
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
version: 21
updated_at: "2026-09-17 17:40:12 +0000"
relations:
  child_of:
    - CA-M-001
---
# Define two Governance origins

Governance Origin classifies **where** a governed Artifact's primary meaning is owned. Governance Origin has **`=2`** values:

- `internal` **means** the current project establishes **and** owns the meaning;
- `external` **means** an identified source outside the current project establishes **or** imposes the meaning, while the project records **and** binds itself **to** that source.

Governance Origin is independent of Artifact form, Content Role, structural scope, provenance, **and** graph relations. a typed graph relation does **not** create another Governance Origin; its Carrier encoding is governed by CA-D-268.

the current project boundary is ambient. Requirement authority defines these two values **and** the admitted Types; Delivery authority governs their Carrier encoding.
