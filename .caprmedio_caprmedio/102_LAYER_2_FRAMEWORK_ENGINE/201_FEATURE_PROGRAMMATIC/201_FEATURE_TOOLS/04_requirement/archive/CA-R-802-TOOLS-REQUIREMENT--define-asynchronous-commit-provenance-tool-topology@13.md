---
subjects:
  declared:
    continuant:
      - feature-boundary
cce_version: cce_1
cce_form: obligation
version: 13
updated_at: 2026-08-25 01:49:10 +0400
---
# Define asynchronous commit-provenance Tool topology

Automatic provenance uses four peer Tool Scope Units plus one independently supervised repository-local COMMIT_AUTOMATION service:

| Component | Kind | Owned responsibility |
|---|---|---|
| COMMIT_TRIGGER | Hook Tool | Atomically accept one immutable source event into the Runtime inbox and return without waiting for provenance work. |
| COMMIT_AUTOMATION | Background service | Reconcile accepted events and repository state, persist the manager-defined execution graph, and mechanically dispatch ready work. |
| COMMIT_CONTEXT | Finder Tool | Gather read-only provisional action context and revalidate it at an effect boundary. |
| APPEND_CHANGE_RECORDS | Doer Tool | Prepare and append governed Journal records through the canonical Journal writer. |
| COMMIT_CHANGE_SET | Doer Tool | Serialize every Git mutation through the single logical repository Git gate. |

The four Tools remain peer unordered_unit Scope Units at Structural level 4; the service is an execution component, not a fifth semantic Tool or authority owner. The service has one deterministic I/O-free manager that receives typed facts and returns the complete admissible execution graph or next command. A mechanical Scheduler persists and advances only manager-declared transitions. Workers perform one atomic operation, return typed facts, and never choose targets, ordering, fallback, retry, acceptance, or downstream work.

Trigger intake may run concurrently and out of order. It MUST NOT start one pipeline worker per Hook event. The service preserves accepted work across Hook completion, manager termination, service restart, pause, stop, and reload. It reconciles missed Hook delivery and external edits without treating a host callback as repository truth. Exactly one logical Git-gate worker may mutate one repository at a time. The fixed action pipeline is COMMIT_CONTEXT -> APPEND_CHANGE_RECORDS -> COMMIT_CHANGE_SET; the final Git Doer MUST NOT import or orchestrate its peers. Real-change commits and Journal-only commits remain independent work classes that share the Git gate.
