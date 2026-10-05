---
atom_id: CA-O-181
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Run host-capable Candidate E2E"
  depends_on: [Action, Test, Docker Image, Framework Package, Journal, Operator]
version: 2
updated_at: "2026-10-05 21:41:23 +0000"
relations:
  relates_to: [CA-O-164, CA-O-186, CA-O-182, CA-R-1525, CA-R-1720]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-181-PROJECT_CONFIGURATION-ACTION--run-host-capable-candidate-e2e.md
  source_atom_id: CA-O-181
  source_atom_revision: 2
  source_sha256: 421a2e43e5d3d020c9769ecc288f4b12ec8f13ecfd3cd2a5a8fb7605fc7dae2a
  original_relations_sha256: 7585aa2fe832080cf75a783d62b089a905536753cf2ea9aed709873323e1dc3b
---
# Summary

Run host-capable Candidate E2E

## Action

Run host-capable Candidate E2E **means** one explicitly authorized host-capable controller execution against CA-O-186's exact candidate image, package, source frontier and N/N+1 bindings.

## Details

The exact E2E inventory is: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py`, and `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py`. Every declared testcase in all three modules must terminal-pass; skipped, excluded, missing or zero-coverage testcase is non-pass. The frozen Docker worker has no Docker socket and cannot claim this phase. A registered explicit host-capable controller and its exact declared capability are required; missing, denied, unsafe, unavailable, stale, non-passing or unjournalable capability yields its actual non-pass outcome. This Action never selects N+1, promotes, retires, mutates sources, expands mounts, exposes credentials or substitutes a cached/focused result. It records one recoverable Journal result bound to the exact candidate and image identity.
