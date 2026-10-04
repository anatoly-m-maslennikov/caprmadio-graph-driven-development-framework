---
subjects:
  governs: "Type-Qualified Status Validation"
  depends_on:
    - "Artifact/Revision/Status"
    - "Artifact/Activity"
    - "Atom/Content Role"
    - "Type"
    - "Atom/Content Role: Plan/Type: Plan/Status"
version: 19
updated_at: "2026-10-02 20:03:51 +0400"
relations: {}
atom_id: "CA-E-386"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-386-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--validate-type-qualified-status-and-artifact-activity.md
---
# Summary

Validate Type-Qualified Status and Artifact Activity

## Scope

Artifacts and their applicable Status and Activity.

## Claim

the Evaluation **must** reject an Artifact **if** **any** applicable condition holds:

- **when** an explicitly defined Status model applies, its Status domain is resolved outside its complete qualified Type **or** Atom Content Role **and** Type path, its current Status cardinality **`!=1`**, its current Status is **not** an allowed value of that domain, its Activity cardinality **`!=1`**, its Activity violates CA-R-1395-CORE_META_MODEL-CORE-REQUIREMENT--derive-active-artifact-activity **or** CA-R-1396-CORE_META_MODEL-CORE-REQUIREMENT--derive-inactive-artifact-activity, a prior transition coexists as current Status metadata, **or** a second revision-disposition axis duplicates Status.
- **when** no explicitly defined Status model applies, its Activity cardinality **`!=0`** under CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models.

the Evaluation **must not** substitute Active **or** Inactive for absent Activity **or** a missing, invalid, **or** ambiguous Status. an Artifact outside the applicability of CA-R-1307 **must not** fail this Evaluation merely because it has no Status **or** Activity.

## Details
