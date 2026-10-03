---
cce_version: cce_1
cce_form: definition
subjects:
  - settings
version: 14
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
    - CAPRMEDIO-META-REQU-627--bind-every-project-scope-unit-graph-value-to-exact-sources
  replacement_of:
    - CAPRMEDIO-GOV-REQU-629--encode-project-settings-projection-rules-as-a-toml-atom
---
# Register Project Scope Unit Graph Projection mechanics

GOVERNANCE MUST register deterministic generation of `.caprmedio/project_scope_unit_graph.projection.toml` and `.caprmedio/project_scope_unit_graph_sources.projection.toml` from the exact current Project Configuration Atom revision, admitted graph Atom contributions, current graph structure, and applicable Journal inputs. Generation MUST preserve exact per-value source bindings and reject missing, ambiguous, stale, contradictory, malformed, or incompletely mapped sources. The generation procedure is provenance only and never grants either Projection authority.
