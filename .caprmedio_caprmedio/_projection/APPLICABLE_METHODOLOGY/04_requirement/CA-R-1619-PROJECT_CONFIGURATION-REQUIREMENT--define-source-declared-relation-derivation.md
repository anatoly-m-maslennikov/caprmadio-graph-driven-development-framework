---
atom_id: CA-R-1619
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Source-declared Relation Derivation"
  depends_on:
    - "Evidence"
    - "Realization Graph"
    - "Relation"
    - "Relation Derivation Class"
version: 4
updated_at: "2026-10-03 01:07:45 +0400"
relations:
  relates_to:
    - CA-R-1616
    - CA-R-1617
    - CA-R-1687
    - CA-R-1746
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1619-PROJECT_CONFIGURATION-REQUIREMENT--define-source-declared-relation-derivation.md
  source_atom_id: CA-R-1619
  source_atom_revision: 4
  source_sha256: ffb1569bf13c6dd0f71ffe2242f2a939cfe7d26533a4d5630f51617bb00ee812
  original_relations_sha256: 9498a3bf925a4c9ab02a1ce984d38e81a4cea3f350b87deeacc61ca5f1581a30
---
# Summary

Define Source-declared Relation Derivation

## Scope

source-declared derivation of represented Realization Graph Relations.

## Claim

Source-declared Relation Derivation **means** that a represented Realization Graph Relation is explicitly encoded **in** an identified selected native source, manifest, **or** configuration.

## Details

the result **must** identify the exact source occurrence **and** the interpretation used **to** read that declaration. declaring a Relation does **not** establish that it executes, resolves successfully, **or** satisfies a Requirement.
