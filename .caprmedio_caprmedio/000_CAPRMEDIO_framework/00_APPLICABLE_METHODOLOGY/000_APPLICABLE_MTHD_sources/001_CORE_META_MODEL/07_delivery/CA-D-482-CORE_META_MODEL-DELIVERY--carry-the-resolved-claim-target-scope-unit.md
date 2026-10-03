---
subjects:
  governs: "Atom/Claim/Target Scope Unit/Carrier"
  depends_on:
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Scope Unit"
    - "Project"
    - "Atom/Revision/Author"
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Scope"
    - "Current-scope Atom"
    - "Relational Atom"
version: 7
updated_at: "2026-10-02 19:54:46 +0400"
relations: {"relates_to": ["CA-R-1595", "CA-R-1596", "CA-R-922", "CA-R-923", "CA-D-478"]}
atom_id: "CA-D-482"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Carry the resolved Claim Target Scope Unit

## Scope

the frontmatter representation of an Atom's resolved Claim Target Scope Unit.

## Claim

a Markdown Atom Carrier **must** carry its resolved Claim Target Scope Unit **in** frontmatter, including a Current-scope Atom whose target is its own Scope Unit.

- choose the current Scope Unit as the default during authoring, **not** by relying on the file's later location.
- a carried target equal **to** the current Scope Unit does **not** make the Atom Relational. a different target still requires the applicable Relational Atom admission.
- Claim Scope restrictions use the body sections under CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections; the RMED Scope section does **not** replace **or** duplicate `claim_target_scope_unit`.

- encode this Property as the top-level nonempty YAML string `claim_target_scope_unit`, resolving **to** **=1** registered Scope Unit. null, lists, **and** a duplicated `claim_scope` field are **not** this encoding.
- an external Project Goal carries its Author fallback under CA-D-276-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter **in** `current_scope_unit` **and** the Project Scope Unit **in** `claim_target_scope_unit`; do **not** register the Author as a Scope Unit **or** infer either value from the filename.

## Details
