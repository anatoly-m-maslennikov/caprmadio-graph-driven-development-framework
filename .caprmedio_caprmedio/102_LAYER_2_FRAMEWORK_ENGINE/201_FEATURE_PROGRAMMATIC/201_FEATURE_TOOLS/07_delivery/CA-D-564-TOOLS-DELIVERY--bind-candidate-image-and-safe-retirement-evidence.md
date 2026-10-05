---
atom_id: CA-D-564
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-06 00:55:29 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Image carrier"
  depends_on: [Tool, Image, Container, Manifest, Journal, Runtime]
relations:
  delivery_for: [CA-R-1879, CA-R-1880, CA-M-333, CA-R-1890, CA-M-346]
---
# Summary

Bind candidate-image and safe-retirement evidence

## Scope

The actual Docker candidate-image proof between the closed Unit Gate and Candidate E2E Gate, and the deferred, exact old-image removal boundary.

## Claim

After the closed Unit Gate passes for a retained N+1 candidate, Release Version **must** bind the candidate build to `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile`, record `candidate_image_digest`, `prior_image_digest`, and exact retaining container/rollback references in the candidateSnapshotManifest result, retain immutable candidate and prior image identities with actual execution evidence, and permit removal only of the exact prior identity after verified N+1 promotion and proof of no retaining container or rollback reference.

## Details

The Dockerfile path does not establish a built, runnable, or accepted image. A passing Unit Gate is the image-build prerequisite, not promotion authority. The current Docker surface retains a mutable local tag, so implementation must produce and return the bound immutable digest fields rather than treating the tag as promotion or retirement proof. The exact inspected `candidate_image_digest` must bind the later fixed candidate canary and all three CA-R-1890 Candidate E2E harnesses; their passing receipts plus the passing Unit receipt are the sole Full Gate promotion prerequisite. This Delivery forbids tag-only equivalence, broad prune, deletion before Full Gate aggregation, and any claim that a build log or Unit-only result substitutes for actual candidate-image execution.
