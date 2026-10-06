---
subjects:
  governs: "Markdown Atom Carrier Validation"
  depends_on:
    - "Atom/Revision"
    - "Markdown Atom Carrier"
    - "Project"
version: 11
updated_at: "2026-09-22 23:02:20 +0000"
relations:
  evaluation_for:
    - CA-D-463
    - CA-D-479
    - CA-D-356
atom_id: "CA-E-457"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation"
---
# Summary

Validate Authoritative Markdown Atom Carriers

## Claim

the Evaluation **must** reject an Atom Revision **if** it has other than **`=1`** authoritative Markdown Atom Carrier on the Project filesystem, its authoritative Carrier does **not** contain YAML Frontmatter followed by structured Main Content under CA-D-479, **or** a TOML, YAML, JSON, database, **or** projected copy is treated as authoritative for that Atom Revision.
