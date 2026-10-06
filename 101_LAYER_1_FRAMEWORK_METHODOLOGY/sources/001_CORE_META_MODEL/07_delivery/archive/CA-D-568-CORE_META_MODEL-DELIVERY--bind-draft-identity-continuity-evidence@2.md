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
version: 2
updated_at: "2026-10-05 07:37:07 +0400"
relations:
  relates_to:
    - CA-D-288
    - CA-D-378
    - CA-D-446
    - CA-D-507
    - CA-D-508
    - CA-D-569
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

an operation that identifies a Draft Atom **must** receive **`=1`** explicit identity basis through CA-D-569's optional `request.parameters.draft_identity_evidence` carrier **and** validate retained history before assigning an Atom ID:

- `prior_identified_revision` **must** carry the existing sealed `prior` **and** `prior_revision` descriptors for the target Draft's own direct retained predecessor lineage. the descriptors **must** prove the identified predecessor's `atom_id`, `version`, digest, **and** Summary, and that Summary **must** equal the target Draft's Summary. only then the later non-Draft Revision **must** use that same Atom Identity and **must not** allocate another number.
- `fresh_unassigned_draft` is admissible only when internal validation finds no identified Atom in the target Draft's direct retained predecessor lineage. only then, when the Draft becomes non-Draft, it **must** receive the next unreused Content Role number under CA-D-508.

the Draft Carrier itself **must not** carry the identity basis or an `atom_id`; its filename, path, Summary, temporary locator, arbitrary historical archive, **or** Journal record **must not** infer, establish, or replace that evidence. a changed Summary requires the separately admitted Replace/fresh-identity path. a verified prior Atom Identity **must not** be assigned to a different Atom.

## Details

this Delivery binds required operation input and history evidence before implementation. it preserves CA-D-446's same-Atom Draft transition and CA-D-288's ID-free Draft filename. Journal records may report the selected and verified basis but are not a second identity authority.
