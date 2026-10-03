---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - framework-engine-mcp
version: 1
updated_at: 2026-08-23 17:40:00 +0400
relations:
  method_for:
    - CA-R-1106
  derived_from:
    - CA-A-057
---
# Discover current immediate Tool units

## Applicable when

Apply when MCP must refresh the project-local exposed Tool set.

## Procedure

1. Resolve the current project graph and its immediate Tool units owned by `TOOLS`.
2. Match each unit to its canonical Tool folder and current enablement decision.
3. Exclude nested helpers and non-Tool folders from the resulting source set.

## Outcome

MCP has one current, authority-derived source set for Tool exposure.

## Failure or stop

Stop discovery when the graph, unit identity, enablement decision, or canonical Tool folder is unresolved.
