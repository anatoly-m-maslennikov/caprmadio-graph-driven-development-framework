---
subjects:
  governs: "Scope Reference Validation"
  depends_on:
    - "Atom/Scope"
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Claim"
    - "Atom/Subjects"
    - "Scope Unit"
    - "Project Structure"
    - "Operator"
    - "Hub Atom"
cce_version: cce_1
cce_form: evaluation
version: 24
updated_at: "2026-09-22 17:59:17 +0000"
relations: {"evaluation_for": ["CA-R-1595", "CA-R-1596", "CA-R-922", "CA-R-923", "CA-R-1588", "CA-R-1271", "CA-R-947", "CA-R-944", "CA-R-1201", "CA-R-1202", "CA-D-476", "CA-D-477"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Atom Scope and Claim Scope

## Claim checked

**every** Atom resolves its ownership, **`=1`** GOVERNS Relation, **and** **`=1`** Claim Target Scope Unit independently of **any** applicability restrictions **in** its Claim text.

## Test case

create a Current-scope Atom with an omitted target; repeat with a narrower restriction **and** a composite restriction **in** its Claim text. create a parent-owned Goal for a declared direct child, an Operator-owned Project Goal with an explicit Project target, **and** a permitted Demand. include a Plan **in** a nested Hub whose omitted target resolves **to** its owning Scope Unit.

**then** omit a required nondefault target, provide two target values, supply a Hub **or** another non-Scope-Unit target, leave a reference unresolved, infer a different target merely from textual restrictions, change ownership from the target, make the referenced Scope Unit bearer-dependent, reorder Subject declarations, **or** use a forbidden Goal **or** Demand target.

## Acceptance criteria

**every** valid fixture retains its ownership, resolves **`=1`** canonical GOVERNS target **and** **`=1`** Claim Target Scope Unit, **and** preserves its applicability restrictions **in** the Claim text. an omitted target resolves **to** the current Scope Unit **where** one exists; an Operator-owned Goal requires its explicit Project target. narrower **or** composite Claim Scope alone does **not** make an Atom Relational. a different permitted target does **not** transfer ownership **or** create Scope Unit ancestry. Subject ordering **and** Hub nesting do **not** change these facts. **every** invalid fixture fails with the exact affected fact identified.

## Failure disposition

report the invalid Atom **and** ownership, target, textual restriction, **or** Subject fact; do **not** repair unresolved references by guessing.
