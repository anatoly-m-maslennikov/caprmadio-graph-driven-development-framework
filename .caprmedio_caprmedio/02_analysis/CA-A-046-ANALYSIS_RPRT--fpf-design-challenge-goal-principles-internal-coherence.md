---
atom_id: CA-A-046
subject_scopes:
  - principles
  - authority
version: 1
updated_at: 2026-08-21 01:52:33
---

## Task, scope, and boundaries

Task: perform the routed `fpf-design-challenge` of the current CAPRMEDIO Goal and fourteen active Project-level Principle Requirements as one internal semantic system. This executes the previously proposed call. :codex-annotation{index="1"}

Receiving use: decide whether the Goal and Principles are internally coherent, self-sufficient, recursively aligned, MECE within a declared constitutional universe, and DRY enough to support a later compact Definition without that Definition inventing new authority.

Saved report: fpf-reports/20260819T222820Z-fpf-design-challenge-goal-principles-internal-coherence.md

Target and current state:

- One Goal carrier: `.caprmedio/CAPRMEDIO-GOAL-001--enable-any-operator-to-build-a-working-system.md`.
- Fourteen active top-level Requirement carriers with `tier: principle` under `.caprmedio/04_requirement/`.
- No carrier with `artifact_subtype: definition` or `tier: definition` was found under `.caprmedio/`.
- Every active Principle has the Goal as its only recorded `child_of` parent. No Principle-to-Principle semantic dependency, constraint, ownership, reinforcement, or conflict relation is recorded.
- The Goal and active Principle carriers are untracked in the current Git working tree. This review is bound to the observed filesystem snapshot, whose ordered aggregate SHA-256 is `fe1e5d810d67ed4a5f3a837b40e6250389c1c184751e73b890e22319b9a6c75f`.
- Thirteen Principles have `principle_order`; REQU-003 has none, leaving value 7 absent between 6 and 8. The inspected set does not define whether this is display order, reasoning order, or precedence.

Proposal claim: the Goal and active Principles should form a coherent constitutional basis in which every Principle supports the Goal, every Principle is compatible with the others, repeated meaning has one owner, and a compact Definition can be derived between Goal and Principles.

Entity of Concern: the selected Goal–Principles semantic structure, not the Markdown files as publication objects and not the uninspected lower-tier realization.

Bounded context: CAPRMEDIO's Project-wide constitutional authority before a Definition is admitted. For the MECE test, the reviewer uses this explicit provisional universe: **the project-wide responsibilities needed for CAPRMEDIO to help an operator turn intent into a working system while governing meaning, authority, realization, evidence, variation, scaling, and improvement**. This universe is a reviewer frame, not accepted project authority.

Resolved FPF source: the split `FPF-Knowledge-Graph` edition generated on 2026-08-02 from `FPF-Spec.md` revision `9a9a42e4d154021ca3f7415e0009a4214832f65f`. FPF is used only as a source of review lenses for distinctions, structure, parsimony, reuse, framework-set architecture, and conflict ordering. This report does not judge CAPRMEDIO–FPF compatibility.

Project evidence: exact bodies and frontmatter of the Goal and fourteen active Principles, their direct relations and ordering metadata, the absence of a Definition carrier, Git source status, and snapshot hashes. Direct FPF evidence: the six pattern pages listed under `FPF sources consulted`.

Decision owner: the CAPRMEDIO operator. Findings and candidate corrections below are reviewer conclusions, not changes, approvals, assurance, or project decisions.

Explicit exclusions: all Core and Standard Requirements; draft and archived Requirements; README prose; implementation, tools, tests, projections, runtime behavior, and Ops evidence; creation of the missing Definition; and edits to project authority. Lower tiers are not allowed to repair or reinterpret a Principle in this review.

Stop condition: every Goal and Principle has an individual finding; the important semantic relations, conflicts, gaps, overlaps, MECE boundary, DRY ownership, and Definition constraints are recorded; and the remaining operator decisions are explicit. Return when the Goal or a Principle changes, a Definition is proposed, the declared constitutional universe is accepted, or conflict and semantic-ownership relations are added.

## High-confidence results (>=95%)

### Proposal, resolved FPF source, and decision boundary

The broad design direction is coherent: operator-controlled graph governance, restrained complexity, structured scaling, controlled variation, evidence-bounded reliance, substrate independence, and feedback from outcomes can all support system building. The current selected structure is nevertheless not self-sufficient or recursively closed. **Overall result: `concern` — 99% confidence.**

This is an internal finding. The FPF pages supply tests such as keeping a selected structure distinct from its graph, requiring non-redundant action-facing distinctions, and making conflicts explicit. They do not supply CAPRMEDIO's Goal, Definition, Principle set, or decision.

### FPF Challenge Findings

#### 1. The Goal and missing Definition do not establish what CAPRMEDIO is

**Result: `concern` — 99% confidence.**

- **Project evidence.** The Goal promises that `any operator`, given `sufficient time and effort`, can turn a `feasible intent` into a `working system` (`Goal`, lines 14–18). No Definition carrier exists. The Principles repeatedly use CAPRMEDIO, operator, project, governed authority, canonical meaning, realization, Extension, Project Adaptation, capability, and working outcome without one constitutional statement that fixes CAPRMEDIO's kind, extent, operating boundary, or relation to the produced system.
- **Direct FPF basis.** A.7 separates the thing under concern from its descriptions and uses; A.22 requires exact constituents, obtaining relations, applied constraints, and a named use before selecting a structure; E.4.PFAD requires a framework's purpose, selected set, relation structure, dependency boundary, quality route, and currentness route to be recoverable (`A.7`, lines 50–77; `A.22`, lines 33–120; `E.4.PFAD`, lines 46–115).
- **Reviewer inference.** The missing Definition is not merely missing prose. The current set has not yet decided whether CAPRMEDIO is primarily a framework, an intelligent work environment framework, a governance system, a graph, a methodology-plus-engine, or some exact combination. A Definition cannot be safely compressed from the set until that object and boundary are settled.
- **Consequence.** Goal success cannot be evaluated consistently, and several Principles can be interpreted as rules about the framework, its graph, its carriers, the operator's project, or the produced system.
- **Candidate correction.** Decide the Definition's subject, kind, extent, and graph-to-real-system boundary first; then require every word in the Definition to be traceable to Goal or Principle authority. Do not use the Definition to add a new Principle.
- **Unchecked dependencies.** Lower-tier definitions may explain vocabulary, but they cannot substitute for the missing constitutional identity in this declared review.
- **Return condition.** Reopen when one candidate Definition is available or the operator fixes CAPRMEDIO's kind and boundary in plain language.

#### 2. The set violates its own recursive checkability rule

**Result: `concern` — 99% confidence.**

- **Project evidence.** REQU-022 says every governed CAPRMEDIO claim must state a condition or boundary showing it false, unsatisfied, or outside applicability (`REQU-022`, line 18). The Goal and most Principles do not state such a boundary. Examples include `feasible`, `working`, `necessary`, `material`, `governed`, `explicit`, `full sovereignty`, `canonical semantic model`, and `narrowest affected scope` without inclusion, exclusion, satisfaction, or stop conditions in the Goal–Principles set.
- **Direct FPF basis.** A.7 requires the exact kind and relation position before force is inherited; A.11 requires an action-facing contribution and a sharp inclusion/exclusion boundary; A.22 requires a named use and non-admissible overread (`A.7`, lines 50–77; `A.11`, lines 61–114; `A.22`, lines 33–120).
- **Reviewer inference.** REQU-022 is itself a coherent Principle, but the constitutional set to which it applies is not recursively conformant. A lower-tier evaluation method may operationalize the check; it should not have to invent what satisfaction means.
- **Consequence.** A Principle can appear authoritative while different operators apply materially different tests. The Goal is especially resistant to disconfirmation because any failure can be reclassified as infeasible or insufficient effort.
- **Candidate correction.** For every Goal or Principle, make at least the essential satisfaction, non-satisfaction, or applicability boundary recoverable at Principle level; delegate only the method of checking it.
- **Unchecked dependencies.** Core and Evaluation children were intentionally not inspected.
- **Return condition.** Reopen when the operator decides whether REQU-022 literally governs Goal and Principle bodies or permits their boundary to live in a direct governed child.

#### 3. The Goal–Principles set is not currently MECE

**Result: `concern` — 99% confidence.**

- **Project evidence.** REQU-002 applies MECE only to a taxonomy or decomposition that claims a declared universe (`REQU-002`, line 16). The Principle set declares neither that it is a canonical decomposition nor what universe it covers. Under the provisional constitutional universe stated above, the set has both uncovered responsibilities and overlapping ownership.
- **Direct FPF basis.** A.7 demands strict categorical separation; A.11 tests overlap, material difference, and boundary clarity; E.4.PFAD requires the selected set and its relation structure to be explicit (`A.7`, lines 50–77; `A.11`, lines 61–114; `E.4.PFAD`, lines 46–115).
- **Reviewer inference.** A set of Principles need not be mutually exclusive as sentences; complementary rules may intersect. The appropriate MECE target is their **primary constitutional responsibility**. On that target, the set is neither demonstrably exclusive nor exhaustive.
- **Uncovered responsibilities.** The current set lacks constitutional ownership for: CAPRMEDIO identity and extent; Goal success and `working system` recognition; graph-versus-reality and representation-versus-authority boundaries; Principle conflict resolution; explicit recursive self-application or exemptions; the external boundary on operator authority; and the protected invariants through which improvement may change authority. The Goal's `any operator` wording also implies an accessibility or comprehensibility responsibility that no active Principle clearly owns.
- **Overlapping responsibilities.** Canonical meaning is independently protected by REQU-003, REQU-009, REQU-010, and REQU-013. Graph organization is independently claimed by REQU-004 and REQU-044. Variation through Extensions is described by REQU-009, REQU-010, and REQU-013. `Necessary` information or complexity is split between REQU-005 and REQU-034 without an ownership relation.
- **Consequence.** New cases cannot be assigned deterministically, and a future Definition would have to hide or resolve gaps that the Principles themselves do not settle.
- **Candidate correction.** First accept the constitutional universe. Then assign one primary responsibility to each Principle, record the important cross-relations, and decide whether each uncovered responsibility belongs in the Goal, Definition, a Principle, or an explicit exclusion.
- **Return condition.** Reopen when the universe and ownership map are project authority.

#### 4. The set is not currently DRY at the semantic-ownership level

**Result: `concern` — 98% confidence.**

- **Project evidence.** REQU-003 requires one canonical owner for each governed meaning (`REQU-003`, line 15). Yet the set contains no semantic ownership or reference relations between Principles. REQU-009 forbids copying or redefining canonical authority; REQU-010 forbids configuration from changing governed meanings; REQU-013 preserves the canonical semantic model. These are potentially valid specializations, but the current graph does not state whether they depend on REQU-003 or independently own the same invariant.
- **Direct FPF basis.** A.11 requires composition and non-redundancy tests before admitting durable distinctions; F.8 requires recovery of the exact kind and use before reuse, aliasing, or new durable naming (`A.11`, lines 61–114 and 152–160; `F.8`, lines 73–194 and 358–384).
- **Reviewer inference.** Repeated words are not automatically duplication. The defect is that the current set cannot distinguish deliberate specialization from repeated authority. The strongest candidate canonical owners are: REQU-003 for single ownership of governed meaning; REQU-004 for graph-mediated governance; REQU-009 for adding Extensions; REQU-010 for selecting capabilities; REQU-013 for discipline adaptation; REQU-022 for claim checkability; and REQU-023 for reliance boundaries.
- **Consequence.** A change to one Principle can leave another sibling with stale or contradictory wording, violating the very DRY rule the set establishes.
- **Candidate correction.** Keep separate Principles only where their action-facing responsibility differs. Add precise dependency, specialization, or constraint relations so the general invariant has one owner and narrower Principles do not silently restate it.
- **Return condition.** Reopen when semantic ownership and specialization relations are proposed.

#### 5. The hierarchy Principle is not realized by the Principle set itself

**Result: `concern` — 99% confidence.**

- **Project evidence.** REQU-044 requires explicit configurable hierarchies within the typed graph (`REQU-044`, line 16). The inspected graph is a flat star: fourteen sibling Principles each point only to the Goal. `principle_order` is incomplete and has no declared conflict meaning. No relation says which Principle constrains, specializes, depends on, or outranks another.
- **Direct FPF basis.** E.3 identifies ambiguity and dead rules in flat Principle lists and requires explicit acyclic precedence; A.22 requires a selected organization to name exact constituents, obtaining relations, constraints, and use (`E.3`, lines 26–78 and 164–169; `A.22`, lines 33–120 and 447–463).
- **Reviewer inference.** CAPRMEDIO need not copy FPF's Principle classes or precedence order. It does need its own deterministic treatment of live tensions, including MECE versus necessary complexity, improvement versus stable canonical meaning, configurability versus invariant semantics, full operator sovereignty versus fail-closed reliance, and extensibility versus DRY.
- **Consequence.** The loudest or most convenient Principle wins when two Principles pull in different directions. Recursive alignment exists only as an intention, not as a governed graph structure.
- **Candidate correction.** Define a small local semantic relation set for Principles and a conflict rule. Keep display order separate from precedence unless the operator explicitly makes them the same.
- **Return condition.** Reopen when Principle relations and conflict handling are proposed.

### Coverage of the provisional constitutional universe

| Constitutional responsibility | Current owner candidates | Finding |
|---|---|---|
| Purpose and intended outcome | Goal | Present but unbounded; `feasible`, `any operator`, and `working system` prevent a stable success test. |
| Framework identity and extent | Missing Definition | Missing; cannot be reconstructed without operator decisions. |
| Governed operating model | REQU-004, REQU-044 | Present but overlapping; graph, selected structure, authority, and actual realization are not sharply separated. |
| Complexity and information scaling | REQU-005, REQU-034 | Present and broadly complementary, but both depend on undefined necessity and materiality tests. |
| Decomposition and semantic ownership | REQU-002, REQU-003 | Present as rules, not applied to the Principle set's own universe and ownership graph. |
| Capability variation and adaptation | REQU-009, REQU-010, REQU-013 | Present but boundaries among adding, selecting, parameterizing, specializing, and adapting remain incomplete. |
| Technical portability | REQU-012 | Present as a distinct axis. |
| Claim and reliance integrity | REQU-022, REQU-023 | Strong and meaningfully distinct, but the rest of the set does not recursively satisfy or reference them. |
| Operator authority | REQU-042 | Present but overbroad and unresolved against external constraints and fail-closed reliance. |
| Learning from outcomes | REQU-046 | Present, but protected invariants, evidence dependencies, and change authority are not linked. |
| Principle conflict and precedence | None | Missing. |
| Graph-to-world and authority-to-realization correspondence | Partial in REQU-004 | Missing as a boundary and correctness responsibility. |
| Human accessibility implied by `any operator` | None clearly | Missing or intentionally excluded; the Goal does not say which. |

### Goal and Principle relationship matrix

The matrix records reviewer-inferred semantic relations. None of these relations is currently encoded in the inspected Principle metadata.

| Artifact | Primary responsibility | Important inferred relations | Internal finding |
|---|---|---|---|
| Goal | Desired outcome | Should receive support from all Principles; currently supplies no bounded success test. | `concern` — 99%. |
| REQU-002 | Completeness and exclusivity of declared decompositions | Constrained by REQU-005; applicable to structures under REQU-044; needs an accepted universe before recursive use. | `no concern found within inspected scope` for its isolated wording — 97%; collective MECE remains a concern. |
| REQU-003 | One canonical owner per governed meaning | Should govern semantic reuse in REQU-009, REQU-010, REQU-013, and changes under REQU-046. | `concern` — 99% because the set records no ownership or reference relations. |
| REQU-004 | Graph-mediated governance operations | Supplies the graph environment for REQU-044 and selective exposure for REQU-034; needs a graph-versus-world boundary. | `concern` — 99%. |
| REQU-005 | Admission of necessary mechanisms | Constrains all mechanism-adding Principles; productive tension with REQU-002 completeness and REQU-034 information preservation. | `concern` — 97% because necessity and materiality have no recoverable boundary in scope. |
| REQU-009 | Addition or specialization through Extensions | Depends on REQU-003 and REQU-005; must remain distinct from REQU-010 selection and REQU-013 discipline adaptation. | `concern` — 98% because those boundaries and relations are absent. |
| REQU-010 | Project selection and parameterization of optional capabilities | Depends on REQU-003, REQU-009, and operator authority in REQU-042; can configure REQU-044 hierarchies only within a stated invariant. | `concern` — 98% because combination and parameterization can alter behavior without a defined meaning boundary. |
| REQU-012 | Independence from technical substrates | Coordinates with but is orthogonal to REQU-013 discipline independence. | `no concern found within inspected scope` — 97%. |
| REQU-013 | Discipline-independent canonical semantics with local adaptation | Depends on REQU-003 and overlaps Extension behavior in REQU-009; orthogonal to REQU-012. | `concern` — 98% because the canonical semantic model and adaptation boundary are undefined in scope. |
| REQU-022 | Checkability of governed claims | Meta-constrains the Goal and every Principle; supplies a prerequisite for REQU-023 and REQU-046. | `no concern found within inspected scope` for its isolated claim — 98%; recursive application is a major concern. |
| REQU-023 | Evidence, uncertainty, and stop conditions for reliance | Applies when any other Principle is relied on; supplies evidence discipline for REQU-046; tensions with an unbounded reading of REQU-042. | `no concern found within inspected scope` for its isolated claim — 98%; its semantic relations are missing. |
| REQU-034 | Preserve information and scale by structure and exposure | Coordinates with REQU-004 and is constrained by REQU-005 and REQU-003. | `no concern found within inspected scope` — 96%; the necessity test remains an unchecked dependency. |
| REQU-042 | Operator's project authority | Should own decisions under REQU-010 and REQU-046; conflicts with external authority and may conflict with REQU-023 if `full` means unconstrained. | `concern` — 99%. |
| REQU-044 | Hierarchical organization of authority | Specializes the graph claim in REQU-004; depends on REQU-002 for declared decompositions and REQU-010 for configuration; requires conflict semantics. | `concern` — 99%. |
| REQU-046 | Governed improvement from outcomes | Depends on REQU-022, REQU-023, REQU-042, REQU-003, and REQU-005; may change the authorities protected by other Principles. | `concern` — 98% because evidence, authority, invariants, and reopening relations are absent. |

### Strengths within inspected scope

1. **The set has a recognizable architecture — 99%.** Purpose, operating structure, parsimony, variation, epistemic control, operator authority, and improvement are all visible.
2. **REQU-022 and REQU-023 are a strong separation — 99%.** One governs whether claims can be challenged; the other governs when a use may rely on them. They should remain separate.
3. **REQU-009, REQU-010, REQU-012, and REQU-013 can become four useful independent axes — 97%.** They respectively address adding capability, selecting capability, technical substrate, and discipline adaptation. Their current problem is missing boundary and ownership relations, not the basic decomposition.
4. **REQU-005 and REQU-034 are compatible — 97%.** One limits admitted mechanisms; the other preserves needed information while managing exposure. Neither has to absorb the other.
5. **REQU-002 is correctly bounded in its own sentence — 98%.** It limits MECE to a declared universe and one abstraction level rather than claiming universal completeness.
6. **REQU-003 distinguishes ownership from reuse — 98%.** Reference, derivation, generation, and adaptation are explicitly permitted, which avoids equating DRY with textual deduplication.
7. **The direct parent topology is acyclic — 100%.** All active Principles point to the Goal and no inspected back-edge exists. This is structural hygiene, not proof of semantic alignment.

### Unchecked claims and insufficient basis

- No lower-tier Requirement was used to define or rescue a Goal or Principle. Their possible contribution is outside this review by design.
- Draft and archived Principles are not project authority for this result and were not used in any finding.
- No implemented behavior or Ops evidence was inspected, so the review does not claim that the Principles are or are not realized.
- The provisional constitutional universe is a reviewer construction. Collective exhaustiveness cannot be finally judged until the operator accepts or replaces that universe.
- The six-page direct-pattern budget was exhausted. No compatibility conclusion with FPF is made or needed.

### Return to project authority

The operator needs to decide, in this order:

1. What exact kind of thing CAPRMEDIO is and where its boundary ends.
2. What constitutional universe the Goal and Principles claim to cover.
3. Whether Goal and Principle boundaries must be present in those Atoms or may be delegated to direct governed children.
4. Which Principle owns each repeated meaning and what semantic relations connect the others.
5. How Principle conflicts are resolved and whether `principle_order` has any authority.
6. What `full sovereignty` means and which external constraints remain outside it.
7. What invariants improvement may change and what it must preserve.

Only after those decisions can a Definition be compacted without adding hidden authority. This report makes none of the decisions and changes no Atom.

## Open questions (confidence <95%)

### What is the intended constitutional universe?

Best current answer: the project-wide responsibilities needed for an operator to turn intent into a working system while CAPRMEDIO governs meaning, authority, realization, evidence, variation, scaling, and improvement. **Confidence: 92%.** Missing input: the operator's accepted inclusion and exclusion boundary. Consequence: MECE cannot be a project finding without it. Exact next action: accept, narrow, or replace that one-sentence universe before changing Principles.

### What kind of thing should the Definition say CAPRMEDIO is?

Best current answer: an Intelligent Work Environment framework whose methodology and engine use a typed project graph to help an operator build and govern working systems. **Confidence: 94%.** Missing evidence: this description is present in discussion but not in the inspected Goal–Principles authority. Consequence: inserting it now would make the Definition a new source of authority rather than a compression. Exact next action: decide which parts are definitional and trace each accepted part to a Goal or Principle responsibility.

### Where must a Principle's checkability boundary live?

Best current answer: the Principle must make its essential satisfaction, non-satisfaction, or applicability boundary recoverable, while a lower-tier Evaluation may define the checking method. **Confidence: 94%.** Missing input: the intended interpretation of REQU-022's word `state`. Consequence: allowing every boundary to live below the Principle makes the Principle set non-self-sufficient; requiring a full test in every Principle makes it too detailed. Exact next action: decide the minimum boundary required at Principle tier.

### What does `full sovereignty` mean?

Best current answer: final authority over project-owned CAPRMEDIO sources and decisions, within declared external legal, contractual, safety, privacy, and shared-ownership constraints. **Confidence: 92%.** Missing input: the operator's intended external and multi-person boundary. Consequence: the current word `full` can override or contradict reliance, Extension, and external obligations. Exact next action: state what the operator controls and what remains externally constrained.

### Is `principle_order` presentation or precedence?

Best current answer: presentation order only. **Confidence: 92%.** Missing evidence: no inspected authority defines it, and REQU-003 has no value 7. Consequence: treating it as precedence would silently create conflict authority from incomplete metadata. Exact next action: name its semantics explicitly or remove it from conflict reasoning.

### How independent are Extensions from the operator's project?

Best current answer: an Extension may evolve independently at its source, while the project operator controls whether and which edition is admitted into the current project. **Confidence: 91%.** Missing input: Extension ownership, import, edition, and local modification boundaries. Consequence: REQU-009's independent evolution and REQU-042's full sovereignty can otherwise conflict. Exact next action: decide that ownership boundary before revising either Principle.

## Skills used

- `fpf-design-challenge` — challenged the current Goal–Principles design as an internal semantic system while keeping project decisions with the operator.

#### FPF sources consulted (8 read; 7 used)

- `FPF-Knowledge-Graph/00-readme/02_Practical-Use Cards.md` — **used**: routed the review from the structure and improvement questions to direct patterns.
- `FPF-Knowledge-Graph/00_Index/FPF - Index.md` — **screened only**.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/07_Strict Distinction (Clarity Lattice)/00_A.07 - Strict Distinction (Clarity Lattice).md` — **used**: tested category boundaries and prevented graph, description, work, evidence, and authority from inheriting one another's force.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/11_Ontological Parsimony/00_A.11 - Ontological Parsimony.md` — **used**: tested composition, non-redundancy, action-facing contribution, and sharp boundaries.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/22_Structure and Structural Views (STRUCT-CAL)/00_A.22 - Structure and Structural Views (STRUCT-CAL).md` — **used**: tested whether the selected Goal–Principles structure states constituents, relations, constraints, use, and graph-versus-structure boundaries.
- `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/02_03_Principle Taxonomy & Precedence Model/00_E.03 - Principle Taxonomy & Precedence Model.md` — **used**: tested flat-list ambiguity, acyclic conflict ordering, and the separation of presentation from precedence.
- `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/03_04_FPF Ecosystem Family Architecture/02_E.04.PFAD - Principle-Framework Architecture Decision.md` — **used**: tested whether framework purpose, selected set, relation structure, dependency boundary, and return conditions are recoverable.
- `FPF-Knowledge-Graph/F_The Unification Suite (U-Suite)- Concept-Sets, SenseCells & Contextual Role Assignment/08_Mint-or-Reuse Decision/00_F.08 - Mint-or-Reuse Decision.md` — **used**: distinguished reuse of one recovered meaning from aliases, overlapping durable meanings, and premature new ownership.

<oai-mem-citation>
<citation_entries>
MEMORY.md:860-879|note=[used bounded FPF challenge routing and evidence separation guidance]
</citation_entries>
<rollout_ids>
019fb801-af36-7993-8d2c-b98cbd0dfc55
</rollout_ids>
</oai-mem-citation>
