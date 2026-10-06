---
atom_id: CAPRMEDIO-META-REQU-096
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "scope-topology"
  depends_on: []
version: 13
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CA-M-001
---
# Propagate CAPRMEDIO change forward

An accepted upstream change propagates **only** forward through the ordered layer graph. It:

1. identifies affected downstream Projections, Methods, Evaluation criteria, Delivery rules, Implementations, **and** Operations consumers;
2. marks **every** affected downstream artifact potentially stale **without** mutating historical atoms;
3. routes required reconciliation to the artifact's owning layer; **and**
4. closes **only** **when** **every** affected currentness **or** evaluation gate reaches its required disposition.

Refreshing a Projection alone does **not** complete propagation. Downstream Method, Evaluation, Delivery, Implementation, **and** Operations remain independently accountable. Feedback from a later layer **may** create a new upstream Concern, but cannot rewrite upstream authority **or** introduce a backward dependency.
