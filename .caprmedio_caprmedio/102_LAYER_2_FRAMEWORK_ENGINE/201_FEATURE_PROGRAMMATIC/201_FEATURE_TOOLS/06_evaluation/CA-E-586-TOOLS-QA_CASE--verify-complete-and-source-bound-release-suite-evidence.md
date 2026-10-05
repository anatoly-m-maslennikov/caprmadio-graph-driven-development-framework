---
atom_id: CA-E-586
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 18:37:31 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite runner QA"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, Source Carrier, Compiled Candidate, JUnit Report, Writable Output]
relations:
  evaluation_for: [CA-R-1886, CA-M-343, CA-D-579]
---
# Summary

Verify complete and source-bound Release suite evidence

## Scope

The Release Version full-suite driver, its declared-case discovery, and its sealed JUnit evidence boundary.

## Claim

The QA case **must** prove that the full-suite driver passes only after every discovered in-tree Framework test case executes once with valid immutable-envelope source-read evidence for all required groups and a compiled-candidate carrier, and rejects incomplete, fabricated, or non-passing evidence.

## Details

Exercise an isolated fixture suite with valid bindings for Methodology, Tools, Apps, MCP, Agentic, Skill, and a compiled-candidate carrier. Verify every sealed `102_FRAMEWORK_ENGINE/**/test_*.py` module is discovered in a fresh process, one JUnit row per discovered case, the exact complete test-ID set, one immutable-envelope SHA-256 property per case, and exact byte-and-digest source-probe records resolving to sealed package rows. Independently verify that a focused subset, omitted module, duplicate test ID, absent or altered envelope, unmapped or unreadable source, altered digest, absent compiled-candidate evidence, failure, error, skip, invalid report location, read-only-workspace write, or unresolved test-ID/import collision cannot produce a passing gate. Equal module basenames are permitted when fresh child processes discover and execute both modules with distinct test IDs and correct source bindings; name equality alone is not an import collision. The test harness may retain its disposable output fixture after execution; that retention is not source or runtime mutation.
