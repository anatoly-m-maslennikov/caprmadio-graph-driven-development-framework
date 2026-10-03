---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Work Journal/Append"
  depends_on: []
version: 14
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805
    - CA-R-812
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Append all related Journal records independently of commit timing

## Claim checked

The Journal Doer completes every related append independently of real-change commit timing and without using the repository Git gate for the append itself.

## Test case

Start two valid actions for the same repository whose related records span disjoint and shared Journal carriers. In separate runs, complete Journal append before, during, and after the corresponding real-change commit; then commit the completed records in a later Journal-only batch.

## Acceptance criteria

Disjoint Journal partitions may append concurrently. Each shared carrier has one canonical writer or batcher, every accepted record is durable and idempotent, and no Journal append acquires the repository Git gate. Real-change commits do not wait for Journal receipts. The later Journal-only commit contains all and only its selected Journal Carriers and shares the single fenced commit gate.

## Failure disposition

Reject the flow if Journal timing gates the real-change commit, an append is lost or duplicated, writers race on one shared carrier, Journal append uses the Git gate, or either commit class contains the other's files.
