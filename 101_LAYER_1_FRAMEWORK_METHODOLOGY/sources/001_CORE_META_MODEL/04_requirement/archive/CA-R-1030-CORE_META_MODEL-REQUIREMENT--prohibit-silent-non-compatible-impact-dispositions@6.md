---
atom_id: CA-R-1030
cce_version: cce_1
cce_form: prohibition
subjects:
  governs:
    continuant:
      - relation-model
  depends_on:
    continuant:
      - atom-boundary
version: 6
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-310-CORE_META_MODEL-REQUIREMENT--classify-lineage-impact-with-four-dispositions
---
# Prohibit silent non-compatible Impact dispositions

TOOLING **must not** select `update_required`, `replacement_required`, **or** `uncertain` **without** an explicit governed disposition.
