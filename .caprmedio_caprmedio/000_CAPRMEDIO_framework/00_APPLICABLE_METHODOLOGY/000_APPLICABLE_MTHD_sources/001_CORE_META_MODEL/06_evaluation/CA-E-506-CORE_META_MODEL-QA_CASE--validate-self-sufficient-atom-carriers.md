---
subjects:
  governs: "Atom/Carrier/Validation"
  depends_on:
    - "Atom/Revision/Author"
    - "Atom"
    - "Atom/Property"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Revision/Status"
    - "Relation"
    - "Markdown Atom Carrier"
version: 7
updated_at: "2026-10-01 21:33:03 +0400"
relations: {"evaluation_for": ["CA-R-1598", "CA-R-1599", "CA-D-478", "CA-D-479", "CA-D-480", "CA-D-481", "CA-D-482", "CA-D-483", "CA-D-485", "CA-D-460", "CA-D-470"]}
atom_id: "CA-E-506"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
---
# Summary

Validate self-sufficient Atom Carriers

## Scope

self-sufficiency **and** representation consistency of Markdown Atom Carriers.

## Claim

the Evaluation **must** accept **only** Atom Carriers that preserve self-sufficiency, **`=1`** internal value source, **and** consistent outward representations.

## Details

### Test case

- construct a valid Atom with its required Properties inside its Markdown Carrier, using the applicable registered fields **and** body sections. include a required defaulted value, an optional absent Property, **and** an inapplicable Property that is correctly absent.
- extract Summary **and** the Content-Role-specific primary contribution under CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties **without** reading the filename **or** containing directories. include fenced code containing example headings; those examples **must not** create Property boundaries.
- for RMED, include **`=1`** Scope, **`=1`** Claim, **and** **`=1`** Details section **in** that order. extract Scope **and** Claim independently; an empty Details section is valid **when** no required nested Property applies. include narrower **and** composite applicability **without** changing the carried target Scope Unit.
- compare the carried values against filename **and** placement representations using the applicable encoding. include a Summary whose slug differs from its readable text.
- include a Current-scope target explicitly equal **to** its owner; it remains Current-scope. include a permitted different target **and** an external Project Goal with its Author fallback.
- include a Plan with its mandatory Markdown file **and** DoD nested inside Details, with **and** **without** a matching directory; include a child-owned decomposition edge with its inverse derived.
- include an unselected inherited confidence setting **and** a selected override currently equal **to** inheritance; change the upstream setting **and** check that **only** the inherited selection follows it.
- include invalid RMED fixtures with missing Scope, duplicated Scope, Scope **after** Claim, a Scope section used instead of Claim, **or** a second applicability copy **in** frontmatter.
- create invalid fixtures by removing a required internal value, supplying that value **only** through an address, duplicating it **in** frontmatter **and** body, repeating a heading **or** YAML key, renaming a required heading, introducing an ambiguous boundary, conflicting with the address, omitting a Plan's file **or** DoD, **or** storing an inverse Atom Relation independently.

### Acceptance criteria

- **every** valid fixture yields the expected Property values **and** Relations.
- **every** invalid fixture fails with the exact Property, location, Relation, **or** address conflict identified.
- address **and** inverse checks **must not** silently rewrite the source **or** treat derived representations as separate authority.
