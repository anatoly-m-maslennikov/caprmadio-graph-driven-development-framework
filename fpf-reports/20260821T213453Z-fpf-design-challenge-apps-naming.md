## Task, scope, and boundaries

### Proposal, resolved FPF source, and decision boundary

The task is to assess these proposed names before they become CAPRMEDIO authority:

```text
APPS
├── GRAPH APP
└── HARNESS PLUGINS
    └── CODEX PLUGIN
```

The receiving use is the planned replacement of the current singular `APP` Feature and the later structural migration. The current project authority still says that FRAMEWORK_ENGINE owns singular `APP`, whose scope is one source indexer, derived database, read-only server, and web interface (`.caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-700--define-framework-engine-feature-topology.md:15` and `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-703--define-app-feature-scope.md:12-14`). The current graph-view Requirement confirms that this product is broader than a browser alone (`.caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/APP/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-616--render-interconnected-html-graph-views.md:12-14`). Existing host-specific authority uses the term `agent-host adapter` (`.caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-578--initialize-the-session-engine-at-host-context-boundaries.md:12-14`).

The FPF source is the local `FPF-Knowledge-Graph` at revision `48c84d84f1074d9d4c73338bcf604fc909249000`. The review uses its structure-selection and module-boundary guidance only as a review lens. Anatoly remains the project decision owner. This review does not authorize renaming, moving files, assigning prefixes, choosing Structural kinds, or implementing a Codex plugin.

Saved report: `fpf-reports/20260821T213453Z-fpf-design-challenge-apps-naming.md`

Inputs were the proposed hierarchy, the current APP and agent-host Requirements, and the inspected FPF pages listed below. The stop condition is a naming recommendation; implementation starts only after an operator decision establishes the target scope and names.

## High-confidence results (>=95%)

### FPF Challenge Findings

#### 1. `HARNESS PLUGINS` has a terminology collision

- **Result state:** concern.
- **Proposal claim and affected entity:** `HARNESS PLUGINS` is the family containing host-specific packages such as `CODEX PLUGIN`.
- **Context and receiving use:** a durable Scope Unit name used in paths, graph identities, Requirements, and generated topology.
- **Direct basis:** A.22 requires constituents and relations to keep independently recoverable identities rather than deriving meaning from a convenient box label (`A.22:1`, lines 34-43; `A.22:4`, lines 111-121). A.6.M warns that platform, package, interface, and module-like labels do not establish the same kind or relation (`A.6.M:2`, lines 85-100).
- **Project evidence:** current CAPRMEDIO authority consistently uses `agent host` and `agent-host adapter`, whereas `harness` also appears in comparative discussion of coding-agent harnesses and can be read as a test harness.
- **Reviewer inference:** `HARNESS` is understandable, but `AGENT HOST` is more precise and already project-native. **Confidence: 98%.**
- **Consequence if unresolved:** readers and future tools may need extra context to distinguish agent-host integrations from test/benchmark harnesses.
- **Candidate correction:** use `AGENT HOST PLUGINS`, with directory/prefix form `AGENT_HOST_PLUGINS`.
- **Unchecked dependency and return condition:** reopen this finding if CAPRMEDIO deliberately defines `harness` as its canonical superclass for Codex, Claude Code, and similar hosts.

#### 2. `GRAPH APP` is a good name for the current declared scope

- **Result state:** no concern found within inspected scope.
- **Proposal claim and affected entity:** `GRAPH APP` owns the derived index/database, read-only service, and graph web interface currently assigned to singular APP.
- **Direct basis:** A.22 separates a structure from its graph or view, but permits ordinary names when their selected use and boundaries remain recoverable (`A.22:3`, lines 100-109; `A.22:4`, lines 111-121).
- **Project evidence:** the current APP scope includes indexing, a rebuildable database, a server, and interconnected pages; therefore `GRAPH BROWSER` would be narrower than the declared product.
- **Reviewer inference:** `GRAPH APP` accurately names the whole product without claiming that its displayed graph is project authority. **Confidence: 98%.**
- **Consequence:** the name remains valid as the product grows beyond visualization while the Requirements preserve its read-only, derived boundary.
- **Candidate correction:** none. Prefer `GRAPH APP` over `GRAPH BROWSER` for the current scope.
- **Unchecked dependency and return condition:** reconsider if the unit is reduced to only a viewer or if non-graph application functions become primary.

#### 3. `CODEX PLUGIN` is a precise leaf name

- **Result state:** no concern found within inspected scope.
- **Proposal claim and affected entity:** one Codex-specific plugin is a child of the generic host-plugin family.
- **Direct basis:** A.22 supports independently named constituents within a selected hierarchy; A.6.M requires platform-specific packaging labels to remain distinct from interface, compatibility, and conformance claims.
- **Project evidence:** Codex is the exact target host, and `plugin` states the packaging/integration form without claiming that the package itself owns provider-neutral CAPRMEDIO behavior.
- **Reviewer inference:** the name is short, specific, and leaves room for sibling host plugins. **Confidence: 99%.**
- **Consequence:** provider-neutral behavior can remain outside the leaf while Codex-only manifest, hooks, metadata, installation, and acceptance evidence belong inside it.
- **Candidate correction:** none.
- **Unchecked dependency and return condition:** reconsider only if the deliverable is an adapter rather than a Codex plugin package.

### Strengths within inspected scope

- The hierarchy separates the graph application from host-integration packaging. **Confidence: 99%.**
- A generic plugin family above `CODEX PLUGIN` prevents Codex-specific mechanics from becoming the definition of all host integrations. **Confidence: 98%.**
- Plural `APPS` honestly signals that the former single-product boundary is expanding. **Confidence: 97%.**

### Unchecked claims and insufficient basis

- **Result state:** insufficient basis for claiming that `APPS` is the final best umbrella name. The proposed children include both a standalone application and plugin packages; the exact common scope has not yet been stated.
- This review did not determine Structural kinds, levels, stable prefixes, authority/Delivery paths, whether `HARNESS PLUGINS` is itself realized code or only a grouping unit, or whether `CODEX PLUGIN` packages Skills, Tools, hooks, the Graph App, or some subset.
- No implementation, manifest, installation behavior, or Codex-host acceptance evidence was inspected. Naming does not establish compatibility or successful installation.

### Return to project authority

My recommendation to the operator is:

```text
APPS
├── GRAPH APP
└── AGENT HOST PLUGINS
    └── CODEX PLUGIN
```

This preserves the proposed shape and changes only the ambiguous label. Before migration, define `APPS` explicitly as the FRAMEWORK_ENGINE scope that owns operator-facing application products and agent-host plugin packages. That definition, not the plural name alone, makes the mixed children coherent.

## Open questions (confidence <95%)

### Is `APPS` the right umbrella for both applications and plugins?

Best current answer: yes, if its Requirement explicitly defines the shared scope as runnable/operator-facing application and host-integration products. **Confidence: 92%.** Missing input: whether the operator intends `APPS` to mean only standalone applications or the broader executable integration surface. If it means standalone apps only, `AGENT HOST PLUGINS` should be a peer Feature or the umbrella needs a broader name such as `APPLICATION SURFACES`. Exact next action: write a one-sentence candidate scope for `APPS`, then test whether both `GRAPH APP` and `CODEX PLUGIN` satisfy it without exceptions.

### Is `AGENT HOST PLUGINS` intended to contain adapters as well as installable plugins?

Best current answer: probably only installable plugin packages; provider-neutral and adapter behavior should remain in its current owning scopes and be referenced rather than copied. **Confidence: 92%.** Missing input: the exact boundary between a Codex adapter, Codex hook integration, and a Codex plugin distribution. If these are conflated, the unit may duplicate SKILLS or TOOLS authority. Exact next action: list the intended Codex Plugin outputs—manifest, skills, hooks, app/MCP components, installer, and tests—and mark the canonical owner of each behavior.

## Skills used

- `fpf-design-challenge` — tested the proposed hierarchy and labels against bounded structure and boundary guidance before any project mutation.

#### FPF sources consulted (5 read; 3 used)

- `FPF-Knowledge-Graph/00-readme/02_Practical-Use Cards.md` — **used**: routed the question to bounded structure selection and label-boundary review.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/22_Structure and Structural Views (STRUCT-CAL)/00_A.22 - Structure and Structural Views (STRUCT-CAL).md` — **used**: tested whether the proposed hierarchy preserves independently identifiable constituents and a clear selection use.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/15_A.06.M - Module Relation Repair.md` — **used**: tested platform, package, interface, and module-like labels against their actual boundaries.
- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/19_31_Modularity and Reusable Structure Characteristics/00_C.31 - Modularity and Reusable Structure Characteristics.md` — **screened only**.
- `FPF-Knowledge-Graph/00_Index/FPF - Index.md` — **screened only**.

<oai-mem-citation>
<citation_entries>
MEMORY.md:106-121|note=[used earlier singular APP decision as continuity and rechecked it live]
MEMORY.md:135-137|note=[used Engine placement and graph validation boundaries]
</citation_entries>
<rollout_ids>
</rollout_ids>
</oai-mem-citation>
