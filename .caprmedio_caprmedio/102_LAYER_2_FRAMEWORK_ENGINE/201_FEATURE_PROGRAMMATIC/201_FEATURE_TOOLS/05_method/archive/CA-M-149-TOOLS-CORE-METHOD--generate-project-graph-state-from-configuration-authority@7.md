---
subject_scopes:
  - project-settings
version: 7
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CA-R-1070
---
# Generate the Project Scope Unit Graph from Configuration Authority

Resolve exactly one Project Configuration Atom through its governed external
binding and treat it as the sole owner of current operator-selected settings.
Enumerate only applicable active Atom contributions admitted under the
top-level `project_scope_unit_graph` or `project_graph_state` map; use them for
registered facts, allowed values, defaults, structural context, and other
non-configurational Project Scope Unit Graph inputs. Reject every
`project_settings` contribution outside the Configuration Atom.

Generate `.caprmedio/project_scope_unit_graph.projection.toml` and
`.caprmedio/project_scope_unit_graph_sources.projection.toml` from the exact
Configuration revision, exact admitted contributions, current graph structure,
and applicable Journal revisions. Preserve per-value source bindings, canonical
source order where a registered output permits multiple sources, and
deterministic bytes. Never read a prior Projection as semantic input. Fail
before writing either Projection when the Configuration binding or an admitted
source is missing, malformed, unresolved, ambiguous, stale, contradictory, or
incompletely mapped.
