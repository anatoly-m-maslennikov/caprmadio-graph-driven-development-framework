---
atom_id: CA-D-492
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Tool/VALIDATE_ATOMS/Request"
  depends_on:
    - "Tool/VALIDATE_ATOMS"
    - "Action"
    - "Project Structure"
    - "Global Tier"
    - "Local Tier"
    - "Scope Unit"
    - "Artifact/Revision"
version: 2
updated_at: "2026-09-23 23:53:58 +0000"
relations:
  delivery_for:
    - CA-R-1622
    - CA-R-1623
  relates_to:
    - CA-O-087
---
# Summary

Serialize Atom validator requests

## Claim

a `VALIDATE_ATOMS` request **must** use a versioned JSON object carrying the Check Atoms inputs:

- `schema_version`: **=1** integer, initially `1`.
- `source_roots`: **>=1** absolute inventory-root paths. these bound candidate discovery; they do **not** define a Scope Unit **or** supply Atom Properties.
- `methodology`: **=1** object identifying applicable source-authority roots **or** the selected Applicable Methodology. optional `action_binding` records the executor-selected Action identity **and** Revision.
- `allowed_read_roots`: **>=1** absolute paths bounding reads; references do **not** grant permission.
- `selection`: **=1** object containing **>=1** of `scope_unit`, `global_tiers`, `local_tiers`, **or** `atoms`. `scope_unit` is a declared Scope Unit name; `include_descendants` is an optional Boolean, default `false`, admitted **only** with `scope_unit`. `global_tiers` is a nonempty integer list; `local_tiers` is a nonempty list of admitted Local Tier names.
- `selection.atoms`: a nonempty list of objects containing `atom_id` with optional `version` **or** `carrier_path`, **or** **only** `carrier_path` for a candidate lacking assigned identity. paths are absolute locators; supplied identity, Revision, **and** locator **must** agree. duplicate matches remain ambiguous. list membership does **not** create missing Atom values.
- optional `project_structure`: the authoritative declared structure Carrier **when** selection requires resolving Scope Unit identity **or** parentage; unavailable required structure remains an explicit selection gap.
- optional `reference_roots`: additional admitted resolution context, **not** targets; optional `limits`: selected execution limits; optional `run_context`: executor-supplied execution identifiers.
- optional `rule_bundle`: derived checks bound **to** governing identities/Revisions, **not** independent methodology authority.

selection behavior follows CA-O-087, including intersection of supplied criteria. unsupported fields, invalid shapes, empty selector lists, **or** `include_descendants` without `scope_unit` produce a request error. valid requests with unresolved membership produce an incomplete assessment **without** silent widening **or** narrowing.
