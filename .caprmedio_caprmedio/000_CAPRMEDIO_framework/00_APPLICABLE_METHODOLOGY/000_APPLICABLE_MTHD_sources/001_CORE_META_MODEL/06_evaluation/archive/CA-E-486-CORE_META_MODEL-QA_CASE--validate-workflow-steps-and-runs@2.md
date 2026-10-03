---
subjects:
  governs: "Workflow"
  depends_on:
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Step Run"
    - "Workflow/Relation Kind: On Result"
    - "Journal/Record"
version: 2
updated_at: "2026-09-18 14:16:20 +0000"
relations: {"evaluation_for": ["CA-R-1508", "CA-R-1509", "CA-R-1510", "CA-R-1511", "CA-R-1513"]}
---
# Validate Workflow Steps and Runs

## Cases

1. define **`=2`** distinct Steps referencing the same Action with different input bindings; follow an admitted conditional transition between the Steps.
2. revisit a Step under an accepted retry allowance within **`=1`** Workflow Run.
3. introduce a Step with **`=0`** Action references, **`>1`** Action references, an unresolved Action, **or** an unresolved required input binding.
4. introduce an untyped edge, an edge whose endpoint is an Action rather than a Step, **or** a next-Step reference missing from that Workflow.
5. record a failed Step Run; separately reference a reusable Workflow definition **without** recording an execution.

## Acceptance

- the valid shared Action retains **`=1`** definition; Step bindings remain distinct.
- **every** actual revisit creates a distinct Step Run within the same Workflow Run **without** resetting its retry allowance.
- invalid Action cardinality, unresolved inputs, invalid endpoints, **and** untyped transitions fail the check.
- failed **or** absent execution evidence **must not** become successful completion, a new Workflow definition, **or** another historical source.

report the exact failing source, case, **and** condition; do **not** change source authority **to** make the check pass.
