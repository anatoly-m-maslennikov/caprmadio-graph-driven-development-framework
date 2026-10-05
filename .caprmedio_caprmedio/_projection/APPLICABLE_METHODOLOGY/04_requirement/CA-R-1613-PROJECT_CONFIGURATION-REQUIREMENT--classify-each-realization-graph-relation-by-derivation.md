---
atom_id: CA-R-1613
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Realization Graph"
  depends_on:
    - "Evidence"
    - "Projection"
    - "Relation"
    - "Relation Derivation Class"
version: 4
updated_at: "2026-10-03 00:55:03 +0400"
relations:
  relates_to:
    - CA-R-1616
    - CA-R-1617
    - CA-R-1687
    - CA-R-1746
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1613-PROJECT_CONFIGURATION-REQUIREMENT--classify-each-realization-graph-relation-by-derivation.md
  source_atom_id: CA-R-1613
  source_atom_revision: 4
  source_sha256: 47b0fc650b5ad10e315e762a3101c3306f0ec74a19f3ab1509d692d91f5ed206
  original_relations_sha256: 9498a3bf925a4c9ab02a1ce984d38e81a4cea3f350b87deeacc61ca5f1581a30
---
# Summary

Classify each Realization Graph relation by derivation

## Scope

Represented Realization Graph Relations and their supported Relation Derivation Classes.

## Claim

**every** represented Realization Graph Relation **must** carry **`>=1`** supported Relation Derivation Classes, with the supporting source **or** execution evidence identified separately for **every** assigned class.

- **when** the same Relation is source-declared, resolved, **or** observed, multiple classifications **may** coexist; they describe evidence origins, **not** mutually exclusive truth values.
- a class identifies how the Relation was obtained. it does **not** prove that the Relation is required, correct, exhaustive, **or** currently applicable.
- missing **or** conflicting derivation evidence remains an explicit unresolved diagnostic; an unsupported class **or** Relation **must not** be presented as established.

## Details
