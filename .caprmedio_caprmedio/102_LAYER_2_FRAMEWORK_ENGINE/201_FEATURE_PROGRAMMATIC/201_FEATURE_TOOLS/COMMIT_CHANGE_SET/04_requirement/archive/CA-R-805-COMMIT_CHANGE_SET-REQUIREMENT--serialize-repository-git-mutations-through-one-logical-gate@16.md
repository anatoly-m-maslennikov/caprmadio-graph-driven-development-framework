---
subjects:
  - feature-boundary
cce_version: cce_1
cce_form: obligation
version: 16
updated_at: 2026-08-23 15:46:20 +0400
---
# Serialize repository Git mutations through one logical gate

`COMMIT_CHANGE_SET` MUST own the only logical Git-mutation gate for one resolved repository. Trigger producers, schedulers, context gatherers, append workers, and retry workers MAY operate concurrently, but all Git staging, committing, and any other repository Git mutation pass through this one gate.

Each sealed action has one durable outbox record keyed by its stable action identity. The outbox preserves its sealed Initiative, exact atomic target or ordered bulk target set, expected Git base and subject frontier, preparation state, and idempotency result. A scheduler may prepare any ready item, but only the gate may select an item for a Git effect. Gate acquisition MUST use a repository-scoped lease with a unique holder identity, expiry, and monotonically increasing fencing token. The holder MUST revalidate the still-current lease and fencing token immediately before staging, immediately before the Git mutation, and before recording the result. A stale, expired, or fenced-out holder MUST perform no further Git mutation. An uncertain or interrupted mutation MUST be reconciled against Git and the outbox before any retry, rather than replayed as a second commit.

Before a Git effect, the gate MUST revalidate the sealed Initiative, action identity, expected Git base, subject frontier, each target's revision or digest, and the complete staged target set. An atomic real-change commit contains exactly that action's one subject change. A bulk real-change commit contains all and only the frozen subjects of its one sealed bulk action. A real-change commit MUST use the Initiative-based message Projection and MUST NOT require its corresponding Journal record in the same commit.

A Journal-only batch commit contains only canonical Journal carrier changes selected by the batcher, may batch completed records for multiple actions, and shares this same Git gate. The gate MUST never combine unrelated real-change actions, mix a real-change item with a Journal-only batch, or treat Journal append itself as a Git-gate operation. Interrupted work remains durable, idempotent, and recoverable through its outbox state and reconciliation without allowing a second Git-mutating worker to bypass the gate.
