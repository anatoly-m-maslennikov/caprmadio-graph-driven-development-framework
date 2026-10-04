---
atom_id: CA-P-1528
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Fresh immutable-image query Workflow E2E"
  depends_on: [Implementation, Workflow, Action, Tool, MCP, Journal, Evaluation]
version: 1
updated_at: "2026-10-05 00:02:29 +0400"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1529]
---
# Summary

prove query workflows in a fresh immutable image

## Objective

Within <=15 minutes, prove both query Workflows through the integrated existing MCP/orchestrator route in a freshly built immutable image. No host-mount substitution, source/RMED revision, or broad Docker inventory.

### Exact inputs, output, ownership, and gate

Inputs: accepted/passing P1527 integration and current Docker golden harness. Ownership: the query-specific fresh-image E2E fixture/test additions under the existing Docker harness and its exact evidence record. Output: image identity plus actual two-route E2E results, source snapshot and truthful Workflow/Action Journal evidence.

P1527 is a true dispatch blocker. Verify default IDs, selected fetch, allowed filters/statuses/properties, pagination/coverage, all required diagnostics, no arbitrary evaluation or secret return, read-only/no-authority behavior, and no undeclared host code/dependencies. A failed/blocked image path remains unfinished with a typed Concern; P1123's wider image closure is separate.

### Definition of Done

Fresh-image proof covers both routes and required negative cases with retained results; an image build or host-only pass is insufficient.
