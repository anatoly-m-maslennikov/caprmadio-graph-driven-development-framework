---
atom_id: CA-R-1886
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-06 00:55:29 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite test execution"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, Methodology, Apps, MCP, Agentic, Skill, JUnit Report, Compiled Candidate]
relations:
  relates_to: [CA-R-1879, CA-R-1890]
---
# Summary

Run every declared Release suite test truthfully

## Scope

The phase-assigned in-tree Framework test execution gates for one sealed Release Version candidate before later release effects.

## Claim

RELEASE_VERSION **must** assign every test case from every sealed in-tree Framework test module exactly once to its closed Unit Gate or its separate Candidate E2E Gate. It accepts the Unit Gate only from its source-bound JUnit evidence and accepts the Full Gate only after that passing Unit evidence and passing candidate-image-bound E2E evidence are aggregated; no case may fail, error, skip, time out, or be omitted.

## Details

The declared suite is every sealed package-row carrier whose source path is `102_FRAMEWORK_ENGINE/**/test_*.py`. Its sealed phase map assigns exactly these three source paths to `candidate_e2e`:

- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py`

Every other declared module is `unit`. The unchanged closed Unit Gate runs all and only the `unit` modules after compilation and before candidate-image construction. Only after it passes may the candidate image be built, inspected, and canaried; only then may the three host-capable E2E harnesses run against that exact immutable image. A focused Tool subset, fixture-only report, unknown or duplicate phase, module exclusion, unexecuted declared case, or Unit-only result is not a Full Gate. Docker-optional and other environment-dependent test cases remain declared cases: an unavailable prerequisite records a non-passing gate rather than silently excluding or skipping them. The Unit report proves each case's binding against the sealed candidate package rows and immutable binding envelope, including the existing schema-2 control-context digest and source probes; E2E evidence proves its own sealed source and candidate-image bindings. A non-passing or incomplete Unit, E2E, or aggregate Full Gate retains N and authorizes no staging, installation, Skill publication, selector change, promotion, image retirement, or source mutation.
