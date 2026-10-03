## Task, scope, and boundaries

### Harvest contract

This report executes the requested SoTA harvest before the later design challenge. :codex-annotation{index="1"}

**Question.** Which current, ready-to-use repositories with MIT-licensed project code can programmatically build the proposed CAPRMEDIO Realization Graph, and what parts of the design remain CAPRMEDIO-owned?

**Proposed graph.** The target view has recursive folder and file scopes; functions, classes, methods, interfaces, and similar declarations inside those scopes; external-library and external-API nodes; and relations such as containment, import, call, inheritance, implementation, and external use. It is intended to reveal actual dependencies and compare them with governed Scope-Unit boundaries.

**Receiving use.** This is evidence for a subsequent design challenge and proof-of-fit pilot. It does not select a dependency, change CAPRMEDIO authority, or implement the graph.

**Decision owner.** The Operator. Repository documentation and this synthesis provide evidence, not project authority.

**Freshness boundary.** Sources were retrieved on 2026-08-23 local time. Repository claims are anchored to exact revisions. Package availability is anchored to current PyPI records where applicable.

**Meaning of ready to use.** A candidate must expose a documented CLI or library and machine-readable graph output. This report establishes documented and packaged readiness, not successful operation in the CAPRMEDIO repository; no candidate was installed or executed locally.

**License boundary.** “MIT” means that the candidate repository's own license at the inspected revision is MIT. Transitive dependencies, generated parsers, optional databases, and redistributed binaries were not license-audited. Apache-2.0, BSD, noncommercial, and archived candidates are retained only as comparison boundaries.

**Excluded.** Popularity-only rankings, secondary tutorials where primary sources were available, LLM-generated semantic descriptions of what code does, runtime truth inferred only from static analysis, and a final architecture decision.

**Saved report:** `fpf-reports/20260822T224444Z-fpf-sota-harvest-realization-graph-repositories.md`

### Resolved FPF source and harvest method

The standalone `fpf-sota-harvest` skill was unavailable. The nearest authoritative local fallback was the toolkit's SoTA-harvest prompt and its source pattern: `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/03_02_SoTA Harvester & Synthesis/00_G.02 - SoTA Harvester & Synthesis.md`, revision `f0b498ddfdf562242984ff7ab7a2557b55af6690`.

The harvest therefore preserves rival traditions, records a CorpusLedger, anchors claims to primary evidence, builds a palette rather than one blended score, and records bridge losses. No diversity-distance gate was applied; diversity is shown through distinct analyzer traditions and explicit non-substitutability.

## High-confidence results (>=95%)

### Executive result

Yes, ready-to-use MIT repositories exist, but no inspected repository is a complete CAPRMEDIO Realization Graph solution.

- **Closest full candidate:** `vitali87/code-graph-rag`. Its offline index, provenance manifest, rich folder/file/symbol/resource schema, multi-language support, and machine exports most closely match the proposed graph.
- **Strongest rich-analysis alternative:** `AppThreat/atom`. It produces a code property graph with syntax, call, reference, control-flow, data-flow, dependency, and endpoint evidence, but CAPRMEDIO must synthesize folder scopes and reduce its richer schema.
- **Pilot candidates:** `CodeGraphContext/CodeGraphContext` and `sh1zen/reql`. Both closely resemble the target model. CodeGraphContext has broader packaging and language reach but repository-owned inconsistency evidence; REQL is simpler and conceptually close but early-stage.
- **Specialist precedents:** `dependency-cruiser` for governed module-boundary enforcement, `gograph` for precise Go analysis and current/stale/unknown evidence, and Tree-sitter or ast-grep as parser/extraction substrates.

The appropriate next step is a bounded, same-fixture comparison of `code-graph-rag`, `AppThreat/atom`, and optionally REQL. The pilot must test graph correctness, unresolved-edge behavior, provenance, reproducibility, installation burden, and mapping to CAPRMEDIO Scope Units. That is a pilot recommendation, not a selected implementation.

### CorpusLedger and coverage boundary

| ID | Candidate and pinned revision | License/status | Evidence role |
|---|---|---|---|
| C01 | [`vitali87/code-graph-rag@12e5ffa`](https://github.com/vitali87/code-graph-rag/tree/12e5ffa8a5bf12688d668b274004353231afe764) | [MIT](https://github.com/vitali87/code-graph-rag/blob/12e5ffa8a5bf12688d668b274004353231afe764/LICENSE); PyPI package | Closest full graph and provenance candidate |
| C02 | [`AppThreat/atom@a2eccc4`](https://github.com/AppThreat/atom/tree/a2eccc4a43565cbd1992b655a78fd7d96ffac142) | [MIT](https://github.com/AppThreat/atom/blob/a2eccc4a43565cbd1992b655a78fd7d96ffac142/LICENSE) | Rich code-property-graph engine |
| C03 | [`CodeGraphContext@39557ad`](https://github.com/CodeGraphContext/CodeGraphContext/tree/39557ada8ea88dfe23ff54cef1df1bedfa542b9a) | [MIT](https://github.com/CodeGraphContext/CodeGraphContext/blob/39557ada8ea88dfe23ff54cef1df1bedfa542b9a/LICENSE); PyPI package | Broad embedded graph pilot with explicit quality debt |
| C04 | [`reql@927c183`](https://github.com/sh1zen/reql/tree/927c1834dce09b321a496ea1d35b2b4d2574d145) | [MIT](https://github.com/sh1zen/reql/blob/927c1834dce09b321a496ea1d35b2b4d2574d145/LICENSE); PyPI package | Lightweight deterministic local graph pilot |
| C05 | [`dependency-cruiser@1f28f44`](https://github.com/sverweij/dependency-cruiser/tree/1f28f44a49c054dc128226543188220818b1ab52) | [MIT](https://github.com/sverweij/dependency-cruiser/blob/1f28f44a49c054dc128226543188220818b1ab52/LICENSE) | JS/TS architecture-rule precedent |
| C06 | [`tree-sitter@74b7d0c`](https://github.com/tree-sitter/tree-sitter/tree/74b7d0c951ebdab16a8a4d64e7cf81e56046408a) | [MIT](https://github.com/tree-sitter/tree-sitter/blob/74b7d0c951ebdab16a8a4d64e7cf81e56046408a/LICENSE) | Incremental parsing substrate, not a graph solution |
| C07 | [`ast-grep@0eb0838`](https://github.com/ast-grep/ast-grep/tree/0eb08389b6c4c5f3e19f90efbcb726fc413ca63d) | [MIT](https://github.com/ast-grep/ast-grep/blob/0eb08389b6c4c5f3e19f90efbcb726fc413ca63d/LICENSE) | Structural extraction/rule substrate |
| C08 | [`gograph@72d19a5`](https://github.com/ozgurcd/gograph/tree/72d19a5950d199c940c674f49ea5cc1f643cf4c3) | [MIT](https://github.com/ozgurcd/gograph/blob/72d19a5950d199c940c674f49ea5cc1f643cf4c3/LICENSE) | Go-specific precision and assurance reference |
| C09 | [`polycodegraph@4c5fb20`](https://github.com/smochan/polycodegraph/tree/4c5fb2093b5b1672a142d2188c22539ab2d532ca) | [MIT](https://github.com/smochan/polycodegraph/blob/4c5fb2093b5b1672a142d2188c22539ab2d532ca/LICENSE); PyPI package | Early SQLite cross-stack graph |
| C10 | [`madge@456057b`](https://github.com/pahen/madge/tree/456057b85c2d063dad9c10147d7686ded4fc5ce5) | [MIT](https://github.com/pahen/madge/blob/456057b85c2d063dad9c10147d7686ded4fc5ce5/LICENSE) | Mature JS module-graph reference |
| C11 | [`code2flow@c2c22af`](https://github.com/scottrogowski/code2flow/tree/c2c22afe5e12f969cc256373bf8f4eec592dc762) | [MIT](https://github.com/scottrogowski/code2flow/blob/c2c22afe5e12f969cc256373bf8f4eec592dc762/LICENSE) | Simple approximate call-graph reference |
| B01 | [`joern@937bec1`](https://github.com/joernio/joern/tree/937bec1c5997403df4d5101db3b04c767f72982b) | Apache-2.0 | Non-MIT mature CPG capability boundary |
| B02 | [`scip@02559b6`](https://github.com/scip-code/scip/tree/02559b6181bcf7a53e93c80995a798457117c431) | Apache-2.0 | Non-MIT language-neutral index protocol boundary |
| B03 | [`Glean@7f8ff21`](https://github.com/facebookincubator/Glean/tree/7f8ff2190220664b58721a9bd6f62fb51091177d) | BSD 3-Clause | Non-MIT source-fact database boundary |
| X01 | [`GitNexus@aac7515`](https://github.com/abhigyanpatwari/GitNexus/tree/aac7515d2a8c50a1f8f923c6fb77218b333560d6) | [PolyForm Noncommercial](https://github.com/abhigyanpatwari/GitNexus/blob/aac7515d2a8c50a1f8f923c6fb77218b333560d6/LICENSE.md) | Excluded from MIT-ready pool |

Coverage includes four traditions: integrated multi-language graph products, rich code-property-graph engines, specialist architecture analyzers, and parser/index substrates. The coverage floor of three distinct entries per load-bearing family is met for graph extraction and machine output. It is not met for exact external-API identity or runtime-only dependencies; those remain open boundaries.

### FlowRecord

1. Fixed the target objects, relations, receiving use, license criterion, and static/runtime boundary.
2. Screened candidate repositories using maintainer-owned repository, license, documentation, package, and defect evidence.
3. Pinned admitted repositories to exact current revisions.
4. Separated complete graph products from CPG engines, specialist boundary checkers, and parser/index substrates.
5. Preserved non-MIT but technically important systems as comparison boundaries rather than silently excluding their capabilities.
6. Compared candidates on a palette; no aggregate score or winner was manufactured.
7. Stopped after the principal design claims had multiple independent candidates or an explicit evidence gap.

### Object and operator inventory

**Objects:** repository revision; directory; file; declaration; function; class; method; interface; external package; external module; external API/resource; resolved edge; unresolved edge; generated index; provenance manifest; CAPRMEDIO Scope Unit; governed dependency allowance or demand; conformance result.

**Operators:** parse; resolve names; extract containment; extract imports/calls/inheritance/implementation; identify external resources; serialize; diff; verify currentness; map source paths to Scope Units; map analyzer relations to CAPRMEDIO relation kinds; compare actual edges with governed edges; emit supported, violated, or unknown findings.

### ClaimSheets and evidence anchors

#### CS-01 — The target graph can be generated programmatically

`code-graph-rag` documents Folder, File, Module, Class, Function, Method, Interface, ExternalPackage, ExternalModule, and Resource nodes, plus containment, definition, import, call, reference, inheritance, implementation, override, and external-dependency relations in its [graph schema](https://github.com/vitali87/code-graph-rag/blob/12e5ffa8a5bf12688d668b274004353231afe764/docs/architecture/graph-schema.md). REQL independently documents Directory, File, declaration, import, dependency, call, endpoint, schema, config, and test entities. Atom independently emits a richer CPG.

**Synthesis.** The proposed graph is technically feasible without inventing a parser platform from scratch. CAPRMEDIO's two-layer presentation should be a projection from the analyzer's richer native graph, not a restriction imposed on extraction.

**Confidence: 99%.** Three independent MIT candidates expose the necessary object families and machine-readable relations.

#### CS-02 — `code-graph-rag` is the closest complete candidate

Its documented offline command writes a canonical index without requiring the interactive graph database. Its [export documentation](https://github.com/vitali87/code-graph-rag/blob/12e5ffa8a5bf12688d668b274004353231afe764/docs/guide/graph-export.md) describes sorted deterministic output, repository-relative identities, source commit and dirty state, analyzer version, schema/configuration hashes, artifact hashes, language coverage, verification, and index diffing. It also models network, database, file, environment, and socket resources.

**Synthesis.** This is the best first pilot because it combines near-target schema, offline generation, provenance, verification, and broad language coverage. The interactive Memgraph/Docker path is optional for the extraction pilot.

**Boundary.** Current PyPI publishes `code-graph-rag` 0.0.720 while the inspected source identifies a later patch line. The pilot must pin one exact package or source revision and must not mix documentation from one with execution of the other. Python 3.12 or later is required by the current package line.

**Confidence: 98%.** The fit is direct; operational success and graph accuracy on CAPRMEDIO remain untested.

#### CS-03 — Atom is the strongest rich-analysis alternative

Atom documents multi-language code-property graphs and exports including GraphML, GEXF, GraphSON, Neo4j CSV, DOT, and JSON-oriented slices. Its schema includes files, methods, type declarations, dependencies, calls, references, inheritance, control flow, imports, and data-flow edges. It also offers HTTP endpoint extraction.

**Synthesis.** Atom is a strong alternative when call/data-flow depth matters more than matching CAPRMEDIO's simple view. It can supply richer evidence from which CAPRMEDIO projects a reduced graph.

**Boundary.** Folder nodes are not a core first-class schema object, so recursive folder scopes must be synthesized from file paths. Java requires compilation, and the Scala/JVM/native toolchain is heavier than a small embedded parser.

**Confidence: 98%.** Repository documentation and schema support the capability; CAPRMEDIO-specific mapping is absent by design.

#### CS-04 — Packaged readiness does not imply trusted graph quality

CodeGraphContext publishes a CLI/library and portable graph bundle with repository, directory, file, function, class, interface, containment, call, import, inheritance, and mapping objects. However its own [`CGC_GRAPH_INCONSISTENCIES.md`](https://github.com/CodeGraphContext/CodeGraphContext/blob/39557ada8ea88dfe23ff54cef1df1bedfa542b9a/CGC_GRAPH_INCONSISTENCIES.md) records missing and inconsistent relations across language backends. Its [`CGC_E2E_BUG_REPORT.md`](https://github.com/CodeGraphContext/CodeGraphContext/blob/39557ada8ea88dfe23ff54cef1df1bedfa542b9a/CGC_E2E_BUG_REPORT.md) is historical relative to the current package, so it is evidence of prior release drift, not proof that every listed defect remains.

**Synthesis.** CodeGraphContext is suitable for a controlled pilot, not for unverified authority or absence claims. A CAPRMEDIO fixture suite must test each required language/relation pair.

**Confidence: 97%.** The quality boundary is repository-owned and explicit; its present severity needs fresh execution.

#### CS-05 — REQL is structurally close but immature

REQL offers a local deterministic property graph, JSON export, incremental compilation, provenance/confidence, unresolved-call summaries, and no mandatory external database or LLM. Its node and edge families closely match the proposed design.

**Synthesis.** REQL is attractive as a lightweight reference or third pilot. Its small repository, early 0.1.x package line, and limited language-specific adapters make it insufficient as the default foundation without stronger fixture evidence.

**Confidence: 97%.** Feature fit and early maturity are directly observable; future stability is unknown.

#### CS-06 — Specialist analyzers remain valuable

Dependency-cruiser can declare forbidden JS/TS module dependencies and report violations, making it a mature precedent for comparing actual edges with allowed architecture. GoGraph adds precise type-checked Go calls, imports, interface relations, architecture boundaries, source digests, and explicit current/stale/unknown handling. Tree-sitter and ast-grep provide reusable parsing and structural matching but do not independently provide a resolved cross-file project graph.

**Synthesis.** CAPRMEDIO should allow language-specialist analyzers behind a common evidence adapter. A universal parser can provide breadth; specialist analyzers can provide stronger evidence for particular languages.

**Confidence: 98%.** The tools' roles are explicit and non-substitutable.

#### CS-07 — Static absence is not proof of runtime independence

Dynamic dispatch, reflection, generated code, configuration-driven imports, plugin loading, network-discovered endpoints, and native/foreign calls may be unresolved or absent from a static index. CodeGraphContext and REQL explicitly preserve unresolved relations; code-graph-rag can overlay runtime traces on static calls.

**Synthesis.** A missing static edge means “not observed under this analyzer and configuration,” not “no dependency exists.” CAPRMEDIO conformance therefore needs at least `supported`, `violated`, and `unknown`, plus exact analyzer/source/configuration provenance. Runtime FIELD evidence complements rather than replaces the Realization Graph.

**Confidence: 99%.** This follows from the analyzers' documented resolution boundaries and the semantics of static analysis.

#### CS-08 — CAPRMEDIO must own the semantic adapter

No inspected candidate knows CAPRMEDIO Scope Units, governing Atoms, ordered-unit dependency rules, contract controller/follower semantics, or which cross-unit dependency is allowed. They model observed code facts.

**Synthesis.** The adapter must map analyzer paths and declarations to Scope Units, normalize relation kinds, preserve unresolved evidence, and compare observed edges with governed demands or prohibitions. The generated graph is evidence or Projection; it does not become governing source of truth.

**Confidence: 100%.** The missing CAPRMEDIO semantics are outside every candidate's declared scope.

### Two heterogeneous microexamples

**Python feature-boundary example.** `payments/service.py::charge()` calls `notifications/email.py::send_receipt()`. An analyzer emits folder/file containment, function definitions, imports, and a call. The CAPRMEDIO adapter maps both paths to sibling Scope Units. If no governing contract or shared upstream unit permits the dependency, the comparison emits a Concern with the exact edge and source revision. If call resolution is incomplete, it emits `unknown`, not a false pass.

**TypeScript external-resource example.** `WEB/client.ts::submit()` calls a URL and imports a generated client; `API/handler.ts::submit()` exposes the endpoint. A candidate may emit file/import/call nodes and a network resource, while a cross-stack analyzer may correlate route and fetch evidence. Mapping a literal URL to one governed API identity is possible; mapping computed URLs or runtime service discovery may remain unknown. This demonstrates why external-API identity requires an adapter and may need runtime evidence.

**Go precision example.** A Go package imports another sibling package and invokes a method through an interface. A universal Tree-sitter extractor may identify syntax and probable calls; a type-checked Go analyzer can resolve the interface implementation and preserve graph-currentness evidence. This supports a common graph contract with stronger language-specific producers rather than one assumed accuracy level.

### SoTA_Set and traditions

| Tradition | Representative systems | Strength | Failure boundary |
|---|---|---|---|
| Integrated multi-language graph | code-graph-rag, CodeGraphContext, REQL, polycodegraph | Fastest path to the proposed graph | Resolution quality varies by language; schemas differ |
| Code property graph | AppThreat atom; Joern as non-MIT boundary | Rich control/data/call/reference evidence | Heavier stack and greater projection effort |
| Specialist architecture analyzer | dependency-cruiser, GoGraph, Madge, code2flow | Stronger bounded language or relation semantics | Cannot alone cover a heterogeneous repository |
| Parser/extraction substrate | Tree-sitter, ast-grep | Maximum schema control and broad parsing ecosystem | CAPRMEDIO must build resolution, storage, provenance, and conformance |
| Language-neutral fact/index protocol | SCIP and Glean as non-MIT boundaries | Stable interoperability and cross-tool facts | Outside the requested MIT pool; still needs CAPRMEDIO semantics |

### Comparison palette

The proof-of-fit should compare candidates without collapsing these coordinates into one score:

1. License of project code and transitive runtime distribution.
2. Reproducible installation and supported runtime/platforms.
3. Language coverage actually required by the project.
4. Folder/file scope fidelity.
5. Declaration identity stability.
6. Import, call, inheritance, implementation, and external-resource resolution.
7. Explicit unresolved/unknown evidence.
8. Deterministic machine output and exact source/configuration/analyzer provenance.
9. Incremental refresh and stale-index detection.
10. Offline/embedded operation versus database/service burden.
11. Mapping effort to CAPRMEDIO Scope Units and relations.
12. Fixture-measured precision, recall, and failure modes.
13. Runtime-evidence integration.
14. Query, diff, and visualization ergonomics after correctness is established.

### BridgeMatrix

| Bridge | Valid correspondence | Loss that must remain explicit |
|---|---|---|
| Rich analyzer graph -> CAPRMEDIO two-layer view | Project richer node/edge schema into folder/file scopes and declarations | Control flow, data flow, unresolved candidates, and provenance must not be discarded silently |
| Source path -> Scope Unit | Longest governed path match can assign a file to one Scope Unit | Generated, vendored, symlinked, moved, and multi-root sources need explicit policy |
| Observed edge -> governed dependency | Normalize analyzer relations and compare endpoints with active authority | An observed call is evidence of coupling, not by itself a governance violation |
| Missing edge -> conformance | None without analyzer-completeness evidence | Absence is normally `unknown`, not permitted or independent |
| Static graph -> runtime graph | Runtime traces can confirm exercised edges and reveal some missed calls | A trace covers only its workload; it cannot establish complete runtime behavior |
| Universal analyzer -> specialist analyzer | Both can emit a common evidence envelope | Their confidence and completeness are not interchangeable |

## Open questions (confidence <95%)

1. **Which repository languages must the first CAPRMEDIO implementation support? — 90%.** The shortlist changes substantially if the first target is Python-only, JS/TS-only, or polyglot.
2. **What minimum precision/recall is acceptable per relation kind? — 88%.** “Correct graph” needs a fixture corpus and separate thresholds for containment, imports, calls, inheritance, external libraries, and APIs.
3. **Should generated, vendored, test, migration, and build-output code enter the same graph? — 89%.** The answer affects identity, noise, and dependency-conformance results.
4. **What is the canonical identity of an external API? — 85%.** URL, OpenAPI operation, service/repository identity, deployment endpoint, and logical capability are different objects.
5. **Will the runtime accept a JVM/native analyzer or require a Python/local embedded implementation? — 90%.** This determines whether Atom's richer evidence is operationally acceptable.
6. **May non-MIT analyzer protocols or tools be optional adapters? — 90%.** The requested harvest uses an MIT core-license gate, but Apache-2.0 SCIP or Joern could materially improve interoperability or evidence without becoming CAPRMEDIO's governing core.
7. **What result should mixed evidence produce? — 92%.** Static and runtime producers may disagree. Governance must define whether stronger evidence overrides, coexists, or opens a Concern.
8. **Where should the generated graph and its provenance manifest live? — 91%.** It should be a Projection/evidence carrier rather than an Atom, but the exact carrier, lifecycle, and refresh trigger require project authority.

### Disagreements, exclusions, and insufficient basis

- GitNexus is excluded from the ready-to-use MIT pool because its pinned license is PolyForm Noncommercial, despite strong graph capabilities.
- Joern, SCIP, Glean, tree-sitter-graph, and archived stack-graphs are not MIT candidates. They remain useful capability or protocol references.
- CodeGraphContext's historical bug report does not establish the current release's exact defect set. Only a current fixture run can do that.
- GitHub stars, recent commits, repository size, and test-file counts are maturity signals, not correctness evidence.
- No candidate was locally installed, benchmarked, or run on CAPRMEDIO. Claims of operational compatibility, graph accuracy, or performance would be premature.
- No evidence supports treating every file as a single flat “layer-1” node if recursive directories are also scopes. The coherent model is a recursive scope tree plus contained declaration nodes; “layer 1/layer 2” is a view, not graph depth.
- No evidence supports treating the static code graph as governing authority or as a complete account of runtime behavior.

### Receiving use and refresh condition

The subsequent design challenge should receive: this corpus, the comparison palette, the CAPRMEDIO-owned adapter boundary, and the pilot shortlist. It should challenge graph identity, recursive scope semantics, static/runtime separation, conformance states, and carrier ownership before any tool is selected.

Refresh this harvest when any of the following occurs: the first implementation language set is fixed; the graph schema or Scope-Unit semantics change; a candidate pilot fails installation or fixture gates; a shortlisted project changes license or major version; runtime tracing becomes mandatory; or evidence is older than six months at the selection decision.

## Skills used

- Exact requested invocation: `$fpf sota harvest`.
- The standalone `fpf-sota-harvest` skill package was not installed. The local `fpf` toolkit's `sota-harvest` prompt was used as the documented fallback.
- FPF sources consulted: 1 direct source, `G.2 SoTA Harvester & Synthesis`, including its problem frame, forces, harvester loop, CorpusLedger, ClaimSheets, palette, bridge, conformance, anti-pattern, and refresh requirements.
- External evidence: maintainer-owned repositories, exact license files, repository documentation, and current PyPI package records. No secondary source was used for a load-bearing claim.
