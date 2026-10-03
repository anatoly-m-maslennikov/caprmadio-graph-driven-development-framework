---
atom_id: CA-E-263
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - file-mutation-recovery
  depends_on:
    continuant:
      - programmatic software
version: 4
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-161
  derived_from:
    - CA-A-053
---
# Recover one partial file write

## Claim checked

One interrupted PROGRAMMATIC file replacement preserves or explicitly reports
its declared recovery boundary without guessing at a completed result.

## Applicable conditions

Apply when a component writes replacement content through a temporary carrier
or otherwise has a declared partial-write recovery boundary.

## Test case

Interrupt one replacement after its temporary carrier is prepared but before
the declared replacement completes.

## Acceptance criteria

Pass only when the original target or a declared recoverable result remains
identifiable, no false completion is reported, and the partial state is
diagnosable from the returned context.

## Failure disposition

Stop the mutation path until its weaker recovery boundary is explicit or its
atomic replacement guarantee is restored.

## Sources

- [CA-M-161 — Bound file and subprocess effects](../05_method/CA-M-161-PROGRAMMATIC-CORE-METHOD--bound-file-and-subprocess-effects.md)
