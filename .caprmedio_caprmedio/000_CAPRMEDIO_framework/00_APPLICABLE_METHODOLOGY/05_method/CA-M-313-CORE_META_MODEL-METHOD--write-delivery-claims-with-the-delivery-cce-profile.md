---
subjects:
  governs: "CCE/Role Profile: Delivery"
  depends_on:
    - "Atom/Content Role: Delivery"
    - "CCE Operator"
    - "Carrier"
    - "Entity/Carrier"
    - "Atom/Claim"
    - "Atom/Subjects"
    - "Relation Type"
version: 5
updated_at: "2026-09-28 22:47:05 +0000"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1342
atom_id: "CA-M-313"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-313-CORE_META_MODEL-METHOD--write-delivery-claims-with-the-delivery-cce-profile.md
  source_atom_id: CA-M-313
  source_atom_revision: 5
  source_sha256: 570884157745cc3016065c683188b6b80ad0376bba2f76948c279562edc0f947
  original_relations_sha256: df4e705715370cdf548abfbeba9ae0eed904bc3f2977ebc87988f011e0ad7418
---
# Summary

Write Delivery Claims with the Delivery CCE Profile

## Scope

authoring Delivery Claims with the Delivery CCE Role Profile.

## Claim

a Delivery Claim **must** use the Delivery CCE Role Profile **to** express its Carrier contribution with the following authoring conventions:

1. name the governed Carrier **or** Entity/Carrier binding **and** state its definition, classification, **or** constraint directly.
2. include format, content, address, placement, **or** lifecycle conditions **when** they are relevant **to** that contribution.
3. choose CCE Operators **to** express the applicable modality, conditions, quantities, **and** comparisons.
4. use **means** for a definition; express a classification **or** binding through its admitted Relation Type.
5. keep the Claim about the governed Subject; use references for separately governed contributions.

## Details

Carrier definitions **and** classifications need **only** the details relevant **to** their own contribution. they do **not** require an invented filename, format, **or** lifecycle condition.
