## Task, scope, and boundaries

### Task and receiving use

Challenge the proposal to make formal language the authoritative representation for Project Principles and Bootstrap Seed authority, while treating human-readable text as a derived Projection or as Translation Atoms. The receiving use is an Operator architecture decision about semantic authority, authoring, validation, and LLM interaction.

### Target and current state

The current Project model authors two representations inside each active Principle. `CA-R-839` declares them semantically equivalent representations of one meaning, and `CA-R-840` requires the human-readable statement first. A live scan found 20 active Principle carriers with `## Formal statement`, using 89 distinct `\operatorname{...}` predicate names. Their local symbol declarations are written in ordinary prose; no Framework Engine parser, type checker, or solver for these statements was found. The three Bootstrap Seed units contain 416 current non-archived, non-draft Markdown carriers and none has a `## Formal statement` section.

The Bootstrap Seed is a scope-ownership chain, `METAMODEL -> SEMANTICS -> GOVERNANCE`, not one semantic Artifact kind. Its carriers span Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, and Ops roles. Therefore “formalize the Bootstrap Seed” is broader than “formalize normative claims.”

### Scope and exclusions

Included: authority ownership, representation boundaries, formal-language prerequisites, human-readable outputs, Translation-Atom admission, and likely LLM effects. Excluded: choosing a final logic or serialization, defining the full language, mutating current Atoms, migrating carriers, and claiming measured CAPRMEDIO-specific LLM improvement without a benchmark.

### Inputs, sources, and evidence

Project evidence includes `CA-R-839`, `CA-R-840`, `CA-R-810`, `CAPRMEDIO-M-087`, `CAPRMEDIO-M-088`, `CAPRMEDIO-METHODOLOGY-REQU-630`, `CAPRMEDIO-META-REQU-126`, `CAPRMEDIO-META-REQU-131`, `CAPRMEDIO-META-REQU-134`, `CAPRMEDIO-META-REQU-135`, `CAPRMEDIO-META-REQU-151`, `CA-E-210`, the 20 active Principle carriers, and the current Bootstrap Seed carrier set.

The resolved FPF edition is the local `FPF-Knowledge-Graph` in `FPF-obsidianized`. The review routed through the DESCRIPTION-USE and WORDING practical-use branches, then inspected representation change, structure-to-narrative rendering, mathematical-lens discipline, plain technical rewriting, and declarative-representation overread.

External LLM evidence is limited to primary sources: OpenAI's constrained-decoding account, the Logic-LM paper, the Faithful Chain-of-Thought paper, and the ICML 2025 grammar-constrained decoding paper.

### Authority, dependencies, and stop condition

FPF supplies review lenses, not CAPRMEDIO authority. The Operator owns the project decision. This finding stops before language design or migration. Return when the Operator selects the authority direction, when a candidate grammar and semantic kernel exist, or when a pilot changes the evidence.

Saved report: `fpf-reports/20260821T215838Z-fpf-design-challenge-formal-first-principles-and-bootstrap-seed.md`

## High-confidence results (>=95%)

### Proposal, resolved FPF source, and decision boundary

The strongest form of the proposal is: “one formal representation is the sole normative source; human-readable forms are non-authoritative representations derived from it.” That proposal is materially different from the current two-authored-representations rule. It eliminates the need to decide whether the prose or formula is “main,” but only if the formal source is genuinely parseable, typed, and semantically governed.

The proposal should not be interpreted as “all files located in Bootstrap Seed units must be formal.” Scope ownership, Content role, and representation form are independent distinctions. The decision boundary is therefore which claim kinds need formal authority, not which directories receive formal syntax.

### FPF Challenge Findings

#### 1. Formalizing by Bootstrap Seed location conflates semantic job with structural ownership — concern, 99%

- **Proposal claim and affected Entity of Concern:** every Principle and every Bootstrap Seed carrier should become purely formal.
- **Bounded context and receiving use:** selecting the canonical representation for CAPRMEDIO authority.
- **Direct FPF basis:** `C.2.P.DR:1-4` requires recovery of the actual governed object or relation before treating a declarative shape as operational or authoritative. `F.19:0-4` requires the object and claim kind to survive a rewrite instead of using a container label as ontology.
- **Project evidence:** the Bootstrap Seed is the METAMODEL, SEMANTICS, and GOVERNANCE ownership chain, while its current carriers occupy multiple Content roles. `CAPRMEDIO-META-REQU-151:15-25` also rejects new durable constructs justified only by carrier shape or location.
- **Reviewer inference:** some Bootstrap Seed claims are good formal-language candidates—definitions, relation signatures, normative constraints, cardinalities, and executable acceptance predicates. Concerns, rationale, uncertainty, alternatives, plans, evaluation findings, and reader guidance are not made safer merely by mathematical notation.
- **Consequence if unresolved:** the migration would create pseudo-formal Analysis and planning material, hide uncertainty, and make the language carry unlike claim kinds without a common semantics.
- **Candidate correction:** select formalization by claim kind and receiving use. Start with normative and definitional RMED authority, not the whole Bootstrap Seed directory tree.
- **Unchecked dependencies and return:** return after a carrier inventory maps each active Type and Content role to `formal-authority`, `structured-but-not-formal`, or `narrative`.

#### 2. The current Principle formulas are semi-formal notation, not yet a canonical formal language — concern, 99%

- **Proposal claim and affected Entity of Concern:** the existing `## Formal statement` blocks can become the sole authority.
- **Bounded context and receiving use:** immediate migration of Project Principle authority.
- **Direct FPF basis:** `C.29:4.1-4.3` says mathematical notation earns authority only for a declared use with preserved structure, declared loss, validation, and a stop boundary. `C.2.P.DR:1-4` blocks a visible formal expression from acquiring stronger force by shape alone.
- **Project evidence:** all 20 active Principles have formulas, but the scan found 89 distinct named predicates. Representative carriers define sets and functions in nearby English and then use predicates such as `CanControl`, `CurrentlyJustified`, and `SufficientFor` without a shared machine-resolved signature or interpretation. `CA-E-210` checks prose/formula equivalence through semantic review; no parser, type checker, bound-variable checker, arity checker, or solver integration was found.
- **Reviewer inference:** replacing the prose with the current formulas would remove the place where much of their meaning is actually defined. Syntactic compactness would look stricter while semantic interpretation remained informal.
- **Consequence if unresolved:** CAPRMEDIO could accept a well-formed formula that binds the wrong entities, uses a predicate inconsistently, or omits an obligation while appearing more authoritative.
- **Candidate correction:** make a typed AST or small DSL canonical only after its abstract syntax, concrete grammar, type system, predicate signatures, reference resolution, modality, scope, time/state semantics, and validation are governed.
- **Unchecked dependencies and return:** exact solver requirements and expressiveness remain open; return after a representative corpus is encoded and rejected counterexamples are executable.

#### 3. One formal semantic source plus human-readable Projections is coherent — no concern found within inspected scope, 99%

- **Proposal claim and affected Entity of Concern:** human-readable Principle and formal authority should no longer be independently authored peers.
- **Bounded context and receiving use:** resolving drift and the ambiguous “main statement” question.
- **Direct FPF basis:** `A.6.3.RT:4-4.6` treats a representation change as a source-to-target construction with explicit preservation, loss, prohibited strengthening, use, and return. `A.6.3.NAR:1-4` permits a readable sequential account derived from selected source structure while keeping omissions and unsupported connective claims visible.
- **Project evidence:** `CAPRMEDIO-METHODOLOGY-REQU-630:13-15` already requires current, non-authoritative, mechanically reproducible Projections with source identity and frontier. `CAPRMEDIO-M-088:14-16` already requires ordinary-language Operator communication.
- **Reviewer inference:** a single authoritative semantic object removes bidirectional synchronization. A human Summary, explanation, documentation page, or task-specific rendering can be derived and must point back to the exact source revision.
- **Consequence if unresolved:** continuing to author both sides preserves the current mismatch surface and makes “same meaning” a recurring human audit obligation.
- **Candidate correction:** generate readable forms from the canonical AST through deterministic templates where possible. Record source identity, source revision, renderer version, audience/use, declared omissions, and a return-to-source link.
- **Unchecked dependencies and return:** a free-form LLM explanation is not mechanically reproducible by default; its admissible use must be narrower unless the generation configuration and acceptance process are separately governed.

#### 4. A Translation Atom should not be the default derived form — concern, 98%

- **Proposal claim and affected Entity of Concern:** human-readable output should be represented as an `A/Translation` Atom instead of or alongside a Projection.
- **Bounded context and receiving use:** Artifact-model admission and authority separation.
- **Direct FPF basis:** `A.6.3.RT:4.5-4.6` separates a target representation from its source, production Work, publication, and authority. `F.19:4` treats a record or schema as apparatus unless it carries an independently material semantic value.
- **Project evidence:** no active Translation Type was found in the current Type surface. `CAPRMEDIO-META-REQU-151:15-25` requires a non-overlapping meaning and action-facing use before admitting a durable construct. `CAPRMEDIO-METHODOLOGY-REQU-630` already provides the Projection route for reproducible derived views.
- **Reviewer inference:** making every generated explanation an Atom would give disposable renderings identity, lifecycle, and governance burden without independent meaning. It would recreate the dual-authority problem if readers treated the Translation Atom as normative.
- **Consequence if unresolved:** source and translation can drift, conflict resolution becomes necessary, and the graph fills with identity-bearing copies.
- **Candidate correction:** use a Projection by default. Consider a Translation or Adaptation Atom only when it carries non-derivable, separately accepted choices—for example a locale-specific terminology decision, audience-specific loss boundary, Operator-approved interpretation, or maintained pedagogical sequence. Such an Atom must remain explicitly non-normative with source revision, applicability, loss, and return conditions.
- **Unchecked dependencies and return:** whether CAPRMEDIO has a recurring independently governed adaptation job is not yet established.

#### 5. “Formal is better for LLMs” is too broad; formal plus constraints and a solver is the supported claim — FPF not decisive, 99%

- **Proposal claim and affected Entity of Concern:** a purely formal source will reduce LLM errors.
- **Bounded context and receiving use:** LLM authoring, retrieval, validation, reasoning, and explanation over CAPRMEDIO authority.
- **Direct FPF basis:** `C.29:4.1-4.3` requires a mathematical or formal lens to change a declared use and expose preserved structure and limits; elegance alone is insufficient. `A.6.3.RT:4.5` says a more formal target does not widen reliability.
- **External evidence:** grammar-constrained decoding can guarantee membership in a context-free grammar, and OpenAI reports exact schema matching through constrained decoding. Logic-LM and Faithful Chain-of-Thought report gains from translating natural language into symbolic forms and executing them with deterministic solvers. Logic-LM also explicitly reports that executable symbolic form does not imply a correct formulation and that semantic translation remains difficult. [OpenAI Structured Outputs](https://openai.com/index/introducing-structured-outputs-in-the-api/), [Logic-LM](https://aclanthology.org/2023.findings-emnlp.248/), [Faithful Chain-of-Thought](https://arxiv.org/abs/2301.13379), [ICML 2025 grammar-constrained decoding](https://proceedings.mlr.press/v267/park25l.html).
- **Reviewer inference:** a typed DSL is better for deterministic parsing, reference checks, constrained generation, impact analysis, and solver-backed checks. Raw LaTeX with locally invented predicates is not necessarily easier for an LLM to understand correctly than controlled technical English. The best LLM interface is hybrid: ordinary-language request -> LLM semantic translation -> constrained AST/DSL -> parser/type checker/solver -> generated human explanation.
- **Consequence if unresolved:** the project may optimize syntactic validity while semantic mistranslation remains undetected.
- **Candidate correction:** benchmark the complete pipeline, not notation alone, and separate syntax validity, semantic fidelity, solver outcome, and Operator comprehension.
- **Unchecked dependencies and return:** no CAPRMEDIO-specific benchmark has compared current dual text with a candidate DSL.

#### 6. Formal-first Bootstrap Seed authority needs an explicit trusted kernel — concern, 97%

- **Proposal claim and affected Entity of Concern:** the Bootstrap Seed can define itself purely in its own formal language.
- **Bounded context and receiving use:** bootstrapping and version evolution.
- **Direct FPF basis:** `A.6.3.RT:4.5-4.6` requires endpoint schemes, preservation, loss, and source return to remain recoverable across representation changes. `C.29:4.3` keeps the formal lens bounded by its actual interpreter and use.
- **Project evidence:** the Bootstrap Seed owns metamodel, semantics, and governance—the very rules needed to interpret its carriers.
- **Reviewer inference:** every formal source depends on a parser, semantic kernel, resolver, and version-selection rule that cannot be justified only by the text they interpret. CAPRMEDIO needs a small explicit trusted base and a governed migration relation between language editions.
- **Consequence if unresolved:** a language update can silently change the meaning of the authority used to validate that same update.
- **Candidate correction:** version a minimal kernel containing grammar/AST schema, primitive sorts and operators, resolver rules, modality and scope semantics, validator version, and migration/check procedure. Make the current language edition explicit before interpreting any Atom.
- **Unchecked dependencies and return:** the boundary between native trusted implementation and governed Bootstrap Seed description still needs an Operator decision.

### Project decision

**Recommended direction:** adopt formal-first authority as a target architecture, but do not migrate to the present LaTeX blocks and do not formalize all Bootstrap Seed carriers by location.

The recommended model is:

1. One canonical typed semantic form for formalizable normative and definitional claims, beginning with Principles and selected Bootstrap Seed RMED authority.
2. Human-readable Summary, explanation, documentation, and task views as non-authoritative Projections with exact source frontier and return.
3. Controlled technical prose remains canonical where the language cannot yet express the complete meaning; partial formalization must not silently outrank it.
4. Concern, Analysis, Plan, evidence narrative, and Operator guidance remain in the representation appropriate to their job.
5. No Translation Atom by default. Admit one only for a recurring, independently governed adaptation meaning that a Projection cannot carry.

The safest first pilot is three to five Principles covering deontic authority, set constraints, state transitions, and applicability. The formal source becomes authoritative only after round-trip rendering, type checking, negative fixtures, cross-Principle consistency checks, and Operator review all pass.

### Strengths within inspected scope

- CAPRMEDIO already has the correct one-term/one-scoped-meaning direction in `CAPRMEDIO-META-REQU-126` and requires vocabulary clarification before admitting a claim in `CAPRMEDIO-META-REQU-131`.
- `CAPRMEDIO-META-REQU-134` already provides a controlled normative sentence frame that can seed the DSL's deontic AST.
- `CAPRMEDIO-M-087` already asks for the strictest syntax needed to preserve distinctions; it does not require maximum formality everywhere.
- The existing Projection rule and Operator-language Method already establish the source/view separation needed by the proposal.
- Prior human/formal mismatches supply valuable negative fixtures for a pilot.

### Unchecked claims and insufficient basis

- There is insufficient basis to select first-order logic, Datalog, SMT, a policy language, a custom DSL, or a mixed system. The project first needs an expressiveness inventory.
- There is insufficient basis to claim that all 20 Principles are completely formalizable without either losing meaning or introducing undecidable/open-world semantics.
- There is insufficient basis to admit a Translation Type; no recurring non-derivable adaptation lifecycle has been demonstrated.
- There is insufficient basis to claim lower CAPRMEDIO LLM error rates until a representative benchmark measures semantic fidelity, not only syntax.

### Return to project authority

The Operator should decide only the architecture direction now: one formal canonical source with derived readable views, conditional on building the prerequisites. The next authority-bearing decision should occur after a pilot returns the candidate language boundary, trusted kernel, non-expressible claims, validation evidence, translation-loss evidence, and LLM benchmark results.

## Open questions (confidence <95%)

### 1. Which formal language family fits CAPRMEDIO? — 85%

**Best current answer:** a small typed domain-specific AST with a readable concrete syntax is more suitable than raw first-order LaTeX. It can compile selected fragments to Datalog/SMT or procedural checks without forcing every claim into one solver.

**Missing evidence:** an inventory of required constructs: deontic modality, open-world/closed-world status, time and revision, scopes, quantification, uncertainty, priorities, graph relations, cardinalities, and executable evaluations.

**Consequence:** choosing a solver first may distort the semantics to fit its expressiveness.

**Next action:** encode 12-20 representative claims and rejected near-misses in two candidate ASTs, then compare expressiveness, decidability, readability, migration cost, and checker coverage.

### 2. Which Principle and Bootstrap Seed claims may become formal authority? — 90%

**Best current answer:** Principles, definitions, relation signatures, cardinality rules, invariants, and binary acceptance predicates are first candidates. Rationale, uncertainty, alternatives, plans, and narrative findings should not be forced into the same language.

**Missing evidence:** a Type-by-Content-role formalizability matrix over the active target set.

**Consequence:** an unbounded migration either leaves hidden natural-language semantics inside formulas or overformalizes non-normative work products.

**Next action:** classify a stable `TARGET_SET` as `formal-authority`, `structured-authority`, `narrative`, or `derived-view`, with one reason and one counterexample for each class.

### 3. Does the candidate architecture improve LLM performance for CAPRMEDIO? — 92%

**Best current answer:** it probably improves generation validity, deterministic retrieval, and checkability when grammar-constrained decoding and validators are used; it may not improve semantic translation or Operator-facing explanation by itself.

**Missing evidence:** CAPRMEDIO tasks evaluated across natural-only, current dual representation, DSL-only, and DSL-plus-generated-projection conditions.

**Consequence:** the project could reduce parse errors while increasing semantic mapping errors or token cost.

**Next action:** benchmark claim creation, relation selection, contradiction detection, impact analysis, and explanation. Score syntax validity, reference/type validity, semantic gold match, solver/check outcome, repair turns, token cost, and Operator comprehension separately.

### 4. Is a Translation Atom ever necessary? — 90%

**Best current answer:** only for a maintained adaptation whose audience-specific choices, terminology, omissions, or acceptance cannot be reproduced mechanically and materially affect use. Otherwise it is a Projection.

**Missing evidence:** at least three recurring translation cases with independent lifecycle, conflict, and reliance needs.

**Consequence:** premature admission creates a shadow authority surface; refusing it categorically could lose legitimate maintained adaptations.

**Next action:** collect real Operator-language and locale adaptations, then test them against `CAPRMEDIO-META-REQU-151`'s admission criteria.

## Skills used

- `fpf-design-challenge` — challenged the formal-first authority proposal against bounded project evidence and representation, formalization, and translation patterns.

#### FPF sources consulted (6 read; 6 used)

- `FPF-Knowledge-Graph/00-readme/02_Practical-Use Cards.md` — **used**: routed the question through description-use and wording branches.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/08_03_Episteme viewing - EntityOfConcern-preserving episteme construction/03_A.06.03.RT - Representation-Scheme Transition- EntityOfConcern-Preserving Representation-Scheme Transition.md` — **used**: governed source-to-representation preservation, loss, use, and return.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/08_03_Episteme viewing - EntityOfConcern-preserving episteme construction/04_A.06.03.NAR - Structure-to-Narrative Rendering.md` — **used**: supported readable derived narratives without authority transfer.
- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/17_29_Mathematical Lens Use/00_C.29 - Mathematical Lens Use.md` — **used**: bounded the claim that stricter mathematical notation increases correctness.
- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/00_02_Epistemic holon composition (KD-CAL)/02_P_Epistemic Precision Restoration/01_C.02.P.DR - Declarative Representation Precision Restoration.md` — **used**: prevented formal appearance from acquiring operational or authority force by shape alone.
- `FPF-Knowledge-Graph/F_The Unification Suite (U-Suite)- Concept Sets, SenseCells, and System-Role Kinds and Assignments/19_Ontology-First Plain Technical Rewriting/00_F.19 - Ontology-First Plain Technical Rewriting.md` — **used**: preserved claim kinds while separating semantic content from representation apparatus.
