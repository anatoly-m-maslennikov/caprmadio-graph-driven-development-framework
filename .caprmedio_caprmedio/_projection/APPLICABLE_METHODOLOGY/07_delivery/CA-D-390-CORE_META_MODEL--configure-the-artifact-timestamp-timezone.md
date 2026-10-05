---
subjects:
  governs: "Framework Instance Settings/Artifact Timestamp Timezone"
  depends_on:
    - "Framework Instance Settings"
    - "Artifact/Revision"
    - "Carrier"
version: 8
updated_at: "2026-10-02 19:36:21 +0400"
relations:
  child_of:
    - "CA-D-311"
    - "CA-R-1402"
atom_id: "CA-D-390"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-390-CORE_META_MODEL--configure-the-artifact-timestamp-timezone.md
  source_atom_id: CA-D-390
  source_atom_revision: 8
  source_sha256: 3042bb9e7056b85e8b0b248e83869f8145260da9813ca31101963e923bf4c67e
  original_relations_sha256: ad300b03e304b312918653de943d5511c34469376b727407e31a64564f30817e
---
# Summary

Configure the Artifact timestamp timezone

## Scope

the Artifact timestamp timezone setting in Framework Instance Settings.

## Claim

the Framework Instance Settings Artifact **may** set `[artifact_timestamps].timezone` **to** `local`, `UTC`, **or** an IANA timezone name, with `local` as the default; **every** emitted `updated_at` value uses `YYYY-MM-DD HH:MM:SS`, **and** the setting supplies its timezone interpretation.

## Details
