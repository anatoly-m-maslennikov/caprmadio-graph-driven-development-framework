---
atom_id: CA-R-835
subject_scopes:
  - scope-topology
tier: core
version: 2
updated_at: 2026-08-21 02:55:24
relations:
  child_of:
    - CA-D-003-PRINCIPLE-DELIVERY--provide-one-project-graph-as-the-operating-model
---
# Scope Artifacts through Scope Units

Every Artifact belongs directly to exactly one Scope Unit and is included in the full scope of that Unit and every ancestor Scope Unit.

For any Scope Unit `u`:

`artifacts_in_full_scope(u) = own_artifacts(u) ∪ ⋃(own_artifacts(d) for d in descendants(u))`
