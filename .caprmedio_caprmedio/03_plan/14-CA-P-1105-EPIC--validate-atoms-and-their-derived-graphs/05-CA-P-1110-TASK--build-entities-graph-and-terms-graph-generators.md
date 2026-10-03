---
atom_id: CA-P-1110
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 99
status: Active
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Projection"
  depends_on:
    - "Atom"
    - "Entity"
    - "Term"
    - "Graph"
    - "Relation"
    - "Subject"
    - "Tool"
    - "Evaluation"
    - "Single Source of Truth"
version: 1
updated_at: "2026-09-23 22:29:51 +0000"
relations:
  is_decomposition_of:
    - CA-P-1105
  blocks:
    - CA-P-1111
---
# Summary

Build Entities Graph and Terms Graph generators

## Claim

the AI Agent **must** deliver tested Tools that reproducibly derive distinct Entities Graph **and** Terms Graph Projections from the validated source Atom corpus **in** a supplied folder.

## Definition of Done

the Plan is **not** Done **if** either graph lacks a reproducible generator, **or** a node **or** edge lacks governed interpretation **and** source traceability, **or** graph kinds share unregistered Relation meanings, **or** the generators require filename-derived Atom Properties, **or** their positive **and** negative test cases do **not** pass.

## Details

- review the existing GENERATE_ENTITY_GRAPH implementation **and** reuse compatible readers **and** graph infrastructure; avoid duplicate authoritative dictionaries.
- derive graph nodes, admitted Relations, **and** constraints from the current methodology-backed declarations. keep Terms distinct from Entities **and** preserve each graph kind's Relation vocabulary.
- use explicit source Atom Properties **and** governed Claims; do **not** invent edges from capitalization, spelling similarity, folder nesting, **or** filename tokens.
- expose source-backed Atom incidence for Entity nodes: Atoms that GOVERNS **and** Atoms that DEPENDS_ON. these are views of declarations, **not** extra source authority.
- report missing definitions, unresolved targets, contradictory declarations, duplicate identities, invalid Relation directions/cardinalities, **and** prohibited cycles. do **not** prohibit admitted multiple parents **or** cycles belonging **to** another graph model.
- accept caller-supplied source folders **and** methodology context, including Core-only, combined methodology, **and** Project corpora; report excluded/incomplete inputs explicitly.
- test source traceability, graph-kind separation, deterministic results, malformed sources, undeclared Terms, qualified Entity paths, admitted multiple parents, forbidden cycles, **and** Atom incidence. graph outputs remain non-authoritative Projections.
- apply current source authority, including CA-R-1598 **and** CA-D-478–483; do **not** treat an outdated compiled copy as newer authority.
- check Project Principles **before** escalating uncertainty; ask the Operator **if** confidence remains **<99%**. do **not** silently weaken an Evaluation **or** discard a finding **to** pass.
- preserve unrelated work **and** history; follow the current revision, replacement, Summary identity, **and** approval rules.
