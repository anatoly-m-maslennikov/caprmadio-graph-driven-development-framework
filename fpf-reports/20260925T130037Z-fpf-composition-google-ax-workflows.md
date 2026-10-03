## Task, scope, and boundaries

### TL;DR

**Google AX is useful to us as an example of how to package, start, inspect, pause, and recover an isolated worker.** CAPRMEDIO already declares the workflow, authority, and evidence rules above that worker. AX could inform a local adapter or become an optional execution backend. [AX concepts][A1], [our orchestration contract][C1].

Four choices are worth keeping:

| Option | Concrete use | Main cost or condition |
|---|---|---|
| **O0 — Keep the current arrangement** | Continue existing execution and retain AX as a reference | Valid while no demonstrated execution need warrants another dependency |
| **O1 — Borrow ideas locally** | Inspectable execution recipes, checked capabilities, clear preparation/process/result states | Local adapter and metadata work; first check what already exists |
| **O2 — AX for evaluation jobs** | Run eligible Implementation or selected Release Readiness evaluations in an isolated remote worker | Cluster operation plus a reliable result bridge; benefits unmeasured |
| **O3 — AX for an Isolated agentic Step** | Source-conflict assessment or proposal that returns to our workflow and Operator | Same platform plus explicit input, conversation, and effect-safe recovery |

**The transferable ideas are stronger than a case for adopting the whole platform.** O1 has the smallest additional infrastructure surface among the change options. O2/O3 remain conditional: inspected default setup does not materialize MCP registries or download skills; readiness can survive setup failures; command exit is not returned to the control plane; and policy/governance features are incomplete or planned. File restoration also does not authorize replay of external effects. [Setup][A3], [runner][A4], [guide][A5], [schema][A2], [roadmap][A10].

This report makes **no adoption choice or implementation change**. It provides six sourced mechanisms, four distinct workflow options, their costs and assumptions, and the evidence needed for any later choice.

### Scope, baseline, and evidence

- **Receiving question:** what useful ideas in google/ax can serve CAPRMEDIO Tools, Apps, MCP, and workflows? Receiver and future decision owner: Anatoly.
- **AX source:** [commit e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7][PIN], committed 2026-09-25 06:31:22 UTC, retrieved and inspected 2026-09-25. GitHub's commit API identified the revision; its commit-addressed source archive was inspected. No AX installation, deployment, build, or tests were executed.
- **Local source:** inspected dirty-worktree bytes over HEAD a49a8d924f4cc6504fb2a8e5fbeabd8be0096fc1. Per-file SHA-256 pins below identify those bytes; HEAD alone does not. Current workflow and interface declarations are verified as source, not as a fully installed runtime. Before/after examples mean declared workflow → proposed execution arrangement.
- **Coverage:** bounded primary documentation, code paths, test assertions, current receiving contracts, and three named workflows. Inspected test expectations are not reported as passing test runs. This one-repository harvest does not establish field-wide SoTA, comparative superiority, production fitness, or measured savings.
- **Authority:** research and report delivery only. No analyzed project target, governing Atom, implementation, or workflow was changed; no software workload or external communication was executed. CA-A-904's earlier creation exception is not inherited.
- **Dependencies and outcome:** both approved analytical steps are complete and independently validated; this report consolidates their full results. No unresolved fact prevents completing the analysis. Direct-use options still require the operational evidence listed in G01–G05. The report uses the installed plain Markdown delivery setting.

Saved report: [fpf-reports/20260925T130037Z-fpf-composition-google-ax-workflows.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/fpf-reports/20260925T130037Z-fpf-composition-google-ax-workflows.md)

### Composition receipt

Exact invocation:

> https://github.com/google/ax
>
> [$fpf](/Users/am/.codex/skills/fpf/SKILL.md) plan sota harvest + how can we use it. our workflows?

Plan FPF-GOOGLE-AX-20260925-4e98a1d7 was approved by exact do. Requested and executed sequence: $fpf sota harvest → $fpf options explore. Both steps passed independent validation at attempt 1. Unexecuted suffix: none. Profile: none. Final analytical state: COMPLETE.

Typed edge result, sota-harvest → options-explore: PASS at the incoming basis gate. The full evidence map supported distinct options while retaining source limits and receiving constraints; STOP_NO_OPTION_BASIS did not apply. Consolidation adds no analytical findings and selects no option.

Context ledger: 2 direct methodology pages read, 2 used, 0 deferred. Carried IDs: AX-H01–H06, AX-I01–I06, AX-F01–F06, AX-G01–G05, AX-O0–O3, AX-X1. Source and exploration policies: AX-HP1 and AX-EXPLORE-1; comparison and reasoning records: AX-CMP-1 and AX-DRR-1. Issues remain OPEN and fixes PROPOSED.

## Issues, weak points, and improvements

### Native result

#### Harvest contract

Frame `AX-HARVEST-1` compares execution mechanisms against the current local workflow boundary, using exact source claims and code regions. Included: AX's English-language public documentation and source at the pinned revision, relevant test assertions, and current CAPRMEDIO receiving contracts. Excluded: other similarly named AX projects, competitor benchmarking, Substrate internals, production operations, full security/governance assurance, and installation instructions. No jurisdictional claim is made.

Policy `AX-HP1`: admit a mechanism when a primary source and a relevant local receiving boundary can be named; mark schema-only, documentation-only, roadmap, and code/test evidence separately. Contradictions remain explicit. Freshness ends at the pinned snapshots. This one-repository request explicitly overrides G.2's default three-family coverage floor to **one external source family**; internal mechanisms are not counted as independent rival products. No popularity, scale slogan, or recency claim establishes superiority.

Ledger `AX-CORPUS-1` was assembled before synthesis. Screening flow `AX-FLOW-1`: supplied repository → identity and commit → archive tree → concepts/schema/runner/setup/reconciler/worker paths and corresponding tests → receiving contracts and three current workflow definitions → six admitted mechanisms. Architecture and roadmap were screened to delimit current support; model planning code was screened, not promoted as a verified automatic environment planner. The stopping condition was adequate evidence for each admitted mechanism and its transfer limits, not whole-repository coverage.

#### Corpus ledger

All AX links use the same pinned commit.

| Source group | Claim regions inspected | Admission and use |
|---|---|---|
| AX-C01: identity and architecture | [README][A0], [concepts][A1], [design][A9] | Included documentation: declarative Task/Workspace/Model resources, separate API/controller/runner, Kubernetes/Substrate/Redis dependencies. Scale claims are not measurements. |
| AX-C02: configuration | [schema lines 61–224][A2], [setup][A3], [setup tests 29–83, 150–200][A3T] | Included schema/code/tests: task bindings, cloned repositories, skill directory, setup marker, errors and retries. Registry declarations do not prove capability materialization. |
| AX-C03: execution adapter | [runner guide][A5], [runner implementation][A4], [runner tests 34–121, 246–286][A4T], [metadata server 54–118][A6], [debug test 166–207][A6T] | Included: runner protocol, metadata, child-process supervision, opt-in guest execution, exit callback. No cluster execution observed. |
| AX-C04: reconciliation | [reconciler][A7], [tests 334–390][A7T], [worker][A8], [worker tests][A8T] | Included code/test expectations: desired state, launch-template identity, readiness conditions, suspend, cleanup, and queue acknowledgement. Mock tests do not establish distributed recovery guarantees. |
| AX-C05: checkpoint boundary | [runner guide][A5], [template construction 212–276][A11] | Included: durable `/workspace`, data-snapshot configuration, fresh process tree after resume. Substrate's actual end-to-end behavior is outside the inspected source. |
| AX-C06: maturity | [roadmap][A10], [schema policy removal][A2] | Included as limits: evolving alpha contracts; separate setup actors, least privilege, automatic idle suspension, state branching, governance, and telemetry are planned. |
| AX-C07: planning helper | [planner lines 27–100][A12] | Screened only: environment-plan data shape and model call. No finding that it installs declared tools or is a completed runtime path. |
| CA-C01: receiving executor | [CA-R-1522][C1], [1523][C2], [1524][C3], [CA-M-302][C4] | Included current full contracts: methodology-driven coordination, client independence, durable handoffs, replaceable workers, Journal authority. |
| CA-C02: invocation boundary | [CA-R-1525][C5], [1527][C6], [1529][C7], [1100][C8], [1107][C9], [1115][C10], [CA-M-222][C11] | Included current full contracts: exact definitions, Integrated/Isolated contexts, self-contained invocation, App and MCP boundaries. |
| CA-C03: real workflow receivers | [Source Reconciliation CA-O-010][W1], [Implementation Workflow CA-O-016][W2], [selected Release Readiness CA-O-025][W3] | Included current full definitions used in the workflow-option comparison. They specify transitions and approvals; reading them did not execute them. |
| CA-C04: prior analysis | [CA-A-903][P1] full report; [CA-A-904][P2] TL;DR and bounded claim/issue sections | Included as prior ideas only. No fresh verification of their external sources or operational-completion claims. |

#### Claim sheets: mechanisms and transfer limits

| ID | Exact source finding | Useful CAPRMEDIO synthesis and limit |
|---|---|---|
| **AX-H01 — Reusable execution context** | Task declares image/command/environment and ordered Workspace bindings; Workspace declares Git, MCP, and skill inputs; Model is separately named configuration. The runner maps bindings by name and uses the first path as command cwd; tests assert multiple workspaces and cwd. [Schema][A2], [runner][A4], [tests][A4T]. | Package each admitted worker's inputs, tool availability, runtime, and output contract explicitly. This fits our self-contained invocation requirement [C7][C7] and makes setup repeatable across clients. **Limit:** the inspected default setup clones Git and creates a skill directory; it does not read MCP configuration or fetch skills from registries. Borrow the declaration pattern without equating configuration with working capabilities. |
| **AX-H02 — Replaceable runner boundary** | A runner receives launch specs, prepares workspaces, supervises the command, serves metadata, and stays alive for inspection. A custom image can implement the same contract; `OnCommandExit` exposes the child result. Guest process/file services are enabled only by `debug`; a test expects process start to fail when debug is off. [Guide][A5], [code][A4], [metadata][A6], [test][A6T]. | Define a narrow execution adapter beneath Workflow Orchestrator, with explicit start, result, inspection, and cancellation behavior. CAPRMEDIO already requires replaceable worker/client adapters [C4][C4]. A future AX adapter would be one possible worker backend; its arbitrary-process interface would not replace admitted Tool calls or gain mutation authority. |
| **AX-H03 — State needs reasons and separate meanings** | AX distinguishes phase from `WorkspaceReady` and `Ready` conditions. Tests preserve workspace readiness across suspend and restore ready state. The runner keeps HTTP services alive after command exit; its guide states the control plane does not read the exit status. [Reconciler][A7], [tests][A7T], [runner tests][A4T], [guide][A5]. | Show accepted work, prepared environment, running process, waiting input, and verified Step outcome separately. This makes [CA-R-1523][C2] and CA-A-904's status idea concrete. **Limit:** `Ready` cannot establish successful work. Static code also shows Git failure returning nil from setup, after which the runner can mark readiness true; bootstrap failure is logged and ignored. Required prerequisites need independent checks before our dispatch. |
| **AX-H04 — Identity from launch configuration** | Reconciliation removes status and suspend from the injected launch spec, sorts environment keys, and derives an image/environment digest for a template name. Tests expect readiness/suspend changes to reuse a template and a changed command to create another. [Code][A7], [test][A7T]. | Separate the identity of the admitted execution recipe from transient status, then record both. This complements exact definition bindings [C5][C5] and MCP frontier binding [C10][C10]. **Limit:** a template digest is not an approval, proof of runtime adoption, or complete input snapshot. AX's short naming digest is not proposed as CAPRMEDIO's evidence hash. |
| **AX-H05 — Pause the environment, resume the application deliberately** | Suspend/resume invokes Substrate; the template defines a durable `/workspace` and data snapshots. The runner guide says resume restores files into a fresh process tree. Setup uses a path-based marker under `/ax`. [Guide][A5], [template][A11], [setup][A3]. | Retain working artifacts while a long action or agent waits, then resume through a recorded invocation and effect receipt. This matches [session independence][C2] and [handoff recovery][C3]. **Limit:** filesystem restoration does not establish resumed computation, exactly-once effects, or permission to replay the command. Persistence of the `/ax` marker across the actual snapshot cycle is unverified in this review. |
| **AX-H06 — Responsive control separate from worker execution** | The gRPC API, stored tasks, event workers, and runner are distinct components. Worker code records reconciliation failure and acknowledges events even on error; deletion retains `Terminating` on actor cleanup failure and a later delete request can retry. Tests exercise reconciliation and deletion against mocks. [Design][A9], [worker][A8], [tests][A8T]. | Let a client submit and reconnect while an executor reports state and routes explicit control requests. Adopt stable request/run/dispatch correlations and visible uncertain outcomes as required by [CA-M-302][C4] and [CA-R-1524][C3]. **Limit:** queue delivery and acknowledgement are not our canonical Journal or completion evidence; no exactly-once handoff guarantee follows from this implementation. |

These six records form `AX-SET-1` and `AX-PALETTE-1` exactly. They are the mechanism palette behind the options below, not an adoption shortlist.

#### Approaches, objects, and bridges

| Approach / family | Objects and operations | Strength and validity region | Cross-boundary loss to preserve |
|---|---|---|---|
| AX declarative workload control | Task, spec, status, condition, actor; submit/watch/suspend/resume/delete | Separates desired runtime state from worker processes; fits remote or numerous isolated executions. | A Task is an execution unit, not our Workflow Run, Step Run, Plan Atom, or approval. |
| AX prepared execution environment | Workspace, runner, launch configuration, metadata; materialize/start/inspect | Reusable setup and a replaceable agent container contract. | An environment name or marker is not complete capability verification or current authority. |
| CAPRMEDIO governed workflow execution | Workflow/Step/Action revisions, invocation, result, Journal; admit/dispatch/evaluate/handoff/revalidate | Explicit semantics for selection, approvals, retries, and evidence. | A conforming logical workflow does not by itself supply remote sandbox infrastructure. |

Bridge matrix `AX-BRIDGES-1`: H01/H02 align at the **invocation-to-worker boundary**; H03/H04 align at **runtime observation-to-evidence binding**; H05/H06 align at **worker lifecycle-to-durable coordination**. These are bounded correspondences, not equivalence, fusion, or replacement claims. No new public names are minted (`AX-UTS-1`: none).

Object map `AX-OBJECTS-1`: Task/actor → candidate execution backend identity; Workspace → candidate environment binding; condition → runtime observation; command result → evidence requiring correlation to a Step Run; Journal → local authority for actual execution history. Proposed indicator families `AX-IND-1`: setup complete/incomplete; process running/exited; outcome accepted/rejected/unknown; definition current/changed; effect observed/uncertain. Branch labels are descriptive; no acceptance threshold or gate is established here. No task generator is admitted.

Micro-examples `AX-ME1`–`AX-ME3` preserve source-level meaning:

1. A task binds `code` then `tools`; the test asserts both directories exist and the child runs in `code`. This demonstrates binding order, not registry installation. [A4T][A4T].
2. A child exits with code 3; the test expects the callback to report 3. A separate test keeps `/healthz` reachable after the child exits. This demonstrates why liveness and result must be distinct. [A4T][A4T].
3. Suspend and readiness updates reuse a launch template; changing the command yields a second template in the test. This is evidence of configuration-sensitive template naming, not end-to-end replay or successful application of a new template to a running actor. [A7T][A7T].

All three are inspected test expectations, not observed passes or executed CAPRMEDIO scenarios.

#### Disagreements, exclusions, and receiving use

The source-to-use gaps are substantive:

- Documentation describes configured MCP/skills and complete setup; default setup code has narrower behavior. Readiness code must therefore be evaluated against actual prerequisites, not the introductory wording. [A1][A1], [A3][A3], [A4][A4].
- Recorded `WorkspaceReady` is trusted on resume even when the readiness endpoint is unreachable in a test. That is different from a fresh currentness check. [A7T][A7T].
- Budget and approval configuration is reserved/removed in the task schema, while governance, automatic telemetry, idle suspension, and task branching appear in the roadmap. They are not harvested as current guarantees. [A2][A2], [A10][A10].
- Snapshotting files and restarting a process is different from continuing an interrupted model/tool operation. Snapshot persistence and external side effects require separate reconciliation. [A5][A5], [C3][C3].
- Kubernetes, Agent Substrate, Redis, container images, credentials, and cluster operations are dependencies of direct AX use. CAPRMEDIO's current method permits a local background coordinator; AX's intended large scale does not establish that this infrastructure is justified here. [README][A0], [C4][C4].

The evidence supports the comparison below: borrow small mechanisms, use a bounded external runner, or retain the current approach. Relevant receiving workflows are Source Reconciliation, Implementation Evaluation within CA-O-016, and the selected Release Readiness workflow. Their source/approval/result rules remain intact. The named Workflow Orchestrator delivery directory currently contains a `.gitkeep`; this limited path inspection is not a repository-wide claim that no related implementation exists elsewhere.

Refresh when the AX commit, an admitted code path, or a local pinned contract changes; reopen runtime evidence if any option progresses toward adoption. No automatic monitoring is started.

The overlap with existing work is explicit: H03 develops CA-A-904's distinction between states, while H04 complements the current exact-definition and frontier-binding requirements. CA-A-903/904 remain prior analysis context; their external sources and operational conclusions were not revalidated here. This harvest adds concrete AX implementation limits to the comparison rather than treating prior ideas as completed features.

#### Exploration contract

**Question and receiving use:** which distinct ways of using AX or its ideas are supportable for our declared workflows, and what would each require? Entity of concern: the invocation-to-worker boundary in CAPRMEDIO workflow execution. Evaluator: this source-grounded analysis; decision owner: Anatoly.

Policy **AX-EXPLORE-1** defines interesting as a concrete, source-supported change to preparation, isolated execution, result inspection, or recovery in an existing named workflow, with a clear Tool/App/MCP receiving boundary. Familiar alternatives are the declared local background coordinator, in-session or isolated action execution, and retaining today's arrangement. Novel naming or AX branding is not a benefit.

Quality coordinates declared before generation:

| Coordinate | Admitted comparison |
|---|---|
| Additional infrastructure | None; local adapter/contract work; remote platform plus integration. Compare only for the same receiving need. |
| Workflow applicability | Named eligible work: unchanged workflow, local action, bounded evaluation, or admitted isolated agentic Step. These categories have no universal ranking. |
| Integration uncertainty | Existing coverage unverified; local mapping unverified; remote capability/result/recovery unverified. Missing evidence stays visible. |
| Reversibility | No dependency added; local contract/adapter; optional backend behind an interface. Reversal cost remains qualitative. |
| Boundary preservation | Hard constraint: exact definitions/frontier, admitted effects and Tools, explicit outcomes, current authority, existing workflow transitions and retries. |

Diversity axes are AX dependency (none / borrowed mechanisms / runtime) and work structure (local action / finite programmatic job / agentic work with possible input and recovery). They describe coverage, not utility. No aggregate novelty score, Pareto front, cost estimate, or winner is justified by the evidence.

Admissible risk is analytical uncertainty stated as such; adoption cannot assume missing operational guarantees. Reversibility favors keeping the backend boundary explicit but is not a selection. Time horizon is a later bounded investigation if selected, with no implementation date. Exploration budget: one pass, four distinct retained options and one explicit exclusion, using only the pinned source frontier. Stop when each option has a receiving workflow, before/after example, boundary, benefit hypothesis, costs, and decisive missing evidence. That condition is met.

Method: verified B.5.2.1 Creative Abduction with NQD, from edition revision 563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef. It grounds provenance-bearing hypotheses, explicit quality coordinates, and diversity without premature selection. G.2 grounds the harvest above. Conditional G.9 was not opened: no runtime benchmark or comparable measured-performance claim is made.

#### CandidateSet AX-OPTIONS-1 and provenance

All benefits below are **hypotheses**. All options are retained for owner comparison, with no adoption ranking.

**AX-O0 — Keep the current execution arrangement**

- **Before → after:** Source Reconciliation, Implementation, and selected Release Readiness retain their declared actions, evidence, approvals, and transitions. Execution continues through whatever current adapters actually satisfy those contracts; AX remains a reference. This option does not assert that every declared service is implemented. [W1][W1], [W2][W2], [W3][W3].
- **Tool/App/MCP boundary:** no new backend or public Tool/MCP operation. Existing boundaries remain the baseline.
- **Why useful:** avoids additional platform and integration obligations when there is no demonstrated isolation, preparation, or session-continuity problem.
- **Cost/trade-off:** any present limitations remain. Their prevalence was not measured, so keeping the baseline is neither proven sufficient nor dismissed as inferior.
- **Provenance:** current C1/C4/C7 and W1–W3; AX-G03/G04/G05 explain why no change remains admissible.
- **Next evidence if considered:** inspect the active executor for one troublesome workflow and document its actual failure or unmet need. Relationship: alternative to introducing O1–O3 now.

**AX-O1 — Borrow execution profiles and precise states locally**

- **Before → after:** Source Reconciliation selects a source frontier, assesses conflict, proposes a resolution, and obtains the required decision before correction. The self-contained invocation is already required. The proposed local adapter makes its execution recipe inspectable: exact source and definition bindings, required Tool/MCP capabilities, environment, allowed effects, expected result, and return route. It reports preparation, running process, waiting input, and accepted outcome separately. This is a possible realization or refinement of existing requirements, not proof they are currently absent. [W1][W1], [C7][C7].
- **Tool/App/MCP boundary:** Workflow Orchestrator admits and routes the invocation; the worker executes the permitted action; MCP keeps complete Tool contracts and current frontier bindings; Apps display the declared status and result. The worker never chooses the next workflow Step. [C1][C1], [C9][C9], [C10][C10], [C11][C11].
- **Expected benefit:** less repeated setup discovery and clearer diagnosis of preparation failure versus execution failure. AX-H01/H03/H04 supply concrete design examples.
- **Cost/trade-off:** local adapter and metadata work, capability checks, input pin maintenance, and result correlation. AX itself is not required.
- **Assumptions and verification:** first inventory existing implementation. For the same admitted assessment, a missing capability must block; status-only changes must not change the recipe; changed governing inputs must trigger new binding or revalidation. Measure preparation effort only in a later trial.
- **Provenance:** H01/H03/H04 → F01/F03/F04, constrained by C5/C7/C10. Alternative execution arrangement to O2/O3 for work that does not need remote infrastructure; its contract ideas can complement either.

**AX-O2 — Use AX as a backend for bounded evaluation jobs**

- **Before → after:** in the Implementation workflow, a selected runnable evaluation produces passed, failed, or blocked evidence for the declared next transition. If Release Readiness was explicitly selected, its evaluation result informs the existing readiness gate. The proposed adapter instead sends an eligible finite job to AX with pinned inputs, image, command, and output destination; it returns exit status, selected evaluation identity, results, logs/artifacts, and input binding. The current workflow interprets that result. [W2][W2], [W3][W3].
- **Tool/App/MCP boundary:** a declared Tool or worker binding owns the executable evaluation contract; AX Task/actor IDs correlate to the CAPRMEDIO invocation and Step Run. MCP can expose accepted work and later results through its admitted contract; the App renders progress. Remote job completion grants no release, commit, or publication authority.
- **Expected benefit:** isolation from the interactive session, reproducible runtime packaging, and potential remote capacity. These are fit hypotheses, not measured speed, reliability, or savings.
- **Cost/trade-off:** Kubernetes, Substrate, Redis, images, artifact transport, permissible credentials, operational ownership, and a result collector/bridge. Platform-specific evaluations may be ineligible. The inspected default runner does not supply working MCP/skill setup merely because it appears in the schema; HTTP Ready does not deliver command success to the control plane. [README][A0], [setup][A3], [guide][A5].
- **Assumptions and verification:** establish a real workload need and eligible evaluation first. On the same candidate, selected tests, dependencies, and expected result, verify missing capabilities, nonzero exit, cancellation, correct result correlation, and artifact integrity. Only then measure duration, cost, or capacity. No new parallelism or retry allowance follows from the backend.
- **Provenance:** H01–H04/H06 → F01–F04/F06; C1/C3/C4/C5/C9/C10 and W2/W3. Retained as a conditional direct-use option, not ready adoption.

**AX-O3 — Use AX for an explicitly Isolated agentic Step**

- **Before → after:** Source Reconciliation includes assessment and proposal work. Where the actual selected Step admits an Isolated agentic context, its self-contained invocation can be sent to an AX-hosted agent runner with selected sources, prior results/effects, allowed operations, instructions, and output route. The runner returns an assessment/proposal or an explicit input request. Operator decision and any correction remain separately admitted workflow actions. This does not classify every Step in CA-O-010 as agentic or isolated. [W1][W1], [C6][C6], [C7][C7].
- **Tool/App/MCP boundary:** the host adapter sits beneath Workflow Orchestrator. It uses admitted Tool calls and MCP bindings; AX is neither the workflow definition store nor the authority for next steps. Runtime suspension, waiting for Operator input, blocked execution, and completed Step remain different states.
- **Expected benefit:** retain working artifacts and an isolated environment across client reconnection or a long assessment, while keeping the workflow in control. No reasoning-quality improvement is established.
- **Cost/trade-off:** O2's infrastructure plus an agent harness, model and credential configuration, structured outcome/input handling, and explicit application recovery. Restoring files into a fresh process does not restore the model conversation or authorize replay of effects. [Guide][A5], [handoff contract][C3].
- **Assumptions and verification:** the chosen Step must admit this context and its required capabilities. Record the invocation and effect receipts; interrupt after known work or while awaiting input, reconnect, and verify preserved artifacts, correct result identity, current authority, and no duplicate uncertain effect. A definition change must not silently restart under new semantics.
- **Provenance:** H01–H06, especially H02/H05/H06 → F01–F06, constrained by C3/C5/C6/C7 and W1. It differs from O2 through agent interaction and continuation state, not branding.

#### Declared-coordinate evaluation and diversity map

Comparison protocol **AX-CMP-1** pins O0 to the local contract bytes hashed below, and AX-dependent options to commit e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7. Freshness window is the 2026-09-25 inspection; refresh changed sources before a later decision. The bridge normalizes every option to the same admitted invocation/result and unchanged governing workflow rules. Policy compares architecture and prerequisites only; it does not equate an AX Task with a Workflow Run or use roadmap features as present capability.

| Option | Additional infrastructure | Applicability / diversity | Uncertainty | Reversibility and useful condition |
|---|---|---|---|---|
| O0 baseline | None introduced | All present declared workflows; no new mechanism | Active implementation coverage remains unverified | No AX dependency; useful when no execution need warrants change |
| O1 borrow locally | Local contract/adapter work | Preparation and inspectable state for local actions | Existing overlap and benefit need checking | Local boundary can evolve independently; useful for setup or status problems |
| O2 AX evaluations | Remote platform plus adapter | Eligible finite programmatic evaluations | Deployment, capability setup, results, cost, recovery | Optional backend limits coupling; useful if isolation or capacity justifies platform |
| O3 AX agentic Step | Same platform plus agent/recovery handling | Explicitly Isolated agentic work, input waits, artifact continuity | O2 gaps plus dialogue and effect-safe continuation | Backend remains replaceable, but continuation state raises switching cost; useful for eligible long isolated work |

No dominance relation is established across all coordinates. A Pareto front would imply unsupported comparability of benefits and cost, so none is claimed. No benchmark ParityReport is applicable or produced. For a future measured O2-versus-local comparison, the owner must first approve a ParityPlan using the same candidate/input frontier, selected evaluation, dependency versions, acceptance rules, resource accounting, and failure cases; inspect conditional G.9 at that point.

Decision/reasoning record **AX-DRR-1**: generation seeds were six harvested mechanisms and three named local workflow receivers. Options were differentiated by dependency level and execution structure; shared contract fixes were deduplicated into F01–F06. Retained: O0–O3. Excluded: AX-X1 below. Archive state: all four remain research candidates, none selected or implemented. Diversity telemetry is four architectural choices across the two declared axes; it is not a merit score or exhaustive search claim.

**AX-X1 — Replace governed workflow coordination with AX task state: excluded.** AX's inspected current lifecycle, reserved policy fields, and roadmap do not supply our selected Workflow/Step/Action definitions, current authority, approvals, bounded retries, evidence gates, or canonical Journal. Such a replacement violates the protected boundary and lacks source support. [Schema][A2], [roadmap][A10], [orchestration][C1], [recovery][C3].

#### Stop condition and decision handoff

COMPLETE: four distinct supported options cover retaining the baseline, borrowing mechanisms, and two different direct-use shapes. The evidence is sufficient for this comparison, not adoption. No selection is necessary to complete the user-requested analysis. The harvest, option set, and TL;DR are consolidated here.

If Anatoly later requests a decision, the receiving handoff is AX-OPTIONS-1 plus the full source ledger, open I/F/G registers, and one named workload with its operational constraints. Selection belongs to a later explicitly requested decision activity; implementation needs separate authority. All direct-use options remain conditional on missing operational evidence.

### Issue registry

These are transfer risks and source limitations, not six asserted CAPRMEDIO defects. Confidence percentages express this reviewer's confidence in the stated interpretation, not measured error rates. Discovering node for all: step 1 `$fpf sota harvest`.

| ID | Bounded issue and consequence | Evidence, confidence, coverage limit | State / fixes |
|---|---|---|---|
| AX-I01 | Treating a workspace declaration as ready capability can start an action without required repositories, MCP, or skills. | A2/A3/A4; **99%**, direct inspected setup/runner path. No deployed bootstrap or custom runner was tested. | OPEN; F01, F03 |
| AX-I02 | Treating liveness, Ready, or Running as successful Step completion loses exit/failure meaning. | A4/A4T/A5/A7; **99%**, code plus explicit guide and test expectations. CAPRMEDIO runtime prevalence unknown. | OPEN; F02, F03 |
| AX-I03 | Confusing transient status with execution identity, or treating a template hash as full provenance, misbinds results. | A7/A7T and C5/C10; **98%**, observed identity mechanism and narrower local requirements. No whole-runtime provenance audit. | OPEN; F04 |
| AX-I04 | Equating data restoration with safe application continuation can repeat effects or skip revalidation. | A5/A11/C3/C5; **98%**, documented fresh process plus required local recovery rules. Actual Substrate snapshot cycle untested. | OPEN; F05 |
| AX-I05 | Treating an acknowledged queue event as a durable, completed workflow handoff hides failed or uncertain effects. | A8/C3; **99%**, explicit acknowledgement-on-failure code. Crash/reclaim semantics outside this review. | OPEN; F06 |
| AX-I06 | Treating AX's execution runtime or roadmap as a complete governed workflow solution imports unproven authority, capability, and infrastructure assumptions. | A0/A2/A10/C1/C4; **98%**, alpha/policy/roadmap distinction and local boundaries. Costs and deployment viability unmeasured. | OPEN; F02, F06 |

### Fix and improvement register

All entries are **PROPOSED research transfers**, not authorized changes. Owner: Anatoly for selecting a direction; any later implementation owner requires a separate admitted change. Order below is conceptual dependency order, not an implementation schedule. “Acceptable” means a supported item for comparison, not selected adoption.

| ID / issues | Exact idea, relationship, receiving surface | Independent confidence and expected result / trade-off | Dependencies/order, future verification, recommendation |
|---|---|---|---|
| AX-F01 / I01 | Make the admitted invocation carry explicit environment inputs and required capabilities; **complementary**, worker/invocation boundary. | **95%**, H01 fits C7. More reproducible preparation; maintaining pins and capability checks costs effort. | No prior idea required. Check missing declared capability produces an explicit block, and the actual bound inputs are inspectable. **Acceptable; PROPOSED**. |
| AX-F02 / I02, I06 | Define a replaceable worker adapter that returns correlated result and cancellation evidence while preserving Tool and approval authority; **complementary**, Orchestrator/host/optional remote runner. | **95%**, H02 fits C4/C6/C7. Backend choice becomes separable from procedure; adapter and credential handling add work. | Requires an admitted invocation; F01 can inform it. Verify swapping workers changes no governing transition or authority, and an exit is associated with the correct Step Run. **Acceptable; PROPOSED**. |
| AX-F03 / I01, I02 | Distinguish prerequisite readiness, liveness, process outcome, and accepted result; **required prerequisite** for trusting an AX-style worker, MCP/App presentation. | **98%**, explicit H03 code/contract mismatch. Fewer unsupported completion claims; richer status and checks. | Define required prerequisites and result rules first; compatible with F01/F02. Verify clone failure, child exit 3, stale ready state, and missing result never produce successful completion. **Preferred as a comparison constraint; PROPOSED**. |
| AX-F04 / I03 | Bind each result to an execution recipe separate from transient status, retaining exact governed definitions and source frontier; **complementary**, invocation/evidence contract. | **95%**, H04 plus C5/C10. Clearer provenance; extra metadata and invalidation handling. | Resolve canonical identity inputs first. Verify status-only changes preserve recipe identity and relevant input changes demand a new binding or revalidation. **Acceptable; PROPOSED**. |
| AX-F05 / I04 | Resume from retained artifacts plus effect-aware receipts and current authority checks; **required prerequisite** for safe resumable execution, Orchestrator/Journal/worker boundary. | **97%**, H05 plus C3/C5. Interrupted work can be recovered explicitly; uncertain non-repeatable effects may require Operator input. | Requires recorded invocation/results, typically F02/F04. Verify restart after an uncertain effect does not blindly replay it, and changed definitions visibly block further dispatch. **Preferred as a comparison constraint; PROPOSED**. |
| AX-F06 / I05, I06 | Separate responsive coordination from workers and rebuildable queue/status views, preserving canonical Journal handoffs; **complementary**, Orchestrator/MCP/App boundary. | **95%**, H06 and C3/C4. Reconnectable control; queue/reconciliation complexity and remote infrastructure costs. | Requires a supported lifecycle and effect identity, F03/F05 where applicable. Verify accepted work survives client loss, failed dispatch stays visible, and acknowledgement cannot close a Step. **Acceptable; PROPOSED**. |

No listed verification was performed. The options map these constraints to O1–O3; none implements the register. Residual risk is unchanged: G01–G05 must be resolved to the extent needed by any selected successor. O0 retains the current arrangement without declaring that risk solved.

#### Local evidence pins

SHA-256 of inspected current files; each ID links to its exact carrier above. These pins identify the dirty bytes independently of HEAD.

| Source | SHA-256 |
|---|---|
| C1 CA-R-1522 | `9f005f1244c2d1658576a9cdbb2e68b8d5e48d9935df6fab35c86ae764404d01` |
| C2 CA-R-1523 | `eb7ddf4f4f3e605ecf2b8bce31fd83779c991d9f81b09cea7e14702187778d9c` |
| C3 CA-R-1524 | `0bfda77c29dd8a5c2fd1a0c964aa2f6825dd3b7505eaee4b3746cda9c8ba7801` |
| C4 CA-M-302 | `d8e1f7eed8bc1d9c3b2f72ff7f14d1a84be21246210634a0e23be0048d41a313` |
| C5 CA-R-1525 | `dee18b09073722dd9b997579ddf5e7a7ff30dc041857a23184227f51548aa9c8` |
| C6 CA-R-1527 | `c72d7eebac638f06008ca5ffe35ab13f5f3aebaff0047ddd136da199f33093cc` |
| C7 CA-R-1529 | `d8aa04092497d634c1716d1baf06b9a5f9a83298b5eddaf85c4459c913400516` |
| C8 CA-R-1100 | `1da267f1676aed64015aaf4bfd83764b0c591bbd20aa0dba4c8aaa150d554497` |
| C9 CA-R-1107 | `0ffeed71691af63a1b75aa6cf33c7ac4164729e44bc162a34b3819021fb2bef4` |
| C10 CA-R-1115 | `d8d64e465be7ef32f18bcb4ee3179363a4533afb4f677198ea1668181edef64b` |
| C11 CA-M-222 | `973bba46ab38aa7ec21bd27231fb5bcace34d67810e2fffaaa8f99989953c9b8` |
| W1 CA-O-010 | `fe23f033b0c68300ba3e63cdab27e574a81b4e4781c79a0ea06d1f659da55e94` |
| W2 CA-O-016 | `77b87ccc1cd5c4df52243352563150c7db4e509a87492f8d3c48862481c6ba2d` |
| W3 CA-O-025 | `b44bfe50bc13762b360c454873fd0d23ee36a57019e48f705d4c5bf00829ddd4` |
| P1 CA-A-903 | `a0f2dc6cdd296afff3609764d665e853c0401bcf179744084d07c8b1c5e66034` |
| P2 CA-A-904 | `2c210017386031aeef23d3cd7075d7669927a6616a8ea83a9d9ed7e4aa887aef` |

#### Source acquisition receipt

The GitHub commit API returned commit e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7, timestamp 2026-09-25T06:31:22Z, and tree 0d5b1930b534e0236cc4b3c834eebc035040193a. The [commit-addressed source archive][ARCHIVE] had SHA-256 75bd3afb0933bb49643c331435a0d7cb4e7e7008a8056067afcc17e9b0b8bffa. Its local acquisition path was /tmp/google-ax-e09ed1bc-source.tar.gz, unpacked at /tmp/ax-e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7. The pinned public references and ledger make the analysis reconstructible without these temporary copies.

Read boundaries: concepts, runner guide, roadmap, sandbox guide, DESIGN, workspace setup, runner implementation, reconciler, worker, and worker tests were read fully. README was inspected through GitHub rendering. Bounded code/test reads: schema 1–230; workspace setup tests 29–83 and 150–200; runner tests 34–121 and 246–286; reconciler tests 334–390; metadata server 54–118 and tests 166–207; substrate client 198–304; planner 1–100 screened only. All C1–C11 and W1–W3 receiving files were read fully; CA-A-903 fully, CA-A-904 lines 1–48 plus targeted claim/issue sections. No whole-system audit or runtime pass is implied.

## Unresolved evidence gaps

| ID / links | Best current answer; missing evidence | Consequence and exact next evidence |
|---|---|---|
| AX-G01 / I01, I02; F01–F03 | Default source paths have the stated capability/readiness/result limits; no end-to-end run was performed. | Do not assume advertised guarantees. If direct use is considered, exercise missing repo/tool, failed bootstrap, nonzero exit, and result correlation against the pinned deployment. |
| AX-G02 / I04, I05; F05–F06 | Resume restores data and starts a fresh process; complete snapshot, marker persistence, crash, and queue recovery were not inspected in Substrate. | No exactly-once or transparent continuation claim. Trace one stop/resume/crash sequence with retained artifacts and an uncertain effect before relying on it. |
| AX-G03 / I06; F02, F06 | Cluster dependencies are documented; this project's actual deployment need, capacity, operating cost, and permissible credentials are unknown. | Direct AX adoption cannot be justified here. A selected option needs workload scale and operating constraints, then a bounded cost/benefit comparison. |
| AX-G04 / all | Current local contracts and example workflows are verified; full implementation coverage is not. | Ideas are not asserted missing features. For a selected option, inspect its active service/adapter/Tool implementation and tests before designing changes. |
| AX-G05 / all | Source-bound harvest establishes useful mechanisms, not comparative superiority or measured savings. | No broad SoTA ranking. Compare additional primary projects or measure a representative workflow only if a later decision requires it. |

## Skills used

1. $fpf sota harvest — completed the bounded source harvest.
2. $fpf options explore — completed the four-option workflow comparison.

### FPF sources consulted (2 read; 2 used)

- **Used in harvest:** FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/03_02_SoTA Harvester & Synthesis/00_G.02 - SoTA Harvester & Synthesis.md; verified fpf_id G.2. Problem frame, Problem, Forces, Solution §§4.1–4.4 and 4.6–4.7, and Consequences used for the reconstructible source palette and explicit bridge losses.
- **Used in options exploration:** FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/04_05_Canonical Reasoning Cycle/02_Abductive Loop/02_B.05.02.01 - Creative Abduction with NQD.md; verified fpf_id B.5.2.1. Problem Frame, Intent and Problem, characteristics, Solution and generation/filtering, and §10a trade-offs inspected; these ground abductive options, declared quality coordinates, and diversity without a manufactured winner. The page has no separate Forces/Consequences headings; §10a supplies the relevant trade-offs. No neighboring pattern was opened.

Both pages resolve under /Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit, edition source revision 563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef, generated 2026-08-26. Conditional G.9 is not included in read/used counts.

[PIN]: https://github.com/google/ax/commit/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7
[A0]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/README.md
[A1]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/docs/concepts.md
[A2]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/pkg/apis/v1alpha1/ax.proto#L61-L224
[A3]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/internal/workspace/setup.go
[A3T]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/internal/workspace/setup_test.go#L29-L200
[A4]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/runner/runner.go
[A4T]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/runner/runner_test.go
[A5]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/docs/runner.md
[A6]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/internal/metadata/server.go#L54-L118
[A6T]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/internal/metadata/server_test.go#L166-L207
[A7]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/internal/controller/reconciler.go
[A7T]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/internal/controller/reconciler_test.go#L334-L390
[A8]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/internal/controller/worker.go
[A8T]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/internal/controller/worker_test.go
[A9]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/DESIGN.md
[A10]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/docs/roadmap.md
[A11]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/internal/substrate/client.go#L212-L276
[A12]: https://github.com/google/ax/blob/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7/internal/workspace/planner.go#L27-L100
[C1]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/04_requirement/CA-R-1522-WORKFLOW_ORCHESTRATOR-REQUIREMENT--provide-workflow-orchestration-from-methodology.md
[C2]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/04_requirement/CA-R-1523-WORKFLOW_ORCHESTRATOR-REQUIREMENT--keep-long-running-work-independent-of-client-sessions.md
[C3]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/04_requirement/CA-R-1524-WORKFLOW_ORCHESTRATOR-REQUIREMENT--recover-workflow-handoffs-without-repeating-effects.md
[C4]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/05_method/CA-M-302-WORKFLOW_ORCHESTRATOR-METHOD--separate-workflow-coordination-from-action-execution.md
[C5]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1525-CORE_META_MODEL-GENERAL-REQUIREMENT--bind-workflow-runs-to-exact-definition-revisions.md
[C6]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1527-CORE_META_MODEL-GENERAL-REQUIREMENT--define-agentic-step-execution-context.md
[C7]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1529-CORE_META_MODEL-GENERAL-REQUIREMENT--provide-self-contained-agentic-step-invocations.md
[C8]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/04_requirement/CA-R-1100-APPS-CORE-REQUIREMENT--define-the-application-scope-unit-topology.md
[C9]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1107-MCP-REQUIREMENT--require-complete-tool-invocation-contracts.md
[C10]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1115-MCP-REQUIREMENT--bind-mcp-operation-to-the-current-project-frontier.md
[C11]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/05_method/CA-M-222-APPS-CORE-METHOD--bind-an-app-interface-to-declared-backend-services.md
[W1]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-010-CORE_META_MODEL-WORKFLOW--reconcile-sources.md
[W2]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-016-CORE_META_MODEL-WORKFLOW--implement-evaluations-before-required-behavior.md
[W3]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-025-PROJECT_CONFIGURATION-WORKFLOW--check-release-readiness-when-selected.md
[P1]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/02_analysis/CA-A-903-FRAMEWORK_ENGINE-ANALYSIS_RPRT--assess-trace-engineering-ideas-for-caprmedio.md
[P2]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/02_analysis/CA-A-904-FRAMEWORK_ENGINE-ANALYSIS_RPRT--harvest-langwatch-ideas-for-tools-apps-and-mcp.md
[ARCHIVE]: https://codeload.github.com/google/ax/tar.gz/e09ed1bc5463ad4b5ca88f755a6e1e2005b3c7b7
