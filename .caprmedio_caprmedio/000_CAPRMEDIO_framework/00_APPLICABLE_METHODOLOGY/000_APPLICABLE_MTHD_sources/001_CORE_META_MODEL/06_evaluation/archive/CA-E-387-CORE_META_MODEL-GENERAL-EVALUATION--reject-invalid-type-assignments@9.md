---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Entity/Type"
  depends_on:
    - "Entity"
    - "Subject Expression"
    - "Type"
version: 9
updated_at: "2026-09-17 04:40:51 +0000"
relations: {"evaluation_for":["CA-R-1285","CA-R-1349","CA-R-1350"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject Invalid Type Assignments

the Evaluation **must** reject a Type assignment **if** **any** of the following holds:

- an Entity occurrence that bears Type has **`!=1`** direct Type values.
- the selected value is **not** allowed by its most-specific applicable qualified Type Subject.
- qualified Type Subjects create **`>1`** Type Property slots for the occurrence.

absence of a Type value **in** an Entity occurrence that does **not** bear Type is **not** a cardinality failure under this Evaluation.
