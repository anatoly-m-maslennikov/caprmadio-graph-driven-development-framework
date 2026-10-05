---
subjects:
  governs: "GOVERNS"
  depends_on:
    - "Definition Atom"
    - "Subject"
    - "Term"
    - "Subject Path"
    - "Atom/Claim"
version: 12
updated_at: "2026-10-02 21:45:33 +0400"
relations: {}
atom_id: "CA-R-1279"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1279-CORE_META_MODEL-CORE-REQUIREMENT--govern-every-defined-term.md
  source_atom_id: CA-R-1279
  source_atom_revision: 12
  source_sha256: 80e2ba7b9461cf5909891d3c7c2c2bcd12baccc161b7a86f7b977552a61666d5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Govern Every Defined Term

## Scope

defined Terms and their canonical direct GOVERNS Subject Relation.

## Claim

**every** Definition Atom **must** use its **`=1`** direct GOVERNS Subject Relation **to** identify the canonical target defined by its Claim, with the defined Term as the terminal name **in** that target's Subject Path. the defining Claim establishes that Term's meaning; the other Term components **in** the path are references **to** their own definitions, **not** additional definitions supplied by this Atom.

## Details
