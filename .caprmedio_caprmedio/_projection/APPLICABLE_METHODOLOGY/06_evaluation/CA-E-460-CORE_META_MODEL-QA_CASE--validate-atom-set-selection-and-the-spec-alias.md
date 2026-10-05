---
atom_id: CA-E-460
content_role: Evaluation
type: QA Case
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Atom selection"
  depends_on:
    - "Atom Collection"
    - "Atom/Claim"
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Content Role"
    - "Atom/Status"
    - "Hub Atom"
    - "Owned Atoms"
    - "Scope Unit"
    - "Subtree-owned Atoms"
    - "Subtree-targeting Atoms"
    - "Targeting Atoms"
version: 12
updated_at: "2026-10-01 21:46:55 +0400"
relations: {"evaluation_for": ["CA-D-482", "CA-D-495", "CA-M-273", "CA-M-288", "CA-R-1271", "CA-R-1447", "CA-R-1448", "CA-R-1449", "CA-R-1595", "CA-R-1596", "CA-R-942"]}
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-460-CORE_META_MODEL-QA_CASE--validate-atom-set-selection-and-the-spec-alias.md
  source_atom_id: CA-E-460
  source_atom_revision: 12
  source_sha256: 630a6a8c3588ce3372c8543c8cc303db8a79ce911f7b144c645e5c7832c39fe5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate Atom-set Selection **and** the spec Alias

## Scope

the four ownership **and** targeting selections for a Scope Unit, including the `spec` alias.

## Claim

### Claim checked

ownership **and** Claim targeting produce their respective direct **and** recursive Atom sets, **and** the alias `spec` selects **only** Active RMED Subtree-targeting Atoms.

## Details

### Test case

construct Scope Unit `A`, its child Scope Unit `A_CHILD`, a sibling Scope Unit `B`, **and** nested Atom Collections inside `A`. the fixture Scope Units are Unordered. use the following distinct source Atoms; a Current-scope Atom explicitly carries its current Scope Unit as target. `d`, `e`, **and** `f` have Content Role Requirement **and** Type Demand under CA-R-932-CORE_META_MODEL-CORE-REQUIREMENT--define-demand-atom, with their applicable Demand conditions satisfied. the remaining rows are valid Current-scope Atoms with admitted non-relational Types; their resolved targets are carried internally under CA-D-482-CORE_META_MODEL-DELIVERY--carry-the-resolved-claim-target-scope-unit; equality **to** ownership does **not** make them Relational.

| Atom | Current Scope Unit | Placement | Claim Target Scope Unit | Content Role | Status |
|---|---|---|---|---|---|
| `a` | `A` | directly under `A` | `A` | Requirement | Active |
| `b` | `A` | nested Atom Collection | `A` | Method | Active |
| `c` | `A_CHILD` | directly under `A_CHILD` | `A_CHILD` | Evaluation | Active |
| `d` | `B` | directly under `B` | `A` | Requirement | Active |
| `e` | `B` | directly under `B` | `A_CHILD` | Requirement | Active |
| `f` | `A` | directly under `A` | `B` | Requirement | Active |
| `g` | `A` | Draft placement | `A` | Requirement | Draft |
| `h` | `A` | directly under `A` | `A` | Plan | Active |
| `i` | `A` | Archived placement | `A` | Delivery | Archived |

derive **all** four sets for `A` **and** the alias `spec`. repeat **after** moving `a` into a nested Atom Collection under `A` **and** changing **only** Local Tiers; repeat with narrower **and** explicitly grouped composite Claim Scope restrictions **in** the Scope section for RMED, **or** the registered primary content for other roles, while retaining the carried targets; repeat with `b` assigned **every** RMED Content Role while retaining its other properties. **then** omit `B` from the claimed-complete source frontier, treat a Hub Plan as a Scope Unit, replace targeting with ownership, copy a selected Atom as new authority, omit a carried target, infer a different target from Claim text, use an unresolved structural target **or** cyclic ancestry, **or** register `spec` as a separate Entity.

### Acceptance criteria

the results **must** be:

| Selection | Members |
|---|---|
| Owned Atoms | `a, b, f, g, h, i` |
| Targeting Atoms | `a, b, d, g, h, i` |
| Subtree-owned Atoms | `a, b, c, f, g, h, i` |
| Subtree-targeting Atoms | `a, b, c, d, e, g, h, i` |
| `spec` alias | `a, b, c, d, e` |

collection nesting, textual applicability restrictions, **and** tier-only changes **must not** alter those results. `spec` **must not** create a separate Entity, independently maintained Atom set, **or** source of authority. incoming `d` **and** `e` retain ownership under `B`; outgoing `f` remains owned by `A` **without** entering its Targeting Atoms **or** `spec`. incomplete source coverage, missing **or** unresolved carried targets, targets inferred from Claim text, cyclic ancestry, ownership/target substitution, **and** duplicate authority fail explicitly.

### Failure disposition

report the source Revision, selected Scope Unit, expected set, **and** exact missing, extra, duplicated, **or** unresolved member; do **not** silently return a complete result **or** rewrite source ownership.
