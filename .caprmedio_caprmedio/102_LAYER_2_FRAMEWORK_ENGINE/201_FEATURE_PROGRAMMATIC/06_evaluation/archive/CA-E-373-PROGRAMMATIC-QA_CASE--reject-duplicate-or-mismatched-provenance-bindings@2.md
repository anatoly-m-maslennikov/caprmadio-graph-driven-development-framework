---
atom_id: CA-E-373
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - provenance-binding
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-192
  derived_from:
    - CA-A-058
---
# Reject duplicate or mismatched provenance bindings

## Claim checked

One sealed action cannot become reconciled while duplicate canonical records,
duplicate real-change commits, or revision or digest mismatches remain.

## Test case

Provide one sealed action with two Journal records that both claim canonical
binding to the same real-change commit.

## Acceptance criteria

Pass only when reconciliation detects the duplicate, returns an explicit
blocked state, and does not select one record by guesswork.

## Failure disposition

Preserve the discrepancy and block provenance reliance until deterministic
repair establishes one binding.

## Sources

- [CA-M-192 — Reconcile independent Git and Journal provenance](../05_method/CA-M-192-PROGRAMMATIC-METHOD--reconcile-independent-git-and-journal-provenance.md)
