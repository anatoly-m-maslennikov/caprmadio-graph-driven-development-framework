---
subjects:
  governs: "Project Settings/Authoritative Carrier"
  depends_on:
    - "Project Settings/Authoritative Carrier/Filename"
version: 9
updated_at: "2026-10-01 21:24:59 +0400"
relations:
  child_of:
    - CA-D-363
atom_id: "CA-D-364"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-364-CORE_META_MODEL-DELIVERY--bind-project-settings-to-its-authoritative-toml-carrier.md
  source_atom_id: CA-D-364
  source_atom_revision: 9
  source_sha256: d3c65961678f87759d0fe6155d1d7ff01c545cd6d93f9593d938241dd4637c1e
  original_relations_sha256: 5bb95efc70c0da210c80e3bdbc8549784b990261ebad7f7e71888cf52216ac85
---
# Summary

Bind Project Settings **to** its authoritative TOML Carrier

## Scope

the authoritative TOML File Carrier for Project Settings of a Project named `<project_name>`.

## Claim

the Project Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/caprmedio_<project_name>_settings.toml` as its **`=1`** authoritative TOML File Carrier.

## Details
