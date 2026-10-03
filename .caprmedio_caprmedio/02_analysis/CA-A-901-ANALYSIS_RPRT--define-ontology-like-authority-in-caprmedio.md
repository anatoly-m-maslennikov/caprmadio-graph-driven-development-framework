---
atom_id: CA-A-901
cce_version: cce_1
cce_form: rationale
subjects:
  governs:
    continuant:
      - ontology-like-authority
      - Core Meta-Model
      - Framework Methodology
  depends_on:
    continuant:
      - Project Configuration
      - CAPRMEDIO Graph
relations:
  analysis_of:
    - CA-R-1248
    - CA-R-1318
    - CA-R-1406
version: 1
updated_at: 2026-09-14 01:08:50
---
# Define ontology-like authority in CAPRMEDIO

## Task, scope, and boundaries

The task was to recover what “ontology” currently means in the CAPRMEDIO Framework and the `caprmedio` Project. This is a structure-recovery result, not a generic philosophy or Semantic Web definition.

The evidence boundary was the live filesystem snapshot on 2026-09-13: active Core Meta-Model and Project Configuration source Atoms under `.caprmedio_framework`, active `caprmedio` Project Atoms under `.caprmedio_caprmedio`, and their direct graph projections. Archive, draft, and plan content was excluded from authority. The worktree is on `amm/next-version` at `2f3708e01d55adbd1cbed6108eca54bdeaab4dcb` and contains uncommitted work, so this is a recovery of current live carriers, not a claim about a published release.

This Analysis Report persists the recovered meaning without introducing `Ontology` as a Governed Term or changing normative authority.

## Issues, weak points, and improvements

### Native result

**Short answer:** in CAPRMEDIO, “ontology” is best understood as the governed agreement about what kinds of things may exist in a project, how those things are identified and classified, which relations may connect them, where claims apply, and which Atoms have authority for those claims.

Strictly, however, `Ontology` is **not currently a CAPRMEDIO Governed Term**. A bounded search of active authority carriers found no active Definition Atom for it. Therefore, “ontology” is safe as explanatory shorthand, but the carrier-backed CAPRMEDIO name is:

> **the Core Meta-Model, expanded by applicable extension and Project Configuration authority, together with active project Atoms that instantiate and govern that model.**

That meaning is distributed rather than stored in one ontology file:

| Question | Current CAPRMEDIO construct | Carrier-backed meaning |
|---|---|---|
| What may exist? | `Entity` | An independently identified or bearer-qualified object admitted as a possible node in at least one CAPRMEDIO Graph. An Entity is a `Primary Entity` or a bearer-dependent `Dependent Entity`. ([CA-R-1248](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1248-CORE_META_MODEL-CORE-REQUIREMENT--define-entity.md), [CA-R-1191](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1191-CORE_META_MODEL-CORE-REQUIREMENT--define-primary-entity.md), [CA-R-1192](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1192-CORE_META_MODEL-CORE-REQUIREMENT--define-dependent-entity.md)) |
| Which words have project-specific meaning? | `Term`, `Governed Term`, `Definition Atom` | A Term has Project-specific meaning; a Governed Term has exactly one active Definition Atom in the applicable Claim Scope. Ordinary English remains a `General Term`. ([CA-R-1318](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1318-CORE_META_MODEL-CORE-REQUIREMENT--define-term.md), [CA-R-1319](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1319-CORE_META_MODEL-CORE-REQUIREMENT--define-governed-term.md), [CA-R-126](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-126-CORE_META_MODEL-CORE-REQUIREMENT--give-each-governed-term-one-definition-atom.md)) |
| What corresponds to classes and instances? | No current primitive `Class` or `Instance`; instead `Term`, `NARROWER_THAN`, `Entity` occurrence, and `Type` | Term-extension inclusion is expressed by `NARROWER_THAN`: every Entity classified by the narrower Term is also classified by the broader Term. Concrete, instance-like things are Entity occurrences. Finite classifications are expressed through a single-valued `Type` Property and allowed values. ([CA-R-1435](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1435-CORE_META_MODEL-CORE-REQUIREMENT--define-narrower-than.md), [CA-R-1284](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1284-CORE_META_MODEL-CORE-REQUIREMENT--define-type.md), [CA-R-1436](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1436-CORE_META_MODEL-CORE-REQUIREMENT--define-is-allowed-value-of.md)) |
| How may things relate? | Graph-specific `Relation Kind` and relation facts | Every Relation Kind belongs to exactly one graph kind; equal names in different graph kinds are not interchangeable. Every relation fact has one authoritative source. ([CA-R-1246](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1246-CORE_META_MODEL-CORE-REQUIREMENT--keep-relation-vocabularies-graph-specific.md), [CA-R-1437](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1437-CORE_META_MODEL-CORE-REQUIREMENT--keep-one-source-for-each-relation-fact.md)) |
| What is asserted and governed? | `Atom` containing one `Claim` | An Atom is the smallest independently governed Artifact; it owns one independently replaceable, human-readable, precisely interpreted Claim. ([CA-R-655](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-655-CORE_META_MODEL-CORE-REQUIREMENT--define-atom-artifact-form.md), [CA-R-1269](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1269-CORE_META_MODEL-CORE-REQUIREMENT--define-claim.md), [CA-R-918](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-918-CORE_META_MODEL-CORE-REQUIREMENT--give-every-atom-one-claim.md)) |
| What is a Claim about? | `Subject` with `GOVERNS` or `DEPENDS_ON` | A Subject is a bearer-dependent Entity that connects an Atom to one referenced Entity. `GOVERNS` makes the Atom authoritative about it; `DEPENDS_ON` requires it without granting authority. ([CA-R-1275](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1275-CORE_META_MODEL-CORE-REQUIREMENT--define-subject-as-a-dependent-entity.md), [CA-R-1199](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1199-CORE_META_MODEL-CORE-REQUIREMENT--define-governs-subject-relation-kind.md), [CA-R-1200](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1200-CORE_META_MODEL-CORE-REQUIREMENT--define-depends-on-subject-relation-kind.md)) |
| Where does it belong and apply? | `Scope Unit` versus `Claim Scope` | A Scope Unit is a structural ownership boundary for Atoms. Claim Scope selects semantic applicability. Structural ownership does not establish or alter applicability. ([CAPRMEDIO-META-REQU-708](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-708-CORE_META_MODEL-CORE-REQUIREMENT--define-scope-unit.md), [CA-R-1364](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1364-CORE_META_MODEL-CORE-REQUIREMENT--define-claim-scope-unit-set.md)) |
| What is only a view? | `Terms Graph`, `Entities Graph`, `Graph of Graphs`, Project Scope Unit Graph, and other projections | A graph projection displays selected relation occurrences and provenance. Materializing, refreshing, or deleting it cannot establish, change, or remove Entity identity or authority. ([CA-R-1335](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1335-CORE_META_MODEL-CORE-REQUIREMENT--define-terms-graph.md), [CA-R-1438](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1438-CORE_META_MODEL-CORE-REQUIREMENT--define-entities-graph.md), [CA-R-1406](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1406-CORE_META_MODEL-CORE-REQUIREMENT--keep-entity-identity-independent-of-graph-materialization.md)) |

The framework-versus-project boundary is therefore:

- **CAPRMEDIO Framework:** the reusable methodology and engine. Its Core Meta-Model defines the reusable semantic primitives, invariants, relation vocabularies, and expansion boundaries. The engine compiles, validates, and renders them; it is not itself the ontology. The Framework is defined as `FRAMEWORK_METHODOLOGY + FRAMEWORK_ENGINE`. ([CAPRMEDIO-REQU-705](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-705-REQUIREMENT--define-framework-composition.md))
- **`caprmedio` Project:** the active project instance that applies those reusable rules, adds bounded Project Configuration, and supplies actual project Entities, Atoms, Claims, Subjects, and relation facts. Core, reusable extension, and project-specific configuration authority remain separate; the project may adapt without rewriting core authority. ([CAPRMEDIO-REQU-686](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-686-CORE-REQUIREMENT--separate-core-extension-and-project-configuration-authority.md), [CA-R-1218](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1218-CORE_META_MODEL-CORE-REQUIREMENT--define-project-configuration.md))
- **Self-hosting consequence:** this repository develops the framework while using it to govern the `caprmedio` Project. That creates one connected Graph of Graphs, but does not collapse reusable model authority into project-instance facts. ([CA-R-1407](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1407-PRINCIPLE-REQUIREMENT--the-caprmedio-instance-and-the-implementation-form-a-graph-of-graphs.md))

So, “the CAPRMEDIO ontology” must not be confused with one generated graph, the directory tree, a database, only the terminology hierarchy, a generic OWL/RDF ontology, or the whole Framework. The closest precise phrase is **“CAPRMEDIO Core Meta-Model plus applicable project-specific expansions and active project-instance claims.”**

### Issue registry

- **ID:** `ONT-001`
  - **Issue:** `Ontology` has no recovered active Definition Atom and is not established as a current Governed Term.
  - **Evidence:** Exact bounded search for `Ontology`, `ontology`, `Ontological`, and `ontological` returned no match in active Core Meta-Model source Atoms, active Project Configuration source Atoms, or active `caprmedio` requirement/method/evaluation/delivery Atoms; the governed-term rule requires one active Definition Atom ([CA-R-126](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-126-CORE_META_MODEL-CORE-REQUIREMENT--give-each-governed-term-one-definition-atom.md)).
  - **Consequence:** The word can explain the model, but must not silently behave as a canonical CAPRMEDIO concept or carry ungoverned assumptions from another ontology tradition.
  - **Affected target/context:** Project vocabulary, explanatory documentation, prompts, and graph tooling that might ask for an “ontology.”
  - **Confidence and basis:** 99%; exact search over the active authority paths and confirmation against the current governed-term rule.
  - **Coverage uncertainty:** Untracked external documents or future/uncommitted carriers outside the inspected active paths could use the word, but they would not establish current authority here.
  - **Lifecycle state:** OPEN.
  - **Mapped fix IDs or no-fix disposition:** No-fix disposition: this approved step is recovery-only and does not authorize adding a Governed Term.

- **ID:** `ONT-002`
  - **Issue:** The compiled Applicable Methodology and graph projections do not uniformly reflect the newest live source-carrier semantics.
  - **Evidence:** The current source [CA-R-1318](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1318-CORE_META_MODEL-CORE-REQUIREMENT--define-term.md) is version 4, while the compiled [CA-R-1318 projection](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/04_requirement/CA-R-1318-CORE_META_MODEL-CORE-REQUIREMENT--define-term.md) is version 3. The current source contains `NARROWER_THAN` and `Entities Graph` definitions ([CA-R-1435](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1435-CORE_META_MODEL-CORE-REQUIREMENT--define-narrower-than.md), [CA-R-1438](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1438-CORE_META_MODEL-CORE-REQUIREMENT--define-entities-graph.md)) absent from the compiled requirement projection, which still exposes older `SUBKIND_OF`/`INSTANCE_OF` terminology in [CA-R-1246](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_framework/00_APPLICABLE_METHODOLOGY/04_requirement/CA-R-1246-CORE_META_MODEL-CORE-REQUIREMENT--keep-term-system-relations-graph-specific.md). The [Project Scope Unit Graph projection](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/project_scope_unit_graph.projection.toml) was generated on 2026-09-06, before inspected source updates through 2026-09-11/12.
  - **Consequence:** A consumer that treats projections as current authority can recover an older and materially different account of terms, class-like relations, and graph kinds.
  - **Affected target/context:** Compiled Applicable Methodology and direct graph-projection consumers.
  - **Confidence and basis:** 100%; direct version/content comparison and projection timestamp comparison.
  - **Coverage uncertainty:** This analysis did not execute recompilation or currentness validators, so it does not determine whether an existing tool already detects every mismatch.
  - **Lifecycle state:** OPEN.
  - **Mapped fix IDs or no-fix disposition:** No-fix disposition: this read-only recovery uses live sources as authority and treats the projections as dated, partial views.

- **ID:** `ONT-003`
  - **Issue:** Specific graph kinds are actively defined, but no active defining Atom for the generic `CAPRMEDIO Graph` primitive was recovered in the bounded Core Meta-Model search.
  - **Evidence:** Active definitions exist for the Terms Graph, Entities Graph, Graph of Graphs, and General Artifact Graph, while active requirements use `CAPRMEDIO Graph` as a common class without a recovered corresponding definition Atom.
  - **Consequence:** The family resemblance is recoverable, but a stronger universal definition of every CAPRMEDIO Graph would exceed current carrier evidence.
  - **Affected target/context:** Any explanation or tooling contract that needs the exact common semantics of all graph kinds.
  - **Confidence and basis:** 97%; exact search across active Core Meta-Model sources plus inspection of graph-kind definition Atoms.
  - **Coverage uncertainty:** A definition may exist under an unexpected identifier or outside the bounded current Core Meta-Model source scope.
  - **Lifecycle state:** OPEN.
  - **Mapped fix IDs or no-fix disposition:** No-fix disposition: do not invent the missing common definition during recovery.

### Fix and improvement register

No fixes or improvements were proposed. The approved command is descriptive and read-only; `ONT-001` through `ONT-003` therefore carry explicit no-fix dispositions rather than implementation records.

## Unresolved evidence gaps

- **Gap ID:** `GAP-ONT-001`; **linked issue:** `ONT-001`; **best current answer:** use “ontology” only as general explanatory shorthand for the governed semantic model, with “Core Meta-Model plus applicable expansions and active project claims” as the precise formulation; **missing evidence:** an owner-approved active Definition Atom that makes `Ontology` a Governed Term; **consequence:** no canonical short label can be claimed; **exact next evidence:** an active authority decision and carrier, if the project later chooses to govern the word. This does not block the present explanation.
- **Gap ID:** `GAP-ONT-002`; **linked issue:** `ONT-002`; **best current answer:** current source Atoms establish meaning and the direct projections are admissible only for what their recorded source revisions captured; **missing evidence:** a successful currentness/recompilation receipt against the complete live source frontier; **consequence:** projection consumers may expose an older model; **exact next evidence:** run the repository’s existing Applicable Methodology and projection-currentness validations in a separately authorized follow-up.
- **Gap ID:** `GAP-ONT-003`; **linked issue:** `ONT-003`; **best current answer:** describe the recovered specific graph kinds and shared graph-specific-relation discipline without asserting a universal graph definition; **missing evidence:** an active Definition Atom for the common `CAPRMEDIO Graph` concept; **consequence:** the generic base remains under-specified; **exact next evidence:** locate a differently named current carrier or obtain an authority decision before defining one.

## Skills used

- `$fpf structure recover` — recovered the selected current structure from authoritative source Atoms and treated generated graph artifacts only as bounded projections.

### FPF sources consulted (2 read; 2 used)

- **Used — primary method:** [A.22 — Structure and Structural Views (STRUCT-CAL)](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/A_Kernel Architecture Cluster/22_Structure and Structural Views (STRUCT-CAL)/00_A.22 - Structure and Structural Views (STRUCT-CAL).md>) — required independently identified constituents, obtaining relation occurrences, constraints, and a named use frame; prevented treating a graph view or directory layout as the ontology itself.
- **Used — result projection:** [C.33 — Structural Information Adequacy for Architecture Capture and Missing-Structure Return](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/C_Kernel Extension Specifications/21_33_Structural Information Adequacy for Architecture Capture and Missing-Structure Return/00_C.33 - Structural Information Adequacy for Architecture Capture and Missing-Structure Return.md>) — required explicit disclosure of missing/lost structure and restricted dated projections to the structure they actually capture.


## Clarification: ontology, meta-model Requirements, and Methodology

Ontology-like authority is primarily expressed by active Core Meta-Model Requirement Atoms. Applicable extension and Project Configuration Requirements can add bounded semantics, while active project Atoms instantiate and govern the model. Graph projections visualize this authority but do not establish it.

This ontology-like component is the semantic substrate of CAPRMEDIO Methodology, not the whole Methodology. It defines what kinds of things and relations mean; Methodology additionally governs how that semantic substrate and its project instances are created, changed, applied, validated, and operated through Plan, Requirement, Method, Evaluation, and Delivery authority. Therefore, the concise answer to "is ontology the meta-model Rs?" is: mostly yes for the reusable ontology-like core, but the complete live meaning also includes applicable expansion/configuration Requirements and the project Atoms that instantiate them.