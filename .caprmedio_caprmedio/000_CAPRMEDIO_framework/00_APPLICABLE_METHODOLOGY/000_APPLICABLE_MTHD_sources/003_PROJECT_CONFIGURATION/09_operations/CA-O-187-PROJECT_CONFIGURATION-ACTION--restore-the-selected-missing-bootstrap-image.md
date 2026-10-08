---
atom_id: CA-O-187
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 22:31:14 +0000"
subjects:
  governs: "Restore the selected missing bootstrap image"
  depends_on: [Action, Operator, Framework Package, Runtime, Skill, Docker Image, Journal]
relations:
  relates_to: [CA-O-164, CA-O-180, CA-R-1897, CA-M-353, CA-E-596, CA-D-591]
---
# Summary

Restore the selected missing bootstrap image

## Action

Restore the selected missing bootstrap image **means** the explicit Operator-invoked Action that rebuilds and verifies the image for one unchanged retained bootstrap package, then publishes only its new immutable image binding under CA-R-1897.

## Scope

The Action binds one frozen bootstrap selector/package/source-context/original-proof/public-Skill intent, one actual build and canary, one guarded image-binding restoration, and one canonical Action Run. It is outside CA-O-180's empty-state first installation and CA-O-164's selected N-to-N+1 Release Version Workflow.

## Details

Invoke the admitted FRAMEWORK_IMAGE_RESTORATION boundary once under explicit registered Operator authorization. Authenticate the retained package and original bootstrap proof, freeze the CA-D-591 intent, establish the selected image's absence from a functioning daemon, and append and reopen canonical started evidence before building. Construct only a filtered disposable copy of the authenticated persistent context, preserve its original bytes/modes, and observe the actual immutable build ID, exact labels and fixed complete-package/MCP canary, ignoring Finder metadata under CA-R-1898. Retain fresh actual attempt observations; a different image digest receives a new canonical proof, while reproduction of the original digest reopens and preserves the original canonical proof/key unchanged.

Under the new fixed selector publication lock shared with normal promotion, reopen all frozen inputs. For a different image digest, atomically replace only image_digest in the same closed bootstrap selector; for the original digest, retain all exact selector bytes. Reopen that selection, applicable canonical proof and fresh attempt and record restored/completed evidence through the canonical Work Journal for either successful build branch. no_op is limited to the exact image already available and freshly verified before building. The package, Version, source context and public Skill remain unchanged. A changed intent under the same requested Run ID, repeated started/terminal invocation or pending recording permits only inspection or explicit exact-recording recovery, never another build or publication for that Run. A separately authorized fresh Run may reference an exact canonically recorded partial terminal only when its sealed result proves unchanged inputs and no selector publication. Authenticate the prior terminal/result and retain the new Run in its own CA-D-591 attempt carrier; preserve the original partial event/result unchanged. Uncertain, unfinished, recording-pending and successfully published effects remain outside retry admission.

Missing authority, changed input, failed proof or uncertain effects stop with their actual evidence. The Action adds no selected route, caller-selected build input, package/source rewrite, image tag/removal, automatic rollback or retry, or release-gate exemption. Later fresh Release Runs retain every Unit, package, image/canary, candidate E2E, Full Gate, promotion and conditional prior-image disposition obligation; historical outcomes are preserved.
