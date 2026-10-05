---
atom_id: CA-D-561
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:38:28 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Source and compilation carriers"
  depends_on: [Tool, Methodology, Projection, Manifest, Project Structure, Framework Settings]
relations:
  delivery_for: [CA-R-1877, CA-R-1878, CA-M-331, CA-M-332]
---
# Summary

Bind Release Version source, compilation, and package carriers

## Scope

The canonical source and derived compilation carriers consumed by a future release Tool.

## Claim

Release Version **must** bind compiler input to the explicitly pinned canonical source snapshot named by `candidateSnapshotManifest` through `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py`; the complete copy at `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources` is a derived delivery, never replacement authority. Candidate compiled output is materialized only below `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/_release_materialized/<candidateSnapshotManifest.sha256>/`, with its manifest at that child root; it must never replace, delete, or otherwise mutate the enclosing `00_APPLICABLE_METHODOLOGY` directory or nested authoritative `000_APPLICABLE_MTHD_sources` subtree. The canonical persisted `.caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY` remains source-bound.

## Details

The candidateSnapshotManifest records canonical source-snapshot references/digests, derived-copy digest, compiler frontier digest, child materialization digest, and `nested_source_recursive_sha256_before` and `nested_source_recursive_sha256_after`. Each nested-source digest is the SHA-256 of the ordered relative-path and byte sequence recursively rooted at `000_APPLICABLE_MTHD_sources`; successful source delivery and compilation require those exact before/after digests to match. The current compiler preserves source/output separation and emits the configured control-root `_projection/APPLICABLE_METHODOLOGY`; it is not a complete Framework-package installer. This Delivery binds the child materialization without authorizing a Project Structure rewrite, replacement of canonical authority with the root copy, overwrite of the authoring tree, or a C447 denied-relocation bypass.
