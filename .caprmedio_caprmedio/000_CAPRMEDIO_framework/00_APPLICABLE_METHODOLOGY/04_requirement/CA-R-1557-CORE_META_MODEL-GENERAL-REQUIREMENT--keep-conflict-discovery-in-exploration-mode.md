---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Operator"
    - "Exploration Mode"
    - "Atom/Content Role: Concern"
version: 5
updated_at: "2026-10-03 00:22:56 +0400"
relations: {"child_of":["CA-R-1702"]}
atom_id: "CA-R-1557"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1557-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-conflict-discovery-in-exploration-mode.md
  source_atom_id: CA-R-1557
  source_atom_revision: 5
  source_sha256: 5aacdee1be98f04966d555e5149fbfaa42c98ecacdef83f96c1fc40490997416
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep conflict discovery in Exploration Mode

## Scope

AI Agent discovery of conflicts in Exploration Mode.

## Claim

an AI Agent **must** keep a discovered conflict **in** Exploration Mode; it **may** create a Concern for that conflict **only** **when** the Operator requests persistence **or** defers its resolution.

## Details
