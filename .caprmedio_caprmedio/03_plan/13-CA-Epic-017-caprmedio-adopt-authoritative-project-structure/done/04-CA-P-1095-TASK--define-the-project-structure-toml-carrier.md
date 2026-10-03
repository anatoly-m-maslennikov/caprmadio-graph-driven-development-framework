---
atom_id: CA-P-1095
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Carrier"
  depends_on:
    - "Artifact"
    - "Atom"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
version: 3
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  depends_on:
    - CA-P-1094
---
# Define the Project Structure TOML Carrier

the Assignee **must** establish the Delivery authority for the authoritative Project Structure TOML Carrier.

## Scope

CORE_META_MODEL at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`; active D authority for structural manifests, per-Project storage, naming, schema, settings overrides, **and** downstream structural Projection Carriers.

## Definition of Done

the Task is **not** Done **if** (the Carrier omits an accepted readability field **or** retains retired duplicate fields **or** stores concrete per-unit path values **in** D Atoms **or** has no distinguishable source/Projection identity **or** lacks precise optional-field, revision/currentness, path-reference, **and** migration-state rules).

## Details

declare the final per-Project location as `.caprmedio_<project name>/project_structure.toml`; for this Project it resolves **to** `.caprmedio_caprmedio/project_structure.toml`. preserve the accepted row shape:

```toml
[[scope_units]]
scope_unit_name = "FRAMEWORK_ENGINE"
parent = "PROJECT"
scope_unit_type = "Ordered"
scope_unit_label = "LAYER"
structural_level = 1
local_order = 2
navigational_order_number = 2
authority_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE"
delivery_path = "102_FRAMEWORK_ENGINE/"
authority_mode = "casual"
```

the example fixes schema **and** field responsibilities, **not** unverified inventory values. `local_order` is present **only** for Ordered units; `authority_mode` is an optional explicit override, **not** a copied effective default. retain `structural_level` **and** `authority_path` for readability **and** validate their declared consistency under R authority. do **not** restore `node_id`, `structural_parent`, `child_composition`, `project_boundary_position`, `authority_materialized`, **or** `numeric_prefix` as authored row fields.

define parent-reference resolution, path bases, optional-value omission, explicit-versus-default binding behavior, encoding, schema version **and** Artifact change/currentness evidence using existing authority rather than Atom-only metadata by analogy. keep concrete `authority_path` **and** `delivery_path` values **only** **in** Project Structure; D owns schema, placement, **and** general Carrier conventions. preserve source/derived separation for the existing graph Projection. define a candidate-to-authoritative cutover boundary so candidate preparation does **not** create two live authorities. review CA-D-297/299/300/374/380/391 **and** related rules. no actual Project Structure file is created by this Task.

execute **only** after the direct prerequisite is Done **when** one is declared. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve unrelated working-tree changes **and** historical records. creating this Task authorizes no execution by itself.

current scope correction: the Operator does **not** require a separate Project Structure Projection now. define the authoritative source Carrier **and** direct-consumer boundary; revise mandatory legacy structural-output declarations **without** adding a new derived structural Artifact. historical Projection formats **may** remain recognized **only** for migration evidence.

completion evidence: CA-D-440–445 define one authoritative TOML Carrier, schema version 1, the accepted 11-field row, optional values, safe repository-relative bindings, event-based Revision evidence, explicit candidate cutover **and** native Carrier layouts. 9 existing D Atoms were aligned, including default directory conventions, numeric TOML values, Settings ownership **and** optional legacy structural formats. 15 changed source files **and** their exact prior revisions were verified; no concrete manifest **or** Projection was created.
