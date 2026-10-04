---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Applicable Methodology Compilation"
  depends_on:
    - "Tool/COMPILE_APPLICABLE_METHODOLOGY"
    - "Applicable Methodology/Sources"
    - "Applicable Methodology/Compilation Output"
version: 7
updated_at: "2026-10-04 23:02:50 +0400"
relations:
  method_for:
    - CA-R-1842
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Compile Projected RMEDO Carriers Transactionally

**to** compile Applicable Methodology, `COMPILE_APPLICABLE_METHODOLOGY` **must** implement CA-M-224 mechanically, stage the complete projected RMEDO Carrier set under `.caprmedio_runtime`, preserve **and** revalidate **every** selected Source Carrier's repository-relative path, Atom ID, Revision, byte digest, and source Relation, **and** replace **only** files **in** `04_requirement`, `05_method`, `06_evaluation`, `07_delivery`, **and** `09_operations` through atomic file replacement with complete transaction rollback on failure. A deleted derived role tree must be fully regenerated from the same current resolved frontier; the transaction never edits source authority.

## Sources

- CA-R-1842 v1; CA-M-224; CA-O-157 v2.
