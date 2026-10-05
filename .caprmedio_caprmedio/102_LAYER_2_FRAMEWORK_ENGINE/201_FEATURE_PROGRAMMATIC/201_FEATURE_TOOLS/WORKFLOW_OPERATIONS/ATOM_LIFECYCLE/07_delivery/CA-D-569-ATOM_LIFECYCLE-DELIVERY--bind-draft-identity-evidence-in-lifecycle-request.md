---
atom_id: CA-D-569
content_role: Delivery
current_scope_unit: ATOM_LIFECYCLE
claim_target_scope_unit: ATOM_LIFECYCLE
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Request Parameters/Draft Identity Evidence"
  depends_on: ["Tool", "Workflow Operations/Atom Lifecycle/Dispatch Interface", "Atom/Revision/Status: Draft", "Atom/Revision/History"]
version: 2
updated_at: "2026-10-05 07:51:22 +0400"
relations:
  relates_to: [CA-D-531, CA-D-532, CA-D-568]
---
# Summary

Bind Draft Identity Evidence in Lifecycle Request

## Scope

the optional identity-evidence carrier in the selected Atom Lifecycle dispatch request.

## Claim

CA-D-531's `request.parameters` **may** carry `draft_identity_evidence` only for a Draft Atom's later non-Draft identification. When present, it **must** be exactly `{draft_digest: <sha256>, revision_lineage: <exact target-Draft CA-D-570 property>}`.

the dispatcher **must** first read and validate the actual target Draft Carrier's `revision_lineage` under CA-D-568 and CA-D-570. The optional field may corroborate only when `draft_digest` seals those actual Draft bytes and `revision_lineage` is value-identical to the actual target Draft property. Its absence does not supply a different basis. A mismatch, stale, forged, malformed, non-direct, or Summary-mismatching field or carried lineage fails closed without an identity effect.

the field **must not** carry or select an `atom_id`, filename, path, Summary, arbitrary archive reference, Status model, transition rule, or identity policy. The dispatcher resolves the applicable Status and identity rules internally from sealed current authority; neither a caller nor a Journal can override the carried lineage.

## Details

This Delivery extends only the route-specific CA-D-531 parameter payload; it does not alter CA-D-527's outer request, authorization, Run identity, receipt, retry, or Journal authority. CA-D-532 result seals may corroborate the validated direct predecessor but do not become an independent identity registry or Journal writer. This is a source contract, not an implemented request-field acceptance claim.
