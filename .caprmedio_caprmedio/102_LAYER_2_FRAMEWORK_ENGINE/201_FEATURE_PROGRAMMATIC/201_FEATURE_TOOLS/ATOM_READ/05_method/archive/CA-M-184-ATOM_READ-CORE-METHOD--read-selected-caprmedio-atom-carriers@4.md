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
    - CA-R-864
  derived_from:
    - CA-A-058
---
# Read selected CAPRMEDIO Atom carriers

## Applicable when

Use this Method when a caller needs the current content, metadata, or both for one or more explicitly selected Atom carriers.

## Procedure

1. Resolve the configured control root and normalize each selector as one exact repository-relative path, full filename, filename stem, or stable Atom ID together with the requested output view.
2. Resolve every selector independently and require at most one current Atom carrier per selector; retain missing and ambiguous outcomes as explicit, attributable results.
3. Read each resolved carrier once without rewriting it, preserving its raw frontmatter and body as read.
4. Derive identity, Content role, Scope Unit, placement, and lifecycle facts from the current filename and location rather than inventing them from the request.
5. Return content only, metadata only, or both exactly as requested, preserving selector-to-result attribution for singular and bulk requests.
6. Perform no mutation, normalization, repair, or selector widening.

## Outcome

Each selector has one attributable result containing the requested current carrier view or one explicit resolution error.

## Failure or stop

Do not guess when a selector is missing, ambiguous, unreadable, or outside the control root; return the exact condition without exposing another carrier.
