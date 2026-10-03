---
subjects:
  governs: "Markdown Atom Carrier Validation"
  depends_on:
    - "Atom/Revision"
    - "Markdown Atom Carrier"
    - "Project"
version: 14
updated_at: "2026-09-25 13:06:06 +0000"
relations:
  evaluation_for:
    - CA-D-463
    - CA-D-479
    - CA-D-356
    - CA-D-470
atom_id: "CA-E-457"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
---
# Summary

Validate Authoritative Markdown Atom Carriers

## Claim

the Evaluation **must** reject an Atom Revision **if** it has other than **`=1`** authoritative Markdown Atom Carrier on the Project filesystem, its authoritative Carrier does **not** contain YAML Frontmatter followed by the Content-Role-specific structured Main Content under CA-D-479, **or** a TOML, YAML, JSON, database, **or** projected copy is treated as authoritative for that Atom Revision.

## Details

the body-structure checks include:

- exact heading spelling, cardinality, **and** order for the selected Content Role; a universal Claim heading is **not** a substitute for Question, Concern, Objective, **or** Operation.
- missing **or** duplicate required sections, unregistered peer sections, ambiguous section boundaries, **and** heading-like fenced examples.
- the nested Plan Definition of Done under CA-D-470; its absence **or** a second carried copy fails validation.

these are Carrier checks. semantic agreement between Details, the first block, **and** Summary requires the content Evaluation, **not** heading recognition alone.
