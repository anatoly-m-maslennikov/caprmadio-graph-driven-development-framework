---
atom_id: CA-M-346
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 00:06:06 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Candidate E2E procedure"
  depends_on: [Tool, Release Version, Candidate Manifest, Docker Image, Test Suite, JUnit Report, Journal]
relations:
  method_for: [CA-R-1890]
---
# Summary

Partition and run the candidate Release E2E gate

## Scope

The fixed host-side E2E execution procedure and Full Gate aggregation for one sealed candidate.

## Claim

RELEASE_VERSION **must** derive one closed phase assignment from sealed package rows, run the closed Unit Gate before image construction, run the fixed Candidate E2E Gate after candidate canary against the exact inspected image digest, and aggregate both observed reports before promotion.

## Details

1. Sort all sealed `102_FRAMEWORK_ENGINE/**/test_*.py` package rows and require exactly one phase assignment per row. `candidate_e2e` is exactly the three named harness paths in CA-R-1890; every other declared row is `unit`. Reject an absent, duplicate, unknown, unsealed, altered, or out-of-set assignment.
2. Compile the candidate, run the unchanged closed Unit Gate for its assigned rows, and require a complete passing Unit report before candidate image build. Preserve the frozen selected N; no Unit result is E2E evidence.
3. Build and inspect the candidate image, run the fixed candidate canary, and require its exact immutable digest, candidate manifest digest, and sealed workspace binding before E2E execution.
4. Create a dedicated executor-owned scratch tree and read-only sealed candidate workspace. Invoke only the three fixed harness argv templates through the trusted host Docker CLI with exact source pins and the inspected candidate digest. Permit only the executor's closed environment allowlist: candidate manifest SHA-256, candidate image digest, phase-map SHA-256, sealed workspace root, dedicated scratch root, report root, and the Framework Instance's configured timeout/output-limit values; no caller supplies a command, path, image, or environment value. The executor provides no Docker socket mount, privileged daemon control, network/pull option, arbitrary environment, ambient image/tag, or host-path override.
5. Reuse the existing fixed mocks and harnesses. Apply the Framework Instance's configured finite inspect, per-harness, and cleanup timeouts and configured stdout, stderr, and JUnit byte caps. Retain only bounded observed bytes and their SHA-256 values. A timeout, overflow, missing terminal status, failed cleanup, unavailable Docker prerequisite, nonzero result, skip, missing case, or candidate/source mismatch is non-passing.
6. Emit one typed E2E receipt for each harness containing candidate manifest SHA-256, inspected candidate image digest, phase-map SHA-256, harness source path/SHA-256, exact argv, exit/timeout outcome, and bounded retained stdout, stderr, and JUnit bytes plus SHA-256 values. Aggregate Unit and E2E reports only by reopening these actual receipts and rejecting a missing, duplicate, tampered, ambiguous-completion, or cross-candidate receipt. Require their candidate manifest, candidate image digest where applicable, phase assignment digest, discovered case set, and Journal lineage to be exact, and every declared case exactly once across the two reports before returning a passing Full Gate. Journal each actual gate/canary result; do not promote or retire here.

This Method neither changes the closed Unit container nor permits an unbound host execution. It creates no selected Workflow or MCP route.
