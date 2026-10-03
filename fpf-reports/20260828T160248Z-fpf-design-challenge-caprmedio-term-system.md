## Task, scope, and boundaries

:codex-annotation{index="1"} The copy-ready `$fpf design challenge` task was executed as written.

- **Task:** falsify the proposed CAPRMEDIO Term system before it becomes Core Meta-Model authority.
- **Receiving use:** an Operator decision on which parts may become general Core Meta-Model rules and which parts require repair or Project-local configuration.
- **Target state:** every in-scope design claim has either survived an explicit counterexample attempt, received a concrete counterexample, or been returned as an unresolved authority decision.
- **In scope:** `Entity`, `Base Entity`, `Dependent Entity`, `Artifact`, `Scope Unit`, `Property`, `Property Value`, `Role`, `Subject Path`, `SUBTYPE_OF`, `IS_BORNE_BY`/`BEARS`, `Atom`, `Claim`, `Content Role`, `Status`, `Task`, `Epic`, `Job`, `Demand`, `Subject`, `Methodology Source`, `Applicable Methodology`, `Artifact Revision`, and `Carrier`.
- **Excluded:** selecting or approving repairs; editing Atoms; normalizing all active carriers; implementing validators or projections.
- **Proposal under challenge:** `SUBTYPE_OF` expresses taxonomy; `IS_BORNE_BY` expresses ontological dependence; each slash in a Subject Path expresses one bearer edge; every Dependent Entity occurrence has exactly one immediate bearer; concrete paths omit the abstract `Property` segment.
- **Primary project evidence:** active carriers under [001_CORE_META_MODEL](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL>), inspected without mutation.
- **Resolved FPF source:** `$fpf design challenge`, routed through E.11.PUA to A.6.M, B.1.1, and C.34 at source revision `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`.
- **Evidence discipline:** project files establish the current candidate model; FPF establishes challenge patterns; all design conclusions below are reviewer inferences unless a source states them directly.
- **Authority:** Anatoly Maslennikov remains the decision owner. No candidate correction below is selected or approved.
- **Dependencies:** exact status axes, complete Entity subtype registry, role-assignment identity, projection identity, and multiple-inheritance policy remain unsettled.
- **Stop condition:** met. Every stated proposal claim was tested; surviving claims, counterexamples, and unresolved choices are separated below.
- **Saved report:** `fpf-reports/20260828T160248Z-fpf-design-challenge-caprmedio-term-system.md`.

## High-confidence results (>=95%)

### Proposal, resolved FPF source, and decision boundary

The proposal contains a sound core distinction: taxonomic inheritance is not bearer dependence. The defect is its attempted scope. B.1.1 requires ontology-side relation kinds to be selected and grounded before graph checks; a generic edge must not substitute for relations with different meanings. C.34 further requires a representation to state what structure it preserves and loses. Therefore, `SUBTYPE_OF` and `IS_BORNE_BY` can govern the **Term Entity Graph and Subject Path grammar**, but they cannot by themselves govern every CAPRMEDIO relation.

The review does not decide whether to adopt, revise, or reject the proposal. It identifies the smallest repair surfaces and returns all selections to the Operator.

### FPF Challenge Findings

#### 1. Two primitive relations are insufficient for the complete governing graph — concern (99%)

- **Proposal claim / Entity of Concern:** all relevant structure can be expressed by `SUBTYPE_OF` and `IS_BORNE_BY`/`BEARS`.
- **Context/use:** the claim is adequate only for a taxonomy plus bearer-qualified Subject Paths.
- **FPF pattern:** [B.1.1 §4.1–4.4](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/00_01_Holon Aggregation and Part-Whole Construction/01_B.01.01 - Dependency Structure and Relation Grounding.md:96>) requires exact participants, grounded relation meaning, declared scope, and separation of ontology from graph representation.
- **Project evidence:** a Claim–Subject Relation is explicitly directional in [CA-R-1198](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1198-MMODEL-CORE-REQUIREMENT--define-claim-subject-relation.md:19>); Applicable Methodology is derived from selected source revisions in [CA-R-1213](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1213-MMODEL-CORE-REQUIREMENT--define-applicable-methodology-as-a-compiled-projection.md:19>); Current Scope and Claim Scope are scope references in [CA-R-920](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-920-MMODEL-CORE-REQUIREMENT--define-current-scope.md:20>) and [CA-R-921](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-921-MMODEL-CORE-REQUIREMENT--define-claim-scope.md:24>). None is subtype or ontological bearer dependence.
- **Reviewer inference:** forcing derivation, reference, ancestry, membership, or claim-subject direction into either primitive changes its semantics.
- **Consequence:** the full graph would contain category errors while appearing structurally valid.
- **Candidate correction:** define the two relations as primitive only within the Term Entity Graph. Govern other graph relations separately, including reference, derivation, scope topology, source selection, and Claim–Subject relations.
- **Unchecked dependencies / return condition:** the exact additional relation registry is not selected here; return after each relation has exact participants, direction, scope, and identity effects.

#### 2. Current Subject Paths mix taxonomy, bearer dependence, and membership — concern (99%)

- **Proposal claim / Entity of Concern:** every `/` means one `IS_BORNE_BY` edge.
- **Context/use:** the rule is coherent, but current active paths do not comply with it.
- **FPF pattern:** [B.1.1 §4.2–4.3](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/00_01_Holon Aggregation and Part-Whole Construction/01_B.01.01 - Dependency Structure and Relation Grounding.md:135>) rejects semantic drift hidden by a generic graph edge.
- **Project evidence:** `Entity/Base Entity` and `Entity/Dependent Entity` are used as paths in [CA-R-1191](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1191-MMODEL-CORE-REQUIREMENT--define-base-entity.md:8>) and [CA-R-1192](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1192-MMODEL-CORE-REQUIREMENT--define-dependent-entity.md:8>), even though the proposal treats these as subtypes. `Applicable Methodology/Sources/Core Meta-Model/Job` in [CA-R-1174](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1174-APPLICABLE_MTHD_SOURCES-DEFINES_JOB_FOR-CORE_META_MODEL--provide-the-minimal-self-applicable-canonical-methodology-model.md:8>) mixes compilation membership, source layering, and a Job-bearing relation.
- **Reviewer inference:** these paths cannot retain their present meanings under the slash-only bearer rule.
- **Consequence:** adopting the new slash rule without migration immediately makes active Subject metadata internally false.
- **Candidate correction:** express taxonomy only with `SUBTYPE_OF`; express collections and source membership with their own relation; reserve `/` exclusively for successive bearer-dependent occurrences.
- **Unchecked dependencies / return condition:** return after a complete active-path inventory assigns one relation meaning to every existing slash.

#### 3. Bearer cardinality belongs to an occurrence, not to a reusable Term — concern (99%)

- **Proposal claim / Entity of Concern:** every Dependent Entity has exactly one immediate bearer.
- **Context/use:** the claim survives only when “Entity” means one occurrence at one path position, not the globally reusable Term.
- **FPF pattern:** [C.34 §4](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/C_Kernel Extension Specifications/22_34_Structural Correspondence, Equivalence, and Morphism Adequacy/00_C.34 - Structural Correspondence, Equivalence, and Morphism Adequacy.md:123>) requires the mapping between source structure and representation to name preserved and lost distinctions.
- **Project evidence:** `Temporal Form` occurs at different positions in `Subject/Temporal Form` in [CA-R-1195](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1195-MMODEL-CORE-REQUIREMENT--define-subject-temporal-form.md:8>) and `Atom/Content Role/Temporal Form` in [CA-R-1208](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1208-MMODEL-CORE-REQUIREMENT--classify-capo-content-roles-as-occurrent.md:8>). `Job` occurs in `Task/Job` and at depth four under Applicable Methodology sources. The global same-ordinal rule in [CA-R-1205](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1205-MMODEL-CORE-REQUIREMENT--keep-each-dependent-entity-term-at-one-subject-path-position.md:20>) therefore already has counterexamples.
- **Reviewer inference:** Term identity, path occurrence, and bearer-qualified identity are currently conflated.
- **Consequence:** valid reuse produces false uniqueness violations, while renaming Terms to satisfy ordinal position creates vocabulary duplication.
- **Candidate correction:** apply the exactly-one-bearer rule to a `Subject Occurrence` or equivalent path position; identify it by its canonical full path or by `(Term, immediate bearer)`. Retire the global ordinal invariant.
- **Unchecked dependencies / return condition:** the name and carrier of the occurrence construct remain an Operator choice.

#### 4. `Property`, `Property Value`, and `Role` are not demonstrated to be disjoint subtypes — concern (97%)

- **Proposal claim / Entity of Concern:** these form three clean Dependent Entity subtypes.
- **Context/use:** a Status may be a Property Value, a classification, and a state; Subject and Methodology Source are proposed Roles but also carry references; a Role can itself have properties.
- **FPF pattern:** [A.6.M §4.1–4.4](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/15_A.06.M - Module Relation Repair.md:115>) is module-specific but supplies a valid repair discipline here: labels do not mint kinds; recover participants, relation meaning, and admissible use before declaring a root kind.
- **Project evidence:** Property is defined only as a characteristic-bearing Dependent Entity in [CA-R-1193](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1193-MMODEL-CORE-REQUIREMENT--define-property.md:18>). No inspected active authority proves exclusion among Property, Value, and Role.
- **Reviewer inference:** the proposal mixes ontological dependence with semantic function. These are separate classification axes unless exclusion is demonstrated.
- **Consequence:** multiple inheritance becomes accidental, and validators cannot know whether overlap is legal.
- **Candidate correction:** keep `Dependent Entity` as the dependence class; model Property, Value, Role, State, and Classification as explicitly governed semantic functions, with declared overlap or disjointness.
- **Unchecked dependencies / return condition:** return after representative Terms are classified against both axes and every overlap has a rule.

#### 5. `Subject` and `Methodology Source` require role occurrences plus references — concern (99%)

- **Proposal claim / Entity of Concern:** Subject can move beneath `Atom/Claim`, and Methodology Source can move to `Artifact/Revision/Methodology Source`.
- **Context/use:** each label currently denotes the thing selected, while the proposed path makes it a dependent role borne by another Entity.
- **FPF pattern:** B.1.1 requires exact participants and relation meaning; C.34 requires the representation not to erase the source identity being referenced.
- **Project evidence:** [CA-R-1198](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1198-MMODEL-CORE-REQUIREMENT--define-claim-subject-relation.md:19>) relates a Claim to a Subject, implying distinct endpoints. [CA-R-1219](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1219-MMODEL-CORE-REQUIREMENT--define-methodology-source.md:18>) defines Methodology Source as an authoritative Artifact Revision used as input, not as the Revision’s dependent characteristic.
- **Reviewer inference:** `Atom/Claim/Subject` can denote a Subject Role or Subject Reference occurrence, but not the independently identified Entity that is the claim’s subject. Likewise, a source-role occurrence can refer to an Artifact Revision without turning that Revision into a dependent child.
- **Consequence:** moving the existing Terms unchanged would collapse role identity and referent identity.
- **Candidate correction:** define claim-local and compilation-local role occurrences borne by their respective contexts, then connect each occurrence to an independently identified Entity with a separate reference/selection relation.
- **Unchecked dependencies / return condition:** the exact role bearer is unresolved and is returned below.

#### 6. `Carrier` is not a Dependent Entity of Artifact — concern (99%)

- **Proposal claim / Entity of Concern:** all Artifact characteristics can appear as bearer-dependent paths such as `Artifact/Carrier` and `Artifact/Revision`.
- **Context/use:** an Artifact Revision can depend on Artifact identity; a file, directory, or native object has its own identity and can outlive or carry more than one governed object.
- **FPF pattern:** B.1.1 distinguishes ontology-side dependence from graph representation and rejects inferring dependence from an edge’s visual placement.
- **Project evidence:** [CA-R-1216](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1216-MMODEL-CORE-REQUIREMENT--define-artifact-carrier.md:19>) defines Carrier as a file, directory, or native object that stores or attaches an Artifact Revision without changing Artifact identity.
- **Reviewer inference:** the storage relation does not make Carrier identity ontologically dependent on the Artifact. `Artifact/Carrier` therefore cannot be a bearer path under the proposed rule. `Artifact/Revision` remains plausible because Revision identity is explicitly Artifact-relative.
- **Consequence:** classifying Carrier as a dependent Property creates wrong identity and lifecycle inheritance.
- **Candidate correction:** classify Carrier as a Base Entity and govern a separate directional `CARRIES`/`IS_CARRIED_BY` relation between Carrier and Artifact Revision.
- **Unchecked dependencies / return condition:** exact carrier cardinalities and whether a Carrier may carry multiple revisions remain unsettled.

#### 7. Task, Epic, Job, Demand, and Content Role need type/value relations, not new root entities — concern (98%)

- **Proposal claim / Entity of Concern:** `Atom/Content Role/Plan/Atom Type/Task` and parallel paths can normalize planning and requirement Types.
- **Context/use:** this is coherent only if a Property Value may bear another Property and if the path expresses dependent classification, not subtype inheritance.
- **FPF pattern:** A.6.M’s relation-repair discipline requires the exact relation and admissible use rather than allowing a convenient label to create a kind.
- **Project evidence:** [CA-R-989](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-989-MMODEL-CORE-REQUIREMENT--define-task-atom.md:22>) defines Task as a Plan Atom but duplicates its intended result as Task Job. [CA-R-1211](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1211-MMODEL-CORE-REQUIREMENT--define-task-job.md:19>) confirms that Task Job is merely the result already stated by the Claim. [CA-R-988](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-988-MMODEL-CORE-REQUIREMENT--define-epic-atom.md:19>) adds a Task-containment relation. [CA-R-925](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-925-MMODEL-CORE-REQUIREMENT--define-job-atom.md:24>) and [CA-R-932](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-932-MMODEL-CORE-REQUIREMENT--define-demand-atom.md:25>) define Job and Demand as Requirement Atom Types.
- **Reviewer inference:** “Plan Atom” is not a separate Term; it is an Atom classified by Content Role. Task and Epic are Plan Atom Type values. Job and Demand are Requirement Atom Type values. Epic-to-Task containment and Consumer-to-Producer Demand direction are separate relations, not bearer edges.
- **Consequence:** treating these labels as root Entities duplicates Atom identity and hides relations in names.
- **Candidate correction:** keep role-qualified type paths; remove `Task/Job`; use the Task Claim as its intended result; govern Epic membership and Demand direction as explicit relations.
- **Unchecked dependencies / return condition:** exact names for Plan containment and Demand dependency relations remain unselected.

#### 8. Scope Unit survives as a Base Entity, but scope coordinates are references — concern (99%)

- **Proposal claim / Entity of Concern:** Scope Unit is a Base Entity and its properties can be modeled through bearer paths.
- **Context/use:** Scope Unit identity does survive independently. Current Scope and Claim Scope, however, point from an Atom or Claim to a Scope Unit or Scope Expression; they do not make the target Scope Unit dependent on the Atom.
- **FPF pattern:** B.1.1 requires relation grounding before representation.
- **Project evidence:** one Atom has exactly one Claim Scope under [CA-R-919](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-919-MMODEL-CORE-REQUIREMENT--give-every-atom-one-claim-scope.md:23>), while Claim Scope is a Scope Expression to which the Claim applies in CA-R-921. Demand direction points from Consumer Current Scope to Producer Claim Scope in CA-R-932.
- **Reviewer inference:** the coordinate value or reference occurrence may be bearer-dependent; the referenced Scope Unit is not. Parent/child ancestry is also neither subtype nor bearer dependence.
- **Consequence:** an unqualified bearer path would collapse the reference object with its target and would make relational Atoms impossible to model correctly.
- **Candidate correction:** keep Scope Unit as a Base Entity; define reference-valued Current Scope and Claim Scope properties plus explicit target relations; keep scope ancestry and Demand dependency separate.
- **Unchecked dependencies / return condition:** the identity of composite Scope Expressions remains outside the inspected evidence.

#### 9. Applicable Methodology can be a Projection, but its projected contents need distinct identities — concern (98%)

- **Proposal claim / Entity of Concern:** Applicable Methodology is a Projection subtype compiled as RMEDO Atoms with source paths.
- **Context/use:** the non-authoritative classification survives. Ambiguity remains between one Projection Artifact, its folder Carrier, and the projected Atom-like files it contains.
- **FPF pattern:** [C.34 §4 and Consequences](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/C_Kernel Extension Specifications/22_34_Structural Correspondence, Equivalence, and Morphism Adequacy/00_C.34 - Structural Correspondence, Equivalence, and Morphism Adequacy.md:123>) requires a directional, scoped mapping that states preserved and lost structure; similar graph shape does not prove semantic equivalence.
- **Project evidence:** CA-R-1213 correctly requires a derived non-authoritative Projection from exact current source revisions. [CAPRMEDIO-META-REQU-657](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-657--define-projection-artifact-form.md:19>) says source Atoms and Journals retain authority.
- **Reviewer inference:** projected Atom-shaped carriers must not silently acquire independent Atom authority or lifecycle merely because they preserve RMEDO content.
- **Consequence:** without distinct projection-element identity, consumers cannot tell source authority from compiled view.
- **Candidate correction:** identify one Applicable Methodology Projection Artifact and Revision, one folder Carrier, and dependent projected elements that reference exact source carriers/revisions and state preserved/lost fields.
- **Unchecked dependencies / return condition:** whether projected elements are dependent Entities, Projection sub-artifacts, or carrier entries is unresolved below.

#### 10. One undifferentiated `Status` cannot represent the observed lifecycles — concern (98%)

- **Proposal claim / Entity of Concern:** Atom has one Status, with values such as Draft, Active, and Archived.
- **Context/use:** current authority distinguishes pre-acceptance draft placement, accepted-current placement, completed/solved evidence placement, and historical archive placement.
- **FPF pattern:** A.6.M warns against one label carrying several kinds or authority consequences.
- **Project evidence:** [CA-M-132](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-132-GOVERN-CORE-METHOD--govern-the-archive-based-atom-lifecycle.md:21>) separately governs draft, accepted-current, solved/done, and archive places while preserving Atom ID across some moves. Atom identity and indivisible lifecycle are defined in [CA-R-655](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-655-MMODEL-CORE-REQUIREMENT--define-atom-artifact-form.md:22>).
- **Reviewer inference:** lifecycle status, admission state, workflow outcome, and carrier placement are different axes even when their labels coincide.
- **Consequence:** one Status property either permits contradictory simultaneous values or discards necessary distinctions.
- **Candidate correction:** define separately named status/state axes, each with its own cardinality and applicability by Content Role; let Delivery govern their carrier materialization.
- **Unchecked dependencies / return condition:** exact axes and value sets require an Operator decision.

#### 11. Core-model and Project-configuration defects are currently mixed — concern (99%)

- **Proposal claim / Entity of Concern:** the active Core Meta-Model is a valid source of general counterexamples.
- **Context/use:** some defects belong to CAPRMEDIO’s current Local Configuration rather than the reusable model.
- **Direct basis:** this classification follows the project’s own Core-versus-Local boundary, not a new FPF rule.
- **Project evidence:** [CA-R-1228](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1228-MMODEL-CORE-REQUIREMENT--define-applicable-methodology-source-layers.md:18>) requires exactly three layers including Installed Extensions, while the latest authority direction is Core Meta-Model plus Local Configuration for now. [CA-R-1235](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1235-MMODEL-CORE-REQUIREMENT--govern-project-root-deliveries-from-caprmedio-project-carrier-root.md:18>) and [CA-R-1239](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1239-MMODEL-CORE-REQUIREMENT--use-runtime-only-for-ephemeral-execution-state.md:15>) encode CAPRMEDIO-specific carrier roots.
- **Reviewer inference:** extensibility concepts belong in the general model; the currently selected source count and CAPRMEDIO repository paths are Project-local configuration.
- **Consequence:** leaving both in Core makes the supposed extension mechanism recursively depend on one Project’s installation.
- **Candidate correction:** retain generic Extension, Local Configuration, compilation, and carrier relation Types in Core; move selected-source counts, concrete roots, and current activation choices to Local Configuration.
- **Unchecked dependencies / return condition:** historical Bootstrap carriers were excluded and should not be moved by this design review.

#### 12. The open Entity taxonomy must not claim exhaustiveness yet — concern (97%)

- **Proposal claim / Entity of Concern:** `Entity` divides into `Base Entity` and `Dependent Entity`; Base Entity then divides into Artifact and Scope Unit.
- **Context/use:** `Entity != Artifact` is correct, and the Base/Dependent identity distinction is useful. The proposed child list is not exhaustive.
- **FPF pattern:** A.6.M requires a label’s participant and identity boundary before it becomes a root kind.
- **Project evidence:** Carrier includes independently identifiable files, directories, and native objects; Operator and AI Agent authorship also refers to independently identified actors; neither fits Artifact, Scope Unit, or Dependent Entity without additional rules.
- **Reviewer inference:** the first split can be exhaustive if every Entity either requires or does not require a bearer, but the Base Entity subtypes must remain open or include additional kinds such as Actor and Carrier.
- **Consequence:** a closed `Base Entity = Artifact | Scope Unit` taxonomy would misclassify real model participants.
- **Candidate correction:** declare the Base/Dependent split exhaustive only after identity tests are specified; declare the Base Entity subtype registry open until all active Terms are classified.
- **Unchecked dependencies / return condition:** a full active-Term inventory is required before closure.

### Strengths

- **No concern found within inspected scope (99%):** keeping `Entity` distinct from `Artifact` is necessary and survived challenge.
- **No concern found within inspected scope (99%):** separating `SUBTYPE_OF` from bearer dependence prevents the largest category error in the current slash notation.
- **No concern found within inspected scope (98%):** exactly one immediate bearer per **Dependent Entity occurrence** gives a deterministic Subject Path when occurrence identity is explicit.
- **No concern found within inspected scope (98%):** omitting the abstract `Property` segment from concrete paths is a viable serialization shortcut if the underlying typed edge remains available to validation.
- **No concern found within inspected scope (99%):** Artifact Revision and Carrier must not change Artifact identity; the current Carrier definition already preserves this boundary.
- **No concern found within inspected scope (99%):** Applicable Methodology as a non-authoritative Projection is consistent with source authority, provided projected-element identity is repaired.
- **No concern found within inspected scope (99%):** removing Task Job as a second statement of the Task Claim reduces duplicate authority.

### Unchecked claims and insufficient basis

- **Insufficient basis:** no complete active-Term classification was executed, so the final Base Entity subtype set is unknown.
- **Insufficient basis:** no parser or validator was run against a migrated slash grammar; implementability and error quality remain untested.
- **Insufficient basis:** exact multiple-inheritance and disjointness rules for Dependent Entity functions are absent.
- **Insufficient basis:** exact cardinalities for Artifact Revision, Carrier, Property, source selection, and projected elements are not established by the inspected carriers.
- **Insufficient basis:** composite Scope Expression identity and reference semantics were not defined in the inspected proposal.

### Return to project authority

The proposal should return to Anatoly Maslennikov as a **bounded Term Entity Graph design**, not as a complete CAPRMEDIO relation model. The smallest coherent repair set is:

1. limit the two primitive relations to taxonomy and bearer-qualified Subject occurrences;
2. introduce explicit relation governance for reference, derivation, membership, ancestry, Claim–Subject direction, Epic containment, and Demand dependency;
3. distinguish reusable Term from path occurrence;
4. treat Carrier as an independent Base Entity related to Artifact Revision;
5. model Subject and Methodology Source as role/reference occurrences without collapsing their referents;
6. separate general Core Types from current Local Configuration;
7. defer closed taxonomy, lifecycle, and projection-element choices until the decisions below are made.

## Open questions (confidence <95%)

### Proposal, resolved FPF source, and decision boundary

FPF is decisive that the missing distinctions must be explicit, but it does not choose CAPRMEDIO’s exact vocabulary, carriers, or cardinalities. Each item below therefore remains below 95% confidence and requires project authority.

### FPF Challenge Findings

#### 1. Exact Subject role carrier — FPF not decisive (85%)

- **Unresolved choice:** should a Subject Role occurrence be borne directly by Claim, or by a Claim–Subject Relation occurrence?
- **Missing evidence:** identity and lifecycle rules for relation occurrences.
- **Smallest next action:** write two counterexamples—one Claim with two governed Subjects and one Subject used by two Claims—and select the representation with no duplicated identity.

#### 2. Exact Methodology Source role carrier — FPF not decisive (82%)

- **Unresolved choice:** should the source-role occurrence be borne by Local Configuration, an Applicable Methodology Compilation Revision, or a Source Set occurrence?
- **Missing evidence:** the canonical identity of one compilation run versus one compiled Projection Revision.
- **Smallest next action:** model replacement of one selected source revision and test which bearer changes identity.

#### 3. Applicable Methodology projected-element kind — insufficient basis (80%)

- **Unresolved choice:** dependent Projection Element, nested Projection Artifact, or carrier entry with provenance metadata.
- **Missing evidence:** required independent replacement, lifecycle, addressability, and consumer behavior of one projected Atom-shaped file.
- **Smallest next action:** state whether one projected file may be replaced, referenced, or validated independently of the Projection Revision.

#### 4. Status axes and values — insufficient basis (75%)

- **Unresolved choice:** exact separation among Lifecycle Status, Admission State, Workflow Outcome, and carrier placement, plus role-specific values.
- **Missing evidence:** a normalized transition table across CAPRMEDIO content roles.
- **Smallest next action:** inventory current transitions for C, A, P, RMED, I, and O before defining any exactly-one rule.

#### 5. Dependent-function overlap policy — FPF not decisive (80%)

- **Unresolved choice:** multiple inheritance among Property, Value, Role, State, and Classification versus independent classification axes.
- **Missing evidence:** representative Terms classified without contradiction.
- **Smallest next action:** classify Content Role, Requirement, Status, Draft, Subject Role, Claim Scope, and Methodology Source Role in a small decision table.

#### 6. Minimum Property cardinality — insufficient basis (78%)

- **Unresolved choice:** whether every Artifact and Scope Unit must bear at least one Property, and which inherited Property satisfies the rule.
- **Missing evidence:** identity requirements for draft Artifacts, native objects, Journals, Projections, and empty Scope Units.
- **Smallest next action:** test the weakest valid instance of each Base Entity subtype and derive the minimum invariant from those cases.

### Strengths

These open choices do not undermine the surviving core distinction between subtype and bearer dependence. They prevent premature closure of the taxonomy and serialization grammar.

### Unchecked claims and insufficient basis

No authority was found that permits the reviewer to select the six choices above. No implementation evidence can substitute for those model decisions.

### Return to project authority

Anatoly Maslennikov should decide these questions before any bulk Subject normalization. The first decision should be the identity of a path occurrence, because it controls bearer cardinality, Subject roles, source roles, canonical paths, and validator behavior downstream.

## Skills used

- `$fpf design challenge`

#### FPF sources consulted (4 read; 3 used)

- **Screened only:** [E.11.PUA — Pattern Use in a Working Situation and First Useful Result](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/10_11_First-Practical Entry and Pattern-Use Discoverability Discipline/01_E.11.PUA - Pattern Use in a Working Situation and First Useful Result.md:57>) — routing entrypoint and stop discipline; not used as a substantive design basis.
- **Used:** [A.6.M — Module Relation Repair](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/15_A.06.M - Module Relation Repair.md:38>) — relation-label repair discipline, applied only by analogy outside its module-specific scope.
- **Used:** [B.1.1 — Dependency Structure and Relation Grounding](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/00_01_Holon Aggregation and Part-Whole Construction/01_B.01.01 - Dependency Structure and Relation Grounding.md:71>) — direct basis for separating ontological dependence, relation kinds, and graph representation.
- **Used:** [C.34 — Structural Correspondence, Equivalence, and Morphism Adequacy](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/C_Kernel Extension Specifications/22_34_Structural Correspondence, Equivalence, and Morphism Adequacy/00_C.34 - Structural Correspondence, Equivalence, and Morphism Adequacy.md:52>) — direct basis for projection mapping, preserved/lost structure, and representation limits.

<oai-mem-citation>
<citation_entries>
MEMORY.md:263-287|note=[term taxonomy and bearer continuity used as context then verified live]
</citation_entries>
<rollout_ids>
</rollout_ids>
</oai-mem-citation>
