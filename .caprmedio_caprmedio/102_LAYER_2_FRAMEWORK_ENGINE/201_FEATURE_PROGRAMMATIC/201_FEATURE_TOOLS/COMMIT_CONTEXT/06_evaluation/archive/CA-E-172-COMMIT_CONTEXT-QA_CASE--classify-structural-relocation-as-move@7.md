---
subjects:
  governs:
    continuant:
      - Governed Change/Change Class
version: 7
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-804
---
# Classify structural relocation as MOVE

## Claim checked

Relocation of one unchanged governed file identity to a different Structural location is classified only as `MOVE`.

## Test case

Supply a trigger for one identity whose directory changes while filename, content, governed carrier state, and version remain unchanged.

## Acceptance criteria

The sealed context reports `MOVE`, preserves the version, records both repository-relative paths, and resolves upstream relations from the unchanged Artifact graph.

## Failure disposition

Reject classification and report any added `UPDATE` flag, version change, or incorrect relation source.
