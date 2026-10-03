---
subject_scopes:
  - authority
  - requirement-topology
  - scope-topology
  - carrier-format
version: 8
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  analysis_of:
    - CAPRMEDIO-REQU-001--ordered-realization-topology
    - CAPRMEDIO-REQU-054--acyclic-layers-with-ops-feedback
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
    - CAPRMEDIO-REQU-056--require-falsifiable-claims-and-stop-conditions
    - CA-M-002-PRINCIPLE-METHOD--dry_dont-repeat-yourself
    - CAPRMEDIO-REQU-057--own-immediate-child-scopes-and-contracts
    - CAPRMEDIO-REQU-058--define-meta-layer-scope-and-contracts
    - CAPRMEDIO-REQU-059--define-gov-layer-scope-and-contracts
    - CAPRMEDIO-REQU-060--define-spec-layer-scope-and-contracts
    - CAPRMEDIO-REQU-061--define-implementation-layer-scope-and-contracts
    - CAPRMEDIO-REQU-062--define-delivery-layer-scope-and-contracts
    - CAPRMEDIO-REQU-063--define-ops-layer-scope-and-contracts
    - CA-D-003-PRINCIPLE-DELIVERY--provide-one-project-graph-as-the-operating-model
    - CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary
    - CAPRMEDIO-REQU-065--natural-operator-surface
    - CAPRMEDIO-REQU-006--minimal-default-project-model
    - CAPRMEDIO-REQU-007--full-minimal-traceability
    - CAPRMEDIO-REQU-008--define-project-scope-boundary
    - CA-R-831-REQUIREMENT--add-reusable-capabilities-through-extensions
    - CA-R-832-REQUIREMENT--select-optional-capabilities-through-configuration
    - CA-R-1056
    - CAPRMEDIO-REQU-066--discipline-independent-core
    - CA-D-001-PRINCIPLE-DELIVERY--provide-replaceable-technical-realizations
    - CAPRMEDIO-REQU-067--default-to-software-application-development
    - CAPRMEDIO-REQU-068--support-portable-execution-platforms
    - CAPRMEDIO-REQU-069--support-any-operator-language
    - CAPRMEDIO-REQU-070--support-any-implementation-language
    - CAPRMEDIO-REQU-071--keep-llm-operation-provider-neutral
    - CAPRMEDIO-META-REQU-189--work-area-scope
    - CAPRMEDIO-META-REQU-082--single-owner-rule-placement
    - CA-R-1051
    - CAPRMEDIO-META-REQU-088--meta-eligibility-rule
    - CAPRMEDIO-META-REQU-090--propagate-atomic-revision-impact-through-lineage
    - CAPRMEDIO-META-REQU-091--normative-atoms-are-the-caprmedio-specification
    - CAPRMEDIO-META-REQU-092--authority-evaluation-and-ops-remain-distinct
    - CAPRMEDIO-META-REQU-093--analysis-and-ops-fact-boundary
    - CAPRMEDIO-META-REQU-096--propagate-caprmedio-change-forward
    - CAPRMEDIO-META-REQU-098--scope-path-does-not-change-semantic-coordinates
    - CAPRMEDIO-META-REQU-261--propagate-structural-scope-through-realization
    - CAPRMEDIO-META-REQU-106--keep-meta-and-gov-implementation-neutral
    - CAPRMEDIO-META-REQU-107--bind-traceability-to-exact-claims-and-revisions
    - CAPRMEDIO-META-REQU-108--evolve-authority-through-governed-history
    - CAPRMEDIO-META-REQU-110--bind-governed-transactions-to-stable-artifact-revisions
    - CAPRMEDIO-META-REQU-269--bound-git-authority-to-repository-provenance
    - CAPRMEDIO-META-REQU-111--nine-content-roles-with-plan
    - CAPRMEDIO-META-REQU-271--caprmedio-framework-identity
    - CAPRMEDIO-META-REQU-113--coordinate-artifacts-without-an-81-type-bijection
    - CAPRMEDIO-META-REQU-114--preserve-content-role-boundaries-through-caprmedio-loop
    - CAPRMEDIO-META-REQU-273--use-canonical-carrier-address-as-authority
    - CAPRMEDIO-META-REQU-118--let-the-dependent-atom-own-the-relation
    - CAPRMEDIO-META-REQU-124--make-requirement-the-only-universally-mandatory-atom
    - CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections
    - CAPRMEDIO-META-REQU-127--define-three-governance-loci
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
    - CAPRMEDIO-META-REQU-129--separate-authority-applicability-and-currentness
    - CAPRMEDIO-META-REQU-130--define-atom-admission-and-lifecycle
    - CAPRMEDIO-META-REQU-135--write-context-complete-minimal-atom-prose
    - CAPRMEDIO-META-REQU-281--share-canonical-features-across-spec-and-implementation
    - CAPRMEDIO-META-REQU-151--admit-only-materially-distinct-framework-constructs
    - CAPRMEDIO-META-REQU-152--preserve-strict-semantic-distinctions
    - CAPRMEDIO-META-REQU-153--preserve-bounded-meaning-across-structural-scales
    - CAPRMEDIO-META-REQU-154--semantic-irreducibility
    - CAPRMEDIO-META-REQU-155--classify-rmed-atoms-by-applicability-tier
    - CAPRMEDIO-META-REQU-156--govern-tier-preserving-requirement-relations
    - CAPRMEDIO-META-REQU-157--narrowest-common-scope-ownership
    - CA-R-1054
---
# Project, META, and GOV Core authority audit

## Conclusion

The proposition that the current Project Requirements and META/GOV Core Requirements are fully coherent, correctly placed, complete, and relation-clean is unsupported. The model is substantially improved and the reviewed relation graph is mechanically strong, but several current Requirements cross their declared authority boundaries, concrete Feature topology is owned by the wrong layers, five Project Cores are behavior Standards in disguise, and the current carriers have not completed their own GOV migration.

The correct repair is to move, split, or retier the affected authority and then repair its direct relations. Creating nominal child Requirements merely to satisfy graph shape would add ceremony without resolving the semantic ownership error.

## Reviewed boundary

This Analysis covers the live working tree at repository HEAD `56508635d2fb88d71b637940e56d6e07e04ef2bf`, including uncommitted Project, META, and GOV changes present during the review. It reviews 28 active Project Requirements, 37 active META Requirements currently classified as Core, the sole active GOV Core, and downstream Standards only when a reviewed move or retiering would affect them.

The review excludes full SPEC, IMPLEMENTATION, DELIVERY, and OPS correctness; runtime behavior; generated Projections; tests; evaluations; release readiness; and implementation of the proposed repairs. No tests or evaluations were run.

The authority boundary used for the review is:

- PROJECT owns project Principles, constitutional Cores governing the complete Layer system, concrete Layer scopes, and Contracts between Layers.
- META owns canonical meanings, vocabulary, semantic axes and distinctions, role and form meanings, applicability tiers, relation meanings, structural interpretation, and construct admission.
- GOV owns carrier identity, naming, placement, frontmatter, provenance, relation encoding, lifecycle mechanics, catalogs, and structural validation.
- SPEC owns applicable Requirement, Method, Evaluation, and Delivery authority defining what and how the project must realize.
- IMPLEMENTATION owns the realized project artifacts.
- Every structural owner defines its immediate child scopes and the Contracts between those children; PROJECT owns Layers and inter-Layer Contracts, while each Layer owns its Features and inter-Feature Contracts.

## Bounded audit verdict

| Check | Result |
|---|---|
| Every reviewed claim has one clear owner | Fail |
| Project, META, and GOV boundaries are respected | Fail |
| Reviewed `child_of` endpoints resolve to active Requirements | Pass |
| Reviewed tier edges are legal under current authority | Pass |
| No reviewed Principle or Core is an orphan | Fail |
| Concrete Feature definitions are owned by their Layers | Fail |
| Inter-Layer Feature correspondence is owned by PROJECT | Fail |
| Carrier metadata follows current GOV authority | Fail |
| No active Requirement points to an archived parent | Fail across the wider active graph |
| Every reviewed claim has an explicit disposition | Pass |

## Relation evidence

The 66 reviewed Requirements contain 70 active `child_of` relations and 20 `replacement_of` relations. All 70 reviewed `child_of` targets resolve to active Requirements, all reviewed tier combinations are legal, all 20 reviewed replacements point to archived carriers, no reviewed direct relation redundantly repeats a transitive ancestor, and all reviewed targets use full filename stems.

| Relation class | Count |
|---|---:|
| Project Core to Project Principle | 11 |
| Project Standard to Project Core | 9 |
| META Core to Project Principle | 46 |
| META Core to Project Core | 2 |
| GOV Core to META Core | 2 |

Five current Project Cores have no active child: R199, R200, R201, R202, and R203. The orphan condition is a symptom of incorrect owner and tier classification. These five claims are SPEC behavior Standards, not constitutional Project Cores.

## Project Requirement dispositions

| Requirement | Current tier | Disposition |
|---|---|---|
| R065 — Ordered realization topology | Core | Keep. It constitutionally defines the complete Layer topology. |
| R096 — Acyclic Layers with Ops feedback | Standard | Keep. It is the concrete dependency rule for R065. |
| R114 — MECE | Principle | Keep. |
| R122 — Falsifiable claims and stop conditions | Principle | Keep. |
| R140 — DRY | Principle | Keep. |
| R174 — Immediate child scopes and Contracts | Core | Keep. It owns recursive structural decomposition. |
| R175 — META Layer scope and Contracts | Standard | Keep owner and tier. |
| R176 — GOV Layer scope and Contracts | Standard | Keep owner and tier. |
| R177 — SPEC Layer scope and Contracts | Standard | Keep owner and tier. |
| R178 — IMPLEMENTATION Layer scope and Contracts | Standard | Keep owner and tier. |
| R179 — DELIVERY Layer scope and Contracts | Standard | Keep owner and tier. |
| R180 — OPS Layer scope and Contracts | Standard | Keep owner and tier. |
| R182 — Graph is the operating model | Principle | Keep. |
| R183 — Necessary complexity only | Principle | Keep. |
| R184 — Natural operator surface | Principle | Keep. |
| R185 — Minimal default Project model | Core | Keep. |
| R186 — Full minimal traceability | Core | Keep. |
| R187 — Project scope boundary | Standard | Keep. |
| R188 — Extensibility | Principle | Keep. |
| R189 — Configurability | Principle | Keep. |
| R190 — Minimum sufficient guidance | Principle | Keep. |
| R197 — Discipline-independent core | Principle | Keep the meaning but replace the Atom with a summary such as `preserve-discipline-independent-semantics`; `Core` is now a canonical applicability-tier term and is misleading in a Principle title. |
| R198 — Replaceable substrates | Principle | Keep. |
| R199 — Default software-application development | Core | Move to SPEC and demote to Standard under a discipline-Profile Core. |
| R200 — Portable execution platforms | Core | Move to SPEC and demote to Standard under a substrate-neutral behavior Core. |
| R201 — Any operator language | Core | Move to SPEC and demote to Standard under the substrate-neutral behavior Core. |
| R202 — Any Implementation language | Core | Move to SPEC and demote to Standard under the substrate-neutral behavior Core. |
| R203 — LLM-provider neutrality | Core | Move to SPEC and demote to Standard under the substrate-neutral behavior Core. |

R199 through R203 must move because Project authority explicitly excludes project behavior assigned to SPEC, while SPEC explicitly owns the normative authority defining what and how the project must realize.

The minimum honest hierarchy is two genuine SPEC Cores: one governing discipline Profile applicability and one governing substrate-neutral framework behavior. R199 becomes a Standard under the first; R200 through R203 become Standards under the second. Five invented child Standards below five retained Project Cores would only preserve the original classification mistake.

## META Core dispositions

| Requirement | Disposition |
|---|---|
| META-011 — Work Area scope | META ownership is correct; Core tier remains an open question. |
| META-026 — Single-owner placement | Keep Core. |
| META-053 — Active authority versus preserved history | Keep Core. |
| META-066 — META eligibility | Keep Core. |
| META-077 — Revision impact through lineage | Keep Core. |
| META-090 — Normative Atoms form the Specification | Keep Core. |
| META-091 — Authority, Evaluation, and Ops distinctions | Keep Core. |
| META-092 — Analysis/Ops fact boundary | Demote to Standard because it governs a proper Content-role subsegment. |
| META-095 — Forward change propagation | Keep Core. |
| META-100 — Scope path is structural | Keep Core. |
| META-104 — Structural scope through realization | Keep Core but replace or materially narrow its claim so corresponding Layer-owned Feature scopes do not share one structural identity. |
| META-118 — META/GOV implementation neutrality | Keep Core. |
| META-121 — Exact claim and revision traceability | Keep Core. |
| META-123 — Governed historical evolution | Keep Core. |
| META-128 — Stable revision-bound transactions | Keep Core. |
| META-129 — Git provenance authority | Keep Core under META-066's explicit operator-mandated constitutional-substrate exception. |
| META-131 — Nine Content roles | Keep Core. |
| META-132 — CAPRMEDIO identity | Keep Core. |
| META-134 — Three-axis coordinate without an 81-Type bijection | Keep Core. |
| META-135 — Content-role boundaries | Keep Core. |
| META-139 — Canonical carrier address authority | Move to GOV and demote to Standard. |
| META-145 — Dependent Atom owns the relation | Keep Core. |
| META-152 — Requirement is the only mandatory Atom | Keep Core. |
| META-154 — Atom, Journal, and Projection forms | Keep Core. |
| META-156 — Governance loci | Keep Core. |
| META-157 — Artifact, carrier, and revision distinction | Keep Core. |
| META-158 — Authority, applicability, and currentness | Keep Core. |
| META-159 — Atom lifecycle meanings | Keep Core but remove physical folder and transition mechanics. |
| META-166 — Minimal Atom prose | Keep Core. |
| META-172 — Shared SPEC and IMPLEMENTATION Features | Archive and replace with correctly owned Project, SPEC, and IMPLEMENTATION Standards. |
| META-190 — Material construct admission | Keep Core. |
| META-191 — Strict semantic distinctions | Keep Core. |
| META-192 — Meaning across structural scales | Keep Core. |
| META-193 — Semantic irreducibility | Keep Core. |
| META-194 — Applicability tiers | Keep Core. |
| META-195 — Tier-preserving relations | Keep Core. |
| META-196 — Narrowest common scope | Keep Core but extract its embedded Rationale into an Analysis Rationale Atom. |

## Structural-scope conflict

META-104 currently says a structural scope is registered once and reused unchanged by every realization Layer. That conflicts with the newer Layer-owned Feature model. A SPEC/TOOLS Feature scope and an IMPLEMENTATION/TOOLS Feature scope have distinct Layer-qualified structural identities. They may correspond to the same subject or capability, but correspondence does not make them one reused structural scope.

META-104 remains a Core, but its claim must be replaced or narrowed to distinguish a stable shared referent from the distinct structural scopes that govern that referent in separate Layers. Their mapping belongs in an explicit Project-owned inter-Layer Contract.

META-172 currently defines the SPEC Feature partition, defines the IMPLEMENTATION Feature partition, and defines the correspondence between the two. These meanings have three owners:

| Meaning | Owner | Tier |
|---|---|---|
| SPEC Feature partition | SPEC | Standard |
| IMPLEMENTATION Feature partition | IMPLEMENTATION | Standard |
| SPEC to IMPLEMENTATION Feature correspondence | PROJECT | Standard Contract |

GOV may encode the accepted scopes in numbered directories, but physical layout cannot establish their semantic identities.

META-143 must be split during the same repair. The rule that each Feature belongs to exactly one Layer is META structural meaning. The rule that Layer and Feature directories are physical siblings with numeric addresses is GOV carrier mechanics.

## Carrier-governance boundary

META-139 governs directories, filenames, extensions, derived frontmatter, resolver behavior, and validation failure. Those are GOV carrier mechanics. Its successor belongs in GOV as a Standard under GOV-181.

META-165 and META-171 must move with it. They should become sibling GOV Standards under GOV-181 rather than Standard children of the moved META-139 successor. Any necessary semantic connection between the Standards should use a precise non-tier relation.

META-159 correctly owns the semantic distinction among candidate, draft, accepted, admitted, committed, active, done, and archived. Literal placement under `drafts/`, `done/`, and `archive/`, plus concrete transition procedures, belongs to GOV.

## GOV Core disposition

GOV-181 remains the sole GOV Core. It correctly governs the complete GOV responsibility: every governed carrier must represent accepted authority deterministically and human-readably without becoming another semantic owner.

GOV-181 should add a direct relation to Project Principle R184 because faithful human-readable carrier representation directly realizes the Natural Operator Surface. Its existing META-191 and META-193 parents remain valid, and R140 remains reachable through META-193 rather than being duplicated as a direct parent.

No additional GOV Core is necessary. Concrete carrier rules remain Standards under GOV-181.

## Missing authority

The minimum missing authority is:

1. A SPEC Core for discipline Profile applicability, with R199 as its Standard default.
2. A SPEC Core for substrate-neutral framework behavior, with R200 through R203 as Standards.
3. A SPEC Core governing the complete SPEC Feature topology.
4. An IMPLEMENTATION Core governing the complete IMPLEMENTATION Feature topology.
5. A Project Standard Contract mapping distinct SPEC and IMPLEMENTATION Feature scopes.
6. SPEC Standards defining the METHODOLOGY, TOOLS, SKILLS, PROFILES, ADAPTERS, EVALUATION, and DOCUMENTATION Feature scopes.
7. IMPLEMENTATION Standards defining the corresponding realization Feature scopes.
8. A META Standard defining Extension identity, version boundary, extension point, compatibility obligation, and the prohibition on redefining canonical authority.
9. A META Standard defining Configuration selection, composition, parameterization, disablement, and precedence without changing capability meanings.
10. A SPEC Skills or Methodology Core applying Minimum Sufficient Guidance to prompts, Skills, and model, host, task, risk, and Evaluation calibration.

These are materially distinct missing claims. They are not nominal graph filler.

## Required relation repairs

1. Move R199 under the new SPEC discipline-Profile Core.
2. Move R200 through R203 under the new SPEC substrate-neutral behavior Core.
3. Make the new SPEC Cores direct children of R197 and R198 respectively.
4. Move the META-139 successor under GOV-181.
5. Move META-165 and META-171 to GOV as sibling Standards under GOV-181.
6. Demote META-092 under META-091.
7. Remove META-093's Standard-to-Standard `child_of` relation to META-092; META-091 is already its valid Core parent.
8. If META-011 becomes Standard, reparent META-057 and CONTRACT-META-001 to appropriate Cores or precise non-tier relations.
9. Split and reparent META-143 when META-172 is replaced.
10. Add the direct R184 parent to GOV-181.

The wider active Requirement graph also contains three active references to archived Requirements:

- REQUIREMENT-003 self-hosted governance loci points to archived META-018.
- TOOL-024 project NDJSON logs to TOON points to archived GOV-099.
- SKILL-011 shared Skill runtime points to archived SKILL-010.

Each dependent must point to the exact active successor, be replaced if its meaning changed, or be archived if obsolete. A successor must not be inferred from title similarity alone.

## Carrier-conformance failures

Within the 66 reviewed carriers:

- 22 still use obsolete singular `subject_scope` rather than the universal `subject_scopes` list.
- 36 repeat a derived `scope_path`.
- 57 repeat derived `artifact_type` and/or `artifact_id` metadata.
- 25 H1 titles repeat an Artifact Type label such as `Requirement`.
- 26 contain `Primary claim` sections that commonly restate an already complete body.
- hard-wrapped prose remains widespread despite the unwrapped-paragraph rule.
- META-196 embeds a Rationale that belongs in a separate Analysis Rationale Atom.

These failures do not invalidate every underlying semantic claim, but they mean the current carriers do not satisfy their own active GOV authority.

## Repair order

1. Replace or narrow META-104.
2. Replace META-172 with the Project, SPEC, and IMPLEMENTATION authority split.
3. Split META-143 into META meaning and GOV mechanics.
4. Add the SPEC and IMPLEMENTATION Feature-topology Cores.
5. Move R199 through R203 into SPEC under two genuine Cores.
6. Move META-139, META-165, and META-171 into GOV.
7. Narrow META-159 to lifecycle meaning.
8. Demote META-092 and repair META-093 ancestry.
9. Resolve META-011's tier and repair its dependents.
10. Add Extension and Configuration Standards.
11. Add the SPEC minimum-guidance Core.
12. Resolve the three active-to-archived references.
13. Run one deterministic carrier migration for frontmatter, H1 titles, duplicated claims, Rationale separation, and paragraph wrapping.
14. Regenerate relation and scope Projections only after semantic authority is stable.

This order avoids temporary backward dependencies and avoids migrating the same carriers twice.

## Open questions

### META-011 tier

The recommended classification is Standard under META-100 because Work Area is one optional structural-scope kind. It may remain Core only if CAPRMEDIO intends Work Area to be a complete reusable structural scope rather than one scope-kind subsegment.

### Layer-boundary atomicity

R175 through R180 currently combine Layer responsibility, accepted inputs, produced outputs, and exclusions. The recommendation is to retain each as one Layer-boundary Atom until its scope definition and interface Contract need independent replacement, applicability, or lifecycle.

### Number of SPEC portability Cores

The recommended count is two: discipline Profile applicability and substrate-neutral framework behavior. One combined Core would mix discipline adaptation with portability; five separate Cores would reproduce the current unnecessary fragmentation.

## FPF basis

The FPF source reviewed at `48c84d84f1074d9d4c73338bcf604fc909249000` contributed four bounded lenses:

- A.11 Ontological Parsimony: use existing composition and correct ownership before admitting new durable constructs; admit a construct only when composition loses a reviewable action-facing distinction.
- E.5.3 Unidirectional Dependency: keep the dependency graph acyclic and preserve declared direction.
- A.6.5 Relation-Declaration Slot Discipline: identify the direct relation and its exact participants before encoding reusable relation structure.
- A.1.1 Bounded Model-Use Structure: recover the exact governed owner and object instead of treating a container, carrier, folder, or representation as semantic authority.

A.22 Structure and Structural Views and F.6 RoleAssignment and Performed-Work Attribution were screened but were not needed for the conclusions.

This is an FPF-informed CAPRMEDIO analysis, not a claim that CAPRMEDIO conforms to or implements FPF.

## Stop condition

Every reviewed Project Requirement and META/GOV Core has a disposition; semantic blockers, mechanical failures, missing authority, relation repairs, uncertainty, and exclusions are explicit. The Analysis stops before mutation, test, evaluation, or release claims.
