---
atom_id: CA-E-572
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 07:06:44 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Package and full-suite QA"
  depends_on: [Tool, Manifest, Methodology, Projection, Test Suite, Runtime]
relations:
  evaluation_for: [CA-R-1877, CA-R-1879, CA-M-332]
---
# Summary

Verify the complete Framework package and full-suite gate

## Scope

Candidate N+1 source delivery, compilation, complete package, and declared full-suite acceptance gate.

## Claim

The QA case **must** verify a successful complete derived source copy at its sealed root with `actual_derived_source_copy_sha256` equal to `expected_derived_source_copy_sha256` before compilation or package staging, accepted compilation from that sealed source frontier into the child-scoped materialization declared by CA-D-561, exact complete N+1 package contents, equality of the authoritative nested-source recursive digest before and after successful source delivery and compilation, and the declared full suite in its sealed environment before N+1 runtime or project-Skill exposure; package preparation may precede the suite, but a successful Engine-only suite or package is insufficient.

## Details

On the success path, assert that only `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/_release_materialized/<candidateSnapshotManifest.sha256>/` is created or replaced and that neither its ancestor nor nested `000_APPLICABLE_MTHD_sources` source subtree changes. Missing, partial, mismatched, stale, or uncertain source-copy evidence refuses compilation and package staging, retains N, and leaves source authority unchanged. On failed compilation, missing Methodology content, changed frontier, or any suite failure, assert the same nested-source digest preservation, retain N, and prevent installation or old-image retirement. No test result authorizes a source correction, recursive release, or C447 denied-relocation bypass.
