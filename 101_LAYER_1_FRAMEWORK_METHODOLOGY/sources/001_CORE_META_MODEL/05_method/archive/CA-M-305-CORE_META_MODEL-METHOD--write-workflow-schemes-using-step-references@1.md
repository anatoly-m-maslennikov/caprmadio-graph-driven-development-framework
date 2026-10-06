---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Workflow"
  depends_on:
    - "Step"
    - "Action"
    - "Atom/Content Role: Operations/Type: Step"
    - "Workflow/Relation Kind: On Result"
version: 1
updated_at: "2026-09-21 00:57:42 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"method_for": ["CA-R-1570"]}
---
# Write Workflow schemes using Step references

**to** write a Workflow scheme, express the graph through references **to** its Step Atoms:

- use **`=1`** unambiguous reference for **every** graph node; readable node labels **may** accompany those references.
- state the entry, typed directed transitions, result conditions, **and** terminal outcomes against those nodes.
- place Action references **and** parameter/input bindings **in** the referenced Step Atoms rather than reproducing them **in** the scheme.
- reference reusable Action behavior from the Steps; do **not** paste it into either the Step **or** graph Claim.
