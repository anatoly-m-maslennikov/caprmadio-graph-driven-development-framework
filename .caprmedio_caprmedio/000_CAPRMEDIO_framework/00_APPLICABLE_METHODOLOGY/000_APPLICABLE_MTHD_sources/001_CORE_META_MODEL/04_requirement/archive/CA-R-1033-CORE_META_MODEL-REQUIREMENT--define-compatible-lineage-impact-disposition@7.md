---
atom_id: CA-R-1033
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Compatible Lineage Impact Disposition
  depends_on:
    continuant:
      - atom-boundary
      - relation-model
version: 7
updated_at: 2026-09-07 09:59:57 +0000
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-310-CORE_META_MODEL-REQUIREMENT--classify-lineage-impact-with-four-dispositions
---
# Define compatible Lineage Impact disposition

`compatible` **means** the child remains valid against the parent Revision required by the gate **and** traversal stops on that branch **without** a child update. **if** the gate requires the revised parent, **then** compatibility **must** be established against that new Revision; permission to consume a pinned earlier Revision **must not** establish compatibility for a gate that requires the new Revision.
