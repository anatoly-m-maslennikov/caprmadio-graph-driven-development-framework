---
atom_id: CA-E-272
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - compatibility-boundary
  depends_on:
    continuant:
      - programmatic software
version: 4
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-166
  derived_from:
    - CA-A-053
---
# Verify declared interface compatibility

## Claim checked

One changed declared PROGRAMMATIC public or host interface preserves its
accepted compatibility behavior or has an accepted bounded replacement.

## Applicable conditions

Apply when a Tool, App backend service, or MCP component changes a declared
technical interface, host integration, transport, or dependency-facing
boundary. A component without such a declared boundary is not applicable.

## Test case

Invoke one changed declared boundary through the behavior accepted by its
current Requirement, technical contract, or pinned external origin.

## Acceptance criteria

Pass only when the invocation preserves the declared behavior or returns the
accepted replacement behavior, without implying an undeclared platform or
cross-host compatibility claim.

## Failure disposition

Stop release and compatibility claims until the boundary has current authority
or an accepted replacement.

## Sources

- [CA-M-166 — Preserve declared interface compatibility boundaries](../05_method/CA-M-166-PROGRAMMATIC-CORE-METHOD--preserve-declared-interface-compatibility-boundaries.md)
