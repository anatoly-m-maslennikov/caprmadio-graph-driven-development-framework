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
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-387-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--reject-invalid-type-assignments.md
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
