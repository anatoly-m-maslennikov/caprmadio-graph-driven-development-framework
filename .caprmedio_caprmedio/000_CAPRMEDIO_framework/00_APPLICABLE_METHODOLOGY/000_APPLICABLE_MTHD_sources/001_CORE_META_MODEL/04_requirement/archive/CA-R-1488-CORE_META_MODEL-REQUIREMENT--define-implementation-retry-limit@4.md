---
version: 4
updated_at: "2026-09-18 14:16:20 +0000"
relations: {}
subjects:
  governs: "Implementation Retry Limit"
  depends_on:
    - "Workflow Run"
    - "Implementation Workflow"
    - "Implementation Retry Control"
    - "Atom/Content Role: Evaluation"
---
# Define Implementation Retry Limit

Implementation Retry Limit **means** the maximum number of additional fix-and-evaluate rounds permitted **after** the initial failed Evaluation **in** one Implementation Workflow Run.

- its value **must** be an integer **`>=0`**.
- a value **`=0`** permits no retry **after** the initial failure.
- the limit does **not** grant permission **to** repair, change authority, **or** bypass an applicable confidence threshold.
