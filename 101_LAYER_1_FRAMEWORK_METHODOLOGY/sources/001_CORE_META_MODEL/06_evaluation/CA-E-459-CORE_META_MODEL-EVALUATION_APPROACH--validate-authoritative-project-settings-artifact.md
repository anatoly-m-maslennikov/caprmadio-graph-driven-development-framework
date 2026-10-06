---
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
version: 16
updated_at: "2026-10-02 20:09:13 +0400"
relations:
  evaluation_for:
    - CA-R-1738
    - CA-R-1750
    - CA-R-1429
    - CA-D-318
    - CA-D-362
    - CA-D-363
    - CA-D-364
    - CA-D-365
    - CA-D-366
    - CA-D-375
    - CA-D-376
atom_id: "CA-E-459"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
---
# Summary

Validate Authoritative Project Settings Artifact

## Scope

authoritative Project Settings Artifacts.

## Claim

the Evaluation **must** reject Project Settings **if**

- it is treated as an Atom **or** Projection,
- has an Atom ID **or** Atom Content Role,
- is **not** available independently of Project Atoms **and** Implementation,
- violates its registered Project-root placement **or** filename,
- has other than **`=1`** authoritative TOML Carrier,
- **contains** Framework Instance choices **or** independently editable Project Structure,
- violates its Core content boundary, applicable General settings specifications, **or** applicable Standard field specifications,
- lacks a required CORE_META_MODEL definition **or** storage rule for Project Name **or** Project Atom prefix,
- lacks an Operator-selected Project Name,
- lacks an Operator-selected Project Atom prefix,
- treats a Methodology Atom, Framework Instance Settings, **or** a Projection as an independent authoritative source of either selected value,
- **or** lacks an exact current Revision, SHA-256 Digest, **and** governed-change Work Journal receipt.

## Details
