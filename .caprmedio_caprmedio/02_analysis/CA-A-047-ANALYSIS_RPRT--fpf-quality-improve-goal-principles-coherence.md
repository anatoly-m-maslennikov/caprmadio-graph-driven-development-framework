---
atom_id: CA-A-047
subject_scopes:
  - principles
  - continuous-improvement
version: 1
updated_at: 2026-08-21 01:52:33
---

## Task, scope, and boundaries

:codex-annotation{index="1"}

This record executes `fpf-quality-improve` for the current CAPRMEDIO Goal and fourteen active Project Principles. The receiving use is an operator decision on one exact candidate edition before any authoritative Atom is changed.

Target version: the current working-tree Goal plus active Project Principle set, with combined content digest `2de1b97d2ae90575016ecd39169d2f2a61845ca7bc6dd2b119c6c77b9ef83be7`. The repository is on `dev` at Git commit `3730084af7f1a890415a22837cc6adee053e685d`, but all fifteen target carriers are currently untracked as part of a much larger in-progress migration, so the digest—not the commit—is the recoverable target identity.

The target contains Goal version 4 and these Principle versions: REQU-002 v9, REQU-003 v8, REQU-004 v4, REQU-005 v8, REQU-009 v5, REQU-010 v5, REQU-012 v3, REQU-013 v5, REQU-022 v6, REQU-023 v6, REQU-034 v4, REQU-042 v3, REQU-044 v1, and REQU-046 v5.

Scope includes:

- internal coherence of the Goal and active Principles;
- whether the Principles can compile into a non-authoritative Definition without adding meaning;
- Goal alignment, Principle self-sufficiency, horizontal coherence, recursive alignment, MECE, DRY, graph/reality separation, variation boundaries, operator authority, improvement integrity, and parsimony;
- exact candidate wording, disposition of every current Principle, ownership and dependency maps, a Definition preview, and downstream impact.

Scope excludes applying the candidate, editing Core or Standard Requirements, changing the Goal → Project → Principle topology, making the Definition authoritative, storing presentation order on Principles, and judging compatibility with FPF. Existing lower-tier rules were inspected only to avoid proposing duplicate Principle-level authority.

Project evidence includes the fifteen target Atoms and the current carriers that already define the Project Principle universe and one-owner rule (REQU-026 and REQU-027), tier conflict behavior (REQU-024, REQU-025, and REQU-028), the current navigation-order rule (GOV-REQU-330), Definition projection status and generation (META-REQU-777 and GOV-REQU-783 through GOV-REQU-785), variation boundaries (REQU-686, META-REQU-160, META-REQU-687, and METHODOLOGY-REQU-690), operator authorization (REQU-043 and REQU-052), and improvement comparison framing (REQU-053).

Authority: this is a read-only proposal. It changes no Goal, Principle, Definition, Core, Standard, relation, ordering metadata, validator, or Projection. The only written artifact is this non-authoritative report.

Saved report: `fpf-reports/20260819T230509Z-fpf-quality-improve-goal-principles-coherence.md`

Stop condition: stop after producing and evaluating one exact candidate edition. Application requires explicit operator acceptance, followed by a new target version and the same evaluation rerun against actual changed carriers.

## High-confidence results (>=95%)

### 1. Loop contract and resolved FPF source

**Result: the loop is sufficiently framed to produce a candidate, but not to claim live improvement — 99% confidence.**

The object under improvement is the digest-pinned Goal–Principles edition above. The evaluation coordinates are:

1. Definition compileability;
2. Goal alignment;
3. individual Principle self-sufficiency;
4. horizontal coherence;
5. recursive alignment;
6. MECE over the declared Project Principle universe;
7. DRY semantic ownership;
8. graph/reality boundary;
9. variation boundaries;
10. operator authority;
11. improvement integrity;
12. parsimony.

The bounded change hypothesis is: **retain the current fourteen-Principle membership and identities, revise only wording that hides a boundary or duplicates another Principle's responsibility, remove presentation-order state from the authoritative Principles, and compile the resulting set into a Definition without adding a new Principle.**

Protected trade-offs are the Goal's broad operator ambition, graph-driven operation, one canonical owner per meaning, the existing tier topology, existing lower-tier authority, Definition non-authority, equal authority among all Project Principles, and the ability to extend and configure CAPRMEDIO. Refusal conditions are any change that silently narrows the Goal to one discipline or substrate, turns the Definition into authority, adds same-tier `child_of` edges, changes lower-tier meaning by implication, or introduces a new Principle without a distinct project-wide invariant.

Expected cost is one Goal body revision, eleven Principle body revisions, removal of the thirteen existing presentation-order fields, replacement or archival of the obsolete navigation-order rule, Definition regeneration, lineage-impact review, and deterministic validation. Primary risks are semantic drift in the Goal, making the graph sound like reality, weakening operator control, or moving Core detail into Principles. The proposal is reversible because no target change is made here; if later applied, the previous versions and repository history remain recoverable.

The FPF source was resolved to the local generated knowledge graph in `/Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph`, whose opened pages identify source revision `9a9a42e4d154021ca3f7415e0009a4214832f65f`. The improvement-loop guidance requires a versioned target, a stable evaluation frame, protected trade-offs, a real target change, re-evaluation, and a local stop or switch decision. That is why this record can propose and forecast a candidate but cannot call the live target improved.

### 2. Baseline target version and evaluation

**Result: the current set has a strong underlying architecture, but the declared quality result is not yet demonstrated across the twelve coordinates — 98% confidence.**

| Coordinate | Baseline finding | Evidence basis | Confidence |
|---|---|---|---:|
| Definition compileability | The Principles can compile into a behavioral description, but current wording forces the compiler to resolve `full sovereignty`, graph-versus-fact status, and improvement-before-evaluation. A Definition that calls CAPRMEDIO an “Intelligent Work Environment framework” would add a label not established by the Principles. | Current Principle bodies; META-REQU-777; GOV-REQU-784. | 98% |
| Goal alignment | Every Principle is directly `child_of` the Goal, but `feasible intent` and `working system` have no boundary in the Goal itself. The two Goal paragraphs repeat the same claim without making success more testable. | Goal v4; fourteen Principle frontmatters. | 99% |
| Principle self-sufficiency | REQU-002, REQU-012, and REQU-023 are already sufficiently bounded. REQU-005, REQU-042, and REQU-046 rely most heavily on unstated boundaries; REQU-004 permits graph membership to be overread as fact. | Exact Principle bodies. | 98% |
| Horizontal coherence | The apparent overlap clusters are mostly legitimate distinct axes, and the existing Core layer already separates them. The Principle wording still repeats canonical-meaning protection across REQU-003, REQU-009, REQU-010, and REQU-013 instead of making their different questions obvious. | Principles plus REQU-686, META-REQU-160, META-REQU-687, and METHODOLOGY-REQU-690. | 98% |
| Recursive alignment | The set already applies `child_of` uniformly to the Goal, and the project already governs the Principle universe and one-owner rule. The concrete set still lacks an explicit responsibility assignment, several Principles do not meet REQU-022 without relying on unstated checks, and stored presentation order adds a rule the authority model does not need. | REQU-026, REQU-027, REQU-022, GOV-REQU-330; deterministic frontmatter inspection. | 99% |
| MECE | The relevant universe is already declared: all irreducible governed invariants that apply across the whole project independently of structural level, scope, role, form, Extension, Project Adaptation, or substrate. The current set has no applied one-owner map showing that each admitted responsibility appears exactly once. | REQU-026 and REQU-027. | 99% |
| DRY | The set has one canonical-owner Principle, but its own repeated semantic protections are not assigned to distinct primary questions. This is a responsibility-ownership gap, not a textual-duplication problem. | REQU-003 and the four variation Principles. | 98% |
| Graph/reality boundary | REQU-004 makes the graph the mandatory operating surface but does not say that a node or edge represents rather than independently establishes its governed fact. | REQU-004; FPF structure/representation boundary. | 99% |
| Variation boundaries | The lower-tier model already distinguishes reusable Extension authority, project-owned configuration and adaptation, discipline adaptation, and substrate independence. The Principle set needs clearer summaries, not another Principle. | REQU-009, REQU-010, REQU-012, REQU-013 and their direct children. | 99% |
| Operator authority | `full sovereignty over the entire current project` overreaches project-owned authority and leaves externally constrained or shared matters ambiguous. REQU-043 correctly establishes operator acceptance or delegation for governed change but does not repair that sentence. | REQU-042 and REQU-043. | 99% |
| Improvement integrity | The lower tier correctly requires operator request, exact baseline, evaluation frame, protected trade-offs, and stop condition. REQU-046 still says outcomes become “improvement” before a changed version is evaluated. | REQU-046, REQU-052, and REQU-053. | 99% |
| Parsimony | No additional Principle is required to repair the demonstrated gaps. Each gap can be resolved by one existing owner's wording, a Projection-level presentation rule, or an already-existing Core/GOV rule. | Current membership; existing lower-tier rules; composition and non-redundancy test. | 96% |

The earlier challenge's claims that the Definition mechanism, Principle universe, conflict rules, and `principle_order` semantics were missing are superseded by the current inspected carriers. The remaining problem is application and wording. The current semantics of `principle_order` are known; this proposal concludes that the field itself is unnecessary because all Principles have equal authority and presentation order belongs to each Projection.

### 3. Bounded change hypothesis and implementation evidence

**Result: one recoverable candidate edition resolves the high-confidence gaps without adding or deleting a Principle — 97% confidence.**

#### Proposed Goal

Keep the existing Goal identity and title. Replace both current body paragraphs with this single claim:

> Within its declared applicability, CAPRMEDIO must enable any operator, given sufficient time and effort, to turn an intent that the project accepts as feasible into a system that satisfies the project's accepted Requirements and Evaluation criteria.

This preserves `any operator`, time and effort, and feasibility while making applicability, feasibility authority, and `working` success recoverable.

#### Disposition and exact wording for every active Principle

1. **REQU-004 — reword; keep identity and title, “The graph is the operating model.”**

   > Every CAPRMEDIO governance operation must read or change the typed graph of governed authority, realization bindings, and direct relations. The graph represents those governed facts; its nodes and edges do not establish facts that lack their required authority or evidence.

2. **REQU-005 — reword; keep identity and title, “Necessary complexity only.”**

   > CAPRMEDIO may admit or retain a mechanism only when existing mechanisms cannot preserve a required outcome or a material governed distinction.

3. **REQU-034 — reword; keep identity and title, “Scale through structure.”**

   > CAPRMEDIO must preserve information required for a governed use and manage its visible volume through structure and selective exposure; information hidden from the current view must remain recoverable.

4. **REQU-009 — reword; keep identity and title, “Extensibility adds governed capabilities.”**

   > CAPRMEDIO must admit independently evolvable reusable capabilities only as explicit Extensions whose extension points, authority boundary, and compatibility conditions are declared.

5. **REQU-010 — reword; keep identity and title, “Configurability selects available capabilities.”**

   > CAPRMEDIO must permit project-owned configuration to select, combine, parameterize, or disable available optional canonical and Extension capabilities only within their declared configuration boundaries and without redefining their governed meanings.

6. **REQU-002 — keep unchanged.**

   > Every canonical CAPRMEDIO taxonomy or decomposition that claims to cover a declared universe must be mutually exclusive and collectively exhaustive within that universe and at that level of abstraction.

7. **REQU-003 — reword; keep identity and title, “Apply DRY across CAPRMEDIO.”**

   > CAPRMEDIO must assign each governed meaning to one canonical owner capable of resolving it completely and unambiguously; every other use must reference, derive, generate, or explicitly adapt that owner without becoming duplicate authority.

8. **REQU-022 — reword; keep identity and title, “Require falsifiable claims.”**

   > Every governed CAPRMEDIO claim must state or directly reference an observable condition or applicability boundary by which it can be shown false, unsatisfied, or out of scope. When a reasonable disconfirming check exists, confirmatory evidence alone is insufficient.

9. **REQU-023 — keep unchanged.**

   > Every governed use of authority, Method, Implementation, Evaluation, Delivery, or Ops conclusions must state the evidence and material uncertainty on which reliance is permitted and the condition that stops, degrades, blocks, or reopens that reliance. A missing, unknown, or contradictory required input fails closed at the affected use.

10. **REQU-013 — reword; keep identity and title, “Preserve discipline independent semantics.”**

    > CAPRMEDIO must keep one discipline-independent canonical semantic model; Extensions and Project Adaptations may adapt discipline-specific terminology, Artifact Types, Methods, Evaluation, and Implementation only through declared mappings that preserve canonical meanings.

11. **REQU-012 — keep unchanged.**

    > CAPRMEDIO must keep its authority and semantics independent of any particular operating system, operator language, programming language, LLM provider or model, or agent host.

12. **REQU-042 — reword; keep identity and title, “Preserve operator sovereignty.”**

    > CAPRMEDIO must preserve the operator's final authority over every project-owned CAPRMEDIO meaning, decision, and Artifact.

13. **REQU-044 — reword; keep identity and title, “Organize authority as a hierarchical graph.”**

    > CAPRMEDIO must organize governed authority as explicit, typed, acyclic hierarchies whose relation kinds and configuration boundaries are declared in its graph.

14. **REQU-046 — reword; keep identity and title, “Improve from observed project outcomes.”**

    > CAPRMEDIO must use material observed project outcomes to propose and evaluate changes at the narrowest affected scope while preserving unaffected authority.

No Principle is merged, split, replaced, or archived. No new Principle is admitted in this candidate.

#### Remove stored Principle presentation order

Remove `principle_order` from every active Project Principle rather than adding the missing value to REQU-003.

Replace or archive GOV-REQU-330 so that it no longer requires order metadata on authoritative Principles. The replacement rule should state:

> Project Principles have equal authority and store no presentation order. Each Projection owns its presentation order; when no projection-specific order is declared, it uses stable Artifact ID order.

This keeps display deterministic while preventing a presentation field from being mistaken for precedence or forcing unrelated renumbering when a Principle is inserted.

#### Declared Principle universe and canonical ownership map

Retain the universe already owned by REQU-026: **all irreducible governed invariants that apply across the entire current project independently of structural level, scope label, Content role, Artifact form, Extension, Project Adaptation, or substrate.**

Apply REQU-027 through this one-question-per-owner map:

| Owner | Sole primary question |
|---|---|
| REQU-004 | Through what operating representation must governance read and change the project? |
| REQU-005 | When may a framework mechanism be admitted or retained? |
| REQU-034 | How is required information preserved while visible volume is controlled? |
| REQU-009 | How do independently evolvable reusable capabilities enter? |
| REQU-010 | How does a project select and parameterize available capabilities? |
| REQU-002 | When is a canonical decomposition complete and non-overlapping? |
| REQU-003 | Where is each governed meaning canonically owned and how may it be reused? |
| REQU-022 | How can a governed claim be disproved, found unsatisfied, or found inapplicable? |
| REQU-023 | Under what evidence, uncertainty, and stop conditions may a governed conclusion be relied on? |
| REQU-013 | How may discipline-specific adaptation preserve canonical semantics? |
| REQU-012 | Which technical substrates may determine CAPRMEDIO authority or semantics? None. |
| REQU-042 | Who has final authority over project-owned CAPRMEDIO meaning and Artifacts? |
| REQU-044 | How is governed authority structurally organized? |
| REQU-046 | How do observed outcomes enter proposed and evaluated focused change? |

This map is MECE at the level of **primary constitutional responsibility**, not at the level of every word or downstream effect. Cross-cutting Principles may constrain the same downstream case without becoming co-owners of the same primary question.

#### Minimal semantic dependency map

The smallest useful dependency reading is:

- REQU-003 constrains REQU-009, REQU-010, REQU-013, and REQU-046: reuse, variation, adaptation, and change must not create duplicate authority.
- REQU-005 constrains REQU-009, REQU-010, REQU-034, REQU-044, and REQU-046: mechanisms, views, structures, and improvement apparatus remain necessity-bounded.
- REQU-002 constrains REQU-044: every declared authority decomposition must name its universe and discrimination basis.
- REQU-004 supplies the operating representation used by REQU-034, REQU-044, and REQU-046.
- REQU-022 supplies the challenge boundary used by REQU-023 and REQU-046.
- REQU-023 constrains reliance on results produced under REQU-046.
- REQU-042 authorizes project-owned selections under REQU-010 and governed changes under REQU-046.
- REQU-013 constrains discipline-specific use of REQU-009 and REQU-010.

This is a review map, not proposed frontmatter. Project authority permits Project Principle `child_of` edges only to the lower-global-tier Goal in the same scope; same-tier Principle-to-Principle `child_of` edges are not admissible. If CAPRMEDIO later wants persisted same-tier semantic dependency relations, META/GOV must first admit precise non-authority relation kinds and their direction rules.

#### Generated Definition preview

> CAPRMEDIO governs project authority and realization through a typed graph, with authority organized as explicit acyclic hierarchies. It gives every governed meaning one canonical owner, keeps declared decompositions complete and non-overlapping, admits only necessary mechanisms, and preserves required information through structure and selective exposure. It admits reusable capabilities through governed Extensions, lets projects configure available capabilities within declared boundaries, preserves canonical meaning across disciplines, and keeps authority independent of technical substrates. Its claims are checkable, its reliance boundaries explicit, its project-owned authority remains under the operator, and observed outcomes drive proposals and evaluated focused changes.

Phrase trace:

| Definition phrase | Principle source |
|---|---|
| governs authority and realization through a typed graph | REQU-004 |
| authority organized as explicit acyclic hierarchies | REQU-044 |
| every governed meaning one canonical owner | REQU-003 |
| declared decompositions complete and non-overlapping | REQU-002 |
| admits only necessary mechanisms | REQU-005 |
| preserves required information through structure and selective exposure | REQU-034 |
| admits reusable capabilities through governed Extensions | REQU-009 |
| configures capabilities within declared boundaries | REQU-010 |
| preserves canonical meaning across disciplines | REQU-013 |
| authority independent of technical substrates | REQU-012 |
| claims are checkable | REQU-022 |
| reliance boundaries explicit | REQU-023 |
| project-owned authority remains under the operator | REQU-042 |
| outcomes drive proposals and evaluated focused changes | REQU-046 |

The preview introduces no independent claim and deliberately does not call CAPRMEDIO an Intelligent Work Environment. It is a candidate projection only; GOV-REQU-785 still requires explicit operator approval before publication.

#### Implementation evidence

There is no implementation evidence because application was not authorized. No target carrier or authority was changed. The report file is evidence of the proposal, not evidence that the candidate edition exists or that quality changed.

### 4. Re-evaluation and declared-coordinate comparison

**Result: the candidate is predicted to improve all demonstrated gap coordinates without a protected-trade-off regression, but this is a proposal evaluation rather than a changed-target evaluation — 97% confidence.**

| Coordinate | Current edition | Candidate edition, if applied | Expected result change |
|---|---|---|---|
| Definition compileability | Requires hidden boundary decisions. | Compiles to the traced preview with no new claim. | Clear positive change. |
| Goal alignment | `feasible` and `working` are unbounded and duplicated. | Applicability, feasibility acceptance, and success criteria are named once. | Clear positive change. |
| Principle self-sufficiency | Several load-bearing terms depend on private interpretation. | Each revised owner carries its minimum inclusion, exclusion, or reference boundary. | Positive change. |
| Horizontal coherence | Repeated canonical-meaning language obscures distinct responsibilities. | Every Principle answers one primary question; narrower effects are inherited through the ownership/dependency maps. | Positive change. |
| Recursive alignment | Universe and one-owner rules exist but are not visibly applied; authoritative Atoms carry unnecessary display state. | Ownership map applies the rules; stored presentation order is removed; checkability may be directly referenced rather than duplicated. | Positive change. |
| MECE | Not demonstrated for the actual set. | Fourteen primary questions cover the accepted universe without duplicate primary ownership. | Positive change, subject to operator acceptance of the map. |
| DRY | Several Principles repeat the same prohibition. | REQU-003 owns duplicate-authority prevention; variation Principles own only their distinct change modes. | Positive change. |
| Graph/reality boundary | Graph presence can be overread as fact. | Representation is explicit; required authority or evidence remains independently necessary. | Clear positive change. |
| Variation boundaries | Correct lower-tier separation is only partly visible at Principle tier. | Extension admission, project configuration, discipline adaptation, and substrate independence are distinct. | Positive change. |
| Operator authority | `full sovereignty` is unbounded. | Final authority is bounded to project-owned CAPRMEDIO meaning, decisions, and Artifacts. | Clear positive change. |
| Improvement integrity | The Principle presupposes improvement. | Outcomes produce proposals and evaluated changes; improvement is established only after comparison. | Clear positive change. |
| Parsimony | Fourteen Principles plus unresolved wording and presentation metadata. | Same fourteen identities; no new Principle, stored order, relation kind, or tier mechanism. | Positive change. |

The candidate preserves all fourteen direct Goal parents and their equal global-tier authority. Different Projections may use different readable orders without changing any Principle or implying precedence.

### 5. Trade-offs, costs, risks, and uncertainty

**Result: the candidate's expected semantic gain is proportionate to its change cost — 96% confidence.**

- **Preserved:** Goal ambition, Project Principle membership, identifiers, direct Goal lineage, tier semantics, Core/Standard authority, Definition non-authority, graph-driven operation, Extension/configuration support, equal Principle authority, and operator control.
- **Reduced:** duplicated wording, undefined success language, graph-as-fact overread, unbounded sovereignty, circular improvement claims, and presentation metadata drift.
- **Cost:** one compact coordinated revision across twelve bodies, removal of the thirteen existing order fields, replacement or archival of GOV-REQU-330, Definition regeneration, and validation. Because the repository is already undergoing a large migration, application should be one isolated logical commit after the current file identities are stable.
- **Risk:** direct children may contain phrases that assumed the old wording. This is a lineage-review obligation, not permission to edit them automatically. The most sensitive descendants are REQU-043, REQU-052, REQU-053, REQU-686, META-REQU-160, META-REQU-687, and METHODOLOGY-REQU-690.
- **Reversibility:** high. The proposal preserves Atom identities and can be reverted by restoring prior bodies and version metadata. A generated Definition can be regenerated from either frontier.
- **Uncertainty:** the analysis can show that the wording and responsibility map are coherent; only an accepted changed edition plus rerun validation can show actual improvement.

### 6. Outcome and stop/continue/rollback/switch decision

**Outcome: `not demonstrated` for the live target — 100% confidence.**

The live target was not changed, so improvement cannot be claimed. The candidate is a high-confidence proposal with a favorable predicted comparison.

**Decision: stop for operator acceptance.**

- **Continue** if the operator accepts the Goal wording, all fourteen dispositions, removal of stored Principle order, the ownership map, and the Definition preview boundary. Then create a new recoverable target edition, update versions and provenance, replace or archive GOV-REQU-330, update affected Projection and validator rules, regenerate the Definition, inspect lineage impact, run deterministic validators, and rerun these same twelve coordinates.
- **Rollback** if an applied candidate changes a protected meaning, invalidates a lower-tier child, or makes any Definition phrase untraceable to one or more Principles.
- **Switch method** if the unresolved Intelligent Work Environment identity must become authoritative. That is a separate design decision about whether the label belongs in a Principle, in another authority carrier, or only in publication; it should not be smuggled into this wording repair.

## Open questions (confidence <95%)

### May the generated Definition call CAPRMEDIO an “Intelligent Work Environment framework”?

Best current answer: **not yet; keep that label out of the exact Principle-only projection unless its intended meaning is accepted as a faithful summary or assigned to an authoritative owner. Confidence: 93%.**

Missing input: the operator's intended inclusion and exclusion boundary for “Intelligent Work Environment,” especially whether `intelligent` claims an LLM/agent property and whether `framework` names a governed kind or only a public label.

Consequence: adding the phrase now may introduce meaning absent from the active Principles; omitting it leaves a precise behavioral Definition but not the preferred category label.

Exact next action: choose one of three dispositions before publishing the Definition: (1) approve the phrase as a meaning-preserving public coarsening of the traced preview; (2) define a distinct project-wide invariant that justifies a new or revised Principle; or (3) keep the phrase in non-authoritative documentation only. Do not change the current fourteen-Principle candidate merely to make the label fit.

## Skills used

- `fpf-quality-improve` — framed one versioned Goal–Principles improvement loop, recovered the baseline, produced one bounded candidate, forecast the same-coordinate comparison, and stopped without claiming unperformed improvement.

#### FPF sources consulted (8 read; 7 used)

- `FPF-Knowledge-Graph/00-readme/02_Practical-Use Cards.md` — **used**: routed the request to a versioned improvement loop rather than another unframed review.
- `FPF-Knowledge-Graph/00_Index/FPF - Index.md` — **screened only**.
- `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/22_23_Quality Improvement Loop Method/00_E.23 - Quality Improvement Loop Method.md` — **used**: governed target identity, baseline, bounded hypothesis, protected trade-offs, real-change boundary, re-evaluation, and stop decision.
- `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/21_22_Improvement-Oriented Quality Evaluation Question Framing/00_E.22 - Improvement-Oriented Quality Evaluation Question Framing.md` — **used**: fixed the evaluation coordinates, consuming use, proposal boundary, and same-frame comparison.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/11_Ontological Parsimony/00_A.11 - Ontological Parsimony.md` — **used**: tested whether any new Principle was necessary and required an action-facing, non-redundant boundary.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/22_Structure and Structural Views (STRUCT-CAL)/00_A.22 - Structure and Structural Views (STRUCT-CAL).md` — **used**: separated the typed graph and its views from the facts, authority, evidence, and realization they represent.
- `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/02_03_Principle Taxonomy & Precedence Model/00_E.03 - Principle Taxonomy & Precedence Model.md` — **used**: kept presentation order separate from authority and conflict precedence.
- `FPF-Knowledge-Graph/F_The Unification Suite (U-Suite)- Concept-Sets, SenseCells & Contextual Role Assignment/08_Mint-or-Reuse Decision/00_F.08 - Mint-or-Reuse Decision.md` — **used**: prevented a convenient “Intelligent Work Environment” label from becoming new governed meaning without an ownership decision.

<oai-mem-citation>
<citation_entries>
MEMORY.md:941-942|note=[used FPF source discovery, evidence separation, and report persistence guidance]
</citation_entries>
<rollout_ids>
019fc257-ad77-7d31-b3e2-1b6b37cc0274
</rollout_ids>
</oai-mem-citation>
