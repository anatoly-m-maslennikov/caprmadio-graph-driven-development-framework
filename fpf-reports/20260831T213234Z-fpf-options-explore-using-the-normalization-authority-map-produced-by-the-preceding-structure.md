## Task, scope, and boundaries

Explore additional CAPRMEDIO normalization candidates from the recovered normalization authority map. The receiving use is an Operator decision backlog: it compares distinct possible normalizations without selecting, approving, implementing, or creating any Atom.

Saved report: fpf-reports/20260831T213234Z-fpf-options-explore-using-the-normalization-authority-map-produced-by-the-preceding-structure.md

Baseline and authority: the active source Atom frontier in .caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL and 003_LOCAL_CONFIGURATION. Applicable Methodology is derived evidence only. The predecessor recovery reported 633 selected current source revisions, zero compilation conflicts, and two material gaps: the Claim-context semantics of X: (A, B, C) are not defined, and no check detects its cross-Atom consolidation pattern.

The Entity of Concern is the normalization boundary around one Atom Claim, one Claim Scope, Term and Subject expressions, source contributions, and their carriers. The decision owner is the Operator. The baseline means existing CA-R-771, CA-R-1270, CA-R-1358, CA-M-115, CA-M-121, CA-M-122, CA-M-224, CA-M-234, CA-M-236, CA-D-267, CA-D-268, and their evaluations remain in force.

Protected constraints are source authority, independent replaceability, one Atom/one Claim/one Claim Scope, no semantic authority for projections, no compiler Claim synthesis or merge, deterministic validation, and extension safety. Interesting candidates remove a recurring structurally identical representation without enlarging a source Claim's authority or asking a compiler or LLM to infer semantic equivalence.

Quality coordinates are evaluated separately: authority preservation; Atom-boundary preservation; deterministic validation; extension and fractal applicability; reversibility; and risk of unintended semantic merging. Novelty, mechanism diversity, and implementation cost are telemetry rather than selection criteria. The exploration budget is six materially different mechanisms. Stop after a candidate matrix and decision handoff.

Campaign handoff: no campaign identifier or finding registry was recorded by the predecessor report, so none is inferred. The predecessor is fpf-reports/20260831T212448Z-fpf-structure-recover-recover-the-current-caprmedio-normalization-system-from-active-core-meta.md. The semantic frontier is unchanged: active Core Meta-Model and Local Configuration source Claims. The carrier frontier is unchanged; this report creates only a plain non-authoritative FPF report. The evaluation profile is source reading plus candidate comparison; it excludes Atom, code, plan, compiler, and Git changes. The registered open gap fingerprints are normalization/value-set-claim-grammar and normalization/cross-atom-value-set-detection. The permitted next transition is an Operator decision followed, if needed, by a bounded decision synthesis or a separate design challenge for an accepted candidate.

Evidence used: the predecessor authority map; live source Atoms CA-R-1358, CA-R-1245, CA-M-115, CA-M-121, CA-M-122, CA-M-224, CA-R-1231, CA-R-1232, CA-R-747, CA-R-1309, CA-R-1316, CA-D-267, CA-D-268, and CA-R-806; and the resolved FPF source below. CA-R-1316 and CA-M-224 make the no-merge boundary direct source evidence, rather than a design assumption.

## High-confidence results (>=95%)

### 1. Exploration contract and resolved FPF source — 99%

The candidate set is bounded to normalizations that are authoring, model, evaluation, delivery, or tool checks. A candidate may propose deterministic detection or a non-authoritative Projection, but it may not cause Applicable Methodology compilation to merge, synthesize, or rewrite a source Claim. This follows CA-R-1316 and CA-M-224 directly.

The primary reasoning source is FPF B.5.2.1. Its contribution here is a deliberately diverse candidate set with separately visible quality coordinates and retained alternatives rather than a synthetic winner. The optional FPF parity source was not opened: this is a structural design comparison, not a benchmark or a parity claim between implementations.

### 2. CandidateSet and provenance — 98%

| Candidate | Normalized pattern | Triggering duplication shape | Safe consolidation condition | Unsafe counterexample | Proposed enforcement location | Unresolved decision |
| --- | --- | --- | --- | --- | --- | --- |
| VSC-1: Claim-side finite value-set grammar | one Claim uses X: (A, B, C) to state an unordered finite allowed-value set for one X | same Current Scope, Claim Scope, and X; separate Claims differ only in the allowed value | all values belong to one authority unit and always change together; X is one property; values have canonical identities; the list has set, not sequence, semantics | one value has a separate owner or lifecycle; value order conveys priority; one source is additive while another declares the final resolved domain | Core Meta-Model: Requirement defining Claim-context syntax; Method for authoring; Evaluation for parse, duplicate, and grouping checks. Local Configuration: formatter or linter implementation | whether an empty list is legal; whether colon is extended from Subject Expression context or Claim syntax gets another delimiter; whether list order is prohibited or merely ignored |
| VSC-2: report-only value-set consolidation detector | emit one candidate group for Claims matching the CA-R-1358 structural pattern; never rewrite sources | two or more active Claims have exact same scope coordinates and normalized X context, with one varying allowed value | exact syntactic/structural fingerprinting is available; the report preserves every source Atom ID and asks for author action | natural-language near-duplicates; semantically similar Claims with different ownership, conditions, type domains, or lifecycle; any automated archive or merge | Core Meta-Model: Evaluation rule and fixtures. Local Configuration: deterministic Tool producing a review report, not a mutation or compilation input | warning versus validation failure; candidate report carrier; the narrow initial fingerprint before a Claim parser exists |
| CCE-1: restricted Boolean-expression normal form | canonicalize explicitly parenthesized conjunction or disjunction of canonical atomic predicates by flattening, de-duplicating, and sorting operands | A and B versus B and A; redundant repeated atomic predicate; different nesting of only and/or groups | operators are pure CCE Boolean operators; operands are canonical atomic predicates; only associative and commutative operations are changed; source grouping has no independent authority | implication, negation distribution, temporal operators, quantifiers, where, unless, or a new extension operator whose laws are not registered | Core Meta-Model: CCE Method plus Evaluation. Local Configuration: optional formatter and duplicate-candidate Tool | whether source grouping should remain preserved as author style even when it is semantically equivalent; exact canonical sort key |
| SCOPE-1: restricted Scope Expression set normal form | canonicalize a finite union or intersection of exact atomic identities as a sorted duplicate-free grouped set | A or B versus B or A; repeated identity inside one finite composite Claim Scope | only exact stable Entity or Atom-ID references; only union/intersection; the same resolution frontier; no dynamic selector or exclusion | without is directional; all ENTITY_KIND and where are context-sensitive selections; a dynamic Scope Expression can change as the Project changes | Core Meta-Model: Scope Expression Method and Evaluation. Local Configuration: resolver formatter or lint report | whether scope source text is preserved as written or revised into normal form; canonical identity order |
| REG-1: additive allowed-value contribution Projection | derive one non-authoritative resolved allowed-value set from explicitly additive source contributions to the same complete Type Subject | Core, Local Configuration, or a selected Extension each contributes values to the same Type domain | each source declares an additive contribution for the same complete Subject Path; source frontier is exact; projection records source revisions and unique values; the Projection cannot modify source Claims | a Claim says it defines the final complete value domain; a source removes or replaces a value; two same-spelled values have different defined Terms; unselected Extension values leak in | Core Meta-Model: contribution and resolution semantics, source-lineage Evaluation, Projection Delivery. Local Configuration: selects sources and invokes the builder | whether existing Core contribution wording is explicitly additive; duplicate-value conflict policy; how a removal is represented without source Claim merge |
| COL-1: explicit set-valued carrier field normal form | every declared set-valued carrier field serializes unique canonical values in one declared deterministic order; sequence fields preserve order | the same relations, subjects, or contribution values appear in a different order or with a duplicate | field metadata says it is unordered; every member has a canonical target or value serialization; ordering is carrier-only | Journal records, task work sequence, an ordered relation, or an extension field with order-sensitive semantics | Core Meta-Model: extend Relation Kind or field metadata with collection shape; Delivery serializer and Evaluation. Local Configuration: formatter and check implementation | whether all relation-target collections are sets; whether collection shape belongs in CA-R-806 metadata or a separate field registry |

VSC-1 and VSC-2 directly address the two recovered gaps. CCE-1 and SCOPE-1 normalize different languages: one constrains Boolean Claim conditions and the other constrains Claim Scope selection. REG-1 normalizes derived domain resolution across extensible sources. COL-1 is carrier-only normalization and deliberately requires an explicit ordered-versus-unordered declaration.

### 3. Declared-coordinate evaluation and diversity map — 97%

| Candidate | Authority and Claim boundary | Deterministic validation | Extension and fractal fit | Reversibility | Semantic-merge risk |
| --- | --- | --- | --- | --- | --- |
| VSC-1 | preserves one source Claim only after the author verifies common lifecycle | high after grammar definition | high because the rule applies at every Scope Unit and source layer | high: one source revision can replace the old Claim group | low only under its narrow same-X condition |
| VSC-2 | preserves all source Claims and creates no new authority | high for an exact fingerprint | high: one generic Tool can inspect any selected source frontier | very high: reporting only | none from the Tool itself |
| CCE-1 | preserves boundaries when restricted to canonical atomic predicates | moderate until the exact permitted grammar subset is governed | high for Claims in all Scope Units | high: authoring rewrite only | low in the restricted subset; high outside it |
| SCOPE-1 | preserves Claim Scope membership only for static identity sets | high for the narrow static subset | high for any Scope Unit with composite Scope | high: source text can be revised without topology change | low in the narrow subset; high for dynamic selectors |
| REG-1 | keeps contribution Claims separate and makes only the resolved index derived | high once contribution polarity is explicit | highest for selected Extensions and Local Configuration | high: rebuild from source frontier | low if additive and final-domain Claims are distinct |
| COL-1 | does not change Claim or relation meaning when a field is declared a set | high after field shape is explicit | high for new extensions; conditional for legacy fields | very high: carrier-only | none for declared sets; unacceptable for sequences |

No single candidate dominates the others. VSC-1 is the semantic prerequisite for the accepted value-set Claim shape. VSC-2 is the lowest-risk enforcement increment. CCE-1 and SCOPE-1 reduce representation variance in separate evaluators. REG-1 solves extensible-domain resolution without Claim merge. COL-1 reduces carrier churn after collection shape is explicitly modeled.

### 4. Parity plan/report — 99%

No parity plan or report applies. The comparator is the recovered active authority frontier, not another implementation or benchmark edition. Comparison uses the six declared design coordinates above, with the baseline fixed to the predecessor report's current source frontier. The conditional parity method is therefore not applicable and was not used.

### 5. Retained options, exclusions, and evidence gaps — 98%

All six candidates are retained as distinct mechanisms. The following are excluded from this exploration because they would exceed current authority or lack a safe equivalence basis:

- compiler-side Claim merge or synthesis: prohibited by CA-R-1316 and CA-M-224;
- LLM-based semantic duplicate detection: not deterministic and prohibited as compilation conflict resolution;
- unrestricted logical equivalence, including De Morgan rewrites, implication rewrites, temporal rewrites, and quantifier rewrites: current CCE authorities do not govern a complete equivalence calculus;
- cardinality-range consolidation: lower and upper bounds may be independently replaceable and do not satisfy CA-R-1358's same-X, one-varying-allowed-value condition;
- source authority inferred from Summary or any other Projection: prohibited by CA-R-1272 through CA-R-1274;
- sorting every YAML list by default: ordered Journal and workflow carriers are explicit counterexamples.

The live evidence also shows an adjacent, already governed normalization rather than a new candidate: CA-D-267 forbids duplicate frontmatter where canonical address already derives a property, and CA-D-268 already requires unique canonical direct-relation targets. Those authorities should be enforced, not duplicated with another policy.

### 6. Stop condition and decision handoff — 99%

The Candidate Exploration Pack is complete: it identifies six non-cosmetic mechanisms, compares them using declared coordinates, preserves source authority, and records the unsafe boundaries. No candidate is selected or approved.

The next allowed action is for the Operator to select a bounded candidate or a small compatible package. If the selected package contains VSC-1, resolve its delimiter and empty-set semantics first. If it contains REG-1 or COL-1, resolve the source-contribution and collection-shape decisions first. Then route the accepted proposal to $fpf decision synthesize or a bounded design challenge before creating Atom changes.

## Open questions (confidence <95%)

1. **Claim-side value-list syntax — 90%.** Best current answer: retain X: (A, B, C) only after an explicit Claim-context meaning is added. CA-R-1245 currently limits colon to one allowed-value relation in a Subject Expression, while CA-R-1358 uses colon in a Claim. Missing input: whether parentheses mean an unordered non-empty finite set, and whether empty sets are legal. Consequence: a parser or linter cannot safely validate VSC-1. Next action: decide the Claim-side value-list grammar and its relationship to Subject Expression syntax.

2. **Contribution polarity for extensible Type domains — 92%.** Best current answer: distinguish additive source contributions from a final resolved allowed-value domain and derive only the latter. Existing Core Claims use the phrase Core contribution, and CA-R-1284 says Type domains are expandable, but no recovered Atom gives contribution polarity or overlap/removal rules. Consequence: REG-1 could accidentally make a closed domain open or treat a replacement as a union. Next action: inspect the intended extension replacement model and choose additive, final, and removal contribution forms.

3. **Ordered versus unordered relation and frontmatter collections — 90%.** Best current answer: normalize only fields expressly declared set-valued. CA-R-806 registers relation cardinality and ordering domain, but no recovered authority states collection order semantics. Consequence: COL-1 cannot safely sort legacy relation lists or extension fields. Next action: decide whether collection shape becomes required Relation Kind metadata and identify the initial set-valued fields.

4. **Canonical expression source form — 88%.** Best current answer: restrict CCE-1 and SCOPE-1 to a mechanically proved static subset. CA-M-121 and CA-M-122 define individual operator evaluation, but no full syntax or equivalence normal form was recovered. Consequence: generalized formatting could change an extension-defined expression or conceal source grouping. Next action: choose whether expression normalization is authoring guidance only, evaluator rejection, or a formatter suggestion; then specify the exact rewrite subset.

## Skills used

- $fpf options explore — generated and compared the read-only normalization candidates from the recovered authority map.

#### FPF sources consulted (1 read; 1 used)

- FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/04_05_Canonical Reasoning Cycle/02_Abductive Loop/02_B.05.02.01 - Creative Abduction with NQD.md — **used**: kept distinct candidate mechanisms, visible quality coordinates, and retained alternatives without selecting a winner.
