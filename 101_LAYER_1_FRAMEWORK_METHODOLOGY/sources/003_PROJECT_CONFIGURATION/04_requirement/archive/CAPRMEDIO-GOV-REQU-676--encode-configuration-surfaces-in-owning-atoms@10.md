---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - settings
version: 10
updated_at: 2026-08-29 01:16:37 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-675--keep-configuration-values-in-the-project-configuration-atom
    - CA-R-1054
---
# Encode configuration surfaces in owning Atoms

GOVERNANCE **may** encode an owning Atom's optional machine-readable contribution to the generated Project Scope Unit Graph under one top-level `project_scope_unit_graph` **or** `project_graph_state` YAML map **only** **when** it faithfully represents that Atom's own governed claim. It **may** declare registered facts, allowed values, defaults, **or** structural contributions, but **must not** encode current operator-selected configuration values **or** a `project_settings` contribution; current selections belong **only** to the Project Configuration Atom.
