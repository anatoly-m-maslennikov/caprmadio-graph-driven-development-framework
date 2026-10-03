---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 6
updated_at: 2026-08-20 23:54:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_TRIGGER--emit-only-operational-hook-triggers
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
  check_of:
    - CA-D-006-DELIVERY-FR_ENGN_TOOLS--deliver-project-local-commit-automation
---
# Produce equivalent context through both input paths

## Claim checked

Passing a Hook trigger directly to the Doer invokes the same context-gathering behavior as the standalone Finder.

## Test case

For one fixed `UPDATE` fixture and one trigger with fixed adapter, source-event, trigger, repository, LLM application, host session UUID, and observation-time values, capture the sealed context returned by `COMMIT_CONTEXT`, then pass the same trigger directly to `COMMIT_CHANGE_SET` in dry-run mode and capture its resolved context.

## Acceptance criteria

The two contexts are byte-identical after excluding only registered non-semantic transport metadata. Both preserve the same adapter provenance, structured `llm_session`, sealed `occurred_at`, and stable action and Journal event identities; both derive the same `<app>:<uuid>:<occurred_at>` presentation without storing it; both report the same predicted lease availability; and neither acquires a lease nor mutates an Atom, Projection, Journal, runtime state, index, or Git reference.

## Failure disposition

Reject the flow and report the first divergent semantic or session-provenance field, acquired lease, or repository mutation.
