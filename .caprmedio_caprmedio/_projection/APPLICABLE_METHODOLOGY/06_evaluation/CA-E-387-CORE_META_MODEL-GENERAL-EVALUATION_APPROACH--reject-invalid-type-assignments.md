---
subjects:
  governs: "Entity/Type"
  depends_on:
    - "Entity"
    - "Subject Expression"
    - "Type"
version: 13
updated_at: "2026-10-02 20:03:51 +0400"
relations: {"evaluation_for":["CA-R-1285","CA-R-1349","CA-R-1350"]}
atom_id: "CA-E-387"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-387-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--reject-invalid-type-assignments.md
  source_atom_id: CA-E-387
  source_atom_revision: 13
  source_sha256: 0fdebfd3a98131382e9c7e5a3be4f536e8e2a43481b081fc08fbce10f5eee93a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Reject Invalid Type Assignments

## Scope

Type assignments on Entity occurrences.

## Claim

the Evaluation **must** reject a Type assignment **if** **any** of the following holds:

- an Entity occurrence that bears Type has **`!=1`** direct Type values.
- the selected value is **not** allowed by its most-specific applicable qualified Type Subject.
- qualified Type Subjects create **`>1`** Type Property slots for the occurrence.

absence of a Type value **in** an Entity occurrence that does **not** bear Type is **not** a cardinality failure under this Evaluation.

## Details
