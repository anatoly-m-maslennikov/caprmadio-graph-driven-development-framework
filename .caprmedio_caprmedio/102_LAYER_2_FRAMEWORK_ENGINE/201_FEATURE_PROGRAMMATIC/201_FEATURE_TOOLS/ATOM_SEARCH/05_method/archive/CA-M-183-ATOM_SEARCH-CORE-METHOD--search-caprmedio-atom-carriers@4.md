---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 4
updated_at: 2026-09-02 01:10:00 +0400
relations:
  method_for:
    - CA-R-863
  derived_from:
    - CA-A-058
---
# Search CAPRMEDIO Atom carriers

## Applicable when

Use this Method when an operator or another Tool needs a deterministic, read-only set of Atom carriers within a declared search frontier.

## Procedure

1. Resolve the configured CAPRMEDIO control root, one declared subtree boundary, the requested output view, and any exact selector, lifecycle, path, filename, frontmatter, or body-text filters.
2. Reject an invalid root, selector, filter, lifecycle, or output-view request before traversing the frontier.
3. Enumerate only Markdown candidates inside the frontier, classify Atom eligibility from their current locations and filenames, and exclude runtime state, projections, and non-Atom files.
4. Apply the exact selector and every supplied filter conjunctively; retain a separate diagnostic for each malformed or unreadable candidate.
5. Read only the filename, frontmatter, and body fields needed for the requested metadata-only, content-only, or combined result.
6. Return an empty, singular, or bulk result in stable repository-relative path order, with one attributable result record per matching Atom.
7. Perform no write, rename, move, lifecycle transition, repair, or projection rebuild.

## Outcome

A reproducible, read-only result set identifies every and only matching Atom carrier within the declared search frontier.

## Failure or stop

Stop without mutation when the root or request grammar is invalid. Report malformed candidates separately from valid non-matches and never infer a match from an unreadable carrier.
