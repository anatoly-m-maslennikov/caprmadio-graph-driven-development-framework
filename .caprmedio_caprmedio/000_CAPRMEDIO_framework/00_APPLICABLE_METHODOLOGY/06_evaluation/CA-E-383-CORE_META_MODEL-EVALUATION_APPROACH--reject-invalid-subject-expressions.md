---
subjects:
  governs: "Subject Expression Evaluation"
  depends_on:
    - "General Term"
    - "Governed Term"
    - "Subject Expression"
    - "Dependent Entity"
    - "Property"
    - "IS_BORNE_BY"
    - "IS_ALLOWED_VALUE_OF"
    - "Term"
    - "CCE Operator"
    - "Scope Unit/Name"
    - "Subject"
    - "Subject Path"
version: 13
updated_at: "2026-10-01 21:36:04 +0400"
relations:
  evaluation_for:
    - CA-R-1194
    - CA-R-1204
    - CA-R-1245
    - CA-R-1436
    - CA-M-229
    - CA-R-1324
    - CA-R-1325
    - CA-R-1321
    - CA-R-1275
    - CA-R-1297
atom_id: "CA-E-383"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-383-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-subject-expressions.md
  source_atom_id: CA-E-383
  source_atom_revision: 13
  source_sha256: 00c3e901fbd18cdb584387386f6b04cd43905f651c4369e16a97d20b469b3274
  original_relations_sha256: f9669e1f1833a322d66483ad6508513c6452d1b1a619dc9d0bbcdaefb6ece8e4
---
# Reject Invalid Subject Expressions

## Scope

Subject Expressions evaluated for invalid component handling.

## Claim

the Evaluation **must** reject a Subject Expression **if**

- `/` does **not** encode **`=1`** valid bearer edge,
- `:` does **not** express **`=1`** admitted IS_ALLOWED_VALUE_OF qualification under CA-R-1436-CORE_META_MODEL-CORE-REQUIREMENT--define-is-allowed-value-of,
- allowed-value admission is treated as assignment **to** a particular Property occurrence **or** as determining its cardinality,
- a Dependent Entity occurrence lacks **`=1`** immediate bearer,
- a reusable Term is rejected **only** for changing ordinal position,
- a Governed Term begins with a lowercase letter,
- a named component fails **to** resolve **to** a Term under CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression,
- an ordinary General Term is substituted for a required Term reference,
- a Term name **contains** `/` **or** `:`,
- a complete composite Subject Expression is classified as one Term,
- **or** a registered CCE Operator is redefined as a Governed Term **or** Scope Unit Name.

## Details

### Term-component cases

`Atom/Content Role: Requirement/Type: Demand` **must** pass the component check **when** its five named Terms **and** exact qualified target are admitted. `/` **and** `:` contribute no Term nodes. an unresolved named component **must** fail the source-reference check; the diagnostic **must** preserve the unresolved reference **without** supplying an invented definition. a complete composite path **must not** be admitted as **`=1`** Term merely because it resolves **to** **`=1`** Entity.
