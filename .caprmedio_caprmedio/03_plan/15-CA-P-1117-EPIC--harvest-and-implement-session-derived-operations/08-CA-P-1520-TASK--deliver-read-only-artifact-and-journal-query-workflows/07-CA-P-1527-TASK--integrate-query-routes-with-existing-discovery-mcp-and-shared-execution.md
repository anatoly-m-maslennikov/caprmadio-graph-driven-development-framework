---
atom_id: CA-P-1527
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
current_scope_unit: caprmedio
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Query route integration with existing discovery, MCP, orchestrator and Journal"
  depends_on: [Implementation, Workflow, Action, Tool, MCP, Journal]
version: 1
updated_at: "2026-10-05 00:02:29 +0400"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1528]
---
# Summary

integrate query routes with existing discovery mcp and shared execution

## Objective

Within <=15 minutes, integrate the two accepted Tools into the existing discovery/MCP/orchestrator/shared Run Journal path. Do not create a second server/executor, treat registration as execution, alter A1142 now, or change original13 packets.

### Exact inputs, output, ownership, and gate

Inputs: accepted P1522/P1524 exact IDs/Versions/paths; passing P1525/P1526 Tool tests; current D547/D548 and their consumer tests, which are closed to original13; current `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py`, `selected_routes.py`, `selected_workflow_bindings.json`, and tests. Ownership is the necessary revisions of the current D547/D548 RMED/route bindings/consumer tests plus those existing integration files; archive meaningful native predecessors when required.

Output: two source-bound routes in the existing stack, with discovery and actual admitted execution (not merely registration), preserving read-only semantics, source snapshots, and one shared Journal support. The route manifest/RMED must expand from thirteen to fifteen only after new source/spec acceptance. Verify both routes through existing consumers, default/selected returns and diagnostics, no credential/secret delivery, and truthful Workflow/Action records only for actual admitted execution. P1522, P1524, P1525, and P1526 are true dispatch blockers.

### Definition of Done

The existing route contract and consumer proof cover both query Workflows without duplicate server/executor or regressions claimed for original13; fresh-image proof remains P1528.
