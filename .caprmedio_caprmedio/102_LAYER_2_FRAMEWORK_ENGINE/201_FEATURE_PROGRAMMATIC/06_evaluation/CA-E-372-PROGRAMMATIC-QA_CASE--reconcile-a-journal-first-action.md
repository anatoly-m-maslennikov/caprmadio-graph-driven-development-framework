---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "provenance"
  depends_on:
    - "programmatic software"
version: 8
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-192
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reconcile a Journal-first action

## Claim checked

one action whose canonical Journal record is prepared **before** its real-change
Git commit becomes reconciled **after** the exact reachable commit SHA is known.

## Test case

prepare one canonical Journal record for a sealed action, complete one
real-change commit, bind the record **to** that exact reachable commit, **and** commit
the Journal carrier later.

## Acceptance criteria

pass **only** **when** the action advances from `journal_recorded_git_pending` **to**
`reconciled` with **=1** record **and** one reachable real-change commit.

## Failure disposition

preserve the pending state **and** reject provenance reliance **until** binding is
complete.

## Sources

- [CA-M-192 — Reconcile independent Git and Journal provenance](../05_method/CA-M-192-PROGRAMMATIC-METHOD--reconcile-independent-git-and-journal-provenance.md)
