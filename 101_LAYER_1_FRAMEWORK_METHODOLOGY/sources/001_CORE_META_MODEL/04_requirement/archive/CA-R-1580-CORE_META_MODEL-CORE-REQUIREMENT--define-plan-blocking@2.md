---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Blocking"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Plan Graph"
    - "Atom/Content Role: Plan/Type: Plan/Status: Done"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Hub Atom"
    - "Subject Relation Kind: DEPENDS_ON"
version: 2
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"relates_to": ["CA-R-1583", "CA-D-471", "CA-R-1200"]}
---
# Define Plan blocking

**in** the Plan Graph, `A BLOCKS B` **means** that Plan `B` **may** start **only** **after** Plan `A` is Done.

- a Plan **may** block **>=0** other Plans **and** have **>=0** blockers.
- **all** blockers **must** be Done **before** the blocked work starts.
- navigation order, a shared Hub, **and** `DECOMPOSES_INTO` do **not** establish `BLOCKS`.
- an inverse lookup is derived from the same explicit fact, **not** separately authored; Subject DEPENDS_ON remains a different Relation Kind.

## relation admission

- owning graph kind: Plan Graph under CA-R-1593; endpoints are Plan Atom references **in** that graph, **not** native nodes of a different graph.
- Status: the Relation Kind is Active; endpoint Plan Revisions use the admitted Plan Status model, **without** requiring every historical **or** pending endpoint **to** be Active.
- authority effect: retain the existing endpoint identities, Claims, Scope Units, **and** tiers; this Relation does **not** transfer authority.
- cardinality: **>=0** distinct direct targets **and** **>=0** distinct incoming blockers; inverse direction is blocked Plan **to** blocker.
- transitivity: retain **only** explicit direct edges; prerequisite reachability **may** be derived for readiness **and** cycle checks **without** creating authored transitive edges.
