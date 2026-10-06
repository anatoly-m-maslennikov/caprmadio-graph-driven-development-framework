---
subjects:
  governs: "Lineage Impact Analysis"
  depends_on:
    - "Atom"
    - "Artifact/Revision"
    - "Atom Change Classification"
    - "Carrier-Only Recoding"
    - "Verification"
version: 20
updated_at: "2026-10-03 01:23:33 +0400"
relations:
  relates_to:
    - CA-R-1632
    - CA-R-1687
atom_id: "CA-R-1633"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Record one Lineage Impact Analysis per changed atom revision

## Scope

`semantic_revision`, `replacement`, `carrier_only`, and equivalent `refinement` changes of admitted Atoms.

## Claim

**every** `semantic_revision` **or** `replacement` of an admitted Atom **must** produce **`=1`** Lineage Impact Analysis Atom whose primary conclusion is the impact state of that exact changed parent Revision, while a `carrier_only` **or** equivalent `refinement` change **must** require lossless-recoding **or** equivalence Verification instead.

## Details
