---
subjects:
  governs: "Project/normative authority graph"
  depends_on:
    - "Project"
    - "Relation"
    - "Normative Authority Relation Pair"
version: 5
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for":["CA-R-833","CA-R-808","CA-R-879"]}
atom_id: "CA-E-481"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
---
# Summary

Validate the normative-authority hierarchy

## Scope

the active normative-authority subgraph.

## Claim

the Evaluation of the active normative-authority subgraph **must** fail **when** **any** declared authority-bearing direct edge lacks its registered typing **or** the directed subgraph **contains** a cycle under CA-R-833.

## Details

- the evaluated input is the active normative-authority subgraph selected under its registered direct Relation types. unresolved selection **or** typing **must not** be reported as a conforming hierarchy.
- retain the distinction between declared direct authority edges **and** inverse-derived views under CA-R-808 **and** CA-R-879. an inverse view **must not** become another independently declared edge **in** the cycle check.

this representation-independent criterion does **not** select a graph-construction implementation **or** a concrete test specimen.
