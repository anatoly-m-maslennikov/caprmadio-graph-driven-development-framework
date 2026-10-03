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
    - CA-M-184
---
# Verify read selected caprmedio atom carriers

## Claim checked

CA-M-184 resolves each exact Atom selector independently and returns only the requested faithful carrier view without mutation.

## Applicable when

Apply to any realization of CA-M-184 before it is relied on as the canonical Atom reader.

## Test case

Use a fixture with two valid Atoms. Address the first separately by exact path, full filename, filename stem, and stable ID; submit a bulk request that selects both Atoms; and include one missing selector and one deliberately ambiguous stem. Request content-only, metadata-only, and combined views while recording source bytes.

## Acceptance criteria

All four selectors for the first Atom resolve to that same carrier; the bulk request returns both and preserves selector-to-result attribution; returned content equals each body; metadata contains raw frontmatter plus correct derived identity, placement, Content-role, Scope Unit, and lifecycle facts; missing and ambiguous selectors remain explicit; and source bytes do not change.

## Failure disposition

Reject the realization and preserve each selector, its observed resolution, returned fields, bulk attribution, and source-byte comparison.
