---
cce_version: cce_1
cce_form: rationale
subjects:
  governs:
    continuant:
      - programmatic-tool-language-options
      - programmatic-tool-stack-profiles
    occurrent:
      - state-of-the-art-harvest
      - comparative-analysis
  depends_on:
    continuant:
      - TOOLS
relations:
  analysis_of:
    - CA-R-1186
atom_id: CA-A-067
version: 1
updated_at: 2026-09-09 04:43:50
---
# Python vs Go for CAPRMEDIO Tools: SoTA harvest

## Task, scope, and boundaries

This is a read-only, dated evidence harvest for a later operator decision about Python versus Go for CAPRMEDIO's actual Programmatic Tools. The receiving use is a subsequent evaluation or decision step, not a language selection here. The target includes the live graph and Atom read/write commands, generators, compilers, migrations, Git commit and hook tooling, project-local installation and launchers, and the currently empty background-service registry. It excludes implementation, repository changes, local performance benchmarks, tool redesign, and claims about future App or MCP workloads that are not represented by the current implementation.

The live baseline was inspected on 2026-09-09. It contains 16 public launchers and approximately 23,121 lines across 65 production Python files, plus approximately 4,494 lines across 15 test files. The installer copies source into content-addressed project-local releases, and launchers invoke the selected host Python in isolated mode. Machine-facing commands already use versioned JSON result envelopes. The repository describes the toolchain as local-only and under active development, and `background_services.toml` currently declares no services.

The governing evidence is not a standard-library-only rule. Active `CA-M-110` prefers the Python standard library when it is comparably clear and reliable but permits a bounded, accepted library or non-Python exception. Active `CA-M-234` already selects Pydantic for untrusted structured Python boundaries. Active `CA-M-221` allows accepted dependencies in `pyproject.toml` and `uv.lock` while requiring installed releases to execute without uv or a project virtual environment. Root `pyproject.toml` currently declares no runtime dependencies and names two authority IDs that now resolve only to archived carriers; it is therefore evidence about the present materialization and freshness drift, not an operator constraint. The operator's correction—mature, well-adopted libraries are allowed in both ecosystems—is the controlling comparison premise.

The comparison is constrained by current CAPRMEDIO requirements: deterministic transformation cores separated from effects; prevalidated file and subprocess actions; explicit operation identity; recoverable partial failure; structured, sanitized diagnostics; compatibility across declared hosts; content-addressed installation separated from mutable runtime state; source and installed-tool conformance; and measurement on representative Hook, interactive, batch, MCP, App, or background workloads before optimization. Current active authority selects Python, so a Go or hybrid implementation would require an accepted bounded Method change; this harvest neither requests nor makes that change.

The research boundary admits live CAPRMEDIO authority/source/test carriers and primary or official language, toolchain, and library documentation available on 2026-09-09. A library is treated as a realistic candidate only when it has maintained official documentation or an active upstream, a stable release line, a credible installed base or ecosystem role, and a bounded purpose in the proposed stack. Popularity alone is not admission evidence. Secondary language shoot-outs, generic microbenchmarks, unsourced productivity claims, and abandoned packages are excluded. Exact dependency versions, licenses, transitive graphs, wheel/binary coverage, and vulnerability state must be refreshed at a later admission gate.

Outcome: `COMPLETE`. The harvest produced a reconstructible comparison and evidence gaps, but intentionally did not choose Python or Go.

## Issues, weak points, and improvements

### Native result

#### 1. Harvest contract and resolved source

- **Question:** What realistic, library-enabled Python and Go stacks could satisfy the current CAPRMEDIO Tool contracts, and what evidence is still required before choosing among them?
- **Entity of concern:** CAPRMEDIO's implemented Programmatic Tools and their project-local installation/runtime boundary.
- **Frame:** evolutionary Python, bundled Python, compiled Go, and staged hybrid implementation traditions; assessed against correctness, recoverability, deterministic interfaces, platform compatibility, dependency governance, packaging, maintainability, operational behavior, and migration cost.
- **Audience and receiver:** the CAPRMEDIO operator and maintainers preparing a later language/architecture decision.
- **Freshness boundary:** local checkout and external documentation observed on 2026-09-09. Language and library release facts require refresh before a decision if the evaluation begins after 2026-12-09 or if authority, supported hosts, or packaging constraints change sooner.
- **Evidence granularity:** exact local carrier or source path for CAPRMEDIO claims; official documentation/release locator for ecosystem claims; CAPRMEDIO-specific measurements for performance claims.
- **Disagreement policy:** retain rival approaches and mark unsupported bridges; do not convert generic ecosystem advantages into CAPRMEDIO-specific results.
- **Publication boundary:** final user-facing result for this approved Plan after validation; no durable report or repository mutation was requested.
- **Resolved method:** the graph-declared `G.2` harvesting method was used to keep a source ledger, separate source claims from synthesis and operator decisions, retain rival traditions, and expose missing evidence.

#### 2. Source ledger and coverage boundary

All web sources below were retrieved or checked on 2026-09-09. “Primary” means an official project, language, or upstream repository source—not that every project claim has independent third-party validation.

| ID | Source and edition/date | Role and admissibility | Evidence anchor |
|---|---|---|---|
| L-01 | CAPRMEDIO `README.md`, live checkout | Local primary; system boundary and principles | [`README.md`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/README.md) |
| L-02 | Root `pyproject.toml` and `uv.lock`, live checkout | Local materialization; current Python/dependency declaration, not governing authority | [`pyproject.toml`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/pyproject.toml), [`uv.lock`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/uv.lock) |
| L-03 | Active `CA-M-110`, `CA-M-234`, `CA-M-221`, `CA-M-229` | Local authoritative Methods; language, library, validation, workflow, and Python-version boundaries | [Programmatic Methods](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method) |
| L-04 | Active `CA-M-160`, `CA-M-161`, `CA-M-163`, `CA-M-165`, `CA-M-166` | Local authoritative Methods; architecture, effects, diagnostics, performance, compatibility | [Programmatic Methods](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method) |
| L-05 | Active `CA-R-1065`, `CA-M-223`, `CA-E-353`, `CA-E-354`, `CA-D-250` | Local authoritative requirement/method/evaluation/delivery carriers | [Tool authority](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS) |
| L-06 | Tool source and tests, live checkout | Local implementation evidence; inventory, interfaces, imports, behavior | [Tool tree](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS) |
| L-07 | `INSTALL_TOOLS/install_tools.py`, live checkout | Local implementation evidence; 16 launchers and content-addressed source-copy installation | [installer](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/INSTALL_TOOLS/install_tools.py) |
| L-08 | `background_services.toml`, live checkout | Local implementation evidence; service mechanism has no configured services | [service registry](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/background_services.toml) |
| PY-01 | CPython 3.14.7, 2026-08-05; lifecycle page current on retrieval | Official Python; current supported runtime and lifecycle | [3.14.7 release](https://www.python.org/downloads/release/python-3147/), [versions](https://devguide.python.org/versions/) |
| PY-02 | Python 3.14 documentation | Official Python; optional free-threading and experimental JIT limitations | [What's New](https://docs.python.org/3/whatsnew/3.14.html), [free-threading guide](https://docs.python.org/3/howto/free-threading-python.html) |
| PY-03 | Python 3.14 standard-library documentation | Official Python; shell-free subprocess and filesystem semantics | [`subprocess`](https://docs.python.org/3.14/library/subprocess.html), [`os`](https://docs.python.org/3.14/library/os.html) |
| PY-04 | uv project lock/sync documentation, current on retrieval | Official uv; locked exact synchronization and export options | [locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/) |
| PY-05 | Click, Typer, and Pydantic current documentation | Official projects; CLI and untrusted-boundary stack candidates | [Click](https://click.palletsprojects.com/en/stable/), [Typer](https://typer.tiangolo.com/tutorial/), [Typer/Click relationship](https://typer.tiangolo.com/tutorial/click/), [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/), [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/) |
| PY-06 | PyInstaller 6.22 documentation and current PEX documentation/repository | Official projects; distinct Python distribution traditions | [PyInstaller](https://pyinstaller.org/en/stable/operating-mode.html), [PEX upstream](https://github.com/pex-tool/pex), [PEX with included interpreter](https://docs.pex-tool.org/scie.html) |
| PY-07 | Ruff, pytest, and pip-audit current documentation/repository | Official projects; static checks, tests, and dependency vulnerability audit | [Ruff](https://docs.astral.sh/ruff/), [pytest parametrization](https://docs.pytest.org/en/stable/how-to/parametrize.html), [pip-audit](https://github.com/pypa/pip-audit) |
| PY-08 | PyYAML official documentation | Official project; YAML safety evidence, with documented API/stability caveats | [PyYAML documentation](https://pyyaml.org/wiki/PyYAMLDocumentation) |
| GO-01 | Go 1.27.1, 2026-09-01, and Go 1.27 notes | Official Go; current release and compatibility baseline | [release history](https://go.dev/doc/devel/release), [Go 1.27 notes](https://go.dev/doc/go1.27) |
| GO-02 | Go module and security documentation | Official Go; version graph, checksums, and reachability-aware vulnerability scanning | [module reference](https://go.dev/ref/mod), [vulnerability management](https://go.dev/doc/security/vuln/) |
| GO-03 | Cobra current documentation | Official project; mature hierarchical CLI candidate | [command guide](https://cobra.dev/docs/how-to-guides/working-with-commands/) |
| GO-04 | Go 1.27 package documentation | Official Go; subprocess, rename, and structured logging semantics | [`os/exec`](https://pkg.go.dev/os/exec), [`os`](https://pkg.go.dev/os), [`log/slog`](https://pkg.go.dev/log/slog) |
| GO-05 | go-playground/validator v10 repository, current on retrieval | Upstream project; optional validation candidate and maintenance/default-change risk | [validator](https://github.com/go-playground/validator) |
| GO-06 | YAML organization fork and two active TOML implementations | Upstream projects; configuration parser candidates and maintenance/API distinctions | [go-yaml v4](https://github.com/yaml/go-yaml), [go-toml v2](https://github.com/pelletier/go-toml), [BurntSushi/toml](https://github.com/BurntSushi/toml) |
| GO-07 | Go race detector and fuzzing documentation | Official Go; integrated dynamic concurrency and fuzz-test tools with explicit coverage limits | [race detector](https://go.dev/doc/articles/race_detector), [fuzzing](https://go.dev/doc/security/fuzz/) |
| DATA-01 | NetworkX 3.6.1 and Gonum graph v0.17 documentation | Official/upstream projects; optional graph-algorithm candidates, not default dependencies | [NetworkX reference](https://networkx.org/documentation/stable/reference/index.html), [Gonum graph](https://pkg.go.dev/gonum.org/v1/gonum/graph) |
| OBS-01 | OpenTelemetry language status and SDK documentation, current on retrieval | Official project; optional cross-language observability layer | [language status](https://opentelemetry.io/docs/languages/), [Go](https://opentelemetry.io/docs/languages/go/), [Python](https://opentelemetry.io/docs/languages/python/instrumentation/) |

Coverage is intentionally non-exhaustive. It is strong for the live CAPRMEDIO constraints, current Python/Go language baselines, representative CLI/validation/configuration/distribution choices, and official test/security facilities. It is incomplete for CAPRMEDIO-specific performance, full dependency/license audits, exact cross-platform artifacts, semantic round-trip fidelity, maintainer ergonomics, and migration effort. No generic benchmark was admitted as a substitute.

#### 3. Claim sheets and evidence anchors

| Claim ID | Source claim and anchor | Reviewer synthesis for CAPRMEDIO | Operator decision |
|---|---|---|---|
| CS-01 | Active `CA-M-110` allows bounded libraries or a non-Python exception; `CA-M-234` selects Pydantic. Root `pyproject.toml` has no runtime dependencies and references two archived authority IDs. L-02, L-03. | Standard-library-only is present implementation state, not the governing decision premise. The carrier drift must be reconciled independently of the language choice. | Mature, well-adopted libraries may be considered in both stacks. |
| CS-02 | The live tree is Python, exposes 16 launchers, uses content-addressed releases and isolated host-Python launch, and has a substantial existing test/source estate. L-06, L-07. | Python is the incumbent with material validated behavior; Go begins as a parity migration, not a greenfield comparison. | None; observation only. |
| CS-03 | CPython 3.14 is in bugfix support; 3.14.7 was current on the harvest date. PY-01. | The declared `==3.14.*` boundary is current, but exact patch/runtime availability remains a platform installation concern. | None. |
| CS-04 | Python free-threading is supported but optional; extension modules can re-enable the GIL. The JIT remains experimental and workload effects vary. PY-02. | Neither free-threading nor the JIT is admissible as a guaranteed CAPRMEDIO performance advantage. | None. |
| CS-05 | Click supplies explicit hierarchical CLI composition; Typer supplies type-hint-driven CLI construction and now vendors Click; Pydantic supports typed validation but coercion and extra-field policy are configurable. PY-05. | A realistic Python stack chooses direct Click or Typer as the CLI layer and uses strict Pydantic only at declared untrusted boundaries. Treating Click plus Typer as two separately justified runtime layers would double-count the same lineage. | None. |
| CS-06 | PyInstaller can ship without a target Python but builds per platform and one-file mode extracts at launch. Traditional PEX artifacts require a compatible target interpreter, while a PEX `--scie eager` artifact can include one. PY-06. | “Python packaging” is not one option: PyInstaller, traditional PEX, and interpreter-including PEX scies have different startup, security, size, build-matrix, cache/bootstrap, and rollback consequences. | None. |
| CS-07 | Go 1.27.1 is current; modules record version graphs/checksums, and `govulncheck` uses call-graph reachability. GO-01, GO-02. | Go provides a cohesive build, module, and vulnerability toolchain, but produced artifacts still need CAPRMEDIO host testing and provenance controls. | None. |
| CS-08 | `os/exec` does not invoke a shell by default; `os.Rename` documents platform-dependent replacement/atomicity behavior; `slog` supplies structured records. GO-04. Python exposes equivalent shell-free subprocess and replace primitives with platform qualifications. PY-03. | Both languages can satisfy the effect and diagnostic boundaries. Neither language removes filesystem atomicity differences; CAPRMEDIO must keep platform-aware verification. | None. |
| CS-09 | Go includes race detection and coverage-guided fuzzing, but the race detector only finds executed races and has material runtime/memory overhead and platform/cgo limits. GO-07. | Go has stronger integrated concurrency-test facilities; that is not evidence that current file/Git-heavy tools need concurrency or will be faster. | None. |
| CS-10 | Current Go YAML stewardship moved to an official YAML organization fork after the prior repository became unmaintained; the TOML candidates expose different stability and syntax-tree guarantees. GO-06. PyYAML distinguishes safe from unsafe loading and documents API caveats. PY-08. | “Well adopted” is necessary but insufficient. Maintenance transitions and preservation semantics are first-class risks for governed files in both ecosystems. | None. |
| CS-11 | CAPRMEDIO requires representative workload measurement and preservation of distributions before optimization. L-04. | No performance, startup, memory, contributor-productivity, or LLM-effectiveness winner can be inferred in this step. | Local benchmarks were explicitly excluded from this harvest. |
| CS-12 | Active `CA-M-110` chooses Python and requires an accepted bounded Method for a non-Python exception. L-03. | A Go or hybrid result would require governance work in addition to technical migration work. | No authority change is authorized. |
| CS-13 | NetworkX and Gonum offer broad graph abstractions and algorithms, while the current Tool source uses project-owned deterministic graph/data structures. DATA-01, L-06. | A mature graph package exists in either ecosystem, but adding one without an identified missing algorithm or measured benefit would enlarge the model and dependency surface. NetworkX 3.6.1 supports the declared Python line; Gonum's current graph line remains pre-v1 and needs an explicit API-stability assessment. | None. |

#### 4. Current comparison set, traditions, palette, and bridges

##### Comparison set

**P1 — evolutionary, library-enabled Python.** CPython 3.14; direct Click or Typer for hierarchical CLI construction; Pydantic v2 in strict/closed modes at untrusted structured boundaries; standard-library subprocess/filesystem primitives for bounded effects; standard logging with project-owned structured envelopes; uv locking and exact synchronization; Ruff, pytest, and pip-audit in development and release checks. YAML/TOML libraries are admitted per format only after the governed-file corpus demonstrates parse and rewrite fidelity. NetworkX is a credible optional graph-algorithm library only if a concrete missing algorithm or measured benefit justifies replacing project-owned structures. OpenTelemetry remains optional behind the project diagnostic abstraction. This profile preserves the current source/test estate and authority with the smallest semantic migration. Its unresolved cost is installing runtime dependencies into content-addressed releases while retaining execution without uv/project environments, plus host-interpreter and wheel/platform management.

**P2 — packaged Python.** The P1 application stack with either PyInstaller, traditional PEX, or PEX `--scie eager` artifacts. These are alternatives, not one merged stack. PyInstaller and a PEX scie can include an interpreter; a traditional PEX bundles the application environment but needs a compatible target interpreter. PyInstaller introduces per-platform builds and one-file extraction/startup/security considerations. A PEX scie changes the artifact/bootstrap and cache model; traditional PEX stays closer to the current host-Python substrate. Every variant requires deterministic artifact manifests, signatures/SBOMs, rollback tests, and compatibility runs across declared hosts.

**G1 — compiled Go tool suite.** Go 1.27.1; Cobra for the 16-command hierarchy; Go's JSON, `os/exec`, filesystem, and `log/slog` facilities; one admitted TOML parser and the maintained YAML v4 line only where required; struct validation through explicit code first, with `go-playground/validator` only when its bounded benefit exceeds its dependency and upgrade risk; Gonum graph only for a justified algorithm after accepting its pre-v1 stability boundary; modules/checksums, `govulncheck`, standard tests/fuzzing, and the race detector for relevant concurrent paths. Distribution can use per-target executables, but each declared OS/architecture combination still needs built, signed, installed, and behaviorally tested artifacts. This profile has the strongest integrated compiled-delivery and concurrency-tooling story, but it must recreate the existing Python semantics, tests, content-addressed installation, JSON contracts, Markdown/YAML/TOML preservation, Git behavior, and failure recovery.

**H1 — evidence-triggered hybrid.** Keep the governed mutation/domain toolset in Python and introduce a Go executable only behind an existing versioned JSON/subprocess boundary for a measured distribution, startup, throughput, or long-running-service pressure point. This limits rewrite scope but adds two toolchains, cross-language release coordination, and failure/diagnostic mapping. No present evidence triggers this profile: the service registry is empty and no representative workload measurement identifies a bottleneck. It is therefore a later conditional option, not a recommendation.

##### Characteristic palette

| Axis | P1 evolutionary Python | P2 packaged Python | G1 compiled Go | H1 staged hybrid |
|---|---|---|---|---|
| Existing semantic/test reuse | Highest | High | Lowest initially | High outside the isolated component |
| Current authority fit | Direct | Direct, with packaging Method detail | Requires bounded non-Python Method | Requires bounded non-Python Method for the Go component |
| Runtime dependency freedom | Host CPython plus admitted packages | PyInstaller or PEX scie: low; traditional PEX: host Python remains | Low for pure-Go binary; cgo/dependencies can change this | Two runtime/build stories |
| Cross-platform delivery | Wheels/interpreter and host matrix | Per-platform bundle or interpreter-compatible PEX | Per-target binary matrix | Both matrices |
| Typed boundary model | Runtime Pydantic plus Python typing | Same as P1 | Compile-time structs plus explicit runtime validation | Interface schema plus both models |
| Dynamic governed-document handling | Natural fit, but round-trip library must be proven | Same semantics as P1 | Feasible, but rewrite fidelity must be proven | Cross-language fidelity burden |
| Graph/data algorithms | Project-owned structures; optional NetworkX 3.6.1 only for a justified gap | Same as P1 | Project-owned structures; optional pre-v1 Gonum graph only for a justified gap | Avoid duplicate graph models unless the interface need is explicit |
| Concurrency/service tooling | `asyncio`, processes, optional free-threading | Same, plus packaging constraints | Goroutines, race detector, fuzzing | Strong only in isolated Go part; coordination cost |
| Supply-chain surface | Python packages/wheels plus interpreter | Same plus packager/build artifacts | Modules plus compiler/target artifacts | Both ecosystems |
| Migration/parity burden | Lowest | Packaging-focused | Full rewrite and equivalence program | Bounded rewrite plus interface operations |
| Current performance evidence | Missing | Missing | Missing | Missing |

##### Explicit bridges

| Contract that can bridge | Python realization | Go realization | Mapping basis | Unresolved distinction |
|---|---|---|---|---|
| Versioned machine result | Existing JSON envelope and Pydantic at untrusted edges | JSON structs plus explicit validation | Current envelope schema and golden outputs | Decoder defaults, unknown-field policy, number/null semantics |
| Bounded Git/process effect | `subprocess.run` with arrays, timeout, checked status, controlled environment, shell disabled | `exec.CommandContext` with explicit arguments/environment and checked exit | `CA-M-161` effect contract | Cancellation, signal propagation, Windows process behavior |
| Project-local release | Current digest-named copied Python release | Digest-named target-specific binary release | `CA-R-1065` content identity and launcher selection | Artifact identity must include OS/architecture/toolchain/dependencies |
| Structured diagnostics | Existing project envelope plus Python logging | Project envelope plus `slog` | `CA-M-163` severity/schema/sanitization contract | Handler backpressure, loss, field-type normalization |
| Deterministic transform core | Pure Python modules | Pure Go packages | `CA-M-160` architecture contract and common golden corpus | Ordering, Unicode, timestamps, filesystem case behavior |

These bridges establish testable comparison surfaces; they do not establish implementation equivalence. Static Go structs are not silently equated with Pydantic's runtime validation, a Go executable is not silently equated with a platform-independent artifact, and a Python bundle is not silently equated with a Go binary.

#### 5. Disagreements, exclusions, and insufficient basis

- **Type guarantees:** Go rejects more type errors at compilation; Pydantic validates runtime data and Python typing supplies development-time checks. Neither subsumes the other at untrusted boundaries.
- **Distribution:** Go normally produces a target executable; Python can remain interpreter-based or bundle the interpreter. The operational difference is real, but CAPRMEDIO artifact size, cold start, installation latency, signing, and rollback have not been measured.
- **Concurrency:** Go's language/runtime and integrated race tooling are stronger for concurrent services. Current CAPRMEDIO evidence shows file/Git-heavy local tools and no configured background service, so the relevance is unresolved.
- **Document fidelity:** Both ecosystems have parsers, but parse success is not preservation of governed Markdown/YAML/TOML bytes, comments, ordering, or error behavior. Only a CAPRMEDIO corpus can settle this.
- **Ecosystem maturity:** Click/Typer/Pydantic and Cobra/validator/YAML/TOML candidates are realistic, but maintenance status, transitive dependencies, licenses, and security change independently of popularity.
- **Maintainability and contributor/LLM ergonomics:** existing Python code and tests reduce near-term change surface; Go's static compiler may reduce some defect classes. No CAPRMEDIO-specific controlled evidence quantifies development speed, review quality, or LLM output quality.
- **Performance:** no local benchmark was run. Generic language benchmarks are excluded because they do not represent Atom mutations, Git subprocesses, graph generation, installation, hooks, or service lifecycle under current contracts.
- **Excluded from this set:** alternate languages, distributed/cloud deployment redesign, database replacement, a new graph model, GUI design, and unimplemented App/MCP workloads.

#### 6. Receiving use and refresh/return condition

The receiving decision should not ask “Which language is faster?” It should compare the four profiles against an agreed weighted set of current Tool contracts, then require evidence for any claimed advantage. Before selection, the receiver needs: reconciled live authority references; a golden behavior/failure corpus for all 16 launchers; exact dependency and license manifests; platform packaging prototypes; representative workload distributions; and a bounded migration-maintenance estimate. A language recommendation is valid only after those gates and the required authority decision.

Return this harvest for refresh when any of the following occurs: active Programmatic/Tools authority changes; supported OS/architecture or Python boundaries change; a background service or App/MCP workload enters the declared estate; a candidate dependency changes major line or stewardship; security advisories affect the shortlist; or the decision starts after 2026-12-09. Otherwise it is suitable as the evidence-map input to a later evaluation, not as a selection record.

### Issue registry

#### ISSUE-001 — Carrier state can be mistaken for a no-library rule

- **Issue or weak point:** root `pyproject.toml` has no runtime dependencies and stale authority references, while active Methods permit bounded libraries and already select Pydantic.
- **Evidence:** L-02 and L-03; the operator correction.
- **Consequence:** a comparison anchored to “standard library only” would exclude authorized realistic stacks and could preserve stale traceability.
- **Affected target or bounded context:** dependency policy and authority trace for Programmatic Tools.
- **Issue confidence and evidence basis:** 99%, direct live carrier comparison.
- **Coverage limit or uncertainty:** no claim is made that a specific new dependency is already approved.
- **Lifecycle state:** observed, open.
- **Mapped fix IDs:** FIX-001, FIX-003.

#### ISSUE-002 — Python library-enabled installation is not yet materialized

- **Issue or weak point:** the current source-copy installer and empty lock contain no runtime package installation path, although active authority permits one.
- **Evidence:** L-02, L-03, L-07, PY-04, PY-06.
- **Consequence:** P1 and P2 cannot be judged operationally complete from library APIs alone; install isolation, offline behavior, artifact identity, rollback, and host compatibility remain unproven.
- **Affected target or bounded context:** `.caprmedio_install` release construction and launcher/runtime substrate.
- **Issue confidence and evidence basis:** 97%, direct local implementation plus official packaging documentation.
- **Coverage limit or uncertainty:** no packaging prototype or platform run was authorized.
- **Lifecycle state:** open evidence gap.
- **Mapped fix IDs:** FIX-003, FIX-004.

#### ISSUE-003 — Go requires full behavioral parity and authority change

- **Issue or weak point:** G1 starts with no current Go implementation and must replace a substantial Python estate while preserving 16 command contracts and failure behavior; active authority selects Python.
- **Evidence:** L-03, L-05, L-06, L-07, GO-01 through GO-07.
- **Consequence:** compile-time and distribution benefits cannot be credited without migration, governance, and parity costs.
- **Affected target or bounded context:** entire Programmatic Tools implementation and its accepted Method.
- **Issue confidence and evidence basis:** 99%, direct repository and authority evidence.
- **Coverage limit or uncertainty:** exact rewrite effort is unknown until a controlled slice is attempted.
- **Lifecycle state:** open decision constraint.
- **Mapped fix IDs:** FIX-001, FIX-002, FIX-006.

#### ISSUE-004 — Governed-document semantic fidelity is unproven for candidate parsers

- **Issue or weak point:** library documentation establishes parsing features and some safety/stability limits, not CAPRMEDIO's byte/meaning/error preservation across Markdown, YAML, and TOML mutations.
- **Evidence:** L-04, L-06, PY-08, GO-06.
- **Consequence:** an apparently cleaner stack could silently alter authoritative artifacts or diagnostics.
- **Affected target or bounded context:** Atom and graph reads/writes, migrations, generators, and configuration updates.
- **Issue confidence and evidence basis:** 96%, direct safe-mutation requirements and library scope mismatch.
- **Coverage limit or uncertainty:** the live corpus has not been formalized into cross-language golden cases.
- **Lifecycle state:** open evidence gap.
- **Mapped fix IDs:** FIX-002, FIX-003.

#### ISSUE-005 — Performance and concurrency relevance are unknown

- **Issue or weak point:** neither CAPRMEDIO workload distributions nor comparable Python/Go measurements exist in this harvest; current services are unconfigured.
- **Evidence:** L-04, L-08, PY-02, GO-07.
- **Consequence:** startup, throughput, memory, parallelism, and service-lifecycle claims cannot support selection.
- **Affected target or bounded context:** Hooks, interactive commands, batch generators/migrations, future MCP/App/background paths.
- **Issue confidence and evidence basis:** 99% that evidence is missing; no confidence assigned to a winner.
- **Coverage limit or uncertainty:** local benchmarking was explicitly outside this step.
- **Lifecycle state:** open evidence gap.
- **Mapped fix IDs:** FIX-005.

#### ISSUE-006 — “Well adopted” does not bound supply-chain or maintenance risk

- **Issue or weak point:** candidate libraries differ in dependency graphs, stewardship, API stability, parser preservation, artifact type, and vulnerability tooling.
- **Evidence:** PY-04 through PY-08, GO-02, GO-03, GO-05, GO-06, DATA-01.
- **Consequence:** choosing by popularity could add unnecessary dependencies or admit a maintained-but-incompatible package.
- **Affected target or bounded context:** all third-party runtime/build/test dependencies in P1, P2, G1, and H1.
- **Issue confidence and evidence basis:** 97%, upstream documentation and observed stewardship transitions.
- **Coverage limit or uncertainty:** exact versions, licenses, advisories, transitive graphs, and platform artifacts were not audited.
- **Lifecycle state:** open screening requirement.
- **Mapped fix IDs:** FIX-003.

#### ISSUE-007 — Contributor and LLM ergonomics lack project-specific evidence

- **Issue or weak point:** ecosystem narratives do not establish which stack yields fewer defects or lower maintenance effort for this repository and its contributors/agents.
- **Evidence:** existing source/test scale in L-06; no admitted controlled comparative study for this codebase.
- **Consequence:** qualitative preference could be misreported as a project result.
- **Affected target or bounded context:** implementation, review, testing, and agent-assisted maintenance workflow.
- **Issue confidence and evidence basis:** 99% that project-specific evidence is absent.
- **Coverage limit or uncertainty:** this harvest did not run developer or LLM trials.
- **Lifecycle state:** open evidence gap.
- **Mapped fix IDs:** FIX-006.

### Fix and improvement register

#### FIX-001 — Reconcile decision authority before a language gate

- **Exact change:** prepare a bounded authority correction that replaces archived IDs in root materialization traceability and makes the active library-permissive Python rule explicit; if Go or H1 remains a candidate, draft but do not accept the required non-Python Method exception until evidence is reviewed.
- **Addressed issue IDs:** ISSUE-001, ISSUE-003.
- **Relationship:** required prerequisite.
- **Independent fix confidence and evidence basis:** 99%, direct conflict between active authority and materialization references.
- **Expected result:** the later decision operates on current authority without converting implementation state into policy.
- **Trade-offs:** requires governance review and may expose additional dependent carriers.
- **Owner and required authority:** CAPRMEDIO operator and authorized Method/Delivery maintainers; explicit acceptance required.
- **Dependencies and execution order:** first; precedes language selection or repository implementation.
- **Deterministic or semantic verification:** resolve every declared authority ID to an active carrier and verify the accepted Method text against the generated materialization.
- **Recommendation:** preferred.
- **State:** proposed, not applied.

#### FIX-002 — Build one cross-language behavioral corpus

- **Exact change:** extract golden success, warning, failure, dry-run, mutation, rollback, and serialization cases for all 16 launchers, including Unicode, ordering, unknown fields, null/number behavior, Git failures, partial filesystem failures, and Markdown/YAML/TOML preservation.
- **Addressed issue IDs:** ISSUE-003, ISSUE-004.
- **Relationship:** required prerequisite.
- **Independent fix confidence and evidence basis:** 98%, current compatibility/effect requirements and existing test estate.
- **Expected result:** P1, P2, G1, and any H1 boundary can be compared against the same externally visible contract.
- **Trade-offs:** corpus construction has material upfront cost and may reveal underspecified current behavior.
- **Owner and required authority:** Tool maintainers; operator adjudication for intentionally unspecified semantics.
- **Dependencies and execution order:** after FIX-001 scope confirmation; before parser choice, migration estimate, or implementation selection.
- **Deterministic or semantic verification:** same fixtures produce equivalent versioned envelopes, file bytes/normalized semantics, exit status, diagnostics, and recoverability results on each declared host.
- **Recommendation:** preferred.
- **State:** proposed, not applied.

#### FIX-003 — Admit libraries by bounded role, not ecosystem bundle

- **Exact change:** for each profile, record exactly one selected implementation per needed role, its version range, transitive graph, license, maintenance/security status, platform artifacts, API stability, failure policy, and removal/rollback path; require corpus proof for parsers and strict/closed configuration for external validators.
- **Addressed issue IDs:** ISSUE-001, ISSUE-002, ISSUE-004, ISSUE-006.
- **Relationship:** complementary.
- **Independent fix confidence and evidence basis:** 97%, active bounded-dependency authority and upstream project distinctions.
- **Expected result:** realistic library-enabled stacks without redundant or unjustified dependencies.
- **Trade-offs:** recurring refresh work; a smaller library set can require more project-owned adapter code.
- **Owner and required authority:** Programmatic Method owner plus security/release maintainer; each runtime dependency requires accepted bounded authority.
- **Dependencies and execution order:** after FIX-002 defines required semantics; before packaging prototypes.
- **Deterministic or semantic verification:** locked clean-environment install, dependency/SBOM and vulnerability report, license check, parser corpus, strict validation fixtures, and dependency-removal fallback test.
- **Recommendation:** preferred.
- **State:** proposed, not applied.

#### FIX-004 — Prototype distribution profiles across declared hosts

- **Exact change:** build one P1 installed release, one chosen P2 packaging variant, and one minimal G1 parity slice using content-addressed, signed manifests for each declared OS/architecture; exercise install, upgrade, rollback, offline start, and missing-substrate failure.
- **Addressed issue IDs:** ISSUE-002, ISSUE-003, ISSUE-006.
- **Relationship:** complementary.
- **Independent fix confidence and evidence basis:** 94%, official packaging/build documentation but no CAPRMEDIO prototype evidence.
- **Expected result:** comparable artifact size, startup, compatibility, provenance, and operational-complexity evidence.
- **Trade-offs:** matrix/build-signing cost; a minimal slice may understate whole-suite packaging complexity.
- **Owner and required authority:** release/tool maintainers; bounded experiment approval and declared host matrix required.
- **Dependencies and execution order:** after FIX-002 and FIX-003; before final selection.
- **Deterministic or semantic verification:** reproducible manifest digest where the toolchain permits, signature/SBOM validation, clean-host execution without project-source imports, and rollback to the prior selected release.
- **Recommendation:** preferred.
- **State:** proposed, not applied.

#### FIX-005 — Measure representative workloads after correctness parity

- **Exact change:** define and run distributions for cold/warm launcher start, Atom read/update, Git-hook transaction, large graph generation, batch migration, installer upgrade/rollback, and any actually admitted long-running service; capture median/tails, memory, artifact size, and failure recovery for the surviving profiles.
- **Addressed issue IDs:** ISSUE-005.
- **Relationship:** required prerequisite.
- **Independent fix confidence and evidence basis:** 99% that measurement is required; results remain unknown.
- **Expected result:** workload-specific evidence instead of generic language performance claims.
- **Trade-offs:** benchmarking effort and environmental control; measurements age with hardware, runtime, and workload changes.
- **Owner and required authority:** performance evaluation owner under `CA-M-165`; operator approves workloads and any budget.
- **Dependencies and execution order:** after FIX-002 correctness parity and FIX-004 runnable artifacts; before performance-based selection.
- **Deterministic or semantic verification:** versioned fixtures/environment, repeated samples with stored distributions and baselines, correctness assertions during every run, and explicit outlier policy.
- **Recommendation:** preferred.
- **State:** proposed, not executed.

#### FIX-006 — Estimate migration and maintainer ergonomics with a controlled slice

- **Exact change:** implement the same bounded, non-authoritative Tool slice in the surviving Python and Go profiles, then review change size, defect yield, diagnostics, test authoring, LLM-generated patch acceptance, and ongoing dependency/toolchain operations without merging either prototype.
- **Addressed issue IDs:** ISSUE-003, ISSUE-007.
- **Relationship:** complementary.
- **Independent fix confidence and evidence basis:** 90%, a controlled slice can improve evidence but may not represent the largest legacy modules.
- **Expected result:** CAPRMEDIO-specific migration and maintenance evidence with explicit sampling limits.
- **Trade-offs:** disposable implementation cost and observer/LLM variability.
- **Owner and required authority:** Tool maintainers and operator; separate experiment authorization required because this harvest is read-only.
- **Dependencies and execution order:** after FIX-001 through FIX-003; use FIX-002 as the acceptance contract; analyze before any full migration decision.
- **Deterministic or semantic verification:** blinded review rubric where practicable, identical task/fixture set, recorded compiler/static/test diagnostics, repeated agent trials, and no merge to authoritative source.
- **Recommendation:** acceptable.
- **State:** proposed, not executed.

## Unresolved evidence gaps

- **GAP-001 — Representative workload distributions.** Linked: ISSUE-005, FIX-005. Best current answer: neither language has a proven CAPRMEDIO performance advantage. Missing evidence: cold/warm startup, tail latency, throughput, memory, artifact size, and failure-recovery distributions on declared hosts. Consequence: performance and concurrency cannot support selection. Next action: execute FIX-005 after parity artifacts exist.
- **GAP-002 — Packaging and installed-runtime matrix.** Linked: ISSUE-002, ISSUE-003, FIX-004. Best current answer: Go has the simpler compiled-artifact default; PyInstaller and a PEX scie can include Python, while traditional PEX cannot, but none is validated against `.caprmedio_install`. Missing evidence: clean-host builds/runs, offline and cache/bootstrap behavior, signatures/SBOMs, upgrades, rollbacks, and platform-specific failures. Consequence: distribution advantage remains generic. Next action: execute FIX-004 across the declared matrix.
- **GAP-003 — Governed-file round-trip corpus.** Linked: ISSUE-004, FIX-002, FIX-003. Best current answer: capable libraries exist in both ecosystems, but preservation equivalence is unknown. Missing evidence: authoritative fixtures and expected bytes/semantics/errors for Markdown, YAML, TOML, JSON, and graph updates. Consequence: parser selection could corrupt or noisily rewrite carriers. Next action: create FIX-002, then run every shortlisted parser through it.
- **GAP-004 — Dependency admission facts.** Linked: ISSUE-006, FIX-003. Best current answer: named packages are credible screening candidates, not accepted dependencies. Missing evidence: exact version, license, transitive graph, advisories, wheel/binary coverage, API stability, and removal plan at decision time. Consequence: supply-chain and maintenance cost is not comparable. Next action: produce the per-role manifests in FIX-003 immediately before shortlist evaluation.
- **GAP-005 — Full Go migration effort.** Linked: ISSUE-003, FIX-006. Best current answer: it is materially higher than evolving the incumbent Python estate, but no defensible effort number exists. Missing evidence: parity slice, dependency sequence, rewrite/review/test defect rates, and dual-run transition design. Consequence: return-on-migration cannot be calculated. Next action: run FIX-006 only if G1 survives authority, packaging, and corpus gates.
- **GAP-006 — Contributor and LLM ergonomics.** Linked: ISSUE-007, FIX-006. Best current answer: existing Python familiarity/reuse and Go compiler feedback are plausible rival advantages. Missing evidence: repeated identical project tasks evaluated by the same rubric. Consequence: maintainability claims remain qualitative. Next action: include the controlled trials defined by FIX-006 and report their sampling limits.
- **GAP-007 — Authority/materialization reconciliation.** Linked: ISSUE-001, ISSUE-003, FIX-001. Best current answer: active authority is library-permissive Python; current root materialization is dependency-empty and has stale authority links. Missing evidence: accepted reconciliation and, if later needed, an accepted Go exception. Consequence: technical evidence alone cannot authorize G1/H1 or establish the exact dependency policy. Next action: execute FIX-001 through the normal governance path.

## Skills used

1. `$fpf sota harvest`

### FPF sources consulted (1 read; 1 used)

- **Used:** `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/03_02_SoTA Harvester & Synthesis/00_G.02 - SoTA Harvester & Synthesis.md` (`G.2`) — supplied the reconstructible source ledger, claim separation, plural comparison set, explicit bridges, evidence-gap handling, and refresh boundary.
