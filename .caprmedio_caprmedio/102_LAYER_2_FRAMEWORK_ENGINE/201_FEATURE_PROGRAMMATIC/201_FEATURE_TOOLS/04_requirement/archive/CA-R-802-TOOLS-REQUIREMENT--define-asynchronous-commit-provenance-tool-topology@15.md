---
atom_id: CA-R-802
subjects:
  governs:
    continuant:
      - feature-boundary
cce_version: cce_1
cce_form: obligation
version: 15
updated_at: 2026-09-04 03:10:59 +0400
---
# Define asynchronous commit-provenance Tool topology

Automatic provenance uses four peer Tool Scope Units plus one independently supervised repository-local COMMIT_AUTOMATION service:

| Component | Kind | Owned responsibility |
|---|---|---|
| COMMIT_TRIGGER | Hook Tool | Atomically accept one immutable source event into the Runtime inbox and return without waiting for provenance work. |
| COMMIT_AUTOMATION | Background service | Reconcile accepted events and repository state, persist the manager-defined execution graph, and mechanically dispatch ready work. |
| COMMIT_CONTEXT | Finder Tool | Gather read-only provisional action context and revalidate it at an effect boundary. |
| APPEND_CHANGE_RECORDS | Doer Tool | Prepare and append governed Journal records through the canonical Journal writer. |
| COMMIT_CHANGE_SET | Doer Tool | Serialize admitted local commit creation through the single logical repository Git gate. |

The four Tools remain peer unordered_unit Scope Units at Structural level 4; the service is an execution component, not a fifth semantic Tool or authority owner. The service has one deterministic I/O-free manager that receives typed facts and returns the complete admissible execution graph or next command. A mechanical Scheduler persists and advances only manager-declared transitions. Workers perform one atomic operation, return typed facts, and never choose targets, ordering, fallback, retry, acceptance, or downstream work.

Trigger intake, context gathering, and Journal preparation may run concurrently and out of order. Trigger intake MUST NOT start one pipeline worker per Hook event. The service preserves accepted work across Hook completion, manager termination, service restart, pause, stop, and reload. It reconciles missed Hook delivery and external edits without treating a host callback as repository truth. Exactly one logical Git-gate worker may create a commit in one repository at a time.

After COMMIT_CONTEXT seals an action, real-change commit work and Journal append work are independent branches. A real-change commit does not wait for a Journal append or Journal-only commit. Journal records remain the canonical append-only provenance stream and are committed later through an independent Journal-only batch. Both commit classes share the same Git gate, while Journal append itself does not.

Automatic execution is limited by the current COMMIT_AUTOMATION autonomy envelope. That envelope may admit only local real-change commits and local Journal-only commits. Branch creation, deletion, or rename; upstream or remote selection or configuration; fetch, pull, merge, or rebase; push or force-push; tags; releases; and every other Git effect remain explicit Operator or external operations outside CAPRMEDIO Tools. The final Git Doer MUST NOT import or orchestrate its peers.
