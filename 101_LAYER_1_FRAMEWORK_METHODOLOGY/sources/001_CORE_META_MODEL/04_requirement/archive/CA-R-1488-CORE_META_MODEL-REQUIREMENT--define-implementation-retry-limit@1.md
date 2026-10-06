---
version: 1
updated_at: "2026-09-16 13:33:23 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
subjects:
  governs: "Implementation Retry Limit"
  depends_on:
    - "Implementation Process"
    - "Implementation Retry Control"
    - "Atom/Content Role: Evaluation"
cce_version: cce_1
cce_form: definition
---
# Define Implementation Retry Limit

Implementation Retry Limit **means** the maximum number of additional fix-and-evaluate rounds permitted **after** the initial failed Evaluation **in** one Implementation Process execution.

- its value **must** be an integer **>=0**.
- a value **=0** permits no retry **after** the initial failure.
- the limit does **not** grant permission **to** repair, change authority, **or** bypass an applicable confidence threshold.
