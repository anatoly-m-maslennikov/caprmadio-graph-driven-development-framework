---
atom_id: CA-M-159
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - technical-interface
  depends_on:
    continuant:
      - programmatic software
version: 3
updated_at: 2026-09-01 01:33:45 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Define typed contracts at replaceable technical boundaries

Declare an explicit typed contract wherever a PROGRAMMATIC component depends on
a replaceable technical implementation, adapter, transport, storage mechanism,
or host boundary.

## Applicable when

Apply when a Tool, App backend service, or MCP component can substitute one
technical implementation for another or crosses a host-owned interface.

## Procedure

1. Define the accepted inputs, outcomes, failure values, ownership boundary,
   and compatibility expectation at the interface.
2. Keep callers dependent on that contract rather than on implementation-only
   state or incidental representation.
3. Use a structural `Protocol` when consumers need one capability contract
   without requiring implementations to inherit from a framework base class.
4. Keep substrate-specific behavior in a small adapter and keep deterministic
   semantic decisions outside that adapter.
5. Record an exception in its bounded owner when a required external interface
   cannot meet the contract directly.

## Outcome

The component can replace the bounded technical implementation without
silently changing its callers' declared expectations.

## Failure or stop

Stop substitution or host integration when the boundary has no explicit
contract, its failures cannot be represented, or compatibility cannot be
identified from current authority.

## Sources

- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [Python documentation: `typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
