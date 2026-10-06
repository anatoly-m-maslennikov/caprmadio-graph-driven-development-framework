---
atom_id: CAPRMEDIO-GOV-REQU-714
subjects:
  governs:
    continuant:
      - relation-model
  depends_on:
    continuant:
      - atom-boundary
cce_version: cce_1
cce_form: obligation
version: 10
updated_at: "2026-09-10 05:08:55 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-706
---
# Derive inverse structural ownership

CAPRMEDIO **must** derive the inverse `structural_children` view from stored `structural_parent` relations **and** **must not** persist that inverse separately.
