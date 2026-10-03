---
subject_scopes:
  - principles
tier: core
version: 5
updated_at: 2026-08-21 02:55:24
relations:
  child_of:
    - CA-D-003-PRINCIPLE-DELIVERY--provide-one-project-graph-as-the-operating-model
    - CA-E-001-PRINCIPLE-EVALUATION--make-accepted-requirements-checkable
  evaluation_for:
    - CAPRMEDIO-REQU-026--define-the-project-principle-universe
    - CA-R-830-REQUIREMENT-BSEED_GOVERNANCE--reserve-principle-conflict-resolution-to-the-operator
---
# Principle-first alignment

## Claim checked

For every selected Structural level and given scope, the complete active Atom set is aligned with every active Project Principle.

## Check

Load the complete active Project Principle set first, resolve the Structural level and scope, collect the complete active Atom set, and evaluate every Atom against every Principle before applying lower-tier authority.

## Acceptance

Pass only when no Atom conflicts with a Project Principle and no lower-tier interpretation weakens or overrides one.

## Failure

Report every conflicting Atom and Principle pair; route each conflict between active Project Principles to the Operator under `CA-R-830`.
