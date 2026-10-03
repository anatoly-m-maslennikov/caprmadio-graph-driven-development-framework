---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - framework-engine-mcp
version: 2
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1115
  derived_from:
    - CA-A-057
---
# Bind one MCP invocation to its current project frontier

## Applicable when

Apply when an MCP service instance discovers or invokes an exposed Tool.

## Procedure

1. Resolve exactly one project root, selected installed Tool release, project-graph frontier, and MCP registry revision.
2. Include sufficient source and revision provenance in discovery and result records.
3. Reject cross-project path escape, unresolved identity, or a stale registry before Tool invocation.

## Outcome

Every MCP operation is attributable to one current project and Tool frontier.

## Failure or stop

Stop at an unresolved or stale frontier; do not guess a project or release.
