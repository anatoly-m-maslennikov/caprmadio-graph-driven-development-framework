---
atom_id: CA-P-1756
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
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
  governs: "Restore authenticated HTTP MCP and protocol coverage"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1757, CA-P-1655]
---
# Summary

Restore authenticated HTTP MCP and protocol coverage

## Objective

Implement the accepted optional Streamable HTTP transport beside unchanged stdio and prove its real SDK session behavior.

## Details

204_MCP HTTP adapter/gateway, Docker lifecycle overlay and their tests; http_mcp_restore plus read-only http_security_review. R1884/1885 M341/342 E584/585 D578. Tokens stay ephemeral and never enter committed files or logs.

This is a restored-delivery composite. Independently bounded <=15-minute assignments separate adapter/lifecycle implementation, host SDK protocol tests, and read-only security review. http_mcp_restore exclusively owns 204_MCP/http_server.py, server.py, hot_reload.py, test_hot_reload_http.py, Docker runtime.py/entrypoint.py/mcp-http.compose.yaml and test_mcp_http_runtime.py. http_security_review is read-only and owns no mutations. Corrections receive a separate bounded producer slice and independent re-review. Root owns integration and Git; P1757 remains the distinct actual Docker proof.

## Definition of Done

Independent security review accepts; host SDK tests prove discovery/calls/reload/drain/auth/shutdown. Actual Docker proof is P1757.

## Pre-execution review

Root accepts this bounded repair/restoration against Operator authority, DRY, preservation of valuable information and the latest continuation. Keep installed N intact and distinguish local tests from required actual runtime gates.
