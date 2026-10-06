---
subject_scopes:
  - relation-model
version: 5
updated_at: 2026-08-22 01:56:15
relations:
  child_of:
    - CA-E-206-EVAL_APPROACH--require-usable-inputs-for-reliance
---
# Validate registered relation direction

GOVERNANCE validators must resolve the relation family, ordering domain, declared target position, and endpoint classes for every declared relation and validate the edge within that domain. Global tiers are compared only for authority relations whose metadata requires them; downstream declarations in another registered domain are not rejected merely because their target has a greater global tier. Validation fails closed when required relation metadata, endpoint state, or domain-specific position cannot be derived.
