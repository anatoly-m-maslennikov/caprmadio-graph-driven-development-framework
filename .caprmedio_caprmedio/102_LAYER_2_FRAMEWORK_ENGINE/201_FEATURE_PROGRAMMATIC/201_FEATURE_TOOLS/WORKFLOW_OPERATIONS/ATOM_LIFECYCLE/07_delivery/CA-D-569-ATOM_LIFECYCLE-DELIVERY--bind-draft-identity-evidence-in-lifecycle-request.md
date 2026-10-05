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
version: 5
updated_at: "2026-10-05 08:55:00 +0400"
relations:
  relates_to: [CA-D-531, CA-D-532, CA-D-568]
---
# Summary

Bind Draft Identity Evidence in Lifecycle Request

## Scope

the optional identity-evidence carrier in the selected Atom Lifecycle dispatch request.

## Claim

CA-D-531's `request.parameters` **must not** carry `draft_identity_evidence` or any caller-selected Draft-history basis. The exclusive admitted lifecycle writer owns the tool-specific retained-history entry schema: it reserves a pre-addressable `history_entry_ref`, writes the Draft output, and appends the entry that binds the exact Draft `path` and `digest`, `origin`, direct `parent_history_entry_ref` when applicable, and any direct identified predecessor. This is the lifecycle trust boundary, not a universal metadata or filesystem contract.

the dispatcher **must** first read the actual target Draft Carrier's `revision_lineage.history_entry_ref`, enumerate only the trusted retained-history chain, and validate its unique current Draft-head predicate under CA-D-568 and CA-D-570. It may reserve only one private pending transition bound to that head, the planned identity/output locator/digest, and the sealed idempotent request; the reservation is not history, does not consume the head, refuses competing promotion or identity selection, and resumes only the same exact transition. An out-of-band Draft byte sequence with no matching current entry, a changed `never_identified`/demotion origin, an unrelated archive, a stale or missing parent, malformed entry, output mismatch, later child, branch, ambiguity, non-head, or Summary mismatch fails closed without an identity effect. Only after exact non-Draft output bytes are observed may it append the consuming `identified_promotion` successor. Failed output or finalization reports truthful incomplete/pending repairable context and never creates phantom history, consumes the old head, or allocates another identity on retry. A later Draft Update must create a new matching entry for its new output and direct parent, preserving the resolved original basis.

request data **must not** carry or select an `atom_id`, filename, path, Summary, arbitrary archive reference, history entry, Status model, transition rule, or identity policy. The dispatcher resolves the applicable Status and identity rules internally from sealed current authority; neither a caller nor a Journal can override the retained history.

## Details

This Delivery extends only the route-specific CA-D-531 lifecycle boundary; it does not alter CA-D-527's outer request, authorization, Run identity, receipt, retry, or Journal authority. CA-D-532 result seals may report the validated entry but do not become an independent identity registry, Events writer, or Journal writer. Fully authoritative Operator reauthoring of both a Draft and its retained history is outside the untrusted-request boundary. This is a source contract, not an implemented request-field acceptance claim.
