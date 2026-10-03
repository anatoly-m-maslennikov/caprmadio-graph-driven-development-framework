# Task, scope, and boundaries

Yes, OOP could be useful here, but **an entity-based foundation does not imply one Python class per Entity kind**. CAPRMEDIO's governed Entity kinds define identities, bearers, and graph-qualified relations; Python classes would be a choice about where implementation state and behavior live. The current direct PROGRAMMATIC Methods already make that choice conditional: use functions for deterministic transformations (`CA-M-157`), objects for owned state, invariants, resources, lifecycle, or replaceable adapters (`CA-M-158`), typed contracts at replaceable boundaries (`CA-M-159`), and explicit separation of decisions from effects (`CA-M-160`). None establishes a blanket class-per-kind rule.

This is the final read-only analysis of the approved two-step Plan, for a possible later architecture decision. It consolidates only the validated current-state recovery and option exploration. The baseline is a **working-tree snapshot**: relevant direct Methods are active-path but uncommitted, and a sampled generator/Atom schema mismatch remains unresolved. This analysis created or changed no project file, governed Atom, implementation, or benchmark. The comparison does not select or rank an architecture, claim deployed-runtime equivalence, or turn the compact PROGRAMMATIC Methods **projection** into authority. Stop state: `COMPLETE` for the approved analysis; no approved step remains.

The installed settings request one plain report. Its workspace-relative destination below is reserved as the planned **exclusive-create** target; it is not a claim that the durable report already exists. The manager may create it only after this final artifact passes validation and must read back identical content.

Saved report: fpf-reports/20260917T190515Z-fpf-composition-entity-foundation-versus-oop.md

### Composition receipt

- Exact invocation: `if our foundation is entities, then maybe OOP can be better? each entity is a class, etc`
- Selected profile: `none`.
- Requested sequence: 1. `$fpf structure recover`; 2. `$fpf options explore`.
- Executed prefix: both steps, in order. Step 1's current-state map and step 2's three-option comparison each passed independent validation on attempt 2. Unexecuted suffix: none.
- Typed edge `structure-recover` → `options-explore`: **passed** for a bounded qualitative comparison. The validated carrier-backed as-is map was the producer output and the option baseline/change boundary was the consumer input. The required structure evidence was sufficient, so `STOP_NO_OPTION_BASIS` did not fire; the edge did not supply runtime, quantitative, or selection evidence.
- Final state: `COMPLETE`; no graph-declared stop. No further transition or project mutation is authorized by this Plan.
- FPF context ledger: 3 direct pages read, 3 used, 0 screened only, 0 deferred. Conditional `G.9` was skipped because this was not a benchmark or parity exercise.
- Carried IDs: issue `I-001`; no fix IDs; gaps `G-001`, `G-002`, `G-003`, `G-004`.

# Issues, weak points, and improvements

### Native result

#### 1. Recovered structure and evidence boundary

The Core Meta-Model distinguishes `Entity` from Action and Process identities (`CA-R-1248`), Primary from Dependent Entity and Property (`CA-R-1191`–`CA-R-1193`), and narrower kinds such as Artifact, Actor, Structural Entity, Scope Unit, and Atom Collection (`CA-R-1249`, `CA-R-1250`, `CA-R-1376`, `CA-R-1257`, `CA-R-1378`, `CA-R-1261`). The taxonomy is open and can have multiple direct `NARROWER_THAN` parents (`CA-R-1244`); it is **not** by itself a Python inheritance hierarchy. An Atom is the smallest independently governed Artifact and owns one independently replaceable Claim (`CA-R-655`, `CA-R-918`). Each Atom has one direct `GOVERNS` target and may have `DEPENDS_ON` targets; its Subjects links point to canonical target identities, without copying targets or creating a new Subject identity per link (`CA-R-1201`, `CA-R-1198`, `CA-R-1194`). `IS_BORNE_BY` and graph-qualified relation meanings add constraints that a class tree alone cannot express (`CA-R-1260`, `CA-R-1246`).

The direct PROGRAMMATIC `05_method/` directory had 23 active Method Atom files in the validated step-1 snapshot; full bodies were inspected for `CA-M-157`–`CA-M-160`, while the other direct Methods were mapped at file/title level. Sampled Python uses generic technical records—`Atom`, `AtomCarrier`, `SubjectRelation`, `Candidate`, and `Approval`—plus parsing, validation, projection, serialization, and effect-boundary functions. This is **not** a complete inventory of every runtime class or an audit of Method conformance. The compact Methods file was used only as a non-authoritative projection for navigation.

| Selected current structure | Constituent and obtaining relation | Boundary/interface |
| --- | --- | --- |
| Governed identity model | Entity kinds, bearer constraints, Atom/Claim identities, direct Subjects links, and graph-qualified relation meanings live in active Atom claims. | Markdown Atoms are authoritative carriers; term names do not instantiate Python classes. |
| Derived graph view | Atom IDs, relation kind/direction, subject paths, target identity, and source revision can be projected from current Subjects. | Projection is a navigational view, not another identity or authority source. |
| Sampled Python implementation | Generic records carry parsed Atom and relation data; functions parse, validate, project, serialize, and manage effect boundaries. | Inspected code is a sample, not a complete runtime architecture map. |

**Evidence labels:** direct observations are the cited active claims, the 23 Method files and four inspected Method bodies, and sampled Python code. The supported inference is only that the entity taxonomy does not *entail* a class-per-kind implementation. Whether classes would improve outcomes is untested. The parser/frontmatter mismatch is a static dispute about current graph generation, not a proven runtime failure. Missing structure includes full caller/class coverage and admission/release status.

Static inspection found that the sampled Entity Graph parser/test fixture expects nested `continuant`/`occurrent` subject blocks while sampled current active Atoms use flat `governs`/`depends_on` fields. That limits use of this generator as a verified current graph; no runtime compatibility test was performed. The active Method carriers' uncommitted state further limits claims about governed admission or released behavior.

#### 2. Exploration contract and distinct hypotheses

The question is interpreted as one class per **Entity kind**, not a new Python class for every individual Entity occurrence. The receiving use is a later owner decision; the operator is the likely decision owner, while a separate evaluator and selection authority were not designated. An option is interesting here only if it changes where identity, behavior, relations, or persistence are owned relative to the inspected generic-record/function baseline—not merely class names. The four comparison coordinates are change locality, relational-rule preservation, extensibility, and Markdown/graph persistence. Protected boundaries are canonical Entity/Action/Process identities, direct graph-qualified relations, one authoritative relation declaration, Atom/Claim distinctions, Markdown Atom authority, and non-authoritative projections. The exploration budget and stop criterion are three materially different mechanisms from the validated checkout, without implementation or ranking. Admissible risk here is uncertain read-only design conjecture, **not** mutation, deployment, or untested equivalence; implementation risk tolerance is unknown. Cost is bounded to exploring three shapes; implementation, migration, and maintenance costs are unmeasured. This analysis is reversible because it applies no change; a later decision must assess serializer, validator, and caller rollback cost. The evidence horizon is the sampled working-tree snapshot and prospective engine evolution; no decision deadline, release window, or migration horizon was supplied. The direct methodological source for candidate exploration is `B.5.2.1`.

| Hypothesis | Mechanism | Distinctive trade-off |
| --- | --- | --- |
| `H-01` — entity-kind classes | Python classes for kinds such as Artifact, Actor, Property, or Scope Unit own applicable behavior/invariants; a registry and serializer map instances to canonical Atom and graph carriers. Inheritance would follow only proven substitutability, not every `NARROWER_THAN` edge. | Can colocate kind-specific behavior, but cross-kind relation rules, serializers, and multiple-parent terms may require coordination across classes. |
| `H-02` — graph/data-first | Generic identity and direct-relation records remain canonical in code; explicit functions/services parse, validate, query, project, and persist them. Objects own technical state only when warranted. | Keeps shared relation predicates and persistence mapping explicit; behavior-specific variation may expand dispatch or service code. |
| `H-03` — selective domain objects | Keep canonical generic graph records, then introduce a focused object where a bounded responsibility actually owns state across calls, an invariant, resource/lifecycle, or replaceable adapter, with an explicit typed contract. | Localizes genuinely owned behavior without forcing every term into a class, but requires care at the record/object boundary. |

`H-01` comes from the operator's OOP proposal; `H-02` from the sampled generic records/functions and `CA-M-157`/`CA-M-160`; `H-03` recombines that baseline with the conditional object and typed-boundary rules in `CA-M-158`/`CA-M-159`. The diversity axes are behavior location, object identity ownership, extension mechanism, and persistence mapping. Relative to sampled code, novelty is highest for `H-01`, lowest for `H-02`, and conditional for `H-03`; novelty is exploration telemetry, not a selection criterion. These are **alternative architecture hypotheses, not fixes** and not claims of existing full conformance. A class per individual Entity instance, automatic inheritance for every term edge, or an ORM/generated graph replacing Markdown/Atom authority is outside the established basis.

#### 3. Comparison on the declared coordinates

| Coordinate | `H-01` classes | `H-02` graph/data-first | `H-03` selective objects |
| --- | --- | --- | --- |
| Change locality | Kind behavior can be local; relation changes may cross classes and serializers. | Shared relation logic can be central; special behavior needs explicit dispatch. | Owned behavior is local; shared rules stay in the graph layer. |
| Relational rules | Object references/inheritance alone do not enforce direct, graph-qualified edges or single authority. | Direct edge records and predicate validators closely match the recovered rules. | Same canonical edges as `H-02`, with objects enforcing only owned invariants. |
| Extensibility | A new kind may need class, registry, serialization, and dispatch changes; multiple parents need deliberate mapping. | Generic kinds can stay data-level; variation may grow dispatch tables. | Generic kinds stay data-level; new owned behavior adds a bounded object/contract. |
| Persistence | Every class needs a lossless Atom/ID round-trip without making in-memory state authoritative. | Generic records align with the inspected file/projection boundary; persistence rules must stay explicit. | Records persist and selected objects are reconstructed at named boundaries; mapping/lifecycle tests matter. |

These are mechanism-based expectations, **not measured outcomes**. No representative common workload, normalized scale, matched implementation result, or cost data was supplied, so no dominance, Pareto front, performance claim, or “OOP is better” verdict is justified. All three options remain live and unranked. A future comparison could hold one authority snapshot fixed and try the same changes—new compatible Entity subkind, new graph-qualified direct relation, Atom-ID/Markdown round-trip, and one stateful lifecycle—while recording touched carriers, invariant failures, persistence behavior, migration effort, and rollback cost. That would be separate owner-authorized work, not a hidden third step of this Plan. `G.9` parity/benchmark analysis was conditional and not executed.

#### 4. Verification, residual risk, and successor condition

The validated as-is map supports comparing responsibility allocation; it does not verify runtime compatibility, repository-wide class coverage, or comparative maintainability. No implementation or test was run for these three hypotheses. Before using a generated graph in an experiment, resolve `I-001`/`G-001`; before treating direct Methods as released policy, resolve `G-002`; before estimating migration size, resolve `G-003`; before selecting a winner, resolve `G-004`. No project architecture decision follows automatically from this analysis.

Representative source carriers: [Entity definition](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1248-CORE_META_MODEL-CORE-REQUIREMENT--define-entity.md>), [Atom Subjects](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1198-CORE_META_MODEL-CORE-REQUIREMENT--define-atom-subjects.md>), [function Method](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-157-PROGRAMMATIC-CORE-METHOD--allocate-deterministic-transformations-to-functions.md>), [object Method](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-158-PROGRAMMATIC-CORE-METHOD--allocate-owned-state-and-lifecycle-to-objects.md>), [typed-boundary Method](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-159-PROGRAMMATIC-CORE-METHOD--define-typed-contracts-at-replaceable-technical-boundaries.md>), [effect Method](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-160-PROGRAMMATIC-CORE-METHOD--separate-deterministic-transformations-from-effects-and-lifecycle.md>), [generic Atom record](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_operations.py:37), and [Entity Graph parser](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py:225).

### Issue registry

- `I-001` — **Issue/weak point:** the inspected Entity Graph parser/test fixture expects a different Subjects shape from sampled active Atom frontmatter. **Evidence:** `generate_entity_graph.py:225-319`, `test_generate_entity_graph.py:20-49`, and sampled active Atom frontmatter, as recorded in validated step 1. **Consequence:** this generator's output is not an established current graph baseline for comparing implementations. **Affected target/context:** this source-to-projection boundary only, not all Python consumers. **Issue confidence and basis:** high for the static format difference from direct text comparison; runtime failure is untested. **Coverage limit/uncertainty:** one generator and sampled Atoms, without a complete consumer inventory. **Lifecycle state:** `OPEN`. **Mapped fix IDs/disposition:** no project fix proposed or authorized; targeted evidence under `G-001` is required before depending on this generator.

### Fix and improvement register

None proposed or applied. The three hypotheses are alternatives for a future architecture decision, not repairs to `I-001`. No fix ID is carried.

# Unresolved evidence gaps

- `G-001` (linked issue `I-001`; no fix ID): Best current answer: static Subjects shapes differ. Missing evidence: a read-only compatibility check against current active-carrier fixtures or an identified replacement generator. Consequence: no verified generated-graph behavior claim. Exact next action: inspect/test the exact parser and current fixtures before using that graph as a comparison baseline.
- `G-002` (no linked fix): Best current answer: direct Methods are active-path, uncommitted working-tree carriers. Missing evidence: governed admission and released-runtime status. Consequence: no committed-policy or deployment claim. Exact next action: establish the authority/release frontier before any project decision or implementation.
- `G-003` (no linked fix): Best current answer: sampled Python classes are generic technical records, but coverage is bounded. Missing evidence: an inventory of remaining runtime classes, dispatch points, and callers. Consequence: no repository-wide OOP or migration-size claim. Exact next action: inventory affected modules if feasibility or cost becomes decisive.
- `G-004` (no linked fix): Best current answer: three mechanisms have plausible, unmeasured trade-offs. Missing evidence: representative common workload, shared observable criteria/scales, matched results, implementation and migration costs, decision horizon, and owner priorities. Consequence: no defensible ranking, Pareto front, or “better” verdict. Exact next action: declare one same-frontier comparison frame and gather matched evidence before asking for selection.

# Skills used

- `$fpf structure recover`
- `$fpf options explore`

### FPF sources consulted (3 read; 3 used)

- **Used in validated step 1:** `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/22_Structure and Structural Views (STRUCT-CAL)/00_A.22 - Structure and Structural Views (STRUCT-CAL).md` (`A.22`); task-relevant structural sections only.
- **Used in validated step 1:** `FPF-Knowledge-Graph/C_Kernel Extension Specifications/21_33_Structural Information Adequacy for Architecture Capture and Missing-Structure Return/00_C.33 - Structural Information Adequacy for Architecture Capture and Missing-Structure Return.md` (`C.33`); task-relevant adequacy sections only.
- **Used in validated step 2:** `FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/04_05_Canonical Reasoning Cycle/02_Abductive Loop/02_B.05.02.01 - Creative Abduction with NQD.md` (`B.5.2.1`); task-relevant candidate-generation and trade-off sections only; this page has no separate Consequences heading.
