# FPF design challenge — CAPRMEDIO Realization Graph design

:codex-annotation{index="1"}

## Task, scope, and boundaries

### Outcome first

The proposed Realization Graph is viable and useful for both intended workflows, but not yet as a canonical two-level graph whose directories, files, declarations, and dependencies automatically become CAPRMEDIO project-graph nodes. The strongest design is a **non-authoritative Implementation Inventory Projection with a CAPRMEDIO-owned semantic contract and replaceable producers**. It observes native implementation structure and can be used as bounded evidence by Evaluation, Analysis, and legacy-adoption work; it never creates Project Scope Units, normative authority, conformance, or runtime truth by itself.

This challenge does not choose among `code-graph-rag`, `AppThreat/atom`, and a CAPRMEDIO-native producer. Those are producer options for the next comparison after the semantic contract is accepted. The Operator remains the decision owner.

### Proposal under challenge

The proposal is a programmatically built graph with:

- folders and files treated as first-layer code scopes;
- functions, classes, methods, interfaces, and similar declarations treated as second-layer nodes;
- imported libraries and external APIs represented as external nodes;
- typed containment, import, call, inheritance, implementation, and external-use relations;
- two intended uses:
  1. `RMED -> Implementation -> Realization Graph -> Evaluation`;
  2. `legacy code -> Realization Graph -> progressive creation of full RMED with AI Agent and Operator participation`.

### Inspected Project authority

The live repository already owns the relevant capability. `IMPLEMENTATION_INVENTORY` must derive reproducible as-is Projections of selected native Implementation carriers, directories, files, modules, declared dependencies, and detectable realization relations without turning observations into Analysis or authority ([R-708](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-708--define-implementation-inventory-tool-unit.md:14)). Its active Method explicitly preserves observations without interpreting directories as Areas or Features, files as governed Module scopes, or the result as project authority ([M-101](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/201_TOOLS/05_method/CA-M-101-IMPL_METHOD-FR_ENGN_TOOLS_IMPLEMENTATION_INVENTORY--build-the-as-is-implementation-inventory.md:13)). No native implementation currently exists in the Tool delivery place, so this proposal materially extends an accepted semantic boundary rather than duplicating a working tool.

The governing graph partitions every governed node into Scope Unit or Artifact ([R-834](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-834-REQUIREMENT-BSEED_METAMODEL--partition-project-graph-nodes.md:14)); Artifact forms are exactly Atom, Journal, and Projection, with only Atoms and Journals authoritative ([META-125](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections.md:17)). A Projection is an exact-frontier, reproducible, non-authoritative view ([META-657](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CAPRMEDIO-META-REQU-657--define-projection-artifact-form.md:15)). The one-graph Principle makes that typed graph the canonical representation of governed meaning and state, with vertices partitioned into Scope Units and Artifacts ([D-003](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/07_delivery/CA-D-003-PRINCIPLE-DELIVERY--provide-one-project-graph-as-the-operating-model.md:12)).

### Evaluation envelope

- **Campaign ID:** `RG-ARCH-20260823-01`
- **Campaign phase:** full design challenge complete; Operator disposition pending
- **Semantic frontier:** the proposal above; live `IMPLEMENTATION_INVENTORY` R-708 v5 and M-101 v2; live Project and Bootstrap Seed authority cited in this report
- **Carrier frontier:** Git `HEAD fd6e6e11d4e3f694c50c521d98d9aa490a28bdaa` plus a dirty working tree with 193 status entries; conclusions therefore bind the inspected live carriers rather than claiming a clean-commit snapshot
- **Predecessor:** `fpf-reports/20260822T224444Z-fpf-sota-harvest-realization-graph-repositories.md`, SHA-256 `3d5497a0ceb2a3e992b517ab7613fc972de6a958ace89e48201c3f4f70af6102`
- **Evaluation profile:** architecture-description adequacy; evidence/provenance separation; Entity-of-Concern-preserving projection; claim-bounded assurance; structural-correspondence adequacy
- **Excluded:** live execution of candidate repositories; language-specific extraction accuracy; performance and scale benchmarks; dependency installation; license dependency-tree verification; downstream schema and filename design
- **Finding states:** all concern findings remain `OPEN`; the producer-neutral boundary is `NO_CONCERN_WITHIN_INSPECTED_SCOPE`
- **Allowed next action:** Operator disposition of the proposed corrections, followed by the planned options comparison; do not repeat this full challenge unless the semantic frontier changes materially

## High-confidence results (>=95%)

### RG-DC-01 — Projection-internal code entities are not automatically governed project-graph nodes — concern (99%)

- **Proposal claim:** files, folders, functions, classes, methods, and interfaces can all be direct nodes of the canonical CAPRMEDIO graph.
- **Entity of Concern:** the identity and admission status of one observed native code entity.
- **Context and use:** both forward Evaluation and reverse legacy adoption.
- **FPF pattern and inspected Solution:** C.30.AD treats a generated graph as an architecture description with an exact Entity of Concern, selected structure, sources, freshness, losses, and admissible uses; A.10 keeps a descriptive evidence edge separate from the fact or authority it cites; A.6.3 prohibits unsupported strengthening during view construction.
- **Project evidence:** the graph admits only Scope Units and Artifacts; Artifact forms are Atom, Journal, and Projection. An Atom has an independently governed claim, scope, and lifecycle ([R-655](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-655-MMODEL-CORE-REQUIREMENT--define-atom-artifact-form.md:18)). A declaration discovered by a parser has none of those properties merely because it exists. The existing rationale says realized code artifacts belong in the operating graph ([ANRP-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/02_analysis/CAPRMEDIO-ANRP-002--the-operating-graph-includes-realized-project-nodes.md:15)), but it does not admit every declaration as an independent governed Artifact.
- **Inference:** the Realization Graph may itself be a governed Projection Artifact, and it may contain typed descriptive records referring to native entities. Those records do not automatically become new canonical graph-node kinds. A native carrier may be represented by an already admitted Implementation Artifact; declaration-level observations remain inside the Projection unless separately governed.
- **Consequence if unchanged:** the extractor would silently extend the Bootstrap Seed metamodel, create thousands of pseudo-Atoms without independent authority or lifecycle, and make parser output appear canonical.
- **Candidate correction:** define `Realization Graph` as an Implementation Inventory Projection. Define its internal elements as `observed implementation entities`, not CAPRMEDIO Scope Units or Artifacts. Bridge selected observations to existing Scope Units and Artifacts through explicit, provenance-bound relations. Admit a new canonical node kind only through a separate Bootstrap Seed change.
- **Unchecked dependency and stop condition:** the exact native-Implementation Artifact identity model still needs a bounded review. Stop this finding when the Operator accepts the Projection-internal/entity boundary or explicitly authorizes a metamodel extension.
- **Fingerprint/state:** `RG-DC-01|node-admission|projection-internal-vs-governed|OPEN`.

### RG-DC-02 — Native code containment and Project Scope Units are different structures — concern (100%)

- **Proposal claim:** folders and files are naturally first-layer scopes.
- **Entity of Concern:** the correspondence between one native container and one Project Scope Unit.
- **Context and use:** dependency enforcement between Features, legacy structure recovery, and navigation.
- **FPF pattern and inspected Solution:** C.34 requires the weakest adequate mapping, preserved and lost structure, directionality, and admissible use when two structures are treated as corresponding. Its code-agent example explicitly forbids using a partial dependency graph as safe-change authority.
- **Project evidence:** M-101 directly forbids interpreting directories as Areas or Features or files as governed Module scopes. Project Scope Units are normative ownership units; directory and file containment is observed realization structure.
- **Inference:** a Project Feature may map to several folders and files; one folder may contain realization for several Scope Units; generated, vendored, test, configuration, and deployment carriers may follow different boundaries. Neither direction is intrinsically one-to-one.
- **Consequence if unchanged:** a repository refactor would change project authority accidentally, while legacy folder conventions would be laundered into accepted Project structure.
- **Candidate correction:** keep two explicit graphs or partitions connected by declared correspondence: `Project Scope Unit Graph` and `Native Implementation Structure`. Bind correspondences through Implementation Journals or derived mappings, recording direction, source frontier, mapping method, confidence where inferred, and known loss. Never derive authority from path shape alone.
- **Unchecked dependency and stop condition:** the exact bridge relation vocabulary is outside this challenge. Stop when a Project Requirement accepts the separation and identifies the owner of the mapping contract.
- **Fingerprint/state:** `RG-DC-02|scope-correspondence|native-container-vs-project-unit|OPEN`.

### RG-DC-03 — “Two-layer graph” is a useful view but an inadequate canonical structure — concern (99%)

- **Proposal claim:** folders/files form layer 1 and declarations form layer 2.
- **Entity of Concern:** the selected structural view of the native implementation frontier.
- **Context and use:** human navigation, dependency queries, and producer interchange.
- **FPF pattern and inspected Solution:** A.6.3 permits a lighter view when it preserves the same Entity of Concern, declares its filter and omissions, and introduces no unsupported commitments. C.30.AD and C.34 require lost nesting and relations to remain explicit.
- **Project evidence:** the inventory already includes recursive directories, files, language-native modules, declared dependencies, and detectable realization relations. The accepted boundary does not flatten these into two structural levels.
- **Inference:** directories nest recursively; classes contain methods; functions may nest; interfaces, generated resources, schemas, and deployment objects are not all peers. External packages, modules, symbols, services, operations, and endpoints also have distinct identity layers.
- **Consequence if unchanged:** flattening loses containment and resolution detail needed for change-impact and legacy-adoption decisions, while the word “layer” risks confusion with normative ordered Scope Units.
- **Candidate correction:** call these **two faces or partitions**, not two levels: (1) recursive native carrier/container structure and (2) typed declaration/resource/dependency structure. Permit a human-facing two-band view, but retain full typed nesting and explicitly declare what that view drops.
- **Unchecked dependency and stop condition:** concrete language schemas are not inspected. Stop when the semantic contract uses recursive structures and reserves “two-layer” only for a declared Projection view.
- **Fingerprint/state:** `RG-DC-03|structural-view|two-band-not-two-level|OPEN`.

### RG-DC-04 — The graph is an Evaluation input, not generic conformance proof — concern (100%)

- **Proposal claim:** `RMED -> Implementation -> Realization Graph -> Evaluation` can evaluate implementation against RMED.
- **Entity of Concern:** one exact Evaluation conclusion about one exact Requirement, Method, Evaluation, or Delivery claim.
- **Context and use:** forward implementation acceptance and architecture-rule checking.
- **FPF pattern and inspected Solution:** A.10 says graph edges establish none of the facts they cite. B.03 requires an exact target claim and use, evidence basis, limitations, disposition, and reopen condition. C.34 makes structural correspondence use-relative and says a dependency graph cannot prove release readiness.
- **Project evidence:** accepted Requirements must have recoverable inputs, procedure, and binary result interpretation ([E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-accepted-requirements-checkable.md:12)); reliance requires every required input to be present, known, consistent, and valid ([E-206](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/06_evaluation/CA-E-206-EVAL_APPROACH--require-usable-inputs-for-reliance.md:14)). Requirements remain realization-agnostic, while code-facing choices belong to Method and operative mechanics to Implementation ([META-104](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-102_BSEED_LAYER_2_SEMANTICS/04_requirement/CAPRMEDIO-META-REQU-104--keep-requirements-realization-agnostic.md:34)).
- **Inference:** a graph can directly support structural checks only when an exact governing claim defines the relevant node/edge semantics. Other claims require tests, runtime observations, human Evaluation, or additional evidence.
- **Consequence if unchanged:** “edge present,” “edge absent,” or “mapping exists” could be mistaken for Requirement satisfaction, independence, correctness, or release readiness.
- **Candidate correction:** define four separate downstream uses: (1) traceability and coverage from Journal bindings; (2) static structural constraint checks against exact Method, Delivery, or Contract claims; (3) behavioral Evaluation from tests and runtime evidence; and (4) graph completeness/currentness checks. A missing required graph input produces no reliable conclusion or an Evidence-needed Concern; the final accepted Evaluation remains `pass` or `fail` only when its input boundary is satisfied.
- **Unchecked dependency and stop condition:** concrete Evaluation Types and relation-to-rule mappings remain unselected. Stop when each planned check names its governed target, procedure, complete required inputs, and binary interpretation.
- **Fingerprint/state:** `RG-DC-04|evaluation-boundary|graph-input-not-proof|OPEN`.

### RG-DC-05 — Static realization and runtime operation need separate views — concern (99%)

- **Proposal claim:** the generated graph represents the actual code and can expose actual dependencies.
- **Entity of Concern:** the program at an exact source revision versus one exact running realization.
- **Context and use:** dependency enforcement, operations, incidents, and release decisions.
- **FPF pattern and inspected Solution:** B.03 keeps design-time and run-time evidence separate; C.30.AD binds a description to its selected source and freshness; C.34 requires lost dynamic wiring and non-admissible uses to be stated.
- **Project evidence:** proof records must bind exact Artifact and Implementation revisions, configuration, evaluator, environment, and inputs ([GOV-353](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-103_BSEED_LAYER_3_GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-353--bind-proof-records-to-dependency-frontiers.md:16)). The operating graph rationale includes executions and operational facts, but does not collapse them into source structure.
- **Inference:** imports and statically resolved calls describe selected source structure. Reflection, dependency injection, configuration, build transforms, network routing, plugin loading, and environment behavior may produce a different runtime structure.
- **Consequence if unchanged:** static absence could be treated as runtime independence, and static possibility as actual execution.
- **Candidate correction:** define separate `Static Realization Structure Projection` and `Runtime Interaction Projection`, with an explicit correspondence or difference view. Every result names source/runtime frontier, observation class, and non-admissible use.
- **Unchecked dependency and stop condition:** runtime instrumentation and privacy/cost policy are outside scope. Stop when the common contract distinguishes `declared`, `resolved`, `inferred`, and `observed_runtime` relations and forbids cross-class inference without a rule.
- **Fingerprint/state:** `RG-DC-05|epistemic-class|static-vs-runtime|OPEN`.

### RG-DC-06 — Legacy code may propose RMED; it cannot recover or establish intent by itself — concern (100%)

- **Proposal claim:** a Realization Graph can help progressively create full RMED from legacy code.
- **Entity of Concern:** one proposed normative claim inferred from one selected legacy implementation frontier.
- **Context and use:** adoption of projects created before CAPRMEDIO.
- **FPF pattern and inspected Solution:** A.6.3 forbids a derived view from strengthening source commitments; A.10 separates evidence paths from truth and authority; C.34 requires preserved/lost structure and a bounded next use.
- **Project evidence:** Concern, Analysis, Task, and native Implementation may propose PRMEDO changes, but only Operator-approved PRMEDO authority establishes them ([META-148](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-102_BSEED_LAYER_2_SEMANTICS/04_requirement/CAPRMEDIO-META-REQU-148--allow-concern-analysis-plan-and-implementation-to-initiate-rmed-change.md:14)). Existing M-102 already treats native structure only as a heuristic for structural drafts and preserves ambiguity.
- **Inference:** code can reveal implemented structure and behavior hypotheses, but not reliably recover goals, requirements, rationale, rejected alternatives, intended boundaries, or obligations absent from the code.
- **Consequence if unchanged:** legacy accidents and temporary coupling would become normative design; absent behavior could be mistaken for prohibited behavior; inferred intent could bypass Operator authority.
- **Candidate correction:** use the pipeline `legacy frontier -> Implementation Inventory/Realization Projection -> Concern and Analysis -> draft or proposed PRMEDO -> Operator acceptance -> active authority`. Each inferred claim binds exact source entities, producer/model/configuration, confidence or uncertainty, counterevidence, and unresolved alternatives. No generated claim is promoted directly.
- **Unchecked dependency and stop condition:** the exact adequacy rules for generated structural discovery require FPF C.35 and a Project-owned adoption Method, neither inspected here. Stop the authority-boundary finding when the above transition is accepted; reopen discovery adequacy when C.35 and representative legacy cases are inspected.
- **Fingerprint/state:** `RG-DC-06|legacy-inference|proposal-not-authority|OPEN`.

### RG-DC-07 — A producer-neutral CAPRMEDIO contract is the right integration boundary — no concern found within inspected scope (98%)

- **Proposal claim:** CAPRMEDIO may implement its own graph builder or use an external repository.
- **Entity of Concern:** the semantic and carrier boundary between CAPRMEDIO and one graph producer.
- **Context and use:** both workflows and the later `code-graph-rag` versus `AppThreat/atom` versus native comparison.
- **FPF pattern and inspected Solution:** C.34 supports use-specific correspondence rather than forced equivalence; A.6.3 permits representation-scheme changes when meaning, loss, and source return remain explicit. A.05 was screened and supports a small core with explicit extension boundaries, but it is only an informative stub and is not relied upon for the conclusion.
- **Project evidence:** D-001 requires replaceable technical realizations; M-002 requires one canonical semantic owner; R-708 already gives `IMPLEMENTATION_INVENTORY` that ownership.
- **Inference:** the three candidates should not define three Realization Graph meanings. They should implement adapters to one CAPRMEDIO-owned output contract, and each may expose richer producer-native data outside the minimum portable view.
- **Consequence:** producer replacement, multi-language composition, and evidence comparison remain possible without rewriting Project authority.
- **Candidate correction:** register one minimum producer envelope containing exact source frontier and digest; producer identity/version; configuration; language and region coverage; typed node and edge identity; observation class; resolution status; confidence only where meaningful; omitted/unexplored regions; deterministic output identity; generation time; and invalidation/currentness conditions. Keep producer-native enrichments namespaced and optional.
- **Unchecked dependency and stop condition:** no candidate has been run. Stop this design finding when the common contract is accepted; then compare candidate coverage, precision, performance, operational burden, and license closure against it.
- **Fingerprint/state:** `RG-DC-07|producer-boundary|one-contract-replaceable-producers|NO_CONCERN_WITHIN_INSPECTED_SCOPE`.

### RG-DC-08 — Every graph and conclusion needs an exact currentness frontier — concern (100%)

- **Proposal claim:** a programmatically generated graph is sufficiently objective to drive later checks.
- **Entity of Concern:** one generated graph revision and each downstream claim that relies on it.
- **Context and use:** incremental rebuilds, CI, change impact, legacy adoption, and Evaluation.
- **FPF pattern and inspected Solution:** C.30.AD requires source paths and freshness; A.10 requires recoverable provenance/currentness/reliance paths; B.03 requires reopen conditions.
- **Project evidence:** currentness must be reported as `current`, `stale`, or `unknown` from dependency frontiers rather than timestamps ([GOV-354](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-103_BSEED_LAYER_3_GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-354--generate-proof-currentness-catalog.md:16)). Projections must declare exact Atom and Journal frontiers, and native traceability belongs in Implementation Journals ([META-105](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-102_BSEED_LAYER_2_SEMANTICS/04_requirement/CAPRMEDIO-META-REQU-105--preserve-implementation-traceability-in-journals.md:16)).
- **Inference:** a generated graph is reliable only for the exact source revision, producer, configuration, resolver environment, language coverage, and exclusions under which it was built. Every Evaluation must bind that exact graph revision.
- **Consequence if unchanged:** cached or partial graphs could silently authorize incorrect change-impact, independence, or conformance conclusions.
- **Candidate correction:** require a source and producer frontier, deterministic graph identity, coverage declaration, invalidation rules, and `current|stale|unknown` status. A stale or unknown graph can support investigation but cannot satisfy an Evaluation input requiring current complete coverage.
- **Unchecked dependency and stop condition:** storage grammar and incremental invalidation algorithm are downstream design. Stop when the semantic fields and reliance rule are accepted.
- **Fingerprint/state:** `RG-DC-08|currentness|exact-producer-and-source-frontier|OPEN`.

### Strengths preserved by the corrections

- Programmatic graph generation is feasible; the prior SOTA harvest found multiple MIT-licensed producers with useful but different extraction depth.
- The same minimum contract can support forward Evaluation and legacy adoption while keeping their claim routes distinct.
- The current `IMPLEMENTATION_INVENTORY` owner already satisfies DRY and avoids adding an unnecessary new Tool unit.
- Projection status preserves Operator authority, replaceable realization, and the separation of governed meaning from observed code structure.
- Explicit relation observation classes make partial static analysis useful without pretending it is complete runtime truth.

## Open questions (confidence <95%)

### RG-DC-09 — External entity identity and granularity — FPF not decisive (92%)

- **Proposal claim:** imported libraries and external APIs can be represented as external nodes.
- **Entity of Concern:** the stable identity of one external dependency or service interaction.
- **Context and use:** cross-boundary dependency checks, supply-chain inspection, runtime operations, and legacy adoption.
- **FPF pattern and inspected Solution:** C.30.AD and C.34 require exact entities, direction, preserved/lost structure, and bounded use, but they do not choose CAPRMEDIO’s code-ecosystem identity scheme.
- **Project evidence:** current authority requires typed, exact-frontier Projections but does not establish whether a package, imported module, symbol, service, API operation, deployment endpoint, or observed runtime target is the canonical external unit.
- **Inference:** one generic `external` node class is too coarse, while one universal cross-language identity scheme is not justified by the inspected evidence.
- **Consequence if guessed:** distinct package versions or service endpoints could collapse; source imports and runtime calls could be conflated; graphs from different producers would not compare reliably.
- **Candidate correction:** keep separate typed identities for at least package distribution, imported module/symbol, external service, API operation, deployment endpoint, and observed runtime target; let adapters populate only the types they can substantiate. Approve canonical keys only after representative language and protocol cases are tested.
- **Missing evidence and stop condition:** supported languages, package ecosystems, API protocols, repository layouts, and runtime observability requirements. Stop when the Operator selects the initial supported frontier and comparison fixtures demonstrate collision-free identity and stable cross-run matching.
- **Fingerprint/state:** `RG-DC-09|external-identity|typed-granularity-undecided|OPEN`.

### Insufficient basis and deliberately unchecked claims

- No claim is made that any candidate extracts every dynamic dependency, supports every language, or meets CAPRMEDIO performance needs.
- No claim is made that absence of a static edge proves independence.
- No claim is made that a Realization Graph alone can prove behavioral correctness, release readiness, security, or runtime conformance.
- No exact native schema, serialization format, relation registry, lifecycle, or filename is selected.
- FPF C.35, Structural Synthesis and Discovery Adequacy, was not opened because the direct-pattern budget was exhausted. It is the next relevant page if the Operator asks for a stronger acceptance procedure for generated legacy structure and inferred candidates.
- Generated/vendor/test/configuration boundaries, monorepo handling, polyglot identity, precision/recall measurement, and incremental update behavior need representative fixtures.

### Return to Project authority

The Operator should decide these three points before the repository comparison:

1. Accept or reject `Realization Graph` as a Projection output of the existing `IMPLEMENTATION_INVENTORY` Tool.
2. Keep code declarations as Projection-internal observed entities, or explicitly authorize a Bootstrap Seed change that admits a new governed node kind.
3. Accept the minimum producer envelope and the separation among normative Scope Units, static realization structure, runtime observations, and Evaluation conclusions.

If accepted, the next call should compare `code-graph-rag`, `AppThreat/atom`, and a CAPRMEDIO-native producer against the same contract for both workflows. A repeat design challenge is justified only if one of these semantic decisions changes.

## Skills used

### Invocation

`$fpf design challenge`

The previously referenced standalone `fpf-design-challenge.skill` package was absent. The current toolkit router resolved the request to the bundled design-challenge prompt in `fpf.skill`; that documented fallback was used without changing the requested analysis.

### FPF sources opened

Used:

- `C.30.AD — Architecture Description Adequacy`: selected structure, exact Entity of Concern, source paths, freshness, loss, and admissible use.
- `A.10 — Evidence Graph Referring`: evidence/provenance paths do not establish the facts or authority they cite.
- `A.6.3 — Episteme viewing`: Entity-of-Concern preservation, no unsupported strengthening, explicit omissions, and source return.
- `B.03 — Trust and Assurance Calculus`: exact target claim/use, bounded evidence, disposition, limitations, and reopen conditions.
- `C.34 — Structural Correspondence, Equivalence, and Morphism Adequacy`: weakest adequate mapping, preserved/lost structure, directionality, and the code-dependency-graph boundary.
- `fpf.skill/SKILL.md`, `prompts/design-challenge.md`, `references/output-style-general.md`, `references/review-campaign.md`, and `references/report-persistence.md`: routing, required report structure, convergence controls, and persistence protocol.

Screened only:

- `A.05 — Open-Ended Kernel & Extension Layering`: consistent with a small producer-neutral core and replaceable extensions, but it is an informative transitional stub and was not used to establish a finding.

No other FPF pattern was opened or used.
