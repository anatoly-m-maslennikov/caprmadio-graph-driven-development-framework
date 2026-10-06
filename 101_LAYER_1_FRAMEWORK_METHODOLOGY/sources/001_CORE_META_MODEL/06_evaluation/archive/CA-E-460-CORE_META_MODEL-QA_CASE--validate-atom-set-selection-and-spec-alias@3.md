---
atom_id: CA-E-460
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom selection"
  depends_on:
    - "Owned Atoms"
    - "Targeting Atoms"
    - "Subtree-owned Atoms"
    - "Subtree-targeting Atoms"
    - "Scope Unit"
    - "Atom Collection"
    - "Atom/Claim/Structural Entity"
    - "Atom/Content Role"
    - "Atom/Status"
version: 3
updated_at: "2026-09-12 04:10:58 +0400"
relations:
  evaluation_for:
    - CA-R-919
    - CA-R-942
    - CA-R-1446
    - CA-R-1447
    - CA-R-1448
    - CA-R-1449
    - CA-M-273
    - CA-M-288
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Atom-set Selection and the spec Alias

## Claim checked

ownership **and** Claim targeting produce their respective direct **and** recursive Atom sets, **and** the alias `spec` selects **only** Active RMED Subtree-targeting Atoms.

## Test case

construct Scope Unit `A`, its child Scope Unit `A_CHILD`, a sibling Scope Unit `B`, **and** nested Atom Collections inside `A`. use the following distinct source Atoms; an omitted target resolves **to** the current Scope Unit.

| Atom | Current Scope Unit | Placement | Claim Structural Entity | Content Role | Status |
|---|---|---|---|---|---|
| `a` | `A` | directly under `A` | omitted | Requirement | Active |
| `b` | `A` | nested Atom Collection | omitted | Method | Active |
| `c` | `A_CHILD` | directly under `A_CHILD` | omitted | Evaluation | Active |
| `d` | `B` | directly under `B` | `A` | Requirement | Active |
| `e` | `B` | directly under `B` | `A_CHILD` | Requirement | Active |
| `f` | `A` | directly under `A` | `B` | Requirement | Active |
| `g` | `A` | Draft placement | `A` | Requirement | Draft |
| `h` | `A` | directly under `A` | `A` | Plan | Active |
| `i` | `A` | Archived placement | `A` | Delivery | Archived |

derive **all** four sets for `A` **and** the alias `spec`. repeat **after** moving `a` into a nested Atom Collection under `A` **and** changing **only** Local Tiers; repeat with `b` assigned **every** RMED Content Role while retaining its other properties. **then** omit `B` from the claimed-complete source frontier, treat an Epic as a Scope Unit, replace targeting with ownership, copy a selected Atom as new authority, use an unresolved structural target **or** cyclic ancestry, **or** register `spec` as a separate Entity.

## Acceptance criteria

the results **must** be:

| Selection | Members |
|---|---|
| Owned Atoms | `a, b, f, g, h, i` |
| Targeting Atoms | `a, b, d, g, h, i` |
| Subtree-owned Atoms | `a, b, c, f, g, h, i` |
| Subtree-targeting Atoms | `a, b, c, d, e, g, h, i` |
| `spec` alias | `a, b, c, d, e` |

collection nesting **and** tier-only changes **must not** alter those results. `spec` **must not** create a separate Entity, independently maintained Atom set, **or** source of authority. incoming `d` **and** `e` retain ownership under `B`; outgoing `f` remains owned by `A` **without** entering its Targeting Atoms **or** `spec`. incomplete source coverage, unresolved required bindings, cyclic ancestry, ownership/target substitution, **and** duplicate authority fail explicitly.

## Failure disposition

report the source Revision, selected Scope Unit, expected set, **and** exact missing, extra, duplicated, **or** unresolved member; do **not** silently return a complete result **or** rewrite source ownership.
