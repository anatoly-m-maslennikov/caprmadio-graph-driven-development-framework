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
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify reconcile independent git and journal provenance

## Claim checked

one action whose real-change Git commit completes **before** its Journal record
converges **to** one canonical reconciled cross-system binding.

## Applicable conditions

apply **when** a sealed action is **in** `git_complete_journal_pending`.

## Test case

create one reachable real-change commit for a sealed action, append exactly one
canonical Journal record bound **to** that commit, **then** commit the Journal carrier
**in** a later separate Git commit.

## Acceptance criteria

pass **only** **when** the action becomes `reconciled`, exactly one canonical Journal
record binds exactly one reachable real-change commit, **and** the Journal record
does **not** embed the SHA of the commit containing that same record.

## Failure disposition

keep the action pending **or** blocked, preserve its sealed state, **and** reject later
provenance reliance **until** reconciliation succeeds.

## Sources

- [CA-M-192 — Reconcile independent Git and Journal provenance](../05_method/CA-M-192-PROGRAMMATIC-METHOD--reconcile-independent-git-and-journal-provenance.md)
