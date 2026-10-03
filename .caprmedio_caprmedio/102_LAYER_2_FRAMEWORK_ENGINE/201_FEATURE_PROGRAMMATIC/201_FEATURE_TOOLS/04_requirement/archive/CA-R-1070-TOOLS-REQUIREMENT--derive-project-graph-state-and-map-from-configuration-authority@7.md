---
subjects:
  declared:
    continuant:
      - project-settings
version: 7
updated_at: 2026-08-23 16:16:20 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d---
# Derive the Project Scope Unit Graph and Sources Projection from Configuration Authority

The Project Scope Unit Graph generator must resolve exactly one governed Project
Configuration Atom as the sole source of current operator-selected values. It
may compose only applicable active Atom `project_scope_unit_graph` or
`project_graph_state` contributions that declare registered facts, allowed
values, defaults, structural context, or other non-configurational inputs. No
ordinary Atom may contribute `project_settings` values.

The generator must derive `.caprmedio/project_scope_unit_graph.projection.toml`
and `.caprmedio/project_scope_unit_graph_sources.projection.toml` from those
exact sources, current graph structure, and applicable Journal inputs; it must
never read either Projection as semantic input, preserve exact per-value
bindings, and fail before writing on missing, malformed, unresolved, ambiguous,
stale, contradictory, or incompletely mapped sources.
