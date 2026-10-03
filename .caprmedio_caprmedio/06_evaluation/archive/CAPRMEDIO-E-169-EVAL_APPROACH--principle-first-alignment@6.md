---
subject_scopes:
  - "principles"
tier: "core"
version: 6
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  child_of:
    - "CA-M-006"
    - "CA-E-001"
  evaluation_for:
    - "CAPRMEDIO-REQU-026--define-the-project-principle-universe"
    - "CA-R-830-REQUIREMENT-BSEED_GOVERNANCE--reserve-principle-conflict-resolution-to-the-operator"
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
