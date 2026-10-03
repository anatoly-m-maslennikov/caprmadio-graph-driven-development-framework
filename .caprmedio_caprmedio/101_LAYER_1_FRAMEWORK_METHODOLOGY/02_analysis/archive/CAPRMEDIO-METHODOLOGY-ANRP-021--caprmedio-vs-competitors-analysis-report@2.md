---
artifact_subtype: analysis_report
version: 2
updated_at: 2026-08-18 22:44:59
llm_session_ids: []
---

# CAPRMEDIO vs. competitors analysis report

## Question and boundary

This report asks: as of 2026-08-02, what is materially similar and different between the current CAPRMEDIO/DSET repository and the current repositories for BMAD Method, Matt Pocock's Skills, and Superpowers; why do those differences exist; and which gaps are visible in CAPRMEDIO or the other projects?

The intended use is architectural and roadmap judgment. This report is analysis, not an accepted CAPRMEDIO Decision and not an adoption authorization.

The comparison covers repository-visible methodology, workflow, artifact model, orchestration, evaluation, runtime state, packaging, and adoption surfaces. It does not claim runtime behavior that was not executed, marketplace health, user counts, issue-response quality, enterprise support quality, or the behavior of external modules stored in other repositories.

## Executive judgment

These projects overlap, but they are not peers at one abstraction level:

- **CAPRMEDIO/DSET is primarily a governed project-truth, evaluation, and traceability substrate.** Its distinctive value is the separation of semantic authority, construction method, concrete implementation, evaluation obligations, delivery, operational facts, provenance, and derived views.
- **BMAD is primarily a broad, adaptive software-delivery product.** Its distinctive value is an approachable path from idea to working software, with optional planning depth, specialized perspectives, persistent context documents, a packaged installer, and an extensible module ecosystem.
- **Matt Pocock's repository is primarily a curated library of small engineering skills.** Its distinctive value is local control, composability, editable installation, strong domain-language practices, issue-tracker integration, and focused techniques such as grilling, wayfinding, TDD, and two-axis review.
- **Superpowers is primarily an enforced implementation methodology for coding agents.** Its distinctive value is behavior-shaping process discipline: mandatory skill selection, design approval, precise plans, isolated worktrees, TDD, fresh verification, subagent review, bounded repair loops, and wide harness distribution.

The strongest direction is therefore **composition, not replacement**: CAPRMEDIO can own durable authority and evidence; BMAD can be an optional product/solution-discovery front end; selected Matt skills can supply lightweight interviewing, domain-language, and tracker ergonomics; and Superpowers-like execution can become a strict implementation profile whose outputs are reconciled into CAPRMEDIO authority and Ops evidence.

The most urgent CAPRMEDIO problem is not missing conceptual depth. It is the distance between that depth and an executable, coherent, installable, currently documented product surface. The repository's own `check` command is broadly red, the live authority has moved beyond the root README, the active `dev` branch is far ahead of the public default branch, no release tag exists, and several accepted structural migrations remain open.

## Inputs and method

### Repositories and exact revisions

All four repositories were fetched on 2026-08-02. Existing clean external clones were fast-forwarded to upstream `main`. CAPRMEDIO was analyzed at the current fetched `dev` head because that is where the current CAPRMEDIO authority lives.

| Subject | Repository | Compared ref and commit | Nearest release tag | Checkout observation |
|---|---|---|---|---|
| CAPRMEDIO/DSET | [anatoly-m-maslennikov/dset-specs-loops-framework](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework) | `dev` at [`675bbe58056925e875042845376857d1431d1ace`](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/commit/675bbe58056925e875042845376857d1431d1ace) | None | Clean; `origin/dev` matched; `origin/main` was at `4c12de8` and the histories differed by 4 commits on `main` versus 704 on `dev` |
| BMAD | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | `main` at [`d25a307e71989c29438f8d2a95c644ea801b4e48`](https://github.com/bmad-code-org/BMAD-METHOD/commit/d25a307e71989c29438f8d2a95c644ea801b4e48) | `v6.10.0` | Clean and synchronized; 51 commits after the tag |
| Matt Pocock Skills | [mattpocock/skills](https://github.com/mattpocock/skills) | `main` at [`2ab958093e83e0ec752e6c1c5932da465bf23e0c`](https://github.com/mattpocock/skills/commit/2ab958093e83e0ec752e6c1c5932da465bf23e0c) | `v1.1.0` | Clean and synchronized; 42 commits after the tag |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | `main` at [`44c9b2d6e889982ac18c27d05a19fefe335194e1`](https://github.com/obra/superpowers/commit/44c9b2d6e889982ac18c27d05a19fefe335194e1) | `v6.2.0` | Clean and synchronized; one commit after the tag |

Repository-scale signals are descriptive, not quality scores: CAPRMEDIO contained 19 `SKILL.md` files, BMAD 57, Matt 41, and Superpowers 14. CAPRMEDIO had no native plugin manifest, BMAD had a Claude plugin surface, Matt had Claude plugin packaging plus Codex metadata but explicitly deferred a native Codex plugin, and Superpowers shipped multiple harness manifests.

### Comparison method

The analysis used a function-first comparison across eleven dimensions: purpose, control philosophy, conceptual model, lifecycle selection, artifact/state model, planning, implementation, evaluation, orchestration, distribution, and adoption maturity. Claims were checked against exact repository files, current Git state, and an independent read-only evidence lane. A capability is described as absent only when it was not evidenced in the inspected current repository surface; this is not a universal proof that no related implementation exists elsewhere.

### Important currentness correction for CAPRMEDIO

The root README is not current authority at this commit. It still describes three revision modes and seven Content roles and says the complete route/type catalog is undefined ([README lines 25–47](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/README.md#L25-L47)). Current accepted META instead defines Atom, Journal, and Projection, retires `revision_mode` as the primary classification axis, and keeps semantic role independent ([META-080 lines 22–42](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/100_LAYER_1_META/decision/CAPRMEDIO-META-REQU-248--three-artifact-forms.md#L22-L42)). It defines eight Content roles, including distinct Delivery and Ops roles ([META-086 lines 24–51](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/100_LAYER_1_META/decision/CAPRMEDIO-META-REQU-254--eight-content-roles-with-delivery-and-ops.md#L24-L51)), and explicitly says the 72-coordinate classification space does not require 72 top-level Types ([META-089 lines 26–44](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/100_LAYER_1_META/decision/CAPRMEDIO-META-REQU-257--coordinate-artifacts-without-a-72-type-bijection.md#L26-L44)). GOV-138 resolves the archived full-catalog Problem and Question by registering the currently admitted Atom surface ([GOV-138 lines 25–60](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/200_LAYER_2_GOV/decision/CAPRMEDIO-GOV-REQU-470--register-current-atom-type-surface.md#L25-L60)).

This report therefore uses the live accepted atoms as CAPRMEDIO's semantic source of truth and treats the README mismatch as a finding.

## Comparison matrix

| Dimension | CAPRMEDIO/DSET | BMAD Method | Matt Pocock Skills | Superpowers |
|---|---|---|---|---|
| Primary objective | Make AI-assisted work reviewable through governed truth, explicit semantics, proof, provenance, and supportability | Turn ideas or changes into working software with process depth matched to complexity | Supply small, adaptable engineering techniques without owning the whole process | Make coding agents follow a reliable end-to-end implementation discipline |
| Primary unit | Governed artifact with Type/subtype, form, role, locus, scope, provenance, and lifecycle | Workflow plus the documents it produces and passes forward | Independently invocable skill plus repository conventions and tracker state | Mandatory process skill plus spec, plan, Git/worktree state, and review scratch data |
| Control philosophy | Authority and effects are explicit; workflows fail closed and stop at authorization boundaries | Guided collaboration; the human keeps important decisions while workflows preserve context | Human control and local editability; explicitly rejects a process-owning framework | Strongly prescriptive behavior shaping; relevant skills and gates are mandatory by default |
| Lifecycle model | State-driven mode selection; no universal end-to-end order; prerequisite closure is bounded and authorization-aware | Four optional-depth phases: Analysis, Planning, Solutioning, Implementation; direct build is allowed | No framework-wide lifecycle; users compose skills, issues, and tracker transitions | Fixed default chain from brainstorming and approval through plans, worktree, TDD, reviews, and branch completion |
| Intent model | Concern → Analysis → realization-agnostic Requirement; Method, Delivery, and Implementation remain distinct | Brief/PRD/UX/METHODOLOGY; the five-field METHODOLOGY kernel is the machine contract | Grilling/domain work, then a spec issue that includes solution, implementation, and testing decisions | Collaborative design document approved by the user before implementation planning |
| Planning model | Separate proof planning and dependency-ordered implementation planning; accepted atoms may compile into projections | Architecture, epics/stories, readiness gate, sprint status; depth increases with project size | Tracer-bullet issues with blocking edges; Wayfinder resolves decision tickets under fog of war | Highly concrete plan with exact files, code, commands, task boundaries, and handoff to execution |
| Execution model | `ca-implement` supports strict or bounded lazy prerequisite closure; thin skills resolve project-local governance | `bmad-build` converges direct intent and planned work; `bmad-build-auto` supports unattended loops | `/implement` orchestrates `/tdd`, tests, `/code-review`, and commit | Per-task implementer/reviewer loop or inline plan execution, normally in an isolated worktree |
| Evaluation | Mechanism-neutral QA Cases and Evaluation Controls; separate Test and Evaluation implementations; Ops stores factual results | Readiness, review lenses, retrospectives, tests, and optional Test Architect module | TDD at agreed public seams plus separate Standards and Spec review axes | Strict red/green TDD, systematic debugging, fresh verification, per-task review, final review, and bounded fix rounds |
| Durable state | Atoms, Journals, non-authoritative Projections, relations, provenance, project-local control plane, runtime records | PRDs, specs, architecture, project context, memlogs, stories, sprint status | `CONTEXT.md`, ADRs, tracker issues, maps, decision tickets, local scratch issues | Committed specs/plans and Git history; plan-scoped scratch ledger/review packages are deleted after clean completion |
| Orchestration | Provider-neutral wrappers, explicit router/specialists, configurable bounded delegation, project-local rule resolution | Specialized agents, configurable skills, party mode, review lenses, optional subagents and modules | User-invoked vs model-invoked skills; selective subagents for research/review | Bootstrap-driven automatic selection and explicit implementer/reviewer dispatch with model-tier guidance |
| Distribution | Python package/CLI plus copy-based Codex and Claude host distribution; source explicitly disclaims install/release proof | `npx bmad-method install`, npm package, web bundles, docs site, official modules | Claude plugin or `npx skills` editable copies; native Codex plugin deferred | Official/marketplace plugins and extensions across many coding-agent harnesses |
| Best fit | Regulated, long-lived, multi-run, or high-consequence projects needing durable authority and auditability | Teams wanting a complete but right-sized product-delivery method | Experienced engineers wanting a toolkit they can adapt without surrendering workflow control | Teams wanting agents to execute code changes with strong default discipline and minimal process choice |

## What is similar

### 1. All four respond to the same family of coding-agent failures

Each project assumes raw conversational coding is insufficient because agents can misread intent, lose context, write prematurely, produce weak tests, or claim completion without evidence.

- CAPRMEDIO connects domain truth, decisions, proof, supportability, and evidence rather than letting chat become authority ([CAPRMEDIO README lines 3–10](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/README.md#L3-L10)).
- BMAD says coding assistants turn unstated assumptions into code, so it makes decisions explicit and preserves them as downstream context ([BMAD README lines 25–35](https://github.com/bmad-code-org/BMAD-METHOD/blob/d25a307e71989c29438f8d2a95c644ea801b4e48/README.md#L25-L35)).
- Matt identifies misalignment, missing feedback loops, weak shared language, and codebase entropy as the recurring failures his skills address ([Matt README lines 84–182](https://github.com/mattpocock/skills/blob/2ab958093e83e0ec752e6c1c5932da465bf23e0c/README.md#L84-L182)).
- Superpowers refuses immediate coding, requires a reviewed design and plan, and then runs an implementation/review process ([Superpowers README lines 10–20](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/README.md#L10-L20)).

### 2. All four turn conversation into durable artifacts

The artifacts differ in authority, but every project externalizes important state from chat. CAPRMEDIO uses governed carriers; BMAD produces briefs, PRDs, a canonical METHODOLOGY, architecture, stories, and status; Matt uses specs, issues, ADRs, `CONTEXT.md`, and Wayfinder maps; Superpowers commits design and plan documents and uses Git plus a plan-scoped ledger during execution.

This similarity exists because agent sessions are bounded and conversational memory is unreliable. Superpowers states the failure concretely: after compaction, controllers can re-dispatch completed work, so the process uses a plan-scoped ledger and Git rather than memory ([SDD lines 110–140](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/subagent-driven-development/SKILL.md#L110-L140)). CAPRMEDIO generalizes that concern into durable identities, lineage, authority ownership, and proof freshness.

### 3. All four separate understanding, planning, implementation, and checking

The names and rigidity differ, but none recommends an undifferentiated “prompt then code” flow. CAPRMEDIO has distinct `clarify`, `decisions`, `compile`, `plan-proof`, `plan-implementation`, `implement`, and `verify` entries ([lifecycle orchestration lines 63–89](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/14_layer_skill/090_dset-skill-procedure-lifecycle-orchestration.md#L63-L89)). BMAD progressively builds context across four phases and lets clear work enter Build directly ([workflow map lines 31–107](https://github.com/bmad-code-org/BMAD-METHOD/blob/d25a307e71989c29438f8d2a95c644ea801b4e48/docs/reference/workflow-map.md#L31-L107)). Matt separates grilling/domain work, spec synthesis, tickets, implementation, TDD, and review ([Matt README lines 184–213](https://github.com/mattpocock/skills/blob/2ab958093e83e0ec752e6c1c5932da465bf23e0c/README.md#L184-L213)). Superpowers makes the stages mandatory ([Superpowers README lines 196–212](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/README.md#L196-L212)).

### 4. All four value human judgment and explicit stop/gate points

CAPRMEDIO treats authorization as an invariant and stops before a new effect class. BMAD emphasizes guided collaboration and keeping important decisions with the user. Matt's grilling makes factual lookup the agent's job but reserves decisions for the human ([grilling lines 6–12](https://github.com/mattpocock/skills/blob/2ab958093e83e0ec752e6c1c5932da465bf23e0c/skills/productivity/grilling/SKILL.md#L6-L12)). Superpowers hard-gates implementation until the design and written spec are approved ([brainstorming lines 8–32](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/brainstorming/SKILL.md#L8-L32)).

### 5. All four use skills as a portable agent-facing unit

Each repository packages behavior into skills, tries to separate reusable instructions from harness-specific mechanics, and supports some form of host adaptation. CAPRMEDIO's core wrappers are provider-neutral and currently claim only Codex and Claude adapters ([skills README lines 7–22](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/skills/README.md#L7-L22)). Matt distinguishes human-only from model-reachable invocation in both Claude and Codex metadata ([invocation lines 1–16](https://github.com/mattpocock/skills/blob/2ab958093e83e0ec752e6c1c5932da465bf23e0c/.agents/invocation.md#L1-L16)). Superpowers keeps skill bodies harness-agnostic and translates actions through per-harness adapters ([porting guide lines 31–77](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/docs/porting-to-a-new-harness.md#L31-L77)).

## What is different, and why

### 1. Governed semantics versus delivery context versus technique versus enforced behavior

CAPRMEDIO asks, “What kind of governed thing is this, who owns its meaning, what may change it, what proves it, and what happened when it ran?” That forces an orthogonal semantic model: Artifact form × Content role × Governance locus, plus structural scope and provenance. Current authority defines eight roles—Concern, Analysis, Requirement, Method, Evaluation, Delivery, Implementation, and Ops—and keeps Requirements realization-agnostic ([META-086 lines 24–55](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/100_LAYER_1_META/decision/CAPRMEDIO-META-REQU-254--eight-content-roles-with-delivery-and-ops.md#L24-L55), [META-112 lines 20–49](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/100_LAYER_1_META/decision/CAPRMEDIO-META-REQU-104--keep-requirements-realization-agnostic.md#L20-L49)).

BMAD asks, “How much process does this change need, and what context will the next workflow need?” Its documents are therefore phase outputs and context carriers. The canonical METHODOLOGY deliberately compresses intent into Why, Capabilities, Constraints, Non-goals, and Success signal, while architecture and story work handle the solution ([BMAD workflow map lines 46–80](https://github.com/bmad-code-org/BMAD-METHOD/blob/d25a307e71989c29438f8d2a95c644ea801b4e48/docs/reference/workflow-map.md#L46-L80)).

Matt asks, “Which small engineering technique would improve this situation without taking control away from the engineer?” The repository explicitly contrasts its approach with GSD, BMAD, and Spec-Kit, preferring small, adaptable, composable skills ([Matt README lines 15–19](https://github.com/mattpocock/skills/blob/2ab958093e83e0ec752e6c1c5932da465bf23e0c/README.md#L15-L19)).

Superpowers asks, “How do we force the agent to behave reliably?” It therefore uses strong mandates: invoke applicable skills before action, brainstorm before planning, use TDD before production code, and require fresh verification before claims ([using-superpowers lines 10–31](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/using-superpowers/SKILL.md#L10-L31), [verification lines 10–35](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/verification-before-completion/SKILL.md#L10-L35)).

### 2. Flexibility is implemented at different layers

- **CAPRMEDIO** is semantically strict but workflow-flexible. It recommends the first useful state-driven mode, allows only a bounded prerequisite closure, and stops at exit or authorization boundaries; it explicitly says every Change need not execute every mode ([lifecycle lines 5–53](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/14_layer_skill/090_dset-skill-procedure-lifecycle-orchestration.md#L5-L53)).
- **BMAD** is product-flow flexible. Small changes go to Build; complex work adds analysis, planning, architecture, and readiness ([BMAD README lines 3–19](https://github.com/bmad-code-org/BMAD-METHOD/blob/d25a307e71989c29438f8d2a95c644ea801b4e48/README.md#L3-L19)).
- **Matt** is composition-flexible. There is no universal lifecycle; the engineer selects skills and owns the resulting local process.
- **Superpowers** is intentionally inflexible at the process layer. It says even a single-function utility or config change must pass a design gate, although the design may be short ([brainstorming lines 12–18](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/brainstorming/SKILL.md#L12-L18)).

These differences are philosophical, not accidental. CAPRMEDIO protects authority; BMAD protects contextual continuity while right-sizing effort; Matt protects practitioner agency; Superpowers protects execution behavior by reducing discretion.

### 3. Evaluation depth and meaning differ

CAPRMEDIO has the broadest semantic evaluation model. A mechanism-neutral QA Case can have distinct Test and Evaluation implementations, while execution results are Ops; continuous Evaluation Controls are distinct from bounded QA ([GOV-139 lines 20–53](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/200_LAYER_2_GOV/decision/CAPRMEDIO-GOV-REQU-317--register-evaluation-atom-subtypes.md#L20-L53)). This allows deterministic tests, qualitative or probabilistic evaluations, operational monitors, and factual results to remain related without collapsing their meanings.

BMAD has broad workflow evaluation—validation, readiness, review lenses, retrospectives, and executable tests—but the deepest risk-based test strategy and traceability are positioned in the separate Test Architect module ([modules lines 59–72](https://github.com/bmad-code-org/BMAD-METHOD/blob/d25a307e71989c29438f8d2a95c644ea801b4e48/docs/reference/modules.md#L59-L72)).

Matt is strongest at test seams and separating standards compliance from spec compliance. Its TDD skill requires public-interface tests at pre-agreed seams ([TDD lines 8–35](https://github.com/mattpocock/skills/blob/2ab958093e83e0ec752e6c1c5932da465bf23e0c/skills/engineering/tdd/SKILL.md#L8-L35)), and its review keeps Standards and Spec as independent axes ([code review lines 6–32](https://github.com/mattpocock/skills/blob/2ab958093e83e0ec752e6c1c5932da465bf23e0c/skills/engineering/code-review/SKILL.md#L6-L32)). It does not evidence a repository-wide qualitative-evaluation or proof-currentness model.

Superpowers is strongest at immediate execution proof. It requires observing red before green, re-running complete verification, and checking agent output rather than trusting a report ([TDD lines 31–45](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/test-driven-development/SKILL.md#L31-L45), [verification lines 22–48](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/verification-before-completion/SKILL.md#L22-L48)). Its evaluation is operationally strict but semantically thinner than CAPRMEDIO's Test/Evaluation/Ops distinction.

### 4. Persistence and provenance differ

CAPRMEDIO intends project-local authority with stable identities, explicit relations, immutable admitted claims, journals, rebuildable projections, Git/forge ownership boundaries, and proof staleness. BMAD persists context in documents and memlogs; Matt persists domain language, ADRs, and tracker issues; Superpowers persists final truth in committed specs, plans, code, and Git, but treats execution ledgers and review packages as temporary scratch that is deleted after a clean final review ([SDD lines 117–140](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/subagent-driven-development/SKILL.md#L117-L140)).

This is a fundamental gap boundary: the other systems preserve enough context to continue work; CAPRMEDIO aims to preserve enough semantics and provenance to explain, audit, invalidate, and re-prove work later.

### 5. Distribution maturity is inverted relative to semantic depth

CAPRMEDIO has the deepest governance model but the weakest public install/release surface. Its own source catalog says the 19 packages passing static audit does not prove host invocation, publication, or cross-platform execution ([skills README lines 51–85](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/skills/README.md#L51-L85)).

BMAD packages a public npm installer, docs site, web bundles, and modules ([BMAD README lines 11–58](https://github.com/bmad-code-org/BMAD-METHOD/blob/d25a307e71989c29438f8d2a95c644ea801b4e48/README.md#L11-L58)). Matt offers a managed Claude plugin or editable `npx skills` copies, while explicitly deferring a native Codex plugin because the current bucket structure cannot express a curated promoted subset ([plugin ADR lines 1–28](https://github.com/mattpocock/skills/blob/2ab958093e83e0ec752e6c1c5932da465bf23e0c/.agents/adr/0002-ship-as-a-claude-code-plugin.md#L1-L28)). Superpowers has the widest evidenced harness surface, including official Codex and Claude marketplace paths and many other integrations ([Superpowers README lines 26–194](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/README.md#L26-L194)).

## Detailed gap analysis

### CAPRMEDIO gaps

#### P0 — The public explanatory surface contradicts current authority

The root README currently presents the retired primary classification, says there are seven roles rather than eight, and points to archived Problem/Question paths as active boundaries. GOV-138 explicitly records `CAPRMEDIO-GOV-CONC-037--semantic-route-catalog-remains-incomplete` and `CAPRMEDIO-GOV-CONC-051--which-types-complete-the-semantic-route-catalog` as resolved, yet the README still says there is no canonical full type matrix and links to their former active paths.

Why this matters: a framework that makes authority and currentness first-class cannot ask adopters to infer that its most visible documentation is stale. This is not cosmetic; it changes the declared artifact model.

Needed closure: update the README and navigation from current atoms, add a deterministic check that README/hub links resolve and that summary claims cite active authority, and make the generated versus manually maintained status of overview documents explicit.

#### P0 — The current self-check fails broadly

At the analyzed `dev` HEAD, `uv run python -m dset_toolchain check .` exited 1. The run emitted 1,735 coded errors: 4 `CAPRMEDIO-E121`, 12 `E139`, 2 `E157`, 493 `E158`, 1,222 `E168`, and 2 `E169`, plus an environment-lock warning. The visible categories included missing or ambiguous META/GOV hubs, installed local rules changed without custom status, obsolete governance-surface settings, invalid projection and relation shapes, unresolved artifact identities, and historical commit-provenance references to retired IDs.

Why this matters: CAPRMEDIO's main differentiator is executable governance and fail-closed validation. A broad red self-hosting state means the conceptual authority cannot currently be presented as an enforced repository contract. It also caps conclusions from static tests or source presence: the canonical end-to-end checker itself rejects the current control plane.

Needed closure: establish a migration-aware validator baseline, separate genuinely current defects from explicitly bounded historical-backlog diagnostics, restore hub/settings/rule resolution first, then migrate relations and provenance in deterministic batches until the canonical check is green. Do not weaken the validator merely to reduce the count; make any intentional degraded evaluation explicit and bounded.

#### P0 — The current product is not available from the public default/release path

The fetched public default branch was `main`, but current CAPRMEDIO work was on `dev`, with a 4-versus-704 commit divergence and no tag. The Python package declares version `0.3.1` and command `dset` ([pyproject lines 5–22](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/pyproject.toml#L5-L22)), but source presence explicitly disclaims release or host proof.

Why this matters: external users cloning the default branch do not receive the current model analyzed here. Documentation, Git default state, package version, tag, release, and host receipts do not form one coherent current release.

Needed closure: reconcile `dev` and `main` through the declared delivery process, produce a tagged release at one verified SHA, publish install instructions tied to that release, and record host smoke evidence separately from static source audit.

#### P0 — Accepted structural semantics are not implemented physically

Three active Problems already state the gap accurately:

- the installed methodology, applied authority, and reusable root still use the retired TOOL → SKILL → IMPLEMENTATION topology instead of META → GOV → METHODOLOGY → PROFILES → IMPL → OPS ([Problem GOV-010 lines 17–42](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/200_LAYER_2_GOV/problem/CAPRMEDIO-GOV-CONC-013--control-plane-uses-retired-layer-layout.md#L17-L42));
- active atoms remain grouped in legacy family directories rather than Type-local roots ([Problem GOV-011 lines 21–48](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/200_LAYER_2_GOV/problem/CAPRMEDIO-PROBLEM-GOV-011-atomic-carriers-are-not-type-local.md#L21-L48)); and
- filenames and relations still use the retired atomic identity grammar ([Problem GOV-012 lines 21–54](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/200_LAYER_2_GOV/problem/CAPRMEDIO-GOV-CONC-015--atomic-identities-use-retired-grammar.md#L21-L54)).

Why this matters: the conceptual model is ahead of the discoverable filesystem, validator, and user mental model. Every additional artifact created under the old layout increases migration cost.

Needed closure: execute the three migrations as one graph-safe program with replay, collision, reference, digest, archive, and installed-source synchronization proofs before expanding the catalog further.

#### P1 — Distribution is implemented as source and copy workflow, not yet as a proven product experience

CAPRMEDIO has a real Python CLI, cross-platform delivery policy, 19 wrapper sources, and host-distribution workflow. The gap is the final mile: no native plugin manifest is present; only Codex and Claude adapters are claimed; and the documentation explicitly withholds host proof.

Compared with BMAD and Superpowers, an adopter must understand more of the framework before experiencing one successful governed change. This raises activation energy and hides CAPRMEDIO's strongest value.

Needed closure: one five-minute quickstart against a tiny fixture repository, a single install/update/uninstall story, native plugin packaging where appropriate, version-pinned receipts, and clean-session acceptance transcripts for the supported hosts.

#### P1 — CAPRMEDIO specifies orchestration more strongly than it packages implementation ergonomics

The lifecycle and delegation rules are sophisticated: bounded lazy closure, strict mode, persisted criterion state, model/effort attestation, and configurable budgets. Yet the skills are intentionally thin and rely on repository-local governance. That is correct for authority but means CAPRMEDIO does not yet provide the same immediately tangible execution experience as BMAD's Build or Superpowers' task/review/fix loop.

Needed closure: ship an optional, governed implementation profile with worktree policy, plan-scoped progress ledger, compact task briefs, review packages, per-task conformance/quality gates, bounded repair rounds, and final verification. Keep these as Method/Evaluation/Implementation profiles, not universal META rules.

#### P1 — External review import and proof currentness remain unresolved

The active external-review Question asks for the minimum identity, provenance, scope, finding, and disposition envelope while keeping native bodies free-form ([Question GOV-015 lines 17–33](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/200_LAYER_2_GOV/question/CAPRMEDIO-GOV-CONC-053--what-external-review-envelope-is-sufficient.md#L17-L33)). The proof-currentness Question asks whether to keep dependencies as judgment-reviewed prose or derive a non-authoritative closure view ([Question GOV-016 lines 18–30](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/blob/675bbe58056925e875042845376857d1431d1ace/.caprmedio/200_LAYER_2_GOV/question/CAPRMEDIO-GOV-CONC-054--how-should-proof-currentness-be-represented.md#L18-L30)).

Why this matters: these are exactly the contracts needed to ingest BMAD reviews, Matt review axes, Superpowers review packages, CI results, external audits, and model evaluations without laundering them into project authority.

Needed closure: prioritize these questions before claiming robust interoperability with other agent frameworks.

#### P2 — Naming and product identity are fragmented

The repository is called `dset-specs-loops-framework`, the README says DSET Spec Loops, the Python package is `dset-spec-loops`, the command is `dset`, the applied control plane and skill catalog say CAPRMEDIO, and many source filenames still start with `dset`.

Why this matters: the distinction may be meaningful internally, but it is not explained as a stable public product architecture. Users cannot easily tell whether CAPRMEDIO is the method, control plane, successor name, artifact language, or product built on DSET.

Needed closure: publish one short naming contract and migration policy. Retain multiple names only if each has one unambiguous responsibility.

#### P2 — The public onboarding and ecosystem surfaces are thin

CAPRMEDIO has detailed specifications, templates, tests, and internal delivery policy, but it does not evidence BMAD's tutorial/module/community surface or Superpowers' harness-by-harness installation coverage. Specialized product, UX, research, and testing roles are not the core product.

This is not necessarily a semantic defect. The gap is adoption leverage. CAPRMEDIO should prefer adapters and profiles over recreating every specialist workflow.

### BMAD gaps relative to CAPRMEDIO

#### Durable semantic authority and provenance are not first-class

BMAD preserves decisions as downstream context, and the METHODOLOGY is a canonical machine contract within its workflow. The inspected repository does not evidence an equivalent orthogonal artifact model, immutable admitted claims, explicit governance locus, type-derived semantics, or proof-currentness closure.

Consequence: BMAD is easier to use as a delivery method but weaker as a long-lived audit substrate when several documents, sessions, external authorities, tests, evaluations, and operational results disagree.

#### Evaluation depth is partly modular

Core BMAD includes review, readiness, retrospective, and tests, but advanced risk-based strategy, NFR assessment, automation, and traceability are delegated to the external TEA module. A user comparing only the BMAD-METHOD repository should not assume CAPRMEDIO-equivalent proof semantics.

#### Supportability and Ops are not a primary semantic axis

BMAD has implementation learning and retrospective artifacts, but the inspected core does not treat runtime evidence, logs, incidents, delivery outcomes, and verification outcomes as one independently governed Content role. This matters for production systems where explanation and repair after release are as important as delivery.

#### Breadth and rendering indirection increase system complexity

BMAD's 57 skill files, installer, configuration merge layers, generated workflows, modules, web bundles, multilingual docs, and mixed Node/Python toolchain create a large maintenance surface. The current `bmad-build` entry is deliberately a thin renderer into generated workflow instructions ([Build skill lines 1–13](https://github.com/bmad-code-org/BMAD-METHOD/blob/d25a307e71989c29438f8d2a95c644ea801b4e48/src/bmm-skills/ship/bmad-build/SKILL.md#L1-L13)). This is powerful but makes behavior harder to audit from the invoked skill alone.

### Matt Pocock Skills gaps relative to CAPRMEDIO

#### Framework-wide consistency is intentionally absent

The repository's central promise is small, adaptable, composable skills rather than a process owner. That makes it easy to adopt selectively but means lifecycle, authority, provenance, retention, and proof policy depend on each repository and practitioner.

#### The spec carrier mixes outcome and realization concerns

Matt's `to-spec` template includes Problem, Solution, User Stories, Implementation Decisions, and Testing Decisions in one issue ([to-spec lines 21–73](https://github.com/mattpocock/skills/blob/2ab958093e83e0ec752e6c1c5932da465bf23e0c/skills/engineering/to-spec/SKILL.md#L21-L73)). This is pragmatic for execution, but it conflicts with CAPRMEDIO's requirement that independently replaceable outcomes, Methods, Delivery rules, and Implementations remain separate.

Consequence: when architecture or delivery changes without changing the required outcome, the combined spec is more likely to become stale or require broad editing.

#### Evaluation is code-centric and currentness is informal

TDD and two-axis review are strong. The inspected repo does not evidence a framework-wide distinction between deterministic tests and qualitative/probabilistic evaluations, nor a durable mapping from proof results to exact governed inputs and invalidation triggers.

#### Native Codex packaging remains deferred

Codex users have a valid `skills.sh` path and OpenAI metadata, but the repository explicitly defers a native Codex plugin because its bucket layout and Codex's single-path manifest do not express the promoted subset cleanly.

### Superpowers gaps relative to CAPRMEDIO

#### The mandatory workflow can over-process low-risk work

Superpowers says every creative project, including small utilities and config changes, must pass brainstorming and design approval; TDD is the default iron law for features, fixes, refactors, and behavior changes. This aggressively reduces agent improvisation but can add latency and ceremony where a project's evidence supports a smaller path.

This is the mirror image of CAPRMEDIO's gap: Superpowers has excellent default behavior but less semantic right-sizing; CAPRMEDIO has state-driven right-sizing but less packaged behavior.

#### Execution records are deliberately temporary

The plan-scoped SDD workspace solves cross-plan contamination and resume failures, but it is deleted after clean final review, leaving Git history as the record. That is sufficient for execution recovery but weaker than a queryable durable graph of requirement, method, task, review, proof input, result, and invalidation.

#### Product discovery, external authority, qualitative evaluation, delivery, and Ops are not first-class

Superpowers has brainstorming, specs, plans, code review, debugging, and verification. The inspected core does not evidence CAPRMEDIO-like external governance loci, separate Evaluation implementations, delivery semantics, or operational evidence/incident carriers.

#### The review loop can be expensive and harness-dependent

The SDD workflow uses an implementer, per-task reviewer, scoped re-reviews, a final reviewer, and bounded fix waves ([SDD lines 45–107](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/subagent-driven-development/SKILL.md#L45-L107)). It now includes explicit model-tier and turn-cost guidance ([SDD lines 157–187](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/skills/subagent-driven-development/SKILL.md#L157-L187)), but the process still assumes a capable subagent runtime for its strongest path. Porting also requires reliable skill discovery and, for non-native harnesses, an always-on bootstrap mechanism ([porting guide lines 81–122](https://github.com/obra/superpowers/blob/44c9b2d6e889982ac18c27d05a19fefe335194e1/docs/porting-to-a-new-harness.md#L81-L122)).

## Recommended direction for CAPRMEDIO

### Sequence 1 — Make current authority legible and releasable

1. Correct the README and hubs from current atoms; remove stale links and retired semantic claims.
2. Restore the canonical self-check through an explicit migration-aware remediation sequence.
3. Publish the DSET/CAPRMEDIO naming contract.
4. Complete the topology, Type-local carrier, and identity migrations as one graph-safe change.
5. Reconcile `dev` to `main` through the protected delivery path and cut one tagged, installable release.
6. Prove a clean install and one small governed change on each claimed host.

This sequence should precede broad feature growth. It turns the existing conceptual advantage into something an adopter can reliably obtain.

### Sequence 2 — Add an optional execution profile, not a universal process law

Borrow the strongest operational patterns from Superpowers: isolated workspaces, plan-scoped ledgers, compact task briefs, fixed-base review packages, per-task spec/quality review, fresh verification, bounded repair rounds, and safe branch completion. Represent them as CAPRMEDIO Method, Evaluation, Implementation, and Ops artifacts under an optional profile. Do not make one workflow mandatory for every Change.

### Sequence 3 — Add interoperability adapters

Define import mappings rather than trying to replace the other systems:

| External artifact | CAPRMEDIO interpretation |
|---|---|
| BMAD PRD/METHODOLOGY | Candidate Concern, Analysis, Requirements, and Non-goals; split Methods before admission |
| BMAD architecture/stories/sprint status | Method, implementation plan/tasks, and Projection/Ops as appropriate |
| Matt spec issue | Split Problem/Requirement from Implementation and Testing Decisions |
| Matt Wayfinder map and decision tickets | Planning Projection plus Concern/Analysis/Requirement or Method atoms when accepted |
| Matt Standards/Spec review | External review envelope with separate finding lenses and project disposition |
| Superpowers design and implementation plan | Candidate Requirement/Method and implementation-plan projection |
| Superpowers task ledger/review package | Temporary runtime state and imported review evidence; promote only selected durable facts |
| CI/test/eval output from any system | Ops result bound to exact implementation and Evaluation inputs |

Resolve the external-review envelope and proof-currentness questions before calling these adapters complete.

### Sequence 4 — Borrow product ergonomics selectively

- From **BMAD**, borrow a five-minute onboarding path, a canonical small machine-readable intent kernel, adaptive “direct build versus deeper planning” messaging, and modular specialized workflows.
- From **Matt**, borrow explicit user-invoked versus model-invoked skill metadata, editable local skill distribution, domain-language maintenance, Wayfinder's frontier/fog model, and native tracker adapters.
- From **Superpowers**, borrow concrete execution and verification discipline plus real multi-harness acceptance tests.

The borrowing rule should be: import ergonomics and evidence-producing mechanisms, but keep CAPRMEDIO's semantic ownership and authority boundaries.

## Bottom line

CAPRMEDIO is conceptually ahead of the other three in durable artifact semantics, authority separation, proof modeling, and operational provenance. It is behind them in executable self-consistency, public coherence, release state, installation simplicity, immediate execution ergonomics, and adoption surface.

BMAD is the most complete delivery product, Matt's skills are the most locally adaptable, and Superpowers is the most behaviorally prescriptive and execution-rigorous. None provides the same governed semantic substrate as current CAPRMEDIO; CAPRMEDIO does not yet provide their polished user journey.

The right competitive thesis is therefore not “CAPRMEDIO does everything they do.” It is: **CAPRMEDIO can be the authority and evaluation layer that lets those workflows coexist without turning their documents, agent reports, or runtime scratch state into unexamined truth.** To make that thesis credible, CAPRMEDIO must first close its own documentation, migration, release, and host-proof gaps.

## Consequences and refresh trigger

This analysis should be refreshed when any compared repository changes its major workflow or artifact model; when CAPRMEDIO resolves Problems GOV-010 through GOV-012 or Questions GOV-015/GOV-016; when CAPRMEDIO publishes a tagged release or native plugin; or after a real cross-framework fixture is executed and evaluated. A runtime benchmark or adopter trial may overturn conclusions about ergonomics, cost, reliability, and host compatibility that source inspection alone cannot establish.
