---
atom_id: CA-R-812
subjects:
  governs: "provenance"
  depends_on:
    - "Journal"
    - "Journal/Record"
    - "Atom"
    - "Artifact/Carrier"
    - "Project"
    - "Applicable Methodology"
cce_version: cce_1
cce_form: obligation
version: 15
updated_at: "2026-09-16 21:24:29 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-R-1491
---
# Append governed action records independently of real-change commits

APPEND_CHANGE_RECORDS **must** prepare **and** append **=1** canonical Journal record for **every** sealed action independently of that action's real-change Git commit.

## Append boundary

- the append **may** complete **before** **or** **after** the real-change commit **and** **must not** be its admission gate.
- apply the storage-integrity boundary of CA-R-1491. nonconforming Atom IDs, filenames, placement, properties, relations, **or** lifecycle state **must not** block recording an observed event.
- preserve the supplied observations **without** converting them into a Project-conformance judgment. Project Evaluations **and** their Tools own those judgments.
- a later Project change does **not** invalidate an intact sealed historical observation merely because the live Project differs. do **not** silently rebind the event **to** that later state.

## Storage behavior

- multiple workers **may** prepare records **and** append concurrently **to** disjoint action-owned Journal partitions. a shared Journal Carrier has **=1** canonical writer **or** batcher at a time; byte-level append safety **must not** depend on operating-system append behavior alone.
- bind the action identity, sealed Initiative, observed subject identity, resulting Revisions **or** digests, available real-change Git commit reference, **and** Journal Event identity. identify the Journal append location **without** embedding the commit SHA of a Git commit that would contain that same record; later reconciliation derives that binding.
- repeated preparation, append, batching, recovery, **or** delayed real-change binding for the same event **must** be idempotent. conflicting payloads under the same Event identity fail storage-integrity checks; the failure **must not** overwrite accepted history.
- Journal-only Git commits **may** batch completed records at the configured interval. **only** the Git mutation passes through COMMIT_CHANGE_SET; preceding Journal appends remain independent.
- preserve append, batch, **or** reconciliation failure as durable blocked state rather than inventing **or** duplicating an event.
