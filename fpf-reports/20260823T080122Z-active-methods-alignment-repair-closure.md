## Task, scope, and boundary

This report closes the repair loop opened by `20260821T231346Z-fpf-alignment-audit-active-methods.md` and planned in `20260822T001133Z-fpf-quality-improve-active-method-repair-plan.md`.

The evaluated target is the current active Method frontier and the upstream authority changed specifically to repair that frontier. The result is a working-tree snapshot, not a released or commit-pinned baseline. The repository contains a larger uncommitted migration, so this report does not claim that every active CAPRMEDIO Atom is relation-clean.

No test suites were run. Verification used current authority inspection, governed Tool dry runs and receipts, static parsing, projection regeneration, installation status, and repeatable active-Method recounts.

## Outcome

**The requested active-Method alignment matrix is closed.** All eight original blocking coordinates now meet the accepted zero-defect target within the active Method frontier.

| Coordinate | Baseline | Current result |
|---|---:|---:|
| Semantic blockers | 5 | 0 |
| Active Methods with no resolved Atom ID | 27 / 53 | 0 / 71 |
| Missing or invalid required Core tier | 4 | 0 |
| Duplicated `atom_id` frontmatter | 2 | 0 |
| Noncanonical relation targets | 38 | 0 |
| Active direct relations to inactive Atoms | 7 | 0 |
| Authored inverse or deferred replacement relations | 5 | 0 |
| Unregistered relation keys | 1 | 0 |

The live frontier contains 71 active Method carriers, 71 resolvable and unique canonical Method IDs, 127 canonical relation occurrences, and no filename/path conflicts in the inspected migration frontier. All 51 `method_for` relations target active Requirements. The external `CA-INTENT` Goal stem remains the explicit permitted non-Atom-ID reference.

## Applied repair phases

### 1. Semantic blockers

- Aligned lifecycle authority around `carrier_only`, `refinement`, `semantic_revision`, and `replacement`; only replacement creates a successor identity.
- Deferred formal replacement relations and made archival Journal events the replacement-history authority.
- Made Project Configuration the sole operator-settings owner and removed active ordinary `project_settings` maps.
- Separated immutable installed Tool code under `.caprmedio_install` from mutable state under `.caprmedio_runtime`.
- Repaired CA-M-091 lineage to information-preservation and necessary-complexity authority.
- Added graph-loose `REPLACE_ATOM` and `CLOSE_ATOM` intent Doers without inventing formal relation payloads.

### 2. Framework Engine topology

The repository-root delivery tree is now:

```text
002_FRAMEWORK_ENGINE/
├── SOFTWARE/
│   ├── TOOLS/
│   ├── APPS/
│   └── MCP/
└── AGENT_INTERFACE/
    └── SKILLS/
```

This is a delivery/source grouping. It does not create duplicate SOFTWARE or AGENT_INTERFACE Scope Units in the governed graph.

### 3. Method-family closure

- Added one composite priority-selection Method with constraints, ordered criteria, tie/incomparability handling, and Operator escalation.
- Added semantic-mapping admissibility authority and Evaluation coverage.
- Bound Python to Framework Engine Software and recorded the technical contract in root `pyproject.toml` without turning the repository into a packaged distribution.
- Operationalized deterministic-versus-agentic execution selection.
- Required exactly one final `Orphans` section in each affected projection Method.
- Declared the four commit-flow participants as Tools/mechanisms in one composite Tool flow.
- Reclassified constraint-shaped Methods as Requirements where no reusable procedure existed.

### 4. Mechanical migration

Two governed dry-run-by-default Tools were added and installed:

- `MIGRATE_ATOM_IDENTITY` for one sealed carrier identity migration;
- `REBIND_ATOM_RELATIONS` for one sealed relation-only update.

The installed Tools applied 92 identity mutations and 169 consolidated relation rebinds. The final active Method allocation has no collisions, no filename-derived tier failures, and no duplicated `atom_id` or `tier` frontmatter.

### 5. Projection regeneration and re-evaluation

The installed generator rebuilt:

- `.caprmedio/project_scope_unit_graph.projection.toml`;
- `.caprmedio/project_scope_unit_graph_sources.projection.toml`.

The current projections contain 18 admitted contributions, 39 Scope Units, and 62 source bindings. A repeat installed-generator dry run returned `changed: false`. Both projection TOML files parse and contain no deleted carrier stems.

The selected installed release is `910458008e2d3f05ab9cfe3ac89e9f7acf17ec6eb05cd65eaf1363106f78a9c1`. Installer status reports source/install match, verified release bytes, all 15 launchers available, Git hooks registered, and all four Codex hook phases present.

## Final narrow upstream cleanup

The same installed relation Doer removed two residual authority payloads found during semantic re-evaluation:

- CA-R-1051 v7 to v8: removed deferred `replacement_of`;
- CA-R-1053 v9 to v10: removed unregistered `relates_to`.

No replacement relation was invented. IDs may remain in prose or code docstrings, while formal relation realization stays deferred.

## Residual boundary

The broader active-Atom graph, outside the requested active-Method matrix, still contains 120 `replacement_of` payloads and 22 `relates_to` payloads. A mass deletion was not performed because replacement history may first need sealed migration into authoritative archival Journal events. That requires a separate history-preserving migration contract before mutation can meet the 97% confidence threshold.

Two legacy projection generators were also not run: their targets are archived or absent and their selectors do not recognize the migrated `CA-*` carriers. They are not part of the current Scope Unit Graph projection path.

## Decision

**Stop the active-Method repair loop as closed.** Reopen it only after a material Method-authority change. Treat the broader legacy relation cleanup as a separate governed migration, not as an unbounded continuation of this matrix repair.
