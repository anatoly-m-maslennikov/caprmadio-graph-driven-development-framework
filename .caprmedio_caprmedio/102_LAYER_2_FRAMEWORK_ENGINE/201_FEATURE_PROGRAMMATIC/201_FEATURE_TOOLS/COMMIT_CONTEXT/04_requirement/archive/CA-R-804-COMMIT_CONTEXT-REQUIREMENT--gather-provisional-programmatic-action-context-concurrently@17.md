---
subjects:
  declared:
    continuant:
      - feature-boundary
cce_version: cce_1
cce_form: obligation
version: 17
updated_at: 2026-08-23 16:16:20 +0400
---
# Gather provisional programmatic action context concurrently

`COMMIT_CONTEXT` MUST be independently invocable and strictly read-only. From one durable trigger it MUST gather a provisional action context containing the sealed Initiative and action identity, resolved repository frontier, affected subject identity, expected and observed revisions or digests, candidate `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE` change, Git state, Journal state, and all provenance bindings required by later workers.

Multiple context gatherers MAY work concurrently because their output is provisional and mutation-free. Identical input and an unchanged observed frontier MUST produce the same context identity. No gathered context grants authority to mutate. Every effectful consumer MUST revalidate the context against the current repository frontier, expected subject revision or digest, and durable action state immediately before its effect; stale or conflicting context MUST be rejected or returned for fresh gathering.
