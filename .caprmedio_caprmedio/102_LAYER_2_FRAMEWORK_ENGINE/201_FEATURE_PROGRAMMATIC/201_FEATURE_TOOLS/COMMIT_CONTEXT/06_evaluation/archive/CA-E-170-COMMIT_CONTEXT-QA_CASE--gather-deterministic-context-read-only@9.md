---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 9
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-803
    - CA-R-804

---
# Gather deterministic context read-only

## Claim checked

`COMMIT_CONTEXT` gathers a deterministic provisional context from one durable trigger without mutating governed or Git state.

## Test case

Prepare one fixed sealed trigger with a fixed Initiative, action identity, expected frontier, observation time, and repository fixture. Snapshot every Atom, Projection, Journal, runtime output, index entry, and Git reference. Invoke the Finder twice for the same trigger and once after changing only non-semantic transport metadata.

## Acceptance criteria

The two equivalent contexts are byte-identical after excluding registered non-semantic transport metadata. Each contains the sealed Initiative and action identity, resolved target, expected and observed revisions or digests, Git and Journal state, and revalidation inputs; it has no lease, Journal record, staged path, commit prediction, or mutable receipt. The changed transport metadata does not alter the context identity. Every snapshot remains unchanged.

## Failure disposition

Reject the Finder and identify the first missing, unstable, or mutable context fact.
