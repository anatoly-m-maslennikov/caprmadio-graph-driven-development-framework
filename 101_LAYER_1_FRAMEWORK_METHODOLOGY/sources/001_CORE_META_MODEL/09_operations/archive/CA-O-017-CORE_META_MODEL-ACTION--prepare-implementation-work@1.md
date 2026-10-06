---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Implementation Preparation"
  depends_on:
    - "Action"
    - "Spec"
    - "Atom"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Dependency Order Derivation"
version: 1
updated_at: "2026-09-15 17:55:09 +0400"
relations:
  child_of:
    - "CA-O-016"
  relates_to:
    - "CA-M-239"
    - "CA-M-266"
---
# Prepare implementation work

Implementation Preparation **means** the Action that resolves the current RMED, complete execution inputs, **and** selected implementation mode into applicable work, explicit prerequisites, **and** the next ready work item. derive prerequisite-first order under CA-M-239; include Evaluation-preparation precedence wherever actual prerequisites permit it **before** deriving that order. use Atom ID **only** **to** break remaining ties between ready work items, **not** **to** override a prerequisite **or** resolve an authority conflict.

unchanged mode, RMED, **and** complete execution inputs **must** yield the same applicable work **and** order. retain completed work **and** candidate-specific Evaluation results while selecting residual work; resolve affected work again **when** its inputs **or** governing baseline change. a prerequisite cycle, unresolved authority conflict, **or** incomplete work with no ready next item **must** remain a reported blocker, **not** successful completion.
