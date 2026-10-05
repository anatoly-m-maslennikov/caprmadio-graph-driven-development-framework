---
subjects:
  governs: "Work Journal/Event/Carrier Serialization"
  depends_on:
    - "Work Journal/Event"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Carrier"
version: 8
updated_at: "2026-10-02 19:36:21 +0400"
relations: {}
atom_id: "CA-D-435"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-435-PROJECT_CONFIGURATION--serialize-atom-replacement-event-references.md
  source_atom_id: CA-D-435
  source_atom_revision: 8
  source_sha256: c325ec117ed4b879a3766aad78c79a6780781ce0718eaf49431f28479eb65263
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Atom replacement event references

## Scope

replacement references in schema-version `3` completed File Carrier events.

## Claim

a schema-version `3` completed File Carrier `MOVE` **or** `MOVE+UPDATE` event recording an Atom replacement **must** serialize its observed replacement references as paired top-level `predecessor_atom_id` **and** `successor_atom_ids` fields.

- `predecessor_atom_id` stores the observed identity as a string; `successor_atom_ids` stores the observed successor identities as an array of strings. preserve their values **and** array order exactly through safe encoding. array order does **not** establish priority **or** execution order.
- the pair is optional on ordinary events; absence does **not** establish whether a move was a replacement. a partial pair, a null field, **or** a value with the wrong storage type fails this encoding.
- both fields participate **in** the existing Event digest. the ordinary result **and** `previous_result_event` retain Carrier **and** Revision evidence **without** duplicating it **in** replacement fields.
- legacy **or** nonconforming IDs, an empty observed successor array, duplicate **or** self-referencing identities, a filename mismatch, **and** an invalid archive placement remain recordable payload. CA-E-462 evaluates the replacement independently; failed conformance **must not** become a Journal-admission gate under CA-R-1491.
- ordinary **and** historical records **without** these fields retain their selected schema. preserved observations **must not** be rewritten **to** satisfy current Atom grammar, archive rules, **or** successor conditions. successful storage proves **only** event **and** storage integrity, **not** a valid replacement.

## Details
