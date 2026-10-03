---
atom_id: CA-M-226
cce_version: cce_1
cce_form: method
subjects:
  governs: "Applicable Methodology Compilation"
  depends_on:
    - "Tool/COMPILE_APPLICABLE_METHODOLOGY"
    - "Applicable Methodology/Sources"
    - "Applicable Methodology/Compilation Output"
version: 4
updated_at: 2026-09-15 05:51:38
relations:
  method_for:
    - CA-R-1240
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Compile Projected RMEDO Carriers Transactionally

to compile Applicable Methodology, `COMPILE_APPLICABLE_METHODOLOGY` **must** implement CA-M-224 mechanically, stage the complete projected RMEDO Carrier set under `.caprmedio_runtime`, preserve and revalidate every selected Source Carrier digest, and replace only files in `04_requirement`, `05_method`, `06_evaluation`, `07_delivery`, and `09_operations` through atomic file replacement with complete transaction rollback on failure.
