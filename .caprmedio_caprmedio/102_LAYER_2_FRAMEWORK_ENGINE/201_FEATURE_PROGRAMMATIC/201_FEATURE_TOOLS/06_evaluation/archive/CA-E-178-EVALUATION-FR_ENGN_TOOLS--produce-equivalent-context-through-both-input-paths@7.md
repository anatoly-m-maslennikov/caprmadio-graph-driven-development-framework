---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 7
updated_at: 2026-08-23 16:45:00 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-803
    - CA-R-804
    - CA-R-805
  check_of:
    - CA-D-006
---
# Produce equivalent context through both input paths

## Claim checked

Context gathered by a scheduled outbox consumer is equivalent to the standalone `COMMIT_CONTEXT` Finder result for the same durable trigger.

## Test case

For one fixed sealed trigger, capture the standalone Finder context. Independently enqueue the same trigger, let `COMMIT_CHANGE_SET` request the scheduled context in dry-run mode, and compare the resulting contexts after excluding only registered transport metadata.

## Acceptance criteria

Both contexts preserve the same Initiative, action identity, repository frontier, target, expected revisions or digests, and provenance bindings, and derive the same real-change message Projection. Neither acquires a Git lease, appends a Journal record, writes runtime state, stages a path, or creates a commit.

## Failure disposition

Reject the flow at the first divergent semantic context field or mutation.
