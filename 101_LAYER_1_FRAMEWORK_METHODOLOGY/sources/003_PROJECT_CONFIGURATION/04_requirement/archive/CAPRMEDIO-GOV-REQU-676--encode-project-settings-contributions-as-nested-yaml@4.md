---
subject_scopes:
  - settings
version: 4
updated_at: 2026-08-22 01:56:15
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-675--encode-project-setting-values-in-owning-rmed-atoms
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Encode configuration surfaces in owning Atoms

GOVERNANCE may encode an owning Atom's optional machine-readable contribution to generated Project Graph State under one top-level `project_graph_state` YAML map only when it faithfully represents that Atom's own governed claim. It may declare registered facts, allowed values, defaults, or structural contributions, but must not encode current operator-selected configuration values or a `project_settings` contribution; current selections belong only to the Project Configuration Atom.
