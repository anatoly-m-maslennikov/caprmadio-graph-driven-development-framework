---
atom_id: CA-P-1757
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 2
updated_at: "2026-10-08 04:07:03 +0400"
subjects:
  governs: "Prove the localhost HTTP MCP Docker path"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1655, CA-P-1124]
---
# Summary

Prove the localhost HTTP MCP Docker path

## Objective

Verify the opt-in HTTP MCP service in an actual isolated candidate container with an explicit loopback port and ephemeral test token. This is required FIRST CUT evidence alongside the six scoped Workflows, existing stdio MCP/orchestrator compatibility, and shared journaling.

## Details

Root owns actual Docker effects; current accepted HTTP packet and P1756 gate execution. Use a disposable project and explicit runtime environment only; no Codex Agent start, host socket mount, baked secret, or undeclared host implementation mount. Preserve permissions, secret isolation, currentness, identity, status-model and Journal-evidence checks.

Estimated bounded slice: <=15 minutes. Workers share the checkout, preserve other edits and do not stage or commit. Root owns integration and Git. Preparation does not prove runtime execution.

## Definition of Done

Actual authenticated initialize/list/call, health and lifecycle tests pass on localhost; invalid credentials, Host and Origin fail before tools; stdio stays usable; and startup/shutdown lifecycle evidence is retained. This must prove HTTP in Docker, not only host or build behavior. It does not claim all-sixteen/full-release coverage, N+1 promotion, automatic Release Version/prior-image retirement, or completion of deferred Scope Unit mutations, Revert, graph builders, or standalone advanced Artifact/Journal queries.

## Pre-execution review

Root accepts this bounded repair/restoration against Operator authority, DRY, preservation of valuable information and the latest continuation. Keep installed N intact and distinguish local tests from required actual runtime gates.
