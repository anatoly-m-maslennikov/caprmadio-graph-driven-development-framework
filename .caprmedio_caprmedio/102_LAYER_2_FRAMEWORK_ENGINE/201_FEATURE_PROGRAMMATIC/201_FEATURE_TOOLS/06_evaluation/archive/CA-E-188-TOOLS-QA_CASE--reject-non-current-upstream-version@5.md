---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
---
# Reject non-current upstream version

## Claim checked

The commit flow cannot seal or apply a typed upstream relation whose target version is not current immediately before the file change.

## Test case

Prepare one `UPDATE` fixture whose direct upstream target is at version 3, then supply a candidate context that names version 2 for that same target.

## Acceptance criteria

The flow returns a deterministic non-current-upstream-version diagnostic, names both versions, and creates no governed or Git state change.

## Failure disposition

Reject the flow if it accepts, silently rewrites, or omits the stale target reference.
