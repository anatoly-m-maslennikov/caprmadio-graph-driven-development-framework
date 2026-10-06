---
subjects:
  governs: "Atom/Carrier/Current Scope Unit/Filename Token"
  depends_on:
    - "Atom/Scope"
    - "Scope Unit"
version: 15
updated_at: "2026-10-01 21:24:59 +0400"
relations: {}
atom_id: "CA-D-291"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-291-CORE_META_MODEL-DELIVERY--serialize-the-current-scope-unit-in-atom-filenames.md
  source_atom_id: CA-D-291
  source_atom_revision: 15
  source_sha256: 9a2855535ac2f6c7a35661ad558d97694f53feaadaba91ba890a20a7be04b9bd
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize the Current Scope Unit in Atom Filenames

## Scope

Project-owned Atom filenames for Carriers contained **in** Scope Units.

## Claim

**every** Project-owned Atom filename **must** serialize the Scope Unit that **contains** its authoritative Carrier **`=1`** time **and** **must** omit that segment **if** the Carrier is **in** the Project Scope Unit.

## Details
