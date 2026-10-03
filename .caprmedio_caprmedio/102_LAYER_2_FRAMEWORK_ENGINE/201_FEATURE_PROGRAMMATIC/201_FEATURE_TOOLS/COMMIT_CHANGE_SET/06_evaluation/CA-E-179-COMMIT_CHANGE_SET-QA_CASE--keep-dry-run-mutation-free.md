---
subjects:
  governs: "Governed Change/Commit Action"
  depends_on: []
version: 14
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805

llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Keep dry-run mutation-free

## Claim checked

`COMMIT_CHANGE_SET` dry run returns the predicted real-change gate result **without** changing repository **or** provenance state.

## Test case

snapshot governed files, outbox state, Journal carriers, runtime outputs, lease state, index entries, refs, **and** object reachability for one valid sealed action. invoke the gate **in** dry-run mode **and** repeat **every** snapshot.

## Acceptance criteria

the result names the exact Initiative, action identity, atomic **or** frozen bulk target set, expected Git base, message Projection, gate eligibility, **and** revalidation result. it **may** identify Journal preparation eligibility but does **not** predict **or** create a Journal batch. **every** captured state remains unchanged, no lease is acquired, **and** no new reachable commit exists.

## Failure disposition

reject the Doer **and** report the first missing prediction **or** mutation.
