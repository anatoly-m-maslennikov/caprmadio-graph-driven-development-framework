---
subjects:
  governs: "Governed Change/Change Class"
  depends_on: []
version: 8
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-804
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Classify file creation as ADD

## Claim checked

Creation of one governed file identity is classified only as `ADD`.

## Test case

Supply a trigger whose resulting staged graph contains one new governed file with no matching identity in the committed graph.

## Acceptance criteria

The sealed context reports `ADD`, names the resulting filename and version, and resolves upstream relations from the resulting staged graph.

## Failure disposition

Reject classification and report the observed competing or missing change set.
