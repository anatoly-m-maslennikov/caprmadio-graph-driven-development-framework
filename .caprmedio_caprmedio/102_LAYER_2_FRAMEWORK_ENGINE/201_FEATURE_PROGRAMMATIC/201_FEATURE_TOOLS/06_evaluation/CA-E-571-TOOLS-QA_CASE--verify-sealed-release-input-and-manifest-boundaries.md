---
atom_id: CA-E-571
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:21:05 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Sealed-input QA"
  depends_on: [Tool, Manifest, Digest, Revision, Project Structure, Framework Settings]
relations:
  evaluation_for: [CA-R-1876, CA-R-1877, CA-M-331]
---
# Summary

Verify sealed Release Version input and manifest boundaries

## Scope

Candidate-manifest construction and rejection before any effect.

## Claim

The QA case **must** prove that one complete sealed N/N+1 request produces a deterministic manifest and that changed source, settings, frontier, destination, digest, duplicate row, traversal, or caller-supplied substitute is rejected without source, runtime, Skill, image, or Journal mutation.

## Details

Assert that the manifest includes Framework Methodology and required Engine entries rather than accepting an Engine-Tools-only candidate. This is construction proof, not release success evidence.
