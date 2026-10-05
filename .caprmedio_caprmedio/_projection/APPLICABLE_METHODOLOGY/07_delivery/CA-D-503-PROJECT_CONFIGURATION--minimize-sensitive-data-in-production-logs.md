---
atom_id: "CA-D-503"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Carrier"
  depends_on: []
version: 1
updated_at: "2026-09-28 15:12:22 +0400"
relations: {}
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-503-PROJECT_CONFIGURATION--minimize-sensitive-data-in-production-logs.md
  source_atom_id: CA-D-503
  source_atom_revision: 1
  source_sha256: 3903147bf1bebdecf68931f0eba3bd40d9ec36ed161293dae95ffd07ffecec29
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Minimize sensitive data in production logs

## Scope

production logs that can contain personal, customer, **or** commercially sensitive data.

## Claim

personal, customer, **and** commercially sensitive data in production logs **must** be omitted, masked, hashed, tokenized, **or** **otherwise** minimized according to the applicable boundary.

## Details

the applicable boundary selects the permitted minimization treatment for sensitive log data.
