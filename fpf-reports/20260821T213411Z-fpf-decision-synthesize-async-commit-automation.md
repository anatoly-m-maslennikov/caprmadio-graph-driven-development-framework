## Task, scope, and boundaries

### Decision contract

Select the best architecture for CAPRMEDIO automatic commit processing after the synchronous Codex hook blocked command execution. The receiving use is the next implementation revision of the commit-automation Tools and background-service runtime.

**Decision owner:** Anatoly. This result is a **Decision-Ready Proposal**, not an accepted project decision. The exact remaining owner action is to approve, revise, or reject the proposed configuration below.

**Target and current state:** current checkout `979b1f44da21b94ef155419b5cf4f3c96d393840`. `COMMIT_TRIGGER` still directly performs reconciliation and invokes the commit flow; its local performance/circuit changes remain uncommitted. `START_BACKGROUND_SERVICES` supports start/status, its registry is empty, and no commit-automation service is registered.

**Inputs and evidence:**

- The predecessor [async hook design challenge](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/fpf-reports/20260821T212733Z-fpf-design-challenge-async-hook-manager-worker.md).
- A complete paginated reread of the last 24 hours of the Codex task **“CA #2: TOOLS Ms”** (`019fc24e-24ed-7921-b4db-cf4df3e14bf7`). It establishes: one zero-I/O manager owns decisions; workers perform atomic non-deciding operations; the manager defines the execution graph; the scheduler advances it mechanically; queued state lets work survive manager termination; repository-level watching/reconciliation is required; and expensive evaluation must stay outside synchronous hooks.
- Current official Codex behavior: `async: true` lets Codex continue without waiting, but background hooks may run concurrently, complete out of order, and be cancelled at session end. Background hooks cannot control the triggering operation. [Official OpenAI documentation](https://learn.chatgpt.com/docs/hooks).
- Current project carriers: the pure-manager Method draft, four COMMIT_* Tools, `START_BACKGROUND_SERVICES`, the empty background-service registry, runtime state, and the unresolved governed commit failure.

**Scope:** event intake, durable queue, scheduling, decision ownership, worker boundaries, repository reconciliation, service lifecycle, failure controls, and confirmation tests.

**Excluded:** changing code or RMED authority, recovering the blocked Journal transaction, accepting cross-session commit policy, and declaring live success before an installed end-to-end run.

**Dependencies:** installed-release resolution, typed envelopes, action IDs, atomic runtime writes, one repository Git lease, Journal recovery, and generic background-service lifecycle control.

**Stop condition:** stop at an owner-ready architecture proposal. Do not modify runtime code or claim the decision is accepted.

**Saved report:** `fpf-reports/20260821T213411Z-fpf-decision-synthesize-async-commit-automation.md`

### Review-campaign handoff

- **Campaign ID:** not assigned in the predecessor report.
- **Phase:** design challenge completed; owner disposition pending.
- **Semantic frontier:** async commit event intake, durable scheduling, pure decision management, atomic Tool execution, and recovery controls. No implementation claim is included.
- **Carrier frontier:** predecessor report, current HEAD above, uncommitted COMMIT_TRIGGER patch, current manager Method draft, current service launcher and registry.
- **Evaluation profile:** Codex async-hook constraints, command-host responsiveness, event durability, single-flight Git mutation, manager/worker policy, repository-wide coverage, lifecycle recovery, and live end-to-end evidence. Implementation quality outside this boundary is excluded.
- **Open finding fingerprints:** `HOOK-LOSSY-ACCEPTANCE`, `SPAWN-STORM`, `HOOK-ONLY-COVERAGE`, `LIFECYCLE-EVIDENCE`, and `FAILURE-BUDGET`; all remain `OPEN` until owner disposition.
- **Allowed next action:** owner accepts/revises/rejects this proposal. If accepted, implementation may begin; another full design challenge is not warranted unless the semantic frontier changes.

## High-confidence results (>=95%)

### Candidate and evidence readiness

Four materially distinct candidates were evaluated:

| Candidate | Result |
|---|---|
| A. Keep the synchronous direct pipeline | Reject: it blocks Codex command dispatch and couples intake to all repository work. |
| B. Make the current heavy hook async and let it spawn workers | Reject: it retains duplicate scans, out-of-order execution, process storms, and lossy handoffs. |
| C. Async intake → durable queue → scheduler → pure manager → atomic Tools | **Recommended:** it satisfies responsiveness, durability, decision ownership, single-flight execution, and recovery. |
| D. Repository watcher only | Reject as the sole source: it covers external changes but loses low-latency Codex provenance and still needs the same queue/manager pipeline. Keep it as a second event source. |

The evidence is sufficient to recommend Candidate C. Confidence: **99%**.

### Decision-Ready Proposal

Adopt one explicit new Tool feature, **`COMMIT_AUTOMATION`**, and keep the existing four Tools as peers. `COMMIT_AUTOMATION` contains the pure decision manager and the mechanical runtime workers; it is installed as one repository-local background service.

```text
Event sources
  ├─ Codex PostToolUse hook (async, enqueue only)
  └─ repository watcher + periodic reconciliation
              │
              ▼
Durable event spool
  .caprmedio_runtime/state/commit_automation/inbox/<event_id>.json
              │
              ▼
COMMIT_AUTOMATION background service
  ├─ pure manager: selects the fixed next command from typed state
  ├─ scheduler worker: advances the accepted state machine
  ├─ queue/lease workers: atomic I/O only
  └─ supervisor interface: pause/start/stop/reload/status
              │
              ▼
Exactly one active repository pipeline
  COMMIT_CONTEXT
    → APPEND_CHANGE_RECORDS
    → COMMIT_CHANGE_SET
```

Confidence: **98%**, based on the hook failure evidence, current Tool boundaries, the 24-hour task record, and official Codex behavior.

### Exact responsibility split

- **`COMMIT_TRIGGER`:** normalize an event and atomically enqueue it. No scan, context gathering, Journal write, staging, commit, retry, or worker spawn.
- **`COMMIT_AUTOMATION/commit_automation.py`:** zero-I/O deterministic manager. Given typed queue/repository/action/worker-result/settings facts, return one typed command: reconcile, gather context, append records, commit, wait, retry, pause, complete, or block.
- **Scheduler worker:** execute only the manager's command, persist the transition, and return facts. It may dispatch a predefined downstream Tool but may not select, reorder, skip, or invent work.
- **`COMMIT_CONTEXT`:** read-only Finder that observes the current repository frontier and seals one target/action context.
- **`APPEND_CHANGE_RECORDS`:** idempotent Doer that writes the Journal records and receipt for that sealed action.
- **`COMMIT_CHANGE_SET`:** atomic Git Doer that revalidates, stages, and commits the sealed action. It must stop importing and orchestrating the other Tools.
- **Git hooks:** independent commit validators/observers, not pipeline drivers.

This preserves the “manager decides; scheduler advances; workers report facts” rule from **“CA #2: TOOLS Ms”**. Confidence: **99%**.

### Queue and concurrency policy

- Each hook writes one immutable, schema-versioned event using temp-file plus atomic rename, then exits `0`.
- Event identity includes source, repository, session, turn, tool-use ID, and a stable event ID. The action record retains every contributing event.
- Delivery order is not trusted. The manager reasons from current repository state.
- Only one commit pipeline may hold the repository lease. New events set `pending=true`; after the active action finishes, reconciliation runs again.
- Several events may coalesce into one current target set, but none are discarded from provenance.
- Hook failure or manager downtime cannot erase an already-spooled event.

Confidence: **99%**. This directly addresses Codex's documented concurrency, ordering, and cancellation limits.

### State machine

Use durable transitions:

```text
queued → reconciling → context_sealed → journaled → committing → completed
                 └──────────────→ no_change
any safe phase ────────────────→ retry_wait | paused | blocked | dead_letter
```

Every transition records `action_id`, input/result digest, selected installed release, attempt, timestamps supplied by an I/O worker, diagnostics, and next admissible transitions. Recovery resumes from persisted state; it does not restart the whole chain blindly. Confidence: **98%**.

### Manual and automatic control

Extend `START_BACKGROUND_SERVICES` into generic lifecycle infrastructure and register `commit-automation` in `background_services.toml`.

- `status`: service/worker PID, release, queue depth/bytes, current action/phase, lease, last success/failure, breaker, and dead letters.
- `pause`/`resume`: stop or resume dispatch while the manager stays available and the inbox remains writable.
- `stop`/`start`: terminate or launch the service without deleting queue/action state.
- `reload`: drain or reach a safe boundary, re-resolve the selected installed release, restart, and reconcile.
- **Automatic pause:** open the circuit on declared queue, timeout, crash, lease, or consecutive-failure budgets.
- **Automatic restart:** the generic service supervisor may restart a crashed service only within a restart budget. Exhaustion leaves it stopped and visible.
- **Automatic resume:** allowed only for classified transient failures after cooldown plus a passing health probe. Governance, Journal, staging, and ambiguous Git failures require manual recovery.
- Never force-kill during the `journaled → committing` critical section; mark recovery required if bounded graceful shutdown cannot prove a safe state.

Confidence: **97%**. This supplies the requested manual and automatic stop/start/reload behavior without allowing a restart loop to become another storm.

### Repository-wide coverage

The background service must combine event-driven wake-ups with low-frequency reconciliation. Codex hooks are latency hints and provenance sources; the repository frontier is the correctness source. This covers older tasks, missed/cancelled hooks, and external editors. Confidence: **99%**.

### Accepted losses and consequences

- Add one explicit Tool feature and a durable state-machine schema.
- Accept modest background-service and migration complexity.
- Accept small coalescing latency to prevent commit storms.
- A commit may represent several contributing tool events; provenance remains many-to-one rather than pretending exact one-event/one-commit causality.
- Queue and action records require versioning and garbage-collection policy.
- The existing batched Git-ignore optimization remains useful, but it moves to reconciliation/worker execution; hook-local circuit/control logic is discarded.

Confidence: **98%**.

### Confirmation path and reopen triggers

The architecture is confirmed only after all of these pass against an installed release:

1. `pwd` and no-op commands start without waiting for repository analysis.
2. Concurrent and out-of-order hook events produce no loss, duplicate action, or parallel Git worker.
3. Killing the hook after the atomic enqueue still leads to later processing.
4. Killing/restarting the service at every safe state resumes correctly.
5. `pause`, `stop`, `start`, and `reload` preserve the queue and respect the critical section.
6. An edit completes the live path: trigger → context → Journal → commit → receipts, with an empty blocked directory.
7. External edits are caught by reconciliation.
8. Pure-manager tests prove identical input gives identical command/result and no I/O occurs.

Reopen the architecture if any event is lost, duplicate/parallel Git mutation occurs, cross-session coalescing proves unacceptable, queue lag breaches the accepted budget, the service repeatedly exhausts its restart budget, or another workflow needs a genuinely generic scheduler rather than this bounded Tool. Confidence: **99%**.

### Proposed ADR projection

- **Status:** Proposed; not authoritative until Anatoly accepts it.
- **Question:** How should CAPRMEDIO process automatic commit triggers without blocking Codex or losing governed work?
- **Outcome:** Candidate C—async event intake, durable spool, repository-local `COMMIT_AUTOMATION` service, pure manager, mechanical scheduler, single-flight atomic peer Tools, and repository reconciliation.
- **Rejected:** synchronous direct execution; async direct spawning; watcher-only intake.
- **Rationale:** separates responsiveness, durability, decisions, mechanical progression, and effects while preserving existing Tool responsibilities.
- **Trade-offs:** one new Tool and durable lifecycle complexity; event-to-commit provenance can be many-to-one.
- **Implementation instruction:** first establish Tool/RMED authority and state schemas; then implement service lifecycle; then reduce the Codex hook; finally run failure-injection and live installed-path confirmation.
- **Supersession condition:** any reopen trigger above or an accepted replacement architecture.

## Open questions (confidence <95%)

1. **May one commit coalesce changes contributed by concurrent Codex sessions? Best current answer: yes, with all event IDs preserved. Confidence: 92%.**

   Missing input: explicit project authority for cross-session commit grouping. Consequence: if forbidden, the queue must partition by session and serialize session-specific frontiers. Next action: Anatoly chooses repository-frontier grouping or session partitioning.

2. **What are the admitted latency, queue, retry, and shutdown budgets? Best current answer: measure first, then declare budgets for hook enqueue, reconciliation lag, queue size, worker duration, retry count, cooldown, and graceful shutdown. Confidence: 91%.**

   Missing evidence: benchmarks on the installed path and representative dirty repositories. Consequence: circuit behavior cannot be accepted yet. Next action: implement a measurement harness before setting numeric gates.

3. **Should the generic service supervisor be framework-portable or use host-native service management? Best current answer: keep the repository service portable and introduce host-specific adapters only when supported-platform authority exists. Confidence: 92%.**

   Missing input: current supported-platform policy. Consequence: crash restart after the supervisor itself dies remains platform-dependent. Next action: establish platform support, then select launchd/systemd/Windows adapters or a portable supervisor boundary.

4. **Which failures may auto-resume? Best current answer: only proven transient failures before governed mutation; never auto-resume governance, Journal, staging, ambiguous Git, or lease-integrity failures. Confidence: 93%.**

   Missing evidence: a complete failure taxonomy and recovery tests. Consequence: an overbroad auto-resume rule could loop or corrupt attribution. Next action: classify every current failure code and attach one recovery policy before enabling automatic resume.

5. **Owner disposition remains unresolved. Confidence: 100% that authority is missing.**

   The proposal is ready, but only Anatoly can change its status to accepted, revised, or rejected. Until then, implementation authority is absent and the campaign findings remain open.

## Skills used

1. `openai-docs` — verified current official Codex background-hook behavior and limitations.
2. `fpf-decision-synthesize` — converted evaluated alternatives and the prior challenge into a recoverable decision-ready proposal and proposed ADR projection.

#### FPF sources consulted (2 read; 2 used)

- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/20_32_Architecture Candidate Synthesis/08_C.32.PAD - Project Architecture Decision After Candidate Synthesis.md` — **used**: decision authority, candidate basis, accepted losses, implementation consequences, and reopen conditions.
- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/20_32_Architecture Candidate Synthesis/09_C.32.ADR - Architecture Decision Record Projection.md` — **used**: proposed reader-facing ADR projection and decision/record separation.

<oai-mem-citation>
<citation_entries>
MEMORY.md:137-137|note=[repository coverage beyond task local hooks]
MEMORY.md:148-148|note=[live hook confirmation and blocked action boundary]
MEMORY.md:102-102|note=[commit pipeline context]
</citation_entries>
<rollout_ids>
019fc24e-24ed-7921-b4db-cf4df3e14bf7
</rollout_ids>
</oai-mem-citation>
