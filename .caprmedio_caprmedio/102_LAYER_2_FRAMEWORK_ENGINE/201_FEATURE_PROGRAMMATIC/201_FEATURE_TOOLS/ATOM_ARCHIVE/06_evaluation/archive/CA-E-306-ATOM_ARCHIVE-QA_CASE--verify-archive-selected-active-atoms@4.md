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
    - CA-M-188
---
# Verify archive selected active atoms

## Claim checked

CA-M-188 removes selected active Atoms from current authority while preserving byte-identical historical carriers and resolvability.

## Applicable when

Apply to any realization of CA-M-188 before it can perform active-to-archive lifecycle transitions.

## Test case

Use one fixture with one active Atom selected singly, two active Atoms selected as a bulk set, one draft, and one existing historical reference to a bulk source. Record dry-runs, attempt delegated apply without authority, submit a mixed bulk request containing the two active Atoms and the draft, then archive the single and bulk active targets through sealed Initiative envelopes.

## Acceptance criteria

The unauthorized and mixed-lifecycle requests change nothing; valid singular and bulk applies place every selected active Atom in its owning Content-role archive with identical filenames, IDs, revisions, and bytes; current discovery excludes them; the draft remains a draft; and historical resolution still finds the archived bulk source and its existing historical reference.

## Failure disposition

Reject the realization and preserve lifecycle classifications, authority result, archive map, current-authority result, digest comparison, and historical-reference evidence.
