## Task, scope, and boundaries

:codex-annotation{index="1"}

**Selected call.** `$fpf sota harvest` was executed for this receiving question: should CAPRMEDIO place broad-context work such as creating and progressing CAO and authoring new RMED Atoms in Codex, while placing validation, implementation, testing, and evaluation in a workflow engine with stable prompts, isolated allowlisted context, no shared memory, and bounded runs?

**Harvest contract (`HP-2026-08-27-v1`).** The task is to map current architectural knowledge, not to approve the proposal. The comparison basis is recoverability, project integrity, semantic adequacy, security, failure recovery, observability, cost, and latency. Included sources must be primary research, an official standard, official product documentation, or a current first-party engineering report with a directly relevant claim region. The freshness boundary is 2026-08-27; older sources remain included only where they establish a still-current backbone. Secondary summaries, generic vendor comparisons, implementation instructions, and claims that one product is universally best are excluded. The family coverage floor is three; six materially distinct architectural traditions were retained. No numerical diversity-by-distance gate was used.

**Resolved FPF source.** The governing source is `G.2 — SoTA Harvester & Synthesis`, status Stable, generated 2026-08-26 from upstream FPF revision `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`. It requires a reconstructible corpus boundary, claim-level anchors, preserved plurality, explicit bridges and losses, and a receiving-use boundary. This report makes no CAPRMEDIO authority change and creates no RMED, implementation, or workflow-engine decision.

**Entity and use boundary.** The entity being compared is a future CAPRMEDIO work-execution architecture, not Codex, a workflow product, or an LLM in isolation. Routing is determined by the pair **`(content role, operation)`**. The content role defines the meaning, authority, and evidence boundary of the subject; the operation defines the required context, control flow, isolation, and replay posture. Neither coordinate is sufficient alone. The intended use is a later architecture challenge and decision; it is not sufficient implementation authority.

**Saved report:** `.caprmedio/fpf-reports/20260826T202459Z-fpf-sota-harvest-broad-context-agent-narrow-workflow.md`

### CorpusLedger

Included sources and exact claim regions:

1. **S01 — FPF G.2, revision `563f4c8`, generated 2026-08-26; include.** Claim regions: problem frame, harvest loop, conformance checklist, anti-patterns, and consequences. Use: harvesting discipline and receiving boundary.
2. **S02 — Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), 2024-12-19; include.** Claim regions: workflows versus agents, when to use each, and cost/latency/error trade-offs. Use: the principal open-ended-versus-predefined distinction.
3. **S03 — Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29; include.** Claim regions: finite attention budget, minimal high-signal context, dynamic retrieval, compaction, and long-term memory. Use: broad-context design and its limits.
4. **S04 — Anthropic, [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents), 2026-04-08; include.** Claim regions: session/harness/sandbox separation, external append-only session log, credential boundary, recovery, and measured time-to-first-token effects. Use: current long-horizon agent architecture.
5. **S05 — Anthropic, [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps), 2026-03-24; include.** Claim regions: structured handoffs, context resets, planner/generator/evaluator separation, self-evaluation weakness, and overhead. Use: handoff and independent-evaluation evidence.
6. **S06 — Temporal, [Workflow Definition](https://docs.temporal.io/workflow-definition), live documentation accessed 2026-08-27; include.** Claim regions: deterministic replay, Activities for API/LLM/database operations, event history, and workflow versioning. Use: durable deterministic orchestration.
7. **S07 — Temporal, [Workflow Execution overview](https://docs.temporal.io/workflow-execution), live documentation accessed 2026-08-27; include.** Claim regions: durable execution, exclusive local state, recovery, replay, commands, and event history. Use: explicit run state and recovery.
8. **S08 — Microsoft, [Durable orchestrator code constraints](https://learn.microsoft.com/en-us/azure/durable-task/common/durable-task-code-constraints), updated 2026-04-03; include.** Claim regions: event sourcing, deterministic replay constraints, activity-recorded nondeterminism, and versioning hazards. Use: a second durable-workflow lineage.
9. **S09 — LangChain, [LangGraph Functional API](https://docs.langchain.com/oss/python/langgraph/functional-api), live documentation accessed 2026-08-27; include.** Claim regions: checkpointed tasks, determinism, idempotency, side effects, retries, and resumption. Use: hybrid agent/workflow runtime.
10. **S10 — LangChain, [LangGraph backward compatibility](https://docs.langchain.com/oss/python/langgraph/backward-compatibility), live documentation accessed 2026-08-27; include.** Claim regions: latest-graph semantics for resumed threads and differences from version-pinned workflow engines. Use: an important disagreement within durable runtimes.
11. **S11 — MLflow, [Create and Edit Prompts](https://mlflow.org/docs/latest/genai/prompt-registry/create-and-edit-prompts/), live documentation accessed 2026-08-27; include.** Claim regions: immutable prompt versions, metadata, comparison, reproducibility, and lineage. Use: prompt/configuration versioning.
12. **S12 — Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 2026-01-09; include.** Claim regions: task/trial/harness/environment separation, transcripts versus outcomes, grader plurality, stable test environments, and cost/latency tracking. Use: evaluation isolation and evidence design.
13. **S13 — Model Context Protocol, [Authorization specification 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization); include.** Claim region: least-privilege scope selection and resource-specific authorization. Use: tool grants.
14. **S14 — NIST SP 800-207, [Zero Trust Architecture](https://doi.org/10.6028/NIST.SP.800-207), final 2020; include.** Claim regions: no implicit trust, per-resource access decisions, least privilege, and continuous evaluation. Use: security boundary independent of any LLM vendor.
15. **S15 — W3C, [PROV overview and PROV-DM references](https://www.w3.org/TR/prov-overview/), 2013 Recommendations; include.** Claim regions: entities, activities, agents, derivations, and provenance interchange. Use: durable lineage vocabulary.
16. **S16 — OpenTelemetry, [Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/), live documentation accessed 2026-08-27; include.** Claim regions: trace/span correlation across service and process boundaries and log correlation. Use: operational observability across planes.
17. **S17 — Liu et al., [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172), arXiv v3 2023-11-20 and TACL 2024; include.** Claim regions: multi-document QA, key-value retrieval, positional effects, and more-context trade-offs. Use: evidence against treating maximum context as uniformly beneficial.

**Parked, not used as load-bearing evidence.** MemGPT was screened as an important memory-hierarchy design, but its 2023 experiments do not by themselves justify CAPRMEDIO’s current memory policy. Product-specific workflow comparisons were parked because the receiving decision has not yet declared hosting, language, deployment, privacy, or operations constraints. OpenAI-specific orchestration material was not needed to establish any claim and was therefore not added merely for symmetry.

### FlowRecord and coverage boundary

The search began from six source families: agent harness/context engineering, durable replay engines, hybrid agent runtimes, prompt/evaluation lifecycle, least-privilege security, and provenance/observability. Each family was expanded only until at least one current first-party source and, where useful, one independent lineage or standard supported the load-bearing claims. Sources were included when they changed a boundary or supplied a replayable mechanism; otherwise they were parked. The resulting set covers six traditions and seventeen included entries. It is intentionally not a market survey, benchmark ranking, workflow-engine selection, or exhaustive memory literature review.

The main evidence limitation is external validity: several 2025–2026 agent-harness findings are first-party engineering reports rather than controlled cross-vendor studies. They can establish viable mechanisms and observed failure modes, but not universal performance. The durable-execution, security, and provenance claims have stronger cross-lineage support from multiple implementations and standards.

## High-confidence results (>=95%)

### SoTA_Set and palette

The reconstructible `SoTA_Set` contains six architectural traditions. The palette preserves them as alternatives and complements rather than collapsing them into one architecture:

1. **T1 — Long-horizon agent harness and context engineering.** Optimizes adaptive search, interpretation, planning, and action over changing context.
2. **T2 — Deterministic durable workflow orchestration.** Optimizes replay, recovery, explicit state transitions, retries, and controlled side effects.
3. **T3 — Hybrid agent graph runtime.** Mixes model-directed and predetermined nodes with checkpoints and resumable state.
4. **T4 — LLMOps and evaluation lifecycle.** Treats prompts, model configuration, datasets, trials, graders, traces, and outcomes as versioned evidence-bearing artifacts.
5. **T5 — Zero-trust and capability security.** Grants only the resources and operations required for a run and keeps credentials outside untrusted execution.
6. **T6 — Provenance and distributed observability.** Carries causal and derivation identity across service, process, and artifact boundaries.

No tradition alone answers the CAPRMEDIO receiving question. T1 and T2 define the main behavioral contrast; T3 shows they can be composed; T4–T6 constrain any safe, reviewable composition.

### SoTAPaletteDescription

The base palette is the six-tradition `SoTA_Set` above, bound to ClaimSheet families `CS-T1` through `CS-T6`, the downstream-stub inventory, the entity-of-concern map, six worked micro-examples, and candidate synthesis record `G2F-01`. It is not a ranking or engine shortlist. The only derived view used in this report is the receiving-use grouping **adaptive authoring/governance**, **durable bounded execution**, and **cross-cutting assurance**; all six source traditions remain recoverable beneath that grouping. **Confidence that this palette is sufficient for the bounded receiving question: 97%.**

### BridgeMatrix

- **T1 ↔ T2 — complementary, not substitutable; 100%.** Both persist state, but T1’s session/knowledge substrate supports selective semantic retrieval while T2’s event history supports recovery and command replay. Loss if merged: “memory” obscures two different guarantees.
- **T1 ↔ T3 — overlapping; 98%.** A hybrid graph can host model-directed work with checkpoints, but checkpointing does not make the model’s reasoning deterministic. Loss if merged: durable agent execution is mistaken for reproducible inference.
- **T2 ↔ T3 — partially aligned with a material disagreement; 100%.** Both support durable state and bounded tasks, but replay entry points and in-flight code-version behavior differ. Loss if substituted: an engine migration silently changes recovery semantics.
- **T1/T2/T3 ↔ T4 — assurance bridge; 99%.** Versioned prompts, environments, datasets, graders, and traces make agent and workflow runs comparable. Loss if omitted: a run can be recovered operationally but not reconstructed epistemically.
- **T1/T2/T3 ↔ T5 — authority bridge; 100%.** Context selection and workflow inputs do not themselves restrict resource access; explicit grants and credential isolation do. Loss if omitted: prompt instructions are treated as a security boundary.
- **All execution traditions ↔ T6 — evidence bridge; 99%.** Campaign, trace, activity, entity, and derivation identifiers connect results without sharing full internal context. Loss if omitted: cross-plane logs remain adjacent but causally ambiguous.

No pair is asserted to be a complete substitute. The candidate composition later in the report therefore carries explicit source union, alignment, and losses rather than silently fusing the traditions.

### ClaimSheets

#### T1 — Long-horizon agent harness and context engineering

- **CS-T1-01 — Open-ended work and predefined work need different control structures — 99%.** Workflows follow predefined code paths; agents dynamically direct their processes and tool use. Agents are suitable when steps cannot be hardcoded, while workflows provide predictability for well-defined tasks. Evidence: S02, “What are agents?” and “When to use agents.”
- **CS-T1-02 — Broad context must still be curated — 98%.** Long context is a finite attention resource; adding tokens can reduce focus, and controlled research shows positional and length-related degradation. “Shared memory” should therefore mean a recoverable source that can be selectively retrieved, not an instruction to inject all history into every inference. Evidence: S03 and S17.
- **CS-T1-03 — Durable session history should live outside the model context — 98%.** A current long-horizon architecture separates an append-only session log from the harness and sandbox, lets replacement harnesses recover from the log, and selects slices for inference. Evidence: S04, especially “Recovering from harness failure” and “The session is not Claude’s context window.”
- **CS-T1-04 — Long-running work benefits from structured handoff artifacts, not transcript dependence — 96%.** Current harness reports use progress records, version control, clean state, and explicit next steps across fresh contexts; compaction alone can lose critical state. Evidence: S04 and S05.

#### T2 — Deterministic durable workflow orchestration

- **CS-T2-01 — Replayable orchestration requires deterministic control flow — 100%.** Given the same recorded input and history, workflow code must issue the same commands in the same sequence. Time, randomness, network calls, database calls, and LLM calls belong in activities/tasks whose results are recorded. Evidence: S06 and S08.
- **CS-T2-02 — A durable workflow cannot literally have “no memory” — 100%.** Recovery and replay depend on explicit run-local state, checkpoints, and/or an event history. What can be prohibited is implicit cross-run semantic memory and unversioned ambient context. Evidence: S07, S08, and S09.
- **CS-T2-03 — Side-effecting tasks need retry and idempotency semantics — 99%.** Activity/task retries can repeat execution after partial failure; side effects therefore require idempotency keys, recorded outcomes, or precondition checks. Evidence: S06 and S09.
- **CS-T2-04 — Workflow code and prompt changes are versioned operational events — 99%.** A code change can break replay for in-flight runs; safe systems pin or route compatible versions. The exact mechanism differs across engines, so it must be part of the selected engine contract. Evidence: S06, S08, and S10.

#### T3 — Hybrid agent graph runtime

- **CS-T3-01 — Agentic and deterministic components can share one durable runtime without becoming the same kind of work — 98%.** LangGraph exposes deterministic entry/task sequencing, checkpointed results, resumable threads, and model-driven nodes. This supports composition, not semantic collapse. Evidence: S09.
- **CS-T3-02 — “Durable” does not imply one universal replay/versioning model — 100%.** Temporal-style engines compare commands with recorded event history and support worker/patch versioning; LangGraph’s Graph API resumes at node boundaries and applies the latest deployed graph to existing threads. Evidence: S06 and S10.

#### T4 — LLMOps and evaluation lifecycle

- **CS-T4-01 — A stable system prompt should be an immutable referenced version, not a mutable string — 100%.** Prompt-registry practice creates a new immutable version for every change and retains metadata and diffs for reproducibility and lineage. Evidence: S11.
- **CS-T4-02 — Reconstructible evaluation needs more than a prompt and score — 99%.** It needs a task input, trial identity, harness, tools, environment, transcript/trace, outcome, grader versions, and repeated trials where model variance matters. Evidence: S12.
- **CS-T4-03 — Evaluation execution should be isolated from generator scratch context when independence matters — 96%.** Current harness evidence reports systematic self-evaluation leniency and improved results from a separately prompted evaluator; stable agent evaluation also requires controlled environments and outcome checks. This supports separate evaluator context, but not necessarily a separate product or model. Evidence: S05 and S12.

#### T5 — Zero-trust and capability security

- **CS-T5-01 — Tool and data access should be granted per run at the narrowest practical resource and operation scope — 100%.** This follows MCP’s least-privilege scope guidance and NIST’s resource-centric zero-trust model. Evidence: S13 and S14.
- **CS-T5-02 — Credential isolation is stronger than prompt-only prohibitions — 99%.** A current managed-agent design keeps tokens outside generated-code sandboxes and proxies authorized calls. Context allowlisting should be paired with an execution and credential boundary; prompt text is not that boundary. Evidence: S04, “The security boundary,” plus S13–S14.

#### T6 — Provenance and distributed observability

- **CS-T6-01 — Logs alone are not sufficient provenance — 98%.** Provenance must relate inputs/entities, activities/runs, responsible agents, outputs, and derivations; operational tracing must also propagate causal identity across service boundaries. Evidence: S15 and S16.
- **CS-T6-02 — One campaign identity should connect Codex authoring, workflow execution, artifacts, and evaluation — 99%.** A propagated trace/campaign ID plus immutable artifact and source identifiers allows cross-plane reconstruction without exposing the entire broad-context session to the narrow executor. Evidence: S15–S16, aligned with S04’s external session identity.

### Main difference: broad-context agent plane versus bounded workflow plane

The primary difference is **who controls the next step and from what admitted state**, not whether an LLM is present.

- The **broad-context agent plane** lets the model choose searches, tools, decompositions, and revisions as understanding changes. Its durable substrate is recoverable project knowledge plus an external session/event log. It optimizes semantic coherence and adaptation. Exact replay is generally not its primary guarantee.
- The **bounded workflow plane** follows a declared graph and versioned contract. Its state is explicit run-local workflow state; nondeterministic work is isolated in recorded activities. It optimizes repeatability, recovery, constrained authority, and auditable side effects.
- A workflow activity may call an LLM or coding agent. That makes the activity nondeterministic, not the orchestration control path. Its inputs, grants, configuration, outputs, and evidence still remain bounded and recorded.

**Confidence: 100%.** This distinction is independently supported by S02, S06–S10.

### Two-axis correction to the proposed process split

The operator-confirmed routing unit is **content role plus operation**:

1. **Content-role coordinate.** This determines what kind of meaning is being handled and what the result is allowed to establish. CAO carries concern, analysis, planning, and observed work context; RMED carries accepted specification authority; Implementation carries encoded realization; Ops carries observed outcomes. A workflow result cannot silently cross from evidence or realization into RMED authority.
2. **Operation coordinate.** This determines how the work should run. Discovering, interpreting, synthesizing, reconciling, or deciding normally needs broad context. Rendering, mechanically validating, executing a declared transformation, running a fixed test, recording a receipt, or persisting through an already governed writer can normally be bounded and replayable.

The same content role can therefore route differently according to the operation:

- **CAO × discover/interpret/coordinate:** broad-context Codex work. **Confidence: 98%.**
- **CAO × validate carrier/register evidence:** bounded workflow work. **Confidence: 98%.**
- **RMED × author/reconcile authority:** broad-context Codex plus operator-governed work. **Confidence: 99%.**
- **RMED × check schema/ID/H1/relations:** bounded deterministic workflow work. **Confidence: 100%.**
- **Implementation × design or resolve an ambiguous change:** broad-context or bounded-agent work, depending on the declared frontier. **Confidence: 99%.**
- **Implementation × apply a complete transformation contract:** bounded workflow activity. **Confidence: 98%.**
- **Evaluation × design criteria or interpret conflicting evidence:** broad-context work. **Confidence: 99%.**
- **Evaluation × execute fixed tests or graders:** bounded isolated workflow work. **Confidence: 100%.**
- **Ops × interpret consequences or decide corrective direction:** broad-context work. **Confidence: 98%.**
- **Ops × capture a timestamped receipt or measurement:** bounded workflow work. **Confidence: 100%.**

The routing classifier is therefore:

1. What is the content role, and what semantic authority may its result carry?
2. What operation is being performed on or for that role?
3. Is the goal and success criterion fully declared?
4. Can the next-step graph be fixed before execution?
5. Can admitted inputs and tool grants be enumerated?
6. Can side effects be made idempotent or committed through a governed boundary?
7. Is the required judgment local, or does it require project-wide semantic reconciliation?

After preserving the content-role authority boundary, prefer a bounded workflow when questions 3–6 are yes and question 7 is local. Otherwise keep the operation in the broad-context agent plane or invoke a bounded agent activity whose evidence returns for broad-context interpretation. **Confidence: 99%.**

### Candidate cross-tradition synthesis record `G2F-01`

This is a candidate architecture for later challenge, not an accepted CAPRMEDIO design:

```text
Codex authoring and governance plane
  broad project context + external session log + operator interaction
                 |
                 | immutable Task Envelope
                 v
Workflow control plane
  versioned graph + explicit run state + retry/recovery + trace identity
                 |
                 | allowlisted Activities
                 v
Isolated execution planes
  deterministic tools | bounded coding agent | test/eval sandbox
                 |
                 | immutable Result Envelope + artifacts + evidence
                 v
Codex interpretation / governed CAPRMEDIO persistence
```

**Provenance union.** T1 mechanisms come from S02–S05 and S17; T2/T3 mechanisms from S06–S10; prompt/evaluation controls from S11–S12; grants from S13–S14; causal and derivation identity from S15–S16.

**Explicit alignment.** An external agent session log and a workflow event history are both durable records, but they are not substitutes. The session log preserves semantically useful interaction history for selective retrieval; the workflow history preserves the exact state transitions and activity results required for recovery/replay. A campaign ID may bridge them while access policy prevents the workflow from reading the entire session.

**Accepted losses and cautions.** Cross-plane handoffs add serialization, version management, infrastructure, and latency. Bounded context can omit a necessary dependency. A workflow can create false confidence if a nondeterministic activity is called “deterministic.” A broad agent can undermine project integrity if it can bypass governed writers. No source supports automatic promotion of an agent result into RMED authority.

**Confidence in viability: 97%. Confidence that this is the best CAPRMEDIO architecture: 86%; selection remains open.**

### Minimum handoff architecture

The narrow executor should receive an immutable **Task Envelope**, not a transcript dump:

- campaign, task, parent-run, and idempotency identifiers;
- work-class and expected side-effect class;
- exact target artifact/source revisions and content digests;
- prompt, model, harness, workflow, tool, and grader version references;
- allowlisted input manifest and explicit denied/ambient-context policy;
- least-privilege tool/resource grants with expiry;
- environment/container/build digest and dependency lock references;
- acceptance criteria and deterministic checks;
- time, token, cost, retry, and concurrency budgets;
- required output schema, evidence schema, and escalation conditions;
- operator approval or governed-change token where authority requires it.

It should return an immutable **Result Envelope**:

- terminal status and failure classification;
- output/artifact locations and digests;
- actual prompt/model/harness/tool/environment versions;
- activity, retry, and side-effect receipts;
- test/grader results with exact criteria versions;
- trace/span IDs and provenance links;
- context manifest actually consumed;
- deviations, unresolved findings, and escalation request;
- no claim of RMED authority unless a separate governed persistence step accepts it.

**Purpose: 99% confidence.** The envelopes isolate the work while preserving enough identity to reconstruct and interpret it. They are also the main defense against stale or hidden context.

### OperatorAndObjectInventory — downstream stubs

The following are candidate objects, not yet lawful CAPRMEDIO types or thresholds: `WorkClass`, `ContextPolicy`, `MemoryPolicy`, `TaskEnvelope`, `ResultEnvelope`, `InputManifest`, `PromptVersionRef`, `ModelVersionRef`, `HarnessVersionRef`, `WorkflowVersionRef`, `ToolGrant`, `EnvironmentDigest`, `AcceptanceCriteriaRef`, `GraderVersionRef`, `IdempotencyKey`, `CampaignId`, `RunId`, `TraceId`, `ArtifactDigest`, `SideEffectReceipt`, `EscalationReason`, and `RetentionPolicyRef`.

Candidate operators are: classify work; freeze admitted inputs; issue grants; start/resume/cancel run; record activity result; validate envelope; compare artifact to acceptance criteria; emit evidence; escalate missing context; reconcile result into broad context; and request governed persistence. Their exact schemas, authority, and acceptance rules remain to be authored downstream.

### Entity-of-concern map

- **Work classification decision:** the CAPRMEDIO work-execution architecture; supported by CS-T1-01, CS-T2-01, and CS-T3-01.
- **Agent session and retrieval:** the Codex authoring/governance plane; supported by CS-T1-02 through CS-T1-04.
- **Workflow run and activities:** the workflow control and isolated execution planes; supported by CS-T2-01 through CS-T3-02.
- **Prompt, eval, and result evidence:** the assurance surface; supported by CS-T4-01 through CS-T4-03.
- **Tool grants and credentials:** the security boundary; supported by CS-T5-01 and CS-T5-02.
- **Campaign, trace, and derivation links:** the cross-plane evidence surface; supported by CS-T6-01 and CS-T6-02.

### Worked micro-examples

1. **Adaptive semantic work, heterogeneous case A:** a new RMED Requirement is proposed from several conflicting Concerns and existing authority. Codex retrieves the relevant graph frontier, compares ownership, asks the operator where needed, and drafts a candidate. Only the final carrier validation and governed write are narrow steps. Evidence anchors: S02–S04. Assurance basis: argument and trace review (TA/LA).
2. **Adaptive semantic work, heterogeneous case B:** a CAO Analysis interprets test failures that could indicate a bad implementation, an inadequate Evaluation, or an incorrect Requirement. The workflow returns bounded evidence; Codex performs the cross-role interpretation. Evidence anchors: S02, S05, S12. Assurance basis: argument plus independent evidence review (TA/VA).
3. **Durable bounded work, heterogeneous case A:** a validator receives exact Atom digests and a schema version, runs deterministic checks, and returns a signed result. Retry is safe because it has no mutation. Evidence anchors: S06–S09. Assurance basis: deterministic verification (VA).
4. **Durable bounded work, heterogeneous case B:** a bounded patch activity runs in a sandbox. The workflow records the input commit, prompt/harness/model versions, tool grants, patch digest, and tests. The LLM output is not replay-deterministic, but the workflow state and evidence are recoverable. Evidence anchors: S06–S09, S11. Assurance basis: test and provenance verification (VA/LA).
5. **Independent assurance, heterogeneous case A:** a coding generator cannot see hidden regression tests; a separately scoped evaluator receives the output artifact and test environment, not the generator’s scratch transcript, and reports outcome plus trace. Evidence anchors: S05 and S12. Assurance basis: independent evaluation (VA).
6. **Independent assurance, heterogeneous case B:** a delivery check needs a remote credential. The sandbox receives no token; a proxy grants only the named operation and records its receipt. Evidence anchors: S04, S13, S14. Assurance basis: access-control and log evidence (VA/LA).

### Purpose, benefits, drawbacks, cost, and latency

**Purpose.** The split is valuable when it prevents exploratory semantic context from becoming ambient execution authority, while letting mechanical work be recovered and independently checked. It is not valuable merely as a technology boundary.

**Benefits — 97–100% confidence:** smaller blast radius; reproducible mechanical checks; independent evaluation; explicit prompt/input/tool provenance; recoverable runs; clearer escalation when context is insufficient; and protection of RMED integrity through a separate governed write boundary.

**Drawbacks — 96–100% confidence:** two state models must be kept distinct; envelopes and version registries add authoring burden; stale or underspecified envelopes can produce locally correct but globally wrong work; nondeterministic activities cannot be made deterministic by orchestration; in-flight version compatibility must be managed; and cross-plane debugging requires correlated traces.

**Cost and latency — 95% confidence on direction, below 95% on CAPRMEDIO magnitude.** Agents trade cost and latency for flexibility; context resets, planner/evaluator calls, and additional harness layers add token and wall-clock overhead (S02, S05). Workflow infrastructure adds state storage, workers, queues, sandboxes, observability, registry maintenance, and operational support. Narrow contexts and smaller models can reduce per-step inference cost, while durable retry can avoid repeating completed work. Decoupling inference from lazily provisioned sandboxes reduced Anthropic’s reported p50 time-to-first-token by roughly 60% and p95 by over 90% in its Managed Agents architecture, but that first-party result cannot be transferred numerically to CAPRMEDIO (S04).

### Disagreements, exclusions, and insufficient bases

1. **“No memory” versus durable state.** Rejected as written with 100% confidence. Use “no implicit cross-run semantic memory; only declared run-local state, recorded activity results, and explicitly referenced artifacts.”
2. **One workflow replay model.** Rejected with 100% confidence. Temporal-style command replay and LangGraph node-boundary/latest-graph behavior differ materially.
3. **Implementation is narrow.** Rejected as a universal claim with 99% confidence. Implementation ranges from deterministic generation to open-ended agent work.
4. **More shared context is always better.** Rejected with 98% confidence. Context must be recoverable but selectively admitted.
5. **A separate evaluator is always worth its cost.** Insufficient basis. Current evidence supports it near capability or judgment boundaries, not for every deterministic check.
6. **One workflow engine is already selected.** Excluded. The corpus establishes mechanism families, not a product choice.
7. **Workflow output may directly update RMED.** Unsupported and contrary to the stated project-integrity objective. The architecture needs an explicit governed persistence boundary.

### Receiving use and return condition

The harvest supports proceeding to a design challenge with a corrected hypothesis:

> Route work by **`(content role, operation)`**. Use the content role to preserve meaning, authority, and required evidence; use the operation to select context breadth and execution control. Keep open-ended, judgment-heavy, project-wide semantic operations in a broad-context Codex authoring/governance plane. Execute contracted, replayable, least-privilege operations through a durable workflow control plane. Allow bounded agent activities inside workflows when an operation remains nondeterministic. Keep shared knowledge and session history external and selectively retrieved; give narrow runs no ambient cross-run semantic memory. Return every result through immutable evidence envelopes, and preserve project integrity through a separate governed CAPRMEDIO persistence step.

**Confidence that this is the right hypothesis to challenge next: 98%.** Return to the harvest when a selected engine changes replay/version semantics, a new agent-memory architecture changes the context boundary, security policy changes the grant model, or CAPRMEDIO supplies measured run data that contradicts the work classifier.

## Open questions (confidence <95%)

1. **Which exact `(content role, operation)` pairs belong in each plane? — the two-axis rule is accepted, but its complete routing matrix is not yet populated; 92%.** Missing evidence: a representative inventory of CAO, RMED, Implementation, Evaluation, and Ops operations, including where humans changed direction. Consequence: routing by either coordinate alone could violate authority or give an operation the wrong context posture. Next action: sample at least ten recent runs, record both coordinates for every step, and classify them using the seven-question classifier above.
2. **Which workflow engine and deployment model fit CAPRMEDIO? — no selection; 82%.** Missing evidence: required languages, local/cloud boundary, persistence store, concurrency, human approval, licensing, privacy, operating budget, and in-flight version behavior. Consequence: Temporal, Durable Task, LangGraph, and a smaller project-owned runner impose different operational and replay semantics. Next action: define a decision frame, then prototype one identical validation-plus-bounded-agent workflow in the two strongest candidates.
3. **How much semantic validation can be isolated? — likely a mechanical/semantic split; 92%.** Missing evidence: an authoritative catalog of current validators and which judgments require project-wide ownership or intent. Consequence: treating semantic review as a deterministic check could protect syntax while damaging meaning. Next action: label each current validator as mechanical, bounded-semantic, or project-semantic and record its admitted evidence.
4. **What level of replay is required for LLM activities? — configuration-and-evidence replay is likely sufficient, not bit-identical output; 90%.** Missing evidence: CAPRMEDIO’s assurance requirement for model/provider nondeterminism and model retirement. Consequence: an impossible bitwise-replay promise would misstate assurance; too weak a policy would make comparisons irreconstructible. Next action: define replay levels for orchestration, activity inputs, provider/model configuration, recorded output, and full re-execution.
5. **What may enter shared long-term memory? — unresolved; 87%.** Missing evidence: retention, privacy, deletion, correction, authority, and stale-memory policy. Consequence: ungoverned memory can leak sensitive or obsolete claims into new work. Next action: define separate stores for authoritative project artifacts, append-only session events, derived summaries, and user preferences, each with provenance and retention rules.
6. **What is the CAPRMEDIO cost/latency break-even point? — unknown; 72%.** Missing evidence: baseline token use, setup time, failure/retry rates, operator wait time, and infrastructure cost for current tasks. Consequence: the architecture could add more overhead than reliability value for short or low-risk work. Next action: benchmark a broad Codex-only baseline against the same tasks using frozen envelopes and isolated execution; measure wall time, tokens, retries, operator interventions, and defect escape.
7. **How should envelopes and provenance map into CAPRMEDIO Atoms and Journals? — likely reuse existing campaign/work/evidence carriers rather than create a parallel ontology; 89%.** Missing evidence: a narrow authority scan of current Tool, Journal, Ops, Evaluation, and commit-receipt contracts. Consequence: inventing a second provenance model would threaten project integrity and duplicate authority. Next action: perform an applicability scan over the live carriers before authoring any new RMED.
8. **Who may authorize the final governed write? — operator or already-authorized deterministic Tool, but exact policy unresolved; 93%.** Missing evidence: the current authority boundary for creating/activating RMED and for automatic low-risk repairs. Consequence: letting the workflow mutate authoritative Atoms directly would collapse evidence into authority. Next action: pin the existing governed-change and commit contracts, then define which result classes can be auto-applied, proposed, or must stop for operator approval.

## Skills used

- `$fpf sota harvest` — selected directly from the user-approved plan and used to produce the bounded corpus, claim sheets, tradition palette, explicit bridge, disagreements, and receiving handoff.

#### FPF sources consulted (1 read; 1 used)

- `G_Discipline SoTA Patterns Kit/03_02_SoTA Harvester & Synthesis/00_G.02 - SoTA Harvester & Synthesis.md` — used as the direct governing pattern; revision and claim regions pinned above.
