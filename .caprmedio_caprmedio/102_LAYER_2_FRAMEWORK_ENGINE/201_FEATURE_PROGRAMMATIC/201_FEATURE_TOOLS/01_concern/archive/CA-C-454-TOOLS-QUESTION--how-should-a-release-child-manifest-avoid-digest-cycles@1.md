---
atom_id: CA-C-454
content_role: Concern
type: Question
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 07:52:02 +0400"
subjects:
  governs: "Release child manifest digest-cycle avoidance"
  depends_on: [Tool, Manifest, Digest, Projection]
relations:
  concern_about: [CA-D-561, CA-D-566, CA-D-567, CA-D-571, CA-E-572]
---
# Summary

How should a Release child manifest avoid digest cycles

## Scope

The deterministic derived manifest placed with compiler-projected output in a sealed Release Version child root.

## Claim

The resolved choice is CA-D-571's `_release_manifest.json`: it inventories every emitted projected output except itself and records only observed compiler, source, frontier, derived-copy, and nested-source facts, so its canonical bytes are deterministically reproducible without a self- or cross-hash dependency.

## Details

A manifest `sha256` member, a row for `_release_manifest.json`, or an `actual_compiled_output_sha256`/final compiled-tree digest would each require digesting bytes that include that same manifest. Recording `candidateSnapshotManifest.sha256` also forms a cross-hash cycle because D566's candidate identity includes `expected_compiled_output_sha256`, while that expected value is the digest of the complete child tree containing this manifest. Those alternatives are rejected.

The selected representation keeps the candidate release as a non-digest identity, preserves D561's child-only materialization boundary, and leaves D566's pre-effect expectation and D567's post-effect tree digest outside the child manifest. This resolves only the deterministic representation question; it neither claims compiler execution nor changes source authority, canonical projection behavior, package admission, or runtime state.
