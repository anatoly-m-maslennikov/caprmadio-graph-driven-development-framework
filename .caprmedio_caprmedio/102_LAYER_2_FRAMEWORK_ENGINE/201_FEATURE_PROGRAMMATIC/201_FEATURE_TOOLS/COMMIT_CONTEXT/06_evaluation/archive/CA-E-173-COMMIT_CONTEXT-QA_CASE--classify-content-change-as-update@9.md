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
# Classify content change as UPDATE

## Claim checked

A content change to one governed file identity without Structural relocation is classified only as `UPDATE`.

## Test case

Supply a trigger for one identity whose governed content and resulting version change while its filename and Structural location remain unchanged.

## Acceptance criteria

The sealed context reports `UPDATE`, names the resulting version, and resolves upstream relations from the resulting staged graph.

## Failure disposition

Reject classification and report any added `MOVE` flag, preserved old version, or incorrect relation source.
