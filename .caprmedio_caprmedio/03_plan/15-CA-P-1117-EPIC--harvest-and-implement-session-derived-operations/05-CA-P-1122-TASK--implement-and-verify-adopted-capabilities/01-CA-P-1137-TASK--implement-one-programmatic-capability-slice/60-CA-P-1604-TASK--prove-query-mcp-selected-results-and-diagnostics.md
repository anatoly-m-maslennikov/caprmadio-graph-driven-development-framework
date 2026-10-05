---
atom_id: CA-P-1604
content_role: Plan
type: Plan
label: Task
work_sequence_number: 60
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Prove query MCP selected results and diagnostics"
  depends_on: [Workflow, Action, Implementation, Evaluation, Journal]
version: 2
updated_at: "2026-10-05 00:37:00 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1519]
---
# Summary

Prove query MCP selected results and diagnostics

## Objective

Within <=15 minutes, Add and execute bounded query-specific current MCP tests for selected fields, heading fetch, allowed filters, stable pagination and truthful diagnostics, preserving actual shared recording and source non-mutation.

## Details

Use image sha256:057792974dc2d81f84f99dee5535a44d5ee30513b03f6154381d99aa0bd558cd, declared dependency groups workflow-orchestrator and rmed-workflow-mcp, and separate disposable Runtime Projects. No host Engine mount, assertion relaxation, live CLI or permission bypass. Other independent batches are separate Tasks; coverage counts only the assigned cases.

## Saved frontier

The host driver could not start: the repository virtual environment contains no Python executable. Provisioning the declared groups also failed on distribution-cache directory rename with EPERM in the existing and fresh permitted temporary cache. These attempts stopped. The bundled runtime lacks MCP, PyYAML and DBOS. No actual-image case ran; image tag was unchanged. CA-C-449 preserves the blocker. Prepared harness source does not count as execution or completion.

## Prepared source and verification

Saved test_selected_query_mcp_e2e.py, SHA256 5ff655f344c3bc79ee0ad517a5ba4ff86c97c91ed86f92868f228a090f2c4f33. It reuses the actual shared recorder and fresh MCP client and supplies four opt-in cases for W14/W15 selected fields, hierarchical headings, filters, stable pagination, snapshots and separate refusal diagnostics. No manual Journal or Run facts are inserted. Development-worker discovery passed one carrier check and intentionally skipped four actual-image cases. No runtime started; C449 still prevents functional execution, so this Task remains Active.

## Definition of Done

The assigned current immutable-image cases have exact passing functional evidence, or remain unfinished with their precise protected blocker.
