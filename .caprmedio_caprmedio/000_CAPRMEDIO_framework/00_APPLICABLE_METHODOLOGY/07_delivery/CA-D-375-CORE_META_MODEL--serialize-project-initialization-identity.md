---
subjects:
  governs: "Project Settings/Project identity/Carrier"
  depends_on:
    - "Project Settings"
    - "Project"
    - "Project Name"
    - "Operator"
    - "Atom"
    - "Implementation"
version: 9
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - "CA-D-366"
atom_id: "CA-D-375"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-375-CORE_META_MODEL--serialize-project-initialization-identity.md
  source_atom_id: CA-D-375
  source_atom_revision: 9
  source_sha256: 404da79b6bb14e62c88ad5409b1f1947f907acf5812fd1b8ca3a53ce18e7c5d7
  original_relations_sha256: 60d285f0b5eadc5cfe0417918004395017eb1104d02fc3179cd56cf1f1493577
---
# Summary

Serialize Project initialization identity

## Scope

the Operator-selected Project Name in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact lowercase value **in** `project.name`, **before** the first Project Atom **or** Implementation is created.

## Details
