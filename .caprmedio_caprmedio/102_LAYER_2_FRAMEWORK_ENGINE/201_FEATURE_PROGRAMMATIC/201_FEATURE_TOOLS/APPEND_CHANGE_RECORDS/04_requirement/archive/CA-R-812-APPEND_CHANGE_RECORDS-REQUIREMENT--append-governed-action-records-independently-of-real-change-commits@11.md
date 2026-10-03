---
subjects:
  - provenance
cce_version: cce_1
cce_form: obligation
version: 11
updated_at: 2026-08-23 15:46:20 +0400
---
# Append governed action records independently of real-change commits

`APPEND_CHANGE_RECORDS` MUST prepare and append one canonical Journal record for each sealed action independently of that action's real-change Git commit. Multiple workers MAY prepare records and append concurrently to disjoint action-owned Journal partitions. A shared Journal carrier has exactly one canonical writer or batcher at a time; byte-level append safety MUST NOT depend on operating-system append behavior alone. Journal preparation and append are not serialized through the repository Git gate.

Each canonical action record MUST bind the stable action identity, sealed Initiative, affected Atom IDs or native subject identities, resulting revisions or digests, real-change Git commit SHA when available, and Journal event identity. The record identifies its own Journal carrier revision or append location. It MUST NOT embed the SHA of the Git commit that contains that same record; reconciliation derives that carrier-to-Git binding from reachable Git history after the Journal-only commit exists. Repeated preparation, append, batching, recovery, or delayed real-change binding for the same action MUST be idempotent.

Journal-only Git commits MAY batch completed Journal records on a configured interval, including approximately once per minute. A batch commit contains only the selected Journal carrier changes and passes through `COMMIT_CHANGE_SET` only for the Git mutation; its preceding Journal appends remain independently concurrent. Recovery MUST retain an append, batch, or reconciliation failure as durable blocked state rather than inventing or duplicating a Journal event.
