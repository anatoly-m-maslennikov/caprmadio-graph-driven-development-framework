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
    - CA-M-185
---
# Verify create sealed caprmedio atom carriers

## Claim checked

CA-M-185 admits one Atom or a frozen bulk set atomically only after complete validation and delegated apply authority.

## Applicable when

Apply to any realization of CA-M-185 before it can create governed Atom carriers.

## Test case

Use one fixture containing a valid single-Atom request and a frozen two-Atom request with valid role placement and unique IDs. Record dry-runs, attempt apply without delegated authority, introduce a collision at the second bulk destination and attempt delegated apply, then remove that collision and apply the unchanged single and bulk requests through sealed Initiative envelopes.

## Acceptance criteria

Dry-runs and the unauthorized apply create nothing; the colliding bulk set creates neither Atom; authorized valid applies create the single carrier and both bulk carriers exactly once as canonical first revisions with complete metadata; no target, filename, or stable ID collides; and no temporary or partial carrier remains.

## Failure disposition

Reject the realization and preserve the sealed envelopes, authority result, collision evidence, dry-runs, resulting directory state, and any partial-write residue.
