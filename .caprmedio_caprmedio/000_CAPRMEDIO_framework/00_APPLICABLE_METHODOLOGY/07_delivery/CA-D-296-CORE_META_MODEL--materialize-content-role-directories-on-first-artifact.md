---
subjects:
  governs: "Artifact/Carrier Placement"
  depends_on:
    - "Atom/Content Role"
    - "Scope Unit"
    - "Artifact"
    - "Directory Carrier"
version: 13
updated_at: "2026-10-02 19:05:39 +0400"
relations: {}
atom_id: "CA-D-296"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-296-CORE_META_MODEL--materialize-content-role-directories-on-first-artifact.md
  source_atom_id: CA-D-296
  source_atom_revision: 13
  source_sha256: 7c4f2e99149fb2d2f0e04207ce06be0b5ce2a056fab7520f19b860d0e13f93da
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Materialize Content Role Directories on First Artifact

## Scope

administrative Content Role directories in Scope Units.

## Claim

a Scope Unit's administrative Content Role directory **must** be materialized for canonical Artifact placement **only** **when** the first current Artifact requires that placement.

## Details

an absent Content Role directory **must** represent empty role placement, **not** an absent Scope Unit. this administrative directory does **not** itself carry a Structural Entity **or** become a Directory Carrier under CA-D-451. this materialization condition does **not** require deletion of an existing empty directory.
