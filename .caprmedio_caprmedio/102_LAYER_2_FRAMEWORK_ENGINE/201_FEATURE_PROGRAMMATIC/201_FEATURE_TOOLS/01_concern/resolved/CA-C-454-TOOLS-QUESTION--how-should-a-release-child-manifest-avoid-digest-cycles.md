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
version: 2
updated_at: "2026-10-05 07:59:34 +0400"
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

The resolved choice is CA-D-571's pure preflight: it uses existing compiler selection and projection rendering in memory to predict the child payload, output rows, and complete child-tree digest before D566 sealing, then requires a later admitted renderer to reproduce those bytes exactly. This avoids a self- or cross-hash dependency without introducing a second compiler.

## Details

A manifest `sha256` member, a row for `_release_manifest.json`, or an `actual_compiled_output_sha256`/final compiled-tree digest would each require digesting bytes that include that same manifest. Recording `candidateSnapshotManifest.sha256` also forms a cross-hash cycle because D566's candidate identity includes `expected_compiled_output_sha256`, while that expected value is the digest of the complete child tree containing this manifest. Deferring expected output derivation until post-effect observation makes D566's pre-effect expectation temporally impossible. Those alternatives are rejected.

The preflight uses one fixed safe child-name placeholder to establish that substituting the actual candidate-manifest component does not alter existing `projection_bytes` output; only then can it seal the prediction. The selected representation keeps the candidate release as a non-digest identity, preserves D561's child-only materialization boundary, and leaves D566's pre-effect expectation and D567's post-effect tree digest outside the child manifest. This resolves only the deterministic representation question; it neither claims compiler execution nor changes source authority, canonical projection behavior, package admission, or runtime state.
