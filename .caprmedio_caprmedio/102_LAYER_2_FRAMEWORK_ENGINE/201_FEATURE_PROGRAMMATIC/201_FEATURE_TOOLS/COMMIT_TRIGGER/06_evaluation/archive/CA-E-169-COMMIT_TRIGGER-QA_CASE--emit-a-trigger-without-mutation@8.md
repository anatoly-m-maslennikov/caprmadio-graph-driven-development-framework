---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 8
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-803

---
# Emit a trigger without mutation

## Claim checked

The operational Hook coalesces one adapter-defined logical change into one stable minimal `COMMIT_TRIGGER` and performs no classification, graph traversal, or mutation.

## Test case

Snapshot the working tree, index, Journals, runtime files, and Git history; configure one registered LLM application and host session UUID; deliver three noisy observations with the same adapter and source-event identities for one registered logical file-change boundary; capture every Hook output; and compare every snapshot after the Hook returns.

## Acceptance criteria

Exactly one schema-valid trigger identifies the adapter, source event, repository, stable trigger identity, observation time, observed before-path and after-path candidates, and one structured LLM-session candidate containing the configured application and UUID without a concatenated timestamped copy. Replaying the observations yields that same identity and candidate; every captured state remains byte-identical; and no change set has been classified.

## Failure disposition

Reject the Hook delivery and report the first duplicate or unstable trigger, missing or duplicated LLM-session field, classification, traversal, or mutation observed.
