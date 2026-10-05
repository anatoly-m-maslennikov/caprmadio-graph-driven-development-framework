---
subjects:
  governs: "Artifact/Carrier Placement"
  depends_on:
    - "Artifact/Activity"
    - "Artifact/Revision/Status"
    - "Atom/Content Role: Delivery"
version: 4
updated_at: "2026-10-02 19:44:54 +0400"
relations: {"relates_to": ["CA-D-461"]}
atom_id: "CA-D-466"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-466-CORE_META_MODEL-STANDARD--place-carriers-by-applicable-status-delivery.md
  source_atom_id: CA-D-466
  source_atom_revision: 4
  source_sha256: d3336f3ff4e75dbe2d02729c0442bdc59e102cbf12f73a0e5fd29539eaad6263
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Place Carriers by Applicable Status Delivery

## Scope

Carrier placement where Artifact Activity applies or does not apply.

## Claim

**when** Activity applies **and** an Artifact has **`=1`** valid current Revision Status, its Carrier placement **must** follow the most specific applicable Delivery rule for that Artifact Type; **only when** no more specific mapping exists, Active uses the canonical current directory **and** another Status uses its lowercase Status subdirectory. **when** Activity does **not** apply, Carrier placement **must not** derive a Status directory from absent Activity.

## Details
