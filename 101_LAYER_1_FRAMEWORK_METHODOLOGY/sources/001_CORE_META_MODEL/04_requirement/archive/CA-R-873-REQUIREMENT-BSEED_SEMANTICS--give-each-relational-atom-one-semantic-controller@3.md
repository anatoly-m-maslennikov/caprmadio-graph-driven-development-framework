---
subject_scopes:
  - relation-model
tier: core
version: 3
updated_at: 2026-08-22 01:51:09
relations:
  child_of:
    - CA-R-871-REQUIREMENT-BSEED_METAMODEL--distinguish-shared-authority-edges-and-relational-atoms
---
# Give each relational Atom one semantic controller

Every directional relational Atom is the one canonical semantic controller of the relationship meaning it declares. It identifies exactly one `controller` descriptor and one or more `follower` descriptors. Each descriptor identifies one exact Scope Unit and the Content role or roles to which the relationship applies. The controller Content role is the relational Atom's own Content role.

Provider, consumer, data source, obligation bearer, and Actor are independent positions and do not identify the controller unless the relational Atom explicitly assigns that meaning.
