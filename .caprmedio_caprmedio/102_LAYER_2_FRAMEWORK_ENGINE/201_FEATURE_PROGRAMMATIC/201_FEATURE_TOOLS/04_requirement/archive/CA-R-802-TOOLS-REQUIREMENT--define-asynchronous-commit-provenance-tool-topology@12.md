---
subjects:
  declared:
    continuant:
      - feature-boundary
cce_version: cce_1
cce_form: obligation
version: 12
updated_at: 2026-08-23 16:16:20 +0400
---
# Define asynchronous commit-provenance Tool topology

The automatic provenance flow uses four peer `unordered_unit` Tool Scope Units after one governed project-path action:

| Scope Unit | Tool kind | Owned responsibility |
|---|---|---|
| `COMMIT_TRIGGER` | Hook | Durably enqueue one sealed action trigger without waiting for provenance completion. |
| `COMMIT_CONTEXT` | Finder | Gather read-only provisional action context concurrently and revalidate it at an effect boundary. |
| `APPEND_CHANGE_RECORDS` | Doer | Prepare and append governed Journal records through the canonical Journal writer. |
| `COMMIT_CHANGE_SET` | Doer | Serialize every Git mutation through the single logical repository Git gate. |

These Tools are peers at Structural level `4`. `START_BACKGROUND_SERVICES` may start and supervise their registered background processes, but it is a lifecycle Tool rather than another provenance stage. Trigger production, provisional context gathering, and action-owned Journal preparation may each run with concurrency greater than one. A scheduler MUST enforce its configured concurrency cap and give every worker one action-isolated target scope with no shared mutable subject state. Exactly one logical Git-gate worker may mutate one repository at a time. Real-change commits and Journal-only commits are independent work classes that share this Git gate instead of one combined commit transaction.
