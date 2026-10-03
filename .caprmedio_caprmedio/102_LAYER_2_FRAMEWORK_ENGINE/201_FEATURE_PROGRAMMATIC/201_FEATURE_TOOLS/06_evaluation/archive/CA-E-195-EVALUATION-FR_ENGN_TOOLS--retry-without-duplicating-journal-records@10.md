---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 10
updated_at: 2026-08-23 16:45:00 +0400
relations:
  evaluation_for:
    - CA-R-804
    - CA-R-805
    - CA-R-812
---
# Retry without duplicating Journal records

## Claim checked

Interrupted Journal append, real-change gate, and Journal-batch work recover from one sealed action without duplicating or redefining evidence.

## Test case

Use one sealed action. Interrupt a Journal append after a proper subset of an action-owned partition is written, retry it with changed process time, then separately interrupt the real-change gate after an uncertain Git effect. Reconcile the gate against Git and outbox state before retrying. Finally batch the completed Journal record.

## Acceptance criteria

The Journal contains one canonical record for the action; an identical append retry reuses its identity and writes only missing bytes. A divergent record payload fails before append. The uncertain Git effect is reconciled before any retry and produces at most one real-change commit. Journal append and batch state remain independent of the gate lease; a later Journal-only batch commits only Journal carrier changes. Recovery state retains durable action, receipt, and reconciliation references without copied mutable provenance.

## Failure disposition

Reject the flow if recovery duplicates or redefines an event, retries an uncertain Git effect blindly, mixes a Journal batch into a real-change commit, or loses the sealed action binding.
