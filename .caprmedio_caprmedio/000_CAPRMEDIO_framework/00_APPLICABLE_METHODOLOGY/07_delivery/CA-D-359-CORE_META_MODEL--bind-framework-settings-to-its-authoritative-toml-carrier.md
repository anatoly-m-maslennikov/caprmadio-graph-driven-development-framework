---
subjects:
  governs: "Framework Instance Settings/Authoritative Carrier"
  depends_on:
    - "File Carrier"
    - "File Carrier/Format"
version: 10
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - CA-D-358
atom_id: "CA-D-359"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-359-CORE_META_MODEL--bind-framework-settings-to-its-authoritative-toml-carrier.md
  source_atom_id: CA-D-359
  source_atom_revision: 10
  source_sha256: bec9916eb5f080ea22b9a19dd1124d8f66a1dde0ff2fa289ebd08e427becfd6f
  original_relations_sha256: 48bb8e84d64eff4539728a3dc750fab3055957a8021a42380f1a6137ce28526a
---
# Summary

Bind Framework Settings to Its Authoritative TOML Carrier

## Scope

the Framework Instance Settings Artifact for a Project named `<project_name>`.

## Claim

the Framework Instance Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml` as its **`=1`** authoritative TOML File Carrier.

## Details
