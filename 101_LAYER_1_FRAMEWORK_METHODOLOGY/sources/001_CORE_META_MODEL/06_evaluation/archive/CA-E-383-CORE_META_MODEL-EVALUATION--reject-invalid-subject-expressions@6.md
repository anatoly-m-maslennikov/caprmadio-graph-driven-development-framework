---
atom_id: CA-E-383
cce_version: cce_1
cce_form: evaluation
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
version: 6
updated_at: "2026-09-13 03:53:49 +0400"
relations:
  evaluation_for:
    - CA-R-1194
    - CA-R-1204
    - CA-R-1245
    - CA-R-1436
    - CA-R-1322
    - CA-R-1323
    - CA-R-1324
    - CA-R-1325
    - CA-R-1297
---
# Reject Invalid Subject Expressions

the Evaluation **must** reject a Subject Expression **if** `/` does **not** encode **`=1`** valid bearer edge, `:` does **not** express **`=1`** admitted IS_ALLOWED_VALUE_OF qualification under CA-R-1436, allowed-value admission is treated as assignment **to** a particular Property occurrence **or** as determining its cardinality, a Dependent Entity occurrence lacks **`=1`** immediate bearer, a reusable Term is rejected **only** for changing ordinal position, a Governed Term begins with a lowercase letter, a General Term begins with a capital letter, a Term name **contains** `/` **or** `:`, a complete composite Subject Expression is classified as one Term, **or** a registered CCE Operator is redefined as a Governed Term **or** Scope Unit Name.
