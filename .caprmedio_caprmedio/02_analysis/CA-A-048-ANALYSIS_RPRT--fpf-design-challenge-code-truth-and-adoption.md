---
atom_id: CA-A-048
subject_scopes:
  - artifact-model
  - development-flow
  - scope-topology
version: 1
updated_at: 2026-08-21 01:52:33
---

## Task, scope, and boundaries

### Proposal, resolved FPF source, and decision boundary

- **Task and receiving use:** challenge the proposed treatment of actual code as a bounded source of truth, add a pre-runtime Evaluation loop, support brownfield adoption modes that create CRMED drafts, and derive as-is code-structure views before this becomes accepted CAPRMEDIO authority.
- **Target and current state:** CAPRMEDIO already defines `I` as “the actual code,” distinguishes Atom, Journal, and Projection as independent artifact forms, and includes realized project nodes in the operating graph. One active Plan still incorrectly lists actual code as an example of an `llm-generated` Projection. Repository evidence was inspected at local HEAD `3730084af7f1a890415a22837cc6adee053e685d`; the working tree contains an in-progress large structural migration, so this review changes no authority carrier or migration artifact.
- **Proposal claim:** code is authoritative for what is currently encoded; code generation is not necessarily deterministic; Evaluation can check code before product execution; CAPRMEDIO must support full, continuing, and partial brownfield adoption; adoption creates only CRMED drafts; and source-tree structure can seed initial project structure through as-is projections.
- **Affected entity:** the CAPRMEDIO operating model and its relations among CRMED draft candidates, accepted RMED authority, native Implementation, Ops evidence, Projections, and project Structural units.
- **Bounded context:** local, Git-backed software projects. This review covers classification, authority boundaries, adoption lifecycle, code-structure projection, and pre-runtime checking. It excludes implementation, command syntax, schemas, atom admission, migration changes, and non-software adoption.
- **Inputs and project evidence:** `README.md:15-20,40-70`; `.caprmedio/03_plan/CAPRMEDIO-PLAN-006--establish-projection-generation-subtypes.md:8-16`; `.caprmedio/02_analysis/CAPRMEDIO-ANRP-002--the-operating-graph-includes-realized-project-nodes.md:13-15`; `.caprmedio/100_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-512--keep-caprmedio-references-outside-native-implementation.md:12-14`; `.caprmedio/100_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-630--govern-current-non-authoritative-projections.md:14-16`; `.caprmedio/_01_BSEED_LAYER_1_METAMODEL/04_requirement/CAPRMEDIO-META-REQU-171--separate-structural-levels-from-scope-labels.md:16-18`; `.caprmedio/_01_BSEED_LAYER_1_METAMODEL/04_requirement/CAPRMEDIO-META-REQU-714--coordinate-structural-units-through-independent-axes.md:13-15`; `.caprmedio/04_requirement/CAPRMEDIO-REQU-706--define-caprmedio-structural-topology.md:16-18`; `.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-381--register-feature-realization-relation-kind.md:14-16`; `.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-363--place-concerns-by-lifecycle.md:13-15`; and `.caprmedio/03_plan/CAPRMEDIO-PLAN-012--development-backlog.md:14-22`.
- **Resolved FPF edition:** split `FPF-Knowledge-Graph` generated from FPF source revision `9a9a42e4d154021ca3f7415e0009a4214832f65f`, generated 2026-08-02, in toolkit checkout `48c84d84f1074d9d4c73338bcf604fc909249000`.
- **Authority:** FPF supplies challenge lenses only. Anatoly is the project decision owner. This report neither adopts nor rejects the proposal and creates no CAPRMEDIO authority.
- **Dependencies and stop condition:** return to project authority when the authority partition, CRMED draft lifecycle, adoption coverage semantics, structure-inference profile, or meaning of “module” changes. Implementation requires a separate accepted project decision after the current repository migration reaches a stable frontier.
- **Saved report:** `fpf-reports/20260820T011055Z-fpf-design-challenge-code-truth-and-adoption.md`

## High-confidence results (>=95%)

### FPF Challenge Findings

#### Finding 1 — no concern found within inspected scope: code may be authoritative, but only for current encoded Implementation

- **Proposal claim and affected entity:** “The actual code is also a source of truth” concerns native Implementation and its relation to RMED and Ops.
- **Bounded context and receiving use:** determining what a software checkout currently contains and using that fact during brownfield adoption or continued development.
- **Direct basis:** `E.10.D2:1-4.1.4` separates an entity, descriptions of it, specification use, carriers, work, and evidence; `C.2.1:1-4` and `C.2.1:13` keep claim-bearing knowledge, carriers, grounding, and truth/currentness distinct; `A.10:1-4.6` requires bounded evidence paths for relied-on claims.
- **Project evidence:** `README.md:15-20,65-70` already gives RMED, I, and O different content roles. `CAPRMEDIO-ANRP-002:13-15` states that Implementation, Delivery, and Ops representing realized state belong in the operating graph.
- **Reviewer inference:** the proposal is coherent if “source of truth” is replaced by a bounded authority statement: **RMED owns what is accepted or required; I owns what is currently encoded; O owns what was observed when it ran or was used.** Current code does not by itself prove intended behavior, successful execution, deployment state, or operational outcome.
- **Consequence if unresolved:** an unqualified “code is truth” rule would let implementation drift silently redefine requirements and would let code presence stand in for runtime evidence.
- **Candidate correction:** define three non-competing authority surfaces—`RMED = accepted intent`, `I = current encoded realization`, `O = observed outcome`—and require explicit lineage or comparison when a use crosses them.
- **Unchecked dependency and return condition:** exact relation names among RMED claims, native targets, and O evidence remain unselected. Return when that relation model is designed.
- **Confidence:** 99%, based on current project role definitions and direct distinction/evidence patterns.

#### Finding 2 — concern: generation mechanism must not classify the generated artifact

- **Proposal claim and affected entity:** code generation may be nondeterministic; the affected classification is Implementation versus Projection.
- **Bounded context and receiving use:** classifying LLM-generated code, LLM-generated diagrams, and deterministic derived views.
- **Direct basis:** `A.15:1-4.2` separates reusable method, method description, work plan, performed work, and produced or described entities; `E.10.D2:2-4` rejects classification by carrier or publication appearance; `C.2.1:7.1-7.2` separates a generation or viewing operation from the identity and later use of its result.
- **Project evidence:** `README.md:40-50` defines artifact form independently from content role. Yet `CAPRMEDIO-PLAN-006:10-16` lists actual code as an `llm-generated` Projection.
- **Reviewer inference:** “generated by an LLM” describes the production method or work occurrence, not the artifact form. LLM-generated source code is Implementation when it is the project’s actual code. An LLM-generated architecture summary is a Projection only when it is a non-authoritative derived view. A programmatic projection from a fixed snapshot can still be deterministic even when the code was originally produced nondeterministically.
- **Consequence if unresolved:** actual code can be demoted to a non-authoritative view, while generated prose can acquire an incorrect form solely from its producer.
- **Candidate correction:** classify the result by its governed use and authority; record `programmatic` or `llm-assisted` as generation provenance, not as the primary artifact-form discriminator. Retire or revise Plan 006 item 3 when project authority permits.
- **Unchecked dependency and return condition:** the project has not yet selected whether generation provenance belongs in Journals, Projection metadata, or both. Return when that metadata contract is designed.
- **Confidence:** 100%, based on the project’s independent axes and the direct method/work/entity distinction.

#### Finding 3 — no concern found within corrected scope: full adoption creates CRMED drafts, not reconstructed authority

- **Proposal claim and affected entity:** full adoption scans pre-existing code and creates only CRMED drafts.
- **Bounded context and receiving use:** bootstrapping CAPRMEDIO over a pre-existing software repository without pretending its original knowledge history is recoverable.
- **Direct basis:** `E.10.D2:4.1.3` requires checkability and a named validation basis before admitting specification use; `C.2.1:1-4` requires exact claim content, entity, and interpretation scheme; `A.10:1-4.6` prevents carrier presence or provenance from establishing truth, performed work, or authority.
- **Project evidence:** `README.md:65-70` assigns distinct meanings to Concern, Requirement, Method, Evaluation, Delivery, Implementation, and Ops. `CAPRMEDIO-PLAN-012:18-20` already calls for repository adoption, graph-independent Atom-to-Implementation lineage, and Evaluation results.
- **Reviewer inference:** the correction is strong. Code can seed R/M/E/D drafts where behavior, method, checking, or delivery mechanics are inferable. Anything ambiguous, contradictory, missing, or not safely inferable becomes a C draft rather than invented RMED meaning. Draft status preserves the operator’s authority boundary.
- **Consequence if unresolved:** none in the corrected proposal. The residual risk is treating “full” as “all meanings recovered” rather than “every selected native target examined and covered by drafts, explicit exclusions, or unresolved concerns.”
- **Candidate correction:** define **full adoption as complete target coverage through CRMED drafts, not complete semantic certainty**. Mechanically derived inventory and structure remain Projections; the only semantic adoption outputs are drafts. Admission of any draft is a later operator-governed act.
- **Suggested modes:**
  - `full adopt` — inspect the entire selected code frontier; create or refresh R/M/E/D drafts for inferable claims and C drafts for gaps or conflicts;
  - `continue` — inspect only new or changed native targets; create or refresh CRMED drafts, and create a C draft when code conflicts with accepted authority instead of silently rewriting it;
  - `partial adopt + continue` — apply the same rule to selected paths, packages, or modules while the remainder stays explicitly outside the adoption frontier.
- **Unchecked dependency and return condition:** current GOV explicitly leaves Concern draft placement unresolved (`CAPRMEDIO-GOV-REQU-363:13-15`). Return before implementing CRMED draft materialization.
- **Confidence:** 99%, based on the user’s corrected lifecycle boundary, role semantics, and direct evidence limits.

#### Finding 4 — concern: an as-is source-tree projection is sound, but directory shape must not automatically become accepted project structure

- **Proposal claim and affected entity:** folder-with-folders → super feature group/area; folder-with-files → feature; file → module.
- **Bounded context and receiving use:** producing an initial structural orientation and seeding candidate CAPRMEDIO scopes for a brownfield codebase.
- **Direct basis:** `A.22:2-4.7` separates selected structure from diagrams, graphs, extracted views, generated representations, and architecture claims; it requires exact constituents, obtaining relations, applied constraints, a named use, and preserved/lost structure. `C.30.AD:1-4.5` keeps architecture descriptions and module/interface views distinct from architecture and selected structure.
- **Project evidence:** `CAPRMEDIO-META-REQU-171:16-18` allows labels such as group, supergroup, and sub-feature without changing structural semantics. `CAPRMEDIO-META-REQU-714:13-15` characterizes Structural units through independent axes. `CAPRMEDIO-REQU-706:16-18` currently constrains the accepted CAPRMEDIO topology. Most decisively, `CAPRMEDIO-GOV-REQU-381:14-16` maps declared Feature scopes to native realization targets **without making those targets Structural scopes**.
- **Reviewer inference:** the raw tree, file inventory, import graph, package declarations, and mechanically detected boundaries are excellent **as-is Projections** and are not Analysis. However, calling a directory a Feature or a file a Module is an interpretation profile. It is useful as a candidate default, not a universal fact: tests, migrations, generated code, vendor trees, configuration, namespace packages, monorepos, and language conventions violate the simple mapping.
- **Consequence if unresolved:** filesystem accidents become semantic authority, refactors appear to change project meaning automatically, and current project topology conflicts with native realization mapping.
- **Candidate correction:** create a `Code Structure Projection` over an exact source frontier. Keep mechanically observed fields factual. Add optional classification candidates with rule ID, confidence, exclusions, and override. Use those candidates to place CRMED drafts initially; promote a code-derived area/Feature/module mapping into accepted project structure only through a later operator decision.
- **Unchecked dependency and return condition:** the default software profile, ignored/generated/vendor rules, language adapters, and meaning of `module` remain open. Return when selecting the profile.
- **Confidence:** 99%, based on direct structure/view boundaries and explicit current project authority.

#### Finding 5 — no concern found within inspected scope: a pre-runtime `I ↔ E` micro-loop fits the model

- **Proposal claim and affected entity:** apply Evaluation to code before product execution and automated tests, including linters and related checks.
- **Bounded context and receiving use:** quick feedback while editing or generating candidate code.
- **Direct basis:** `A.15:1-4.2` distinguishes an Evaluation method or description from its performed check work and result record; `A.10:1-4.6` requires exact work, bindings, result owner, and bounded reliance when check results are used.
- **Project evidence:** `README.md:65-70` defines Evaluation as how claims are checked and Ops as evidence from running and using the system. The current Engine model already treats deterministic checking as a Tool/Checker concern.
- **Reviewer inference:** static linting, formatting checks, type checking, schema validation, compilation, dependency checks, and static security checks can evaluate candidate I before product runtime. Automated tests remain Evaluation too, although many tests execute code. The useful nested loop is `I candidate → pre-runtime E → repair I`, followed by executable tests and Delivery/run only after the applicable gate passes.
- **Consequence if unresolved:** none found in the proposal itself. The only risk is calling a configured linter or test definition proof that a check actually ran.
- **Candidate correction:** model the Evaluation claim/criterion, performed check, result, and gate use separately; do not create an Atom for every invocation unless its result must be governed or retained.
- **Unchecked dependency and return condition:** result retention and the boundary between Evaluation results and Ops evidence require a later design pass.
- **Confidence:** 98%, based on current role definitions and direct work/evidence separation.

### Strengths within inspected scope

- **Brownfield work becomes first-class.** CAPRMEDIO would no longer assume RMED existed before code.
- **CRMED drafts preserve honesty.** Inferable semantics become R/M/E/D drafts; uncertainty becomes C drafts instead of fabricated intent.
- **The proposal restores I to its stated meaning.** It corrects the residual Plan 006 classification error without weakening Projections.
- **As-is projections reduce hallucination pressure.** Agents can inspect exact tree, file, language, package, dependency, and digest facts before interpreting them.
- **Partial adoption is operationally realistic.** It permits useful governed work without pretending legacy code is already understood.
- **The pre-runtime Evaluation loop creates cheap feedback.** It strengthens I before Delivery and runtime evidence while preserving the larger `RMED → I → O` flow.

### Unchecked claims and insufficient basis

- This review does not establish a complete adoption ontology, relation vocabulary, command interface, storage schema, or draft admission workflow.
- No representative external brownfield repositories were inspected, so the proposed directory heuristics have not been tested across Python, TypeScript, Java, Go, Rust, monorepos, generated-code repositories, or mixed-language projects.
- The current checkout is in a large active migration. It is sufficient for design evidence but insufficient as a safe implementation frontier. No authority carrier should be revised from this report alone.
- Whether `continue` may leave legacy targets permanently unmodeled, or must eventually close full coverage, is a project policy decision rather than an FPF result.

### Return to project authority

The project decision owner can now decide whether to accept this corrected design direction:

1. bounded authority partition: `RMED = accepted intent`, `I = encoded realization`, `O = observed outcome`;
2. artifact form classified by governed use, with generation mechanism recorded only as provenance;
3. full adoption defined by complete target coverage through CRMED drafts and honest unknowns;
4. continue and partial-adopt modes creating or refreshing CRMED drafts against an explicit adoption frontier;
5. code structure emitted first as a source-frontier-bound as-is Projection, with Feature/area/module classifications remaining candidates until accepted;
6. a nested pre-runtime `I → E → I` repair loop before later tests, Delivery, execution, and O evidence.

FPF does not authorize this decision. Anatoly remains the owner of acceptance and of any later implementation Plan.

## Open questions (confidence <95%)

### 1. What should `module` mean across implementation languages?

- **Best current answer:** use language-native module/package detection where available; use “source file” as the universal factual unit; expose file-as-module only as a profile-specific candidate.
- **Confidence:** 92%.
- **Missing evidence:** representative adopter repositories and language-profile requirements.
- **Consequence:** a universal file=module rule will misclassify package initializers, generated files, partial classes, multi-module files, and non-code carriers.
- **Next action:** evaluate the proposed projection against a small mixed-language corpus and record exceptions before selecting a default profile.

### 2. May Concern have a draft lifecycle?

- **Best current answer:** yes for brownfield adoption, because a machine-discovered ambiguity is not yet an operator-admitted active Concern; however, this must be settled explicitly rather than inferred.
- **Confidence:** 90%.
- **Missing evidence:** project resolution of `CAPRMEDIO-META-CONC-004--do-concerns-need-a-draft-lifecycle` and a current GOV placement rule. Current `CAPRMEDIO-GOV-REQU-363:13-15` says Concern draft placement is unregistered.
- **Consequence:** CRMED draft output cannot be materialized consistently while C has no admitted draft lifecycle.
- **Next action:** decide the Concern draft lifecycle before specifying the adoption writer.

### 3. What exact carrier owns the adoption frontier and drift state?

- **Best current answer:** keep the native code untouched; store source-frontier-bound coverage and structure as Projections, append adoption/rebuild work to Journals, and keep CRMED candidates in draft Atom carriers.
- **Confidence:** 91%.
- **Missing evidence:** the final post-migration Projection registry, Journal event schema, draft lifecycle rules, and accepted Implementation-lineage relations.
- **Consequence:** a wrong carrier choice can make rebuildable state authoritative or bury draft semantics in generated output.
- **Next action:** settle the post-migration artifact/relation registry, then design the minimal adoption coverage Projection and events against it.

## Skills used

- `fpf-design-challenge` — tested the proposal’s authority, classification, structure-view, evidence, and lifecycle boundaries before project acceptance.

#### FPF sources consulted (7 read; 6 used)

- `FPF-Knowledge-Graph/00-readme/02_Practical-Use Cards.md` — **screened only**
- `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/09_10_Unified Lexical Rules for FPF/05_E.10.D2 - EntityOfConcern, Description Episteme, and Specification-Use Discipline.md` — **used**: separated implementation, description, specification use, carrier, and authority
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/22_Structure and Structural Views (STRUCT-CAL)/00_A.22 - Structure and Structural Views (STRUCT-CAL).md` — **used**: distinguished observed code structure from derived views and accepted semantic structure
- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/18_30_Grounded Architecture and Selected-Structure Adequacy/01_AD_Architecture Description Adequacy/00_C.30.AD - Architecture Description Adequacy.md` — **used**: bounded module and architecture descriptions and their admissible use
- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/00_02_Epistemic holon composition (KD-CAL)/01_C.02.01 - U.Episteme- Constitution, Empirical Grounding, and Edition Relations.md` — **used**: separated claim identity, carrier, grounding, generation, and truth
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/15_Role-Method-Work Alignment/00_A.15 - Role-Method-Work Alignment.md` — **used**: separated generation/check methods, performed work, and resulting artifacts
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/10_Evidence Graph Referring- Claim-Bound Evidence and Provenance Graph/00_A.10 - Evidence Graph Referring- Claim-Bound Evidence and Provenance Graph.md` — **used**: bounded reliance on code and check results without inflating them into runtime truth

<oai-mem-citation>
<citation_entries>
MEMORY.md:48-52|note=[current engine projection and atom continuity]
MEMORY.md:164-170|note=[authority projection and implementation boundary continuity]
</citation_entries>
<rollout_ids>
</rollout_ids>
</oai-mem-citation>
