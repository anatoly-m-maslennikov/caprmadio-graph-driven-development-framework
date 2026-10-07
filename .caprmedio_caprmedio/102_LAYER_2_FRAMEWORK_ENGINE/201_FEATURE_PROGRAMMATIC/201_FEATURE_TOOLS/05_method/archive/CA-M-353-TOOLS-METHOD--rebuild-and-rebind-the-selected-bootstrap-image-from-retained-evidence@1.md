---
atom_id: CA-M-353
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-07 22:31:14 +0000"
subjects:
  governs: "Tool/FRAMEWORK_IMAGE_RESTORATION/Retained-context construction"
  depends_on: [Tool, Operator, Framework Package, Runtime, Skill, Docker Image, Journal]
relations:
  method_for: [CA-R-1897]
---
# Summary

Rebuild and rebind the selected bootstrap image from retained evidence

## Scope

The bounded construction and publication of one same-package bootstrap image restoration under CA-R-1897 and CA-O-187.

## Claim

FRAMEWORK_IMAGE_RESTORATION **must** construct its restoration image from the authenticated retained context, verify the actual immutable image and complete package, and retain or publish the sole image binding only after frozen-input revalidation and canonical started-Run proof.

## Details

1. Read the exact bootstrap selector and retained package. Authenticate the original canonical bootstrap proof through the retained-package reader without requiring the old image to remain available. Verify the complete public Skill against the retained package. Freeze the CA-D-591 intent and retain exact prior selector bytes; validate all input paths, bytes and modes. Planning performs no build or publication.
2. Independently observe a functioning Docker daemon and the selected immutable image's absence. Refuse an unavailable daemon or ambiguous inspection failure. If the same authenticated selected image is already available, report that observation without rebuilding or changing the selection.
3. Admit the new closed direct Action and append and reopen its canonical started evidence before any Docker build. A requested Run ID binds exactly one frozen intent and authority pin. A repeated started, terminal or recording-pending invocation is inspected or explicitly recovered, never redispatched.
4. Materialize a fresh disposable context from the original proof's admitted persistent files, preserving observed modes and excluding the existing Release inventory's ephemeral files only in the copy. Reject secret-shaped paths, symlinks and special files before copying. Re-digest every copied file and require the filtered context's persistent tree digest to equal the authenticated original context digest. Revalidate original context and package before and after materialization.
5. Execute only the existing fixed bootstrap build vector with the retained Dockerfile, dependencies, package and canary inputs, the exact package-manifest and source-context labels, and an internally derived iidfile. Capture the actual immutable image ID; independently inspect it and run the existing fixed complete-package/MCP canary against that exact ID. Retain actual command vectors, status, timing and immutable output bytes. A test double is never production proof.
6. Retain fresh actual build/inspect/canary attempt observations in the private restoration evidence. If the observed immutable image digest equals the original digest, reopen and preserve the existing canonical proof at the unchanged CA-D-575 key; do not overwrite it with the new attempt. Otherwise retain a new canonical bootstrap proof at the CA-D-575 location derived from the unchanged package-manifest SHA-256 and actual different image digest. Reopen the applicable canonical proof with the unchanged retained-package reader and freshly inspect the exact observed image. Preserve the original proof and all uncertain or failed attempts.
7. Acquire the new fixed Project-wide selector publication lock also acquired by normal promotion. Reopen the exact frozen selector, package, public Skill, applicable canonical proof and fresh attempt; refuse any drift. For a different image digest, stage a selector of the same closed bootstrap shape with only image_digest changed, then atomically replace the selection. For the original digest, keep the exact selector bytes unchanged. Reopen the resulting exact selection and verified image binding in either case. The distinct first-install lock alone does not provide this mutual exclusion.
8. Retain the actual CA-D-591 result and record its image/proof/selector effects through the sole canonical Work Journal. Both successful build branches return restored and record canonical completed evidence; only an exact image already available and freshly verified before building qualifies for no_op. Completion requires the reopened selection, applicable authentic canonical proof, fresh attempt and canonical terminal receipt to agree. An effect or recording failure reports its actual state; it triggers no implicit rebuild, rollback, deletion, promotion or retry.

The Method does not recompile Methodology, reconstruct a package from current sources, overwrite a retained package or Skill, add selector/proof schema fields, create a selected route, or substitute a later Release Run's acceptance for restoration evidence.
