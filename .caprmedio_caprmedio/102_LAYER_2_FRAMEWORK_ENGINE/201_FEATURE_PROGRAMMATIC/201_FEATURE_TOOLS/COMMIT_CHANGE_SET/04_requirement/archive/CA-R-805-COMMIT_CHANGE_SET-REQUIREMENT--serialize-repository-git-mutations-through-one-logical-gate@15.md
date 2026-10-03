---
subjects:
  - feature-boundary
cce_version: cce_1
cce_form: obligation
version: 15
updated_at: 2026-08-23 15:33:04 +0400
---
# Serialize repository Git mutations through one logical gate

`COMMIT_CHANGE_SET` MUST own the only logical Git-mutation gate for one resolved repository. Any number of schedulers or workers MAY prepare work, but exactly one gate holder may stage or commit at a time. The gate MUST select one ready work item, revalidate its sealed Initiative, action identity, expected Git base, subject frontier, revision or digest, and staged target set, then create either one real-change commit or one Journal-only batch commit.

A real-change commit contains only the governed subject change for its sealed atomic or bulk action and uses the Initiative-based message Projection. It MUST NOT require the corresponding Journal record to be present in the same commit. A Journal-only batch commit contains only canonical Journal changes selected by the batcher and MUST bind them to their real-change commit SHAs when those SHAs are available. The gate MUST never combine unrelated real-change actions or mix a real-change work item with a Journal-only batch. Interrupted work MUST remain durable and idempotently resumable without allowing a second Git-mutating worker to bypass the gate.
