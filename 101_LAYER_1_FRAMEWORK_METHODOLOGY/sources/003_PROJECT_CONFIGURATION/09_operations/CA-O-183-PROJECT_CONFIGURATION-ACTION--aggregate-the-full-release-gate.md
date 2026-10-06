---
atom_id: CA-O-183
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Aggregate the full Release Gate"
  depends_on: [Action, Test, Docker Image, Framework Package, Journal]
version: 2
updated_at: "2026-10-05 21:41:23 +0000"
relations:
  relates_to: [CA-O-164, CA-O-185, CA-O-186, CA-O-182, CA-O-184, CA-R-1525, CA-R-1720]
---
# Summary

Aggregate the full Release Gate

## Action

Aggregate the full Release Gate **means** the read-only decision over the exact closed-unit, image-canary and host Candidate E2E receipts for one frozen N/N+1 candidate.

## Details

Every receipt must name the same candidate manifest, source frontier, compiled output, package, immutable image and parent lineage. The Unit receipt must cover every declared testcase except exactly `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py`, and `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py`; the E2E receipt must cover every testcase in those exact three modules. Every declared testcase must terminal-pass: skipped, excluded, missing or zero-coverage testcase is non-pass. Missing, stale, mixed-candidate, partial or unjournalable evidence is non-pass. This Action creates no runtime/Skill selection, image removal, retry, Docker effect or new authority.
