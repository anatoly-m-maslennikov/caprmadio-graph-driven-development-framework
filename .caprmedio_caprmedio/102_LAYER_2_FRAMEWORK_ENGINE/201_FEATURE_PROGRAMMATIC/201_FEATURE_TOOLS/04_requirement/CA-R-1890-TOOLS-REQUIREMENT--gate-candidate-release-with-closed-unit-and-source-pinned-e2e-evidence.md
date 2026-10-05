---
atom_id: CA-R-1890
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 00:06:06 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Candidate E2E gate"
  depends_on: [Tool, Release Version, Candidate Manifest, Docker Image, Test Suite, JUnit Report, Journal]
relations:
  relates_to: [CA-R-1879, CA-R-1886]
---
# Summary

Gate a candidate Release with closed Unit and source-pinned E2E evidence

## Scope

One sealed N+1 candidate after compilation and before promotion, without changing frozen N.

## Claim

RELEASE_VERSION **must** accept a candidate Full Gate only after its unchanged closed Unit Gate and its separate Candidate E2E Gate both pass. Every sealed `102_FRAMEWORK_ENGINE/**/test_*.py` package-row module is assigned exactly once to phase `unit` or `candidate_e2e`; omissions, duplicates, unknown phases, failure, error, skip, unavailable prerequisite, or evidence mismatch fail the Full Gate and retain N.

## Details

The Candidate E2E Gate runs only these three sealed source-pinned harness modules against the exact candidate immutable image: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py`, and `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py`. It uses their sealed package-row paths and SHA-256 values, the sealed candidate workspace, and dedicated executor-owned scratch. It invokes a trusted host Docker CLI only through fixed executor command vectors; it accepts no arbitrary command, host path, socket mount, privileged daemon option, ambient image, mutable tag, caller selector, or automatic execution. The query harness receives only the exact immutable candidate image digest; a local mutable tag is never a candidate identity. Existing fixed mocks and harnesses remain the test surface. Candidate E2E observations and both gate results are Journaled with exact candidate/N bindings; neither gate stages, selects, promotes, retires, or mutates source.
