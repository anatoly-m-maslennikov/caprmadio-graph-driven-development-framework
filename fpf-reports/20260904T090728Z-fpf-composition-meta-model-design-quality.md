# Task, scope, and boundaries

The validated Plan challenged the current active CAPRMEDIO meta-model authority in `CORE_META_MODEL`, then conditionally attempted `$fpf quality improve`. The challenge inspected 619 active Markdown Atom carriers under `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL` and produced seven open issues with seven proposed fixes. For step 2, the Operator answered blocking question `BQ-001` with option `3`, **No mutation**. No issue ID was accepted and no mutation authority was granted, so the quality-improvement step returned `STOP_NO_AUTHORIZED_CHANGE` before target analysis or change.

The challenged frontier is identified by digest `94b287a0eb2e01344641bf8e362e76a09496104b4d053cf297f8ea52df225319`. Its validated recipe starts at the workspace root, enumerates regular `*.md` files below the Core carrier root, excludes paths containing `/archive/` or `/drafts/`, sorts relative paths bytewise with `LC_ALL=C`, emits standard `shasum -a 256` lines, concatenates them, and hashes that concatenation once with `shasum -a 256`.

`LOCAL_CONFIGURATION`, settings TOML carriers, Tool consumers, project artifacts, generated Applicable Methodology, and implementation migration were excluded throughout. No analyzed `CORE_META_MODEL` carrier or excluded target was changed. Validated delivery of this report is separate from target mutation.

Saved report: fpf-reports/20260904T090728Z-fpf-composition-meta-model-design-quality.md

### Composition receipt

- Exact invocation:
  ```text
  [$fpf](/Users/am/.codex/skills/fpf/SKILL.md) plan challenge design + improve quality
  about meta-model onlyb
  ```
- Selected profile: none.
- Requested sequence: `$fpf design challenge` -> `$fpf quality improve`.
- Executed prefix: `$fpf design challenge`, followed by the step-2 authorization-gate resolution.
- Unexecuted suffix: quality target mutation and before/after re-evaluation.
- Typed-edge results:
  - validated Plan -> design challenge: passed with the Core-only target and all exclusions preserved;
  - design challenge -> quality improve: the complete validated issue, fix, gap, evidence, and frontier handoff was available;
  - quality-improvement authorization gate: Operator option `3` accepted no issues and granted no mutation authority, producing `STOP_NO_AUTHORIZED_CHANGE`.
- Final state: `STOP_NO_AUTHORIZED_CHANGE`.
- Context ledger: 6 direct FPF pages read and used in step 1; 0 new direct pages read, used, or deferred in step 2.
- Carried IDs: `DC-001..DC-007`, `FX-001..FX-007`, and `GAP-001..GAP-005`; none was accepted, applied, or closed.

### Campaign handoff

- Campaign ID: `FPF-CAMPAIGN-4bc1f7d2`.
- Phase: complete and stopped without an authorized quality target change.
- Semantic and carrier frontier: the unchanged Core frontier described above.
- Finding lifecycle: `DC-001..DC-007` remain `OPEN`; `FX-001..FX-007` remain `PROPOSED`.
- Operator disposition: `BQ-001 = 3`; this is an authority decision, not evidence that any finding is resolved.
- Permitted successor: a new, explicitly authorized invocation may accept issue IDs and declare a recoverable target change; this Plan does not continue automatically.

# Issues, weak points, and improvements

### Native result

#### Design challenge: 1. Proposal, resolved FPF source, and decision boundary

The proposal is an open, recursively self-describing Core Meta-Model whose active Atoms define its entity taxonomy, relation vocabulary, carrier rules, Claim boundaries, and extension boundary. The FPF challenge tested kernel minimality, kind/value/relation separation, model/representation separation, relation-participant precision, and self-application. The Operator, not FPF, retains authority to accept or reject every issue and fix.

#### Design challenge: 2. FPF Challenge Findings

The highest-consequence defect is a direct contradiction in the Artifact subtype authority. Further findings concern Methodology Source participant conflation, explicit/effective Claim Scope conflation, project-specific identifier policy in the Core, incompatible ninth Content Role labels, a self-application violation, and a potentially representation-coupled Entity boundary. The complete validated records appear in the registry below.

#### Design challenge: 3. Strengths within inspected scope

- `CA-R-1261`, `CA-R-1217`, and `CA-R-1375` already define an open extension boundary.
- `CA-R-1307`, `CA-R-1394`, `CA-R-1395`, `CA-R-1396`, and `CA-E-386` separate type-qualified Status from Artifact-level Activity.
- Structural Entity, Scope Unit, and Atom Collection are distinguishable.
- `CA-R-918`, `CA-R-154`, and `CA-E-384` already state the intended one-Atom/one-Claim discipline.

#### Design challenge: 4. Unchecked claims and insufficient basis

The challenge did not run repository validators, inspect excluded layers, or perform an exhaustive semantic pairwise comparison of all 619 Atoms. It does not claim that the findings are exhaustive or safe to materialize without authorization and re-evaluation.

#### Design challenge: 5. Return to project authority

All findings were returned to the Operator. The Operator selected no mutation, so none was accepted for the quality loop.

#### Quality improve: 1. Loop contract and resolved FPF source

The loop required an accepted issue set, recoverable Core target version, rerunnable evaluation frame, and bounded mutation authority. Option `3` supplied no change authority. The command stopped at this project-authority gate before native target analysis, so no new direct FPF page was opened.

#### Quality improve: 2. Baseline target version and evaluation

The inherited Core frontier remains the candidate baseline reference. No baseline quality evaluation was executed because no authorized target version existed for a valid before/after comparison.

#### Quality improve: 3. Bounded change hypothesis and implementation evidence

No change hypothesis was selected. No carrier was edited, versioned, replaced, or archived. Implementation evidence is none.

#### Quality improve: 4. Re-evaluation and declared-coordinate comparison

No re-evaluation occurred. Without a changed target version, no improvement, regression, or unchanged-quality claim is valid.

#### Quality improve: 5. Trade-offs, costs, risks, and uncertainty

The stop prevented unauthorized changes and protected concurrent repository work. Its cost is that all seven design findings remain unresolved and downstream impact remains unknown.

#### Quality improve: 6. Outcome and stop/continue/rollback/switch decision

- Outcome: `insufficient basis` for a quality-improvement claim because no target change was authorized.
- Stop: `STOP_NO_AUTHORIZED_CHANGE`.
- Continue: prohibited under this Plan.
- Rollback: not applicable because no mutation occurred.
- Switch method: not authorized or needed.

### Issue registry

#### DC-001 - Artifact subtype authority contradicts active classifications

- FPF result state: `concern`.
- Issue: `CAPRMEDIO-META-REQU-741` prohibits an Artifact subtype axis, while `CA-R-1252`, `CA-R-1253`, `CA-R-1254`, `CA-R-1377`, `CA-R-1400`, and `CA-R-1403` actively declare Artifact subtypes.
- Proposal claim and affected Entity of Concern: the Core has one coherent Artifact classification system; Entity of Concern is the Artifact subtype axis.
- Bounded context and receiving use: active Core taxonomy consumed by graph construction and conformance evaluation.
- Direct FPF pattern record: `C.3.1 - U.Kind and U.SubkindOf Core`, edition `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, locator `C.3.1:5 Solution`; recover membership boundaries and do not use subkind for dependency, part-whole, slot filling, or admission.
- Direct FPF basis: subkind and allowed Type value are different claims with different tests.
- Project evidence: `CAPRMEDIO-META-REQU-741--prohibit-artifact-subtypes.md:19-21`, `CA-R-1252...classify-atom-as-an-artifact.md:16-18`, and the equivalent active classifications named above.
- Reviewer inference: **reviewer inference** - both sides cannot be simultaneously satisfied.
- Consequence: graph construction and validation cannot produce one authoritative taxonomy.
- Candidate correction: preserve explicit Artifact subtypes and replace the universal prohibition with separate subtype-admission and Type-value laws.
- Affected target or bounded context: Core Entity taxonomy.
- Issue confidence and evidence basis: `100%`, direct textual contradiction.
- Coverage limit or uncertainty: future subtype admission criteria were not exhaustively inspected.
- Unchecked dependency and stop/return condition: return if a proposed subtype lacks a sharp membership boundary; stop before mutation without accepted `DC-001`.
- Lifecycle state: `OPEN`.
- Mapped fix IDs: `FX-001`.

#### DC-002 - Methodology Source conflates source selection with revision provenance

- FPF result state: `concern`.
- Issue: `CA-R-1228` treats Scope Units as Methodology Sources, while `CA-R-1219` defines Methodology Source as the `DERIVED_FROM` target role of one exact Artifact Revision.
- Proposal claim and affected Entity of Concern: one stable Term serves source selection and exact provenance; Entity of Concern is the source-selection/derivation boundary.
- Bounded context and receiving use: active Core authority used by Applicable Methodology compilation.
- Direct FPF pattern record: `A.6.5 - Relation-Declaration Slot Discipline`, edition `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, locator `A.6.5:4-4.2 Solution`; recover the direct relation and exact participant ValueKinds while keeping participants, references, and fields distinct.
- Direct FPF basis: relations with different participant kinds and predicates must not share one overloaded participant role.
- Project evidence: `CA-R-1228...require-core-and-local-sources...md:18-20`, `CA-R-1219...define-methodology-source.md:17-19`, `CA-D-305`, and `CA-D-313`.
- Reviewer inference: **reviewer inference** - source selection targets a Scope Unit or collection, while member provenance targets an Artifact Revision.
- Consequence: the compiler cannot distinguish source selection from exact member provenance.
- Candidate correction: define Methodology Source at source-Scope-Unit level and reserve `DERIVED_FROM` for projected revision -> exact source revision.
- Affected target or bounded context: Applicable Methodology selection and provenance.
- Issue confidence and evidence basis: `99%`, incompatible participant kinds are named for one Term.
- Coverage limit or uncertainty: compiler representation was excluded.
- Unchecked dependency and stop/return condition: return if excluded compiler schemas already separate both relations formally; stop before mutation without accepted `DC-002`.
- Lifecycle state: `OPEN`.
- Mapped fix IDs: `FX-002`.

#### DC-003 - Claim Scope conflates optional authored and mandatory effective values

- FPF result state: `concern`.
- Issue: `CA-R-919` permits `<=1` explicit Scope, `CA-R-921` derives effective Scope when absent, but `CA-R-655` and `CA-E-384` require one unqualified Claim Scope.
- Proposal claim and affected Entity of Concern: one Claim Scope Term serves both input and resolved output; Entity of Concern is Atom/Claim/Scope.
- Bounded context and receiving use: Core Claim-boundary authority used by validators.
- Direct FPF pattern record: `A.11 - Ontological Parsimony`, edition `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, locator `A.11:2 Solution`; preserve reviewable distinctions and sharp boundaries.
- Direct FPF basis: parsimony does not justify collapsing values whose presence, cardinality, and evaluation consequences differ.
- Project evidence: `CA-R-919...limit-each-claim-to-one-explicit-scope.md:17-19`, `CA-R-921...resolve-optional-claim-scope.md:17-19`, `CA-R-655...define-atom-artifact-form.md:19-21`, and `CA-E-384...validate-composite-claims...md:17-19`.
- Reviewer inference: **reviewer inference** - optional authored and exactly-one effective Scope are different properties.
- Consequence: a validator can reject a valid Atom whose explicit Scope is omitted.
- Candidate correction: qualify Explicit Scope and Effective Scope and define a deterministic fallback.
- Affected target or bounded context: Atom/Claim/Scope and Claim validation.
- Issue confidence and evidence basis: `99%`, active laws use one unqualified Term for two stages.
- Coverage limit or uncertainty: validator implementation was not executed.
- Unchecked dependency and stop/return condition: return if excluded Tool schemas already distinguish both formally; stop before mutation without accepted `DC-003`.
- Lifecycle state: `OPEN`.
- Mapped fix IDs: `FX-003`.

#### DC-004 - Project-specific identifier policy leaks into the Core

- FPF result state: `concern`.
- Issue: Core rules hard-code the current Project Prefix `CA` in Epic and Plan identifiers.
- Proposal claim and affected Entity of Concern: Core is reusable without project-local coupling; Entity of Concern is the Core admission boundary.
- Bounded context and receiving use: Core reused across Projects and specialized outside Core.
- Direct FPF pattern record: `A.5 - Open-Ended Kernel & Extension Layering`, edition `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, locator `A.5:4 Solution`; keep the kernel minimal and project-specific vocabulary outside it.
- Direct FPF basis: a project literal is not a universal kernel invariant without separate evidence.
- Project evidence: `CA-R-1304...define-epic-identifier-grammar.md:13-15`, `CA-R-1305...reserve-ca-p-identifiers...md:17-19`, and boundary authorities `CA-R-1217`, `CA-R-1218`, `CA-R-1261`, `CA-R-1375`.
- Reviewer inference: **reviewer inference** - hard-coded `CA` prevents prefix substitution without Core replacement.
- Consequence: another Project inherits caprmedio-specific identity policy.
- Candidate correction: keep generic grammar in Core and supply Project Prefix outside Core.
- Affected target or bounded context: Core admission and Artifact identifiers.
- Issue confidence and evidence basis: `99%`, exact project token appears in active Core authority.
- Coverage limit or uncertainty: all 619 Atoms were not classified as Core or local.
- Unchecked dependency and stop/return condition: return if the Operator declares `CA` universal; stop before mutation without accepted `DC-004`.
- Lifecycle state: `OPEN`.
- Mapped fix IDs: `FX-004`.

#### DC-005 - The ninth Content Role has incompatible canonical labels

- FPF result state: `concern`.
- Issue: active authority uses `Operations`, `Ops`, and `OPERATIONS` for the same exact Content Role value.
- Proposal claim and affected Entity of Concern: Content Role has one exact allowed-value set; Entity of Concern is its ninth value.
- Bounded context and receiving use: Core vocabulary consumed by identifiers, folders, selectors, and projection membership.
- Direct FPF pattern record: `A.11 - Ontological Parsimony`, edition `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, locator `A.11:2 Solution`; test overlap and a sharp boundary before admitting another value.
- Direct FPF basis: labels without distinct membership criteria should not act as distinct authoritative values.
- Project evidence: `CA-R-1283...register-content-role-values.md:13-15`, `CAPRMEDIO-META-REQU-116...use-nouns...md:16-22`, and `CA-R-1315...select-only-current-active-rmedo...md:17-19`.
- Reviewer inference: **reviewer inference** - the spellings compete for one value rather than define separate roles.
- Consequence: exact-value validation and selectors can disagree.
- Candidate correction: Operator chooses one canonical label; the other may remain only as a non-authoritative migration alias.
- Affected target or bounded context: Atom/Content Role.
- Issue confidence and evidence basis: `100%` that one label is required; no evidence-based preference between the labels.
- Coverage limit or uncertainty: external consumers were excluded.
- Unchecked dependency and stop/return condition: return for a neutral Operator label choice; stop before mutation without accepted `DC-005` and that choice.
- Lifecycle state: `OPEN`.
- Mapped fix IDs: `FX-005`.

#### DC-006 - The Core violates its own one-Atom/one-Claim authority

- FPF result state: `concern`.
- Issue: `CAPRMEDIO-META-REQU-116` contains several independently replaceable obligations plus a duplicated Primary claim, contrary to `CA-R-918` and `CA-R-154`.
- Proposal claim and affected Entity of Concern: Core Atoms conform to their own Claim-boundary rules; Entity of Concern is `CAPRMEDIO-META-REQU-116`.
- Bounded context and receiving use: Core self-application and Claim validation.
- Direct FPF pattern record: `A.11 - Ontological Parsimony`, edition `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, locator `A.11:2 Solution`; preserve independently reviewable distinctions and reject redundancy.
- Direct FPF basis: contributions with independent replacement conditions should remain separately reviewable.
- Project evidence: `CAPRMEDIO-META-REQU-116...use-nouns...md:16-26`, `CA-R-918...give-every-atom-one-claim.md:16-18`, and `CA-R-154...keep-each-atom-semantically-irreducible.md:18-20`.
- Reviewer inference: **reviewer inference** - noun constraint, canonical labels, future admission, and summary restatement can change independently.
- Consequence: the self-describing Core is not valid input to its own stated invariant.
- Candidate correction: split independent claims, remove the duplicate projection, then evaluate every active Core Atom.
- Affected target or bounded context: Core self-application.
- Issue confidence and evidence basis: `99%`, one counterexample refutes universal conformance.
- Coverage limit or uncertainty: no exhaustive Atom Claim audit was run.
- Unchecked dependency and stop/return condition: return if a deterministic claim-boundary decision is unavailable; stop before mutation without accepted `DC-006`.
- Lifecycle state: `OPEN`.
- Mapped fix IDs: `FX-006`.

#### DC-007 - Entity identity may depend on graph representation

- FPF result state: `FPF not decisive`.
- Issue: `CA-R-1248` defines Entity through representation in a CAPRMEDIO Graph.
- Proposal claim and affected Entity of Concern: Entity is correctly admitted by graph participation; Entity of Concern is root Entity admission.
- Bounded context and receiving use: Core ontology before and after graph materialization.
- Direct FPF pattern record: `C.3.2 - Kind Intent, Membership Judgment, and Extension`, edition `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, locator `C.3.2:4-8 Solution and change discipline`; keep kind, declaration, judgment, and representation separately recoverable.
- Direct FPF basis: representation must not create identity unless the candidate kind is explicitly representation-bound.
- Project evidence: `CA-R-1248...define-entity.md:13-15` and non-authoritative Projection authority `CA-R-1213`.
- Reviewer inference: **reviewer inference** - the wording is unsafe under a general Entity reading but may be acceptable under an explicit modeled-Entity reading.
- Consequence: graph absence or staleness may appear to change Entity admission.
- Candidate correction: decouple Entity from graph materialization or explicitly narrow and rename it to `CAPRMEDIO Entity`.
- Affected target or bounded context: root Entity admission.
- Issue confidence and evidence basis: `94%`, because the intended candidate domain is not explicit.
- Coverage limit or uncertainty: the Core does not state whether only modeled participants qualify.
- Unchecked dependency and stop/return condition: return for an Operator domain decision; stop `FX-007` until one alternative is accepted.
- Lifecycle state: `OPEN`.
- Mapped fix IDs: `FX-007`.

### Fix and improvement register

#### FX-001 - Separate Artifact subtype and Type-value laws

- Exact change: replace the universal Artifact-subtype prohibition with an open subtype-admission law, retain Type as a single-valued allowed-value Property, and prohibit conflating the two.
- Addressed issue IDs: `DC-001`.
- Relationship: `required prerequisite`.
- Independent fix confidence and evidence basis: `99%`, preserves active classifications and FPF kind/subkind separation.
- Expected result: one satisfiable Artifact taxonomy.
- Trade-offs: future subtypes need explicit boundary tests.
- Owner and required authority: Operator; Core source authority.
- Dependencies and execution order: first.
- Deterministic or semantic verification: no active prohibition contradicts `SUBTYPE_OF Artifact`; subtype and Type-value validators remain distinct.
- Recommendation: `preferred`.
- State: `PROPOSED`.

#### FX-002 - Split Methodology Source selection from revision provenance

- Exact change: define Methodology Source at selected source Scope Unit or collection level; reserve `DERIVED_FROM` for projected Artifact Revision -> source Artifact Revision and name that target role separately.
- Addressed issue IDs: `DC-002`.
- Relationship: `required prerequisite`.
- Independent fix confidence and evidence basis: `99%`, participants, cardinalities, and predicates differ.
- Expected result: source selection and member provenance become deterministic.
- Trade-offs: coordinated subject and Delivery replacement is required.
- Owner and required authority: Operator; Core source authority.
- Dependencies and execution order: after `FX-001` only if shared taxonomy changes are material.
- Deterministic or semantic verification: Scope Units occur only in selection and Artifact Revisions only in derivation.
- Recommendation: `preferred`.
- State: `PROPOSED`.

#### FX-003 - Separate Explicit and Effective Claim Scope

- Exact change: define optional `Atom/Claim/Explicit Scope` and exactly-one `Atom/Claim/Effective Scope`, with fallback to Atom/Scope.
- Addressed issue IDs: `DC-003`.
- Relationship: `required prerequisite`.
- Independent fix confidence and evidence basis: `99%`, preserves the intended fallback while separating input and result.
- Expected result: omission of explicit Scope is valid and still yields one effective Scope.
- Trade-offs: subject paths require migration.
- Owner and required authority: Operator; Core source authority.
- Dependencies and execution order: before self-application validation.
- Deterministic or semantic verification: zero or one explicit Scope yields one Effective Scope; more than one fails.
- Recommendation: `preferred`.
- State: `PROPOSED`.

#### FX-004 - Parameterize project identifier policy

- Exact change: require Core admission necessity, replace hard-coded `CA` with a Project Prefix parameter, and remove project-specific values from the Core target.
- Addressed issue IDs: `DC-004`.
- Relationship: `complementary`.
- Independent fix confidence and evidence basis: `99%`, follows the declared extension boundary and kernel minimality.
- Expected result: Core becomes Project-neutral.
- Trade-offs: exact Prefix values must be supplied outside Core.
- Owner and required authority: Operator; Core source authority.
- Dependencies and execution order: after taxonomy and source-relation ambiguity.
- Deterministic or semantic verification: changing Project Prefix changes valid identifiers without changing Core Atoms.
- Recommendation: `preferred`.
- State: `PROPOSED`.

#### FX-005 - Select one canonical ninth Content Role label

- Exact change: Operator selects `Ops` or `Operations`; all Core exact-value authorities use the selected label while retaining `O`.
- Addressed issue IDs: `DC-005`.
- Relationship: `required prerequisite`.
- Independent fix confidence and evidence basis: `100%` that one label is required; neither label is evidence-preferred.
- Expected result: registries and selectors agree.
- Trade-offs: the losing label may require a migration alias.
- Owner and required authority: Operator; Core vocabulary authority.
- Dependencies and execution order: complete before recompilation.
- Deterministic or semantic verification: one canonical label appears in every active Core exact-value use.
- Recommendation: `preferred`.
- State: `PROPOSED`.

#### FX-006 - Normalize active Core Atoms against their Claim boundary

- Exact change: split `CAPRMEDIO-META-REQU-116`, delete its duplicate projection, then repair only confirmed violations from a complete active-Core Claim evaluation.
- Addressed issue IDs: `DC-006`.
- Relationship: `complementary`.
- Independent fix confidence and evidence basis: `99%`, a direct counterexample exists.
- Expected result: Core becomes valid input to its own Claim authority.
- Trade-offs: Atom count and replacement history increase.
- Owner and required authority: Operator authorizes; assigned AI Agent may edit.
- Dependencies and execution order: after `FX-003`.
- Deterministic or semantic verification: every active Core Atom has one independently replaceable Claim and one Effective Claim Scope.
- Recommendation: `preferred`.
- State: `PROPOSED`.

#### FX-007 - Clarify Entity independence from graph materialization

- Exact change: either define Entity independently of graph generation or narrow and rename it to an explicitly representation-bound `CAPRMEDIO Entity`.
- Addressed issue IDs: `DC-007`.
- Relationship: `alternative`.
- Independent fix confidence and evidence basis: `94%`, risk is supported but intended domain is missing.
- Expected result: Entity identity has an explicit stable boundary.
- Trade-offs: broader definition needs admission rules; narrower definition adds vocabulary.
- Owner and required authority: Operator; Core ontology authority.
- Dependencies and execution order: only after an explicit domain decision.
- Deterministic or semantic verification: Entity identity remains stable through graph generation/deletion, or the representation-bound exception is explicit.
- Recommendation: `acceptable`.
- State: `PROPOSED`.

# Unresolved evidence gaps

#### GAP-001 - Exhaustiveness of the active-Core conflict set

- Linked issue or fix IDs: `DC-001..DC-007`, `FX-001..FX-007`.
- Best current answer: seven findings are sufficient for challenge but not exhaustive.
- Missing evidence: deterministic all-pairs conflict, duplicate, and implication analysis across all 619 active Core Atoms.
- Consequence: additional conflicts may appear later.
- Exact next evidence or action: in a new authorized invocation, freeze the frontier and run a complete Core-only semantic scan.

#### GAP-002 - Runtime behavior of validators and graph generation

- Linked issue or fix IDs: `DC-001`, `DC-002`, `DC-003`, `DC-006`; `FX-001`, `FX-002`, `FX-003`, `FX-006`.
- Best current answer: authority text is inconsistent without implementation evidence.
- Missing evidence: before-state validator and graph-generation outputs.
- Consequence: no measured before/after quality claim is possible.
- Exact next evidence or action: in a new authorized invocation, establish a rerunnable Core-only evaluation frame and capture baseline outputs.

#### GAP-003 - Downstream compatibility outside scope

- Linked issue or fix IDs: `FX-002`, `FX-003`, `FX-004`, `FX-005`.
- Best current answer: plausible downstream effects remain intentionally unmeasured.
- Missing evidence: compatibility checks against all excluded targets.
- Consequence: a locally coherent repair may break consumers.
- Exact next evidence or action: after an authorized Core target passes, open a separately authorized downstream compatibility step.

#### GAP-004 - Canonical ninth Content Role label

- Linked issue or fix IDs: `DC-005`, `FX-005`.
- Best current answer: exactly one of `Ops` or `Operations` must be canonical; `O` remains stable.
- Missing evidence: Operator label choice and alias policy.
- Consequence: `FX-005` is not deterministic.
- Exact next evidence or action: obtain a neutral Operator choice before accepting `DC-005` for mutation.

#### GAP-005 - Entity candidate domain

- Linked issue or fix IDs: `DC-007`, `FX-007`.
- Best current answer: current wording is risky under a general Entity reading and potentially sound under an explicitly representation-bound reading.
- Missing evidence: owner-approved inclusion/exclusion test.
- Consequence: immediate change could broaden or narrow the ontology incorrectly.
- Exact next evidence or action: obtain an Operator domain decision before accepting `FX-007`.

# Skills used

- `$fpf design challenge`

`$fpf quality improve` stopped at its authorization gate before native quality analysis and is therefore not listed as an executed analytical skill.

### FPF sources consulted (6 read; 6 used)

- **used** - `A.5 - Open-Ended Kernel & Extension Layering`.
- **used** - `A.11 - Ontological Parsimony`.
- **used** - `A.1.1 - Bounded Model-Use Structure and DDD Bounded-Context Recovery`.
- **used** - `A.6.5 - Relation-Declaration Slot Discipline`.
- **used** - `C.3.1 - U.Kind and U.SubkindOf Core`.
- **used** - `C.3.2 - Kind Intent, Membership Judgment, and Extension`.
