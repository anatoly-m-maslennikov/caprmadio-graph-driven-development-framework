---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "commit-automation"
  depends_on: []
version: 8
updated_at: "2026-09-17 03:10:35 +0000"
relations: {"evaluation_for":["CA-M-087","CA-R-803","CA-R-802"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize concurrent and out-of-order commit events

## Claim checked

concurrent asynchronous intake preserves accepted work while **`<=1`** fenced Git-gate worker performs a Git-mutating effect **in** the repository at a time. independent non-Git branches remain permitted under CA-R-802 **and** CA-M-087.

## Test cases

1. deliver distinct, repeated, **and** out-of-order events concurrently while a repository action holds the valid fenced Git lease.
2. allow admitted intake, context gathering, **and** Journal preparation/append work **to** continue independently. queue a real-change Commit **and** a later Journal-only batch against the same repository gate.
3. attempt a Git effect with a stale fencing token **and** observe both lease admission **and** actual Git-effect intervals. repeat the pending-work reconciliation **after** service restart.

## Acceptance criteria

- **every** distinct accepted identity remains durable; repeated delivery is idempotent; later work marks the repository pending **without** losing **or** duplicating an action.
- **`<=1`** valid fenced Git-gate worker operates at a time. Git effects do **not** overlap, **and** a stale token does **not** authorize an effect.
- real-change **and** Journal-only Commits retain their distinct classes **and** share the same serialized gate. holding that gate does **not** itself block admitted intake, Finder work, **or** independent Journal recording.
- completion prompts further reconciliation of pending work rather than bypassing the gate. restart preserves correlation **and** the pending frontier.
- event arrival order does **not** determine correctness. concurrency outside the Git-mutating boundary is **not** falsely reported as a gate violation.

## Failure disposition

reject the realization on lost identity, duplicate action, overlapping Git effects, concurrent valid leases, stale-token effects, collapsed Commit classes, blocked independent work solely because of the Git lease, **or** event-order-dependent correctness. retain event identities, lease/fencing evidence, effect intervals, branch transitions, **and** reconciliation results.
