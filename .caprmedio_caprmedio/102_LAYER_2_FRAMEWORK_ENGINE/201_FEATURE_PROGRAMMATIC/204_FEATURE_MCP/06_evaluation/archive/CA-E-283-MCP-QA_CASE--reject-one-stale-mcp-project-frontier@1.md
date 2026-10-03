---
atom_id: CA-E-283
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:40:00 +0400
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
