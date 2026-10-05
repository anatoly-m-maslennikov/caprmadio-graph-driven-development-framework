---
subjects:
  governs: "CAPRMEDIO Framework Instance/Carrier Root"
  depends_on: []
version: 12
updated_at: "2026-10-05 00:25:37 +0400"
relations: {}
atom_id: "CA-D-317"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-317-CORE_META_MODEL--place-each-project-framework-instance-inside-its-project.md
  source_atom_id: CA-D-317
  source_atom_revision: 12
  source_sha256: c93ede85518a750816c36cff62d6f7e1ec3a66377f31ae221d17296cac30c8ef
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Place each Project Framework Instance inside its Project

## Scope

CAPRMEDIO Framework Instances serving Projects.

## Claim

the Methodology **and** Tool governance of the CAPRMEDIO Framework Instance serving a Project **must** reside under that Project's `.caprmedio_<project_name>/000_CAPRMEDIO_framework/` Directory Carrier. this Carrier **must** contain that Project's Methodology Sources **and** Framework Instance Settings. another Project's Framework Instance **or** a repository-shared framework directory **must not** substitute for this Project's instance.

## Details

Applicable Methodology **is** a Projection; its delivered Carriers use the Project's `_projection/` root, **not** this source-governance Carrier.
