---
subjects:
  governs: "Atom/Revision/Status: Draft/Identity Continuity Evidence"
  depends_on:
    - "Atom/Identity"
    - "Atom/Identifier"
    - "Atom/Revision/Identifier"
    - "Atom/Revision/Status: Draft"
    - "Atom/Revision/Version"
    - "Atom/Revision/History"
    - "Tool/Workflow Operations/Atom Lifecycle/Request Parameters"
version: 3
updated_at: "2026-10-05 07:51:22 +0400"
relations:
  relates_to:
    - CA-D-288
    - CA-D-378
    - CA-D-446
    - CA-D-507
    - CA-D-508
    - CA-D-569
    - CA-D-570
atom_id: "CA-D-568"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Bind Draft Identity Continuity Evidence

## Scope

the required identity basis for a Draft Atom when a later Revision becomes non-Draft.

## Claim

an operation that identifies a Draft Atom **must** read and validate **`=1`** `revision_lineage` property from the actual target Draft Carrier under CA-D-570 before assigning an Atom ID. Optional CA-D-569 `request.parameters.draft_identity_evidence` may corroborate the exact carried property, but **must not** provide, select, alter, or override the identity basis.

- `kind: demoted_identified` is valid only when its `direct_predecessor` descriptor exactly resolves to the target Draft's own retained immutable direct predecessor history. It **must** match that predecessor's `atom_id`, `version`, `content_role`, `summary`, digest, and immutable locator; the target Draft's Summary **must** equal the predecessor Summary. Only then the later non-Draft Revision **must** use that same Atom Identity and **must not** allocate another number.
- `kind: never_identified` is valid only when produced by the admitted Create effect and validation confirms that the target Draft has no identified direct predecessor. Only then, when the Draft becomes non-Draft, it **must** receive the next unreused Content Role number under CA-D-508.

a Draft Carrier **must not** carry an `atom_id`; `revision_lineage` is direct predecessor provenance, not the Draft's own assigned identity. A filename, path, Summary, temporary locator, arbitrary historical archive, Journal record, or caller evidence **must not** infer, establish, or replace that provenance. A missing, unknown, malformed, stale, forged, non-direct, or Summary-mismatching lineage fails closed without an identity effect. A changed Summary requires the separately admitted Replace/fresh-identity path. A verified prior Atom Identity **must not** be assigned to a different Atom.

## Details

this Delivery binds carried Draft provenance and its validation before implementation. It preserves CA-D-446's same-Atom Draft transition and CA-D-288's ID-free Draft filename. Journal records and request evidence may report or corroborate the verified basis but are not a second identity authority.
