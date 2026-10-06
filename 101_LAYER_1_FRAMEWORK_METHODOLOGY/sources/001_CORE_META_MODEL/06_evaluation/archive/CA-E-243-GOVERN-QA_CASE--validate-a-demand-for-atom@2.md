---
subject_scopes:
  - relation-model
version: 2
updated_at: 2026-08-22 06:00:00
relations:
  child_of:
    - CA-E-001-PRINCIPLE-EVALUATION--make-accepted-requirements-checkable
    - CA-E-206-EVAL_APPROACH--require-usable-inputs-for-reliance
  evaluation_for:
    - CA-R-904
    - CA-R-905
    - CA-R-907
    - CA-R-908
    - CA-R-912
    - CAPRMEDIO-GOV-REQU-747--register-external-and-relational-atom-types
    - CA-R-859
  replacement_of:
    - CA-E-238
---
# Validate a Demand For Atom

## Claim checked

An active Demand For Atom is a Requirement Atom whose filename names one Claim Scope after `DEMAND_FOR`. Its Claim Scope differs from its Current Scope and is neither an ancestor nor a descendant of its Current Scope.

## Test case

Construct one valid Demand For Atom between separate Structural branches. Then independently remove the Claim Scope, add a second Claim Scope, make the Claim Scope equal the Current Scope, use an unknown Claim Scope, target an ancestor, target a descendant, use a non-Requirement Content role, declare semantic shape, or add endpoint, controller, follower, or target Content-role metadata.

## Acceptance criteria

The valid fixture passes. Every invalid fixture fails and identifies the exact missing, duplicate, equal, unknown, role-inconsistent, topology-inconsistent, or prohibited element.

## Failure disposition

Record a Concern naming the invalid Demand For carrier and stop acceptance for that carrier.
