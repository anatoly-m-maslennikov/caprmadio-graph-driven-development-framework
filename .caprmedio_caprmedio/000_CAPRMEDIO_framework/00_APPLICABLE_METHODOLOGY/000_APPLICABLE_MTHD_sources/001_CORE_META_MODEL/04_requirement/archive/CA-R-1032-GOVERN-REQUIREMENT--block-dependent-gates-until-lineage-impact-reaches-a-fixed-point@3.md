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
version: 3
updated_at: 2026-08-23 15:24:07
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-312--lineage-impact-analysis-records
---
# Block dependent gates until Lineage Impact reaches a fixed point

EVERY release or downstream gate that requires a revised Atom MUST remain blocked until its Lineage Impact Analysis concludes that every affected branch has reached a fixed point.
