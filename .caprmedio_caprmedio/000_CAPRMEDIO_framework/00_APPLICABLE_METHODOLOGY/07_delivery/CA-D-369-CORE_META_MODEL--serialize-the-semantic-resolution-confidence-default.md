---
subjects:
  governs: "Framework Instance Settings/Confidence/Semantic Resolution Threshold/Carrier"
  depends_on:
    - "Framework Instance Settings"
    - "Confidence Threshold"
version: 8
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-369"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-369-CORE_META_MODEL--serialize-the-semantic-resolution-confidence-default.md
  source_atom_id: CA-D-369
  source_atom_revision: 8
  source_sha256: 400ff65877f571b7155d9035e39096c7aeee5690c5dee5f570a2d34d21308d82
  original_relations_sha256: dbd41c990ca96026d80a7c6e36e3203724208ce3569ca634233af924bbbfab2f
---
# Summary

Serialize the semantic-resolution confidence default

## Scope

an explicit semantic-resolution confidence default in the Framework Instance Settings TOML Carrier.

## Claim

an explicit semantic-resolution confidence default **in** the Framework Instance Settings TOML Carrier **must** use the integer-percentage field `confidence.semantic_resolution_threshold_percent`.

## Details
