## Task, scope, and boundaries

### Audit contract

This audit challenges the claim that the complete current active CAPRMEDIO Method set is internally coherent, aligned with the active Project Principles, and sufficiently specified for governed use. `fpf-alignment-audit` is used as a review lens, not as CAPRMEDIO authority. :codex-annotation{index="1"}

The target is the 53 active Method carriers returned from the working tree by:

```bash
python3 FRAMEWORK_ENGINE/TOOLS/ATOM_SEARCH/atom_search.py \
  --repository . run --lifecycle active --limit 5000 --view both
```

The audit includes staged and uncommitted working-tree content observed on 2026-08-21 at 23:13 UTC. It excludes draft, archived, done, and solved Methods. Other active Atoms were inspected only when they directly govern or test a finding. Implementation code and runtime behavior were not audited. The repository is undergoing a large uncommitted structural and CCE migration, so this is a working-frontier verdict, not a verdict on a released baseline.

### Resolved FPF source

The accessible source was `/Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph`, generated on 2026-08-22 from source revision `f0b498ddfdf562242984ff7ab7a2557b55af6690`.

The direct lenses used were:

- A.3.1: identify a reusable way of doing through its applicability, participants, preconditions, intended effect or preserved condition, bounds, and nearest stop.
- A.3.2: distinguish a Method from the MethodDescription carrier and judge description adequacy only for a named receiving use.
- A.15: keep Method, MethodDescription, WorkPlan, Work, capability, authority, and evidence distinct.
- B.1.5: when several Methods form a composite, state exact parts, order, joins, adapters, whole boundary, failure route, and whole identity.
- A.6.1: distinguish an operational Method from a law-governed mechanism or declaration.

### Inspected project authority

The audit read every active Method carrier, the active Intent and Project Principles, and the directly relevant identity, tier, relation, lifecycle, configuration, installation, and priority-order Requirements. Project authority—not FPF—decides CAPRMEDIO filename grammar, relation direction, lifecycle validity, and configuration ownership.

## High-confidence results (>=95%)

### Bounded verdict

**Verdict: unsupported.**

The claim that the current active Method set is coherent and ready for reliance is unsupported at this working-tree frontier. Four semantic conflicts, one materially wrong Method lineage, and several systematic carrier/relation failures are sufficient to block that claim. Many individual Methods are usable and several are unusually well bounded, but those local successes do not close the set-level failures.

### Per-claim alignment matrix

| Active Method claim(s) | Disposition | Result |
|---|---|---|
| `CA-M-001`, `CA-M-002`, `CA-M-003`, `CA-M-005`, `CA-M-006` Project Principle Methods | no concern found within inspected scope | Each states a project-wide way CAPRMEDIO works, is parented by Intent, and remains distinct from dated Work. |
| [`CA-M-091`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/05_method/CA-M-091-IMPL_METHOD--keep-only-necessary-and-sufficient-reusable-project-information.md:7) | concern | Its claim concerns information sufficiency, but both authored relations point to the Operator-priority Requirement. The graph does not identify the actual information-preservation authority or a method for deciding necessity, reusability, and sufficiency. |
| `CA-M-092` | no concern found within inspected scope | Delegation, active authority, threshold, and fail-closed boundary are explicit enough for the claimed use. |
| [`CA-M-093` through `CA-M-100`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/05_method/CA-M-093-IMPL_METHOD--optimize-project-velocity-at-its-declared-priority.md:13) | set-level gap | Each individual optimization criterion is intelligible, but no active Method composes them into the one effective priority order required by [`CA-R-860`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CA-R-860-REQUIREMENT--derive-one-effective-operator-priority-order.md:11), handles ties or incomparability, applies non-negotiable constraints, or returns an unresolved choice to Operators. |
| `CA-M-105`, `CA-M-106`, `CA-M-107`, `CA-M-108` | residual adequacy gap | The four claims establish one model, required mappings, and semantic preservation, but do not state how preservation is checked, when a mapping is inadmissible, or what stops use. They identify a coherent family, not yet a sufficient receiving-use procedure. |
| [`CA-M-110`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/05_method/CA-M-110-IMPL_METHOD--implement-framework-engine-software-in-python.md:8) | concern | The language-selection rule is reasonable, but `comparable clarity and reliability` and benefit exceeding boundary cost have no decision procedure. Its Principle/Requirement alignment is prose labelled `Candidate alignment`, while the formal relation map is empty. It also has no required Core tier. |
| `CAPRMEDIO-M-087`, `CAPRMEDIO-M-088`, `CAPRMEDIO-M-089` Project language Methods | no semantic concern found; mechanical failure | Canonical internal language, ordinary-language adaptation, and name screening have distinct purposes and useful stop rules. Their legacy filenames do not resolve current Atom IDs. |
| [`CAPRMEDIO-METHODOLOGY-METH-046`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/FRAMEWORK_METHODOLOGY/05_method/CAPRMEDIO-METHODOLOGY-METH-046--select-the-least-costly-sufficient-execution-mechanism.md:14) | residual adequacy gap | The deterministic-versus-LLM heuristic is clear, but `fully specifiable`, `requires interpretation`, and equal-cost boundary cases are not operationalized. |
| Codex Plugin Methods `085`, `086`, `087` | no semantic concern found; mechanical failure | Selection, packaging, and fresh installed-path verification are distinct, ordered, bounded Methods. All three legacy carriers lack current Atom IDs. |
| Graph App Methods `078`, `079` | no semantic concern found; mechanical failure | Projection generation and strictly read-only serving are properly separated, with explicit inputs, failures, and non-mutation boundaries. Both legacy carriers lack current Atom IDs. |
| [`CA-M-087` Tool flow](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/FRAMEWORK_ENGINE/TOOLS/05_method/CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change.md:14) | residual composition gap | The eight-step flow has order, handoffs, retries, failure behavior, and a whole boundary. Its four participating Tools are referenced only through Requirements; exact part-Method identities and join contracts are not separately represented as Methods. |
| `CA-M-101`, `CA-M-102` | no concern found within inspected scope | Observation and adoption are kept distinct; the second consumes a reproducible inventory and emits only reviewable drafts. |
| Tool Methods `053`, `054` | no semantic concern found; structural failure | Runtime versus installation and per-owner runtime directories are coherent. Both carriers author inverse `replacement_of` edges to archived Atoms and lack current Atom IDs. |
| [`Method 076`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/FRAMEWORK_ENGINE/TOOLS/05_method/CAPRMEDIO-FRAMEWORK-ENGINE-METH-076--route-and-invoke-tools-through-the-common-cli.md:19) | conflict | Step 4 executes through an environment under `.caprmedio_runtime`; current Tool authority requires executable releases and libraries under `.caprmedio_install` and permits Runtime to contain only mutable execution state. |
| [`Method 077`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/FRAMEWORK_ENGINE/TOOLS/05_method/CAPRMEDIO-FRAMEWORK-ENGINE-METH-077--generate-active-requirement-subject-catalog.md:17), [`Method 080`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/FRAMEWORK_ENGINE/TOOLS/05_method/CAPRMEDIO-FRAMEWORK-ENGINE-METH-080--generate-active-requirement-lineage-map.md:17) | ambiguity | Both say to emit “one `Orphans` section after every ... group.” This can mean one section per group, but the accepted discussion said orphans go below the grouped result. The location and cardinality should be stated unambiguously. |
| Tool Methods `081`, `082` | no concern found within inspected scope | Current snapshot and historical reconstruction separate present and Git-revision frontiers, define complete rollups, and state failure/currentness conditions. |
| [`Method 083`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/FRAMEWORK_ENGINE/TOOLS/05_method/CAPRMEDIO-FRAMEWORK-ENGINE-METH-083--compose-project-settings-from-rmed-contributions.md:13) | conflict | It composes current settings from RMED `project_settings` contributions. Current authority makes the native Project Configuration Atom the sole settings owner and expressly forbids `project_settings` contributions in other Atoms. [`GOV Method 086`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/05_method/CAPRMEDIO-GOV-METH-086--resolve-framework-and-project-settings-separately.md:13) implements the newer separation. |
| [`Method 084`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/FRAMEWORK_ENGINE/TOOLS/05_method/CAPRMEDIO-FRAMEWORK-ENGINE-METH-084--govern-portable-repository-text-bytes.md:11) | incomplete for Method use | It states a required outcome—stable normalized text bytes—but no reusable procedure, applicability, inputs, failure, or stop. Whether it should be expanded or reclassified is open. |
| `CA-M-103`, `CA-M-104` | no semantic concern found; mechanical failure | Installation and service startup are bounded and include rollback/failure behavior. Both omit Core tier and duplicate their filename identity in forbidden `atom_id` frontmatter. |
| `CA-M-109` | no semantic concern found; mechanical failure | CCE authoring has a complete decision and stop boundary, but the active Implementation Method omits its required Core tier. |
| [`GOV Method 001`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/05_method/CAPRMEDIO-GOV-METH-001--atomize-carrier-transitions.md:16) | conflict | It says every semantic change requires a successor Atom. Current revision authority permits same-ID refinement and semantic revision while the primary claim remains recognizable; only replacement creates a new ID. |
| `GOV Method 002` | incomplete for Method use | It states where legal files belong and what they are not. It does not state a reusable selection or placement procedure with applicability and failure boundaries. Reclassification remains an open decision. |
| [`GOV Method 003`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/05_method/CAPRMEDIO-GOV-METH-003--archive-based-atomic-lifecycle.md:36) | conflict | It places authored `replacement_of` on the active successor and then archives the predecessor. Current authority requires direct `replaced_by` on the archived predecessor and derives `replacement_of`; active direct relations may target only active Atoms. This also conflicts with active `GOV Method 006`. |
| `GOV Method 004` | no semantic concern found; structural failure | Bounded, fail-closed migrations are coherent, but the carrier authors unregistered `relates_to` relations and has no current Atom ID. |
| `GOV Method 006` | no semantic concern found; mechanical failure | Its declared/inverse registry procedure agrees with current replacement authority, but its legacy carrier lacks an Atom ID and several relations use noncanonical full filename references. |
| `GOV Method 008` | no semantic concern found; structural failure | Generated-only provenance is coherently excluded from implementation coverage, but the active carrier directly targets archived Atoms and authors inverse `replacement_of`. |
| `GOV Method 010` | incomplete for Method use | It specifies a proof-frontier serialization, not a complete reusable encoding/checking procedure. Whether it is a Method, Delivery, or Requirement is open. |
| `GOV Method 085`, `GOV Method 086` | no semantic concern found; mechanical failure | Identity discovery and Configuration/Graph-State resolution have explicit fail-closed boundaries. Both legacy carriers lack current Atom IDs; Method 086 is the coherent current alternative to conflicting Tool Method 083. |

### Semantic blockers

1. **Lifecycle change classes conflict.** [`GOV Method 001`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/05_method/CAPRMEDIO-GOV-METH-001--atomize-carrier-transitions.md:25) requires a successor for every semantic change, while [`GOV REQU-311`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-311--atomic-revision-change-classes.md:21) keeps the ID for refinement and recognizable semantic revision. Both cannot govern the same change.
2. **Replacement ownership conflicts.** [`GOV Method 003`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/05_method/CAPRMEDIO-GOV-METH-003--archive-based-atomic-lifecycle.md:38) puts `replacement_of` on the successor. [`GOV REQU-309`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages.md:75), [`GOV REQU-311`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-311--atomic-revision-change-classes.md:35), and `GOV Method 006` require `replaced_by` on the archived predecessor and derive the inverse.
3. **Settings ownership conflicts.** [`Tool Method 083`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/FRAMEWORK_ENGINE/TOOLS/05_method/CAPRMEDIO-FRAMEWORK-ENGINE-METH-083--compose-project-settings-from-rmed-contributions.md:15) creates settings from many RMED contributors. [`SEMANTICS REQU-618`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/SEMANTICS/04_requirement/CAPRMEDIO-META-REQU-618--separate-framework-and-project-configuration.md:13) makes one Project Configuration Atom the sole settings owner, and [`GOV REQU-676`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-676--encode-project-settings-contributions-as-nested-yaml.md:13) forbids `project_settings` contributions elsewhere.
4. **Installation/runtime boundaries conflict.** [`Tool Method 076`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/FRAMEWORK_ENGINE/TOOLS/05_method/CAPRMEDIO-FRAMEWORK-ENGINE-METH-076--route-and-invoke-tools-through-the-common-cli.md:24) executes through Runtime. [`Tool REQU-603`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/FRAMEWORK_ENGINE/TOOLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-603--separate-project-local-tool-installation-and-runtime.md:12) assigns executable releases, libraries, registries, launchers, and Hook carriers to Installation and only mutable state to Runtime.
5. **Information-method lineage is materially wrong.** [`CA-M-091`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/05_method/CA-M-091-IMPL_METHOD--keep-only-necessary-and-sufficient-reusable-project-information.md:7) is related only to Operator-priority authority, not to the information-preservation claim it implements. This makes graph traversal produce the wrong explanation of why the Method exists.

### Structural/mechanical failures

- **Identity:** 27 of 53 active Method carriers return `atom_id: null` from the canonical active-Atom Finder. These are the legacy `CAPRMEDIO-M-*`, `CAPRMEDIO-*-METH-*`, and `CAPRMEDIO-GOV-METH-*` carriers. Current authority requires the leading immutable `<PROJECT_PREFIX>-<content_role_letter>-<NUMBER>` identity segment; see [`GOV REQU-731`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-731--place-immutable-atom-id-before-mutable-scope-path.md:19) and [`GOV REQU-736`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-736--derive-atom-classification-from-carrier-address.md:18).
- **Tier:** four active Implementation Methods—`CA-M-103`, `CA-M-104`, `CA-M-109`, and `CA-M-110`—omit `tier: core`. [`GOV REQU-756`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-756--restrict-implementation-methods-to-core-tier.md:13) admits Implementation Methods only at Core, and [`GOV REQU-799`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-R-799-REQUIREMENT-BSEED_GOVERNANCE--encode-rmedo-applicability-tiers.md:15) requires non-Principle tier-classified PRMEDO Atoms to resolve a registered tier.
- **Duplicated identity:** `CA-M-103` and `CA-M-104` embed `atom_id` in frontmatter even though their filenames are identity authority. [`GOV REQU-348`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-348--use-canonical-carrier-address-as-authority.md:14) forbids that duplication.
- **Relation target syntax:** 38 authored relation targets across 16 active Method carriers use full identified filename stems where current [`GOV REQU-327`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-327--use-atom-ids-as-stable-artifact-references.md:15) requires exact Atom IDs. This is migration debt even where the target resolves today.
- **Inactive targets:** seven direct relations from five active Methods target archived Atoms: Tool Methods `053` and `054`, and GOV Methods `001`, `003`, and `008`. [`GOV REQU-767`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-767--keep-active-rmed-relations-out-of-archives.md:13) and [`GOV REQU-768`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CAPRMEDIO-GOV-REQU-768--validate-active-rmed-relation-target-lifecycle.md:12) reject these edges.
- **Inverse relations authored directly:** Tool Methods `053` and `054`, and GOV Methods `001`, `003`, and `008`, author `replacement_of`. [`CA-R-879`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CA-R-879-REQUIREMENT-BSEED_GOVERNANCE--register-foundational-inverse-relation-pairs.md:12) registers `replaced_by` as direct and `replacement_of` as inverse-derived.
- **Unregistered relation:** GOV Method `004` authors `relates_to`, but the current canonical relation dictionary contains no such direct relation. Its meaning is therefore neither exclusive nor machine-governed.

### Residual gaps and optional improvements

- Add one composite alternative-selection Method that consumes the effective order from `CA-R-860`, applies constraints, defines comparison/tie behavior, and returns an unresolved choice to Operators. Keep `CA-M-093` through `CA-M-100` as reusable criterion Methods if they remain independently useful.
- Give `CA-M-105` through `CA-M-108` an Evaluation-backed semantic-preservation criterion and explicit failure/stop behavior.
- Convert `CA-M-110` candidate alignment prose into typed relations, add Core tier, and define the decision evidence for non-Python exceptions and dependency admission.
- Decide one exact Orphans-section cardinality and location for Methods `077` and `080`.
- If the Tool change pipeline is intended as a composite Method, add separate part Methods or explicitly declare that the named Tools are mechanisms/operations rather than Method parts; then state each join and failure handoff once.
- Expand or reclassify Methods `084`, GOV `002`, and GOV `010` so that representation constraints do not masquerade as complete execution procedures.

### Excluded and uninspected claims

- Draft Methods under Project, FRAMEWORK_ENGINE, TOOLS, APPS, SKILLS, and FRAMEWORK_METHODOLOGY were excluded by the active-only contract.
- Archived Methods were used only as relation-target evidence and were not re-audited.
- Code conformance, test quality, runtime performance, and actual Tool behavior were not evaluated.
- The full 959-Atom active graph was not semantically audited; only active Methods, active Principles/Intent, and authority directly needed to decide Method findings were read.
- The large current migration was not mutated, committed, installed, or validated as a whole.

### Bounded verdict and stop/return

Stop at `unsupported`: the complete active Method set cannot be relied on as coherent until the four semantic conflicts and wrong information lineage are resolved. Then repair identity, tier, and relation encoding, add the missing composite priority-selection Method, and clarify the bounded ambiguities. Re-run this audit only after those changes materially alter the semantic frontier; repeated review of the unchanged set would add activity, not evidence.

## Open questions (confidence <95%)

1. **Method versus Requirement/Delivery:** should Tool Method `084`, GOV Method `002`, and GOV Method `010` remain Methods after being expanded, or should their current normative/representation claims move to Requirement or Delivery while separate operational Methods are added? Confidence in the need to resolve the classification is 98%; confidence in any one reclassification without Operator intent is below 95%.
2. **Priority family boundary:** are `CA-M-093` through `CA-M-100` intended as a closed Project priority catalog or merely the currently useful criteria? Their wording does not claim completeness, while `CA-R-815` supports any admissible Operator-established priority model. The composite-selector gap exists either way, but MECE can be judged only after the intended universe is declared.
3. **Semantic mapping threshold:** what evidence is sufficient to say an Extension or Project Adaptation preserves a canonical meaning? The active Methods do not select equivalence, refinement, tolerated loss, or Operator acceptance as the decisive criterion.
4. **Transitional filename tolerance:** the CCE migration may intentionally preserve legacy carriers temporarily, but no inspected active Method-specific exception makes an `atom_id: null` active Method safe for graph reliance. The intended migration stop condition should decide whether these are temporarily tolerated diagnostics or immediate blockers.

## Skills used

- `fpf-alignment-audit` — resolved the live target and FPF source, separated project evidence from FPF review lenses, assigned per-claim dispositions, and stopped at a bounded verdict.

#### FPF sources consulted (8 read; 5 used)

- `00-readme/02_Practical-Use Cards.md` — screened only.
- `00_Index/FPF - Index.md` — screened only.
- `A_Kernel Architecture Cluster/03_Transformer Constitution (Quartet)/01_A.03.01 - U.Method- Reusable Way of Doing with Explicit Applicability.md` — used.
- `A_Kernel Architecture Cluster/03_Transformer Constitution (Quartet)/02_A.03.02 - U.MethodDescription- Description Episteme for a Way of Doing.md` — used.
- `A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/06_A.06.01 - U.Mechanism - Reusable Law-Governed Operation Declaration.md` — used.
- `A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/18_A.06.07 - MechSuiteDescription - Description of a set of distinct mechanisms.md` — screened only.
- `A_Kernel Architecture Cluster/15_System-Role-Method-Work Alignment/00_A.15 - System-Role-Method-Work Alignment.md` — used.
- `B_Trans-disciplinary Reasoning Cluster/00_01_Holon Aggregation and Part-Whole Construction/05_B.01.05 - Gammamethod - Order-Sensitive Method Composition and Work Enactment.md` — used.

<oai-mem-citation>
<citation_entries>
MEMORY.md:1092-1111|note=[bounded FPF review and authority separation]
</citation_entries>
<rollout_ids>
019fb801-af36-7993-8d2c-b98cbd0dfc55
</rollout_ids>
</oai-mem-citation>
