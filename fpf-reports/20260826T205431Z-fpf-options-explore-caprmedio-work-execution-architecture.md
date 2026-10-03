## Task, scope, and boundaries

:codex-annotation{index="1"}

**Selected call.** `$fpf options explore` was executed to generate and compare plural CAPRMEDIO work-execution architectures using the completed SoTA harvest. The operator's latest correction is authoritative for this exploration: routing is determined by **`(content role, operation)`**. Content role determines meaning, authority, and evidence posture; operation determines context breadth, execution control, isolation, and replay posture. **Confidence: 100%.**

**Exploration contract (`WEA-OE-2026-08-27-v1`).** The target is a future architecture for CAO, RMED, Implementation, Evaluation, and Ops operations across Codex, durable workflow control, deterministic Tools, bounded agent activities, memory/session logs, evaluation, provenance, and governed persistence. A candidate is interesting only if it materially changes at least one of these axes: control locus, state topology, agent placement, authority topology, evaluation topology, or adoption path. Renaming the same two-plane design or substituting one workflow product for another does not count as a distinct architecture. The generation budget is six steady-state mechanism families plus one separately evaluated adoption overlay. The admissible-risk budget permits unproven cost or implementation complexity when declared, but permits no candidate to silently promote evidence, implementation, evaluation, or Ops results into RMED authority. **Confidence that this contract matches the request: 99%.**

**Protected constraints — eligibility, not trade-off coordinates.** Every eligible target architecture must:

1. route by the explicit pair `(content role, operation)` rather than by phase name alone;
2. preserve content-role authority, especially the separation between produced evidence and admitted RMED authority;
3. keep broad semantic session history distinct from workflow event history and admit context selectively;
4. give bounded runs explicit run-local state, versioned inputs, and least-privilege capabilities rather than ambient memory or credentials;
5. correlate inputs, activities, agents, outputs, evaluations, and writes through immutable task/result identities and provenance;
6. make side effects idempotent, previewable, or mediated by an already governed writer; and
7. retain an operator-governed stop when required context, authority, or acceptance criteria are missing.

These constraints are supported by predecessor source families T1–T6, particularly S03–S04, S06–S09, and S13–S16. They also preserve the already-established CAPRMEDIO boundary that Graph/UI surfaces remain read-only while mutations go through governed preview/dry-run Tools. **Confidence: 98%.**

**Declared comparison coordinates.** No weights or scalar total are assigned. Each candidate is compared on: semantic adequacy; project integrity; determinism and recovery; security; observability and provenance; cost and latency; implementation and operating burden; and reversibility/evolvability. Ratings are ordinal and explanatory: `strong`, `favorable`, `mixed`, `weak`, or `unknown`; for burden, `low`, `medium`, `high`, or `very high`. A rating is not a measured benchmark. **Confidence that these coordinates cover the operator's requested concerns: 100%.**

**Resolved FPF sources.** Candidate generation follows `B.5.2.1 — Creative Abduction with NQD`: generate mechanism-distinct hypotheses, preserve provenance and plurality, evaluate on declared coordinates, and do not collapse the set to one winner. Comparison follows `G.9 — Parity and Benchmark Harness`: pin the baseline and evidence window, declare equal conditions before comparison, keep telemetry separate from decision coordinates, and preserve a partial order when evidence does not justify aggregation. Both were generated from FPF source revision `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef` on 2026-08-26. **Confidence: 100%.**

**Evidence and carrier frontier.** The immediate predecessor is [the SoTA harvest](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/fpf-reports/20260826T202459Z-fpf-sota-harvest-broad-context-agent-narrow-workflow.md), SHA-256 `921bd5cb5cd22f66616e1ec7e5091313920eb8af6f8575784f0cb0cba5cceefe`, currently untracked in the live checkout. It contains seventeen included sources across long-horizon agent harnesses, durable workflows, hybrid agent runtimes, LLMOps/evaluation, zero-trust security, and provenance/observability, fresh through 2026-08-27. The repository carrier revision observed for this report is `999b7712362b338a69aeda6536c43938837219ec`; the worktree contains unrelated concurrent changes, which this exploration does not modify. The live FPF toolkit checkout is `18d0c5bc8ace1cf5d99e4af2796694dd1de16ece`; the two used generated source files pin the upstream revision above. **Confidence in these carrier readings: 100%.**

**Campaign handoff.** The report-local campaign ID is `CAPRMEDIO-WEA-2026-08-27`. Its current semantic frontier is `SF-02: route by (content role, operation)`; this supersedes the initial phase-labelled broad/narrow hypothesis, and the predecessor report already incorporates that correction. No further meaning change is introduced here. The evaluation profile is `desk-evidence-architecture-v1`; it excludes implementation proof, engine benchmarks, measured CAPRMEDIO cost/latency, and runtime parity. The predecessor is the pinned SoTA report above. The decision owner is the operator. The current phase is candidate exploration; allowed next transitions are evidence recovery or a separately authorized `$fpf decision synthesize`. No RMED, implementation, workflow-engine, or persistence decision is made. Open finding fingerprints carried forward are `WEA-GAP-01/routing-matrix`, `WEA-GAP-02/engine-deployment`, `WEA-GAP-03/semantic-validation-split`, `WEA-GAP-04/replay-level`, `WEA-GAP-05/memory-policy`, `WEA-GAP-06/cost-latency`, `WEA-GAP-07/envelope-provenance`, and `WEA-GAP-08/write-authority`; all remain `OPEN`. **Confidence: 100%.**

**Saved report:** `fpf-reports/20260826T205431Z-fpf-options-explore-caprmedio-work-execution-architecture.md`

## High-confidence results (>=95%)

### CandidateSet and provenance

The baseline and candidates are mechanism families, not commitments to products. Their source tags refer to the predecessor's `S01`–`S17` corpus and `T1`–`T6` traditions.

**`B0 — Codex-centred assisted coordination` (comparison baseline, not an asserted complete current implementation).** A broad Codex session retrieves project knowledge, chooses steps, and invokes deterministic Tools or tests directly. Continuity primarily comes from shared project artifacts, session history, and human coordination. This baseline represents the architecture that the proposed split is trying to improve; it does not claim that every listed control is absent from the live project. Provenance: operator problem statement, T1, and the project's existing governed-Tool direction. **Confidence in usefulness as a baseline: 97%.**

**`O1 — Hard-contract two-plane split`.** Codex performs all discovery, interpretation, reconciliation, planning, and authority-bearing authoring. A durable workflow executes only completely contracted deterministic operations. It cannot invoke a coding or reasoning agent; missing semantics always return to Codex. Inputs and results cross the boundary through immutable envelopes, and only a governed writer may persist accepted effects. Provenance: T1 + T2 + T5 + T6; this is the strongest literal separation of adaptive and predetermined control. **Confidence in architectural viability: 98%.**

**`O2 — Durable hybrid with bounded agent activities`.** Codex remains the broad authoring/governance plane, while a durable workflow owns retries, checkpoints, approvals, and causal identity. The workflow may invoke deterministic Tools, test sandboxes, or nondeterministic bounded coding/evaluation agents whose inputs, grants, configuration, outputs, and evidence are recorded. Results return to Codex or a governed writer; agent output never becomes authority by itself. Provenance: predecessor synthesis `G2F-01`, T1–T6, especially S06–S16. **Confidence in architectural viability: 98%.**

**`O3 — Policy-compiled execution kernel`.** A central policy compiler receives `(content role, operation)` plus target frontier, risk, authority, success criteria, and side-effect class. It compiles a minimal `ExecutionContract`: route to Codex, deterministic Tool, durable workflow, bounded agent, evaluator, or human gate; admit only named context and capabilities; require the appropriate evidence and writer. A workflow engine is one backend rather than the universal control plane. Provenance: the operator-confirmed two-axis classifier combined with T4–T6; this is a new synthesis rather than a direct source recommendation. **Confidence in architectural viability: 96%.**

**`O4 — Content-role-owned execution mesh`.** CAO, RMED, Implementation, Evaluation, and Ops each have a stewarded execution service or adapter with role-specific contracts, context policy, validators, and evidence rules. A thin pair router delegates an operation to the owning role service; cross-role work uses explicit producer/consumer envelopes. RMED retains one governed admission boundary even if other services are distributed. Provenance: content-role authority plus service and producer/consumer mechanisms; it is not directly prescribed by the SoTA corpus. **Confidence in architectural viability with a single authority registry: 95%.**

**`O5 — Provenance-log-centred execution backbone`.** An immutable campaign/event log and content-addressed artifact store become the coordination spine. Broad Codex sessions, workflows, Tools, bounded agents, evaluators, and governed writers consume admitted views and append typed events. Workflow replay history and semantic session events remain distinct event classes even when stored on the same infrastructure. Executors can be replaced and recover from the log without receiving an ambient transcript. Provenance: T1 session-log mechanisms, T2 event sourcing, and T6 provenance/trace correlation. **Confidence in architectural viability: 97%.**

**`O6 — Dual-control assurance pipeline`.** Codex or a bounded generator produces a candidate artifact; a separately scoped evaluator receives the artifact, declared criteria, and controlled environment but not generator scratch context; a policy gate checks evidence and authority before any governed writer can act. Deterministic checks may satisfy the evaluator role without an LLM. Provenance: T4 independent evaluation, T5 least privilege, T6 traceable evidence, and CAPRMEDIO's integrity requirement. **Confidence in architectural viability for high-risk operations: 98%.** Universal application to every operation is not asserted and remains an open question below.

**`A1 — Progressive pair-cell migration` (adoption overlay, not a peer steady-state architecture).** Keep broad work in Codex, first envelope existing deterministic validation, testing, receipts, and governed commits, then move individual `(content role, operation)` cells only after their contracts and failure behavior are proven. `A1` can be applied to O1–O6 and is therefore excluded from the steady-state Pareto comparison. Provenance: the predecessor's unresolved routing matrix and engine choice, plus reversibility discipline. **Confidence that it is correctly treated as an overlay: 99%.**

### Diversity map

The generated set is materially diverse along the declared mechanism axes:

- **`O1`:** workflow-centred control; separate session/workflow state; no agent inside workflow; central governed writer; evaluation only when explicitly called.
- **`O2`:** workflow-centred durable control; separate but correlated state; bounded agents inside activities; central governed writer; mixed deterministic and independent evaluation.
- **`O3`:** policy-centred control; contracts compiled per pair and risk; plural execution backends; central authority registry; evaluation selected by policy.
- **`O4`:** role-centred control; distributed role state and services; agents or Tools owned by role; federated execution with one RMED admission boundary.
- **`O5`:** log-centred control and recovery; typed shared infrastructure with logically separated histories; replaceable executors; provenance is the primary integration surface.
- **`O6`:** assurance-centred control; generator and evaluator contexts separated; writes require two-stage evidence and policy admission.

The set covers all declared control, state, agent-placement, authority, and evaluation topologies. Further generation stopped because additional candidates either changed only a product, combined existing candidates, or expressed an adoption sequence already captured by `A1`. No numerical novelty score was promoted into a decision coordinate. **Confidence that the finite set has reached qualitative diversity saturation for this question: 96%.**

### ParityPlan `WEA-PP-01`

**Comparison subjects.** `B0` is the exact conceptual baseline; `O1`–`O6` are comparators. `A1` is evaluated separately as an adoption overlay. The comparison does not imply that `B0` is the complete live architecture or that any comparator is implemented. **Confidence: 100%.**

**Pinned evaluation profile.** `desk-evidence-architecture-v1`, with evidence fresh through 2026-08-27, predecessor digest `921bd5...ceefe`, source set S01–S17, and the eight declared decision coordinates. Every candidate receives the same protected constraints, the same two-axis routing rule, the same authority boundary, and the same source corpus. No candidate receives assumed runtime performance or product-specific operational maturity. **Confidence: 100%.**

**Evidence classes.** `E1` is cross-lineage external evidence from standards and multiple implementations; `E2` is current first-party architecture evidence; `E3` is report-local mechanism inference; `E4` would be CAPRMEDIO runtime measurement, which is absent. Ratings below use E1–E3 and explicitly do not claim E4. Cost, latency, operating burden, and failure rate remain directional until measured. **Confidence: 100%.**

**Aggregation and freshness rules.** Protected-constraint failure makes a candidate ineligible regardless of other benefits. Eligible candidates remain partially ordered; there is no weighted sum, average, or winner. A future ParityReport must be rerun if the routing frontier, authority policy, engine candidates, deployment boundary, or measured task corpus changes. **Confidence: 100%.**

### ParityReport `WEA-PR-01` — desk evidence only

**Protected-gate result.** `B0` is not eligible as a target architecture unless immutable envelopes, least-privilege execution, causal provenance, and the governed-writer boundary are made explicit. `O1`, `O2`, `O3`, `O5`, and `O6` are eligible in principle. `O4` is eligible only if distributed role services share one authoritative pair-policy registry and cannot independently admit RMED. `A1` is eligible only as a transition policy and cannot excuse a protected-constraint violation in a migrated cell. **Confidence: 98%.**

#### `O1 — Hard-contract two-plane split`

- **Semantic adequacy: mixed.** It preserves broad judgment, but any underspecified operation must round-trip to Codex; it cannot finish bounded nondeterministic implementation work locally.
- **Project integrity: strong.** The execution boundary is simple and RMED admission remains visibly separate.
- **Determinism and recovery: strong.** Only contracted operations enter the durable plane, minimizing replay ambiguity.
- **Security: strong.** Its allowlist and no-inner-agent rule keep the execution surface small.
- **Observability and provenance: favorable.** Two planes and explicit envelopes are easy to correlate, though semantic reasoning remains less replayable.
- **Cost and latency: mixed.** Narrow tasks can be cheap, but semantic escalations and context re-entry add operator and wall-clock delay.
- **Implementation/operations burden: medium.** It needs a durable runner, envelope registry, grants, and writer integration, but avoids agent orchestration inside workflows.
- **Reversibility/evolvability: favorable.** The boundary is easy to reason about, but operations cannot migrate inward until fully deterministic.

**Assessment confidence: 97%.** Its key trade is maximum clarity and replay posture versus reduced local flexibility. Evidence basis: T1, T2, T5, T6; no runtime measurement.

#### `O2 — Durable hybrid with bounded agent activities`

- **Semantic adequacy: strong.** Bounded agents can handle locally ambiguous implementation or evaluation without giving the whole run ambient project context.
- **Project integrity: strong.** Envelopes, recorded activities, evaluator separation, and a governed writer preserve the authority boundary when correctly enforced.
- **Determinism and recovery: favorable.** Orchestration is recoverable; agent outputs are recorded but not inference-deterministic.
- **Security: favorable.** Capability-scoped sandboxes and credential isolation can be strong, but each agent activity expands the attack and data surface.
- **Observability and provenance: strong.** Activity boundaries naturally carry versions, consumed context, traces, retries, and artifacts.
- **Cost and latency: mixed.** It can avoid repeating completed work and reduce context per step, but orchestration, sandboxing, and evaluator calls add overhead.
- **Implementation/operations burden: high.** Durable state, workers, sandboxes, versioning, registries, and cross-plane debugging are all required.
- **Reversibility/evolvability: favorable.** Activity types can be introduced gradually, but in-flight workflow compatibility must be governed.

**Assessment confidence: 98%.** Its key trade is broad mechanism coverage versus infrastructure and policy complexity. Evidence basis: T1–T6; no CAPRMEDIO benchmark.

#### `O3 — Policy-compiled execution kernel`

- **Semantic adequacy: strong.** Routing can reflect both role and operation instead of forcing all work through one engine topology.
- **Project integrity: strong.** A single compiler can make authority, admitted context, required evidence, and writer class explicit before execution.
- **Determinism and recovery: favorable.** Compiled contracts are replayable when routed to durable backends; direct Codex routes remain intentionally non-replayable at reasoning level.
- **Security: strong.** Capabilities can be derived per contract rather than granted per host or session.
- **Observability and provenance: favorable.** Every route can share one contract identity, but heterogeneous backends need rigorous trace adapters.
- **Cost and latency: favorable in principle, unmeasured.** Simple operations can avoid a heavy workflow path; policy compilation and backend switching add fixed overhead.
- **Implementation/operations burden: high.** The policy language, compiler, conformance suite, backend adapters, and conflict resolution become critical infrastructure.
- **Reversibility/evolvability: strong.** Routes and backends can change per pair without rewriting the semantic model, provided policy versions remain compatible.

**Assessment confidence: 96%.** Its key trade is flexible, explicit routing versus central policy-compiler complexity and the risk of a new meta-system. Evidence basis: two-axis operator correction plus T4–T6; mainly E3 synthesis.

#### `O4 — Content-role-owned execution mesh`

- **Semantic adequacy: strong.** Each service can specialize context and checks for CAO, RMED, Implementation, Evaluation, or Ops.
- **Project integrity: mixed.** Local ownership is useful, but distributed policy can drift or accidentally create multiple authority boundaries.
- **Determinism and recovery: mixed.** Each service may recover well locally while cross-role transactions remain difficult.
- **Security: mixed.** Role-scoped grants reduce local breadth, but the number of trust and credential boundaries grows.
- **Observability and provenance: mixed.** Producer/consumer envelopes help; causal reconstruction across services requires mature correlation and schema governance.
- **Cost and latency: weak directionally.** Cross-service handoffs, duplicated infrastructure, and coordination add overhead before scale justifies them.
- **Implementation/operations burden: very high.** Each role needs contracts, ownership, deployment, versioning, and integration governance.
- **Reversibility/evolvability: mixed.** A role service can evolve independently, but contracts and distributed state can make topology changes expensive.

**Assessment confidence: 95%.** Its unique benefit is role-local stewardship; its principal risk is fragmenting project authority and infrastructure. Evidence basis: role authority plus E3 service synthesis; weak E4 basis.

#### `O5 — Provenance-log-centred execution backbone`

- **Semantic adequacy: favorable.** Codex can recover selected semantic history while executors receive typed admitted views; correctness depends on projection quality.
- **Project integrity: strong.** Append-only evidence and a separate governed writer make derivation and admission distinguishable.
- **Determinism and recovery: strong.** Recorded events and content-addressed artifacts support replacement, retry, audit, and reconstruction; workflow history must still retain its own replay semantics.
- **Security: mixed.** Per-consumer views can be narrow, but a central log becomes a sensitive high-value resource requiring field-level access and retention controls.
- **Observability and provenance: strong.** This is the candidate's defining advantage: campaign, trace, activity, artifact, evaluator, and write identities share one causal spine.
- **Cost and latency: mixed.** Reuse and recovery can reduce repeated work; durable ingestion, indexing, projection, and retention add storage and read-path cost.
- **Implementation/operations burden: very high.** Event schemas, migrations, projections, artifact storage, retention, privacy, and replay adapters must all be maintained.
- **Reversibility/evolvability: favorable.** Executors are replaceable, but event schemas become long-lived compatibility commitments.

**Assessment confidence: 97%.** Its key trade is best-in-set reconstruction and observability versus the heaviest data-governance substrate. Evidence basis: T1, T2, T6.

#### `O6 — Dual-control assurance pipeline`

- **Semantic adequacy: favorable.** Independent evaluation reduces generator blind spots, but an evaluator with an incomplete criterion can reject good work or certify the wrong thing.
- **Project integrity: strong.** No single generator or executor can both produce evidence and authorize its admission.
- **Determinism and recovery: favorable.** Deterministic graders replay well; LLM evaluators remain nondeterministic but are versioned and recorded.
- **Security: strong.** Generator, evaluator, and writer can receive distinct least-privilege grants and isolated context.
- **Observability and provenance: strong.** The architecture forces explicit links among task, candidate, criteria, evaluation, disposition, and write receipt.
- **Cost and latency: weak for low-risk work, favorable only where escaped defects are expensive.** Separate evaluation and gating add at least one stage.
- **Implementation/operations burden: high.** Criteria registries, evaluator environments, disposition policy, disagreement handling, and false-positive monitoring are required.
- **Reversibility/evolvability: favorable.** Assurance levels can vary by risk, but changing graders or criteria changes the evidence frontier and requires versioned comparison.

**Assessment confidence for high-risk use: 98%.** Its key trade is strongest separation of duties versus systematic extra cost and latency. Evidence basis: T4–T6.

### Partial order, crossings, and retained set

No candidate dominates across all declared coordinates:

- `O1` is stronger than `O2` on control simplicity and replay clarity, while `O2` is stronger on locally ambiguous implementation and evaluation work.
- `O2` is more directly supported as a composed durable architecture than `O3`; `O3` is more flexible and reversible across heterogeneous backends.
- `O3` centralizes policy consistency; `O4` maximizes role-local stewardship but pays in cross-role integrity and operating burden.
- `O5` is stronger than `O2` on reconstruction and replaceability, while `O2` has a simpler state and data-governance story.
- `O6` is stronger than `O2` for high-risk independent assurance, while `O2` avoids universal evaluator latency and can incorporate `O6` selectively.

The steady-state Pareto set is therefore retained as **`{O1, O2, O3, O5, O6}`**, with `O4` retained conditionally for a future in which independent role ownership or scale justifies its distributed burden. `A1` is retained as a compatible adoption overlay. This is a recoverable option set, not a ranking. **Confidence in the partial-order conclusion: 96%.**

### Common invariants and excluded families

The comparison reveals a common kernel that is required without selecting an architecture: pair-based classification; versioned Task and Result Envelopes; explicit run state; separation of session history from workflow replay history; least-privilege grants; content and configuration digests; causal campaign/trace identity; independent evaluation when the risk policy requires it; and a separately governed persistence boundary. These are protected constraints, not evidence that the candidates are equivalent. **Confidence: 98%.**

The following families are excluded:

- **`E1 — Everything in one broad Codex session`.** Excluded as a target when it lacks explicit contracts, least privilege, recovery, and governed persistence; adding those controls turns it toward O2 or O3. **Confidence: 99%.**
- **`E2 — Everything in a deterministic workflow`.** Excluded because project-wide interpretation, new authority reconciliation, and evaluation design cannot be reduced to a fixed graph merely by placing them in a workflow. **Confidence: 99%.**
- **`E3 — Durable workflow with no state or memory of any kind`.** Excluded as incoherent; durable recovery requires explicit run-local history, while the valid prohibition is against ambient cross-run semantic memory. **Confidence: 100%.**
- **`E4 — Workflow output directly becomes RMED`.** Excluded because it collapses evidence into authority and violates project integrity. **Confidence: 100%.**
- **`E5 — One weighted score chooses the architecture`.** Excluded because no admissible weights or empirical measurements exist and the options cross on protected qualities. **Confidence: 100%.**
- **`E6 — Select a workflow product now`.** Excluded because language, local/cloud boundary, persistence, concurrency, privacy, licensing, budget, and version semantics remain undeclared. **Confidence: 100%.**

### Stop condition and decision handoff

Generation stopped after all declared diversity axes were covered and further candidates became cosmetic recombinations or product substitutions. The desk parity report cannot select a final architecture because CAPRMEDIO runtime data, owner trade-off priorities, and engine/deployment constraints are absent. The decision frontier is therefore the retained set plus `O4` conditional and `A1` overlay. A final selection belongs in a separately authorized `$fpf decision synthesize`; before that, the highest-value evidence action is a parity run on representative `(content role, operation)` cells under identical envelopes and grants. **Confidence that stopping here is correct: 98%.**

## Open questions (confidence <95%)

1. **Which exact `(content role, operation)` cells should be moved first? — 92%, probable but unconfirmed.** Best current answer: start with high-frequency, low-semantic-ambiguity cells such as schema/ID/relation validation, fixed tests, receipts, and already-governed commits; keep authority reconciliation broad. Missing evidence: a representative inventory of recent work steps and human redirections. Consequence: the wrong first cells could produce a misleading success or harm meaning. Exact next action: sample at least ten recent CAO, RMED, Implementation, Evaluation, and Ops runs, label every step by both coordinates, and record its context and authority dependencies.

2. **Which retained architecture is best for CAPRMEDIO? — 88%, uncertain.** Best current answer: O2 is the most directly supported general composition, O1 is the safest minimal boundary, O3 is the most evolvable router, O5 is strongest for reconstruction, and O6 is strongest for high-risk assurance; this is not enough to choose. Missing evidence: operator priorities and matched runtime results. Consequence: choosing on conceptual attractiveness could overbuild infrastructure or underprotect integrity. Exact next action: declare must-have versus trade-off coordinates, then run `$fpf decision synthesize` only after the owner accepts the remaining evidence limits.

3. **Which workflow engine and deployment model fit the chosen mechanism? — 82%, uncertain.** Best current answer: keep the architecture engine-neutral until local/cloud, language, persistence, concurrency, human approval, privacy, licensing, and in-flight version requirements are fixed. Missing evidence: those constraints and a matched prototype. Consequence: an early product decision can silently determine replay and operating semantics. Exact next action: implement the same validation-plus-bounded-agent experiment in the two strongest engine families after the execution contract is frozen.

4. **How much semantic validation can be bounded? — 92%, probable but unconfirmed.** Best current answer: split mechanical checks, bounded-semantic checks, and project-semantic reconciliation; only the first class is deterministic by default. Missing evidence: an authoritative catalog of validators and their required evidence. Consequence: a syntactically valid result may still violate project meaning or ownership. Exact next action: classify every current validator into those three classes and pin the admitted frontier for each.

5. **What replay level is required for LLM activities? — 90%, probable but unconfirmed.** Best current answer: require exact orchestration replay plus reconstructible input, configuration, grants, recorded output, and evidence; do not promise bit-identical model output. Missing evidence: CAPRMEDIO assurance requirements for provider/model retirement and later re-execution. Consequence: an impossible promise misstates assurance, while a weak policy makes evidence incomparable. Exact next action: define replay levels for control flow, activity inputs, configuration, captured output, and fresh re-execution.

6. **What belongs in shared memory or the provenance log? — 87%, uncertain.** Best current answer: keep authoritative artifacts, append-only session events, derived summaries, workflow replay histories, and user preferences as distinct stores or typed namespaces with selective retrieval. Missing evidence: retention, privacy, deletion, correction, authority, and stale-memory policy. Consequence: a central log can become an authority-confused privacy and contamination surface. Exact next action: define ownership, provenance, retention, correction, and access rules for each store before O5 or broad shared-memory behavior is implemented.

7. **What is the cost/latency break-even for isolation and independent evaluation? — 72%, uncertain.** Best current answer: use stronger isolation and O6-style dual control in proportion to authority and defect cost, not universally. Missing evidence: baseline tokens, wall time, retries, operator interventions, infrastructure cost, and escaped defects for representative tasks. Consequence: the architecture may add more friction than reliability value for short or low-risk work. Exact next action: benchmark matched broad-only and envelope/workflow runs and record both operational telemetry and defect outcomes without folding telemetry into a single score.

8. **How should envelopes, campaign identity, and receipts map to existing CAPRMEDIO carriers? — 89%, uncertain.** Best current answer: reuse existing Tool, Journal, Plan/work, Evaluation, Ops, and commit-receipt authority where applicable instead of creating a parallel ontology. Missing evidence: a narrow applicability scan of the live carriers. Consequence: duplicate provenance concepts would damage project integrity and migration clarity. Exact next action: run an applicability scan over current authoritative carriers before proposing any new RMED Atom.

9. **Who can authorize the final governed write for each result class? — 93%, probable but unconfirmed.** Best current answer: the operator or an already-authorized deterministic Tool may admit only the exact result class covered by its contract; agent or evaluator output alone never authorizes a write. Missing evidence: the current authority matrix for creating, changing, activating, archiving, and auto-repairing Atoms. Consequence: an overbroad writer collapses the control planes at the most consequential boundary. Exact next action: pin the existing governed-change and commit contracts and classify every result as auto-applicable, proposal-only, or operator-stop.

## Skills used

- `$fpf options explore` — used to establish the exploration contract, generate mechanism-distinct candidates, preserve provenance, compare them under protected constraints and declared coordinates, retain a partial order, and stop without selecting an architecture.

#### FPF sources consulted (2 read; 2 used)

- `FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/04_05_Canonical Reasoning Cycle/02_Abductive Loop/02_B.05.02.01 - Creative Abduction with NQD.md` — used for plural hypothesis generation, novelty/quality/diversity discipline, declared coordinates, provenance, finite budget, and non-collapse to one winner.
- `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/10_09_Parity and Benchmark Harness/00_G.09 - Parity and Benchmark Harness.md` — used for the pinned ParityPlan/ParityReport, equal comparison conditions, freshness and evidence boundaries, partial ordering, and explicit exclusions.
