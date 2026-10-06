---
subjects:
  governs: "Atom/Claim/Target Scope Unit/Carrier"
  depends_on:
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Scope"
    - "Current-scope Atom"
    - "Relational Atom"
version: 3
updated_at: "2026-09-24 14:16:19 +0000"
relations: {"relates_to": ["CA-R-1595", "CA-R-1596", "CA-R-922", "CA-R-923", "CA-D-478"]}
---
# Summary

Carry the resolved Claim Target Scope Unit

## Claim

a Markdown Atom Carrier **must** carry its resolved Claim Target Scope Unit **in** frontmatter, including a Current-scope Atom whose target is its own Scope Unit.

- choose the current Scope Unit as the default during authoring, **not** by relying on the file's later location.
- a carried target equal **to** the current Scope Unit does **not** make the Atom Relational. a different target still requires the applicable Relational Atom admission.
- Claim Scope restrictions remain part of the Claim text under CA-D-477.

- encode this Property as the top-level nonempty YAML string `claim_target_scope_unit`, resolving **to** **=1** registered Scope Unit. null, lists, **and** a duplicated `claim_scope` field are **not** this encoding.
- an Operator-owned Project Goal carries the named Operator **in** `current_scope_unit` **and** the Project Scope Unit **in** `claim_target_scope_unit`; do **not** register the Operator as a Scope Unit **or** infer either value from the filename.
