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
status: Active
version: 1
updated_at: "2026-10-06 03:53:17 +0000"
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

Verify the opt-in HTTP service in an actual isolated candidate container with an explicit loopback port and ephemeral test token.

## Details

Root owns actual Docker effects; current accepted HTTP packet and P1756 gate execution. Disposable project and explicit runtime environment only; no Codex Agent start or host socket mount.

Estimated bounded slice: <=15 minutes. Workers share the checkout, preserve other edits and do not stage or commit. Root owns integration and Git. Preparation does not prove runtime execution.

## Definition of Done

Actual authenticated initialize/list/call, health and lifecycle tests pass on localhost; invalid credentials/Host/Origin fail before tools; stdio stays usable; retain bounded evidence.

## Pre-execution review

Root accepts this bounded repair/restoration against Operator authority, DRY, preservation of valuable information and the latest continuation. Keep installed N intact and distinguish local tests from required actual runtime gates.
