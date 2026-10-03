---
subjects:
  declared:
    continuant:
      - project-settings
    occurrent:
      - evaluation
version: 6
updated_at: 2026-08-23 17:53:53 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1070
---
# Rebuild the Scope Unit Graph and Sources Projection from Configuration Authority

## Test case

**Fixture:** Remove both generated Project Scope Unit Graph outputs from an
isolated current-project fixture whose Project Configuration binding and
admitted active `project_scope_unit_graph` or `project_graph_state`
contributions are valid.

**Expected result:** One authorized generator run recreates both outputs from
the exact Configuration revision, current graph structure, admitted sources,
and applicable Journal inputs, with exact per-value bindings and without
reading a prior Projection.
