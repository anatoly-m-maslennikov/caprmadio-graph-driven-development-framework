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
version: 1
updated_at: "2026-09-28 15:12:22 +0400"
relations: {}
---
# Summary

Use the governed production logging platform

## Scope

production logs emitted by production-relevant components.

## Claim

production logs use the deployment environment's governed logging sink. governed CAPRMEDIO workflow Journals **and** local project-control Journals are **not** substitutes for the production system's log platform.

## Details

the governed sink is the production-log platform; workflow Journals **and** project-control Journals retain their own governed records **without** replacing that platform.
