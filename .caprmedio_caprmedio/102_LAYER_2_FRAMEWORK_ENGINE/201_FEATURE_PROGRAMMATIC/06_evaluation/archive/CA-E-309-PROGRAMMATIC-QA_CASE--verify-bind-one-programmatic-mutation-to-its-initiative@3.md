---
atom_id: CA-E-309
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - programmatic-mutation
  depends_on:
    continuant:
      - programmatic software
version: 3
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-191
---
# Verify bind one programmatic mutation to its initiative

## Claim checked

One accepted programmatic mutation preserves exactly one sealed Initiative and
one stable action identity through asynchronous handoffs and retry.

## Applicable conditions

Apply when one accepted human instruction causes a programmatic mutation that
passes through a queue or worker boundary.

## Test case

Create one sealed Initiative and action identity, dispatch the mutation through
one queue and worker, force one retry, and observe every handoff plus the final
mutation receipt.

## Acceptance criteria

Pass only when every handoff and the final receipt retain the same Initiative
and action identities, while process, queue, worker, and retry identities remain
linked execution context and never replace them.

## Failure disposition

Reject the mutation provenance and return the identity propagation boundary to
its owner before later reliance.

## Sources

- [CA-M-191 — Bind one programmatic mutation to its Initiative](../05_method/CA-M-191-PROGRAMMATIC-METHOD--bind-one-programmatic-mutation-to-its-initiative.md)
