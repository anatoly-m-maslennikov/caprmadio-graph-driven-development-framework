---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - graph-app-access
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1104
  derived_from:
    - CA-A-058
---
# Route selected graph context into governed Codex work

## Applicable when

Use this Method when an operator selects graph nodes as the bounded context for a Codex question or governed action.

## Procedure

1. Seal the operator-selected node set with node IDs, source paths, current digests, and the selection frontier.
2. Transfer only that context and its provenance to the selected provider-neutral Skill or MCP operation.
3. Preserve the meaning, input contract, and diagnostic vocabulary of every invoked Tool across the Codex adapter.
4. Return answers and proposed actions with their source-node attribution and unmodified failure states.
5. Require the host's required operator confirmation before any irreversible action and prohibit implicit scope widening, source mutation, secret disclosure, Tool-validation bypass, or host-permission bypass.

## Outcome

Codex work remains bounded to the selected current graph context and attributable to its exact source frontier.

## Failure or stop

Stop when selection digests are stale, the boundary cannot be sealed, a route would widen authority, host permission denies it, or an irreversible action lacks required confirmation.
