---
atom_id: CA-E-253
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - technical-contract
  depends_on:
    continuant:
      - programmatic software
version: 4
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-110
  derived_from:
    - CA-A-053
---
# Verify changed component technical-contract conformance

## Claim checked

One changed PROGRAMMATIC Tool, App backend service, or MCP component conforms
to the Python, runtime, and dependency selections owned by accepted Methods,
as materialized in current configuration and Implementation.

## Applicable conditions

Apply when such a component is added or materially changed and no bounded
technical-contract exception is proposed.

## Test case

Evaluate one changed component against the applicable Method-owned selections
and compare its configuration and Implementation carriers with those
selections.

## Acceptance criteria

Pass only when the component conforms to every applicable Method-owned
selection, its materializations agree, and no configuration, Implementation,
or Delivery carrier claims independent selection authority.

## Failure disposition

Reject admission or release of the component until it conforms or enters the
separate bounded-exception evaluation.

## Sources

- [CA-M-110 — Implement PROGRAMMATIC components in Python](../05_method/CA-M-110-PROGRAMMATIC-CORE-IMPL_METHOD--implement-programmatic-components-in-python.md)
