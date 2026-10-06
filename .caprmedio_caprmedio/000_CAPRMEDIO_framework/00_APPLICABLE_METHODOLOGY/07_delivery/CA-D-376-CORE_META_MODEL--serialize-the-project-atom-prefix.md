---
subjects:
  governs: "Project Settings/Atom Prefix/Carrier"
  depends_on:
    - "Project Settings"
    - "Atom"
    - "Operator"
version: 8
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - "CA-D-366"
atom_id: "CA-D-376"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-376-CORE_META_MODEL--serialize-the-project-atom-prefix.md
  source_atom_id: CA-D-376
  source_atom_revision: 8
  source_sha256: a8a1e395a50127fcc7ab120f2d4ca0d33c1176f35793cbaf218b6643bfdba46b
  original_relations_sha256: 60d285f0b5eadc5cfe0417918004395017eb1104d02fc3179cd56cf1f1493577
---
# Summary

Serialize the Project Atom prefix

## Scope

the Operator-selected Atom prefix in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

## Details
