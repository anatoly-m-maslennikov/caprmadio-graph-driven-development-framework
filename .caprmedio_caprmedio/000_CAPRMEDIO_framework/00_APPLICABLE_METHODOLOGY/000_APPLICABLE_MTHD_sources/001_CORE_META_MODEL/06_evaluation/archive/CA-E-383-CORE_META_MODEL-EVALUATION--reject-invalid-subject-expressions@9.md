---
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
    - "Subject"
    - "Subject Path"
version: 9
updated_at: "2026-09-15 21:31:49 +0000"
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
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject Invalid Subject Expressions

the Evaluation **must** reject a Subject Expression **if**

- `/` does **not** encode **`=1`** valid bearer edge,
- `:` does **not** express **`=1`** admitted IS_ALLOWED_VALUE_OF qualification under CA-R-1436,
- allowed-value admission is treated as assignment **to** a particular Property occurrence **or** as determining its cardinality,
- a Dependent Entity occurrence lacks **`=1`** immediate bearer,
- a reusable Term is rejected **only** for changing ordinal position,
- a Governed Term begins with a lowercase letter,
- a named component fails **to** resolve **to** a Term under CA-R-1321,
- an ordinary General Term is substituted for a required Term reference,
- a Term name **contains** `/` **or** `:`,
- a complete composite Subject Expression is classified as one Term,
- **or** a registered CCE Operator is redefined as a Governed Term **or** Scope Unit Name.

## Term-component cases

`Atom/Content Role: Requirement/Type: Demand` **must** pass the component check **when** its five named Terms **and** exact qualified target are admitted. `/` **and** `:` contribute no Term nodes. an unresolved named component **must** fail the source-reference check; the diagnostic **must** preserve the unresolved reference **without** supplying an invented definition. a complete composite path **must not** be admitted as **`=1`** Term merely because it resolves **to** **`=1`** Entity.
