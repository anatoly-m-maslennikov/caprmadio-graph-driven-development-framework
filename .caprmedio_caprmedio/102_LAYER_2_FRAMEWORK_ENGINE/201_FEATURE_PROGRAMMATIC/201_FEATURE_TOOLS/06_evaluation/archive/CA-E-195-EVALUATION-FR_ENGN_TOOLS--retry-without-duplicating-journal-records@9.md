---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 9
updated_at: 2026-08-21 00:03:00
relations:
  evaluation_for:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
---
# Retry without duplicating Journal records

## Claim checked

A partial Journal append or later commit failure can be retried under the same repository lease with the same event identities, LLM-session provenance, occurrence time, and payload digests without duplicating or redefining any record.

## Test case

Use one sealed context with multiple related records. Interrupt after a proper subset is appended, change the process clock and detectable host session UUID, and retry the same event identities and payload digests. Then attempt one accepted event identity with different `llm_session` or `occurred_at` payload data. After the complete receipt set is returned, force Git commit creation to fail, attempt to advance a different action for the repository, and finally resume the original context.

## Acceptance criteria

The Journal contains exactly one copy of every sealed record identity; an identical retry preserves the originally sealed `llm_session` and `occurred_at`, reuses existing receipts, and appends only missing records despite the changed host context; the divergent payload fails before mutation with a stable identity-collision diagnostic. Git failure leaves one visible recoverable blocked action whose runtime state contains only Journal-resolvable action, event, receipt, and lease references, not copied LLM-session or occurrence-time values; the different action waits; and resuming the original context creates exactly one final commit with all related sidecar lines before releasing the lease.

## Failure disposition

Reject the flow if retry duplicates or redefines a record, refreshes or copies LLM-session or occurrence-time provenance outside the Journal, changes a partition, loses an existing receipt, silently loses or bypasses the lease, lets another action mutate the repository, omits a related sidecar line, or creates more than one successful commit.
