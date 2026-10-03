---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - extension-packaging
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-218
---
# Verify resolve GitHub Extension source

## Claim checked

CA-M-218 resolves the declared GitHub repository and package-root boundary for one Extension without choosing an installed state.

## Applicable when

Apply whenever GitHub Extension source-boundary resolution changes.

## Test case

Resolve one Extension whose package root is a declared repository subdirectory, then resolve another whose package root is the complete repository. Repeat with an undeclared subdirectory.

## Acceptance criteria

Each valid case reports the declared GitHub repository and its exact complete-repository or declared-directory package root. The undeclared-subdirectory case produces an explicit failure and no alternative source boundary.

## Failure disposition

Reject the realization and preserve source declarations, resolved boundaries, undeclared-subdirectory finding, and proof that installed Extension state was unchanged.
