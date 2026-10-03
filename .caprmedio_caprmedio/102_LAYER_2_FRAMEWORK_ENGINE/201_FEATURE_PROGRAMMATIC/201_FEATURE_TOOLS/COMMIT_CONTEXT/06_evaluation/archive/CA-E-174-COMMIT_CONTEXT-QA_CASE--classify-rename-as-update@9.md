---
subjects:
  governs: "Governed Change/Change Class"
  depends_on: []
version: 9
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-804
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Classify rename as UPDATE

## Claim checked

A filename-only rename of one governed file identity without Structural relocation is classified only as `UPDATE`.

## Test case

Supply a trigger for one identity whose filename changes while content, Structural location, governed meaning, and version remain unchanged.

## Acceptance criteria

The sealed context reports `UPDATE`, records both filenames, preserves the version, and does not report `MOVE`.

## Failure disposition

Reject classification and report any identity split, version change, or competing change set.
