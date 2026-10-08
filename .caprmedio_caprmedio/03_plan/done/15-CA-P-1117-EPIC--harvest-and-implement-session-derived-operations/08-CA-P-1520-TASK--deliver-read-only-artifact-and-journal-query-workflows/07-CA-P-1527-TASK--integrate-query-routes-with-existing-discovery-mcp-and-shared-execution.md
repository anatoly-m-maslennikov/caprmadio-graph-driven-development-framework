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
version: 5
updated_at: "2026-10-05 02:06:04 +0000"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1528]
---
# Summary

integrate query routes with existing discovery mcp and shared execution

## Objective

Within <=15 minutes, integrate the two accepted Tools into the existing discovery/MCP/orchestrator/shared Run Journal path. Do not create a second server/executor, treat registration as execution, alter A1142 now, or change original13 packets.

### Exact inputs, output, ownership, and gate

Inputs: accepted P1618@1 current Artifact source frontier, P1619@1 current W14 binding receipt, and P1535 final Journal exact IDs/Versions/paths/hashes; P1532 remains historical Artifact acceptance only; accepted P1547 repaired combined Tool coverage and passing P1525/P1526 completion; accepted P1543 current fifteen-route MCP source/RMED from P1542; accepted P1552's fifteen-route CA-D-521 queue admission. P1533 and P1544 are completed rejected reviews, not admission. Read current `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/implementation_server.py`, `selected_routes.py`, the one `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json`, current APPS/WORKFLOW_ORCHESTRATOR/selected_execution.py, and their tests. P1542/P1551 own source changes separately; this packet owns existing integration files, query native handlers in selected_execution.py, source-bound derived manifest and necessary consumer tests only. Preserve P1536/P1540/P1541 Step packet and Run identity changes. No second server, executor, filter grammar or Journal writer.

Output: two source-bound routes in the existing stack, with discovery and actual admitted execution (not merely registration), preserving read-only semantics, source snapshots, and one shared Journal support. The single manifest expands from thirteen to fifteen only after P1543 and P1552 accept the source admission boundaries. Verify both routes through existing consumers, default/selected returns and diagnostics, no credential/secret delivery, and truthful Workflow/Action records only for actual admitted execution. Journal snapshot capture precedes its own Run records; pagination continues the same admitted snapshot. P1618, P1619, P1535, P1543, P1547, P1552, P1525 and P1526 are true dispatch blockers. Stage integration work by separately bound remainder Tasks if this packet cannot finish within fifteen minutes.

### Definition of Done

The existing route contract and consumer proof cover both query Workflows without duplicate server/executor or regressions claimed for original13; fresh-image proof remains P1528.

## Current result frontier

Current source and binding are accepted, not all consumer execution. CA-P-1618@1 accepts O158@4 and the seven companion sources. CA-P-1619@1 rebinds the closed fifteen-route contract to those exact bytes; independent review accepted that minimal rebind and eight focused development-worker tests passed. C451 is resolved for the source-order/admission defect. P1604 still requires actual admitted MCP/queue execution, currently blocked by the designated host test environment C449; P1528 still requires actual fresh-image proof. This Task remains Active until those consumer gates are satisfied. Existing historical fifteen-route evidence is not a sixteen-route release proof.
