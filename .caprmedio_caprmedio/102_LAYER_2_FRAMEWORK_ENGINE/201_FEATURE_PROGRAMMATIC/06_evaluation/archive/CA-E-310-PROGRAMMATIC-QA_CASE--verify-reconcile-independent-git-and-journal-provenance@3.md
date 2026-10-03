---
atom_id: CA-E-310
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - provenance
  depends_on:
    continuant:
      - programmatic software
version: 3
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-192
---
# Verify reconcile independent git and journal provenance

## Claim checked

One action whose real-change Git commit completes before its Journal record
converges to one canonical reconciled cross-system binding.

## Applicable conditions

Apply when a sealed action is in `git_complete_journal_pending`.

## Test case

Create one reachable real-change commit for a sealed action, append exactly one
canonical Journal record bound to that commit, then commit the Journal carrier
in a later separate Git commit.

## Acceptance criteria

Pass only when the action becomes `reconciled`, exactly one canonical Journal
record binds exactly one reachable real-change commit, and the Journal record
does not embed the SHA of the commit containing that same record.

## Failure disposition

Keep the action pending or blocked, preserve its sealed state, and reject later
provenance reliance until reconciliation succeeds.

## Sources

- [CA-M-192 — Reconcile independent Git and Journal provenance](../05_method/CA-M-192-PROGRAMMATIC-METHOD--reconcile-independent-git-and-journal-provenance.md)
