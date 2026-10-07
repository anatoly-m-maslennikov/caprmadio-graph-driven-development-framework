---
atom_id: CA-R-1897
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-07 22:25:26 +0000"
subjects:
  governs: "Tool/FRAMEWORK_IMAGE_RESTORATION/Same-package image restoration"
  depends_on: [Tool, Operator, Framework Package, Runtime, Skill, Docker Image, Journal]
relations:
  relates_to: [CA-R-1880, CA-R-1881, CA-D-562, CA-D-575]
---
# Summary

Restore the selected missing bootstrap image without changing its package

## Scope

One explicitly Operator-authorized restoration of the missing immutable image selected by an exact first-runtime bootstrap selector, using its authenticated retained package and image-build proof.

## Claim

FRAMEWORK_IMAGE_RESTORATION **must** restore an independently verified immutable image binding for the same retained selected Framework package while preserving that package's identity, Version, source context, public Skill and historical evidence.

## Details

Admission requires explicit registered Operator authorization, the exact closed bootstrap selector defined by CA-D-575, its complete manifest-addressed package and matching public Skill, authentic retained Docker build/inspect/canary proof, and established absence of the selected image from a functioning Docker daemon. A daemon failure, unrelated image, tag, label-only assertion, normal N+1 selector, incomplete package or changed proof does not establish this case.

The Action freezes the exact prior selector bytes and SHA-256, package manifest and persistent inventory, sealed source-context SHA-256, original immutable image digest, original proof receipt and context digests, and complete public Skill inventory. It builds only from a disposable mode-preserving copy of the retained admitted context; ephemeral metadata is excluded only in that copy. Originals remain unchanged. Current authoring sources, current compiled Methodology, unrelated Docker images and caller-selected build inputs do not replace retained inputs.

Publication requires fresh actual build/inspect/canary evidence and exact package/source-context labels. If the build reproduces the original immutable image digest, the Action reopens and preserves the original canonical proof and retains the fresh attempt observations separately; it does not rewrite the already verified selector. If the build yields a different digest, the Action retains a new canonical bootstrap proof for that actual image. Under one new Project-wide selector publication lock shared with normal promotion, it rechecks all frozen inputs immediately before atomically replacing only the bootstrap selector's image_digest value in that different-digest case. Both successful build cases record restored/completed evidence. no_op is limited to the exact image already being available with a passing fresh retained-proof inspection before any build. Every other selector value, package and Skill byte and mode remains unchanged.

The canonical Work Journal records actual started evidence, observed new image/proof/selector digests and any supported terminal Action evidence. Build timeout, interrupted execution, uncertain publication or unavailable terminal recording retains its actual partial, uncertain or recording-pending evidence and the started Run or original pending recording without inventing a terminal outcome or replaying an effect. Restoration neither establishes N+1 promotion nor waives Unit, package, image/canary, three candidate E2E harnesses, Full Gate, promotion or conditional prior-image disposition. Historical failed and unknown Runs retain their outcomes.
