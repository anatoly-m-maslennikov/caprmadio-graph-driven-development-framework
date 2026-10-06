---
atom_id: CA-E-459
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Project Settings Validation"
  depends_on:
    - "Project Settings"
    - "Project Settings/Authoritative Carrier"
    - "Project Settings/Revision Binding"
    - "Project Name"
    - "Atom/Identifier/Project Prefix"
    - "Framework Instance Settings"
    - "CORE_META_MODEL"
version: 7
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CAPRMEDIO-META-REQU-619
    - CAPRMEDIO-META-REQU-675
    - CA-R-1429
    - CA-D-318
    - CA-D-362
    - CA-D-363
    - CA-D-364
    - CA-D-365
    - CA-D-366
    - CA-D-375
    - CA-D-376
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Authoritative Project Settings Artifact

the Evaluation **must** reject Project Settings **if** it is treated as an Atom **or** Projection, has an Atom ID **or** Atom Content Role, is not available independently of Project Atoms **and** Implementation, violates its registered Project-root placement **or** filename, has other than **`=1`** authoritative TOML Carrier, contains Framework Instance choices **or** independently editable Project Structure, violates its Core content boundary, applicable General settings specifications, **or** applicable Standard field specifications, lacks a required CORE_META_MODEL definition **or** storage rule for Project Name **or** Project Atom prefix, lacks an Operator-selected Project Name, lacks an Operator-selected Project Atom prefix, treats a Methodology Atom, Framework Instance Settings, **or** a Projection as an independent authoritative source of either selected value, **or** lacks an exact current Revision, SHA-256 Digest, **and** governed-change Work Journal receipt.
