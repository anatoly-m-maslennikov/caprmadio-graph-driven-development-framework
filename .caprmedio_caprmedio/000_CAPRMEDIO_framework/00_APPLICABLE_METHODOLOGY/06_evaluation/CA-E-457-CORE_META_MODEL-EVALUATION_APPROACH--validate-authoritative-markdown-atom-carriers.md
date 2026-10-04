---
subjects:
  governs: "Markdown Atom Carrier Validation"
  depends_on:
    - "Atom/Revision"
    - "Markdown Atom Carrier"
    - "Project"
version: 15
updated_at: "2026-10-01 21:31:46 +0400"
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
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-457-CORE_META_MODEL-EVALUATION_APPROACH--validate-authoritative-markdown-atom-carriers.md
---
# Summary

Validate Authoritative Markdown Atom Carriers

## Scope

the authoritative Markdown Carrier **and** body structure of an Atom Revision.

## Claim

the Evaluation **must** reject an Atom Revision **if** it has other than **`=1`** authoritative Markdown Atom Carrier on the Project filesystem, its authoritative Carrier does **not** contain YAML Frontmatter followed by the Content-Role-specific structured Main Content under CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties, **or** a TOML, YAML, JSON, database, **or** projected copy is treated as authoritative for that Atom Revision.

## Details

the body-structure checks include:

- exact heading spelling, cardinality, **and** order for the selected Content Role; a universal Claim heading is **not** a substitute for Question, Concern, Objective, **or** Operation.
- RMED requires Scope, Claim, **and** Details **in** that order; the earlier Claim **and** Details layout alone fails. Scope **and** Claim **must** be separately addressable; an empty Details section remains admitted under CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties.
- missing **or** duplicate required sections, unregistered peer sections, ambiguous section boundaries, **and** heading-like fenced examples.
- the nested Plan Definition of Done under CA-D-470-CORE_META_MODEL-DELIVERY--serialize-plan-file-sections; its absence **or** a second carried copy fails validation.

these are Carrier checks. semantic agreement between the primary contribution, its applicability, Details, **and** Summary requires the content Evaluation, **not** heading recognition alone.
