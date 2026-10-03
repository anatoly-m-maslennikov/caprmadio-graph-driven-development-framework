---
subjects:
  governs: "Governed Change/Git Commit Creation"
  depends_on: []
version: 18
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
# Commit one governed change independently from a Journal batch

## Claim checked

one sealed real-change action creates exactly one Initiative-named Git commit for its governed target, while its canonical Journal record **and** **any** Journal-only batch commit remain independent evidence.

## Test case

prepare one valid `UPDATE` action with a sealed Initiative, an unrelated unstaged change, **and** an independently prepared Journal record. run the real-change gate, **then** run a later Journal batch **and** reconciliation. inspect the two commit trees, Journal record, outbox state, **and** returned envelopes.

## Acceptance criteria

the real-change commit **contains** **all** **and** **only** the resolved action target changes, no Journal carrier change, **and** the exact Initiative-based message. the unrelated change remains untouched. the Journal-only batch **contains** **only** selected Journal carrier changes **and** has the distinct batch message. reconciliation binds the same action **to** both evidence streams **without** duplicate record **or** commit.

## Failure disposition

reject the flow at the first extra commit, mixed commit class, missing action binding, message difference, duplicate Journal record, **or** unintended working-tree effect.
