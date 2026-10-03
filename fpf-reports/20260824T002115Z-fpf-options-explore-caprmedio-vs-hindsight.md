## Task, scope, and boundaries

Compare CAPRMEDIO with Hindsight, identify the main differences, and explore additions CAPRMEDIO could independently design after studying Hindsight's public behavior. This is an options report, not an implementation decision or authorization to change CAPRMEDIO authority.

Saved report: `fpf-reports/20260824T002115Z-fpf-options-explore-caprmedio-vs-hindsight.md`

**Comparison baseline.** CAPRMEDIO was inspected in the live worktree at commit `a797695331dbf9c879b7624c99b4b96e3cfaca24` on 2026-08-24. That worktree contains a large in-progress authority migration, so this report describes the inspected worktree and does not pretend that the commit alone reproduces it. Hindsight was inspected from its actual repository at commit [`3295716cafcc593b6a2cdebd03dd71373b091859`](https://github.com/vectorize-io/hindsight/tree/3295716cafcc593b6a2cdebd03dd71373b091859), dated 2026-08-23. Confidence: **99%**; evidence basis: direct Git inspection of both repositories.

**Exploration contract.** Candidate mechanisms are evaluated on six declared coordinates, each scored from 1 (poor) to 5 (strong): governance integrity, operator control/privacy, provenance/replayability, useful context reduction, local/provider-neutral fit, and reversibility. Implementation burden and time-to-first-evidence are reported separately because they must not be hidden inside one quality score. Diversity is preserved across capture, synthesis, projection, partitioning, retrieval, and evaluation mechanisms. Confidence: **97%**; evidence basis: the FPF creative-abduction and parity patterns listed below.

**Protected constraints.** No inferred memory may silently become project authority; raw-session access remains explicitly approved and bounded; local-only and provider-neutral behavior remain defaults; graph, Tool, MCP, and host-plugin authority boundaries remain intact; and no Hindsight code, documentation wording, visual design, schema, or branding is copied. Confidence: **99%**; evidence basis: CAPRMEDIO's [principles and current boundaries](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/README.md), [raw-session approval requirement](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/AGENTIC/SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-580--require-per-run-approval-for-raw-session-access.md), and [provider-neutral MCP boundary](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/MCP/04_requirement/CA-R-1113-MCP-REQUIREMENT--provide-one-project-local-provider-neutral-mcp-service.md).

**Resolved FPF source.** The live generated knowledge graph was used, derived from FPF source revision `f0b498ddfdf562242984ff7ab7a2557b55af6690` and generated on 2026-08-22. The repository checkout itself is dirty, so the embedded generated-source revision, rather than the checkout HEAD, pins the consulted content. Confidence: **99%**; evidence basis: provenance metadata in each consulted generated FPF page.

## High-confidence results (>=95%)

### Main difference

CAPRMEDIO and Hindsight overlap in their concern for continuity, but they are not competing implementations of the same thing.

- **CAPRMEDIO is a governed project-development system.** It stores small authoritative artifacts with typed relations and covers the path from observations and concerns through requirements, methods, evaluations, delivery, implementation, and operational evidence. Its graph exists to preserve project meaning, authority, traceability, and controlled change. Confidence: **99%**; evidence basis: CAPRMEDIO [README lines 11–20 and 38–78](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/README.md) and the [full-minimal-traceability requirement](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-007--full-minimal-traceability.md).
- **Hindsight is a runtime long-term-memory system for agents.** It ingests information, extracts facts/entities/relations/time, retrieves memories, consolidates observations, and maintains standing answers called mental models. Its primary object is an isolated memory bank, not a governed software-project lifecycle. Confidence: **99%**; evidence basis: Hindsight's commit-pinned [core concepts](https://github.com/vectorize-io/hindsight/blob/3295716cafcc593b6a2cdebd03dd71373b091859/README.md#L271-L367).
- **Therefore the useful relationship is complementarity:** Hindsight-like mechanisms may improve how CAPRMEDIO captures signals and prepares bounded context, while CAPRMEDIO must remain the authority and admission layer. Confidence: **98%**; evidence basis: the purpose and authority mismatch above.

### Parity plan and report

The declared comparison frame is capability coverage under each system's own stated purpose, using repository state no older than one day apart. It does not compare benchmark accuracy, latency, cost, or overall superiority: CAPRMEDIO has no equivalent long-term-memory benchmark, and Hindsight is not a project-governance framework. Confidence: **99%**; evidence basis: pinned baselines plus the FPF parity rule against mixing unlike semantics or collapsing a partial order into one scalar.

| Comparison coordinate | CAPRMEDIO | Hindsight | Result |
|---|---|---|---|
| Primary purpose | Govern project meaning and delivery | Give agents learned long-term memory | Different system classes |
| Knowledge admission | Governed Artifacts; operator sovereignty; explicit mutation boundaries | Automatic fact extraction and background consolidation | CAPRMEDIO is stricter; Hindsight is more automatic |
| Knowledge forms | Atom, append-only Journal, generated non-authoritative Projection | Raw facts/experiences, observations, mental models, knowledge pages | Partly analogous shapes, different authority semantics |
| Retrieval | Typed graph, scoped authority loading, selected graph context | Semantic + BM25 + graph + temporal retrieval, rank fusion, reranking, token trimming | Hindsight has the more explicit runtime recall pipeline |
| Session continuity | Minimum bounded session state; retrospective review with approval | Recall before prompts and retain after turns; configurable project banks | Hindsight provides broader automatic continuity |
| Provenance | Direct typed relations plus independent Git and Journal histories | Source memories/evidence, proof counts, model history | Both value provenance; CAPRMEDIO additionally governs normative authority |
| Current interfaces | Local-only Graph App, Tools, Skills, Codex Plugin, provider-neutral MCP boundaries | Server, embedded mode, cloud, SDKs, MCP, many agent integrations | Hindsight is more deployment- and ecosystem-mature |
| Isolation | Project and structural-scope boundaries | Strict per-user/agent/project memory banks and scoped models | Both isolate, at different conceptual layers |

Confidence: **97%** for the table as a whole. Evidence basis: CAPRMEDIO's [framework model and structure](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/README.md), [bounded rehydration requirement](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/101_PROJECT_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-509--govern-session-engine-rehydration-behavior.md), [selected Codex graph-context boundary](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/04_requirement/CA-R-1104-CODEX_PLUGIN-CORE-REQUIREMENT--route-selected-graph-context-into-governed-codex-work.md), and Hindsight's [retrieval and memory concepts](https://github.com/vectorize-io/hindsight/blob/3295716cafcc593b6a2cdebd03dd71373b091859/README.md#L275-L367), [Codex hooks and controls](https://github.com/vectorize-io/hindsight/blob/3295716cafcc593b6a2cdebd03dd71373b091859/hindsight-integrations/codex/README.md#L5-L13), and [configuration](https://github.com/vectorize-io/hindsight/blob/3295716cafcc593b6a2cdebd03dd71373b091859/hindsight-integrations/codex/README.md#L75-L124).

### CandidateSet and provenance

These candidates were independently derived from public feature descriptions and CAPRMEDIO's own authority. Hindsight source code was not inspected or used to derive an implementation. The candidates use CAPRMEDIO-native names and boundaries.

**C1 — Evidence-backed correction candidates (synthesis).** Consolidate repeated Ops, Journal, and approved-session signals into draft Concern or Analysis candidates with exact source references, contradiction state, and support count. Operator admission remains mandatory.

**C2 — Standing project briefs (projection).** Declare questions such as “current architecture,” “open risks,” or “in-flight work,” then regenerate read-only Markdown Projections when their source graph changes.

**C3 — Bounded hybrid context retrieval (retrieval).** Combine lexical, semantic, typed-graph, and temporal candidates, then fuse, rerank, and token-trim results while preserving source identity and authority tier.

**C4 — Context partitions (partitioning).** Maintain separate derived indexes by project, structural scope, operator-approved session set, or agent host. Deny implicit cross-partition retrieval.

**C5 — Opt-in session lifecycle adapter (capture).** At session start, inject a bounded current-context Projection. At stop, create only a sealed candidate signal record after the required approval and secret/PII checks.

**C6 — Recall and authority-contamination harness (evaluation).** Test relevance, omission, staleness, token cost, provenance completeness, secret leakage, and whether non-authoritative material is mistaken for authority.

**C7 — Full autonomous learning-memory subsystem (combined).** Continuously retain sessions and rewrite learned project beliefs as a new CAPRMEDIO core service.

Scores use this order: governance, control, provenance, utility, local fit, reversibility.

| ID | Scores | Burden | First evidence |
|---|---|---|---|
| C1 | 5 / 5 / 5 / 4 / 5 / 5 | Medium | Medium |
| C2 | 5 / 5 / 5 / 5 / 5 / 5 | Low–medium | Short |
| C3 | 4 / 4 / 5 / 5 / 4 / 4 | High | Long |
| C4 | 5 / 5 / 5 / 4 / 5 / 5 | Medium | Short–medium |
| C5 | 5 / 5 / 5 / 4 / 4 / 5 | Medium–high | Medium |
| C6 | 5 / 5 / 5 / 4 / 5 / 5 | Low–medium | Short |
| C7 | 1 / 2 / 3 / 5 / 2 / 2 | Very high | Very long |

The Q-vector values and relative burden categories have **95% confidence** as architecture-level ordering, not calendar estimates. Evidence basis: CAPRMEDIO's explicit authority, privacy, provenance, and replaceability constraints contrasted with Hindsight's documented retain/recall/consolidation behavior.

### Diversity map and retained front

The set is intentionally non-redundant: C1 learns candidate claims; C2 materializes stable views; C3 retrieves; C4 isolates; C5 captures; C6 evaluates; C7 represents the maximal integrated alternative. Confidence: **98%**; evidence basis: mechanism decomposition and separate failure modes.

No single winner is justified. The retained, non-dominated front is:

- **C1** for the strongest learning-to-governance bridge. It directly extends CAPRMEDIO's existing retrospective correction signals and field-feedback routing without granting those signals authority.
- **C2** for the best utility-to-risk ratio. CAPRMEDIO already defines Projection as generated and non-authoritative, so standing briefs add continuity without inventing a competing truth system.
- **C6** for assurance. Any automated capture or learned synthesis needs evidence that recall helps and does not leak secrets or contaminate authority.
- **C3** for maximum retrieval capability when real benchmarks justify its additional services, models, indexes, and operational burden.

Confidence: **96%** that these four form the decision-ready front under the declared coordinates. Evidence basis: dominance across the Q vector while preserving one high-upside/high-cost alternative.

C4 and C5 are retained as composable alternatives: C4 becomes important when one runtime serves multiple scopes, and C5 becomes useful only after C6 defines acceptable leakage and authority-contamination limits. C7 is excluded from the current front because it duplicates a large independent subsystem and conflicts with CAPRMEDIO's minimum-state, explicit-session-access, local-only, and operator-sovereignty constraints. Confidence: **97%**; evidence basis: the candidate comparison and current requirements.

### What can safely be inspired by Hindsight

The legally and architecturally safest pattern is to adopt the **problem decomposition**, not Hindsight's expression or identity:

1. Write new CAPRMEDIO requirements and evaluations from the desired outcomes above.
2. Use original CAPRMEDIO terminology, schemas, UX, diagrams, and code.
3. Treat every learned result as a derived signal or Projection until an existing governed path admits it.
4. Keep raw-session capture opt-in, scoped, redactable, inspectable, and deletable.
5. If any Hindsight MIT-licensed code is later reused, preserve its copyright and license notices and record the exact reused files and revision. Hindsight's [MIT license](https://github.com/vectorize-io/hindsight/blob/3295716cafcc593b6a2cdebd03dd71373b091859/LICENSE) permits use and modification subject to retaining its notice.
6. Do not use the Hindsight name, logo, look-and-feel, or confusingly similar feature branding for CAPRMEDIO. The repository itself presents “Hindsight™”; the [USPTO explains](https://www.uspto.gov/trademarks/basics/what-trademark) that marks identify and protect brands in connection with goods or services.

In the United States, copyright does not protect ideas, procedures, processes, systems, or methods of operation, although it can protect their particular expression; this supports independent implementation from public concepts, not copying prose or code. Confidence: **99%**; evidence basis: [U.S. Copyright Office Circular 33](https://www.copyright.gov/circs/circ33.pdf). This is engineering guidance, not legal advice.

### Stop condition and decision handoff

Exploration stops here because the set covers every materially distinct mechanism visible in the comparison—capture, synthesis, projection, partitioning, retrieval, evaluation, and full-system replacement—and the last alternative exposes the boundary that should not be crossed casually. Additional brainstorming without a chosen use case or benchmark would mostly produce combinations of these mechanisms. Confidence: **96%**; evidence basis: diversity coverage and the FPF bounded-exploration rule.

The next decision is not “copy Hindsight or not.” It is: **which CAPRMEDIO problem should be solved first—cross-session orientation, recurring-signal discovery, or richer retrieval—and what privacy/authority envelope applies?** Once the operator chooses that target, the selected candidate should receive a design challenge and then CAPRMEDIO-native Concern/Analysis/Requirement/Evaluation work. No candidate is approved by this report.

## Open questions (confidence <95%)

### 90–94%: probable, but needs confirmation

- **C2 may already be partly covered by planned Graph App projections.** The inspected authority clearly defines Projections and selected graph-context routing, but this review did not trace every Graph App draft and implementation carrier. Confidence: **92%**. Confirmation: inventory current Projection generators and Graph App query/view contracts before creating new authority.
- **C1 probably belongs in the existing continuous-improvement/session-review path rather than a new core subsystem.** Current requirements already route field facts to exploration and derive retrospective correction signals. Confidence: **94%**. Confirmation: trace their active Methods, Evaluations, and implementations after the current migration settles.
- **C4 may be expressible through existing project and structural-scope identities instead of introducing a “bank” abstraction.** Confidence: **93%**. Confirmation: test whether derived-index isolation can be defined entirely with current scope coordinates and runtime envelopes.

### Below 90%: materially uncertain

- **Calendar cost is unknown.** Relative ordering is reliable, but implementation time depends on the unfinished Graph App, MCP, session-engine, and migration state. Confidence: **75%**. Confirmation: freeze a target set and inspect live implementation coverage before estimating.
- **Hybrid retrieval may not outperform simpler graph + lexical retrieval on CAPRMEDIO tasks.** Hindsight's published long-memory claims are not transferable to governed project work. Confidence: **65%**. Confirmation: build C6 first and compare retrieval variants on a commit-pinned CAPRMEDIO corpus and task set.
- **Legal clearance outside copyright and trademark is not established.** The MIT license is permissive but contains no explicit patent grant, and this review did not perform a patent, jurisdiction, or commercial-product clearance search. Confidence: **60%**. Confirmation: obtain qualified legal review before shipping a close commercial reimplementation or reusing substantial Hindsight code.
- **Whether raw Codex sessions should ever be retained continuously remains an operator policy decision.** The current CAPRMEDIO rule requires per-run approval for raw transcript review, which is intentionally stricter than Hindsight's documented default automatic recall and retain behavior. Confidence: **85%**. Confirmation: decide the admissible data classes, retention duration, deletion behavior, and consent UX before designing C5.

## Skills used

- `$fpf options explore`

#### FPF sources consulted (3 read; 2 used)

- `00_Hubs/FPF - First Principles Framework (FPF) - Core Conceptual Specification.md` — screened only; verified generated-source identity and revision.
- `B_Trans-disciplinary Reasoning Cluster/04_05_Canonical Reasoning Cycle/02_Abductive Loop/02_B.05.02.01 - Creative Abduction with NQD.md` — used; candidate diversity, provenance, bounded generation, and non-scalar selection.
- `G_Discipline SoTA Patterns Kit/10_09_Parity and Benchmark Harness/00_G.09 - Parity and Benchmark Harness.md` — used; pinned baselines, comparability limits, evidence trace, and partial-order reporting.

<oai-mem-citation>
<citation_entries>
MEMORY.md:1123-1123|note=[rediscovered the current FPF source before analysis]
MEMORY.md:1163-1163|note=[verified the live FPF knowledge graph repository]
</citation_entries>
<rollout_ids>
</rollout_ids>
</oai-mem-citation>
