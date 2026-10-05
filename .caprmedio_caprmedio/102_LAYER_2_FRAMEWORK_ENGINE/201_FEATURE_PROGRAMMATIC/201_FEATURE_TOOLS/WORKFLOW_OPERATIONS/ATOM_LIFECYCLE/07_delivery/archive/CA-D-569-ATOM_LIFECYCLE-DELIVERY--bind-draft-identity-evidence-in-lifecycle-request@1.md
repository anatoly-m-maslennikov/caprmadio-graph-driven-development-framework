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
version: 1
updated_at: "2026-10-05 07:37:07 +0400"
relations:
  relates_to: [CA-D-531, CA-D-532, CA-D-568]
---
# Summary

Bind Draft Identity Evidence in Lifecycle Request

## Scope

the optional identity-evidence carrier in the selected Atom Lifecycle dispatch request.

## Claim

CA-D-531's `request.parameters` **may** carry `draft_identity_evidence` only for a Draft Atom's later non-Draft identification. when present, it **must** be exactly one of:

- `{kind: "prior_identified_revision", prior: <sealed descriptor>, prior_revision: <sealed descriptor>}`; both descriptors are the existing lifecycle `prior` and `prior_revision` seals for the target Draft's direct retained predecessor lineage.
- `{kind: "fresh_unassigned_draft"}`; the dispatcher verifies internally that the target Draft's direct retained predecessor lineage contains no identified Atom.

the field is evidence only: it **must not** carry an `atom_id`, a filename, path, Summary, arbitrary archive reference, Status model, transition rule, or caller-selected identity policy. the dispatcher resolves the applicable Status and identity rules internally from the sealed current authority and validates the field under CA-D-568. A missing, stale, forged, non-direct, or Summary-mismatching evidence carrier fails closed or returns the separately admitted Replace handoff without an identity effect.

## Details

This Delivery extends only the route-specific CA-D-531 parameter payload; it does not alter CA-D-527's outer request, authorization, Run identity, receipt, retry, or Journal authority. CA-D-532 returns the same verified `prior` and `prior_revision` seals in history/lineage; it does not create an independent identity registry or Journal writer. This is a source contract, not an implemented request-field acceptance claim.
