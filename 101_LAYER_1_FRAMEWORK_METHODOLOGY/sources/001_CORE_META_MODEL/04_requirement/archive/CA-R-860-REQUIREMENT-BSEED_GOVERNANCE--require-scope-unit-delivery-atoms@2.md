---
subject_scopes:
  - scope-topology
version: 2
updated_at: 2026-08-21 16:19:30
relations:
  child_of:
    - CA-R-858
  replaced_by:
    - CA-R-862-REQUIREMENT-BSEED_GOVERNANCE--require-scope-unit-delivery-atoms
---
# Require Scope Unit Delivery Atoms

Every Scope Unit must carry one active Delivery Atom that binds its authority place to its Delivery place. Each path is expressed relative to the corresponding parent Scope Unit in the authority structure or Delivery structure, and the Atom names both parents when they differ. A root-level Unit states its root place directly. When an exact Delivery path is not yet decided, the Delivery Atom must state the known Delivery parent or boundary and mark the relative path `TBD` without inventing one.
