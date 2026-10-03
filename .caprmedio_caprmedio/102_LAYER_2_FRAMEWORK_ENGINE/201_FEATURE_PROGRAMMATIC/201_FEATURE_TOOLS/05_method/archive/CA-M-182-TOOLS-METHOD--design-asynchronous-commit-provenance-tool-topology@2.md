---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - artifact-operations
version: 2
updated_at: 2026-08-25 01:49:10 +0400
relations:
  method_for:
    - CA-R-802
  derived_from:
    - CA-A-058
---
# Design asynchronous commit-provenance Tool topology

## Applicable when

Apply when a Tool chain must accept work without blocking its host and must survive interruption, backpressure, retry, or service replacement.

## Procedure

1. Give the chain one deterministic I/O-free manager. Supply repository, queue, action, worker-result, settings, lease, circuit, and clock facts as explicit typed inputs; return one complete typed execution graph or one admissible next command.
2. Persist the immutable graph and every transition under .caprmedio_runtime. Give each step a stable action and step identity, typed input and output contracts, declared dependencies, bounded retry routes, and terminal outcomes.
3. Let a mechanical Scheduler claim only ready steps and advance only manager-declared transitions. A completion may make one declared step ready but may not select, reorder, skip, or invent downstream work.
4. Give each worker one atomic mechanical operation. Isolate filesystem, process, clock, environment, logging, and persistence effects in workers or adapters.
5. Use a direct typed handoff only for short synchronous work that needs no independent recovery. Use durable scheduling when work must survive interruption, wait, apply backpressure, or retry independently.
6. Use idempotency for repeatable effects and an exclusive lease or compare-and-set boundary for non-repeatable effects. Record attempts, leases, input and result digests, completion identities, diagnostics, and admissible recovery transitions.

## Outcome

The manager owns every business decision, the Scheduler advances the accepted graph without semantic discretion, workers remain atomic and non-deciding, and queued work survives manager or service termination.

## Failure or stop

Reject undeclared cycles or transitions. Stop autonomous execution when state, authority, lease integrity, or the next admissible transition is absent, ambiguous, stale, or invalid.
