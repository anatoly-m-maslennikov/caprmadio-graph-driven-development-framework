---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - settings
version: 14
updated_at: "2026-09-09 21:56:59 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-675--keep-configuration-values-in-the-project-configuration-atom
    - CA-R-1054
---
# Encode configuration surfaces in owning Atoms

an owning Atom **may** carry its optional machine-readable contribution to the generated Project Scope Unit Graph under one top-level `project_scope_unit_graph` **or** `project_graph_state` YAML map **only** **when** it faithfully represents that Atom's own governed Claim. it **may** declare registered facts, allowed values, defaults, **or** structural contributions, but **must not** encode current Operator-selected Project identity, Atom prefix, Authority Mode values, **or** a `project_settings` contribution; those current selections belong **only** to the Project Settings Artifact.
