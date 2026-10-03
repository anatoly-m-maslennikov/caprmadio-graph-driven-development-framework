---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 7
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---
# Record successor IDs while archiving predecessor

## Claim checked

Archiving a replaced predecessor records the explicit predecessor and already active successor Atom IDs only in the authoritative Work Journal event. Formal replacement relations are deferred.

## Test case

Prepare an active successor at version 1 and an active predecessor at version 4, both at global tier `N`, then gather and apply one `MOVE` that preserves the predecessor's content, filename, frontmatter, and version while moving it into `archive/`. Seal the explicit predecessor and successor IDs in that archival Work Journal event.

## Acceptance criteria

The resulting one-file commit event records the predecessor path transition as version 4 to version 4 and stores only explicit predecessor and successor Atom IDs in the archival Work Journal event. It stores no replacement relation in either Atom frontmatter or Journal payload and creates no inverse navigation view.

## Failure disposition

Reject the flow if the explicit predecessor or successor IDs are absent; if a formal replacement relation is authored or inferred; if the successor was not active first; if the predecessor remains active; if either Atom carrier stores replacement history; or if the archival `MOVE` changes the predecessor version.
