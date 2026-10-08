---
atom_id: CA-P-1770
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 2
updated_at: "2026-10-06 04:12:31 +0000"
subjects:
  governs: "Implement the opt-in HTTP gateway"
  depends_on: [Implementation, Evaluation, Workflow, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1756]
  blocks: [CA-P-1771, CA-P-1772]
---
# Summary

Implement the opt-in HTTP gateway

## Objective

Implement the opt-in HTTP gateway under the parent's exact source contract.

## Details

http_mcp_restore exclusively owns 204_MCP/http_server.py, server.py, hot_reload.py and WORKFLOW_ORCHESTRATOR/docker/entrypoint.py, runtime.py, mcp-http.compose.yaml.

Estimated execution slice <=15 minutes. Preserve other workers' changes. Root alone owns index, commits and actual shared runtime effects. Tests and disposable smoke evidence are not release promotion.

## Definition of Done

The optional adapter and lifecycle honor R1884/1885 M341/342 D578; unchanged stdio regression passes.

## Pre-execution review

Root accepts this exclusive bounded assignment as the minimal current parent repair. Preserve installed N and truthful observed effects.

## Recorded verification

e63cb5457; the accepted optional adapter and lifecycle preserve stdio default and explicit HTTP configuration. Root's full 18-case transport/runtime suite passed.
