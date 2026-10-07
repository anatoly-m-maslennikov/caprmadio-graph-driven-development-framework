---
atom_id: CA-E-586
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-06 14:06:45 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite runner QA"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, Source Carrier, Compiled Candidate, JUnit Report, Writable Output]
relations:
  evaluation_for: [CA-R-1886, CA-M-343, CA-D-579]
---
# Summary

Verify complete and source-bound Release suite evidence

## Scope

The Release Version closed Unit driver, its phase-derived declared-case discovery, and its sealed JUnit evidence boundary.

## Claim

The QA case **must** prove that the closed Unit Gate passes only after every phase-assigned `unit` in-tree Framework test case executes once with valid immutable-envelope source-read evidence for all required groups and a compiled-candidate carrier, and rejects incomplete, fabricated, or non-passing evidence. It must also prove that this Unit result alone cannot be credited as the Full Gate.

## Details

Exercise an isolated fixture suite with valid bindings for Methodology, Tools, Apps, MCP, Agentic, Skill, and a compiled-candidate carrier. Verify that every sealed `102_FRAMEWORK_ENGINE/**/test_*.py` module receives exactly one sealed phase assignment: the three paths named by CA-R-1890 are `candidate_e2e` and every other path is `unit`. Verify every `unit` module is discovered in a fresh process, one Unit JUnit row per discovered case, the exact Unit test-ID set, one immutable-envelope SHA-256 property per case, and exact byte-and-digest source-probe records resolving to sealed package rows. Independently verify that a focused subset, omitted or duplicated phase assignment, duplicate test ID, a candidate-E2E module represented as a Unit skip, absent or altered envelope, unmapped or unreadable source, altered digest, absent compiled-candidate evidence, failure, error, skip, invalid report location, read-only-workspace write, or unresolved test-ID/import collision cannot produce a passing Unit Gate. Verify the fixed closed Unit CLI and schema-2 control-context digest remain unchanged, and that a passing Unit report authorizes candidate-image construction only; its result cannot authorize promotion without the actual source-pinned, candidate-image-bound E2E evidence and Full Gate aggregation verified by CA-E-589. Equal module basenames are permitted when fresh child processes discover and execute both Unit modules with distinct test IDs and correct source bindings; name equality alone is not an import collision. The test harness may retain its disposable output fixture after execution; that retention is not source or runtime mutation.
Exercise an isolated fixture suite with valid bindings for Methodology, Tools, Apps, MCP, Agentic, Skill, and a compiled-candidate carrier. Verify that every sealed `102_FRAMEWORK_ENGINE/**/test_*.py` module receives exactly one sealed phase assignment: the three paths named by CA-R-1890 are `candidate_e2e` and every other path is `unit`. Verify every `unit` module is discovered in a fresh process, one Unit JUnit row per discovered case, the exact Unit test-ID set, one immutable-envelope SHA-256 property per case, and exact byte-and-digest source-probe records resolving to sealed package rows. Independently verify that a focused subset, omitted or duplicated phase assignment, duplicate test ID, a candidate-E2E module represented as a Unit skip, absent or altered envelope, unmapped or unreadable source, altered digest, absent compiled-candidate evidence, failure, error, skip, invalid report location, read-only-workspace write, or unresolved test-ID/import collision cannot produce a passing Unit Gate. Verify the fixed closed Unit CLI and schema-2 control-context digest remain unchanged, and that a passing Unit report authorizes candidate-image construction only; its result cannot authorize promotion without the actual source-pinned, candidate-image-bound E2E evidence and Full Gate aggregation verified by CA-E-589. Equal module basenames are permitted when fresh child processes discover and execute both Unit modules with distinct test IDs and correct source bindings; name equality alone is not an import collision. The test harness may retain its disposable output fixture after execution; that retention is not source or runtime mutation.

Also verify the finite source-owned Unit budget: the canonical `[release_suite].unit_timeout_seconds = 3600` default, an explicit Framework Instance override in `(0, 7200]`, default fallback when the instance key is absent, and rejection of boolean, non-finite, non-positive, over-maximum, malformed, missing, stale, or mode-changed values. Verify the private `unit-deadline.json` snapshot contains the declared source/context fingerprints plus configured/effective finite values, remains bound by `control_context_digest`, and introduces no public receipt, schema-2, CLI, environment, manifest, or MCP field. A private fixture timeout may only shorten the configured budget; timeout or invalid budget evidence is non-passing and retains N.
