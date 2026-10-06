---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Operations/Type/Filename Token"
  depends_on:
    - "Atom/Content Role: Operations/Type"
    - "Atom/Content Role: Operations/Type: Foundation"
    - "Atom/Content Role: Operations/Type: Rule"
    - "Atom/Content Role: Operations/Type: Action"
    - "Atom/Content Role: Operations/Type: Workflow"
    - "Atom/Content Role: Operations/Type: Actor"
    - "Artifact/Carrier"
version: 1
updated_at: "2026-09-20 23:49:39 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-O-075", "CA-D-283", "CA-D-284", "CA-D-285"]}
---
# Serialize Operations Atom Type tokens

an Operations Atom File Carrier **must** serialize its Type using this filename-token mapping:

| Operations Atom Type | Filename token |
|---|---|
| Foundation | `FOUNDATION` |
| Rule | `RULE` |
| Action | `ACTION` |
| Workflow | `WORKFLOW` |
| Actor | `ACTOR` |
