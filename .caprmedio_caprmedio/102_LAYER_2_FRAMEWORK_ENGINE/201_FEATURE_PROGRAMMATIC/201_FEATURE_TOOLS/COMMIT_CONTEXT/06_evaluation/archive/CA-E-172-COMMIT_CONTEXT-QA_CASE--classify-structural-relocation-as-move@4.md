---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 4
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
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
