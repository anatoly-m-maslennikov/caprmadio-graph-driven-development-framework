---
subjects:
  governs: "Governed Change/Git Commit Class Boundary"
  depends_on: []
version: 11
updated_at: "2026-09-12 04:12:43 +0400"
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805
    - CA-R-812
    - CA-D-417
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Keep real-change commits separate from Journal batches

## Claim checked

the Git gate keeps each real-change action **and** each Journal-only batch as distinct commit classes.

## Test case

Prepare one real-change action with a completed Journal record **and** one unrelated completed Journal record. Apply the real-change gate, **then** batch both Journal records. Inspect both commit trees **and** the outbox/reconciliation bindings.

## Acceptance criteria

the real-change commit **contains** **all** **and** **only** the sealed governed target set **and** the Initiative-based message. The later Journal-only batch **contains** **only** the selected Journal carriers **and** the distinct batch message. Neither commit includes the other class's changes, **and** each Journal record remains attributable **to** its action.

## Failure disposition

Reject the gate at the first mixed commit class, included unrelated target, missing selected Journal record, **or** incorrect message form.
