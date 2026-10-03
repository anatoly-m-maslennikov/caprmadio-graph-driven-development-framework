---
atom_id: CA-E-232
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-804
  check_of:
    - CA-D-008
---
# Log a file change despite graph defects

## Claim checked

`COMMIT_CONTEXT` records one valid file action without requiring the surrounding Artifact graph or the changed carrier's authored relations to be valid.

## Test case

Prepare one changed active Atom, two unrelated active carriers with the same Atom identity, and a changed-carrier relation whose stated target version differs from the observable target version; then gather commit context.

## Acceptance criteria

Context gathering succeeds with the correct file action. The unrelated identity collision does not affect the subject. The observable relation target is included with its observable filename and version, while the stated-version difference is exposed as a non-blocking diagnostic. The Finder performs no governed, Journal, index, or Git mutation.

## Failure disposition

Reject the logger if it blocks the file action, silently invents graph correctness, mutates project state, or omits the available relation diagnostic.
