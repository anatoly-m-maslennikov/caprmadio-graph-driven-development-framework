---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1106
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Discover current immediate Tool units

## Applicable when

Apply **when** MCP **must** refresh the project-local exposed Tool set.

## Procedure

1. Resolve the current project graph **and** its immediate Tool units owned by `TOOLS`.
2. Match each unit **to** its canonical Tool folder **and** current enablement decision.
3. Exclude nested helpers **and** non-Tool folders from the resulting source set.

## Outcome

MCP has one current, authority-derived source set for Tool exposure.

## Failure or stop

Stop discovery **when** the graph, unit identity, enablement decision, **or** canonical Tool folder is unresolved.
