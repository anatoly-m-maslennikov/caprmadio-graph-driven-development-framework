---
atom_id: CA-M-331
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:21:05 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Candidate construction"
  depends_on: [Tool, Manifest, Digest, Artifact, Revision]
relations:
  method_for: [CA-R-1876, CA-R-1877]
---
# Summary

Construct one sealed Release Version candidate manifest

## Scope

Pure construction of the N/N+1 candidate inventory before release effects.

## Claim

The Tool constructs one canonical `candidateSnapshotManifest` by normalizing the sealed request into ordered repository-relative input/output rows, binding each row to its digest and destination, and deriving one candidate manifest SHA-256 without copying, installing, compiling, testing, or deleting anything.

## Details

Construction rejects duplicate destinations, traversal, missing required Framework Methodology or Engine rows, mismatched versions, and ambiguous current selections. The result is an input to later admitted effects, not a Workflow or an execution receipt.
