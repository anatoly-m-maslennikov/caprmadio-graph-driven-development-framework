---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 9
updated_at: 2026-09-04 03:10:59 +0400
relations:
  method_for:
    - CA-R-802
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Design asynchronous commit-provenance Tool topology

## Applicable when

apply **when** a Tool chain **must** accept work **without** blocking its host **and** **must** survive interruption, backpressure, retry, **or** service replacement.

## Procedure

1. give the chain one deterministic I/O-free manager. supply repository, queue, action, worker-result, settings, lease, circuit, **and** clock facts as explicit typed inputs; return one complete typed execution graph **or** one admissible next command.
2. resolve the current COMMIT_AUTOMATION autonomy envelope **before** admitting work. fail closed **unless** the repository, subject scope, time window, action class, queue **and** resource caps, **and** Work binding are current **and** the action class is a local real-change commit **or** local Journal-only commit.
3. persist the immutable graph, resolved envelope identity, **and** **every** transition under .caprmedio_runtime. give each step a stable action **and** step identity, typed input **and** output contracts, declared dependencies, bounded retry routes, **and** terminal outcomes.
4. let a mechanical Scheduler claim **only** ready steps **and** advance **only** manager-declared transitions. a completion **may** make one declared step ready but **may** **not** select, reorder, skip, **or** invent downstream work. enforce pause, resume, narrowing, expiry, **and** circuit state **before** dispatch **and** again **before** each effect.
5. give each worker one atomic mechanical operation. isolate filesystem, process, clock, environment, logging, **and** persistence effects **in** workers **or** adapters. the actor that authorizes **or** overrides an envelope **must not** be the worker that executes its commit effect.
6. use a direct typed handoff **only** for short synchronous work that needs no independent recovery. use durable scheduling **when** work **must** survive interruption, wait, apply backpressure, **or** retry independently.
7. use idempotency for repeatable effects **and** an exclusive lease **or** compare-and-set boundary for non-repeatable effects. record attempts, leases, input **and** result digests, completion identities, diagnostics, **and** admissible recovery transitions.

## Outcome

the manager owns **every** business decision, the Scheduler advances the accepted graph **without** semantic discretion, workers remain atomic **and** non-deciding, **and** queued work survives manager **or** service termination.

## Failure or stop

reject undeclared cycles **or** transitions. stop autonomous execution **when** state, authority, Work binding, envelope, cap, lease integrity, **or** the next admissible transition is absent, ambiguous, stale, exceeded, **or** invalid. recovery **may** resume **only** under the same still-current envelope **or** a narrower **or** independently authorized replacement.
