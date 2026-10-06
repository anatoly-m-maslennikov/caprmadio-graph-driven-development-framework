---
subject_scope: scope-topology
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-204--forward-change-propagation
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-203--acyclic-layer-dependencies
      - CAPRMEDIO-META-REQU-228--optional-thin-maintained-views
---

# Requirement — Propagate accepted change forward

An accepted upstream change propagates only forward through the ordered layer
graph. It:

1. identifies affected downstream maintained views, Methods, Implementations,
   Observations, and evaluation;
2. marks each affected downstream artifact potentially stale without mutating
   historical atoms;
3. routes required reconciliation to the artifact's owning layer; and
4. closes only when every affected currentness or evaluation gate reaches its
   required disposition.

Refreshing a maintained view alone does not complete propagation. Downstream
implementation and evaluation remain independently accountable. Feedback from
a later layer may create a new upstream Inquiry, but cannot rewrite upstream
authority or introduce a backward dependency.

## Primary claim

Accepted upstream change propagates potential staleness forward to every
affected owner without creating backward governance or treating one view
refresh as complete reconciliation.

## Rationale

The successor preserves the forward propagation invariant using the current
maintained-artifact vocabulary.
