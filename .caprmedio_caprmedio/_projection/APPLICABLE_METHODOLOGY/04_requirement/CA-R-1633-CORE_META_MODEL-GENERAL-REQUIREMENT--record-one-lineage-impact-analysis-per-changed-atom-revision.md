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
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1633-CORE_META_MODEL-GENERAL-REQUIREMENT--record-one-lineage-impact-analysis-per-changed-atom-revision.md
  source_atom_id: CA-R-1633
  source_atom_revision: 20
  source_sha256: bd6d8f8d72e05f3a90e490e1d0d3804f2843a8fc7a42b3bec6b4f1944366cfdd
  original_relations_sha256: c7fa64331151a0cf79b662ca47c7f4718bd3cf68c09cb3f68cd810e2a706fd05
---
# Summary

Record one Lineage Impact Analysis per changed atom revision

## Scope

`semantic_revision`, `replacement`, `carrier_only`, and equivalent `refinement` changes of admitted Atoms.

## Claim

**every** `semantic_revision` **or** `replacement` of an admitted Atom **must** produce **`=1`** Lineage Impact Analysis Atom whose primary conclusion is the impact state of that exact changed parent Revision, while a `carrier_only` **or** equivalent `refinement` change **must** require lossless-recoding **or** equivalence Verification instead.

## Details
