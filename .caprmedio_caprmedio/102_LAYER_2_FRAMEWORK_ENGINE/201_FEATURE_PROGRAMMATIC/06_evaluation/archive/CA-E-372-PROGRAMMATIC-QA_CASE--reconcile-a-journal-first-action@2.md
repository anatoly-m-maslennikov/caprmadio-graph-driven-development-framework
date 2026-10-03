---
atom_id: CA-E-372
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - provenance
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
# Reconcile a Journal-first action

## Claim checked

One action whose canonical Journal record is prepared before its real-change
Git commit becomes reconciled after the exact reachable commit SHA is known.

## Test case

Prepare one canonical Journal record for a sealed action, complete one
real-change commit, bind the record to that exact reachable commit, and commit
the Journal carrier later.

## Acceptance criteria

Pass only when the action advances from `journal_recorded_git_pending` to
`reconciled` with exactly one record and one reachable real-change commit.

## Failure disposition

Preserve the pending state and reject provenance reliance until binding is
complete.

## Sources

- [CA-M-192 — Reconcile independent Git and Journal provenance](../05_method/CA-M-192-PROGRAMMATIC-METHOD--reconcile-independent-git-and-journal-provenance.md)
