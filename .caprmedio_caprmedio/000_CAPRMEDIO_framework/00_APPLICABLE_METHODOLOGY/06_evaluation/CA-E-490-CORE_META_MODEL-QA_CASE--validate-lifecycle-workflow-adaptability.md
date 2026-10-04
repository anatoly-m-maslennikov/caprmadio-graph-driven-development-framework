---
subjects:
  governs: "Workflow"
  depends_on:
    - "Entity"
    - "Atom"
    - "Atom/Content Role"
    - "Type"
    - "Status"
    - "Scope Unit"
    - "Atom Collection"
    - "Carrier"
version: 4
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for": ["CA-R-1521"]}
atom_id: "CA-E-490"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-490-CORE_META_MODEL-QA_CASE--validate-lifecycle-workflow-adaptability.md
---
# Summary

Validate lifecycle Workflow adaptability

## Scope

a status-change Workflow **and** its target Entity's applicable model.

## Claim

the Evaluation **must** check that a status-change Workflow follows the target Entity's applicable model under CA-R-1521.

## Details

- supply **`=2`** applicable status models with different admitted values, including a newly admitted value absent from the original model; the same Workflow definition **must** support their admitted transitions.
- specialize an Atom's model by Content Role **and** Type; checking **only** a universal Atom value list fails.
- supply an applicable Scope Unit **or** Atom Collection model; admit its valid change **without** imposing an Atom lifecycle.
- request an unknown value, a prohibited transition, **or** a change **without** a defined model: reject **without** inventing a value **or** bypassing required Carrier behavior.
- supply a model requiring an unsupported capability: require an explicit limitation rather than a false pass.

these cases validate the methodology definition; an executor requires separate Implementation checks.
