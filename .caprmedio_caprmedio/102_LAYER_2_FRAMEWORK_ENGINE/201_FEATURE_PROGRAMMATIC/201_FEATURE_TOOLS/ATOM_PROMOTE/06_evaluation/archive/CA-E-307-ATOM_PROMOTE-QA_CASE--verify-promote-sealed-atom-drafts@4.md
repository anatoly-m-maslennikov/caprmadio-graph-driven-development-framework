---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 01:10:00 +0400
relations:
  evaluation_for:
    - CA-M-189
---
# Verify promote sealed atom drafts

## Claim checked

CA-M-189 promotes each accepted draft to exactly one byte-identical active Atom with the assigned stable role-matching ID.

## Applicable when

Apply to any realization of CA-M-189 before it can admit draft authority into the active graph.

## Test case

Use one fixture with one valid draft selected singly and two valid drafts selected as a frozen bulk set. Assign the bulk set one valid ID and one ID whose role token conflicts with its draft; record dry-runs, attempt delegated apply without authority, attempt the invalid bulk promotion, then assign a valid role-matching ID, reseal the corrected bulk request, and apply the single and bulk promotions through sealed Initiative envelopes.

## Acceptance criteria

The unauthorized and mismatched requests promote no draft; valid singular and bulk promotions create exactly one canonical active carrier per source, remove the source draft carriers, preserve each source carrier's full byte digest, assign unique stable role-matching IDs, and derive canonical filenames and active locations.

## Failure disposition

Reject the realization and preserve source digests, draft identities, assigned IDs, promotion maps, authority result, final lifecycle locations, and any duplicate or partial active identity.
