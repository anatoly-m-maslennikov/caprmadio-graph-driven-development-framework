---
atom_id: "CA-R-1782"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Implementation"
  depends_on:
    - "Logging Policy"
version: 1
updated_at: "2026-09-28 15:12:22 +0400"
relations: {}
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1782-PROJECT_CONFIGURATION--control-production-debug-enablement.md
  source_atom_id: CA-R-1782
  source_atom_revision: 1
  source_sha256: 7499855f508732e322b6fa817a13deeac0a282ba6182275bbbd53f5d35d939ba
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Control production DEBUG enablement

## Scope

logging Implementation for production DEBUG logging under Logging Policies.

## Claim

logging Implementation **must** keep production DEBUG logging disabled by default. temporary enablement **must** be scoped by component, subject, run, entity, **or** another bounded selector, have an automatic expiry, **and** preserve the same redaction rules as **every** other level.

## Details

the selector **and** expiry bound temporary production DEBUG use while preserving its required redaction treatment.
