---
tier: core
version: 3
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - CA-R-846
  evaluation_for:
    - CA-R-846
subjects:
  governs:
    occurrent:
      - "AI Agent/authorization"
  depends_on:
    continuant:
      - "Operator"
      - "AI Agent Delegation"
      - "AI Agent"
      - "Carrier"
      - "Atom/Content Role: Implementation"
cce_version: cce_1
cce_form: evaluation
atom_id: CA-E-230
---
# Evaluate Operator control of AI permissions

## Claim checked

the Operator can create, inspect, limit, modify, suspend, **and** revoke AI Agent Delegations **and** mandatory authorization rules for identified AI Agents.

## Applicable conditions

apply **to** **every** supported delegation **or** mandatory-authorization-rule Carrier **and** **after** a material change **to** their governance **or** Implementation.

## Check

for one identified AI Agent, exercise creation, inspection, limitation, modification, suspension, **and** revocation on one test AI Agent Delegation **and** one test mandatory authorization rule through Operator-controlled paths. **after** **every** operation, inspect the effective state of the affected delegation **or** rule **and** verify that it matches the Operator action. check **every** applicable control operation for the test delegation **and** the test authorization rule; successful delegation control **must not** substitute for authorization-rule control.

## Acceptance

pass **only** **when** **every** required operation for delegations **and** mandatory authorization rules is available **to** the authorized Operator **and** produces the inspected effective state requested by that Operator.

## Failure

fail **and** report **every** unavailable operation, unauthorized state change, **or** mismatch between requested **and** effective delegation **or** authorization-rule state.
