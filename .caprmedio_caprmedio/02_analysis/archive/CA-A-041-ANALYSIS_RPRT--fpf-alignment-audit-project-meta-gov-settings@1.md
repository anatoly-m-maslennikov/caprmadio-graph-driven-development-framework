---
atom_id: CA-A-041
subject_scopes:
  - authority
  - scope-topology
  - settings
  - carrier-format
version: 1
updated_at: 2026-08-21 01:52:33
---

## Task, scope, and boundaries

Audit CAPRMEDIO again after the latest repairs, using the same bounded surface as the preceding alignment audit.

Receiving use: decide whether Project RMED authority, META/GOV Core authority, and settings are coherent enough to continue upward construction. This report is non-normative Analysis; it is not Evaluation, a release gate, or authorization to mutate carriers.

Audited repository state:

- Repository: `/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework`
- HEAD: `3730084af7f1a890415a22837cc6adee053e685d`
- Worktree: dirty, with 2,010 reported status paths; findings apply only to the inspected state.
- Saved report: `fpf-reports/20260818T100913Z-fpf-alignment-audit-project-meta-gov-settings.md`

Audit contract:

- Inspect every active Project RMED Atom.
- Inspect every active META and GOV Core RMED Atom.
- Inspect Framework Settings, Project Settings, and the Project Settings Map.
- Inspect downstream carriers only where needed to test strict parent/child topology.
- Test semantic irreducibility, tier ownership, relation direction, strict topology, settings separation, revision metadata, Projection replayability, and semantic authority fidelity.

Excluded from the claim:

- Downstream SPEC, REALIZATION, RELEASES, and FIELD semantic correctness except required dependencies.
- Runtime correctness beyond settings-currentness mechanics.
- Tests, evaluations, release readiness, and repository acceptance. No project tests or evaluations were run.

Evidence used: current active carriers, the two settings carriers, the Project Settings Map, deterministic graph inspection, and read-only currentness checks for native Framework Settings and generated Project Settings.

Acceptance boundary: the audited surface is aligned only if accepted authority is coherent, its strict topology is valid, settings outputs are replayable, and effective settings are faithfully derived from their declared RMED sources. Reproducible output bytes and exact source references are necessary but insufficient when the effective values are independently authored in Tool code.

## High-confidence results (>=95%)

### Verdict

**unsupported**

The previous blockers around Atom revision metadata, strict topology, Framework Settings revision binding, and Project Settings replay metadata are repaired. The remaining blocker is deeper: Project Settings can now be reproduced and checked for currentness, but its effective values are authored in the generator rather than derived from RMED authority. The Project Settings Map also acts as semantic generator input while being declared a generated, non-authoritative Projection. Several META Cores additionally remain semantically reducible.

### Per-claim alignment matrix

| Audited claim | Result | Confidence | Evidence |
|---|---|---:|---|
| Every active Project/META/GOV strict-scope RMED Atom carries valid revision metadata | boundedly supported | 100% | All 321 inspected active strict-scope RMED Atoms have positive `version`, exact `updated_at` in `YYYY-MM-DD HH:MM:SS`, and one `subject_scopes` value. |
| Active strict Project/META/GOV RMED topology is valid | boundedly supported | 100% | No missing required parents, strict orphans, cycles, tier-direction errors, or active `child_of` references to inactive targets were found. Four apparently childless Atoms have valid active downstream children. |
| Framework Settings has a coherent external Atom revision binding | boundedly supported | 100% | The read-only native revision check returned `CAPRMEDIO-FRAMEWORK-SETTINGS@1,2026-08-18 07:15:24`, `changed=false`. |
| Project Settings and its Map expose replay/currentness metadata | boundedly supported | 100% | Both carry `updated_at`, generator identity/digest, source frontier/digest, and exact source references; the read-only generator check returned `changed=false`. |
| Framework Settings and Project Settings remain distinct carriers | boundedly supported | 100% | Framework-owned operating parameters remain in root TOML; Project-owned generated selections remain in `.caprmedio/caprmedio_project_settings.toml`. |
| Project Principle authority is internally distinct and topologically coherent | boundedly supported | 97% | The 14 active Project Principles have distinct named claims and valid downstream authority paths within this audit boundary. |
| The configured LLM confidence threshold is a local heuristic rather than a universal comparable probability | boundedly supported | 98% | REQU-035 binds use to the effective framework configuration and allows model/version/effort-specific adjustment. |
| Effective Project Settings values are derived from RMED authority | unsupported | 100% | `generate_project_settings.py` emits the hardcoded `SETTINGS` constant; RMED source references are attached separately and do not determine those values. |
| The Project Settings Map is only a generated, non-authoritative Projection | unsupported | 100% | The generator reads the existing Map binding tree as semantic input and refreshes its metadata/frontier; the binding selection is not independently regenerated from RMED authority. |
| META Core authority satisfies semantic irreducibility | unsupported | 98% | META-108, META-110, META-128, META-153, and META-175 each retain independently replaceable claims beyond their named primary claim. |
| Overall audited surface | unsupported | 100% | Structural and revision repairs pass, but the settings authority inversion and remaining Core reducibility violate active authority. |

### Repaired findings

1. **Atom revision metadata is now complete.** The previous set of active Atoms missing `version` or `updated_at` has been repaired. All 321 active strict-scope RMED Atoms satisfy the current carrier shape checked here.

2. **Strict authority topology is clean within the bounded graph.** There are no strict orphans, cycles, invalid tier directions, or active child edges to inactive RMED targets. The four Atoms with no strict-scope child have active children in the downstream dependency surface: REQU-013, REQU-053, META-159, and META-173.

3. **Framework Settings now has a stable external revision binding.** The native TOML remains clean while the governed revision/currentness mechanism identifies the exact Framework Settings Atom version without embedding CAPRMEDIO metadata in the executable carrier.

4. **Project Settings is mechanically replayable and current.** [Project Settings](../.caprmedio/caprmedio_project_settings.toml) and the [Project Settings Map](../.caprmedio/08_implementation/CAPRMEDIO-MAPS-001--project-settings-source-map.yaml) expose generator, source-frontier, digest, and currentness information. The read-only generator reported no pending change.

### Blocking findings

1. **Project Settings has reproducible bytes but not RMED-derived meaning.** [REQU-622](../.caprmedio/04_requirement/CAPRMEDIO-REQU-622--establish-project-configuration-through-rmed.md), [META-620](../.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-620--classify-project-settings-as-an-implementation-projection.md), [META-627](../.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-627--bind-every-projected-setting-to-exact-source-authority.md), and [GOV-647](../.caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-647--register-project-settings-projection-mechanics.md) require Project Settings to be projected from RMED authority. Instead, [generate_project_settings.py](../02_TOOLS/generate_project_settings.py) declares all effective values in its `SETTINGS` constant and emits that constant. The Map supplies references, but those references neither calculate nor validate the corresponding values. Provenance labels do not establish semantic correspondence.

2. **The Project Settings Map is simultaneously output and semantic input.** [GOV-669](../.caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-669--register-project-settings-source-map-projection.md) classifies the Map as a generated, non-authoritative Projection. The generator nevertheless loads the existing binding tree and preserves it while refreshing metadata and the source frontier. No inspected RMED authority or deterministic extraction rule can regenerate the binding selection from scratch. The Map therefore carries an independent decision while disclaiming authority for it.

3. **Current validation checks identity and coverage, not claim-to-value fidelity.** Missing, ambiguous, or contradictory-source checks can establish that referenced Atoms exist and that settings have bindings. They do not establish that `strict`, a tier number, a confidence threshold, or any other emitted value is entailed by the cited Atom claim. This falls short of [GOV-345](../.caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully.md).

4. **Five META Cores remain semantically reducible.** [META-108](../.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-108--evolve-authority-through-governed-history.md) combines Atom mutation/freeze, successor behavior, Journal append-only semantics, Projection regeneration, currentness, and Git/Journals provenance. [META-110](../.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-110--bind-governed-transactions-to-stable-artifact-revisions.md) combines transaction ontology, scope restrictions, ordering, refinement, and Git resilience. [META-128](../.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision.md) combines identity-level separation with migration, native-carrier, revision-binding, and historical-resolution rules. [META-153](../.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-153--preserve-bounded-meaning-across-structural-scales.md) repeats one-way authority dependency already owned by Project authority. [META-175](../.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-175--use-canonical-meta-subject-scopes.md) combines the Subject catalog with scope-path boundaries, cardinality, admission, and extension rules. Each identified secondary rule can change without changing the carrier's named primary claim.

### FPF alignment

The result follows six bounded FPF checks:

- The Principle Taxonomy and Precedence Model supports explicit, acyclic precedence rather than implicit or circular authority.
- Unidirectional Dependency requires stable semantics not to be derived from downstream Tool implementation.
- Relation-Declaration Slot Discipline requires the direct semantic owner and exact participants; a schema or representation does not establish the world-side relation by itself.
- Trust and Evaluation Calculus treats evaluation as typed and bounded; provenance labels alone do not prove the represented claim.
- Measurement and Metrics Characterization supports treating configured LLM confidence as context-bound rather than universally comparable.
- Evidence Graph Referring distinguishes claim, source, carrier, work, and currentness; exact source references preserve provenance but do not establish claim-to-value truth.

### Return condition

Repeat this bounded audit after effective setting values and their source selections are deterministically extracted from governed RMED authority, the Map is a pure derived output rather than preserved semantic input, claim-to-value correspondence is validated, and the five identified META Cores are narrowed or split without losing authority.

## Open questions (confidence <95%)

1. **What does “Project RMED Atom” mean in the settings authority? — 91%.** CAPRMEDIO uses `PROJECT` as a named structural root, but the current settings frontier includes Project, META, GOV, SPEC, and REALIZATION sources. If the intended meaning is any applicable RMED Atom in the current project, the authority should use that canonical phrase. If it means only Project-root RMED, the current frontier is too broad.

2. **Where should machine-readable setting values be encoded? — 89%.** Two coherent designs remain inside current Principles: encode each setting value in the owning RMED Atom through a governed field/grammar, or establish one governed RMED source Atom for a cohesive setting set. The audit can reject hardcoded Tool ownership and a self-authoring Projection, but it cannot select between these two authority-preserving encodings without an operator decision.

## Skills used

- `fpf-alignment-audit` — bounded post-implementation alignment audit and report persistence.
- No subagents or additional skills were used.

FPF sources consulted:

- `E.03 — Principle Taxonomy & Precedence Model`
- `E.05.03 — Unidirectional Dependency`
- `A.06.05 — Relation-Declaration Slot Discipline`
- `B.03 — Trust and Evaluation Calculus`
- `C.16 — Measurement & Metrics Characterization`
- `A.10 — Evidence Graph Referring`
