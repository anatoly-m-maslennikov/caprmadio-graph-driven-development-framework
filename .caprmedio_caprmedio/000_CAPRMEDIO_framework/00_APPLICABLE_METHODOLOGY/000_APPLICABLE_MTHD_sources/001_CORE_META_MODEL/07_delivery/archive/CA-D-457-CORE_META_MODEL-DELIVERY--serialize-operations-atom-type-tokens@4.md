---
subjects:
  governs: "Atom/Content Role: Operations/Type/Filename Token"
  depends_on:
    - "Atom/Content Role: Operations/Type"
    - "Atom/Content Role: Operations/Type: Action"
    - "Atom/Content Role: Operations/Type: Workflow"
    - "Atom/Content Role: Operations/Type: Step"
    - "Atom/Content Role: Operations/Type: Actor"
    - "Artifact/Carrier"
version: 4
updated_at: "2026-09-21 00:57:42 +0000"
relations: {"relates_to": ["CA-R-1565", "CA-D-283", "CA-D-284", "CA-D-285", "CA-R-1569"]}
---
# Serialize Operations Atom Type tokens

an Operations Atom File Carrier **must** serialize its Type using this filename-token mapping:

| Operations Atom Type | Filename token |
|---|---|
| Action | `ACTION` |
| Workflow | `WORKFLOW` |
| Step | `STEP` |
| Actor | `ACTOR` |
