---
subject_scopes:
  - artifact-model
version: 1
updated_at: 2026-08-22 05:30:00
relations:
  child_of:
    - CA-D-003-PRINCIPLE-DELIVERY--provide-one-project-graph-as-the-operating-model
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
  replacement_of:
    - CA-R-880
---
# Define Demand For as a cross-scope Requirement Type

Every Demand For Atom is a Requirement Atom with Type `demand_for`.

Every Demand For Atom belongs to exactly one current Scope Unit.

Every Demand For Atom names exactly one distinct target Scope Unit.

Every Demand For Atom states exactly one required outcome for exactly one Delivery Atom in the target Scope Unit.

A Demand For Atom does not assert acceptance or mutual agreement.

The structural relationship between the current Scope Unit and the target Scope Unit does not change the meaning of Demand For.
