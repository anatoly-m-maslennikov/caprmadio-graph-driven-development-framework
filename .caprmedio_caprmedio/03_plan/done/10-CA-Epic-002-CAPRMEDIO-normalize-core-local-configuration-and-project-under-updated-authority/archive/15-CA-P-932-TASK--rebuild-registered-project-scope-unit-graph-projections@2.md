---
atom_id: CA-P-932
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Project Scope Unit Graph Projections
    occurrent:
      - Project Scope Unit Graph Projection Rebuild
  depends_on:
    occurrent:
      - CA-P-931
version: 2
updated_at: 2026-08-31 20:43:58 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Rebuild Registered Project Scope Unit Graph Projections

**when** CA-P-931 is Done, **then** the Assignee **must** rebuild both registered persistent Project Scope Unit Graph Projections from the migrated generator and exact current source frontier.

## Scope

`((.caprmedio_caprmedio/project_scope_unit_graph.projection.toml) union (.caprmedio_caprmedio/project_scope_unit_graph_sources.projection.toml) union (their active registration authority) union (the migrated generator and exact declared sources))`

## Definition of Done

the Task is **not done if** (**either** Projection retains a retired source path, generator path, topology row, Project identity, **or** digest **or** the two Projections disagree about their source frontier **or** output lacks generation procedure, updated-at value, exact source digest, **or** deterministic output digest **or** deleting both Projections prevents byte-identical regeneration **or** a Projection gains independent authority).

## Details

rebuild **only** the two registered persistent Scope Unit Graph Projections. preserve on-demand Entity Graphs and Subject indexes as non-persistent views.

## Completion Evidence

The selected installed `GENERATE_PROJECT_GRAPH_STATE` Tool rebuilt exactly the two registered persistent Projections from the resolved revision-4 nested Local Configuration receipt and 13 active typed Scope Unit Directory Carriers. Both TOML Projections share the exact source frontier, lowercase `caprmedio` identity, current control root, generation procedure, and non-authoritative status. Deleting both outputs and regenerating produced the same deterministic output-set digest; a repeated regeneration reported no change. Full falsifiable evidence is stored in `execution_evidence/CA-P-932-project-scope-unit-graph-projection-rebuild.projection.json`.
