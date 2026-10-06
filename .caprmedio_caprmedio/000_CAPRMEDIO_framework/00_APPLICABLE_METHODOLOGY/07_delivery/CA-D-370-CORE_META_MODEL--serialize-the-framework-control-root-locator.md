---
subjects:
  governs: "Framework Instance Settings/framework control-root locator"
  depends_on:
    - "Framework Instance Settings"
    - "Project"
    - "Directory Carrier"
version: 8
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-370"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-370-CORE_META_MODEL--serialize-the-framework-control-root-locator.md
  source_atom_id: CA-D-370
  source_atom_revision: 8
  source_sha256: 69e3f575cb2373de175ff1407ad953f7d7ee42e105551c6da58de9c66b2c9177
  original_relations_sha256: dbd41c990ca96026d80a7c6e36e3203724208ce3569ca634233af924bbbfab2f
---
# Summary

Serialize the framework control-root locator

## Scope

the framework control-root locator for a Project in the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must** encode the framework control-root locator for its Project, resolving **to** the Directory Carrier prescribed by CA-D-317 **without** selecting a different authority root.

## Details
