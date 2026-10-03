---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - settings
version: 13
updated_at: 2026-09-04 04:05:44 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-675--keep-configuration-values-in-the-project-configuration-atom
    - CA-R-1054
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CAPRMEDIO-GOV-REQU-676--encode-configuration-surfaces-in-owning-atoms.md
---
# Encode configuration surfaces in owning Atoms

GOVERNANCE **may** encode an owning Atom's optional machine-readable contribution to the generated Project Scope Unit Graph under one top-level `project_scope_unit_graph` **or** `project_graph_state` YAML map **only** **when** it faithfully represents that Atom's own governed Claim. it **may** declare registered facts, allowed values, defaults, **or** structural contributions, but **must not** encode current Operator-selected Project identity, Atom prefix, Authority Mode values, **or** a `project_settings` contribution; those current selections belong **only** to the Project Settings Artifact.
