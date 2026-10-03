---
atom_id: CA-R-1032
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - relation-model
  depends_on:
    continuant:
      - atom-boundary
      - lifecycle-traceability
version: 6
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-312-CORE_META_MODEL-REQUIREMENT--record-one-lineage-impact-analysis-per-changed-atom-revision
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1032-CORE_META_MODEL-REQUIREMENT--block-dependent-gates-until-lineage-impact-reaches-a-fixed-point.md
---
# Block dependent gates until Lineage Impact reaches a fixed point

**every** release **or** downstream gate that requires a revised Atom **must** remain blocked **until** its Lineage Impact Analysis concludes that **every** affected branch has reached a fixed point.
