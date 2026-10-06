---
subjects:
  governs: "Projection/Carrier/Updated At"
  depends_on: []
version: 11
updated_at: "2026-10-02 19:05:39 +0400"
relations: {}
atom_id: "CA-D-310"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-310-CORE_META_MODEL--serialize-projection-updated-at.md
  source_atom_id: CA-D-310
  source_atom_revision: 11
  source_sha256: 40a88c75afa5bcdad37a417c7dbc12a392b5afc7b38d6f44c35acf23bd884d70
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Projection Updated At

## Scope

Projection Carrier latest completed rebuild times.

## Claim

**every** Projection Carrier **must** serialize the time of its latest completed rebuild as `updated_at` **in** Project time **without** treating that value alone as proof of currentness.

## Details
