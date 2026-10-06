---
subjects:
  governs: "Workflow"
  depends_on:
    - "Step"
    - "Action"
    - "Atom/Content Role: Operations/Type: Step"
    - "Workflow/Relation Kind: On Result"
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations: {"method_for": ["CA-R-1570"]}
atom_id: "CA-M-305"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Workflow schemes using Step references

## Scope

Workflow schemes using Step references.

## Claim

**to** write a Workflow scheme, express the graph through references **to** its Step Atoms:

- use **`=1`** unambiguous reference for **every** graph node; readable node labels **may** accompany those references.
- state the entry, typed directed transitions, result conditions, **and** terminal outcomes against those nodes.
- place Action references **and** parameter/input bindings **in** the referenced Step Atoms rather than reproducing them **in** the scheme.
- reference reusable Action behavior from the Steps; do **not** paste it into either the Step **or** graph Claim.

## Details
