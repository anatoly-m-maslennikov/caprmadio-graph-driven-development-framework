---
atom_id: CA-R-1032
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - relation-model
  prerequisite:
    continuant:
      - atom-boundary
      - lifecycle-traceability
version: 4
updated_at: 2026-08-29 01:16:37 +0400
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-312--lineage-impact-analysis-records
---
# Block dependent gates until Lineage Impact reaches a fixed point

**every** release **or** downstream gate that requires a revised Atom **must** remain blocked **until** its Lineage Impact Analysis concludes that **every** affected branch has reached a fixed point.
