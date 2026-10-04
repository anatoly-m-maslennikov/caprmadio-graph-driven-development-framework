---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Operator"
    - "AI Agent Delegation"
    - "Confidence Threshold"
version: 5
updated_at: "2026-09-28 15:12:22 +0400"
relations: {"child_of":["CA-R-1713"]}
atom_id: "CA-R-1555"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1555-CORE_META_MODEL-GENERAL--govern-ca-execution-gates.md
---
# Summary
Govern CA execution gates

## Scope
identified AI Agents considering clarification omission under applicable configured confidence requirements.

## Claim

an identified AI Agent **may** omit clarification **only** **when** confidence **in** **every** following item meets its applicable configured requirement:

- intent;
- scope;
- route;
- entry criteria.

confidence **must not** create delegated authority **or** bypass per-action Operator approval **when** active authority requires it.

## Details
