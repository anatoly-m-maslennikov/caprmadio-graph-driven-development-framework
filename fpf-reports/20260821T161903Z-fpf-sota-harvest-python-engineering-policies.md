## Task, scope, and boundaries

### Harvest contract

**Question.** What current Python engineering methods, evaluation methods, and resulting technical qualities are appropriate for CAPRMEDIO's active file tools, background processes, Codex hooks, and Git hooks when the purpose is fast building, modification, diagnosis, and repair without sacrificing runtime performance, traceability, or useful level-based logs?

**Receiving use.** This pack is evidence for a later, compact set of project M, E, and D policies. It does not select, accept, or implement those policies.

**Entity of concern.** The Python realization of the CAPRMEDIO framework engine, including installed copies and runtime behavior.

**Audience and authority.** The project Operator is the decision owner. Sources and this synthesis inform that decision but do not establish project authority.

**Freshness boundary.** Evidence was retrieved on 2026-08-21. Python 3.14 is treated as the latest stable language line because the Python 3.14 documentation identifies it as the latest stable release. Pre-release or experimental facilities are not treated as defaults.

**Included source classes.** Current project carriers and code, the bounded FPF harvesting patterns, current official Python and PEP documentation, and maintainers' documentation for candidate engineering tools.

**Excluded.** Functional product requirements, detailed specifications for individual tools, archived Principles, generic popularity lists, secondary tutorials where primary documentation was available, and implementation changes.

**Saved report:** `fpf-reports/20260821T161903Z-fpf-sota-harvest-python-engineering-policies.md`

### Current project evidence

The active input is the working-tree state at Git `d8ced0181f4ff7a366ad720e26c3ea528d63ae03`, not a claim that the large local migration is already committed.

- The active Principle snapshot contains 20 non-archived carriers across P, R, M, E, D, and O.
- The local interpreter is Python 3.14.7, while `.github/workflows/publish-release.yml` explicitly runs Python 3.12. No project-level `pyproject.toml` or `requires-python` declaration was found.
- A read-only AST inventory of `102_FRAMEWORK_ENGINE/TOOLS` found 40 Python files and 17,626 lines: 34 production files, 6 test files, and 17 migration files.
- The same inventory found 740 functions, 38 classes, 108 methods, 6 nested functions, 148 functions longer than 25 physical lines, and 31 files longer than 200 lines. These are descriptive counts, not quality conclusions.
- The inventory found 0 standard logging calls, 82 `print` calls, 709 f-string nodes, and 3 calls with `shell=True`.
- Imported roots were standard-library or repository-local modules. No third-party runtime dependency was evident in the scanned tools.

### Active Principle snapshot

The digest prefixes below pin the exact working-tree evidence used by this harvest.

| Principle | Version | SHA-256 prefix | Constraint used here |
|---|---:|---|---|
| CA-P-032 | 2 | `e507329393fb` | Attribute governed actions to Operator or AI Agent |
| CA-P-033 | 5 | `9831414e72e9` | Operator performs or authorizes governed actions |
| CA-P-034 | 4 | `62ec15ec5b52` | AI Agents act only within delegated authority |
| CA-R-004 | 10 | `b047af706d8c` | Preserve Operator control of the CAPRMEDIO instance |
| CA-R-815 | 8 | `2832f7befda0` | Support Operator priorities for trade-offs |
| CA-R-819 | 7 | `fb7f08685a11` | Avoid requiring specialist craft work from human participants |
| CA-R-827 | 6 | `06c24d24b0ba` | Preserve Operator control of the project |
| CA-R-846 | 4 | `61d7d2e1282e` | Make AI delegation inspectable and revocable |
| CA-R-861 | 1 | `d920d3ff6f76` | Produce a working and evolvable framework |
| CA-M-001 | 5 | `d27fe35f4a70` | Use MECE only for declared canonical universes |
| CA-M-002 | 7 | `e9a0dd913d55` | Give governed meaning one canonical owner |
| CA-M-003 | 7 | `3142289a765d` | Preserve necessary information and expose a sufficient subset |
| CA-M-005 | 5 | `e12ada6660e7` | Admit complexity only when needed for an outcome or distinction |
| CA-M-006 | 5 | `c92c0fa948c3` | Keep shared meaning discipline-independent |
| CA-E-001 | 6 | `a67e05ec047f` | Make accepted Requirements checkable |
| CA-E-002 | 8 | `2d0fda183a8c` | Bind reliance to evidence, uncertainty, and reliance conditions |
| CA-D-001 | 12 | `066c806887e6` | Keep technical realizations replaceable within prerequisites |
| CA-D-002 | 10 | `d0e7cc060db0` | Make governed meaning sufficient for Operator use |
| CA-D-003 | 8 | `f2489ffdf8d3` | Keep one typed graph as the canonical operating representation |
| CA-O-003 | 11 | `4281d290ce99` | Turn observed outcomes into narrow evaluated improvements |

### Source-use rules and stop condition

Primary or maintainer-owned documentation was preferred. Recency alone was not treated as superiority. A source was used only for claims within its stated scope. Rival approaches were kept separate unless a bounded bridge was supportable. The harvest stops at an evidence-backed palette of policy themes; selection and policy authoring belong to the next call.

## High-confidence results (>=95%)

### CorpusLedger and coverage boundary

| ID | Source and edition | Status | Evidence role |
|---|---|---|---|
| L01 | Active CAPRMEDIO Principle carriers, working tree at 2026-08-21 | Include | Project constraints and decision authority |
| L02 | `102_FRAMEWORK_ENGINE/TOOLS`, read-only AST inventory, Python 3.14.7 | Include | Current realization shape and observable gaps |
| L03 | `.github/workflows/publish-release.yml` and local interpreter | Include | Runtime compatibility boundary |
| F01 | FPF `G.02 - SoTA Harvester & Synthesis` | Include | Plural corpus, claim sheets, palette, and refresh discipline |
| F02 | FPF `G.0 - Frame Standard and Comparability Governance` | Include | Explicit frame and lawful comparison boundary |
| F03 | FPF `G.07 - Cross-Tradition Bridge Calibration Kit` | Include | Loss-aware bridges without silent fusion |
| P01 | [Python 3.14 release notes](https://docs.python.org/3.14/whatsnew/3.14.html), Python 3.14.7 docs | Include | Latest stable language boundary and new facilities |
| P02 | [PEP 8](https://peps.python.org/pep-0008/) | Include | Readability, consistency, compatibility, and judgment |
| P03 | [PEP 750](https://peps.python.org/pep-0750/), final for Python 3.14 | Include | Structured template strings and their non-string semantics |
| P04 | [PEP 544](https://peps.python.org/pep-0544/) | Include | Structural interfaces and replaceability without nominal inheritance |
| P05 | [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html) and [dataclasses](https://docs.python.org/3.14/library/dataclasses.html) | Include | Multi-paradigm boundary and data-object facilities |
| P06 | [Python Logging HOWTO](https://docs.python.org/3.14/howto/logging.html) and [Logging Cookbook](https://docs.python.org/3.14/howto/logging-cookbook.html) | Include | Severity levels, context, queues, and non-blocking logging patterns |
| P07 | [asyncio TaskGroup documentation](https://docs.python.org/3.14/library/asyncio-task.html#task-groups) | Include | Structured concurrency for related asynchronous work |
| P08 | [cProfile documentation](https://docs.python.org/3.14/library/profile.html) and [pyperf 2.10](https://pyperf.readthedocs.io/en/latest/) | Include | Profiling and repeatable benchmark evidence |
| P09 | [subprocess security](https://docs.python.org/3.14/library/subprocess.html#security-considerations), [tempfile](https://docs.python.org/3.14/library/tempfile.html), and [`os.replace`](https://docs.python.org/3.14/library/os.html#os.replace) | Include | Safe process and file-effect boundaries |
| P10 | [PyPA `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/) | Include | Canonical runtime and tool configuration carrier |
| T01 | [Ruff documentation](https://docs.astral.sh/ruff/) | Include | Fast formatting/linting, caching, and current syntax upgrades |
| T02 | [mypy 2.3 documentation](https://mypy.readthedocs.io/en/stable/existing_code.html) | Include | Gradual static checking, strictness ratchet, and incremental checking |
| T03 | [pytest good practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html) | Include | Isolated tests, installed-code testing, and strict configuration |
| T04 | [Hypothesis 6.165 documentation](https://hypothesis.readthedocs.io/en/latest/) | Include | Property-based and stateful input exploration |
| T05 | [Coverage.py 7.15 branch coverage](https://coverage.readthedocs.io/en/latest/branch.html) | Include | Observation of unexecuted branches, not correctness proof |
| O01 | [OpenTelemetry Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) and [log concepts](https://opentelemetry.io/docs/concepts/signals/logs/) | Include with boundary | Correlated telemetry schema; Python log implementation remains in development |
| H01 | [Git hooks documentation](https://git-scm.com/docs/githooks) | Include | Synchronous commit gates and exit semantics |

The corpus intentionally parks Black, Flake8, pylint, pyright, structlog, Pydantic, and daemon frameworks. Their relevant method families are already represented by admitted sources; adding them now would increase breadth without changing the comparison frame. They remain valid refresh candidates if a later option depends on a capability absent from this corpus.

### Flow record

1. Identified the current project surfaces, 20 active Principles, 40 Python files, local Python 3.14.7, and the Python 3.12 release workflow.
2. Screened the FPF graph by title and opened three direct patterns: harvesting, comparison-frame governance, and bridge calibration.
3. Admitted official Python language, standard-library, packaging, testing, typing, performance, observability, and Git-hook sources.
4. Parked redundant tool families and secondary tutorials.
5. Distilled claims per tradition without selecting a policy bundle.
6. Built bounded bridges and recorded losses or non-substitutability.
7. Stopped when every declared execution surface had at least one method family for implementation, evaluation, performance, and diagnostics.

### ClaimSheets and evidence anchors

#### CS-01 — Stable runtime first, current idioms second

**Source claim.** Python 3.14 is the latest stable release and adds t-strings, deferred annotations, improved asyncio inspection, and a safe external debugger interface. PEP 8 explicitly warns against breaking compatibility merely to follow a style recommendation. The packaging specification provides `requires-python` for declaring the supported interpreter range.

**Reviewer synthesis.** “Use the newest pattern” is sound only after the supported runtime is explicit. CAPRMEDIO currently has a real 3.12/3.14 split; therefore Python 3.14-only syntax cannot yet be a universal project policy.

**Principle fit.** Supports CA-R-861, CA-M-005, CA-D-001, CA-E-002, and Operator priorities in CA-R-815.

**Confidence: 99%.** Evidence is direct in the release workflow, local interpreter, Python release documentation, PEP 8, and PyPA specification.

#### CS-02 — T-strings are structured templates, not newer f-strings

**Source claim.** A t-string returns `string.templatelib.Template`, has no canonical `Template.__str__()`, and is intended for custom processing such as validated HTML, safe domain-specific processing, or structured logging. An f-string returns an ordinary string.

**Reviewer synthesis.** Use f-strings for immediate trusted string construction. Use t-strings only when a processor needs the interpolation structure. Replacing f-strings mechanically with t-strings would change types and behavior and would fail under Python 3.12.

**Principle fit.** Supports CA-M-005, CA-D-001, and CA-D-002; avoids novelty-driven complexity.

**Confidence: 99%.** [PEP 750](https://peps.python.org/pep-0750/) is final and explicit about the type and absence of canonical string conversion.

#### CS-03 — Python remains deliberately multi-paradigm

**Source claim.** Python supports procedural, object-oriented, and functional styles; its own HOWTO states that different sections of a large program may appropriately use different approaches. Protocols allow structural interfaces without forcing explicit inheritance, while dataclasses reduce data-carrier boilerplate.

**Reviewer synthesis.** No admitted primary source supports “use OOP everywhere.” For CAPRMEDIO, a defensible bridge is: pure or mostly pure functions for deterministic transformations; immutable or frozen data objects for stable values; objects for owned state, lifecycle, resources, or polymorphic adapters; Protocols at replaceable boundaries; composition before inheritance.

**Principle fit.** Supports CA-M-005, CA-D-001, CA-M-002, and CA-D-002.

**Confidence: 97%.** The multi-paradigm and structural-interface claims are direct; the CAPRMEDIO allocation is a bounded synthesis rather than a universal Python rule.

#### CS-04 — Automated style, lint, and typing are complementary

**Source claim.** PEP 8 prioritizes readability and project consistency while allowing justified exceptions. Ruff combines fast formatting, linting, upgrade rules, and caching. Mypy recommends starting with a bounded passing subset, preventing regressions, and ratcheting toward stricter checking; its daemon accelerates incremental runs.

**Reviewer synthesis.** Formatting should remove style negotiation, linting should catch mechanical defects, and typing should check interface consistency. They do not replace tests or runtime validation. A single canonical configuration should own interpreter targets and tool rules.

**Principle fit.** Supports CA-M-002, CA-M-005, CA-R-819, CA-E-001, and CA-D-002.

**Confidence: 98%.** The roles and incremental adoption boundaries are explicit in the maintainers' documentation.

#### CS-05 — Tests need several evidence forms

**Source claim.** Pytest recommends isolated environments and testing installed code. Hypothesis explores generated inputs and unanticipated edge cases. Branch coverage identifies unexecuted control-flow alternatives that statement coverage can miss.

**Reviewer synthesis.** Example tests, integration tests, property/state-machine tests, and branch coverage answer different questions. Coverage is navigation evidence, not proof of correctness. Tests should emphasize public behavior and failure boundaries rather than mirror implementation structure.

**Principle fit.** Supports CA-E-001, CA-E-002, CA-R-861, and CA-O-003.

**Confidence: 98%.** Each evidence form and its boundary is directly documented.

#### CS-06 — Logs should be structured, contextual, and levelled

**Source claim.** Python logging defines `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`; the cookbook supports contextual records and queue-based handling when handlers would block. OpenTelemetry defines structured records with timestamp, severity, body, resource, instrumentation scope, trace ID, and span ID, and explains correlation across logs and traces.

**Reviewer synthesis.** CAPRMEDIO tools should emit stable structured diagnostic records with severity and action context while keeping concise human-readable CLI outcomes. Operational logs should not redefine governed Work Journal meaning; they should reference the canonical action/event identifiers.

**Principle fit.** Supports CA-P-032, CA-M-002, CA-M-003, CA-E-002, CA-D-002, CA-D-003, and CA-O-003.

**Confidence: 99%.** Field meanings and severity semantics are directly documented. The log-versus-journal ownership split follows CAPRMEDIO DRY and graph Principles.

#### CS-07 — OpenTelemetry is an optional bridge, not a current default

**Source claim.** The OpenTelemetry log signal is stable at the specification level, but the Python logs implementation is documented as “Development.” Python's built-in logging can already produce structured and contextual records.

**Reviewer synthesis.** Define a neutral internal log/event schema first. Add an OpenTelemetry exporter only when cross-process correlation or an external backend is actually required. This preserves replaceability and avoids a premature runtime dependency.

**Principle fit.** Supports CA-M-005, CA-D-001, CA-M-002, and CA-R-815.

**Confidence: 99%.** The implementation maturity boundary is explicit in current OpenTelemetry documentation.

#### CS-08 — File and subprocess effects require explicit safety boundaries

**Source claim.** `subprocess` does not invoke a shell implicitly; with `shell=True`, quoting and injection safety become the application's responsibility. `tempfile` supplies securely created temporary carriers. On the same POSIX filesystem, `os.replace` provides atomic replacement.

**Reviewer synthesis.** File-changing tools should plan and validate before mutation, write through a same-filesystem temporary carrier, replace atomically where supported, and report recoverable failure. Subprocess calls should use argument arrays, explicit timeouts, checked exit status, controlled environment, and `shell=False` by default.

**Principle fit.** Supports CA-R-004, CA-R-827, CA-R-846, CA-E-001, CA-D-001, and CA-R-861.

**Confidence: 99%.** The mechanisms and their platform boundaries are directly documented.

#### CS-09 — Structured concurrency is preferable when concurrency is real

**Source claim.** `asyncio.TaskGroup` reliably awaits related tasks and offers stronger failure safety than unstructured `gather()` nesting by cancelling remaining related tasks after a child failure.

**Reviewer synthesis.** Background services that genuinely need asynchronous concurrency should use structured task ownership, explicit cancellation, bounded shutdown, and visible failure propagation. Synchronous tools should remain synchronous when concurrency would add no measured benefit.

**Principle fit.** Supports CA-M-005, CA-R-861, CA-D-002, and CA-E-002.

**Confidence: 98%.** The TaskGroup behavior is direct; the “only when real” constraint follows the necessary-complexity Principle.

#### CS-10 — Hook critical paths must remain minimal

**Source claim.** Git pre-commit and commit-msg hooks execute synchronously and abort the commit on non-zero exit. In this session, even trivial read-only commands repeatedly incurred substantial end-to-end latency while the installed hook pipeline observed the operation.

**Reviewer synthesis.** A hook should perform only the smallest deterministic gate or durable trigger needed before the host action continues. Expensive graph scans, broad tests, indexing, and enrichment should use changed-target scopes, caches, background processing, or later explicit gates. The hook must still fail closed for the narrow invariant it owns.

**Principle fit.** Supports CA-R-819, CA-R-861, CA-M-003, CA-M-005, CA-R-815, and CA-O-003.

**Confidence: 96%.** Git's synchronous semantics are direct. The CAPRMEDIO latency attribution is a strong session observation but has not yet been isolated by a controlled benchmark.

#### CS-11 — Performance claims require profiles and reproducible benchmarks

**Source claim.** `cProfile` records call counts and execution time and is recommended for most users. `pyperf` calibrates runs, uses multiple workers, detects unstable results, preserves metadata, and compares benchmark suites.

**Reviewer synthesis.** Optimize measured bottlenecks, not code appearance. Keep separate budgets for interactive hooks, batch file tools, and background services. Preserve benchmark inputs, environment metadata, baseline, result distribution, and regression threshold.

**Principle fit.** Supports CA-E-002, CA-R-815, CA-O-003, CA-M-005, and CA-R-861.

**Confidence: 99%.** The evidence facilities and stability controls are directly documented.

#### CS-12 — Fixed size limits are guardrails, not established quality laws

**Source claim.** PEP 8 governs readability and consistency but does not define universal maximum file, class, or function sizes. Automated formatters deliberately avoid deciding architecture.

**Reviewer synthesis.** A 25-line function or 200-line file threshold can be a project heuristic, but crossing it is not itself a defect and satisfying it is not itself evidence of good design. Stronger evaluation checks cohesion, responsibility, dependency direction, cyclomatic paths, change locality, and testability. Any hard threshold needs an Operator-established purpose and exception process.

**Principle fit.** Supports CA-M-005, CA-E-001, CA-E-002, CA-D-002, and CA-R-815.

**Confidence: 97%.** The negative finding is stable across the admitted primary style and tooling sources.

### SoTA_Set and traditions

| Tradition | Characteristic method | Strength | Limit or failure mode | CAPRMEDIO applicability |
|---|---|---|---|---|
| Stable-language/stdlib-first | Declare runtime; prefer stable stdlib facilities | Low dependencies and high replaceability | Can lag useful ecosystem automation | Runtime code and installed tools |
| Current-idiom modernization | Adopt newer syntax and APIs inside a declared runtime | Less boilerplate and safer primitives | Compatibility breaks when the boundary is implicit | New code and deliberate migrations |
| Multi-paradigm modular design | Allocate functions, data objects, stateful objects, and interfaces by responsibility | Good change locality without one dogma | Can become inconsistent without boundaries | Parsers, planners, adapters, services |
| Static automation | Formatter, linter, upgrade rules, type checker | Fast deterministic feedback | False confidence if treated as behavioral proof | Every maintained Python carrier |
| Behavioral and generative testing | Example, integration, property, stateful, and failure tests | Finds regressions and edge cases | Cost and flakiness if scope is uncontrolled | File transforms, protocols, lifecycle tools |
| Observability and event correlation | Structured logs, severity, context IDs, traces when justified | Diagnosis and operational learning | Log volume, blocking handlers, duplicate truth | Background services, hooks, multi-step tools |
| Evidence-based performance | Profiles, representative benchmarks, explicit budgets | Prevents speculative optimization | Benchmarks mislead when environment or workload drifts | Hook latency, scans, serialization, startup |
| Boundary resilience | Atomic file effects, safe subprocesses, explicit cancellation and shutdown | Preserves control under failure | Platform-specific guarantees need declaration | Doers, installers, hooks, services |

### Comparison palette

The downstream policy comparison should use these separate coordinates rather than one aggregate score:

1. Time to implement or modify a governed behavior.
2. Time to obtain useful failure localization.
3. Interactive latency for hooks and CLI commands.
4. Batch throughput and memory use for repository-scale work.
5. Behavioral confidence and recoverability of evidence.
6. Operator understandability of code, diagnostics, and failures.
7. Dependency and operational complexity.
8. Runtime and platform compatibility.
9. Replaceability of adapters, tools, and telemetry sinks.
10. Traceability from action through log, journal, commit, and graph state.

No scalar ranking is asserted. CA-R-815 gives the Operator authority to establish priorities among these trade-offs.

### BridgeMatrix

| Traditions bridged | Bounded correspondence | Explicit loss or non-substitutability |
|---|---|---|
| New syntax ↔ stable runtime | New facilities are admissible inside the declared interpreter range | “Newer” cannot override compatibility |
| Functional ↔ object-oriented | Functions fit transformations; objects fit owned state and lifecycle | Neither paradigm universally replaces the other |
| Protocols ↔ inheritance | Both can define substitutable behavior | Protocols do not supply shared implementation or runtime invariants |
| Formatting/linting ↔ readability | Automation creates consistency and removes mechanical defects | It cannot establish cohesion or understandable architecture |
| Typing ↔ testing | Types constrain interfaces; tests observe behavior | Neither substitutes for the other |
| Coverage ↔ correctness | Missing branches reveal missing observations | High coverage does not prove correct behavior |
| Logs ↔ Work Journal | Both can carry action identifiers and timestamps | Logs diagnose operations; the Journal owns governed event history |
| Logging ↔ tracing | Trace/span IDs can correlate records across operations | Full tracing adds dependency and operational cost |
| Profiling ↔ benchmarking | Profiling locates cost; benchmarks compare representative outcomes | Microbenchmarks do not establish end-to-end performance |
| Hook gates ↔ background evaluation | Hooks establish narrow synchronous gates; background work can enrich or scan broadly | Deferred checks cannot replace a required pre-action invariant |

No fusion or free substitution across traditions is asserted. Every bridge above retains its stated loss.

### Operator and object inventory for downstream policy authoring

These are stubs, not accepted policies or thresholds.

#### Candidate M themes

1. Declare one canonical supported-Python and tool configuration boundary.
2. Use stable current idioms only when they improve a declared quality inside that boundary.
3. Separate deterministic transformation logic from I/O and lifecycle ownership.
4. Use explicit, typed, replaceable interfaces at technical boundaries.
5. Make file and subprocess effects planned, validated, bounded, and recoverable.
6. Keep synchronous hook work minimal and move non-gating work off the critical path.
7. Emit structured contextual logs through one logging abstraction and schema.
8. Profile and benchmark before accepting performance changes.
9. Ratchet automation and typing without blocking all current work at once.

#### Candidate E themes

1. Parse/format/lint/type-check every changed Python target under one pinned configuration.
2. Test public behavior across unit, integration, property/stateful, and failure cases as applicable.
3. Validate branch observations without treating a coverage percentage as correctness.
4. Test the installed realization under every supported Python/platform boundary.
5. Validate log schema, severity, correlation identifiers, and secret exclusion.
6. Benchmark interactive, batch, and background performance separately against pinned baselines.
7. Exercise interruption, partial writes, subprocess failure, timeout, and restart behavior.

#### Candidate D themes

1. A self-contained installed toolset with an explicit runtime prerequisite envelope.
2. Small replaceable adapters around a shared deterministic semantic core.
3. Stable machine-readable CLI envelopes plus concise human diagnostics.
4. Atomic or explicitly recoverable mutation outcomes.
5. Structured diagnostic records linked to canonical project action identifiers.
6. Code whose responsibilities and public interfaces remain understandable without specialist framework knowledge.

### Microexamples

#### File metadata updater

Parse and validate Markdown/TOML into typed values, compute a pure change plan, render to a same-filesystem temporary file, and atomically replace the target. Example tests cover known cases; property tests vary Unicode, line endings, missing fields, and idempotence; failure tests interrupt before replacement. This combines transformation, boundary resilience, and evidence without requiring an object hierarchy for the pure core.

#### Git or Codex hook

Parse the host event, identify the smallest changed target set, perform the one required synchronous gate, emit a correlated trigger, and return. Broad graph scans or journal enrichment run only after the critical host action when their result is not required to permit it. A latency benchmark and recursion test are part of the evidence.

#### Background service

Own lifecycle state in a service object, keep work functions separately testable, use structured task ownership only when concurrent work exists, handle termination explicitly, and send log records through a non-blocking queue if the sink can stall. Tests cover startup, duplicate start, cancellation, child failure, and clean shutdown.

#### Human and structured message rendering

Use an f-string for an immediate trusted CLI sentence. Use a t-string only when a logging or rendering processor must preserve field identities, apply escaping, or emit both human and structured forms. Compatibility tests prevent Python 3.14 syntax from entering a Python 3.12 execution path.

### Alignment with the active Principles

- **Operator authority and delegation:** deterministic dry-runs, explicit effects, visible diagnostics, and inspectable configuration preserve CA-P-032–034, CA-R-004, CA-R-827, and CA-R-846.
- **Operator priorities:** separate quality coordinates and performance budgets let CA-R-815 govern real trade-offs instead of hiding them in one style score.
- **Operation without specialist craft:** automated checks, stable CLI envelopes, and actionable logs support CA-R-819 without hiding failures.
- **Working and evolvable framework:** compatibility declarations, replaceable interfaces, tests, and observability support CA-R-861.
- **MECE and DRY:** distinct method families avoid conflating style, types, tests, logs, and performance; one configuration and one event owner prevent duplicate governing meaning under CA-M-001 and CA-M-002.
- **Selective exposure and necessary complexity:** contextual diagnostics and optional telemetry expose what a task needs while CA-M-003 and CA-M-005 prevent always-on machinery.
- **Discipline-independent meaning:** language-specific code realizes rather than redefines shared CAPRMEDIO semantics, supporting CA-M-006.
- **Checkability and bounded reliance:** deterministic checks, explicit benchmark evidence, and stated uncertainty support CA-E-001 and CA-E-002.
- **Replaceability and understandability:** Protocol-like boundaries, neutral schemas, concise diagnostics, and mixed-paradigm allocation support CA-D-001 and CA-D-002.
- **One project graph and improvement loop:** logs reference canonical action identities, while observed failures and performance evidence can feed narrow proposals under CA-D-003 and CA-O-003.

### Disagreements, exclusions, and insufficient basis

- **OOP versus functional style:** the evidence supports Python as multi-paradigm, not an OOP default. A contextual allocation is supportable; a universal mandate is not.
- **Strictness immediately versus ratcheting:** strict end states can be valuable, but current mypy and pytest guidance explicitly recognizes staged adoption and pinned strictness.
- **Stdlib-only versus third-party automation:** runtime simplicity favors stdlib-only tools; development speed and defect detection favor Ruff, a type checker, pytest, Hypothesis, and coverage. The corpus does not authorize which dependencies CAPRMEDIO should accept.
- **Structured logs versus full telemetry:** stable structured logs are well supported; OpenTelemetry's Python log implementation remains developmental, so full telemetry is not established as the default.
- **Hard code-size limits:** there is insufficient primary-source basis for treating 25 function lines or 200 file lines as universal quality laws. They remain possible local warning thresholds.
- **Performance thresholds:** the corpus supports measurement methods but contains no CAPRMEDIO workload-specific latency, throughput, or memory thresholds.
- **Platform guarantees:** atomic replacement and process behavior vary by operating system and filesystem. The current corpus does not prove a complete Windows/macOS/Linux compatibility envelope.

### Receiving use and refresh condition

The immediate handoff is the candidate M/E/D inventory, ClaimSheets, comparison palette, and open questions for `fpf-options-explore`. That call should produce several compact policy bundles rather than copy this entire evidence pack into normative Atoms.

Refresh this harvest when any of the following changes:

- the declared minimum Python version;
- a supported operating system or installation model;
- the active Principle digest set;
- the accepted runtime dependency policy;
- Python's stable release line;
- pytest, mypy, Ruff, or OpenTelemetry maturity in a way that affects an active candidate;
- measured CAPRMEDIO hook, batch, or background-service performance.

## Open questions (confidence <95%)

### What is the authoritative supported Python range?

**Best current answer:** Python 3.12 is the lowest evidenced execution boundary because the release workflow pins it; Python 3.14.7 is the current local development interpreter.

**Confidence: 93%.** There is no project-level runtime declaration, so the workflow may be incomplete evidence rather than intended policy.

**Missing evidence:** an Operator-accepted `requires-python` or equivalent runtime prerequisite carrier.

**Consequence:** t-strings and other Python 3.14-only facilities cannot safely become universal project patterns.

**Next action:** establish the supported range before authoring syntax or tooling policies.

### Which third-party tools may become project prerequisites?

**Best current answer:** keep runtime code stdlib-first; consider Ruff, typing, pytest, Hypothesis, coverage, and pyperf as isolated development or evaluation dependencies only when their benefit is accepted.

**Confidence: 92%.** The code is currently stdlib-only, but no explicit dependency-admission policy was found.

**Missing evidence:** installation, update, offline-use, lockfile, and supply-chain requirements.

**Consequence:** selecting an attractive tool could violate replaceability or local-only operation.

**Next action:** compare a stdlib-only bundle, a minimal fast-tool bundle, and a fuller assurance bundle in the options call.

### What performance budgets should govern each execution surface?

**Best current answer:** hooks need the tightest budget, interactive CLI tools a larger but still bounded budget, and background/batch tools separate throughput and memory budgets.

**Confidence: 91%.** The ordering is operationally probable, but no representative workloads or accepted thresholds exist.

**Missing evidence:** benchmark fixtures, repository sizes, cold/warm start measurements, and Operator priorities.

**Consequence:** “fast” cannot yet produce a binary E result.

**Next action:** capture representative workloads and baseline hook, CLI, and background-service measurements.

### How should logs and the Work Journal divide ownership?

**Best current answer:** the Work Journal owns governed action history; logs own diagnostic observations and reference the same canonical action/event identifiers.

**Confidence: 93%.** This follows the active DRY and graph Principles, but a current explicit schema boundary was not inspected in this harvest.

**Missing evidence:** accepted retention, privacy, redaction, correlation, and diagnostic-event schemas.

**Consequence:** implementations may duplicate governed meaning or omit necessary diagnostic detail.

**Next action:** make the boundary explicit during policy option generation and test it against current Journal atoms.

### Should CAPRMEDIO adopt OOP as the recommended Python style?

**Best current answer:** no universal OOP recommendation; recommend responsibility-based multi-paradigm design, with objects for owned state and lifecycle and functions for deterministic transformations.

**Confidence: 93%.** This is strongly supported as a practical synthesis, but exact allocation criteria remain a project design choice.

**Missing evidence:** change-history and defect data showing which current modules suffer from state scattering, oversized procedural flows, or inappropriate classes.

**Consequence:** a universal OOP rule could add boilerplate and inheritance without improving change locality.

**Next action:** compare the mixed-paradigm rule against representative file tool, hook, and service refactors before acceptance.

### What is the supported platform envelope?

**Best current answer:** current operation is macOS-local, while the release workflow provides some Ubuntu evidence; Windows support is not established here.

**Confidence: 90%.** The repository contains cross-platform intentions, but this harvest did not execute a platform matrix.

**Missing evidence:** an accepted platform Requirement and current passing installations/tests per platform.

**Consequence:** file locking, atomic replacement, process groups, signals, and hooks may behave differently.

**Next action:** declare the platform envelope and make platform-specific mechanisms explicit adapters.

## Skills used

- `fpf-sota-harvest` — built a bounded, plural, reconstructible evidence pack for later CAPRMEDIO Python-policy options.

#### FPF sources consulted (3 read; 3 used)

- `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/03_02_SoTA Harvester & Synthesis/00_G.02 - SoTA Harvester & Synthesis.md` — **used**: corpus, claim-sheet, palette, plurality, and refresh structure.
- `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/01_00_Frame Standard and Comparability Governance - CG-Spec/00_G.0 - Frame Standard and Comparability Governance - CG-Spec.md` — **used**: explicit comparison frame, separate coordinates, and evidence boundaries.
- `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/08_07_Cross-Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT-Sentinels)/00_G.07 - Cross-Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT-Sentinels).md` — **used**: bounded, loss-aware bridges and refusal of silent substitution.
