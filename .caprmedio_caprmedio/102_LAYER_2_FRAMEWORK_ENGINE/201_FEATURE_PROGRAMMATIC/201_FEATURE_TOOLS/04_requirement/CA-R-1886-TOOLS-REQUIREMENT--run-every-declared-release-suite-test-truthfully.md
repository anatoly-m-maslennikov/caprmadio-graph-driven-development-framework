---
atom_id: CA-R-1886
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 22:00:58 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite test execution"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, Methodology, Apps, MCP, Agentic, Skill, JUnit Report, Compiled Candidate]
relations:
  relates_to: [CA-R-1879]
---
# Summary

Run every declared Release suite test truthfully

## Scope

The complete in-tree Framework test-suite execution gate for one sealed Release Version candidate before later release effects.

## Claim

RELEASE_VERSION **must** execute every test case from every sealed in-tree Framework test module exactly once and accept its full-suite gate only from a JUnit report in which every executed case has sealed source-binding evidence, the Methodology, Tools, Apps, MCP, Agentic, and Skill groups and **>=1** compiled-candidate carrier are covered, and no case fails, errors, or skips.

## Details

The declared suite is every sealed package-row carrier whose source path is `102_FRAMEWORK_ENGINE/**/test_*.py`. A focused Tool subset, fixture-only report, module exclusion, or unexecuted declared case is not a full suite. Docker-optional and other environment-dependent test cases remain declared cases: an unavailable prerequisite records an incomplete or failed gate rather than silently excluding or skipping them. The report proves each case's binding against the sealed candidate package rows and immutable binding envelope, not an unverified caller assertion. A non-passing or incomplete gate retains N and authorizes no staging, installation, Skill publication, selector change, image retirement, or source mutation.
