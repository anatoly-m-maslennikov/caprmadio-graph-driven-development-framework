---
subjects:
  governs: "Structural Entity/Direct Containment"
  depends_on:
    - "Containment Relation Pair"
    - "Directory Carrier/Nesting"
version: 14
updated_at: "2026-10-02 18:57:51 +0400"
relations: {}
atom_id: "CA-D-264"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-264-CORE_META_MODEL-DELIVERY--derive-direct-containment-from-the-nearest-directory-carrier.md
  source_atom_id: CA-D-264
  source_atom_revision: 14
  source_sha256: 0f19e5fd28ed760867d261ad14aa29e0bed6b95d7482ad8a0bd196483f144f36
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Direct Containment from the Nearest Directory Carrier

## Scope

Artifact Revisions whose canonical Carriers are nested below Directory Carriers.

## Claim

an Artifact Revision whose canonical Carrier is nested below a Directory Carrier **must** derive **`=1`** direct `CONTAINS` **and** `IS_CONTAINED_BY` relation pair with the Structural Entity Revision carried by its nearest ancestor Directory Carrier.

## Details
