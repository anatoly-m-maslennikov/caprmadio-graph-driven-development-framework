---
atom_id: CA-A-042
subject_scopes:
  - artifact-model
  - carrier-format
version: 1
updated_at: 2026-08-21 01:52:33
---

## Task, scope, and boundaries

### Exploration contract and resolved FPF source

- **Question:** Which database mechanisms could support a CAPRMEDIO local derived-data pipeline in which Atoms and full Journals remain file-backed `src`, parsed and derived data lives in database stages (`stg`, `int`, `dim`, `fct`, `mrt`, `biz`), and marts are published as real HTML pages with JavaScript data snapshots? Which engine treats CAPRMEDIO's directed typed relations most naturally at engine level?
- **Entity of concern:** the rebuildable CAPRMEDIO knowledge runtime: source ingestion, typed graph, complete Journal event history, transformation stages, local monitoring service, and HTML publication.
- **Receiving use and decision owner:** this pack supplies alternatives and a comparison plan for Anatoly's later architecture decision. It does not amend CAPRMEDIO authority, select an engine, or implement a database.
- **Current baseline:** the repository currently specifies Markdown STG projections, one embedded-JavaScript HTML MRT, and a read-only service over current Atom/STG files in `CAPRMEDIO-SPEC-TOOLS-REQU-616`, `CAPRMEDIO-SPEC-TOOLS-REQU-617`, and `CAPRMEDIO-SPEC-TOOLS-METH-079`. The new proposal moves all derived stages into a database and expands publication from one HTML file into real generated pages.
- **Observed scale:** the current `.caprmedio` tree contains 1,261 regular files totaling 2,817,813 bytes, including 1,185 Markdown files and two Journals totaling 508,918 bytes. At this size, correctness and simplicity matter more than large-graph performance. **Confidence: 99%**, from a direct current-worktree inventory.
- **Authority boundary:** Atoms and append-only Journals remain authoritative source carriers. The database, its derived stages, `data.js`, and HTML pages are disposable Projections that must be reproducible from an explicit source frontier. **Confidence: 99%**, from the user's `src` formulation and current CAPRMEDIO Projection rules.
- **What counts as interesting:** a candidate must differ materially in mechanism and illuminate a real trade-off among native relation semantics, dbt-like transformations, full Journal replay, local operation, static publication, and operational complexity. Cosmetic variants are excluded.
- **Quality coordinates:** native typed-relation semantics; ability to enforce endpoint/cardinality rules; complete Journal/event handling; relational transformation ergonomics; embedded/local-server fit; deterministic rebuild and export; Python/JavaScript integration; maturity and storage stability; operational burden; reversibility.
- **Protected constraints:** file sources stay authoritative; database writes never mutate Atoms or Journals; full raw source and Journal records remain recoverable; every derived row is tied to a source frontier; source changes publish atomically; runtime state stays deletable and rebuildable; no engine is selected from an opaque aggregate score.
- **Diversity axes:** relational versus property-graph versus semantic relation model; embedded versus server; one engine versus dual-engine index; SQL/Cypher/TypeQL/Datalog; current-state versus native temporal facilities.
- **Risk, cost, and horizon:** accept a bounded prototype dependency, but not an unmaintained production dependency or a mandatory heavyweight service without demonstrated semantic value. Optimize the first architecture for the current few-megabyte repository while preserving a migration path.
- **Evidence inputs:** current CAPRMEDIO requirements and files; current official engine documentation and release state accessed on 2026-08-18; the verified FPF graph edition generated from source revision `9a9a42e4d154021ca3f7415e0009a4214832f65f`.
- **Exploration budget:** six distinct mechanisms, a capability-level parity comparison, and one executable parity-spike design. No performance benchmark or implementation is included.
- **Stop condition:** stop when the candidate set spans the meaningful mechanism families, identifies the non-dominated alternatives, and states the evidence needed for an engine decision.
- **Saved report:** `fpf-reports/20260818T173038Z-fpf-options-explore-caprmedio-graph-database.md`

## High-confidence results (>=95%)

### Architecture that remains valid across engines

The safest first implementation is a full transactional rescan after every filesystem trigger, not a clever per-event mutation algorithm. A filesystem event determines **when** to reconcile; it need not determine exactly **what** changed. At 2.82 MB, reparsing the complete source set avoids dropped/coalesced watcher events, rename ambiguity, partial saves, and platform-specific inode assumptions. A startup scan and explicit `sync` command provide additional recovery paths. **Confidence: 98%**, based on the observed repository size and the requirement for deterministic rebuilds.

```text
.caprmedio Atoms + complete Journals
                 │
       file event / startup / explicit sync
                 │
       full scan + path/digest manifest
                 │
      atomic database build/transaction
                 │
 src_file / src_atom / src_relation / src_journal_event
                 │
 stg_* → int_* → dim_* + fct_* → mrt_* → biz_*
                 │
       deterministic query + export
                 │
       HTML pages + versioned data.js
```

The database source-shaped layer should contain:

- `src_file`: canonical path, file kind, byte length, digest, encoding, raw text, parse status, and source-frontier ID.
- `src_atom`: one row per Atom with stable identity, raw frontmatter, normalized frontmatter columns, full Markdown, body without frontmatter, H1 summary, lifecycle state, and every value derived from filename and location.
- `src_relation`: one row per authored edge with source Atom, relation type, target identity, ordinal, source revision/digest, and resolution status. Reverse and transitive edges remain derived.
- `src_journal_event`: every Journal line/event, not an aggregate—journal path, line number and/or byte offset, raw JSON, raw digest, event identity, timestamp, session, operation, status, subjects, outputs, and source frontier.
- normalized Journal child tables where one event contains multiple governed subjects, outputs, paths, or evidence references.
- `ingest_run` and `source_frontier`: parser/schema editions, complete path/digest manifest, start/commit times, diagnostics, and publication status.

For incremental Journal parsing, the loader may resume from a prior byte offset only after proving that the prior byte prefix is unchanged; otherwise it must replay the complete Journal. The database may enforce append-only behavior internally, but the file Journal remains the authority. **Confidence: 98%**, because this preserves full replay without trusting mutable cache state.

### CandidateSet and provenance

1. **C1 — SQLite typed-edge warehouse.** Store all stages in one SQLite file. Model nodes and edges as strict relational tables; use a relation-type registry, foreign keys, checks, unique constraints, and triggers to enforce CAPRMEDIO endpoint and mode rules. Traverse with recursive CTEs. SQLite explicitly supports graph walking through recursive CTEs, but graph labels and endpoint matrices are an application schema rather than a native graph type. [SQLite recursive graph queries](https://www.sqlite.org/lang_with.html), [foreign keys](https://www.sqlite.org/foreignkeys.html). **Confidence: 99%.**

2. **C2 — LadybugDB embedded property graph.** Use node tables for Atoms/events and one relationship table per CAPRMEDIO relation type. Ladybug is the actively maintained successor to archived Kùzu, embeds in Python/Node/Rust and other hosts, uses Cypher, and provides typed `CREATE REL TABLE ... FROM ... TO ...` declarations with relationship properties and multiplicities. It is the closest current mechanism to “SQLite for graphs.” It cannot yet express an “exactly one” multiplicity, and CAPRMEDIO rules involving tier, lifecycle, or authority mode still need validation outside the relationship declaration. [Ladybug table definitions](https://docs.ladybugdb.com/cypher/data-definition/create-table/), [current releases](https://github.com/LadybugDB/ladybug/releases), [embedded concurrency model](https://docs.ladybugdb.com/concurrency/). **Confidence: 98%.**

3. **C3 — SurrealDB local multi-model server.** Store Atoms and Journal events as schemafull records, edges as `TYPE RELATION` tables with constrained `IN`/`OUT` record types, and derived layers as tables or incrementally maintained table views. Run one local server to own writes and serve UI queries; use live queries/changefeeds if interactive freshness is later desired. SurrealDB can also embed, but its embedded Python mode does not support live queries, so the server mode is the fair comparison for this proposal. [typed graph relations](https://surrealdb.com/docs/learn/data-models/graph/creating-relations), [pre-computed table views](https://surrealdb.com/docs/reference/query-language/statements/define/table), [live queries](https://surrealdb.com/docs/learn/querying/real-time/live-queries), [embedded limitations](https://surrealdb.com/docs/reference/python/concepts/embedded-databases). **Confidence: 97%.**

4. **C4 — TypeDB semantic relation server.** Model Atom roles as entity subtypes and each CAPRMEDIO edge as a relation type with named roles; declare which Atom subtypes may play each role and apply cardinality constraints. TypeDB makes entities, relations, attributes, roles, subtyping, and role-playing part of the schema and validates connections at write/commit time. This is the strongest engine-level answer to “typed relations,” including n-ary relations, but it requires a server, credentials, drivers, TypeQL, and a separate publication application; it is not naturally a dbt/SQL warehouse. [TypeDB entity/relation/attribute model](https://typedb.com/docs/core-concepts/typeql/entities-relations-attributes/), [schema integrity](https://typedb.com/docs/core-concepts/typeql/schema-data/), [server deployment](https://typedb.com/docs/home/install/ce/). **Confidence: 99%.**

5. **C5 — SQLite warehouse plus Ladybug graph index.** Keep `src` through `biz` and full Journals in SQLite, then rebuild a Ladybug database from selected SQLite models for Cypher traversal and visualization. This preserves SQL transformation ergonomics and native property-graph querying, but duplicates derived state and creates a cross-engine consistency boundary. Both databases remain disposable. **Confidence: 97%**, derived from the documented capabilities of C1 and C2.

6. **C6 — CozoDB temporal Datalog experiment.** Store facts as relations, use Datalog for recursive graph queries, and use native validity/time-travel relations for historical state. Cozo is embedded and unusually well matched to Journal/as-of questions, but its own project status says versions before 1.0 do not promise syntax/API or storage compatibility. Retain it as an experimental alternative, not a default production dependency. [Cozo project status](https://github.com/cozodb/cozo), [time travel](https://docs.cozodb.org/en/latest/timetravel.html). **Confidence: 98%.**

These candidates are genuine mechanism variants: relational constraints, embedded property graph, multi-model live server, semantic relation schema, dual-engine projection, and temporal Datalog. Their differences are not naming differences.

### Declared-coordinate evaluation and diversity map

The labels below are coordinate-specific judgments, not a combined score.

| Coordinate | C1 SQLite | C2 Ladybug | C3 SurrealDB | C4 TypeDB | C5 SQLite + Ladybug | C6 CozoDB |
|---|---|---|---|---|---|---|
| Native typed relations | Weak: edge typing is designed by us | Strong: relationship tables and typed endpoint tables | Strong: relation tables with `IN`/`OUT` types | Very strong: relation types, named roles, role players, subtyping | Strong in graph index | Strong query relations; weaker schema semantics |
| CAPRMEDIO semantic-rule enforcement | Strong but custom triggers/validators | Medium: endpoint/multiplicity native; tier/mode rules external | Medium: schema/assertions help; cross-record rules remain custom | Strongest native schema fit | Strong, split across two engines | Medium; validation queries remain important |
| Full Journal and temporal analytics | Very strong relational fact model | Workable event node table; no special temporal model | Strong records/changefeeds/views | Workable semantic event model; aggregation less familiar | Very strong in SQLite | Very strong native time travel |
| `stg/int/dim/fct/mrt/biz` ergonomics | Very strong SQL views/tables | Medium: Cypher tables/materialization, not dbt-native | Strong multi-model tables and incremental views | Weak-to-medium: TypeQL pipelines, not SQL/dbt | Very strong in SQLite | Medium: Datalog relations, unfamiliar tooling |
| Local footprint | Excellent, one serverless file | Excellent embedded database, one owning process | Good as one local service; more runtime machinery | Weakest: mandatory authenticated server/driver | Medium: two database runtimes | Good embedded footprint |
| Live local UI/service | Application supplies server and events | Application supplies server; one process owns write DB | Native server, live queries, and changefeeds | Native server, but UI/API still custom | Application supplies unified service | Application supplies server/API |
| Deterministic static export | Excellent SQL-to-JSON/JS tooling | Good query export; generator is custom | Good query/export path; views assist | Custom application required | Excellent from SQLite marts | Custom application required |
| Maturity and stability | Highest | Active but young successor project | Active, broader and more complex | Active, specialized ecosystem | SQLite mature; Ladybug risk remains | Lowest: pre-1.0 compatibility warning |
| Reversibility | Highest: standard SQL and easy dumps | Good if source files remain canonical; Cypher schema is engine-specific | Good logical export, but engine-specific schema | Medium: specialized model/query language | Medium: two schemas to retire | Medium-low until storage/API stabilize |

No candidate dominates every coordinate. The capability-level Pareto front therefore retains:

- **C1 SQLite** for minimum operations, strongest Journal/warehouse fit, maturity, and reversibility.
- **C2 LadybugDB** for embedded native property-graph querying without a separate database server.
- **C3 SurrealDB** for a single local service combining graph records, incremental views, change notifications, and API access.
- **C4 TypeDB** for the strongest native semantic typing of relations and role players.
- **C5 dual-engine** only if both SQL transformation ergonomics and native Cypher are protected requirements worth an extra consistency boundary.

C6 remains an archive-worthy experimental branch because native time travel is illuminating, but its compatibility risk keeps it off the current capability front.

### Parity plan/report

#### ParityPlan@CAPRMEDIO-local-graph-runtime

- **Baseline:** C1 SQLite with one Atom table, one Journal-event fact table, one authored-edge table, relation registry, foreign keys/checks/triggers, recursive CTEs, and generated HTML/JavaScript.
- **Comparators:** LadybugDB 0.19.x current release line; SurrealDB current 3.x documentation/runtime; TypeDB current 3.x Community Edition; optional CozoDB 0.7 experiment. Pin exact packages and checksums when the spike starts.
- **Input frontier:** one immutable manifest of all `.caprmedio` source paths and SHA-256 digests, including active and historical Atoms and complete Journal bytes. The current inventory is evidence of scale, not a stable benchmark frontier.
- **Shared implementation policy:** the same parser, normalized source records, relation vocabulary, source manifest, test queries, and HTML/data contract. Database-specific schemas may differ, but semantic outputs may not.
- **Required scenarios:** clean full rebuild; Atom add/edit/move/rename/delete; Journal append and non-append corruption detection; unresolved target; invalid relation endpoint; forbidden same/downstream tier edge; active and RMED orphan detection; ancestor/descendant traversal; as-of Journal query; current active-Atom snapshot; lineage sections; deterministic `data.js`; server restart and database deletion/rebuild.
- **Measures:** semantic result equality; invalid-state rejection location; amount of custom validation code; dependency/install footprint; full rebuild time; triggered reconciliation time; database size; query clarity; HTML export determinism; crash/restart recovery; cross-platform packaging. Performance measures use the same hardware and repeated runs, but no weighted total is permitted.
- **Outcome shape:** publish a selected set or partial order by coordinate. An engine that is fastest but cannot reproduce source lineage or reject required invalid states does not pass the protected constraints.
- **Freshness window:** engine documentation, packages, and release status rechecked at spike time; current evidence is pinned to 2026-08-18.

#### Current ParityReport@CAPRMEDIO-local-graph-runtime

This is a documentation-and-project-evidence report, not an executable benchmark.

- TypeDB has the most natural engine-level model for semantically typed relations because relation types, named roles, permitted role players, subtyping, and cardinalities are schema concepts. **Confidence: 99%.**
- LadybugDB has the most natural embedded property-graph model: typed node/relationship tables, endpoint table declarations, edge properties, Cypher, ACID transactions, and current multi-language packages. **Confidence: 98%.**
- SurrealDB has the closest one-engine match to the whole local-service proposal because it combines graph relation tables, schemafull records, pre-computed table views, changefeeds/live queries, and server or embedded deployment. **Confidence: 97%.**
- SQLite has the strongest fit for full Journals, dbt-like relational stages, deterministic rebuilds, packaging, and long-term reversibility, while still supporting recursive graph traversal. Its graph semantics are schema conventions and triggers, not a native graph model. **Confidence: 99%.**
- Current scale does not justify choosing by graph-query speed. All retained engines should handle a few megabytes; the meaningful test is semantic correctness and operational shape. **Confidence: 98%.**
- DuckDB plus DuckPGQ is not a current front-runner: DuckDB's own documentation says the community extension is unavailable in current 1.5.x, requires 1.4.4, remains under active development, and has incomplete features. [DuckDB graph-query status](https://duckdb.org/docs/current/guides/sql_features/graph_queries). **Confidence: 99%.**
- Kùzu should not be adopted for new work: its official repository was archived on 2025-10-10. LadybugDB is the maintained fork/successor to evaluate instead. [Kùzu archive notice](https://github.com/kuzudb/kuzu). **Confidence: 100%.**

### Retained options, exclusions, and evidence gaps

**Retained for an executable spike:** C1 SQLite, C2 LadybugDB, C3 SurrealDB, and C4 TypeDB. They isolate four genuinely different answers: build graph semantics relationally; use an embedded property graph; use one live multi-model service; or use a semantic relation type system.

**Retained only conditionally:** C5 if one engine cannot satisfy both transformation and graph-query needs; C6 if native temporal Datalog becomes a protected requirement.

**Excluded from the spike:** archived Kùzu; DuckPGQ until it is supported on the current DuckDB release; Neo4j because a dedicated server/JVM and product surface add cost without evidence that CAPRMEDIO's current scale needs them; PostgreSQL graph extensions because they preserve server complexity while adding an extension boundary; pure in-memory graph libraries because they do not supply the durable staged database requested.

**Evidence gaps:** no pinned source manifest; no executable endpoint-rule matrix for every CAPRMEDIO relation; no representative set of Journal replay/as-of queries; no agreed static-site/data.js packaging contract; no prototype measurements for install size, rebuild latency, export determinism, or recovery.

### Stop condition and decision handoff

Exploration stops here because the candidate set covers the meaningful mechanisms, the capability front is preserved, and the missing evidence is executable rather than conceptual. No engine is selected.

The next action is a bounded four-engine spike using the parity plan. A later selection should use `fpf-decision-synthesize` to record the chosen engine, accepted losses, fallback/migration route, version pins, and reopen triggers. A practical reopen trigger is any of: repository size or traversal latency exceeds its declared budget; native relation enforcement becomes mandatory; one-process write ownership blocks required tooling; package/storage compatibility changes; or the static publication contract changes materially.

## Open questions (confidence <95%)

1. **Should one engine own both the warehouse and the graph?** Best current answer: start with one engine unless the parity spike proves a protected query or constraint cannot be met. **Confidence: 92%.** Missing evidence: actual graph queries and acceptable operational burden. Consequence: choosing C5 prematurely doubles schemas, rebuilds, diagnostics, and failure modes. **Next action:** run the same required scenarios against C1–C4 before prototyping C5.

2. **Which CAPRMEDIO rules must be rejected by the database itself?** Best current answer: native endpoint and cardinality constraints are desirable; tier direction, lifecycle, authority mode, and projection-currentness may remain deterministic validator rules if every ingestion transaction runs them before publication. **Confidence: 92%.** Missing evidence: an authoritative relation-by-source-type/target-type/cardinality matrix. Consequence: this distinction determines whether TypeDB's semantic strength is necessary or merely elegant. **Next action:** generate the complete rule matrix from current GOV/SPEC authority and mark each rule `engine`, `ingest-validator`, or `post-ingest-diagnostic`.

3. **Does `data.js inside` mean one sibling JavaScript snapshot shared by pages, one JavaScript file per page, or data literally inlined in each HTML page?** Best current answer: use content-hashed shared `data.<frontier>.js` plus real HTML pages so publication is cacheable and every page exposes the same frontier. **Confidence: 85%.** Missing input: desired offline-opening and asset layout. Consequence: it changes atomic publication and browser security behavior. **Next action:** choose the exact static-site package contract before the spike's export scenario is frozen.

4. **Should archived Atoms be loaded alongside active Atoms?** Best current answer: yes, as source history with explicit lifecycle columns; active marts filter them out by default. **Confidence: 92%.** Missing input: whether every archive is semantically parseable under the current schema or needs edition-specific decoding. Consequence: excluding archives prevents historical lineage queries; treating them as current pollutes operational views. **Next action:** define archive decoding/version rules and one historical-lineage acceptance case.

5. **Where should the database and generated site live?** Best current answer: keep the disposable database, watcher state, and build staging under `.caprmedio_runtime`; publish only governed Projection outputs to their configured destination. **Confidence: 92%.** Missing input: whether generated HTML/data.js should be committed, ignored, or always runtime-only. Consequence: this affects repository noise, offline use, and currentness validation. **Next action:** declare the publication destination and retention policy independently from the database engine.

## Skills used

- `fpf-options-explore` — generated and compared mechanism-diverse database candidates, preserved the partial-order result, and defined the decision evidence still required.

#### FPF sources consulted (3 read; 3 used)

- `FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/04_05_Canonical Reasoning Cycle/02_Abductive Loop/02_B.05.02.01 - Creative Abduction with NQD.md` — **used**: candidate diversity, declared coordinates, provenance, and non-dominated-front discipline
- `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/10_09_Parity and Benchmark Harness/00_G.09 - Parity and Benchmark Harness.md` — **used**: parity plan/report, pinned baselines, comparable scenarios, and partial-order outcome
- `FPF-Knowledge-Graph/00_Index/FPF - Index.md` — **used**: FPF edition identity and direct-pattern navigation
