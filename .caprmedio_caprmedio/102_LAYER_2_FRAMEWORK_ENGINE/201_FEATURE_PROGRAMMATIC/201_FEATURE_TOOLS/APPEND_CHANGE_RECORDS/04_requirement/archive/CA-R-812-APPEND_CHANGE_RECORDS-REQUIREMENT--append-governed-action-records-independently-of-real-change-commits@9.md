---
subjects:
  - provenance
cce_version: cce_1
cce_form: obligation
version: 9
updated_at: 2026-08-23 13:54:18
relations:
  child_of:
    - CA-R-802
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-522--append-work-journal-events
    - CA-R-1087
---
# Append governed action records independently of real-change commits

`APPEND_CHANGE_RECORDS` MUST prepare and append the canonical Journal record for each sealed action independently of the action's real-change Git commit. Multiple workers MAY prepare action-owned records or append to safely partitioned action-owned fragments concurrently. Exactly one canonical writer or batcher MUST own mutation of any shared Journal carrier so that byte-level append safety does not depend on operating-system append behavior alone.

Each canonical action record MUST bind the action identity, Initiative, affected Atom ID or native subject identity, resulting revision or digest, real-change Git commit SHA when available, Journal event identity, and later Journal-batch commit SHA. Repeated preparation, append, batching, or recovery of the same action MUST be idempotent. Journal-only Git commits MAY batch completed Journal records on a configured interval, including approximately once per minute, but every such commit MUST pass through the same repository Git gate as real-change commits.
