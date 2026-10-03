---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - scope-topology
tier: core
version: 6
updated_at: 2026-08-29 01:16:37 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-231--forward-only-change-propagation
  child_of:
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
---
# Propagate CAPRMEDIO change forward

An accepted upstream change propagates **only** forward through the ordered layer graph. It:

1. identifies affected downstream Projections, Methods, Evaluation criteria, Delivery rules, Implementations, **and** Ops consumers;
2. marks **every** affected downstream artifact potentially stale **without** mutating historical atoms;
3. routes required reconciliation to the artifact's owning layer; **and**
4. closes **only** **when** **every** affected currentness **or** evaluation gate reaches its required disposition.

Refreshing a Projection alone does **not** complete propagation. Downstream Method, Evaluation, Delivery, Implementation, **and** Ops remain independently accountable. Feedback from a later layer **may** create a new upstream Concern, but cannot rewrite upstream authority **or** introduce a backward dependency.
