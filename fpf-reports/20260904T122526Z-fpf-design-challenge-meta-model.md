# Task, scope, and boundaries

The validated Plan challenged one concrete design: the current active CAPRMEDIO Core Meta-Model authority carried by the 615 active Markdown Atom files under `CORE_META_MODEL`. Its single `$fpf design challenge` step passed validation at attempt 2 and produced six open issues with six proposed fixes.

The observed source frontier is:

- carrier root: `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`;
- active-source inventory digest: `1459eacae8e0076726920ef9585541be71cf0caf106b0894bd3aef443ac20151`;
- digest recipe: from the workspace root, enumerate regular `*.md` files below the carrier root, exclude every path containing `/archive/` or `/drafts/`, sort the workspace-relative paths bytewise with `LC_ALL=C`, and for each path emit the path bytes, one NUL byte, the lowercase SHA-256 hex digest of the file bytes, and one newline; concatenate those records and calculate SHA-256 over the resulting byte stream;
- repository base revision: `962a69011c6c1fa58619e1c877b7f848347cbaa9`;
- source state: tracked working-tree files were clean when the frontier was inspected.

The challenge tests internal coherence, self-application, ontological parsimony, extension boundaries, relation and classification precision, and failure modes. It excludes `LOCAL_CONFIGURATION`, generated Applicable Methodology, settings carriers, Tool consumers, project artifacts, and implementation migration. No analyzed `CORE_META_MODEL` carrier or excluded target was modified. Validated delivery of this report is separate from target mutation.

Saved report: fpf-reports/20260904T122526Z-fpf-design-challenge-meta-model.md

### Composition receipt

- Exact invocation: `[$fpf](/Users/am/.codex/skills/fpf/SKILL.md) plan design challenge for meta-model`
- Selected profile: none.
- Requested sequence: `$fpf design challenge`.
- Executed prefix: `$fpf design challenge`.
- Unexecuted suffix: none.
- Plan-to-step edge result: passed Plan `fpf-plan-a6b80bac` supplied one bounded Core-only target and the complete exclusions; the target was recoverable, so `STOP_NO_CHALLENGE_TARGET` did not apply.
- Step state: `COMPLETE`; whole Plan state: `COMPLETE`.
- Context ledger: 7 direct FPF methodology pages read; 5 used and 2 screened only.
- Produced issue IDs: `DC-001` through `DC-006`.
- Produced fix IDs: `FX-001` through `FX-006`.

### Campaign handoff

- Campaign ID: `FPF-CAMPAIGN-a6b80bac`.
- Current phase: design challenge complete and returned for Operator disposition.
- Semantic frontier: the active `CORE_META_MODEL` authority identified by the carrier root, active-file count, and reproducible digest above.
- Evaluation frame: primitive-relation completeness, Type/classification consistency, universal-rule exception consistency, status/activity totality, kernel admission, and recursive self-application.
- Predecessors: validated Plan `fpf-plan-a6b80bac` and passed step set `step-001` attempt 2.
- Finding lifecycle: all issues are `OPEN`; all repair candidates are `PROPOSED`.
- Allowed next action: the Operator may accept, reject, or refine issue and fix IDs in a separately authorized task; this completed Plan grants no repository mutation authority.

# Issues, weak points, and improvements

### Native result

#### 1. Proposal, resolved FPF source, and decision boundary

The challenged proposal is a minimal, open, recursively self-applicable Core Meta-Model. Its active Atoms define the Term System, Entity and Artifact classifications, Scope Unit structure, lifecycle properties, carrier-independent authority, and the boundary through which extensions and Local Configuration may expand the model.

The direct FPF basis supports five decisive tests:

1. a primitive relation requires recoverable participants, applicability, and an obtaining condition before graph notation can use it safely;
2. a subtype relation, a single-valued property, and an allowed property value are distinct claims;
3. a universal classification rule must state a candidate domain that is consistent with its explicit exceptions;
4. a minimal kernel admits only reusable necessities and keeps instance policy outside the kernel;
5. a self-applicable model must satisfy the same independently replaceable-claim boundary that it imposes on its members.

The decision boundary is analytical disposition, not mutation. The findings identify concrete defects and bounded candidate repairs. The Operator retains authority over which issue IDs, vocabulary choices, and repair designs become new Core authority.

#### 2. FPF Challenge Findings

The highest-impact defect is that the Term System declares three primitive relations without defining their relation semantics. The next defects make the Type architecture ambiguous or unsatisfiable in ordinary use and directly contradict Project classification. Artifact Activity is then required for a wider domain than the declared Status models cover. Finally, instance policies inflate the claimed minimal Core and one such policy Atom violates the Core's own one-Atom/one-Claim boundary.

#### 3. Strengths within inspected scope

- The model explicitly keeps its Entity taxonomy open and makes Core permission, extensions, and Local Configuration visible rather than treating the current taxonomy as exhaustive.
- The model distinguishes Term-System relations from claim-subject relations and declares graph-specific validation rather than assuming that one relation vocabulary applies everywhere.
- Artifact Activity is modeled as derived rather than as a second independent lifecycle axis; this is a good normalization direction once Status-domain coverage is closed.
- Structural Entity, Scope Unit, and Atom Collection are separated, allowing containment and Scope ownership to remain different concepts.
- The Core already states a strong self-application target through `CA-R-1174`, `CA-R-918`, `CA-R-154`, and `CA-E-384`; the challenge exposes repairable counterexamples rather than absence of intent.

#### 4. Unchecked claims and insufficient basis

This challenge did not run excluded Tool validators, inspect `LOCAL_CONFIGURATION`, inspect generated Applicable Methodology, or attempt implementation migration. It does not claim that the six findings are exhaustive across all 615 active Atoms. The direct textual contradictions and missing relation declarations do not depend on Tool behavior, but before/after improvement claims would require a separately authorized, rerunnable evaluation frame.

#### 5. Return to project authority

The Operator should review issue IDs individually. The recommended review order is `DC-001`, `DC-002`, `DC-003`, `DC-004`, `DC-005`, then `DC-006`. The first four close semantic preconditions for deterministic graph and lifecycle validation; the last two repair the Core boundary and self-application after those foundations are stable.

### Issue registry

#### DC-001 - Primitive Term-System relations lack direct relation definitions

- FPF result state: `concern`.
- Proposal claim and affected Entity of Concern: the Term System provides a precise graph language; the Entity of Concern is each primitive Relation Kind `SUBTYPE_OF`, `IS_BORNE_BY`, and `IS_ALLOWED_VALUE_OF`.
- Bounded context and receiving use: active `CORE_META_MODEL` Term graph construction, Subject Expression construction, and Term-System evaluation.
- Direct FPF pattern record: `A.6.5 - Relation-Declaration Slot Discipline`, edition `source_revision 563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, stable locator `A.6.5:1 and A.6.5:4 Solution`, inspected Solution: recover the direct relation and its participant meanings first; define its predicate, applicability, participant ValueKinds, and identity rule before a reusable declaration or notation uses it, because declaration notation cannot recover a missing ontology.
- Direct FPF basis: relation names and graph cardinalities do not define what ordered participants a relation admits or what makes the relation obtain. `C.3.1:4-5` independently shows the necessary distinction for a subtype relation: exact narrower and broader participants, applicability, and a criterion-entailment or closed-domain obtaining branch.
- Issue: `CA-R-1242` registers exactly three primitive Relation Kinds and `CA-R-1335` makes them the Term-System graph, but the active Core defines only graph/cardinality constraints for them. It does not give the three relations direct signatures, participant meanings, applicability, or obtaining conditions. In particular, `CA-R-1244` and `CA-R-1345` constrain `SUBTYPE_OF` parent count and acyclicity without defining when one Term is legitimately a subtype of another.
- Evidence: `04_requirement/CA-R-1242-MMODEL-CORE-REQUIREMENT--register-term-system-primitive-relations.md:16-18`; `04_requirement/CA-R-1335-MMODEL-CORE-REQUIREMENT--define-term-system.md:19-21`; `04_requirement/CA-R-1244-MMODEL-CORE-REQUIREMENT--limit-direct-subtype-parents.md:16-18`; `04_requirement/CA-R-1345-MMODEL-CORE-REQUIREMENT--keep-the-subtype-graph-acyclic.md:16-18`; `04_requirement/CA-R-1346-MMODEL-CORE-REQUIREMENT--limit-direct-allowed-value-parents.md:16-18`; `06_evaluation/CA-E-382-MMODEL-CORE-EVALUATION--reject-invalid-term-system-graphs.md:16-18`.
- Reviewer inference: **reviewer inference** - two graph builders can satisfy every current cardinality and acyclicity rule while disagreeing about valid endpoints and truth conditions for the same edge, so the current graph is not semantically deterministic.
- Consequence: malformed subtype, bearer, or allowed-value edges can pass the declared evaluation; valid edges can be rejected by an implementation-specific interpretation that is absent from authority.
- Candidate correction or alternative: add one direct definition Atom for each primitive Relation Kind, specifying ordered participant meanings, participant domains, applicability, and obtaining condition; then make the existing cardinality and cycle rules depend on those definitions. For `SUBTYPE_OF`, require an explicit membership criterion and use criterion entailment or exhaustive evaluation over a deliberately closed finite domain.
- Affected target/context: Term System, every Subject Expression built from the Term graph, and every graph consumer relying on these primitive edges.
- Issue confidence and basis: `100%`, the primitives are registered and used while direct semantic definitions are absent from the bounded active source frontier.
- Coverage limit or uncertainty: this does not prescribe whether relation occurrences need independent identifiers; that remains receiving-use dependent.
- Unchecked dependencies and stop/return condition: Tool-side implicit interpretations were excluded and cannot substitute for source authority; return to the Operator if any primitive is intentionally syntax-only, and stop mutation unless that reduced claim is made explicit.
- Lifecycle: `OPEN`.
- Mapped fix: `FX-001`.

#### DC-002 - One single-valued Type slot is used for incompatible classification axes

- FPF result state: `concern`.
- Proposal claim and affected Entity of Concern: Type is one coherent single-valued Property; the Entity of Concern is `Entity/Type` and its qualified Artifact and Scope Unit uses.
- Bounded context and receiving use: active `CORE_META_MODEL` Entity classification and Scope Unit navigation.
- Direct FPF pattern record: `C.3.1 - U.Kind and U.SubkindOf Core`, edition `source_revision 563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, stable locator `C.3.1:4-5 Solution`, inspected Solution: recover each kind by candidate domain and membership condition, keep subtype distinct from dependency and slot filling, and distinguish kind identity from classification and representation.
- Direct FPF basis: an ontological subtype classification and a value of a single-valued property require separate predicates; independent property axes cannot share one single-valued slot unless their domains are mutually exclusive.
- Issue: `CA-R-1284` defines Type as single-valued, `CA-R-1285` limits an Entity occurrence to at most one direct Type value, and `CA-R-1349` says every qualified Type Subject for one Entity occurrence identifies the same Type Property. Yet `CA-R-1405` admits Artifact Type values such as Projection and Structural Entity, `CAPRMEDIO-META-REQU-709` requires every Scope Unit to have Ordered or Unordered as its Type value, and `CA-R-1213` classifies Applicable Methodology as both a Projection and a Structural Entity. The authority does not say which of these are Type values, which are subtype memberships, or how an occurrence can retain independent axes under one slot.
- Evidence: `04_requirement/CA-R-1284-MMODEL-CORE-REQUIREMENT--define-type.md:18-20`; `04_requirement/CA-R-1285-MMODEL-CORE-REQUIREMENT--limit-each-entity-occurrence-to-one-direct-type-value.md:17-19`; `04_requirement/CA-R-1349-MMODEL-CORE-REQUIREMENT--identify-one-type-property-slot.md:17-19`; `04_requirement/CA-R-1405-MMODEL-CORE-REQUIREMENT--register-core-artifact-type-values.md:20-22`; `04_requirement/CAPRMEDIO-META-REQU-709--register-ordered-and-unordered-scope-unit-types.md:18-20`; `04_requirement/CA-R-1213-MMODEL-CORE-REQUIREMENT--define-applicable-methodology-as-a-compiled-projection.md:19-21`.
- Reviewer inference: **reviewer inference** - either Projection/Structural Entity and Ordered/Unordered are competing values in one slot, which violates single-valuedness for valid multi-axis cases, or some are subtype claims, in which case the current `Type` wording and allowed-value registries misclassify them.
- Consequence: a conforming compiler cannot derive one unambiguous Type value for Scope Units and Applicable Methodology, and different consumers can encode the same classification through incompatible mechanisms.
- Candidate correction or alternative: reserve `Type` as a generic property family but qualify independent single-valued properties by bearer and discriminator, such as `Artifact Kind` and `Scope Unit Ordering`, or move ontological classifications entirely to `SUBTYPE_OF` while retaining Type only for mutually exclusive allowed-value axes. State explicitly which mechanism classifies Projection, Structural Entity, Scope Unit, Ordered, and Unordered.
- Affected target/context: Entity/Type, Artifact classification, Scope Unit classification, Applicable Methodology classification, and downstream status qualification.
- Issue confidence and basis: `99%`, the active claims require either multi-valued use or an unstated distinction between subtype and Type-value classification.
- Coverage limit or uncertainty: the intended choice between qualified property axes and subtype-only classification is not stated and remains an Operator design decision.
- Unchecked dependencies and stop/return condition: return to the Operator before choosing the canonical axis design; stop mutation if the replacement would silently change membership or filenames outside the Core-only scope.
- Lifecycle: `OPEN`.
- Mapped fix: `FX-002`.

#### DC-003 - Project is both required to have and prohibited from having a Scope Unit Type

- FPF result state: `concern`.
- Proposal claim and affected Entity of Concern: Scope Unit governance applies recursively while preserving the Project exception; the Entity of Concern is the Project Scope Unit's Type cardinality.
- Bounded context and receiving use: active `CORE_META_MODEL` Scope topology and fractal Scope Unit governance.
- Direct FPF pattern record: `C.3.2 - Kind Intent, Membership Judgment, and Extension`, edition `source_revision 563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, stable locator `C.3.2:4-7 Solution`, inspected Solution: state the exact candidate domain and applicability before classification, and keep declaration, admissibility, judgment, and extension distinct.
- Direct FPF basis: a universal rule over every member of a candidate kind cannot coexist with an explicit zero-cardinality rule for a named member unless the exception is removed from the universal domain or the property is distinguished.
- Issue: `CAPRMEDIO-META-REQU-709` requires every Scope Unit to have exactly one Type value in Ordered or Unordered. `CAPRMEDIO-META-REQU-710` calls the Project a Project Scope Unit and requires it to have zero Type values. `CA-R-927` also treats Project as a Project Scope Unit, while `CA-R-917` requires the same Scope Unit governance pattern recursively.
- Evidence: `04_requirement/CAPRMEDIO-META-REQU-709--register-ordered-and-unordered-scope-unit-types.md:18-20`; `04_requirement/CAPRMEDIO-META-REQU-710--keep-project-without-scope-unit-type.md:17-19`; `04_requirement/CA-R-927-MMODEL-CORE-REQUIREMENT--let-operators-define-project-goals.md:21-23`; `04_requirement/CA-R-917-MMODEL-PRINCIPLE-REQUIREMENT--apply-the-same-scope-unit-governance-recursively.md:19-21`.
- Reviewer inference: **reviewer inference** - because Project is explicitly a Scope Unit in active authority, the two cardinality requirements cannot both be true for the Project occurrence.
- Consequence: any validator must reject either the Project exception or the universal Scope Unit rule; the claimed recursive governance pattern has an unmodeled exception.
- Candidate correction or alternative: keep Project as a Scope Unit and scope the Ordered/Unordered property to non-Project Scope Units, or give Project its own explicitly allowed ordering value. Prefer the first repair if Project ordering is intentionally not meaningful.
- Affected target/context: Scope Unit/Type, Project classification, recursive Scope governance, and navigation validation.
- Issue confidence and basis: `100%`, direct contradictory cardinalities apply to the same explicitly named Project Scope Unit.
- Coverage limit or uncertainty: the challenge does not decide whether a future Project may contain ordered peer Projects; that is outside the current candidate domain.
- Unchecked dependencies and stop/return condition: return if the Operator intends Project not to be a Scope Unit, because that would require a wider fractality redesign; otherwise stop mutation until the non-Project candidate domain is stated exactly.
- Lifecycle: `OPEN`.
- Mapped fix: `FX-003`.

#### DC-004 - Mandatory Artifact Activity has no complete Status-domain basis

- FPF result state: `concern`.
- Proposal claim and affected Entity of Concern: every Artifact has exactly one derived Activity; the Entity of Concern is `Artifact/Activity` and its source `Entity/Type/Status`.
- Bounded context and receiving use: active `CORE_META_MODEL` lifecycle validation across all registered Artifact types.
- Direct FPF pattern record: `A.6.5 - Relation-Declaration Slot Discipline`, edition `source_revision 563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, stable locator `A.6.5:4-4.2 Solution`, inspected Solution: type every reused participant meaning completely, keep the direct predicate and applicability recoverable, and do not let a declaration field hide a missing domain.
- Direct FPF basis: a total derived property requires its source property and allowed-value domain to be defined throughout the derivation's declared candidate domain.
- Issue: `CA-R-1307` requires exactly one Activity for every Artifact; `CA-R-1394` derives Activity from the Artifact's current type-qualified Status; and `CA-E-386` rejects an Artifact whose current Status cardinality is not exactly one. The Core declares Status domains for Requirement, Method, Evaluation, Delivery, Task, and Epic, but no active source Atom declares a Status domain for other registered Artifact types such as Journal, Projection, Scope Unit/Structural Entity, Project Settings, or Framework Instance Settings.
- Evidence: `04_requirement/CA-R-1306-MMODEL-CORE-REQUIREMENT--define-status-as-a-type-qualified-property.md:17-19`; `04_requirement/CA-R-1307-MMODEL-CORE-REQUIREMENT--give-every-artifact-one-activity.md:16-18`; `04_requirement/CA-R-1394-MMODEL-CORE-REQUIREMENT--define-artifact-activity.md:18-20`; `04_requirement/CA-R-1395-MMODEL-CORE-REQUIREMENT--derive-active-artifact-activity.md:16-18`; `04_requirement/CA-R-1396-MMODEL-CORE-REQUIREMENT--derive-inactive-artifact-activity.md:16-18`; `06_evaluation/CA-E-386-MMODEL-CORE-EVALUATION--validate-type-qualified-status-and-artifact-activity.md:18-20`; registered Artifact types in `04_requirement/CA-R-1405-MMODEL-CORE-REQUIREMENT--register-core-artifact-type-values.md:20-22`.
- Reviewer inference: **reviewer inference** - a Journal or Projection can be a valid Artifact under the Core while lacking any authoritative allowed Status value, so its required Activity cannot be derived without an implementation-invented default.
- Consequence: the universal lifecycle evaluation is incomplete and can reject valid non-Atom Artifacts or assign them Activity using non-authoritative assumptions.
- Candidate correction or alternative: either define a complete type-qualified Status domain and current-Status rule for every admitted Artifact kind, or narrow the Activity obligation and evaluation to the explicitly status-bearing Artifact domain. Do not retain a universal `every Artifact` claim with partial domains.
- Affected target/context: Artifact lifecycle, all non-Atom Artifact kinds, and Activity-based source selection.
- Issue confidence and basis: `100%`, the universal source requirement and finite list of declared Status domains are directly observable in the active Core frontier.
- Coverage limit or uncertainty: the correct Status values for settings and Structural Entities are a policy choice not derivable from the inspected Core.
- Unchecked dependencies and stop/return condition: return to the Operator for the intended lifecycle domain; stop mutation if filling the gap would invent status values rather than recover an accepted policy.
- Lifecycle: `OPEN`.
- Mapped fix: `FX-004`.

#### DC-005 - The claimed minimal Core contains framework-instance and optional-surface policy

- FPF result state: `concern`.
- Proposal claim and affected Entity of Concern: `CORE_META_MODEL` is the minimal self-applicable canonical model necessary and sufficient for extension, configuration, validation, and compilation; the Entity of Concern is the Core admission boundary.
- Bounded context and receiving use: active `CORE_META_MODEL` reused as the base of project-specific methodology sources.
- Direct FPF pattern record: `A.5 - Open-Ended Kernel & Extension Layering`, edition `source_revision 563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, stable locator `A.5:4 Solution`, inspected Solution: keep the kernel minimal, keep domain- and instance-specific vocabulary and laws outside it by default, and keep dependency distinct from specialization.
- Direct FPF basis: a reusable kernel may define the extension point and configuration mechanism without fixing one framework instance's presentation mode or one optional projection surface's navigation policy.
- Issue: `CA-R-1174` claims a minimal Core, while active Core Atoms prescribe concrete framework-instance reporting modes and defaults, detailed silent/verbose interaction behavior, optional architecture-view layout, and tier placement for implementation methods and decisions. These are usable policies, but the active Core does not provide an admission argument showing that they are necessary for representing or extending the meta-model rather than Local Configuration choices.
- Evidence: `04_requirement/CA-R-1174-APPLICABLE_MTHD_SOURCES-DEFINES_GOAL_FOR-CORE_META_MODEL--provide-the-minimal-self-applicable-canonical-methodology-model.md:16-18`; `04_requirement/CAPRMEDIO-GOV-REQU-294--interaction-reporting-mode-setting.md:18-45`; `04_requirement/CAPRMEDIO-GOV-REQU-297--enabled-one-level-architecture-views.md:18-26`; `04_requirement/CAPRMEDIO-GOV-REQU-756--restrict-implementation-methods-to-core-tier.md:17-19`; `04_requirement/CAPRMEDIO-GOV-REQU-757--restrict-implementation-decisions-to-standard-tier.md:17-19`.
- Reviewer inference: **reviewer inference** - these policies can vary while the Entity, Term, relation, Scope, carrier, and expansion model remains unchanged; therefore their necessity to the Core is not established.
- Consequence: the Core grows with current instance behavior, making extension boundaries harder to review and forcing projects to replace Core authority when they should configure or expand it.
- Candidate correction or alternative: add a Core-admission test requiring composition failure, action-facing necessity, non-redundancy, and a sharp boundary; retain only the generic settings, projection, and tier mechanisms in Core, and classify concrete reporting, view, and tier-placement policies as Local Configuration or Extension authority.
- Affected target/context: Core admission, `LOCAL_CONFIGURATION` boundary, future extensions, and reuse across projects.
- Issue confidence and basis: `98%`, the policies are visibly instance- or surface-specific and no necessity record was found; the Operator could still declare one of them universal by adding a passing admission rationale.
- Coverage limit or uncertainty: this is not an exhaustive placement audit of all 615 Atoms, and the excluded destination layer was not inspected.
- Unchecked dependencies and stop/return condition: return if a policy is claimed as universal so its necessity can be tested explicitly; stop before relocating anything because `LOCAL_CONFIGURATION` is excluded from this challenge.
- Lifecycle: `OPEN`.
- Mapped fix: `FX-005`.

#### DC-006 - The Core violates its own independently replaceable Claim boundary

- FPF result state: `concern`.
- Proposal claim and affected Entity of Concern: every active Core Atom has one independently replaceable Claim and only content necessary for that Claim; the Entity of Concern is `CAPRMEDIO-GOV-REQU-294` as an active Atom.
- Bounded context and receiving use: active `CORE_META_MODEL` self-application and Claim-boundary evaluation.
- Direct FPF pattern record: `A.11 - Ontological Parsimony`, edition `source_revision 563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, stable locator `A.11:2 Solution and A.11:3 Conformance Checklist`, inspected Solution: require composition, non-redundancy, action-facing contribution, and a sharp inclusion/exclusion boundary; convenient packaging does not justify collapsing independently reviewable distinctions.
- Direct FPF basis: obligations with independent replacement conditions remain distinct claims even when they concern one feature or carrier.
- Issue: `CA-R-918` requires exactly one independently replaceable Claim per Atom, `CA-R-154` permits only content necessary for that Claim, and `CA-E-384` rejects an independently replaceable component inside one Claim. `CAPRMEDIO-GOV-REQU-294` combines at least the settings schema, exact allowed values, default value, silent-mode behavior, verbose-mode behavior, invariant safety reporting, non-effect on authorization and routing, and one authoritative settings source. These components can change independently.
- Evidence: `04_requirement/CA-R-918-MMODEL-CORE-REQUIREMENT--give-every-atom-one-claim.md:16-18`; `04_requirement/CA-R-154-MMODEL-CORE-REQUIREMENT--keep-each-atom-semantically-irreducible.md:18-20`; `06_evaluation/CA-E-384-GOVERN-CORE-EVALUATION--validate-composite-claims-and-derived-summaries.md:17-19`; counterexample `04_requirement/CAPRMEDIO-GOV-REQU-294--interaction-reporting-mode-setting.md:18-45`.
- Reviewer inference: **reviewer inference** - changing the default from silent to verbose does not require changing the allowed-value set, and changing reporting content does not require changing the settings carrier; therefore the Atom contains multiple independently replaceable Claims.
- Consequence: the self-describing Core is not valid input to its own Claim-boundary authority, weakening confidence in recursive application and automated normalization.
- Candidate correction or alternative: split the counterexample into separate Atoms for carrier/schema, allowed values, default, each mode's behavior, invariant reporting, and authority-source rule; then evaluate the complete active Core frontier with the existing independently replaceable-Claim test.
- Affected target/context: Core self-application, Claim normalization, revision history, and any compiled source that treats one carrier as one semantic unit.
- Issue confidence and basis: `100%`, one active counterexample refutes the universal self-application claim and the independent replacement probes are concrete.
- Coverage limit or uncertainty: this challenge does not enumerate every other multi-Claim Atom.
- Unchecked dependencies and stop/return condition: a complete Claim audit remains unrun; return when a borderline component cannot be separated at 95% confidence, and stop before splitting because mutation and migration are outside this step.
- Lifecycle: `OPEN`.
- Mapped fix: `FX-006`.

### Fix and improvement register

#### FX-001 - Define every primitive Term-System relation directly

- Exact change: add one Core Definition Atom for each of `SUBTYPE_OF`, `IS_BORNE_BY`, and `IS_ALLOWED_VALUE_OF`; each definition names ordered participant meanings, admissible participant domains, applicability, and obtaining condition, while separate evaluation Atoms test those declarations and the existing cardinality constraints.
- Issue IDs: `DC-001`.
- Relationship: `required prerequisite`.
- Independent fix confidence and evidence basis: `100%`, the registered primitives currently have no complete direct relation definitions.
- Expected result: one authoritative interpretation of every Term-System edge and deterministic rejection of invalid endpoints or truth conditions.
- Trade-offs: more Core Atoms and stricter migration of legacy edges; `SUBTYPE_OF` validation becomes semantically heavier than acyclicity alone.
- Owner and required authority: Operator; Core Meta-Model relation authority.
- Dependencies and execution order: first, before relying on the Term graph to validate later fixes.
- Deterministic or semantic verification: each primitive resolves to exactly one active definition; endpoint and obtaining-condition probes pass or fail identically across independent evaluators; all existing edges satisfy the declared domains.
- Recommendation: `preferred`.
- State: `PROPOSED`.

#### FX-002 - Separate ontological classification from independent Type-property axes

- Exact change: state that `SUBTYPE_OF` carries ontological classification; replace the one global qualified Type slot with separately named, single-valued properties for independent discriminators, including Scope Unit ordering, and rewrite Artifact/Type registries according to whether each value is a subtype or a true mutually exclusive property value.
- Issue IDs: `DC-002`.
- Relationship: `required prerequisite`.
- Independent fix confidence and evidence basis: `99%`, the current single slot cannot explain the active multi-axis classifications without an unstated mechanism.
- Expected result: Applicable Methodology can be classified consistently, Scope Unit ordering remains single-valued, and Status qualification has an unambiguous bearer path.
- Trade-offs: qualified Subject paths and dependent evaluations require coordinated replacement; the Operator must choose canonical property names.
- Owner and required authority: Operator; Core Meta-Model taxonomy and vocabulary authority.
- Dependencies and execution order: after `FX-001`, because classification migration relies on defined Term-System relations.
- Deterministic or semantic verification: no occurrence receives more than one value per qualified single-valued property; subtype facts are not serialized as Type values; every classification query names its axis.
- Recommendation: `preferred`.
- State: `PROPOSED`.

#### FX-003 - Make the Project exception explicit in Scope Unit ordering authority

- Exact change: replace `CAPRMEDIO-META-REQU-709` with a rule over every non-Project Scope Unit, preserving exactly one Ordered or Unordered value, and retain `CAPRMEDIO-META-REQU-710` only as the Project exception; update the evaluation so its candidate domain uses the same exclusion.
- Issue IDs: `DC-003`.
- Relationship: `required prerequisite`.
- Independent fix confidence and evidence basis: `99%`, it preserves Project as a Scope Unit and preserves the explicit zero-Type intention without contradiction.
- Expected result: one satisfiable recursive Scope Unit model with an explicit root exception.
- Trade-offs: fractality is qualified at the Project root rather than literally uniform; a future nested Project design would require reopening the exception.
- Owner and required authority: Operator; Core Meta-Model Scope authority.
- Dependencies and execution order: after or together with `FX-002`, using the canonical replacement property name selected there.
- Deterministic or semantic verification: Project has zero ordering values; every other Scope Unit has exactly one; the validator uses precisely that candidate domain.
- Recommendation: `preferred`.
- State: `PROPOSED`.

#### FX-004 - Close the lifecycle domain before requiring universal Artifact Activity

- Exact change: choose and encode one complete lifecycle policy: either define current Status and allowed values for every admitted Artifact kind, or narrow Activity and `CA-E-386` to an explicitly named status-bearing Artifact domain. Preserve Activity as derived and prohibit a second independent lifecycle axis.
- Issue IDs: `DC-004`.
- Relationship: `required prerequisite`.
- Independent fix confidence and evidence basis: `100%` that domain closure is required; `95%` that the two stated alternatives exhaust the minimal repairs.
- Expected result: every Artifact inside the Activity candidate domain has exactly one authoritative Status from which Activity is derivable.
- Trade-offs: universal lifecycle coverage adds status policy for settings, projections, journals, and structures; narrowing coverage makes Activity unavailable for some Artifact queries.
- Owner and required authority: Operator; Core Meta-Model lifecycle authority.
- Dependencies and execution order: after `FX-002`, because Status is qualified by the chosen classification path.
- Deterministic or semantic verification: enumerate every admitted Artifact kind and prove either one total Status domain plus derivation or explicit exclusion from Activity; no Tool default fills a missing source value.
- Recommendation: `preferred`.
- State: `PROPOSED`.

#### FX-005 - Introduce a Core-admission test and relocate instance policies

- Exact change: require every Core candidate to record failed expression by existing Core composition, action-facing necessity, non-redundancy, a sharp inclusion/exclusion boundary, and a reopen condition; retain generic extension and settings mechanisms in Core while proposing concrete reporting, optional-view, and implementation-tier policies for authority outside Core.
- Issue IDs: `DC-005`.
- Relationship: `complementary`.
- Independent fix confidence and evidence basis: `98%`, it follows the existing minimal-Core goal and FPF kernel/parsimony tests without assuming the excluded destination's implementation.
- Expected result: Core growth becomes reviewable and reusable while configurable policies remain expandable without Core replacement.
- Trade-offs: admission has more review overhead; relocation requires a separately authorized compatibility and destination-layer step.
- Owner and required authority: Operator; Core Meta-Model admission authority and, later, Local Configuration authority.
- Dependencies and execution order: after foundational relation and Type repairs; before adding more Core vocabulary.
- Deterministic or semantic verification: every retained Core Atom has a completed admission record; each relocated policy can vary without changing Core graph semantics; excluded targets remain unchanged in this step.
- Recommendation: `preferred`.
- State: `PROPOSED`.

#### FX-006 - Normalize the active Core against its own Claim boundary

- Exact change: split `CAPRMEDIO-GOV-REQU-294` at every independently replaceable Claim boundary and run the existing Claim-boundary evaluation across the frozen active Core frontier, creating separate issue records for additional counterexamples rather than silently bulk-rewriting them.
- Issue IDs: `DC-006`.
- Relationship: `complementary`.
- Independent fix confidence and evidence basis: `100%` for the demonstrated counterexample; completeness requires the deferred full-frontier audit.
- Expected result: the Core becomes admissible input to its own one-Atom/one-Claim authority and later normalization is evidence-driven.
- Trade-offs: Atom count and revision history grow; semantic judgment is still needed for borderline composite Claims.
- Owner and required authority: Operator authorizes; an assigned AI Agent may execute a bounded migration under the accepted threshold.
- Dependencies and execution order: after `FX-001` through `FX-004`, so the self-application evaluator operates on stable relation, Type, Scope, and lifecycle semantics.
- Deterministic or semantic verification: every active Core Atom has exactly one independently replaceable Claim and exactly one effective Claim Scope; any decision below the task threshold returns to the Operator.
- Recommendation: `preferred`.
- State: `PROPOSED`.

### FPF sources consulted (7 read; 5 used, 2 screened only)

- [used] `A.5 - Open-Ended Kernel & Extension Layering` - tested minimal-kernel admission and the boundary between reusable Core authority and instance policy.
- [used] `A.11 - Ontological Parsimony` - tested action-facing necessity, non-redundancy, sharp boundaries, and independently reviewable contributions.
- [screened only] `A.1.1 - Bounded Model-Use Structure and DDD Bounded-Context Recovery` - checked model/representation boundaries; no separate finding depended on it because the stronger issues were recoverable from direct relation, classification, and kernel patterns.
- [used] `A.6.5 - Relation-Declaration Slot Discipline` - tested primitive Relation Kind completeness and total typed source domains.
- [used] `C.3.1 - U.Kind and U.SubkindOf Core` - tested subtype obtaining, participant order, and separation of subtype classification from property values.
- [used] `C.3.2 - Kind Intent, Membership Judgment, and Extension` - tested candidate-domain and applicability consistency for universal classification rules.
- [screened only] `E.11.PUA - Pattern Use in a Working Situation and First Useful Result` - used only as the routing entrypoint for selecting the direct patterns above; no finding depends on it directly.

# Unresolved evidence gaps

#### GAP-001 - Exhaustiveness of the active-Core defect set

- Linked issue or fix IDs: `DC-001` through `DC-006`; `FX-001` through `FX-006`.
- Best current answer: the six findings are sufficient to reject the current design as internally complete and self-consistent, but they are not an exhaustive inventory.
- Missing evidence: a complete machine-assisted dependency, contradiction, duplicate-claim, missing-definition, and self-application scan over all 615 active Core Atoms using the repaired primitive semantics.
- Consequence: additional defects may become visible after foundational relation and Type ambiguities are removed.
- Exact next evidence or action: after the Operator accepts a foundational repair direction, freeze the same frontier and run a complete Core-only semantic audit, assigning new stable issue IDs rather than extending these findings silently.

#### GAP-002 - Canonical Type-axis design

- Linked issue or fix IDs: `DC-002`, `DC-003`, `DC-004`; `FX-002`, `FX-003`, `FX-004`.
- Best current answer: independent discriminators require independent qualified single-valued properties, while ontological classification belongs to `SUBTYPE_OF`.
- Missing evidence: the Operator's canonical decision on property names and on whether Artifact labels such as Projection and Structural Entity are subtype classifications, Type values, or both under explicitly separate predicates.
- Consequence: a migration could preserve surface names while changing classification truth or status qualification.
- Exact next evidence or action: present one bounded replacement taxonomy with member/non-member probes for each axis and obtain Operator approval before any Atom replacement.

#### GAP-003 - Lifecycle policy for non-Atom Artifacts

- Linked issue or fix IDs: `DC-004`, `FX-004`.
- Best current answer: universal Activity is valid only if all admitted Artifact kinds have one authoritative current Status; otherwise Activity must use a narrower candidate domain.
- Missing evidence: accepted Status values and transitions for Journal, Projection, Structural Entity/Scope Unit, Project Settings, and Framework Instance Settings.
- Consequence: the preferred alternative within `FX-004` cannot be selected without inventing policy.
- Exact next evidence or action: ask the Operator to choose universal lifecycle coverage or an explicit status-bearing subset, then define one allowed-value and transition model for every included type.

#### GAP-004 - Complete Core-versus-configuration placement audit

- Linked issue or fix IDs: `DC-005`, `DC-006`; `FX-005`, `FX-006`.
- Best current answer: reporting modes, optional architecture-view behavior, and implementation-tier placement fail the current minimal-Core necessity test unless a universal rationale is added.
- Missing evidence: a complete admission record for every active Core Atom and compatibility evidence for proposed destinations in excluded methodology sources.
- Consequence: relocating only the sampled policies could leave the boundary inconsistent, while moving them without destination analysis could break consumers.
- Exact next evidence or action: perform a separately authorized Core-admission audit first; only then inspect and modify destination sources and consumers in a distinct migration step.

# Skills used

- `$fpf design challenge`
