---
atom_id: "CA-D-504"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Carrier"
  depends_on:
    - "Journal"
version: 2
updated_at: "2026-10-04 22:11:24 +0000"
relations: {}
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-504-PROJECT_CONFIGURATION--use-the-governed-production-logging-platform.md
  source_atom_id: CA-D-504
  source_atom_revision: 2
  source_sha256: 4761972e101bf628d970012da9c9a4a73ef6560e5b52973848122c91979df708
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Use the governed production logging platform

## Scope

production technical and business runtime log Journal Carriers.

## Claim

production technical **and** business runtime log Journals **must** use the deployment environment's governed logging sink. governed CAPRMEDIO workflow **and** local project-control Journals **are not** substitutes for the production system's log platform.

## Details

The configured production-log sink may be a local database, remote database, or another governed logging platform. Runtime logs retain Journal classification and recorded-history authority without being forced into _journal. Workflow and project-control Journals retain their own governed records without replacing that platform or duplicating authority for the same historical fact.
