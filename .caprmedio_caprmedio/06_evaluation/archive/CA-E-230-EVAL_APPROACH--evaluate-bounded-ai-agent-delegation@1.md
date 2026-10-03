---
subject_scopes:
  - principles
tier: core
version: 1
updated_at: 2026-08-21 05:03:35
relations:
  child_of:
    - CA-R-846-PRINCIPLE-REQUIREMENT--provide-bounded-delegation-to-ai-agents
  evaluation_for:
    - CA-R-846-PRINCIPLE-REQUIREMENT--provide-bounded-delegation-to-ai-agents
---
# Evaluate bounded AI Agent delegation

## Claim checked

Operators can create, inspect, limit, modify, suspend, and revoke delegations to identified AI Agents.

## Applicable conditions

Apply to every supported delegation carrier and after a material change to delegation governance or realization.

## Check

For one identified AI Agent and one test delegation, exercise creation, inspection, limitation, modification, suspension, and revocation through Operator-controlled paths. After each operation, inspect the effective delegation state and verify that it matches the Operator action.

## Acceptance

Pass only when every required operation is available to an authorized Operator and produces the inspected effective delegation state requested by that Operator.

## Failure

Fail and report every unavailable operation, unauthorized state change, or mismatch between requested and effective delegation state.
