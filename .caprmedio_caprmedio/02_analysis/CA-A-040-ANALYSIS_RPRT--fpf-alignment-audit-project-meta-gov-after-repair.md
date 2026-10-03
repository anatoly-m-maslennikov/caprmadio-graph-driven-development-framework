---
atom_id: CA-A-040
subject_scopes:
  - authority
  - scope-topology
  - settings
  - carrier-format
version: 1
updated_at: 2026-08-21 01:52:33
---

## Task, scope, and boundaries

Audit whether the accepted repair plan resolved the previously identified alignment defects in CAPRMEDIO Project authority, META/GOV Core authority, and settings.

Receiving use: decide whether this bounded authority surface is coherent enough to continue upward construction, and identify any remaining blockers. This report is non-normative Analysis; it is not Evaluation, a release gate, or authorization to mutate carriers.

Audited repository state:

- Repository: `/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework`
- HEAD: `3730084af7f1a890415a22837cc6adee053e685d`
- Worktree: dirty, with 1,897 reported status paths; findings apply only to the inspected state.
- Saved report: `fpf-reports/20260818T015741Z-fpf-alignment-audit-project-meta-gov-after-repair.md`

Audit contract:

- Inspect all active Project RMED authority.
- Inspect active META and GOV Core RMED authority.
- Inspect current framework and Project settings carriers.
- Inspect downstream carriers only where needed to test strict parent/child topology.
- Inspect the repair migration helper where it can explain an observed defect.
- Test semantic irreducibility, tier ownership, relation direction, strict topology, settings separation, revision metadata, Projection replayability, and the confidence-threshold boundary.

Excluded from the claim:

- Downstream SPEC, REALIZATION, RELEASES, and FIELD semantic correctness.
- Runtime behavior of Tools and Skills.
- Generated catalogs or other Projections outside the two settings carriers.
- Tests, evaluations, release readiness, and repository acceptance. No tests or evaluations were run.

Evidence used: active carriers and settings in the worktree, the deterministic repair helper, a bounded relation/topology scan, TOML parsing, symlink resolution, `git diff --check`, and the consulted FPF sources listed below.

Acceptance boundary: the audited surface is aligned only if the accepted claims are semantically coherent, the strict authority graph is valid, and the carriers preserve enough identity, revision, provenance, and source-frontier information to replay the governed state. The audit must refuse acceptance when a required carrier property is absent even if the intended design is clear.

## High-confidence results (>=95%)

### Verdict

**unsupported**

The semantic decomposition and strict authority topology are now substantially repaired, but the checked repository state violates its own Atom revision rules and does not make either settings carrier fully replayable as its declared artifact form. Those are current-state blockers, not optional improvements.

### Per-claim alignment matrix

| Audited claim | Result | Confidence | Evidence |
|---|---|---:|---|
| DRY and materialized-representation authority were separated into irreducible owners | boundedly supported | 99% | REQU-003 now owns DRY; REQU-644 owns admission; GOV-645 owns reconciliation mechanics. |
| Previously overloaded META Cores were narrowed or split | boundedly supported | 98% | META-088, 113, 124, 125, and 155 are narrower; META-648 and META-655–660 carry the extracted definitions. |
| Core/Standard classification repairs were applied | boundedly supported | 99% | META-092, META-169, META-638, and GOV-338 now use the default Standard tier; META-180 was re-tiered. |
| Evaluation remains distinct from Requirement while retaining valid authority topology | boundedly supported | 99% | EVAL-001 uses `evaluation_for` for the assured claims and `child_of` for its normative parent. |
| Active strict Project/META/GOV RMED topology is acyclic, parent-covered, child-covered, directionally valid, and free of retired relation syntax | boundedly supported | 100% | Corrected deterministic scan: 317 active strict RMED carriers including the Goal, zero issues. Downstream active children were included; generated Catalog Projections were excluded. |
| Framework settings and Project settings are separated into exactly two settings carriers | boundedly supported | 99% | Root `caprmedio_framework_settings.toml`, generated `.caprmedio/caprmedio_project_settings.toml`, and the relative framework link all exist; both TOML files parse. |
| The LLM confidence threshold is treated as a configurable heuristic rather than a comparable universal measurement | boundedly supported | 98% | REQU-035 now binds decisions to the effective framework-owned threshold and disclaims cross-configuration comparability. |
| Every active Atom carries its governed revision metadata | unsupported | 100% | Twenty-five active strict-scope Atoms lack `version`, `updated_at`, or both, contrary to GOV-356. |
| Project Settings is a replayable generated Projection | unsupported | 100% | The TOML carrier has no `updated_at`, source frontier, generator/configuration binding, or exact source-Atom revisions required by META-166, META-627, and GOV-626. |
| Framework Settings has coherent Atom identity and revision semantics | unsupported | 99% | META-619 classifies it as an Atom; GOV-356 requires Atom revision properties; GOV-625 forbids embedded Atom identity/provenance metadata in the native TOML carrier; the file contains neither an authorized exception nor an external revision binding. |

### Resolved findings

1. **The accepted semantic splits are materially present.** The former multi-owner claims were narrowed into separate authority for DRY, materialized-copy admission and reconciliation, META eligibility, constitutional substrates, artifact forms, and tier meanings. Within this audit boundary, the new owners are more irreducible and their relations are directionally coherent.

2. **The strict authority graph is currently structurally clean.** The corrected scan found no missing required parents, no missing required children, no same-scope equal-tier parent edges, no tier-direction violations, no cycles, no active strict-scope references to inactive RMED carriers, no retired relation wrappers, and no active `technical_decision` subtype in the audited strict scopes.

3. **The two-settings architecture is materially represented.** [Framework Settings](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/caprmedio_framework_settings.toml:1) contains framework-operating thresholds. [Project Settings](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/caprmedio_project_settings.toml:1) contains derived Project structure and selections. The framework link resolves to `../../caprmedio_framework_settings.toml`; both TOML carriers parse; `git diff --check` passes.

### Blocking findings

1. **The repair migration removed mandatory revision metadata from 25 active Atoms.** The affected set is Project REQU-003, 035, 037, 644, and 646; META-088, 092, 113, 124, 125, 155, 169, 638, 648, and 655–660; and GOV-290, 338, 370, 645, and 647. [GOV-356](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-356--encode-atom-revision-properties.md:15) requires every Atom to carry a positive `version` and `updated_at`, with edits incrementing the version and refreshing the timestamp.

2. **The migration helper makes that regression reproducible.** [apply_fpf_audit_repairs.py](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/02_TOOLS/migrations/apply_fpf_audit_repairs.py:506) reconstructs Requirement frontmatter without `version` or `updated_at`; it also hardcodes run identity/time near the top of the file. Re-running the claimed idempotent repair would preserve the invalid metadata state.

3. **Project Settings is not self-describing enough to be replayed or checked for currentness.** [Project Settings](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/caprmedio_project_settings.toml:1) says it is generated from RMED authority but exposes neither `updated_at` nor the exact source frontier, generator identity, or configuration binding. Therefore a reader cannot distinguish current, stale, or unknown output, reconstruct the derivation, or verify the single-owner source selection required by [META-627](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-627--bind-project-settings-to-source-atoms.md:15).

4. **Framework Settings has contradictory artifact-form rules.** [META-619](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-619--classify-framework-settings-as-implementation-atom.md:15) makes it an Implementation Atom. GOV-356 requires Atom revision properties, while [GOV-625](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-625--encode-framework-settings-as-native-toml.md:14) forbids embedded identity, relation, rationale, and provenance metadata in its native TOML. The current authority supplies no alternate governed location for the required Atom identity and revision state.

### Return condition

Repeat this bounded audit after all 25 affected Atoms regain valid incremented revision metadata, the migration helper preserves those properties, Project Settings exposes currentness and exact derivation bindings, and the native Framework Settings identity/revision contradiction is resolved by explicit authority.

## Open questions (confidence <95%)

1. **Where should native Framework Settings Atom identity and revision metadata live? — 93%.** The strongest current option is to keep the executable TOML clean while deriving its canonical identity from its governed address and recording revision/currentness in a Journal or another explicitly governed external binding. Reclassifying it as a native Implementation carrier rather than an Atom is also coherent, but changes the artifact model. Without an operator decision, stable Atom identity and version conformance cannot both be demonstrated.

2. **How should Project Settings carry its exact source frontier without creating a third settings carrier? — 92%.** The best current answer is carrier-native Projection metadata inside the same TOML, including `updated_at`, generator/configuration identity, and exact source Atom references. A pointer to a separate generated manifest would weaken the accepted two-carrier simplicity. The exact table grammar remains undecided; until it is governed, replayability and currentness remain unsupported.

## Skills used

- `fpf-alignment-audit` — bounded, evidence-backed comparison of the implemented repair state against the relevant FPF patterns and CAPRMEDIO’s own accepted authority.
- No subagents or additional skills were used for this audit.

#### FPF sources consulted (6 read; 6 used)

1. `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/02_03_Principle Taxonomy & Precedence Model/00_E.03 - Principle Taxonomy & Precedence Model.md` — tier precedence, parent direction, and acyclic authority structure.
2. `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/04_05_Four Guard-Rails of FPF/03_E.05.03 - Unidirectional Dependency.md` — one-way dependency and semantic-stability boundaries.
3. `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/16_A.06.05 - Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline.md` — explicit relation meaning and participant discipline.
4. `FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/02_03_Trust and Evaluation Calculus (F-G-R with Congruence)/00_B.03 - Trust and Evaluation Calculus (F-G-R with Congruence).md` — bounded evaluation claims and evidence separation.
5. `FPF-Knowledge-Graph/C_Kernel Extension Specifications/04_16_Measurement & Metrics Characterization (MM-CHR)/00_C.16 - Measurement & Metrics Characterization (MM-CHR).md` — measurement context and non-comparability of uncalibrated confidence values.
6. `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/10_Evidence Graph Referring- Claim-Bound Evidence and Provenance Graph/00_A.10 - Evidence Graph Referring- Claim-Bound Evidence and Provenance Graph.md` — claim/carrier/provenance/currentness separation and replayable evidence binding.
