---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 7
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805
  check_of:
    - CA-D-010
---
# Keep dry-run mutation-free

## Claim checked

`COMMIT_CHANGE_SET` dry run returns the predicted real-change gate result without changing repository or provenance state.

## Test case

Snapshot governed files, outbox state, Journal carriers, runtime outputs, lease state, index entries, refs, and object reachability for one valid sealed action. Invoke the gate in dry-run mode and repeat every snapshot.

## Acceptance criteria

The result names the exact Initiative, action identity, atomic or frozen bulk target set, expected Git base, message Projection, gate eligibility, and revalidation result. It may identify Journal preparation eligibility but does not predict or create a Journal batch. Every captured state remains unchanged, no lease is acquired, and no new reachable commit exists.

## Failure disposition

Reject the Doer and report the first missing prediction or mutation.
