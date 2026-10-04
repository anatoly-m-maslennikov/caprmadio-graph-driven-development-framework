---
subjects:
  governs: "CAPRMEDIO Main Skill/Host Invocation"
  depends_on:
    - "CAPRMEDIO Main Skill"
version: 9
updated_at: "2026-10-01 21:24:59 +0400"
relations: {}
atom_id: "CA-D-344"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-344-PROJECT_CONFIGURATION-DELIVERY--serialize-main-skill-invocation-per-host.md
---
# Summary

Serialize Main Skill Invocation per Host

## Scope

Host Invocations for the CAPRMEDIO Main Skill **and** separately authorized compatibility layers.

## Claim

for the CAPRMEDIO Main Skill, the Host Invocation **must** serialize as `$ca` **in** Codex; **if** a Claude compatibility Extension **or** Operator-provided compatibility layer is separately authorized by the Operator, **then** its Host Invocation **must** serialize as `/ca` **in** Claude.

## Details
