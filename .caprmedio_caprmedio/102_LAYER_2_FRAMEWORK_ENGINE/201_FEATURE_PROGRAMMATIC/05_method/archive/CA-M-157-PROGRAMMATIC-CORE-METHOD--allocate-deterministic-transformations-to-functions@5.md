---
atom_id: CA-M-157
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - deterministic-transformation
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
# Allocate deterministic transformations to functions

Use a side-effect-free function as the default unit of PROGRAMMATIC behavior.
Implement one deterministic transformation as a function when its result
follows only from its declared inputs and the responsibility needs no identity
across calls.

## Applicable when

Apply when Tools, App backend services, or MCP components parse, classify,
validate, plan, project, format, or otherwise transform explicit input into a
result.

## Procedure

1. Use a function unless the responsibility must own mutable state, an
   invariant across calls, a resource, a lifecycle, or a replaceable adapter.
2. Give the function a specific, intention-revealing verb phrase that states
   its one responsibility; prefer clarity over brevity and split a function
   whose accurate name requires multiple responsibilities.
3. State the function's input, result, and failure values explicitly.
4. Do not mutate inputs or shared state, perform I/O or logging export, or read
   the filesystem, process, clock, environment, network, persistence, or
   randomness.
5. Pass every required observation and setting as explicit input rather than
   obtaining them implicitly.
6. Group related functions in a specifically named module; do not create a
   class only to provide a namespace.

## Outcome

Behavior is locally readable, reproducible from declared input, and free of
observable side effects. It can be reused, checked, or extended without
constructing component lifecycle state.

## Failure or stop

Stop treating the unit as a deterministic transformation when it applies an
external effect. A bounded one-shot effect may remain a function under
CA-M-160; allocate an object only when identity across calls or owned state,
invariant, resource, lifecycle, or adapter behavior is required.

## Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
