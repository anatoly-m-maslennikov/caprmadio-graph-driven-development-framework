## Task, scope, and boundaries

**FPF Challenge Finding — async hook → manager → worker**

Yes. The split is sound, with one necessary correction: the manager must do no repository analysis or commit work on the hook path, but it must **durably accept and acknowledge** the event before the async hook exits. Then it may schedule the actual worker. Merely receiving an in-memory message and returning would be lossy.

:codex-annotation{index="1"} The earlier diagnosis was specific to the current synchronous handler. Codex waits for hooks by default, while an `async: true` hook runs in the background; background hooks cannot block or control the triggering action. Codex may run up to eight background hooks concurrently, they may finish out of order, and unfinished ones can be cancelled when the session ends. Therefore, making the current full-scan hook async is insufficient—the hook itself must become a tiny durable enqueue operation. See the official [Codex hooks documentation](https://learn.chatgpt.com/docs/hooks).

- **Proposal:** replace synchronous commit-trigger processing with an asynchronous event-acceptance hook, a long-lived manager, and isolated worker execution.
- **Entity of Concern:** the CAPRMEDIO automatic commit-trigger runtime boundary.
- **Bounded context:** Codex hook dispatch, repository-local queueing, installed-tool selection, worker lifecycle, and recovery controls. The semantics of `COMMIT_CHANGE_SET` itself are outside this review.
- **Intended result:** shell/tool dispatch never waits for repository scanning or commit work, while triggers remain recoverable and governed.
- **Receiving use:** implementation decision for the next COMMIT_TRIGGER/manager revision.
- **Decision owner:** Anatoly as project operator. FPF informs the decision but does not establish project authority.
- **Current evidence boundary:** this is a design finding. No hook or service code was changed in this pass. The earlier performance/circuit changes remain local and uncommitted, and the existing stale blocked action still prevents a governed commit/install proof.
- **Saved report:** `fpf-reports/20260821T212733Z-fpf-design-challenge-async-hook-manager-worker.md`

Recommended boundary:

```text
Codex async PostToolUse hook
  -> atomic durable inbox write (then exit 0)
  -> repository manager
       -> deduplicate and coalesce
       -> enforce one active worker lease
       -> stop/start/reload/status and circuit state
  -> worker
       -> observe current repository frontier
       -> form canonical governed trigger
       -> run COMMIT_CHANGE_SET
       -> persist receipt or dead-letter result
```

The hook event is a **wake-up trigger**, not yet the canonical semantic file-change trigger. The worker creates the governed trigger from current repository evidence. This separates the hook occurrence, manager scheduling, worker Work, result, and evidence instead of treating them as one “hook succeeded” claim (FPF A.6.C and A.15).

## High-confidence results (>=95%)

1. **Concern — an in-memory catch-and-spawn boundary can lose triggers. Confidence: 99%.**

   The hook should atomically write an event file such as `.caprmedio_runtime/state/commit_manager/inbox/<event-id>.json` before optional IPC notification. Only that durable write is acceptance. If the manager is down, the event remains queued and `start`/`reload` drains it. This follows the boundary discipline of separating what occurred from what result and evidence support reliance (FPF A.6.C, especially sections 1–4).

2. **No concern found — asynchronous `PostToolUse` is the correct Codex dispatch mechanism. Confidence: 99%.**

   Remove automatic commit work from `PreToolUse`. Use `PostToolUse` with `async: true`, a 1–2 second timeout, and O(1) enqueue behavior. A `Stop` hook may add a final wake-up event, but it must use the same durable path. The current batched-ignore optimization should remain because the worker still needs it. The official hook semantics support this dispatch choice: [Codex hooks documentation](https://learn.chatgpt.com/docs/hooks).

3. **Concern — spawning one worker per hook recreates a process storm. Confidence: 99%.**

   The manager should enforce one active worker per repository. Further events mark the repository pending; after the worker exits, the manager reconciles the current frontier again. Multiple hook events may be coalesced into one job while retaining every contributing `session_id`, `tool_use_id`, event type, and event ID. This keeps System, role, Method, and dated Work assignments explicit (FPF A.15).

4. **Concern — hook delivery cannot be the sole correctness boundary. Confidence: 98%.**

   Background hooks can be cancelled and external editors or older/unhooked tasks produce no hook event. The manager therefore needs a low-frequency repository reconciliation pass. Hooks reduce latency; repository state remains the source of truth. This also matches the framework's earlier finding that repository-level coverage is required beyond task-local hooks.

5. **Concern — stop/reload must control Work without deleting evidence. Confidence: 99%.**

   Implement these manager operations:

   - `stop`: stop admitting new workers; cooperatively terminate or time-bound the active worker; preserve the inbox.
   - `start`: resume admission and drain the inbox.
   - `reload`: stop admission, settle/terminate the worker, re-resolve the selected installed release, restart, then drain.
   - `status`: report manager PID, selected release, queue depth/bytes, active worker PID and lease, last success/failure, circuit state, and dead-letter count.

   Autonomy must have an explicit budget, guard, ledger, and pause/resume path; depletion must halt further autonomous Work (FPF E.16, sections 1–4 and 7).

6. **Concern — automatic recovery needs bounded failure policy. Confidence: 98%.**

   Open the circuit and pause worker admission on any declared limit: queue count/bytes, consecutive failures, worker timeout, lease collision, stale PID ambiguity, or repeated recovery failure. Keep queued events. Automatic resume may occur only under a declared cool-down policy; otherwise require manual `start`/`reload`. Record each check as `satisfied`, `violated`, `unknown`, or `error` rather than treating a missing check as success (FPF A.20, sections 4.1–4.2 and 9–10).

7. **No concern found — reuse the existing service launcher as infrastructure, not as the manager's semantics. Confidence: 96%.**

   `START_BACKGROUND_SERVICES` already resolves installed services, detaches processes, persists PID state, and reports status. It currently supports start/status only and the service registry is empty. Extend its generic lifecycle with stop/reload, while keeping queueing, leases, coalescing, and circuit logic in a dedicated `COMMIT_MANAGER` tool/service.

8. **Project disposition — revise and implement, not accept `async: true` alone.**

   Move the circuit/control logic out of the hook runner and into `COMMIT_MANAGER`; reduce `codex_hook` to durable enqueue; keep batched Git-ignore scanning in the worker. The existing blocked commit lease should pause worker admission but must not make command dispatch unhealthy.

## Open questions (confidence <95%)

1. **FPF not decisive — repository-local or machine-wide manager? Confidence: 92%.**

   Best current answer: one manager per repository because installation selection, runtime state, leases, and recovery are repository-scoped. A machine-wide supervisor could later manage those repository-local instances. Confirmation depends on the desired cross-repository operating model.

2. **Insufficient basis — may one commit coalesce events from concurrent Codex sessions? Confidence: 90%.**

   Best current answer: yes only when the resulting target set is governed as one current repository frontier and the receipt lists all contributing events. If project policy requires one-session/one-commit attribution, the manager must partition queues by session and serialize those partitions. The current evidence does not establish that policy choice.

3. **Insufficient basis — exact worker cancellation semantics during `reload`. Confidence: 90%.**

   Best current answer: cooperative shutdown first, bounded wait second, forced termination last, followed by lease recovery and frontier reconciliation. The safe timeout and whether an in-progress Git commit may be interrupted require a state-transition specification and fault-injection tests.

## Skills used

1. `openai-docs` — verified current official Codex async-hook behavior and constraints.
2. `fpf-design-challenge` — challenged the proposed architecture and separated proposal, Work, results, evidence, autonomy controls, and unresolved project decisions.

#### FPF sources consulted (5 read; 5 used)

- `FPF-Knowledge-Graph/00-readme/02_Practical-Use Cards.md` — used to route the architecture question to a bounded pattern set.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/03_A.06.C - Contract Unpacking for Boundaries.md` — used for boundary, Work/result, and evidence separation.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/15_System-Role-Method-Work Alignment/00_A.15 - System-Role-Method-Work Alignment.md` — used for manager/worker role and Work alignment.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/20_Constraint Validity for Transformation Steps/00_A.20 - Constraint Validity for Transformation Steps.md` — used for explicit check outcomes and failure-state handling.
- `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/15_16_RoC-Autonomy Budget & Enforcement/00_E.16 - RoC-Autonomy Budget & Enforcement.md` — used for budgets, guards, ledgers, and manual pause/resume controls.

<oai-mem-citation>
<citation_entries>
MEMORY.md:137-137|note=[repository coverage beyond task local hooks]
MEMORY.md:148-148|note=[live hook proof and blocked action boundary]
MEMORY.md:102-102|note=[commit trigger pipeline context]
</citation_entries>
<rollout_ids>
019fc24e-24ed-7921-b4db-cf4df3e14bf7
</rollout_ids>
</oai-mem-citation>
