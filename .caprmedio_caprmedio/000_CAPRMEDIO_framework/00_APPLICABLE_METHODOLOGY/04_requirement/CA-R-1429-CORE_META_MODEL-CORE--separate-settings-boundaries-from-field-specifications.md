---
subjects:
  governs: "settings specification"
  depends_on:
    - "Project Settings"
    - "Framework Instance Settings"
    - "Default Settings"
    - "Atom/Local Tier"
    - "Scope Unit"
version: 10
updated_at: "2026-10-02 22:59:46 +0400"
relations: {}
atom_id: "CA-R-1429"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1429-CORE_META_MODEL-CORE--separate-settings-boundaries-from-field-specifications.md
  source_atom_id: CA-R-1429
  source_atom_revision: 10
  source_sha256: ba0e34e5057a5acb5f3c1a875214a373b167a860ed3ac0b6d708a3c657fdd7ed
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Separate settings boundaries from field specifications

## Scope

the authority boundary between settings foundations, shared settings specifications, **and** concrete specifications.

## Claim

- the Core-tier Atoms for Project Settings, Framework Instance Settings, **and** Default Settings **must** define their purpose, content, **and** authority boundaries;
- an independently governable shared settings specification **must** belong **to** General **when** General is admitted **in** its current Scope Unit **and** it preserves those foundations **without** selecting a concrete representation;
- **every** concrete section, field, **or** Carrier syntax specification **must** belong **to** Standard.

a setting **must not** require a General Atom **unless** a distinct shared specification requires independent authority.

## Details
