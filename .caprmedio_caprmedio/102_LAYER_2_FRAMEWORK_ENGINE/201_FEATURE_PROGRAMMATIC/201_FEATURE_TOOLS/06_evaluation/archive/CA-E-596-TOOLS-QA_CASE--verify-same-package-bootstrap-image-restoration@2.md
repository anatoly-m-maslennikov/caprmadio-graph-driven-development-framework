---
atom_id: CA-E-596
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 22:52:33 +0000"
subjects:
  governs: "Tool/FRAMEWORK_IMAGE_RESTORATION/Restoration acceptance"
  depends_on: [Tool, Operator, Framework Package, Runtime, Skill, Docker Image, Journal]
relations:
  evaluation_for: [CA-R-1897, CA-M-353, CA-D-591]
---
# Summary

Verify same-package bootstrap image restoration

## Scope

Acceptance of the closed CA-O-187 restoration and its CA-D-591 evidence, including actual Docker proof and interruption/refusal boundaries.

## Claim

The QA case **must** accept restoration only when actual immutable-image and canonical Journal evidence prove the unchanged retained package is selected with its verified replacement image and every unauthorized, stale or uncertain case preserves its truthful outcome.

## Details

Both success cases begin with an authentic retained bootstrap package/proof and a selected image absent from a functioning daemon. Each obtains an actual immutable image ID, exact package/source-context labels, fresh successful build/inspect/complete-package/MCP canary observations, and a canonical started/completed Action receipt with restoration result restored. The different-ID case retains a new canonical proof accepted by the unchanged retained-package reader and changes only image_digest in the exact bootstrap selector shape. The same-ID case reopens the original canonical proof, preserves its exact bytes/key and all selector bytes, and retains the fresh attempt separately; it is restored, not a prebuild no_op. A separate no_op case requires the exact image already available and a passing fresh retained-proof inspection before any build. Package manifest, package and public Skill bytes/modes, source context, Version, original proof and historical Journal prefix remain unchanged. The unchanged installed-N executor accepts the resulting exact binding in both restored cases; this is not evidence that a later Release Unit or Full Gate passed.

Filtering assertions place .DS_Store and other already excluded ephemeral metadata in the retained context and prove their omission from the disposable build input. Also inject .DS_Store after copying or into the built image: its presence does not fail validation under CA-R-1898. Preserve every original persistent byte/mode and require the persistent context digest and complete persistent canary package inventory to match. Symlinks, special files, secret-shaped paths, unexpected persistent files, missing rows and byte/mode changes are refused.

Failure cases cover missing authorization, wrong selector shape or package identity, mismatched public Skill, absent/tampered original proof or command outputs, source-context mismatch, daemon unavailability, ambiguous missing-image observation, wrong labels, unrelated image, failed canary, test-double proof, context/package drift during copy/build, and denied proof materialization. Before publication these retain the prior selector; a build or canary timeout remains uncertain without replay.

Concurrency checks prove restoration and normal promotion acquire the same new selector publication lock, a competing holder refuses publication, and optimistic exact selector/package/Skill revalidation rejects changed input. The existing empty-state initialization lock is not treated as that shared lock. Crash checks cover successful build without complete proof, complete proof before selection, selection replacement before result/terminal recording, and denied atomic publication. Each reports observed partial or uncertain state and retains recovery evidence without automatic rollback or another build.

Run checks reject duplicate active invocation and a changed frozen intent under the same requested Run ID, preserve completed/failed/unknown historical receipts, retain the started Run or original pending recording for uncertain outcomes without inventing a terminal result, and recover only an exact pending canonical event without replaying effects. A separately authorized fresh Run may retry a known canonical partial result only with the exact prior terminal reference, unchanged eight-field intent and no prior publication. Its separate result must leave the original result/event bytes intact; an absent authorization, changed intent, uncertain effect, unresolved started Run, pending recording or prior successful publication must not admit redispatch. Regression checks retain first-install empty-state refusal, normal promotion gates, selector/proof schemas and the exact three candidate E2E harness set. Mechanical and test-double cases are reported separately from required actual Docker acceptance.
