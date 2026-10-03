---
atom_id: CA-M-226
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Applicable Methodology Compilation
  depends_on:
    continuant:
      - Tool/COMPILE_APPLICABLE_METHODOLOGY
      - Applicable Methodology/Sources
      - Applicable Methodology/Compilation Output
version: 1
updated_at: 2026-08-27 21:37:28 +0400
relations:
  method_for:
    - CA-R-1240
---
# Compile Projected RMEDO Carriers Transactionally

to compile Applicable Methodology, `COMPILE_APPLICABLE_METHODOLOGY` **must** implement CA-M-224 mechanically, stage the complete projected RMEDO Carrier set under `.caprmedio_runtime`, preserve and revalidate every selected Source Carrier digest, and replace only files in `04_requirement`, `05_method`, `06_evaluation`, `07_delivery`, and `09_ops` through atomic file replacement with complete transaction rollback on failure.
