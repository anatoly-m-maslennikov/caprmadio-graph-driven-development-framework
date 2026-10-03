---
subjects:
  governs: "Atom/Revision/Frontmatter"
  depends_on:
    - "Atom/Claim"
    - "Project Structure"
    - "Project Settings"
    - "Framework Instance Settings"
version: 10
updated_at: "2026-10-01 21:24:33 +0400"
relations:
  {"depends_on": ["CA-D-311", "CA-R-1750"]}
atom_id: "CA-D-398"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Encode configuration surfaces **in** owning Atoms

## Scope

configuration surfaces carried by their owning Atoms.

## Claim

an owning Atom **may** carry an optional machine-readable representation of its own Claim **only** **if** it faithfully preserves that Claim **and** is **not** an independent source. legacy `project_scope_unit_graph` **or** `project_graph_state` YAML maps **may** be read as migration evidence; they **must not** own current Scope Unit declarations, paths, Name/order values, Project identity, Atom prefix, **or** selected Authority Modes. Project initialization inputs belong **to** Project Settings; instance defaults belong **to** Framework Instance Settings; unit declarations **and** explicit unit overrides belong **to** Project Structure. this format does **not** require creation **or** consumption of a structural Projection.

## Details
