---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-177
  derived_from:
    - CA-A-057
---
# Reject one stale MCP project frontier

## Claim checked

An MCP invocation must bind to one current project, installed release, graph frontier, and registry revision.

## Test case

Invoke one Tool through a registry made stale by a changed project frontier.

## Acceptance criteria

MCP rejects the invocation explicitly and exposes enough provenance to identify the stale boundary.

## Failure disposition

Stop before Tool execution; do not guess a current release or project root.
