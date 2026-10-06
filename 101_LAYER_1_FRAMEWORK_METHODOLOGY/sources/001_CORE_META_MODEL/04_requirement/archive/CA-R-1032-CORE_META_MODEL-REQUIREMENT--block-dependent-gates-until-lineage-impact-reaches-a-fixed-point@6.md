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
---
# Block dependent gates until Lineage Impact reaches a fixed point

**every** release **or** downstream gate that requires a revised Atom **must** remain blocked **until** its Lineage Impact Analysis concludes that **every** affected branch has reached a fixed point.
