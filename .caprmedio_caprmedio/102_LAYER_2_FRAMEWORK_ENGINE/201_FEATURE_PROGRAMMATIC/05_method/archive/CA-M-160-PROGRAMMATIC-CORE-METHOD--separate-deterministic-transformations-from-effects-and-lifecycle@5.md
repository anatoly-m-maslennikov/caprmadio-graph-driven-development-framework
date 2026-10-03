---
atom_id: CA-M-160
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - effect-boundary
  depends_on:
    continuant:
      - programmatic software
version: 5
updated_at: 2026-09-01 01:33:45 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Separate deterministic transformations from effects and lifecycle

Keep PROGRAMMATIC decisions in a function-based deterministic core. Apply
filesystem, process, clock, environment, network, persistence, or
logging-export effects through a specifically named bounded one-shot function
when no identity or ownership is required, or through a specifically named
method on an object that owns state, an invariant, a resource, a lifecycle, or
a replaceable adapter.

## Applicable when

Apply when a Tool, App backend service, or MCP component combines a decision
with an external effect, asynchronous work, or lifecycle transition.

## Procedure

1. Form the decision, target, ordering, and expected outcome with deterministic
   functions from explicit observations before applying an effect.
2. Pass the resulting plan to one bounded effect boundary.
3. Use a function for a one-shot effect only when its complete target,
   dependency, input, outcome, and failure boundary are explicit and it owns
   no identity across calls, state, invariant, resource, lifecycle, or adapter.
4. Use a specifically named object method when the effect must own any of those
   responsibilities across calls.
5. Return typed observations or completion facts to the decision boundary;
   do not let the effect owner invent, reorder, or suppress a decision.

## Outcome

Decision logic is locally readable and replayable. Each effect has a visible,
bounded function or object owner, ordered input, and recoverable result
boundary. Objects exist only where persistent identity or ownership requires
them.

## Failure or stop

Stop execution when the plan is incomplete, an effect owner would make a new
business decision, a one-shot effect hides a dependency or exceeds its declared
boundary, an object exists without owned identity or ownership, or the effect
boundary cannot report a typed result.

## Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [Python documentation: data classes](https://docs.python.org/3.14/library/dataclasses.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
