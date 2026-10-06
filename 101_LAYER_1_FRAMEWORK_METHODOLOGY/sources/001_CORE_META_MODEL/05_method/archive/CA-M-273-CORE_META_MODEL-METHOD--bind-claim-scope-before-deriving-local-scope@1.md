---
atom_id: CA-M-273
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - "Scope Unit/Scope/derivation"
  depends_on:
    continuant:
      - "Scope Unit"
      - "Atom/Scope"
      - "Atom/Claim/Scope"
      - "Atom/Content Role"
      - "Atom/Status"
      - "Atom/Revision"
      - "Structural Parent Relation"
version: 1
updated_at: "2026-09-10 02:19:47 +0400"
relations: {}
---
# Bind Claim Scope before deriving local Scope

**to** derive a Scope Unit's Scope under CA-R-931, the resolver **must** perform **all** of:

1. verify the complete coherent authoritative frontier **and** its current Atom identities, Active Revisions, digests, ownership, Content Roles, complete Claims, Subjects, **and** explicit Scope constraints; generated copies **and** archived Revisions are **not** additional active inputs.
2. resolve the structural owner independently of Claim Scope, **then** resolve Atom Scope from its current Scope Unit context **or** named Operator fallback, governed Entity, **and** explicit Claim constraints under CA-R-1014; a reference **to** another Scope Unit **must not** transfer ownership.
3. bind an omitted Claim Scope **to** the current Scope Unit context under CA-D-367. resolve an explicit expression in its authoring context under the applicable Scope-expression authority, using CA-M-121 **where** its grammar applies; retain composite grouping **and** constraints, **and** determine whether its target differs from current Scope **without** selecting a highest tier, deriving candidate members first, **or** discarding contradictory explicit targeting.
4. derive the set governed by CA-R-931 from those resolved bindings. retain inherited applicability **and** incoming **or** outgoing relational Claims as separately effective authority **without** transferring their ownership **or** including descendant-owned Atoms; a complete empty basis remains empty **without** removing the Scope Unit **or** its other obligations.
5. report the exact unresolved source, owner, expression, **or** binding **and** withhold a complete Scope result **when** the required information is incomplete, contradictory, ambiguous, **or** cannot be resolved independently of the set being derived. do **not** choose a fixed point, silently omit an ambiguous Atom, equate incomplete input with an empty set, **or** infer unconstrained authority from emptiness.
