---
atom_id: CA-D-562
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 21:16:31 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Runtime package carrier"
  depends_on: [Tool, Runtime, Manifest, Methodology, Installation]
relations:
  delivery_for: [CA-R-1877, CA-R-1879, CA-M-332]
---
# Summary

Bind the full Framework runtime-installation boundary

## Scope

The complete content-addressed Framework N/N+1 runtime package, distinct from the existing Engine Tools release.

## Claim

Release Version **must** stage and retain N/N+1 complete Framework packages at `.caprmedio_runtime/framework/releases/<candidateSnapshotManifest.sha256>/`, containing `manifest.toml`, `FRAMEWORK_ENGINE/`, `METHODOLOGY/`, and staged `SKILLS/ca/`; it may prepare that package before testing but installs retained N+1 only after the full suite, while N remains the active runtime selection until all later promotion gates pass. `.caprmedio_runtime/framework/current.toml` is atomically replaced only at promotion and contains the candidate manifest SHA-256, selected release root, `FRAMEWORK_ENGINE` root, and `METHODOLOGY` root. It **must not** represent the current Engine Tools installer as satisfying that full-package obligation merely because it installs `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS` below `.caprmedio_runtime/tools/releases/<release>/TOOLS` and selects `.caprmedio_runtime/tools/current.toml`.

## Details

The existing installer interfaces are `describe`, `status`, dry-run `run`, and explicit `run --apply`; their Tools-only paths remain a separate package. This Delivery defines the required full-Framework carrier contract for implementation and review; it does not claim that the new package or selector is already implemented or promoted.

For the normal Release Version selector, `candidate_image_digest` **must** name the verified immutable image, and `candidate_image_context_sha256` **must** contain the exact `ImageBuildEvidence.context_sha256` already verified for that image at selector publication. The selected package and image remain bound to the same candidate manifest SHA-256. Before using selected N to execute a candidate suite, admission **must** verify the frozen selected-N selector and inspect that exact image; its candidate and context labels **must** equal the selector bindings. A syntactically valid context digest or image label alone is not evidence of that binding. The first-runtime bootstrap selector retains its separately declared exact package-manifest and source-context proof; it does not weaken this normal-selector contract.
