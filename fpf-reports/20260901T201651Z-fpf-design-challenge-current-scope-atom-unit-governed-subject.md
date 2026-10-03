## Task, scope, and boundaries

The proposal is to redefine Current Scope as the combination of an Atom's owning Scope Unit and its governed Subject, then determine whether this creates problems for the Core Meta-Model and the exact Claim Value Set consolidation detector. The proposal corrects the earlier statement that Current Scope can be derived from the carrier alone. :codex-annotation{index="1"}

The review covers active Core Meta-Model authority for Current Scope, Claim Scope, governed Subjects, Current-scope and Relational Atoms, external Job Atoms, and CA-E-403. It excludes file changes, tool implementation, source migration, and approval of revised authority. The Operator remains the project decision owner.

Project evidence was inspected directly in the active Core Meta-Model source carriers. The scope analysis was checked against the FPF scope, lexical, naming, and strict-distinction guidance identified below. The analysis completed without changing the repository.

Planned report after validation: `fpf-reports/20260901T201651Z-fpf-design-challenge-current-scope-atom-unit-governed-subject.md`. Report creation is deferred pending validation; no durable report has been created.

## Issues, weak points, and improvements

### Native result

#### Proposal, resolved source, and decision boundary

The proposal is sound only if Current Scope becomes an explicitly composite **authority-locality coordinate**, not a synonym for Claim Scope:

- the structural component identifies the Atom's owning Scope Unit;
- the subject component identifies the canonical set of Subjects referenced by the Atom's GOVERNS relations.

The scope guidance supports composite, exact, mechanically comparable scope values, but it also keeps the claim-bearing artifact, its subject, and the set-valued extent where the claim holds distinct. Therefore, a governed Subject may contribute one coordinate to CAPRMEDIO Current Scope, but it must not become or determine Claim Scope.

#### FPF Challenge Findings

##### Finding CS-CF01 — active definitions contradict the proposal

- **Result state:** concern.
- **Proposal claim and affected Entity of Concern:** Current Scope includes the Atom's owning Scope Unit and governed Subject; the affected Entity of Concern is `Atom/Current Scope`.
- **Bounded context and receiving use:** active Core Meta-Model authority used to derive and compare Current Scope.
- **Direct FPF pattern, edition, stable locator, and inspected Solution:** `A.2.6`, FPF-Knowledge-Graph source revision `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, sections `A.2.6:5` and `A.2.6:6.1–6.3`. The inspected Solution requires an exact, independently identified scope value and exact declared selectors; it does not let a carrier label silently supply the complete value.
- **Project evidence:** CA-R-920 line 20 defines Current Scope only as the owning Scope Unit reference; CA-R-1014 line 23 says Subjects must not determine Current Scope or Claim Scope.
- **Direct FPF basis:** the scope value, selector values, claim-bearing object, and Claim Scope remain distinguishable even when a composite coordinate is admitted.
- **Reviewer inference:** the proposal is a semantic replacement, not a compatible interpretation of the two active statements.
- **Consequence if unresolved:** active methodology simultaneously requires and prohibits the Subject component.
- **Candidate correction:** replace CA-R-920 and CA-R-1014 together through CS-F01 and CS-F02.
- **Unchecked dependencies and stop/return condition:** the complete downstream Current Scope dependency set is not inventoried; return when replacement wording or the dependency inventory changes.

##### Finding CS-CF02 — whole-value equality no longer classifies relationality

- **Result state:** concern.
- **Proposal claim and affected Entity of Concern:** Current Scope becomes a structural-plus-subject coordinate; the affected Entities of Concern are Current-scope Atom and Relational Atom classification.
- **Bounded context and receiving use:** CA-R-922 and CA-R-923 classification used by Job, Demand, and local Atom governance.
- **Direct FPF pattern, edition, stable locator, and inspected Solution:** `A.2.6`, the same source revision, sections `A.2.6:5`, `A.2.6:6.2`, and `A.2.6:6.3`. The inspected Solution keeps exact scope kinds, values, predicates, and claim-bearing objects distinct and permits comparison only across compatible exact values.
- **Project evidence:** CA-R-922 line 24 defines Current-scope Atom by complete equality; CA-R-923 line 24 defines Relational Atom by complete inequality; CA-R-921 line 18 keeps Claim Scope as an atomic or composite Scope Expression.
- **Direct FPF basis:** exact comparison requires compatible participant meanings; a structural-plus-subject locality coordinate is not automatically the same kind of value as a Claim Scope expression or its extension.
- **Reviewer inference:** after the proposal, `=` and `!=` over the two complete values are ill-typed for the intended cross-unit distinction.
- **Consequence if unresolved:** Subject differences can create false Relational Atoms, while real cross-unit relations can become ambiguous.
- **Candidate correction:** classify relationality through the structural Scope Unit coordinate under CS-F03.
- **Unchecked dependencies and stop/return condition:** composite Claim Scopes spanning units were not inventoried; return if their admission changes the one-target structural rule.

##### Finding CS-CF03 — the Subject component is a small set, not necessarily one Subject

- **Result state:** concern.
- **Proposal claim and affected Entity of Concern:** Current Scope contains “governed Subject”; the affected Entity of Concern is the proposed Current Scope Subject component.
- **Bounded context and receiving use:** deterministic Current Scope identity for active and draft Atoms.
- **Direct FPF pattern, edition, stable locator, and inspected Solution:** `A.2.6`, the same source revision, sections `A.2.6:5`, `A.2.6:6.1`, and `A.2.6:6.2`. The inspected Solution distinguishes one exact selector value from one exact finite set and requires identity-preserving comparison rather than syntax or list order.
- **Project evidence:** CA-R-1195 line 18 exhaustively defines Temporal Form values as CONTINUANT and OCCURRENT; CA-R-1201 requires `>=1` GOVERNS relation; CA-R-1202 permits `<=1` per Temporal Form; CA-R-1203 defines the same-form split boundary.
- **Direct FPF basis:** a composite scope component must have one exact value and deterministic equality; an unordered finite set is not identified by carrier order.
- **Reviewer inference:** the active cardinalities admit one or two governed Subjects, so a singular undefined field cannot identify Current Scope reproducibly.
- **Consequence if unresolved:** equivalent Atoms can receive different Current Scope identities through ordering or omission.
- **Candidate correction:** define the canonical Governed Subject Set under CS-F04.
- **Unchecked dependencies and stop/return condition:** no other Temporal Form value is currently admitted; return if CA-R-1195 or GOVERNS cardinality changes.

##### Finding CS-CF04 — external Job Atoms need an explicit no-unit branch

- **Result state:** concern.
- **Proposal claim and affected Entity of Concern:** Current Scope includes the Atom's owning Scope Unit; the affected Entity of Concern is the Current Scope of a Project-establishing Job Atom.
- **Bounded context and receiving use:** the external Operator-owned Job exception that establishes the Project Scope Unit.
- **Direct FPF pattern, edition, stable locator, and inspected Solution:** `A.2.6`, the same source revision, sections `A.2.6:6.2` and `A.2.6:7.8`. The inspected Solution requires explicit exact values and distinguishes an empty scope from a missing or differently typed selector; it does not define CAPRMEDIO external ownership.
- **Project evidence:** CA-R-927 line 20 requires an empty Current Scope and human Operator owner; CA-R-928 line 23 removes the Project Atom ID; CA-R-930 line 21 resolves the empty Current Scope to Operator names; CA-R-947 line 23 targets the Project Scope Unit.
- **Direct FPF basis:** absence of a structural selector must not be silently treated as the same value as an owned Scope Unit or as a set with no members.
- **Reviewer inference:** the proposed Atom-unit component needs a tagged external-owner alternative; FPF does not decide which project owner kind to select.
- **Consequence if unresolved:** the Project-establishing Job is excluded or its external ownership distinction disappears.
- **Candidate correction:** preserve the no-Scope-Unit branch and resolve it to canonical Operator owners under CS-F05.
- **Unchecked dependencies and stop/return condition:** multiple-Operator identity and carrier syntax remain unsettled; return when the Operator-set identity rule is decided.

##### Finding CS-CF05 — Current Scope derivation does not resolve Claim Scope for CA-E-403

- **Result state:** concern.
- **Proposal claim and affected Entity of Concern:** carrier plus GOVERNS Subjects determine Current Scope; the affected Entity of Concern is Claim Value Set Consolidation Candidate Evaluation.
- **Bounded context and receiving use:** exact, non-mutating CA-E-403 candidate grouping.
- **Direct FPF pattern, edition, stable locator, and inspected Solution:** `A.2.6`, the same source revision, sections `A.2.6:1`, `A.2.6:5`, and `A.2.6:6.3`. The inspected Solution keeps the claim-bearing object and exact Claim Scope distinct and requires independent designation of where the Claim holds.
- **Project evidence:** CA-E-403 line 25 requires identical Current Scope, Claim Scope, Property, and exact qualifiers; CA-R-921 line 18 independently defines Claim Scope; CA-R-1014 line 23 prohibits Subject-derived Claim Scope.
- **Direct FPF basis:** the subject coordinate and exact set-valued claim extent answer different questions and cannot substitute for one another.
- **Reviewer inference:** the proposal strengthens one grouping key but does not provide the independent Claim Scope or qualifier parser.
- **Consequence if unresolved:** the detector can report false consolidation candidates by treating Subject equality as Claim Scope equality.
- **Candidate correction:** require independent mechanical Claim Scope and qualifier resolution under CS-F06.
- **Unchecked dependencies and stop/return condition:** parser coverage was not inspected; return when formal Claim parsing or its accepted subset changes.

##### Finding CS-CF06 — Current Scope and Claim Scope need an explicit lexical boundary

- **Result state:** concern.
- **Proposal claim and affected Entity of Concern:** both the authority-locality coordinate and Claim applicability retain “Scope” names; the affected Entities of Concern are Current Scope and Claim Scope terminology.
- **Bounded context and receiving use:** Core Meta-Model authoring, navigation, Claim parsing, and normalization tooling.
- **Direct FPF pattern, edition, stable locator, and inspected Solution:** `E.10`, the same FPF source revision, sections `E.10:0`, `E.10:0.2c.24`, and `E.10:4`; coordinated with inspected `A.2.6:5–6.3`. The lexical Solution requires “scope” to be unpacked to the exact subject-defined mechanism rather than treated as one generic kind.
- **Project evidence:** CA-R-920 currently uses ownership for Current Scope, CA-R-921 uses direct Claim application for Claim Scope, and CA-R-1199 defines GOVERNS as authority about a referenced Subject.
- **Direct FPF basis:** wording must preserve the distinction between what the Claim concerns, the locality of its authority, and where the Claim holds.
- **Reviewer inference:** CAPRMEDIO can retain both names only if the two mechanisms and their components are stated explicitly; the external framework does not override the Operator's local naming decision.
- **Consequence if unresolved:** Subject metadata can be mistaken for claim extent and Claim Scope can appear redundant.
- **Candidate correction:** define the two-component Current Scope under CS-F01 and preserve independent Claim Scope under CS-F02 and CS-F06.
- **Unchecked dependencies and stop/return condition:** reader-facing naming alternatives were not compared; return if the Operator reopens the Current Scope name rather than only its definition.

#### Strengths within inspected scope

- The proposal identifies authority more precisely than the carrier alone: two Atoms in one Scope Unit but governing different Subjects no longer appear to share the complete Current Scope.
- Both components are mechanically available without adding duplicate frontmatter: the carrier supplies the owning Scope Unit and `subjects.governs` supplies Subject references.
- The model can preserve Subject identity because Current Scope contains references to Subjects; it does not make Subjects dependent entities of the Atom.
- The added subject coordinate gives CA-E-403 a stronger deterministic grouping key and prevents consolidation across different governed Subjects.

#### Unchecked claims and insufficient basis

- No complete Claim parser or Claim Scope resolver was inspected. This review therefore does not establish that CA-E-403 can resolve Claim Scope or exact qualifiers for every active Atom.
- No migration impact count was produced for every authority that tests `Current Scope is empty`, compares Current Scope with Claim Scope, or derives direction from them.
- The exact carrier syntax for an external Current Scope owner with more than one Operator is not settled by the inspected authority.

#### Return to project authority

The Operator can accept the composite Current Scope model without accepting Subject-to-Claim-Scope derivation. The smallest coherent decision is:

> Current Scope consists of one Current Scope Owner coordinate and one canonical Governed Subject Set. GOVERNS relations determine only the Subject component. Claim Scope remains independently resolved from the Claim. Relational classification compares structural Scope Unit coordinates, not the complete Current Scope and Claim Scope values.

This decision is sufficient to revise the model. It is not sufficient by itself to complete CA-E-403; exact Claim Scope and qualifier resolution remains a separate prerequisite.

### Issue registry

#### CS-01 — active authority contradiction

- **Issue or weak point:** CA-R-920 and CA-R-1014 reject the proposed Subject component of Current Scope.
- **Evidence:** `CA-R-920...define-current-scope.md:20` and `CA-R-1014...separate-subjects-from-scope-coordinates.md:23`.
- **Consequence:** the same active methodology would both require and prohibit Subject-derived Current Scope information.
- **Affected target or bounded context:** Core Meta-Model Current Scope authority and every active or draft Atom.
- **Issue confidence and evidence basis:** 100%; direct active source statements.
- **Coverage limit or uncertainty:** replacement wording and migration count were not evaluated.
- **Lifecycle state:** identified.
- **Mapped fix IDs:** CS-F01, CS-F02.

#### CS-02 — incompatible equality used for Atom classification

- **Issue or weak point:** CA-R-922 and CA-R-923 compare values that would have different structures after the proposal.
- **Evidence:** `CA-R-922...define-current-scope-atom.md:24`, `CA-R-923...define-relational-atom.md:24`, and CA-R-921's independent Scope Expression definition.
- **Consequence:** ordinary and Relational Atoms become ambiguous or are classified by Subject differences instead of cross-unit relation.
- **Affected target or bounded context:** Current-scope Atom and Relational Atom taxonomy, including Job and Demand.
- **Issue confidence and evidence basis:** 100%; direct active definitions plus the proposed value shape.
- **Coverage limit or uncertainty:** composite Claim Scopes spanning multiple Scope Units were not exhaustively inventoried.
- **Lifecycle state:** identified.
- **Mapped fix IDs:** CS-F03.

#### CS-03 — governed-subject cardinality is underspecified

- **Issue or weak point:** the proposal says one governed Subject, while active rules admit one or two GOVERNS relations.
- **Evidence:** CA-R-1195 line 18 limits Temporal Form to CONTINUANT and OCCURRENT; CA-R-1201 requires `>=1`; CA-R-1202 permits `<=1` per Temporal Form; CA-R-1203 splits only independently replaceable same-form Subjects.
- **Consequence:** two equivalent Atoms could receive different Current Scope identities because of ordering or an omitted Occurrent/Continuant component.
- **Affected target or bounded context:** Current Scope identity and deterministic comparison.
- **Issue confidence and evidence basis:** 100%; direct cardinality rules.
- **Coverage limit or uncertainty:** none material for the stated 1–2 cardinality.
- **Lifecycle state:** identified.
- **Mapped fix IDs:** CS-F04.

#### CS-04 — external Job exception has no owning unit

- **Issue or weak point:** Project-establishing Jobs cannot supply the proposed Atom-unit component.
- **Evidence:** CA-R-927 requires an empty Current Scope, CA-R-930 resolves it to Operator names, CA-R-928 omits Project Atom ID, and CA-R-947 targets the Project Scope Unit.
- **Consequence:** the fractal Project Job exception is lost or becomes an undocumented second Current Scope kind.
- **Affected target or bounded context:** external Job Atoms and Project establishment.
- **Issue confidence and evidence basis:** 100%; direct active authority.
- **Coverage limit or uncertainty:** multiple-Operator canonicalization remains unspecified.
- **Lifecycle state:** identified.
- **Mapped fix IDs:** CS-F05.

#### CS-05 — CA-E-403 still lacks an independent Claim Scope resolution

- **Issue or weak point:** carrier plus GOVERNS relations determine the proposed Current Scope, not the independent Claim Scope or all Claim qualifiers.
- **Evidence:** CA-E-403 requires identical Current Scope, Claim Scope, Property, and qualifiers; CA-R-921 defines Claim Scope independently; current CA-R-1014 correctly blocks Subject-to-Claim-Scope derivation.
- **Consequence:** an exact detector can still produce false positives if it substitutes governed Subject equality for Claim Scope equality.
- **Affected target or bounded context:** Claim Value Set consolidation candidate detection.
- **Issue confidence and evidence basis:** 100%; direct required detector key and independent Claim Scope definition.
- **Coverage limit or uncertainty:** a future bounded parser may support only a formal subset.
- **Lifecycle state:** identified.
- **Mapped fix IDs:** CS-F06.

#### CS-06 — authority locality and claim extent can be conflated

- **Issue or weak point:** Current Scope and Claim Scope would both use “Scope” while answering different questions.
- **Evidence:** project authority uses Current Scope for ownership and Claim Scope for direct application; the inspected scope pattern keeps the claim-bearing object, subject-related coordinates, and the set where a claim holds distinct.
- **Consequence:** Subjects may be incorrectly treated as scope extents, or Claim Scope may be reconstructed from metadata instead of the Claim.
- **Affected target or bounded context:** terminology, Claim parsing, navigation, and normalization tooling.
- **Issue confidence and evidence basis:** 98%; direct project definitions and scope-pattern distinction, with CAPRMEDIO retaining final naming authority.
- **Coverage limit or uncertainty:** the project may intentionally use a local meaning of Current Scope, provided the distinction is explicit.
- **Lifecycle state:** identified.
- **Mapped fix IDs:** CS-F01, CS-F02, CS-F06.

### Fix and improvement register

#### CS-F01 — define Current Scope as a two-component derived coordinate

- **Exact change:** replace CA-R-920 with a definition equivalent to: “Current Scope means the derived authority-locality coordinate consisting of one Current Scope Owner and one canonical Governed Subject Set.”
- **Addressed issue IDs:** CS-01, CS-06.
- **Relationship:** required prerequisite.
- **Independent fix confidence and evidence basis:** 99%; it directly expresses the proposal while preserving component distinctions.
- **Expected result:** Current Scope becomes mechanically derivable from structural ownership plus governed Subjects without duplicate frontmatter.
- **Trade-offs:** changes the kind and equality semantics of an established Property.
- **Owner and required authority:** Operator; Core Meta-Model Requirement replacement authority.
- **Dependencies and execution order:** first; precedes CS-F02 through CS-F06.
- **Deterministic or semantic verification:** deterministic schema and equality tests over both components, plus semantic review of the local term.
- **Recommendation:** preferred.
- **State:** proposed.

#### CS-F02 — narrow subject-scope independence instead of deleting it

- **Exact change:** replace CA-R-1014 with: “an Atom's GOVERNS Subjects determine only its Current Scope Subject component; Subjects must not determine its Current Scope Owner or Claim Scope.”
- **Addressed issue IDs:** CS-01, CS-06.
- **Relationship:** complementary.
- **Independent fix confidence and evidence basis:** 99%; preserves the valuable anti-conflation boundary while admitting the new coordinate.
- **Expected result:** Subject identity contributes to Current Scope without laundering Subject metadata into structural ownership or claim extent.
- **Trade-offs:** every consumer of CA-R-1014 must distinguish the two Current Scope components.
- **Owner and required authority:** Operator; Core Meta-Model Requirement replacement authority.
- **Dependencies and execution order:** after CS-F01 and before detector changes.
- **Deterministic or semantic verification:** fixtures where GOVERNS changes only the Subject component and cannot change the owner or Claim Scope.
- **Recommendation:** preferred.
- **State:** proposed.

#### CS-F03 — classify relationality through the structural coordinate

- **Exact change:** replace CA-R-922 and CA-R-923 so Current-scope versus Relational Atom classification compares the Claim Scope's target Scope Unit coordinate with Current Scope Owner, not complete Current Scope and Claim Scope values.
- **Addressed issue IDs:** CS-02.
- **Relationship:** required prerequisite.
- **Independent fix confidence and evidence basis:** 99%; cross-unit direction is the active purpose of Job and Demand relations.
- **Expected result:** Subject differences do not turn local Atoms into Relational Atoms; Job and Demand remain cross-unit Requirement Atoms.
- **Trade-offs:** Claim Scope needs an exact structural-target projection for classification.
- **Owner and required authority:** Operator; Core Meta-Model taxonomy authority.
- **Dependencies and execution order:** after CS-F01; before migrating Job, Demand, and direction rules.
- **Deterministic or semantic verification:** same-owner and different-owner fixtures, including direct-child Job and permitted Demand targets.
- **Recommendation:** preferred.
- **State:** proposed.

#### CS-F04 — canonicalize all governed Subjects as one set-valued component

- **Exact change:** define Governed Subject Set as the unique set of all GOVERNS Subject references on the Atom, with cardinality 1–2, `<=1` per Temporal Form, canonical comparison by Temporal Form and canonical Subject Path, and no authority in authored list order.
- **Addressed issue IDs:** CS-03.
- **Relationship:** required prerequisite.
- **Independent fix confidence and evidence basis:** 99%; directly follows CA-R-1195 and CA-R-1201 through CA-R-1203.
- **Expected result:** Current Scope identity is reproducible for Atoms with one Continuant, one Occurrent, or both.
- **Trade-offs:** Current Scope is not a simple two-scalar tuple; its Subject component is a small set.
- **Owner and required authority:** Operator; Core Meta-Model Requirement and Delivery authority.
- **Dependencies and execution order:** after CS-F01; before Current Scope comparison tooling.
- **Deterministic or semantic verification:** duplicate, missing, reordered, same-form, and dual-form fixtures.
- **Recommendation:** preferred.
- **State:** proposed.

#### CS-F05 — preserve external ownership as an explicit structural branch

- **Exact change:** define Current Scope Owner as the owning Scope Unit when present and the canonical identified Operator owner set when the Atom has no owning Scope Unit; rewrite “Current Scope is empty” checks as “Current Scope has no Scope Unit owner.”
- **Addressed issue IDs:** CS-04.
- **Relationship:** complementary.
- **Independent fix confidence and evidence basis:** 98%; it preserves the accepted external Project Job exception, while multi-Operator identity needs exact carrier governance.
- **Expected result:** Project-establishing Jobs remain outside Project scope-unit ownership without losing Current Scope identity.
- **Trade-offs:** Current Scope Owner becomes a tagged union rather than only a Scope Unit reference.
- **Owner and required authority:** Operator; Core Meta-Model and Delivery authority.
- **Dependencies and execution order:** after CS-F01 and before Job validation migration.
- **Deterministic or semantic verification:** one-Operator and multiple-Operator Project Job fixtures, plus rejection of ambiguous owners.
- **Recommendation:** preferred.
- **State:** proposed.

#### CS-F06 — keep Claim Scope resolution independent in CA-E-403

- **Exact change:** use the composite Current Scope as one grouping key, but require a mechanically parsed Claim Scope and exact qualifiers as separate keys. Skip and report any Atom whose Claim Scope cannot be resolved; never substitute GOVERNS Subjects for Claim Scope.
- **Addressed issue IDs:** CS-05, CS-06.
- **Relationship:** required prerequisite.
- **Independent fix confidence and evidence basis:** 100%; CA-E-403 explicitly requires both values and prohibits semantic inference.
- **Expected result:** the detector gains stronger Subject-aware grouping without false consolidation across different claim extents.
- **Trade-offs:** coverage remains partial until the formal Claim parser supports every relevant Claim form.
- **Owner and required authority:** Operator for authority; AI Agent for later implementation after approval.
- **Dependencies and execution order:** after CS-F01, CS-F02, and CS-F04; Claim parser or resolver before complete detector coverage.
- **Deterministic or semantic verification:** positive candidates with identical parsed scopes and negative fixtures differing by scope, qualifier, Subject, or owner.
- **Recommendation:** preferred.
- **State:** proposed.

## Unresolved evidence gaps

### CS-G01 — complete impact surface

- **Linked issue or fix IDs:** CS-01 through CS-05; CS-F01 through CS-F05.
- **Best current answer:** CA-R-920, CA-R-1014, CA-R-922, CA-R-923, external Job rules, and direction rules must change together.
- **Missing evidence:** exhaustive active-Atom and tool inventory of every Current Scope equality, emptiness, ownership, and direction dependency.
- **Consequence:** a partial migration could leave contradictory active authority or stale validators.
- **Exact next evidence or action:** run a bounded dependency search over active Core Meta-Model, Local Configuration, and related Tool Scope Units before authoring replacements.

### CS-G02 — exact external-owner identity

- **Linked issue or fix IDs:** CS-04, CS-F05.
- **Best current answer:** the external structural component should be a canonical Operator owner set.
- **Missing evidence:** accepted rule for ordering and identifying multiple Operators in the Current Scope Owner component.
- **Consequence:** two equivalent external Job Atoms may receive different Current Scope identities.
- **Exact next evidence or action:** settle one canonical Operator-set identity rule before migrating external Job carriers.

### CS-G03 — complete Claim Scope parser coverage

- **Linked issue or fix IDs:** CS-05, CS-F06.
- **Best current answer:** CA-E-403 may safely report only the subset whose Claim Scope and qualifiers are mechanically resolved.
- **Missing evidence:** formal parser coverage for atomic and composite Scope Expressions in active Claims.
- **Consequence:** VSC-2 remains incomplete, though it can fail closed without false positives.
- **Exact next evidence or action:** inventory relevant Claim forms, define parser acceptance boundaries, and test exact skip diagnostics.

## Skills used

- `$fpf design challenge`

### FPF sources consulted (5 read; 4 used)

- **used:** `E_The FPF Constitution and Authoring Guides/10_11_First-Practical Entry and Pattern-Use Discoverability Discipline/01_E.11.PUA - Pattern Use in a Working Situation and First Useful Result.md` — routing entrypoint and result boundary.
- **used:** `A_Kernel Architecture Cluster/02_System-Role Kinds and Assignments/06_A.02.06 - Unified Scope Mechanism (USM)- Context Slices & Scopes.md` — exact, composite, set-valued scope and claim-scope separation.
- **used:** `E_The FPF Constitution and Authoring Guides/09_10_Unified Lexical Rules for FPF/00_E.10 - Unified Lexical Rules for FPF.md` — recovery of the exact mechanism hidden by “scope.”
- **screened only:** `F_The Unification Suite (U-Suite)- Concept Sets, SenseCells, and System-Role Kinds and Assignments/18_Local-First Unification Naming Protocol/00_F.18 - Local-First Unification Naming Protocol.md` — durable naming guidance; not decisive for the project term.
- **used:** `A_Kernel Architecture Cluster/07_Strict Distinction (Clarity Lattice)/00_A.07 - Strict Distinction (Clarity Lattice).md` — separation of entity, formal coordinate, relation, and representation.
