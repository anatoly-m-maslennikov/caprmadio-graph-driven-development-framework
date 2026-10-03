# FPF Challenge Finding: CCE authority profile for BSeeds and Principles

## Task, scope, and boundaries

### Proposal

Make CAPRMEDIO Controlled English (CCE) the canonical formal language for authority-bearing BSeeds and Principles, while treating ordinary human-readable wording, documentation, and filename summaries as derived projections. Make CCE stricter than the current requirement-sentence convention, but retain an English surface rather than mathematical notation.

### Source and bounded target

The bounded target is the proposed CCE language contract, especially its use for BSeed and Principle statements. Current local evidence includes:

- `CAPRMEDIO-META-REQU-134`, which already restricts requirements to bearer, modality, observable predicate, optional target, and applicability;
- `CAPRMEDIO-META-REQU-126`, `CAPRMEDIO-META-REQU-131`, and `CAPRMEDIO-META-REQU-135`, which require canonical vocabulary, exact terms, and context-complete minimal prose;
- `CA-R-839`, `CA-R-840`, and `CA-R-810`, which currently make human-readable and formal Principle statements co-representations and require a general-English Principle Summary;
- `CA-R-855`, which constrains Principle meaning by Content role;
- `CAPRMEDIO-METHODOLOGY-REQU-630`, which already supplies the right non-authoritative, mechanically reproducible projection model.

The checkout has extensive unrelated in-progress changes. This review does not modify BSeeds, Principles, tooling, or current migration work. It adds only this report.

### Decision boundary

This report evaluates whether stricter CCE is desirable and proposes a minimum authority profile. It does not accept CCE as project authority, settle its exact grammar, migrate existing atoms, or claim that a parser exists. Those decisions remain with the project operator.

### Verdict

Adopt a single strict **CCE Authority Profile**, not separate loose and strict CCE dialects. Its target should be deterministic formal semantics comparable to the `P^5` class in Kuhn's controlled-natural-language classification: fully formal syntax and semantics, one mechanically derivable meaning, and rigorously defined consequences. A documentation-oriented controlled language such as ASD-STE is useful evidence for lexical and sentence-level clarity, but it is not sufficient authority semantics by itself. See the [controlled-natural-language survey](https://doi.org/10.1162/COLI_A_00168), [ACE construction rules](https://attempto.ifi.uzh.ch/site/docs/ace_constructionrules.html), [ACE interpretation rules](https://attempto.ifi.uzh.ch/site/docs/ace_interpretationrules.html), and [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf).

## High-confidence results (>=95%)

### Findings

1. **Result: concern. Confidence: 99%.** “More strict” is not sufficient unless CCE has declared semantics. A restricted vocabulary and sentence template can improve consistency while still permitting several meanings. CCE authority needs a grammar, typed vocabulary, interpretation rules, and a canonical abstract representation. FPF `C.2.3` makes the same distinction: controlled narrative is lower-formality than explicit typed predicates or invariants, and surface notation alone does not raise formality.

2. **Result: no concern. Confidence: 99%.** One strict authoritative CCE plus derived ordinary-language projections is coherent. It removes the present possibility that the “main” statement and the “formal” statement diverge. FPF `E.10` supports stable technical vocabulary with Plain wording kept outside normative constraints; FPF `F.19` requires a kind-preservation and loss check for any plain rewrite.

3. **Result: concern. Confidence: 99%.** One universal requirement-shaped sentence template is too narrow for all BSeeds and Principles. Definitions, classifications, cardinalities, permissions, invariants, derivations, methods, and evaluation criteria have different semantic shapes. They need one language with several typed statement forms, not one grammatical mold and not several languages.

4. **Result: concern. Confidence: 99%.** Surface restrictions without predicate signatures create false formality. Every admitted predicate must declare its subject kind, object kinds, arity, direction, polarity behavior, and applicability. FPF `A.6.5` specifically warns that declaration notation cannot recover a missing relation ontology and requires exact participant typing only after the direct relation and its predicate are known.

5. **Result: no concern. Confidence: 98%.** BSeed layers should own different parts of CCE without redefining one another:

   - **METAMODEL** owns abstract syntax: statement kinds, slots, cardinalities, and structural composition.
   - **SEMANTICS** owns the meanings of terms, predicates, modalities, quantifiers, negation, identity, and each statement form.
   - **GOVERNANCE** owns concrete tokens, canonical serialization, parser and validator obligations, version pinning, and projection rules, including filename summaries.
   - **Framework Engine** implements these accepted contracts; implementation does not define their meaning.

6. **Result: concern. Confidence: 98%.** Principles need explicit atomicity discipline. “One Principle, one invariant” does not necessarily mean “one sentence.” An invariant may require several inseparable clauses. CCE should allow a canonical clause group only when all clauses jointly express one independently replaceable invariant; otherwise the content must be split into separate Principles. FPF `F.19` supports splitting heterogeneous claims instead of inventing a false common head.

7. **Result: concern. Confidence: 99%.** Current formulations such as “for which a faithful formalization is possible” must not survive in authoritative CCE. They leave admission to an unstated judgment and permit partial formalization. A carrier either parses completely under its pinned CCE version or it is not yet CCE authority.

8. **Result: no concern. Confidence: 99%.** Filename text can be a deterministic CCE projection but must not be canonical authority. It should be generated from selected semantic slots, with fixed omission, normalization, maximum-length, and collision rules. This is consistent with the existing CAPRMEDIO projection discipline.

### Recommended CCE Authority Profile v0.1

1. **One canonical representation.** Every authoritative CCE statement parses to one typed abstract syntax tree. Exactly one canonical CCE serialization is rendered from that tree. Require the round trip `parse(render(AST)) = AST`.

2. **Fail closed.** An unknown term, undeclared predicate, invalid participant kind, unresolved reference, unsupported construction, or ambiguous parse rejects the statement. The parser must never guess.

3. **Closed function vocabulary.** Reserve and define the meanings of `MUST`, `MUST NOT`, `MAY`, `EVERY`, `NO`, `AT LEAST ONE`, `AT MOST ONE`, `EXACTLY ONE`, `AND`, `OR`, `IF`, `THEN`, `WHEN`, `FOR`, `WITHIN`, `IS`, and `IS NOT`. `MAY` means permission only, never possibility.

4. **Typed content vocabulary.** Every noun term denotes one registered kind or individual. Every verb phrase denotes one registered predicate with arity, ordered participant roles, participant kinds, direction, and applicability. Synonyms may exist only in Translation projections.

5. **Typed statement forms.** Start with a small closed family:

   - definition: `<Term> MEANS <Definition>`;
   - classification: `EVERY <A> IS A <B>`;
   - cardinality: `EVERY <A> HAS EXACTLY ONE <B>`;
   - obligation or permission: `<Bearer> MUST | MUST NOT | MAY <Predicate> <Target> [WHEN <Condition>] [WITHIN <Scope>]`;
   - invariant: `FOR EVERY <A>, <Predicate> MUST HOLD`;
   - derivation: `<Projection> MUST BE DERIVED FROM <Source> BY <Registered Method>`;
   - evaluation: `<Evaluation> PASSES IF <Predicate>` and `<Evaluation> FAILS IF <Predicate>`.

   Add a new form only when an existing form cannot preserve an independently needed semantic distinction.

6. **Explicit quantification.** Forbid bare plural subjects and unstated cardinality. Use only registered quantifiers. Define `OR` as inclusive; use `EXACTLY ONE OF` for exclusive alternatives.

7. **Explicit Boolean scope.** Forbid `and/or`. Do not mix `AND` and `OR` in one clause without an explicit supported grouping form. Prefer one logical clause per CCE sentence.

8. **Restricted negation.** Admit only scoped `MUST NOT`, `NO`, and `IS NOT` forms initially. Forbid double negatives, `unless`, and `not every` until their semantics are explicitly added.

9. **No implicit reference.** Forbid pronouns, anaphora, ellipsis, and context-dependent demonstratives such as `this`, `that`, `it`, and `they`. Use canonical terms or Atom references.

10. **No hidden actors or predicates.** Prefer active voice. Forbid nominalizations or passive forms that omit the bearer, actor, target, or direct relation. A grammatical verb does not by itself establish a Method, Work, agency, or relation kind.

11. **Explicit applicability and state.** Conditions, scope, state, version, temporal boundary, exception, and tolerance must be explicit whenever they change truth or action. Define whether each predicate uses open-world or closed-world reasoning; default absence should mean unknown, not false.

12. **Direct relations only.** Store one declared relation direction. Derive inverse readings mechanically. Similar labels do not establish identity or a relation.

13. **No semantic defaults hidden in prose.** A canonical address may supply registered carrier facts such as BSeed layer or Content role, but the parsed semantic object must expose those facts. No other meaning may be inferred from folder, filename, typography, or author convention.

14. **Versioned language contract.** Every authoritative statement pins a `cce_version` or inherits one through an explicit governed rule. Grammar and vocabulary changes require compatibility classification and migrations.

15. **Projection verification.** Human-readable text and filename summaries are generated or checked against the canonical AST. A projection must preserve identity, polarity, quantity, predicate participants, applicability, and other action-guiding distinctions; it remains non-authoritative.

### BSeed-specific application

- Use CCE for the claim body of authority-bearing BSeeds, not necessarily for rationale, examples, evidence, or explanatory notes.
- Require each BSeed statement to use the semantic form appropriate to its Content role. Do not force a Method or Evaluation into an obligation form merely to reuse the Requirement grammar.
- Keep each cross-layer assertion in its owning layer. For example, METAMODEL may define that a statement has a `Predicate` slot; SEMANTICS defines what that predicate means; GOVERNANCE defines how its token is serialized and validated.
- Require cross-layer dependencies to be explicit relations rather than duplicated natural-language explanations.

### Principle-specific application

- Require one canonical CCE invariant or one justified CCE clause group per Principle.
- Require the parsed content to expose the Principle bearer or subject, claim kind or modality, predicate, participants, quantifier, polarity, and applicability.
- Keep Content-role constraints semantic. Do not require every Requirement Principle to contain the literal word `provide`, or every Method Principle the same surface phrase.
- Reject partial formalization. If the full Principle meaning cannot yet be expressed in accepted CCE, retain it outside CCE authority and open a vocabulary or grammar extension proposal.

Example migration:

```text
Current:
CAPRMEDIO must preserve information necessary for governed use, expose only the
currently justified sufficient set for the task, and keep unexposed preserved
information recoverable.

Candidate CCE clause group:
C1. CAPRMEDIO MUST preserve EVERY Information Item that is necessary for a Governed Use.
C2. FOR EVERY Task, CAPRMEDIO MUST expose EXACTLY ONE Information Set that is justified and sufficient for the Task.
C3. CAPRMEDIO MUST keep EVERY preserved Information Item that is not exposed to the Task recoverable.
ALL OF C1, C2, AND C3 MUST HOLD.
```

This example is intentionally a language-design test, not accepted CCE. It exposes unresolved vocabulary (`necessary`, `justified`, `sufficient`, and `recoverable`) that must become registered predicates or evaluation-backed terms before the Principle can be formal authority.

A simpler BSeed example is already close to admissible CCE:

```text
EVERY active Principle MUST have EXACTLY ONE Canonical CCE Statement.
EVERY Human-readable Principle Projection MUST be derived from the Canonical CCE Statement of that Principle.
```

### Strengths preserved

- English remains readable and authorable by LLMs and humans.
- Canonical vocabulary, modality, minimal prose, and projection discipline already present in CAPRMEDIO become foundations rather than discarded work.
- Formal authority no longer depends on maintaining two manually authored equivalent statements.
- LLM output becomes easier to constrain and validate because invalid language fails mechanically; however, parser acceptance proves well-formed meaning, not truth, adequacy, evidence, or project acceptance.

### Project decision

Recommended operator decision: accept the direction **“one CCE Authority Profile with typed formal semantics and derived human projections”**, then specify only the minimum v0.1 forms needed to migrate a small representative set of BSeeds and Principles. Do not bulk-migrate until a parser, canonical renderer, vocabulary registry, negative tests, projection tests, and round-trip tests exist.

## Open questions (confidence <95%)

1. **Confidence: 92%.** Should a Principle be allowed to contain a clause group, or must every clause become a separate Principle linked by an explicit composition relation? Decide using independently replaceable meaning, not sentence count.

2. **Confidence: 90%.** Which predicates are open-world and which are closed-world? This must be settled before absence, completeness, exclusivity, and validation claims have deterministic consequences.

3. **Confidence: 88%.** What are the exact semantic forms for Method and Evaluation Principles? Obligation grammar is clearly suitable for Requirements, but reusing it everywhere could collapse “how,” “what must hold,” and “how conformance is decided.”

4. **Confidence: 90%.** Which carrier facts may be derived from canonical address without appearing in the sentence? The AST should expose all inherited facts, but the project must decide whether the concrete CCE serialization must repeat them.

5. **Confidence: 92%.** Should CCE v0.1 permit relative clauses such as `that is necessary for`, or require named predicates and shorter clauses? The stricter latter option improves normalization but increases vocabulary and Atom count.

6. **Confidence: 90%.** Does the filename projection include bearer, predicate, and target only, or also polarity and quantifier when they distinguish otherwise colliding claims? This needs corpus testing against actual filenames.

### Unchecked

- No CCE grammar, parser, AST schema, or vocabulary registry was implemented or executed.
- No full corpus migration or ambiguity benchmark was run.
- The candidate clause examples were not type-checked.
- No decision was made about a logic substrate, inference regime, or proof level beyond deterministic CCE semantics.
- External controlled-language references were used as architectural evidence, not adopted wholesale.

### Return authority

The project operator decides whether to accept this direction, the atomicity rule, the inference regime, and the v0.1 grammar. Accepted semantics belong in BSeed METAMODEL and SEMANTICS authority; accepted serialization and validation rules belong in BSeed GOVERNANCE; implementation and conformance evidence belong in the Framework Engine and Evaluation loci.

## Skills used

- `fpf-design-challenge`
- Exact FPF sources consulted:
  - `00-readme/02_Practical-Use Cards.md` (`WORDING` route)
  - `E.10 - Unified Lexical Rules for FPF`
  - `C.2.3 - Unified Formality Characteristic F`
  - `A.6.5 - Relation-Declaration Slot Discipline`
  - `F.19 - Ontology-First Plain Technical Rewriting`
