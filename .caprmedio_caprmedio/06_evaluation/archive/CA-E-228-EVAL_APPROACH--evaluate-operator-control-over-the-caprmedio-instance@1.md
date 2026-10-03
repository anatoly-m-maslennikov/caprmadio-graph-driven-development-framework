---
subject_scopes:
  - principles
tier: core
version: 1
updated_at: 2026-08-21 05:03:35
relations:
  child_of:
    - CA-R-004-PRINCIPLE-REQUIREMENT--provide-operator-control-over-the-caprmedio-instance
  evaluation_for:
    - CA-R-004-PRINCIPLE-REQUIREMENT--provide-operator-control-over-the-caprmedio-instance
---
# Evaluate Operator control over the CAPRMEDIO instance

## Claim checked

The declared Operators collectively retain control over every governed part of the CAPRMEDIO instance and can use the instance to change the project within their current authority.

## Applicable conditions

Apply after a material change to the CAPRMEDIO instance, its authority, or the mechanisms through which Operators change the project.

## Check

Enumerate every governed part of the current CAPRMEDIO instance and every Operator-authorized project-change operation exposed through it. For each part, demonstrate that the declared Operators can collectively inspect and direct it under their current authority. For each operation, demonstrate that at least one admissible Operator-controlled path can apply the change to the project.

## Acceptance

Pass only when every governed instance part is collectively inspectable and directable by the declared Operators and every admitted project-change operation has an admissible Operator-controlled execution path.

## Failure

Fail and report every uncontrolled instance part or unavailable Operator-controlled project-change path.
