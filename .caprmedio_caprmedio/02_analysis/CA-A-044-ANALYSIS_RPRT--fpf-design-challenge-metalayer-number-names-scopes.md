---
atom_id: CA-A-044
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-21 01:52:33
---

## Task, scope, and boundaries

:codex-annotation{index="1"}

### Proposal, resolved FPF source, and decision boundary

- **Task:** challenge the number, canonical names, ordering, and scope of CAPRMEDIO metalayers above Project level 0.
- **Proposal under review:** `CONCEPT_MODEL → SEMANTICS → GOVERNANCE → PROJECT`.
- **Entity of Concern:** CAPRMEDIO’s upstream structural authority model.
- **Receiving use:** an operator decision that will precede replacement Requirements, relation repair, and mechanical migration.
- **Scope:** how many metalayers are necessary, what each is called, its structural number, and its irreducible responsibility.
- **Exclusions:** existing mixed claims are treated as repairable migration work; this review does not classify every Atom, define global tiers, or authorize migration.
- **Project evidence:** current Project scope authority for META and GOV, the structural-level catalog, and representative Metamodel-, Semantics-, and Governance-like Requirements.
- **FPF source:** First Principles Framework Knowledge Graph generated from source revision `9a9a42e4d154021ca3f7415e0009a4214832f65f` on 2026-08-02.
- **Authority:** FPF supplies bounded challenge evidence. The CAPRMEDIO operator owns the decision.
- **Stop condition:** return a smallest sufficient metalayer set with names, numbers, and one non-overlapping scope formula per layer.
- **Saved report:** `fpf-reports/20260818T193750Z-fpf-design-challenge-metalayer-number-names-scopes.md`

## High-confidence results (>=95%)

### FPF Challenge Findings

#### Finding 1 — Three metalayers are the smallest sufficient partition — no concern found within inspected scope (96%)

- **Proposal and Entity:** split upstream authority into three owners before the concrete Project.
- **Project evidence:** current META already contains construct catalogs and graph grammar (`META-111`, `META-125`, `META-171`, `META-679`) as well as interpretive rules (`META-128`, `META-152`), while GOV owns carrier representation (`GOV-306`, `GOV-326`, `GOV-348`). These are three independently replaceable jobs.
- **Direct FPF basis:** A.7 separates independently governed categories even when one document or workflow presents them together (`A.7:61-87`); C.3.2 distinguishes a kind, its declaration, a judgment, and a representation (`C.3.2:56-85`); A.6.0 keeps reusable declarations separate from later realization and publication (`A.6.0:69-119`, `401-418`).
- **Reviewer inference:** two metalayers would force graph-language declarations and their cross-construct consequences back into one owner. Four metalayers would require an additional boundary—such as Ontology versus Metamodel—that the current proposal cannot make non-overlapping.
- **Consequence:** three owners expose real independent change boundaries without adding an unsupported fourth abstraction.
- **Candidate correction:** retain exactly three metalayers above Project.
- **Unchecked dependency:** the full active Atom inventory still has to be migrated after the operator decides.

#### Finding 2 — The canonical names should be `METAMODEL`, `SEMANTICS`, and `GOVERNANCE` — concern with `CONCEPT_MODEL` (98%)

- **Proposal and Entity:** name the first metalayer `CONCEPT_MODEL`.
- **Project evidence:** current META scope describes CAPRMEDIO’s vocabulary, axes, Artifact forms, Content roles, tiers, relations, and structural interpretation (`CAPRMEDIO-REQU-015:14-16`). That is the language used to model project authority, not a model of the project’s domain concepts.
- **Direct FPF basis:** C.3.2 keeps a local kind distinct from its reusable declaration and represented extension (`C.3.2:76-104`); A.6.0 requires a reusable declaration to name its subject, vocabulary, laws, and applicability without becoming the subject (`A.6.0:69-119`).
- **Reviewer inference:** “Concept Model” is a legitimate downstream project artifact and would create recurring ambiguity. “Metamodel” precisely names the model that defines how other CAPRMEDIO models and graph instances may be formed. “Ontology” overlaps both Metamodel and Semantics and therefore does not earn a fourth layer.
- **Consequence if unresolved:** framework grammar and project/domain concepts can be routed to the same owner.
- **Candidate correction:** use `METAMODEL → SEMANTICS → GOVERNANCE → PROJECT`.
- **Unchecked dependency:** `FRAMEWORK_METAMODEL` is a possible longer public label, but the structural context already makes `METAMODEL` sufficiently specific.

#### Finding 3 — Use metalayers −3, −2, and −1, with Project at 0 — no concern found within inspected scope (97%)

- **Proposal and Entity:** metalayers exist above Project level 0 and must have explicit numbers.
- **Project evidence:** current authority already treats structural level as a numbered parentage coordinate (`META-679:14-16`) and separately requires explicit configurable graph hierarchies (`CAPRMEDIO-REQU-044:14-16`).
- **Direct FPF basis:** A.22 requires selected structure to expose exact constituents, relations, constraints, and use frame; a visible ordering does not itself establish those relations (`A.22:33-73`, `110-120`). A.1.1 likewise preserves direct relations instead of collapsing several facts into one proxy (`A.1.1:103-135`).
- **Reviewer inference:** the most foundational metalayer should be farthest from Project 0. Each step toward zero adds constraints closer to the concrete project:

  ```text
  -3  METAMODEL
  -2  SEMANTICS
  -1  GOVERNANCE
   0  PROJECT
  ```

- **Consequence:** negative numbering makes “above Project” mechanical and leaves Project as the stable zero point.
- **Candidate correction:** metalayer numbers encode structural distance and order, not applicability tier, authority strength, or folder sequence.
- **Unchecked dependency:** global RMED tier numbers must be recalculated separately after adoption.

#### Finding 4 — Each metalayer needs one irreducible scope formula — concern if broad topic ownership remains (99%)

- **Proposal and Entity:** layer names should determine each layer’s scope.
- **Project evidence:** current GOV scope assigns identity and lifecycle wholesale to GOV (`CAPRMEDIO-REQU-016:14-16`), while META owns semantic Artifact identity (`META-128:13-15`) and GOV owns physical encoding and address derivation (`GOV-326:13-28`; `GOV-348:14-18`). Topic names alone therefore do not establish non-overlapping ownership.
- **Direct FPF basis:** A.7 separates the item under concern, its description, publication form, and carrier (`A.7:157-177`); A.22 separates selected structure from its graph or view (`A.22:79-120`, `234-265`); A.6.0 permits declaration, realization, and publication to change independently (`A.6.0:401-418`).
- **Reviewer inference:** the layer formulas should be:

  - **METAMODEL, level −3:** defines CAPRMEDIO’s admissible graph constructs, identity-bearing categories, independent axes, relation signatures, formation rules, and minimal constitutive definitions. It answers: **what can a well-formed CAPRMEDIO graph contain?**
  - **SEMANTICS, level −2:** defines what well-formed CAPRMEDIO constructs and relations mean together and what follows for authority, applicability, identity continuity, lifecycle/currentness, inheritance, conflict, propagation, and revision impact. It answers: **what does a well-formed CAPRMEDIO graph mean and imply?**
  - **GOVERNANCE, level −1:** defines how accepted CAPRMEDIO meaning is materialized and controlled through carriers, identifiers, names, placement, frontmatter, provenance encoding, validation, versioning, and change constraints. It answers: **how is CAPRMEDIO authority represented and kept governable?**
  - **PROJECT, level 0:** defines the concrete topology, scopes, adaptations, settings sources, and RMED authority adopted by one project. It answers: **which valid CAPRMEDIO instance does this project use?**

- **Consequence if unresolved:** identity, lifecycle, and relation rules will remain duplicated or migrate according to keywords instead of their actual claims.
- **Candidate correction:** classify claims by the question they answer, not by whether their text contains “identity,” “relation,” or “lifecycle.”
- **Unchecked dependency:** operational procedures remain Methodology and executable mechanisms remain Realization; Governance owns their constraints, not their work.

#### Finding 5 — Structural order must not replace typed relations — concern (97%)

- **Proposal and Entity:** express the design as one descending arrow chain.
- **Project evidence:** CAPRMEDIO’s authority is an explicitly typed graph (`CAPRMEDIO-REQU-044:14-16`).
- **Direct FPF basis:** A.22 says a diagram or graph does not make a relation obtain (`A.22:110-120`); A.1.1 returns related facts to their exact direct relations (`A.1.1:103-135`).
- **Reviewer inference:** `−3 → −2 → −1 → 0` is structural order only. Project constructs may instantiate Metamodel constructs, Project authority may specialize applicable upstream authority, and Project carriers may conform to Governance. Those relations remain explicit.
- **Consequence if unresolved:** readers can mistake Governance for the source of Semantics or infer that Project reaches Metamodel only indirectly.
- **Candidate correction:** govern structural parentage and semantic relation kinds independently.
- **Unchecked dependency:** exact relation names and signatures remain a later Project/GOV decision.

### Strengths within inspected scope

- **MECE improvement (98%):** graph grammar, graph interpretation, carrier control, and concrete adoption have distinct replacement triggers.
- **Natural expansion point (97%):** projects may add domain Concept Models without confusing them with CAPRMEDIO’s Metamodel.
- **Recursive compatibility (96%):** CAPRMEDIO can use the same three metalayers to describe its own self-hosted Project instance.
- **Readable operator model (97%):** the negative sequence ends naturally at Project 0 and each name answers a different plain-language question.

### Unchecked claims and insufficient basis

- **Insufficient basis (100%):** this challenge does not prove that every current META/GOV Atom has exactly one destination; that needs a complete claim-level classification.
- Current structural Requirements, Contracts, parent relations, folder names, project settings, global tiers, and generated Projections remain unchanged.
- This is not a migration plan, implementation authorization, or final alignment result.

### Return to project authority

The strongest bounded candidate is:

```text
001_METALAYER_MINUS_3_METAMODEL
002_METALAYER_MINUS_2_SEMANTICS
003_METALAYER_MINUS_1_GOVERNANCE
--
PROJECT_LEVEL_0
```

The leading `001..003` values are directory-order prefixes. `MINUS_3..MINUS_1` are Structural-level coordinates. They must not be interpreted as global tiers.

FPF does not authorize adoption. The CAPRMEDIO operator decides whether to accept this three-metalayer model and then initiate the authority-first migration.

## Open questions (confidence <95%)

### Should the folder label be `METAMODEL` or `FRAMEWORK_METAMODEL`? — 93%

- **Best current answer:** `METAMODEL`. Metalayer placement already supplies framework context, and the shorter name is sufficient.
- **Missing input:** whether cold readers will encounter project/domain metamodels beside this folder often enough to require explicit disambiguation.
- **Consequence:** `FRAMEWORK_METAMODEL` is clearer in isolation but adds permanent naming ceremony; `METAMODEL` is cleaner but relies on structural context.
- **Exact next action:** operator selects the public label; no semantic decision depends on the longer form.

## Skills used

- `fpf-design-challenge` — challenged the proposed metalayer count, names, numbers, and scope boundaries without authorizing implementation.

#### FPF sources consulted (10 read; 6 used)

- `FPF-Knowledge-Graph/00-readme/02_Practical-Use Cards.md` — **used**: routed the design question through architecture and description boundaries.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/01_Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)/01_A.01.01 - Bounded Model-Use Structure and DDD Bounded-Context Recovery.md` — **used**: supported direct-relation and semantic-locality boundaries.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/07_Strict Distinction (Clarity Lattice)/00_A.07 - Strict Distinction (Clarity Lattice).md` — **used**: supported category separation.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/05_A.06.00 - U.Signature - Reusable Law-Governed Declaration Episteme.md` — **used**: separated reusable declarations from subjects, realizations, and publications.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/22_Structure and Structural Views (STRUCT-CAL)/00_A.22 - Structure and Structural Views (STRUCT-CAL).md` — **used**: supported exact structure and relation boundaries.
- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/01_03_Kinds, Intent and Extent, and Typed Reasoning/02_C.03.02 - Kind Intent, Membership Judgment, and Extension.md` — **used**: separated kinds, declarations, judgments, and representations.
- `FPF-Knowledge-Graph/F_The Unification Suite (U-Suite)- Concept-Sets, SenseCells & Contextual Role Assignment/07_Concept-Set Table/00_F.07 - Concept-Set Table.md` — **screened only**.
- `FPF-Knowledge-Graph/F_The Unification Suite (U-Suite)- Concept-Sets, SenseCells & Contextual Role Assignment/00/00_F.00.01 - Contextual Lexicon Principles.md` — **screened only**.
- `FPF-Knowledge-Graph/00_Index/FPF - Index.md` — **screened only**.
- `FPF-Knowledge-Graph/00_Index/FPF - Term Index.md` — **screened only**.
