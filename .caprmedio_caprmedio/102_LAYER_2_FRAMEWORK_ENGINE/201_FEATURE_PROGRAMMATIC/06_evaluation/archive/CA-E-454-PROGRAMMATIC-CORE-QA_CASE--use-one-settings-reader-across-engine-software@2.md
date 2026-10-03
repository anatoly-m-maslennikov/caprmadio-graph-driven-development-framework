---
atom_id: CA-E-454
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - engine-settings-reader
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: "2026-09-11 20:58:34 +0400"
relations:
  evaluation_for:
    - CA-M-284
  derived_from:
    - CA-A-053
---
# Use one Settings Reader across Engine software

## Claim checked

Representative Tool, App, and MCP consumers use one immutable, validated,
versioned settings snapshot.

## Test case

Replace the shared Reader with a recording fake and execute one representative
consumer from each PROGRAMMATIC child feature.

## Acceptance criteria

Pass only when each consumer reads exactly once through the fake, receives the
same carrier and digest provenance, and performs no direct read, fallback,
private default selection, or mutation.

## Failure disposition

Reject the bypassing consumer until it accepts the shared snapshot explicitly.

## Sources

- [Python documentation: `unittest.mock`](https://docs.python.org/3.14/library/unittest.mock.html)
- [CA-M-284 — Read Engine settings through one shared boundary](../05_method/CA-M-284-PROGRAMMATIC-CORE-METHOD--read-engine-settings-through-one-shared-boundary.md)
