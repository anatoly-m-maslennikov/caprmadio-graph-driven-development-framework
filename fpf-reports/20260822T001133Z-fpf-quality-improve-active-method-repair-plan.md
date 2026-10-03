## Task, scope, and boundaries

### Loop contract and resolved FPF source

This is the repair plan for the active-Method audit’s per-claim alignment matrix. It converts each finding into the smallest ordered change set that can be applied and then re-evaluated. It does not yet mutate CAPRMEDIO authority. :codex-annotation{index="1"}

The repair object is the working-tree active Method set audited in `fpf-reports/20260821T231346Z-fpf-alignment-audit-active-methods.md`: 53 active Method carriers at semantic frontier `e591b890b4efa3af5c3df43f1ebd538374640fd5ab3b2c563c5fb954145a2adb`.

The new repository-root delivery topology is part of the proposed repair:

```text
FRAMEWORK_ENGINE/
├── SOFTWARE/
│   ├── TOOLS/
│   ├── APPS/
│   └── MCP/
└── AGENT_INTERFACE/
    └── SKILLS/
```

The direct FPF lens is E.23, Quality Improvement Loop Method. It requires an exact target version, a bounded change hypothesis, implementation evidence, re-evaluation with the same coordinates, protection of trade-offs, and an explicit stop, continue, rollback, or switch decision. FPF is a review lens; current CAPRMEDIO authority remains decisive.

Saved report: `fpf-reports/20260822T001133Z-fpf-quality-improve-active-method-repair-plan.md`.

### Baseline target version and evaluation

Baseline verdict: `unsupported`.

| Coordinate | Baseline |
|---|---:|
| Semantic blockers | 5 |
| Active Methods with no resolved Atom ID | 27 |
| Missing required Core tier | 4 |
| Duplicated `atom_id` frontmatter | 2 |
| Noncanonical filename-form relation references | 38 |
| Active direct relations to archived Atoms | 7 |
| Authored inverse `replacement_of` relations | 5 |
| Unregistered `relates_to` relations | 1 |

The baseline also has an absent composite priority selector, incomplete semantic-mapping checks, several claims that may be constraints rather than Methods, and ambiguity in projection ordering and software policy boundaries.

## High-confidence results (>=95%)

### Bounded change hypothesis and implementation evidence

The smallest coherent repair is five ordered phases. Semantic repairs must precede mechanical migration; otherwise renamed carriers would preserve contradictory authority and make the change harder to review.

#### Phase 1 — repair the five semantic blockers

1. **Lifecycle classification:** replace GOV Method 001’s “every semantic change creates a successor” rule with a fail-closed classifier implementing the existing `carrier_only`, `refinement`, `semantic_revision`, and `replacement` classes from GOV Requirement 311. Only `replacement` creates a new identity.
2. **Replacement ownership:** rewrite GOV Method 003 to author direct `replaced_by` on the predecessor and derive inverse `replacement_of`. The successor is created active; the predecessor is then archived. Active relations must not point into Archive. Keep historical closure in the archived carrier and Journal.
3. **Settings ownership:** retire or replace Tool Method 083 and its stale supporting Requirement/Evaluations. The replacement Method reads the one Project Configuration authority and admitted `project_graph_state` contributions; it must not compose `project_settings` from arbitrary RMED Atoms.
4. **Installation/runtime boundary:** change Tool Method 076 so executable releases and libraries run from `.caprmedio_install`; only mutable execution state is written under `.caprmedio_runtime`.
5. **Information lineage:** remove CA-M-091’s relations to the Operator-priority Requirement. Relate it to active information-preservation and necessary-complexity authority. If no accepted Requirement owns the intended information-preservation outcome, accept that Requirement first instead of inventing lineage to a draft.

#### Phase 2 — establish the Engine delivery topology

Move the repository-root implementation without changing each component’s internal subtree:

- `TOOLS`, `APPS`, and `MCP` under `FRAMEWORK_ENGINE/SOFTWARE/`;
- `SKILLS` under `FRAMEWORK_ENGINE/AGENT_INTERFACE/`.

Update imports, launchers, installers, Hook carriers, tests, and Delivery bindings to the new paths. Treat this first as a delivery/source grouping, not automatically as new graph authority. That avoids creating duplicate structural authority merely because folders exist.

Shared programmatic policies should apply to the bounded Software set—Tools, Apps, and MCP. Skills retain separate Agent Interface policies. A narrower Tool Method remains under Tools when it does not apply safely to Apps or MCP.

#### Phase 3 — close Method-family gaps

- Add one composite priority-selection Method for CA-R-860. It loads the effective priority order, applies non-negotiable constraints, invokes the relevant criterion Methods CA-M-093 through CA-M-100, defines tie and incomparability behavior, and returns unresolved choices to the Operator.
- Add an Evaluation-backed admissibility rule and stop condition to CA-M-105 through CA-M-108. Do not claim semantic preservation until the Operator selects the accepted threshold for equivalence, specialization, or tolerated loss.
- Scope CA-M-110 to Software, add its required Core tier and typed lineage, and state the evidence needed for a non-Python exception or new dependency.
- Operationalize CA-M-046’s deterministic-versus-LLM choice: required inputs, sufficient determinism, tie handling, cost comparison, and stop condition.
- Rewrite Methods 077 and 080 to emit exactly one final `Orphans` section after all normal groups.
- Keep CA-M-087 as one composite change-processing Method, but state that COMMIT_TRIGGER, COMMIT_CONTEXT, APPEND_CHANGE_RECORDS, and COMMIT_CHANGE_SET are participating Tools/mechanisms with explicit handoff contracts—not unnamed part-Methods.
- Reclassify the current claims in Tool Method 084, GOV Method 002, and GOV Method 010 when they only define an outcome, placement rule, or representation. Add a separate Method only where a reusable procedure is genuinely needed.
- Replace GOV Method 004’s unregistered `relates_to` with the exact registered typed relation that expresses its intended authority, likely `method_for` where the target is a Requirement.

#### Phase 4 — perform one sealed mechanical migration

Build a collision table before changing identities. The current Project `CAPRMEDIO-M-087` and Tool `CA-M-087` demonstrate why blind renumbering is unsafe. Operator acceptance is required for any stable-ID allocation or collision resolution.

After that decision:

- give every active Method one canonical `CA-M-NNN-...` identity;
- add `tier: core` to CA-M-103, CA-M-104, CA-M-109, and CA-M-110;
- remove embedded `atom_id` from CA-M-103 and CA-M-104;
- convert relation targets to exact Atom IDs;
- remove active-to-archived direct edges;
- remove all authored inverse `replacement_of` edges;
- keep direct `replaced_by` only where lifecycle authority permits it;
- validate each move as one governed Atom action with its related Journal records and Git commit.

Do not mix semantic rewrites and mass carrier migration in one commit. Separate commits preserve reviewability and permit phase rollback.

#### Phase 5 — regenerate and re-evaluate

Regenerate Project Graph State and every affected projection from the repaired authority. Then run the same active-only Method search and the same alignment coordinates used by the predecessor audit. Also run deterministic filename, frontmatter, tier, relation, lifecycle, archive-target, configuration-ownership, import, installation, and runtime-boundary checks.

### Re-evaluation and declared-coordinate comparison

No repair has been applied in this loop, so the result coordinates have not changed and improvement is **not demonstrated**.

The acceptance target for the next loop is:

| Coordinate | Required result |
|---|---:|
| Semantic blockers | 0 |
| Active Methods with no resolved Atom ID | 0 |
| Missing required Core tier | 0 |
| Duplicated `atom_id` frontmatter | 0 |
| Noncanonical filename-form relation references | 0 |
| Active direct relations to archived Atoms | 0 |
| Authored inverse `replacement_of` relations | 0 |
| Unregistered relation types | 0 |

Every residual adequacy gap must either be closed by accepted authority or explicitly deferred with an owner and reliance boundary. Passing mechanical validation alone is not sufficient.

### Trade-offs, costs, risks, and uncertainty

Protected properties are stable identity and history, DRY authority, graph traceability, the installation/runtime separation, the root source layout, and necessary complexity only.

The primary risk is treating the new root folders as proof that new governed Features exist. That would silently change the structural graph. The second risk is auto-renumbering legacy Methods before collision ownership is decided. The third is improving descriptions while leaving stale Requirements or Evaluations active, producing two authorities for the same meaning.

The cost is a staged migration rather than one bulk rename. The benefit is that each semantic decision remains recoverable and the final mechanical pass becomes deterministic.

### Outcome and stop/continue/rollback/switch decision

**Decision: stop for Operator disposition, then continue by applying the accepted repair phases.** The request asked how to fix the findings, not to mutate the authority. A repeated audit of the unchanged frontier would add no evidence.

Campaign handoff:

- campaign: `caprmedio-active-methods-20260821-e591b890`;
- current phase: repair proposal;
- predecessor: `fpf-reports/20260821T231346Z-fpf-alignment-audit-active-methods.md`;
- open finding families: lifecycle classification, replacement ownership, settings ownership, install/runtime boundary, information lineage, identity/tier/relations, priority composition, mapping criteria, Method adequacy, and root Engine layout;
- allowed next action: accept or adjust this repair batch, then apply it outside the review step;
- rollback boundary: one Git-recoverable commit per semantic repair or governed carrier action.

## Open questions (confidence <95%)

1. What semantic-preservation threshold governs CA-M-105 through CA-M-108: equivalence, permitted specialization, explicitly tolerated loss, or Operator acceptance case by case?
2. Are CA-M-093 through CA-M-100 a closed priority catalog or an extensible current set? The composite selector is needed either way, but only a declared universe can support a MECE claim.
3. Which stable IDs should be assigned to the 27 legacy Method carriers where current identities collide? This must not be guessed programmatically.
4. Should the present claims in Tool Method 084, GOV Method 002, and GOV Method 010 be reclassified as Requirements or Deliveries, or expanded into operational Methods? Their current form is insufficient as a Method, but the intended content-role ownership is an Operator decision.

## Skills used

- `fpf-quality-improve` — converted the bounded audit baseline into an ordered repair hypothesis, preserved explicit trade-offs, declared re-evaluation coordinates, and stopped before unaccepted authority changes.

#### FPF sources consulted (1 read; 1 used)

- `E_The FPF Constitution and Authoring Guides/22_23_Quality Improvement Loop Method/00_E.23 - Quality Improvement Loop Method.md` — used for versioned target selection, bounded change, same-coordinate re-evaluation, trade-off protection, and the stop/continue decision.
