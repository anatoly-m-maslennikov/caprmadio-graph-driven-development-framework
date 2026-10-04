---
subjects:
  governs: "Project Structure"
  depends_on:
    - "Scope Unit"
    - "Project Settings"
    - "Framework Instance Settings"
    - "Carrier"
version: 8
updated_at: "2026-10-02 20:09:13 +0400"
relations:
  evaluation_for:
    - "CA-R-1483"
    - "CA-R-1484"
    - "CA-R-1485"
    - "CA-M-291"
atom_id: "CA-E-469"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-469-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--validate-project-structure-declarations.md
---
# Summary

Validate Project Structure declarations

## Scope

Project Structure declarations.

## Claim

the Evaluation **must** reject Project Structure **if**

- its registered Carrier schema is invalid,
- a Scope Unit Name is duplicated **or** invalid,
- a parent is unresolved **or** self-referential,
- parentage **contains** a cycle,
- a parent refers **to** another Project,
- a retained Structural Level disagrees with parent depth,
- **or** a declaration assigns an invalid Type, Label, order, navigation value, Authority Mode, **or** Carrier binding.

- Ordered siblings **must not** share structural Local Order; Navigational Order Number duplicates alone **must not** fail validation.
- an Unordered unit **must not** carry structural Local Order.
- Label **must not** determine Type.
- retained readable fields **must** agree with governing source fields **and** admitted Carrier exceptions.
- lexical **and** resolved-path collisions, traversal outside the authorized repository boundary, **and** ambiguous unit lookup **must** fail.
- the Evaluation **must** test a valid declaration **and** a falsifying example for **every** applicable condition, with explicit failures for unknown fields **or** unsupported schema versions.

## Details
