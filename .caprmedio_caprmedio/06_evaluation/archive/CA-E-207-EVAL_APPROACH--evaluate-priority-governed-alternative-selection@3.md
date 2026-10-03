---
atom_id: CA-E-207
subject_scopes:
  - operator-priorities
tier: core
version: 3
updated_at: 2026-08-21 07:29:53
relations:
  child_of:
    - CA-R-815-PRINCIPLE-REQUIREMENT--provide-operator-priority-governed-project-trade-offs
  evaluation_for:
    - CA-R-860-REQUIREMENT--derive-one-effective-operator-priority-order
---
# Evaluate priority-governed alternative selection

## Claim checked

The selected alternative satisfies active constraints and the current Operator priority ordering.

## Applicable conditions

Apply when CAPRMEDIO selects among acceptable alternatives for an affected scope and project stage.

## Acceptance

Pass only when the selected alternative satisfies every active constraint and follows the current Operator priority ordering for that scope and stage.

## Failure

Reject the selection and report every breached constraint or priority-order mismatch to the Operator.
