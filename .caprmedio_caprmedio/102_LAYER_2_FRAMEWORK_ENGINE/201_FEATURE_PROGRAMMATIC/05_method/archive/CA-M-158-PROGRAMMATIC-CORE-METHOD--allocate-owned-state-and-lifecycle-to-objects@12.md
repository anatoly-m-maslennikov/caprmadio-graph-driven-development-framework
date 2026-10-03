---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "component-lifecycle"
  depends_on:
    - "programmatic software"
version: 12
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Allocate owned state and lifecycle to objects

introduce an object **only** **when** one PROGRAMMATIC responsibility needs identity
across calls because it owns mutable technical state, preserves an invariant,
manages a resource **or** lifecycle, **or** implements a replaceable adapter. do **not**
create an object merely **to** group functions **or** **to** perform a bounded one-shot
effect.

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component **must** retain state,
preserve an invariant across calls, acquire **or** release a resource, transition
through a lifecycle, **or** encapsulate one replaceable technical adapter.

## Procedure

- give the class **or** object a specific, intention-revealing noun phrase that
   states the one state, invariant, resource, lifecycle, **or** adapter
   responsibility it owns; do **not** use an unqualified generic name such as
   `Manager`, `Helper`, **or** `Utils`.
- give each effectful method a specific verb phrase that declares the effect
   **or** lifecycle transition it performs.
- keep construction free of I/O **and** start acquisition **or** activation through
   an explicit method.
- make acquisition, use, failure, **and** release **or** recovery boundaries
   explicit.
- keep deterministic transformations outside the object **unless** they require
   its owned responsibility.
- compose the object from explicit collaborators instead of inheriting
   behavior for code reuse.
- use inheritance **only** for one stable, substitutable subtype contract; stop
   **when** a module, function, **or** composed adapter expresses the variation.

## Outcome

each object has one clearly named owner responsibility, a visible invariant **or**
lifecycle, explicit collaborators, **and** no unrelated function-grouping role.

## Failure or stop

stop **and** split **or** redesign the object **when** it owns unrelated state **or**
lifecycle concerns, hides an external effect, exists **only** as a namespace **or**
one-shot effect wrapper, **or** uses an ambiguous generic name **or** inheritance
**where** composition provides the same substitution boundary.

## Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [Python documentation: data classes](https://docs.python.org/3.14/library/dataclasses.html)
- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
