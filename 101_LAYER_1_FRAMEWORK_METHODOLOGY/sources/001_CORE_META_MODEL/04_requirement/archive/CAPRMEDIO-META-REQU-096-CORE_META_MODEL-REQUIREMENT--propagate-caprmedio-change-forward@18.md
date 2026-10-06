---
subjects:
  governs: "scope-topology"
  depends_on: []
version: 18
updated_at: 2026-09-15 05:51:38
relations:
  child_of:
    - CA-M-001
---
# Propagate CAPRMEDIO change forward

an accepted upstream change propagates **only** forward through the ordered layer graph. it:

1. identifies affected downstream Projections, Methods, Evaluation criteria, Delivery rules, Implementations, **and** Operations consumers;
2. marks **every** affected downstream artifact potentially stale **without** mutating historical atoms;
3. routes required reconciliation **to** the artifact's owning layer; **and**
4. closes **only** **when** **every** affected currentness **or** evaluation gate reaches its required disposition.

refreshing a Projection alone does **not** complete propagation. downstream Method, Evaluation, Delivery, Implementation, **and** Operations remain independently accountable. Feedback from a later layer **may** create a new upstream Concern, but cannot rewrite upstream authority **or** introduce a backward dependency.
