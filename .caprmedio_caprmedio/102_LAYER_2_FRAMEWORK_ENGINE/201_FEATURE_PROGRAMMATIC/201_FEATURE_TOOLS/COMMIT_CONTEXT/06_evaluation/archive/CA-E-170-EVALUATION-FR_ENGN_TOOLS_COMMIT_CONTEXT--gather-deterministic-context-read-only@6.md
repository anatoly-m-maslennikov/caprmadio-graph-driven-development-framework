---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 6
updated_at: 2026-08-20 23:52:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_TRIGGER--emit-only-operational-hook-triggers
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
  check_of:
    - CA-D-008-DELIVERY-FR_ENGN_TOOLS_COMMIT_CONTEXT--deliver-commit-context-script
---
# Gather deterministic context read-only

## Claim checked

The optional `COMMIT_CONTEXT` Finder returns complete deterministic context without mutating governed or Git state.

## Test case

Prepare one fixed `UPDATE` trigger with a fixed observation time and repository fixture, snapshot every Atom, Projection, runtime output, index entry, and Git reference, then invoke the Finder twice for each Codex resolver fixture: first with distinct valid `CODEX_THREAD_ID` and `CODEX_SESSION_ID` values and then with only `CODEX_SESSION_ID`.

## Acceptance criteria

Repeated envelopes for each fixture are byte-identical and contain the adapter and source-event provenance, one file identity, the `UPDATE` change set, before and after carriers, versions, digests, Git base, complete typed upstream relations, structured event, predicted sidecar record set, deterministic Git message Projection, lease availability, and validation results. The first fixture seals `llm_session.app: codex` with the thread UUID; the fallback fixture seals the session UUID; both seal the fixed timezone-qualified `occurred_at`, can derive `<app>:<uuid>:<occurred_at>`, and store no combined copy. Every Atom, Projection, and other snapshot remains unchanged and no apply lease is acquired.

## Failure disposition

Reject the Finder and identify the first missing, incorrectly prioritized, unstable, duplicated, or mutated provenance field or state.
