---
subjects:
  governs: "Artifact/Carrier Placement"
  depends_on:
    - "Project"
    - "Atom/Content Role"
    - "Structural Entity"
    - "Directory Carrier"
version: 9
updated_at: "2026-09-17 15:24:58 +0000"
relations: {"relates_to":["CA-D-296","CA-D-451"]}
---
# Register Project Current-Scope Content Role Directories

the caprmedio Project **must** use the following administrative Content Role directories directly under `.caprmedio_caprmedio/` for its current-scope Artifact placement:

- `01_concern/`;
- `02_analysis/`;
- `03_plan/`;
- `04_requirement/`;
- `05_method/`;
- `06_evaluation/`;
- `07_delivery/`;
- `08_implementation/`;
- `09_operations/`.

materialization follows CA-D-296. these administrative directories provide placement; they do **not** become Structural Entities **or** Directory Carriers under CA-D-451.
