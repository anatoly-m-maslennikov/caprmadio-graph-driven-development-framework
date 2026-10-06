---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Decomposition"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Plan Graph"
    - "Atom/Content Role: Plan/Type: Plan/Label"
    - "Relation Kind"
    - "Atom/Content Role: Plan/Type: Plan/Status"
    - "Scope Unit"
    - "Atom/Claim"
version: 2
updated_at: "2026-09-22 23:02:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1574", "CA-R-1583", "CA-D-481"]}
---
# Summary

Define Plan decomposition Relations

## Claim

**in** the Plan Graph, `A DECOMPOSES_INTO B` **means** that completing Plan `B` contributes required work **to** completing Plan `A`; `B IS_DECOMPOSITION_OF A` is the inverse view of the same fact.

- the source **and** target are distinct Plan Atoms, independently of their Labels.
- decomposition is an all-of relation: **all** decomposed Plans are required for completion under CA-R-1583.
- decomposition concerns planned work, **not** Claim containment, Scope Unit parentage, **or** Type inheritance.
- the decomposing Plan owns the direct `IS_DECOMPOSITION_OF` declaration under CA-D-481; derive `DECOMPOSES_INTO` from that same fact, **not** from folder placement.

### relation admission

- owning graph kind: Plan Graph under CA-R-1593; endpoints are Plan Atom references **in** that graph, **not** native nodes of a different graph.
- Status: the Relation Kind is Active; endpoint Plan Revisions use the admitted Plan Status model, **without** requiring every historical **or** pending endpoint **to** be Active.
- authority effect: retain the existing endpoint identities, Claims, Scope Units, **and** tiers; this Relation does **not** transfer authority.
- cardinality: **`<=1`** authored `IS_DECOMPOSITION_OF` target **and** **`>=0`** derived `DECOMPOSES_INTO` targets per Plan.
- transitivity: the direct Relation is **not** transitively materialized; recursive reachability is derived under CA-R-1537.
