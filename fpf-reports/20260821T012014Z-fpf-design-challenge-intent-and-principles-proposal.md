## Task, scope, and boundaries

Challenge the current CAPRMEDIO Intent and active Project Principles as a proposed design, applying the Method, Evaluation, Delivery, and Ops Principles to the whole set and testing individual claims, pairwise boundaries, and set-level coherence. :codex-annotation{index="1"}

Inspected target:

- `.caprmedio/CA-INTENT.md`.
- The 19 active Project Principle carriers under Plan, Requirement, Method, Evaluation, Delivery, and Ops.

Excluded from the target:

- all Project Cores and Standards;
- all Bootstrap Seed authority;
- all implementation, realization, release, field, and operational evidence;
- archived and draft Principles;
- Principle-set completeness beyond the current proposal.

Proposal boundary: these carriers describe a proposed framework. Their existence demonstrates neither acceptance nor realization. The project is understood to be more than 95% unimplemented and to lack more than 70% of its intended Atoms. Those facts therefore cannot be used as conformance failures in this challenge.

Resolved source boundary: the live Intent and 19 active Principle carriers are the sole project-side semantic source for this review. FPF supplies challenge lenses, not CAPRMEDIO authority.

Decision boundary: the findings identify proposal concerns and repair options. They do not adopt, reject, approve, or implement a design.

Overall result: **concern**. The proposal has a coherent center, but eight high-confidence semantic defects should be repaired before this Principle edition is treated as stable.

Saved report: `fpf-reports/20260821T012014Z-fpf-design-challenge-intent-and-principles-proposal.md`

## High-confidence results (>=95%)

### Strengths

1. **Proposal and realization remain distinguishable — no concern found within inspected scope (100%).** The Principles use normative future-facing language, which is appropriate in a proposal. No implementation or conformance conclusion follows from their carriers. This matches the FPF distinction among a proposed framework organization, a settled architecture, its publication carrier, and performed work.

2. **Intent expansion is present at the aggregate level — no concern found within inspected scope (97%).** The lifecycle outcome is expanded by R-819; Operator control by R-004 and R-827; AI assistance under bounded authority by P-032 through P-034 and R-846; and Operator-priority resource trade-offs by R-815. The Intent need not be divided into statement-level Atoms to establish this aggregate relation.

3. **The Actor authority split is directionally sound — no concern found within inspected scope (98%).** P-033 gives original authority to human Operators; P-034 denies original authority to AI Agents; R-846 makes delegation inspectable and revocable. This preserves Actor, authority, and delegated action as distinct concepts rather than treating a Plan or Agent capability as performed work.

4. **The Method Principles are mostly distinct — no concern found within inspected scope (98%).** M-001 governs partition quality, M-002 semantic ownership, M-003 information exposure, M-005 complexity admission, and M-006 discipline-independent shared meaning. Their named primary claims are independently changeable and do not inherently duplicate one another.

5. **The proposal does not claim Principle-set completeness — no concern found within inspected scope (100%).** MECE can be checked only against a declared universe. No sufficient criterion for discovering every necessary Principle exists here, and none should be inferred. The current set can be checked for internal MECE, DRY, and cross-Principle alignment without claiming that no missing Principle exists.

### FPF Challenge Findings

1. **R-004 and R-827 are not human-text MECE — concern (100%).** R-004 governs the CAPRMEDIO instance. R-827's human statement governs “every governed part of the project,” which ordinarily includes that instance, while its formal statement silently narrows `P(s)` to project parts outside the instance. The pair is overlapping in human language and disjoint only in the formal layer.

   Recommended repair: keep two Principles, but make their human scopes explicitly disjoint. R-004 owns the CAPRMEDIO instance; R-827 owns the governed project outside that instance. Define `control` once below the Principle tier so it means authority over admissible change and recovery, not arbitrary mutation of immutable records.

2. **R-004 does not fully formalize its preservation claim — concern (98%).** Its second predicate requires the ability to change the project only after every admissible instance transition. It never directly asserts that the current state already has that ability. A transition invariant cannot establish its own initial condition.

   Recommended repair: assert the capability for every governed state, then separately assert its preservation across every admissible instance transition.

3. **R-846 gives every Operator unrestricted delegation administration — concern (100%).** The human statement says Operators can manage delegations, but the formal statement quantifies `forall o in O, forall d in D` and gives each Operator power over every delegation. That can contradict P-033's per-Operator declared-authority boundary and the collective-authority wording in R-004 and R-827.

   Recommended repair: constrain delegation creation and administration by current Operator authority, or assign management to the authorized Operator set rather than every Operator individually.

4. **R-819 silently strengthens collective capability into universal individual capability — concern (98%).** “Enable declared Operators” can describe the Operator group, while the formal statement requires every individual Operator to obtain the full create-deliver-run-maintain lifecycle for every feasible project. The Intent says “any Operator,” so the stronger meaning may be intended, but the human and formal statements must say the same thing.

   Recommended repair: either change the human statement to “enable each declared Operator,” or change the formal statement to a collective capability of the declared Operator set.

5. **M-003 assumes perfect knowledge of the minimum task context — concern (99%).** `E(t)=R(t)` requires exact identification of everything and only everything the task requires. Under uncertainty, that equality either omits safety-relevant context or makes `R(t)` expand retrospectively to whatever was exposed. It is not a stable falsification boundary.

   Recommended repair: require a minimum sufficient set and allow only explicitly justified additional exposure for uncertainty, safety, Operator request, or bounded navigation. For example, `R_min(t) subseteq E(t) subseteq R_min(t) union J(t)`, where every member of `J(t)` has a recoverable justification. Preserve the existing losslessness condition for hidden information.

6. **E-002 conflicts with M-002, M-003, M-005, and D-002 by requiring every reliance-bearing conclusion to state its full support envelope — concern (99%).** Evidence, uncertainty, and begin/change/end conditions may need independent owners and may be too large or technical for the current Operator view. Repeating them in every conclusion duplicates meaning and defeats selective exposure. FPF's human-centric working-model pattern supports recoverable assurance beneath the human-facing statement rather than mandatory inline disclosure.

   Recommended repair: replace “must state” with “must be bound to recoverable” evidence, uncertainty, and reliance conditions. Require their exposure when the current reliance decision needs them. This retains bounded reliance without forcing duplicated or indiscriminate presentation.

7. **D-002 promises an unguaranteeable cognitive result — concern (100%).** `UnderstandableBy(g,o)` claims actual understanding by every Operator whenever meaning is exposed. A framework controls representations and interaction, not a person's cognitive state. The claim has no admissible failure result when an Operator cannot understand a representation.

   Recommended repair: govern the framework-controlled result: adapt the representation to the Operator and current use, test whether it is sufficient for the governed action, and expose a comprehension gap when no sufficient representation can be produced. Human-readable meaning should remain first; formal support should remain recoverable underneath it.

8. **D-003 conflates the canonical graph representation with represented world-side operation — concern (100%).** `RepresentedIn(x,G)` is a description/model claim. `OperatedThrough(x,G)` for every governed meaning and state can be read as making code, performed work, deployments, and outcomes constituents of the graph rather than represented entities or records. FPF explicitly separates entity, description, carrier, plan, method, performed work, and result.

   Recommended repair: retain one graph Principle, but state that one typed project graph is the canonical operating representation of governed project meaning and state. Add the boundary that world-side entities, work occurrences, and results remain distinct from their graph nodes and records. Put independently changeable graph invariants—typed nodes, two structural/artifact layers, hierarchy, acyclicity, and precise relations—below it as Cores.

9. **O-003's formal statement uses authority as though it were the supported Actor — concern (100%).** The human statement says CAPRMEDIO supports the Operator. The formal statement defines `O` as “declared Operator authority” and passes `O` into `CanSupport`. Authority is not an Actor or Actor set.

   Recommended repair: let `O(s)` denote the declared Operators in state `s`, keep their authority as a separate constraint, and state that CAPRMEDIO can support those Operators in producing and evaluating a proposal. Preserve the proposal-versus-performed-improvement boundary: support or selection does not prove that improvement work occurred or that an outcome improved.

10. **Human and formal statements are not yet governed as equivalent representations — concern (99%).** R-004, R-819, R-827, and O-003 already demonstrate narrowing, strengthening, or category change between the two sections. Human-first publication is a strength only when the formal statement does not silently change its meaning.

   Recommended repair: add a proposal-level acceptance rule for every Principle: the human statement owns the readable claim; the formal statement may sharpen it but must be extensionally equivalent within the declared vocabulary. If equivalence cannot be established, keep the formal statement absent or explicitly mark the unresolved difference.

### Per-Principle disposition

| Principle | Result | Confidence | Main reason |
| --- | --- | ---: | --- |
| P-032 | no concern found within inspected scope | 97% | Closed Actor taxonomy is coherent if non-Actor tools remain attributable to an Actor. |
| P-033 | no concern found within inspected scope | 96% | Original human authority and scoped permission are distinct. |
| P-034 | no concern found within inspected scope | 96% | No original AI authority and bounded delegation are coherent; authorization scope remains an open question below. |
| R-004 | concern | 100% | Human overlap with R-827 and incomplete preservation formalization. |
| R-815 | no concern found within inspected scope | 96% | One effective Operator priority order governs admissible trade-offs without claiming the priorities themselves are objective value. |
| R-819 | concern | 98% | Human collective wording and formal individual universal differ. |
| R-827 | concern | 100% | Human/formal scope mismatch and undefined control boundary. |
| R-846 | concern | 100% | Formal quantifiers overgrant delegation administration. |
| M-001 | no concern found within inspected scope | 99% | Correctly bounds MECE to a declared universe and abstraction level. |
| M-002 | no concern found within inspected scope | 99% | One canonical semantic owner with explicit derived/adapted uses. |
| M-003 | concern | 99% | Exact exposure equality presumes an unavailable perfect task-information oracle. |
| M-005 | no concern found within inspected scope | 97% | A distinct necessity gate for mechanisms. |
| M-006 | no concern found within inspected scope | 98% | Shared canonical meaning remains invariant while discipline-specific adaptations can live elsewhere. |
| E-001 | no concern found within inspected scope | 99% | Applies to accepted Requirements when used; it does not claim the proposed Principles are already accepted or checked. |
| E-002 | concern | 99% | Inline statement requirement duplicates and overexposes assurance material. |
| D-001 | no concern found within inspected scope | 96% | Specification-preserving replacement is a distinct Delivery invariant; exception policy remains open below. |
| D-002 | concern | 100% | Guarantees a human cognitive state rather than a framework-controlled representation and check. |
| D-003 | concern | 100% | Representation and world-side operation are conflated. |
| O-003 | concern | 100% | Formal statement confuses Operator authority with the supported Actor. |

### Recommended repair order returned to project authority

1. Repair human/formal equivalence in R-004, R-819, R-827, R-846, and O-003.
2. Make R-004 and R-827 explicitly disjoint while preserving both instance control and project control.
3. Replace M-003's exact-exposure oracle with minimum sufficient exposure plus justified bounded overhead.
4. Change E-002 from repeated inline statements to recoverable bindings with selective exposure.
5. Rewrite D-002 around adaptable representation, comprehension testing, and an explicit gap result.
6. Narrow D-003 to one canonical typed graph representation and move graph invariants below the Principle tier.
7. Re-run the same bounded challenge on the revised Intent and Principles before designing their Cores. Do not use this challenge as evidence of implementation or operational conformance.

## Open questions (confidence <95%)

1. **May an AI Agent authorize another Actor's governed action, including subdelegation? — 93%.** P-034 deliberately permits AI Agents to “perform or authorize,” while R-846 governs Operator management of delegations. If AI authorization excludes creating or widening delegation, define that boundary. If delegated subauthorization is intended, require the complete downstream authority chain to remain bounded and revocable.

2. **Must R-815's effective priority order produce one unique winner? — 92%.** The `Max` operator may return several tied alternatives. This is coherent if later decision authority handles ties; it is incomplete if the Principle intends deterministic selection.

3. **Should D-001 admit an Operator-accepted irreducibility exception? — 94%.** Universal technical replaceability may be intentionally aspirational, or it may wrongly exclude projects constrained by unique external infrastructure, regulation, or physical assets. The current scoped proposal does not decide this.

4. **How are deterministic non-AI tools attributed under P-032? — 93%.** The two-Actor taxonomy is coherent if tools are mechanisms used by an Operator or AI Agent and their governed actions are attributed to that Actor. It is not exhaustive if a deterministic autonomous service can itself perform a governed action as an Actor.

5. **Who establishes each Operator's “declared authority” in P-033? — 92%.** “Original authority” and “declared authority” can coexist if the latter is the project-visible scope of the former. The scoped proposal does not state whether Operators declare their own boundaries collectively, whether one Operator can constrain another, or whether an external authority can do so.

### Unchecked claims and insufficient basis

- Principle-set completeness: **insufficient basis**. The proposal neither supplies nor needs a sufficient completeness criterion.
- Realization of any Principle: **insufficient basis**. Implementation and operational evidence were explicitly excluded and are largely absent.
- Adequacy of lower-tier Cores, Standards, Evaluations, and acceptance procedures: **insufficient basis**. They were outside the target.
- Current project conformance: **insufficient basis**. A design challenge of a proposal cannot establish it.

## Skills used

1. `fpf-design-challenge` — challenged the proposed Intent and Principles without treating their carriers as realized work.

#### FPF sources consulted (7 read; 7 used)

- `00-readme/02_Practical-Use Cards.md` — used for result-versus-plan and proposal-versus-realization boundaries.
- `E_The FPF Constitution and Authoring Guides/03_04_FPF Ecosystem Family Architecture/03_DPF_Domain Principle Framework Authoring and Publication-or-Access Carrier Assembly/00_E.04.DPF - Domain Principle Framework Authoring and Publication-or-Access Carrier Assembly.md` — used for proposal, framework-edition, carrier, and authoring-stage distinctions.
- `A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/00_A.06 - Signature Stack & Boundary Discipline.md` — used for atomic claim ownership, boundary classification, and entity/description/carrier separation.
- `A_Kernel Architecture Cluster/15_Role-Method-Work Alignment/00_A.15 - Role-Method-Work Alignment.md` — used for Actor, authority, plan, method, performed work, and result distinctions.
- `E_The FPF Constitution and Authoring Guides/12_13_Pragmatic Utility and Value Alignment/00_E.13 - Pragmatic Utility and Value Alignment.md` — used for Operator-priority trade-offs and proxy-versus-value discipline.
- `E_The FPF Constitution and Authoring Guides/13_14_Human-Centric Working-Model/00_E.14 - Human-Centric Working-Model.md` — used for human-first meaning, recoverable formal support, and non-leaking assurance machinery.
- `E_The FPF Constitution and Authoring Guides/22_23_Quality Improvement Loop Method/00_E.23 - Quality Improvement Loop Method.md` — used for proposal-versus-improvement-work and outcome-change boundaries.
