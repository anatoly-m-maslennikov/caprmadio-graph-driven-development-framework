---
tier: core
version: 3
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - CA-R-004
  evaluation_for:
    - CA-R-004
subjects:
  governs:
    occurrent:
      - "CAPRMEDIO Framework Instance/control"
  depends_on:
    continuant:
      - "Operator"
      - "Project"
      - "CAPRMEDIO Framework Instance"
cce_version: cce_1
cce_form: evaluation
atom_id: CA-E-228
---
# Evaluate Operator control over the CAPRMEDIO instance

## Claim checked

the declared Operators collectively retain control over **every** governed part of the CAPRMEDIO instance **and** can use the instance **to** change the Project within their current authority.

## Applicable conditions

apply **after** a material change **to** the CAPRMEDIO instance, its authority, **or** the mechanisms through which Operators change the Project.

## Check

enumerate **every** governed part of the current CAPRMEDIO instance **and** **every** Operator-authorized Project-change operation exposed through it. for **every** part, demonstrate that the declared Operators can collectively inspect **and** direct it under their current authority. for **every** operation, demonstrate that **`>=1`** admissible Operator-controlled path can apply the change **to** the Project.

## Acceptance

pass **only** **when** **every** governed instance part is collectively inspectable **and** directable by the declared Operators **and** **every** admitted Project-change operation has an admissible Operator-controlled execution path.

## Failure

fail **and** report **every** uncontrolled instance part **or** unavailable Operator-controlled Project-change path.
