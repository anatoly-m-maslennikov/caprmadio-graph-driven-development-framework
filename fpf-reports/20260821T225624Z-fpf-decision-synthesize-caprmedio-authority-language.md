## Task, scope, and boundaries

Task: decide which language approach best fits CAPRMEDIO when governed statements must have one clear meaning for humans, LLMs, and deterministic tools.

Direct answer: **use CAPRMEDIO's own controlled authority language, backed by a typed representation and a fail-closed parser. Do not use raw FPF prose or the unrelated biomedical CCE/DUC vocabulary as CAPRMEDIO's canonical language.**

Receiving use: settle the language architecture and identify the next implementation slice. This report does not modify current language authority, implement a parser, migrate Atoms, or declare `cce_1` admitted.

Current target: branch `dev`, working tree at HEAD `979b1f44da21b94ef155419b5cf4f3c96d393840`, plus extensive uncommitted changes. The language direction exists in active, non-draft carriers [CA-R-892](../.caprmedio/_02_BSEED_LAYER_2_SEMANTICS/04_requirement/CA-R-892-REQUIREMENT-BSEED_SEMANTICS--define-cce-as-the-canonical-authority-language.md) through [CA-R-899](../.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/04_requirement/CA-R-899-REQUIREMENT-BSEED_GOVERNANCE--govern-cce-version-admission-and-migration.md), supported by [CA-M-109](../.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/05_method/CA-M-109-IMPL_METHOD-BSEED_GOVERNANCE--author-cce-claims-and-derive-projections.md) and [CA-E-241](../.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/06_evaluation/CA-E-241-QA_CASE-BSEED_GOVERNANCE--validate-cce-authority-and-projections.md). This is current working-tree evidence, not proof of a committed or released state.

Decision owner: the CAPRMEDIO Operator. The current carriers already select the architectural direction. The remaining owner decision is whether to rename the language namespace before implementation.

Inputs:

- The live CAPRMEDIO language, vocabulary, projection, portability, and evaluation carriers.
- The preceding [CCE authority-profile challenge](20260821T222024Z-fpf-design-challenge-cce-authority-profile.md).
- The preceding CCE terminology harvest, which established that external “Common Conditions of use Elements” is a biomedical vocabulary and DUC is its neighboring policy-statement structure.
- The current FPF decision and decision-record patterns.

Comparison boundary:

- “No ambiguity” means every accepted authority statement produces exactly one typed interpretation under a pinned language version. It does not mean every reader will understand it immediately, and it does not prove that the statement is true, adequate, or authorized.
- Human clarity is a separate requirement. It must be evaluated through generated general-language wording, examples, and comprehension checks.
- LLM reliability must be gated by parser output and structured diagnostics. Prompting an LLM to “be precise” is not a language guarantee.

Saved report: `fpf-reports/20260821T225624Z-fpf-decision-synthesize-caprmedio-authority-language.md`

### Campaign handoff

- Campaign ID: `caprmedio-controlled-authority-language-20260821`.
- Predecessor: `fpf-reports/20260821T222024Z-fpf-design-challenge-cce-authority-profile.md`.
- Semantic frontier: the earlier proposal has changed into active working-tree requirements CA-R-892 through CA-R-899, Method CA-M-109, and Evaluation CA-E-241, all at version 1.
- Evaluation profile: unique interpretation, typed statement forms, registered vocabulary and predicate signatures, canonical serialization, projection fidelity, version admission, and fail-closed rejection. Excludes truth evaluation, legal language, arbitrary prose, and full-corpus migration.
- Existing challenge findings about declared semantics, one profile, typed forms, predicate signatures, atomicity, projections, and version admission are represented in active carriers. They are not yet verified as a working language implementation.
- New issue: the bare acronym `CCE` now demonstrably collides with “Common Conditions of use Elements.” Treat namespace resolution as an open naming decision, not as a reason to discard the architecture.
- Allowed next action: settle the namespace, then implement and evaluate one minimal parser/renderer vertical slice. Stop before bulk migration or declaring the version current.

## High-confidence results (>=95%)

### Recommendation

The best fit is a three-view, one-meaning stack:

1. **Canonical authoring view:** restricted CAPRMEDIO Controlled English with a closed grammar and registered terms.
2. **Machine interpretation:** one typed abstract representation produced by the parser and available as canonical structured data for tools and LLM context.
3. **Reader projection:** generated general English, and later other operator languages, derived from the same typed representation.

There must be only one governed meaning. The views are not three separately authored claims.

Confidence: 99%.

Evidence: the current design already requires one typed representation, one form identifier, typed fillings, one canonical serialization, round-trip equality, and non-authoritative translations. This directly matches the stated need better than the alternatives.

### Candidate and evidence readiness

| Candidate | Fit | Decision |
|---|---|---|
| Ordinary natural language, including simplified English | Easy to read, but grammar and words remain open to multiple interpretations | Use only as a derived reader projection |
| Raw FPF language | Rich semantic distinctions and valuable design guidance, but not a closed project parser grammar and expensive for ordinary readers | Use as a derivation and review source, not CAPRMEDIO authority syntax |
| External Common Conditions of use Elements plus DUC | Useful for biomedical data/sample use policies; only 20 domain terms and a simple term-rule-scope structure | Reject as CAPRMEDIO's language; its domain and statement needs are too narrow |
| ASD-STE100-style simplified technical English | Improves readability and translation consistency, but does not guarantee one formal interpretation | Optional rule set for reader projections, not canonical authority |
| CAPRMEDIO's current `cce_1` design | Project-specific forms for definitions, relations, obligations, methods, evaluations, and deliveries; typed terms; explicit logic; fail-closed validation | Select and complete |
| Structured data without controlled English | Strong machine contract, but poor as the only human authoring and review surface | Use as the parser's typed representation, not as a separate authority source |

Candidate readiness: sufficient for the architectural choice. Implementation technology and migration details remain open, but they do not change which architecture best fits the requirement.

Confidence: 98%.

### Why the current CAPRMEDIO design is the right base

The working tree already contains most of the necessary language contract:

- [CA-R-893](../.caprmedio/_01_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-893-REQUIREMENT-BSEED_METAMODEL--define-cce-claim-structure.md) requires one typed, role-specific meaning with required and optional typed fields.
- [CA-R-894](../.caprmedio/_02_BSEED_LAYER_2_SEMANTICS/04_requirement/CA-R-894-REQUIREMENT-BSEED_SEMANTICS--define-cce-1-interpretation-rules.md) defines quantifiers, obligation, prohibition, permission, Boolean operators, negation, condition order, and open- versus closed-world interpretation. Unsupported syntax has no interpretation.
- [CA-R-895](../.caprmedio/_02_BSEED_LAYER_2_SEMANTICS/04_requirement/CA-R-895-REQUIREMENT-BSEED_SEMANTICS--register-cce-1-statement-forms.md) provides distinct forms for questions, definitions, classifications, exclusions, cardinalities, relations, obligations, prohibitions, permissions, invariants, derivations, methods, evaluations, and deliveries.
- [CA-R-896](../.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/04_requirement/CA-R-896-REQUIREMENT-BSEED_GOVERNANCE--encode-cce-1-claims-canonically.md) defines exact serialization and rejects noncanonical input instead of guessing.
- [CA-R-897](../.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/04_requirement/CA-R-897-REQUIREMENT-BSEED_GOVERNANCE--register-cce-vocabulary-and-predicate-signatures.md) requires meaning-owned terms and predicates with arity, ordered participant roles, kinds, direction, cardinality, reference mode, and world assumption.
- [CA-R-898](../.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/04_requirement/CA-R-898-REQUIREMENT-BSEED_GOVERNANCE--derive-cce-summaries-and-translations.md) makes filenames, titles, and ordinary-language translations reproducible projections rather than competing authority.
- [CA-R-899](../.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/04_requirement/CA-R-899-REQUIREMENT-BSEED_GOVERNANCE--govern-cce-version-admission-and-migration.md) correctly refuses to make a language version current until its parser, renderer, migration, and positive, negative, ambiguity, round-trip, and projection evaluations pass.

This is substantially stricter than “write in FPF style.” It makes ambiguity a validation failure rather than a reviewer preference.

Confidence: 100% for the carrier content.

### Critical current-state finding

`cce_1` is designed but not yet implemented or admitted.

The active repository scan found:

- no Atom declaring `cce_version`;
- no active `cce_terms` or `cce_predicates` registry entries;
- no CCE parser, canonical renderer, or validator implementation;
- no evidence that the admission evaluation passed.

[CA-R-899](../.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/04_requirement/CA-R-899-REQUIREMENT-BSEED_GOVERNANCE--govern-cce-version-admission-and-migration.md) therefore keeps the foundation Atoms under the preceding canonical framework language until admission. The repository has a strong specification, not a running strict language.

Confidence: 100% within the inspected working tree.

### Project decision relation

Decision question: which language architecture should carry CAPRMEDIO's governed meanings while remaining clear to humans and LLMs?

Selected configuration: the project-owned controlled-English design in CA-R-892 through CA-R-899, with its typed parser representation and derived reader projections.

Rejected as canonical authority:

- ordinary or simplified natural language alone;
- raw FPF prose;
- external CCE/DUC;
- machine structure without a governed human-readable serialization.

Governing criteria:

- exactly one parser interpretation;
- explicit type, participant, quantity, modality, polarity, condition, scope, and world assumption;
- fail-closed behavior;
- deterministic round trip and projection;
- readable authoring and review surface;
- provider-neutral use by LLM harnesses;
- versioned migration and reproducibility.

Rationale: only the selected configuration combines the project's domain coverage with a formal acceptance boundary and a human-readable surface. FPF supplies distinctions; CAPRMEDIO owns its meaning. The parser supplies determinism; the LLM does not.

Status: architectural direction is present in active working-tree authority; `cce_1` implementation and admission remain incomplete. No release or committed-state claim is made.

Confidence: 99%.

### Required adjustment: remove the acronym ambiguity

The external field already uses `CCE` for **Common Conditions of use Elements**. CAPRMEDIO currently uses `CCE` for **CAPRMEDIO Controlled English**. A strict language should not begin with an avoidable global name collision.

Keep the full human name if desired, but namespace every machine identity. Recommended convention:

- display name: `CAPRMEDIO Controlled English`;
- short label: `CA-CE`;
- language namespace: `caprmedio.ce`;
- version identifier: `caprmedio_ce_1` or `caprmedio.ce/1`;
- never use bare `CCE` or bare `cce_1` outside a clearly declared CAPRMEDIO namespace.

This is a naming adjustment, not a change to the language architecture.

Confidence: 99% that a namespace is required; the exact spelling remains an owner choice.

### What “strict and clear” must mean in implementation

For deterministic tools:

- Publish a complete grammar, not placeholders such as `<typed clause>` or `<registered predicate clause>`.
- Specify tokenization, multiword-predicate matching, names, reference resolution, variable binding, Boolean grouping, and error positions.
- Parse to one typed representation. Reject zero parses and multiple parses.
- Render exactly one canonical English serialization from that representation.
- Require `parse(render(value)) = value` and `render(parse(text)) = canonical_text`.

For LLMs:

- Give the model the allowed statement form, relevant term and predicate subset, and typed structured representation schema for the current task.
- Require the model to submit text to the parser before the claim can be accepted.
- Return structured diagnostics naming the unknown token, missing field, wrong participant kind, or ambiguous scope.
- Prefer supplying the validated typed representation to later LLM calls rather than asking them to reinterpret the sentence repeatedly.

For humans:

- Show the canonical statement and one generated general-English explanation together.
- Provide short definitions and examples for registered terms.
- Test whether different readers recover the same bearer, action, target, quantity, condition, and scope.
- Treat comprehension failure as a projection or vocabulary defect even when the parser succeeds.

Confidence: 98%.

### Accepted losses and consequences

Accepted losses:

- Authors cannot express arbitrary English directly as authority.
- A new semantic shape requires a governed grammar or statement-form extension.
- Vocabulary and predicate registries require maintenance.
- Initial authoring is slower than free prose.
- Migration will reveal claims whose current meaning is incomplete or internally mixed.

Positive consequences:

- Humans, LLMs, and tools refer to one accepted meaning.
- Unknown or ambiguous language stops instead of being silently interpreted.
- Names, translations, filenames, and summaries become reproducible.
- Version changes can be migrated and audited.
- FPF terminology can be adopted selectively without making the external FPF corpus runtime authority.

Negative consequences and controls:

- Parser acceptance can create false confidence. Control: keep truth, adequacy, evidence, and authorization evaluations separate.
- A huge global vocabulary can overload LLM context. Control: retrieve only the statement form and terms relevant to the current Atom.
- Generated general English can conceal a missing semantic field. Control: mutation-test every meaning-bearing field against the projection.
- The custom language can become expensive to maintain. Control: keep the initial grammar small and reopen the decision if maintenance exceeds its measured value.

### Implementation handoff

The smallest useful implementation sequence is:

1. Decide and apply the namespaced language identifier before public use.
2. Freeze a complete grammar for three representative forms: one simple requirement, one Method, and one Evaluation.
3. Define the typed representation schema and term/predicate registry schema.
4. Implement tokenizer, parser, type checker, canonical renderer, and structured diagnostics as one vertical slice.
5. Add positive, negative, ambiguity, kind-error, Boolean-scope, reference-resolution, round-trip, projection, and byte-determinism fixtures.
6. Convert a small representative set of BSeed and Principle Atoms without making the version current.
7. Generate two projections from accepted meanings: canonical structured data for tools/LLMs and general English for readers.
8. Run blind comprehension checks: humans and at least two LLM harnesses must independently recover the same semantic fields.
9. Admit the version only through the existing CA-R-899 gate after every target passes or receives an explicit exclusion.

Do not start with bulk migration. The first deliverable is one complete parser-to-projection path with rejection evidence.

### Reopen triggers

Reopen the architecture choice when any of these occurs:

- one accepted sentence produces two typed interpretations;
- two non-equivalent typed meanings receive the same canonical sentence;
- representative CAPRMEDIO claims cannot be expressed without frequent grammar exceptions;
- general-English projections repeatedly reduce human comprehension;
- LLMs perform no better with validated structured input than with ordinary prose;
- language maintenance cost exceeds the observed reduction in defects;
- an established controlled-language implementation provides equivalent CAPRMEDIO semantics at materially lower cost.

### ADR projection

Status: selected direction in current working-tree authority; implementation not admitted.

Context: CAPRMEDIO needs governed claims that humans can review, LLMs can author and consume, and tools can interpret without guessing.

Decision: continue the project-owned controlled-English architecture. Use a closed, versioned grammar and registered typed vocabulary; compile every accepted statement to one typed representation; derive structured and general-language projections from that meaning. Use FPF as a semantic design source. Do not adopt raw FPF prose or external CCE/DUC as the canonical authority language.

Rationale: this is the only evaluated option that combines CAPRMEDIO-specific semantic coverage, deterministic validation, readable authoring, provider neutrality, and versioned migration.

Trade-offs: accept grammar and vocabulary maintenance, reduced free-form expression, and staged migration in exchange for one recoverable meaning and fail-closed ambiguity handling.

Confirmation: CA-E-241 plus parser, type, round-trip, ambiguity, mutation, projection, byte-determinism, and human/LLM comprehension evaluations.

Supersession condition: replace this choice if its controlled-language maintenance cost or coverage failures exceed its measured ambiguity reduction, or if another language meets the same semantics and validation contract with lower total cost.

## Open questions (confidence <95%)

### 1. What exact namespace should replace bare `CCE` and `cce_1`?

Best current answer: use `CAPRMEDIO Controlled English`, short label `CA-CE`, and machine identifier `caprmedio_ce_1`.

Confidence: 94% — probable, but confirmation is still needed.

Missing input: Operator naming decision and collision screening against the repository's other canonical abbreviations.

Consequence: implementing the parser before naming is settled creates avoidable migrations in frontmatter, registries, schemas, and tools.

Next action: accept this namespace or select another unique namespaced identifier before implementation.

### 2. Which representation is persisted in each Atom?

Best current answer: persist the canonical controlled-English serialization as the reviewed claim, parse it deterministically to the typed representation, and generate canonical structured data as a reproducible projection. Do not manually maintain both English and structured meanings.

Confidence: 92% — probable, but confirmation is still needed.

Missing evidence: a worked carrier prototype showing edit, diff, parser, renderer, migration, and source-return behavior.

Consequence: storing two independently editable forms would recreate the divergence the language is intended to remove.

Next action: prototype one Atom and confirm which carrier yields the clearest Git review while preserving deterministic reconstruction.

### 3. Which parsing technology should implement the grammar?

Best current answer: use a small deterministic parser generated from a declarative grammar, with a separate type-checking phase. PEG, LALR, or another deterministic approach can work.

Confidence: 80% — materially uncertain.

Missing evidence: grammar prototype, ambiguity behavior, diagnostic quality, Python portability, maintenance cost, and performance measurements.

Consequence: the wrong parser technology can make the grammar hard to evolve or errors hard for humans and LLMs to repair.

Next action: implement the same three-form slice in two small parser candidates and compare diagnostics, determinism, and code size.

### 4. How large should the first admitted vocabulary be?

Best current answer: only the terms and predicates needed by a representative BSeed/Principle pilot, not the whole repository.

Confidence: 90% — probable, but confirmation is still needed.

Missing evidence: the selected pilot target set and its extracted term/predicate coverage.

Consequence: too small a set cannot test real coverage; too large a set delays the parser and overloads authoring context.

Next action: select roughly ten structurally diverse Atoms, extract their required terms and predicates, and seal that as the v1 pilot vocabulary.

### 5. When should controlled language extend beyond BSeeds and Principles?

Best current answer: only after the initial profile is admitted and shows measured value. Other authority-bearing Atoms may need different forms and cost profiles.

Confidence: 88% — materially uncertain.

Missing evidence: defect rates, authoring cost, comprehension results, and form coverage from the pilot.

Consequence: immediate framework-wide adoption could turn a useful strict core into an expensive universal language project.

Next action: keep the initial boundary, measure it, then make a separate extension decision for each additional content role or structural scope.

## Skills used

- `fpf-decision-synthesize` — compared the recoverable candidates, identified the current project selection, separated specification from implementation, and produced the decision relation and ADR projection.

#### FPF sources consulted (2 read; 2 used)

- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/20_32_Architecture Candidate Synthesis/08_C.32.PAD - Project Architecture Decision After Candidate Synthesis.md` — **used**: required an explicit selected configuration, criteria, accepted losses, work consequences, confirmation, and reopen triggers.
- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/20_32_Architecture Candidate Synthesis/09_C.32.ADR - Architecture Decision Record Projection.md` — **used**: kept the readable decision record as a projection of the decision rather than a competing source of authority.

<oai-mem-citation>
<citation_entries>
MEMORY.md:109-115|note=[used the preference for strict internal language and general operator wording]
MEMORY.md:1177-1179|note=[used FPF evidence separation and report persistence conventions]
</citation_entries>
<rollout_ids>
019fc257-ad77-7d31-b3e2-1b6b37cc0274
</rollout_ids>
</oai-mem-citation>
