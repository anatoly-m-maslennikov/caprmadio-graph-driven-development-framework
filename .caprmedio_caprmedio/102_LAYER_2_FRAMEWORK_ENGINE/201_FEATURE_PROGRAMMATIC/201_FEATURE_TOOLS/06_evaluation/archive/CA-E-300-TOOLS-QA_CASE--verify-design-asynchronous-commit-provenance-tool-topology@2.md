---
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-25 01:49:10 +0400
relations:
  evaluation_for:
    - CA-M-182
---
# Verify asynchronous commit-provenance architecture

## Claim checked

CA-M-182 realizes CA-R-802 through one pure decision manager, one mechanical recoverable Scheduler, atomic non-deciding workers, durable state, and one serialized Git boundary.

## Test case

Inspect the exact source frontier and run a controlled plan whose ready worker succeeds, whose completion is delivered twice, whose service stops before the next dispatch, and whose fixture attempts one undeclared transition and one second concurrent Git claim.

## Acceptance criteria

The manager performs no I/O and returns the same typed plan for equal inputs. Only declared steps become ready. Repeated completion is idempotent. Restart resumes the persisted plan. The undeclared transition and second Git claim are rejected without mutation. No worker selects downstream work, and COMMIT_CHANGE_SET neither imports nor invokes a peer Tool.

## Failure disposition

Reject the realization and preserve the first impurity, discretionary worker decision, undeclared transition, lost state, duplicate effect, peer orchestration, or concurrent Git mutation as a blocked architecture discrepancy.
