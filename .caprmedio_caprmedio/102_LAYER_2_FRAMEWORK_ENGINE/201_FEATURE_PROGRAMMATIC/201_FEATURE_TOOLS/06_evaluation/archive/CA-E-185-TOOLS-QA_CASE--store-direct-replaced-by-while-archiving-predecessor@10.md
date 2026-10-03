---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 10
updated_at: 2026-09-01 02:45:00 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805
    - CA-R-807
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

## Sources

- [CA-R-807 — Record replacement transitions in the Journal](../../../../../.caprmedio_framework/00_APPLICABLE_METHODOLOGY/04_requirement/CA-R-807-REQUIREMENT-BSEED_GOVERNANCE--record-replacement-transitions-in-the-journal.md)
- [CA-M-087 — Process one file change](../05_method/CA-M-087-TOOLS-CORE-IMPL_METHOD--process-one-file-change.md)
